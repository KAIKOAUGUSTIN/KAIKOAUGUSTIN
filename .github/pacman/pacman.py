#!/usr/bin/env python3
"""Pac-Man na grade de contribuições do GitHub, como SVG animado.

O jogo inteiro é simulado antes, em tempo contínuo, e cada personagem vira um
<animateMotion> com a trajetória completa. Assim o movimento não anda aos
saltos, o Pac-Man olha para onde anda e as curvas são arredondadas.

- Pac-Man: come os quadrados verdes numa ordem planejada (caixeiro-viajante
  com 2-opt e or-opt) e anda pelo caminho com menos curvas. Desvia dos
  fantasmas e, depois de uma pílula de poder, caça os que estiverem ao alcance.
- Fantasmas: a regra do jogo original. A cada quadrado escolhem, sem dar meia
  volta, a saída mais perto do alvo de cada um (Blinky persegue, Pinky mira 4
  quadrados à frente, Inky usa o Blinky de referência e Clyde foge quando
  chega perto). Nunca chegam a menos de 2 quadrados do Pac-Man, então ninguém
  morre.

Uso:
  GITHUB_TOKEN=... python3 pacman.py --user KAIKOAUGUSTIN --out dist
  python3 pacman.py --data contribuicoes.json --out dist
"""

import argparse
import heapq
import json
import math
import os
import random
import urllib.request
from datetime import date

PITCH = 22          # quadrado de 20 px + 2 px de espaço
CELL = 20
TOP = 18            # faixa dos nomes dos meses
TICK = 0.15         # segundos para o Pac-Man andar um quadrado
READY = 1.2         # pausa antes de começar, em segundos
END = 2.5           # pausa no fim, antes de recomeçar
FRIGHT = 6.0        # duração do susto depois de uma pílula de poder
FLASH = 2.0         # parte final do susto, com os fantasmas piscando
CORNER = 7.0        # raio das curvas, em px
SUB = 16            # passos de simulação por quadrado andado
TURN = 0.35         # custo de virar, para o Pac-Man preferir retas
HUNT = 7            # distância máxima, em quadrados, para caçar um fantasma assustado
MAX_TICKS = 6000

DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]   # cima, esquerda, baixo, direita: o desempate do jogo original

THEMES = {
    "light": {"bg": "#ffffff", "text": "#57606a", "pac_stroke": "#c79a00",
              "levels": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]},
    "dark": {"bg": "#0d1117", "text": "#7d8590", "pac_stroke": None,
             "levels": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]},
}
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

# nome, cor, quando sai da casa (em quadrados andados pelo Pac-Man), velocidade
GHOSTS = [
    ("blinky", "#ff0000", 0, 0.88),
    ("pinky", "#ffb8ff", 8, 0.85),
    ("inky", "#00ffff", 20, 0.85),
    ("clyde", "#ffb852", 34, 0.85),
]
FRIGHT_SPEED = 0.55
EYES_SPEED = 2.2

QUERY = """query($login: String!) { user(login: $login) { contributionsCollection {
  contributionCalendar { weeks { contributionDays { date weekday contributionCount contributionLevel } } } } } }"""


def fetch(user, token):
    body = json.dumps({"query": QUERY, "variables": {"login": user}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": "bearer " + token, "Content-Type": "application/json", "User-Agent": "pacman-graph"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if data.get("errors"):
        raise SystemExit("GitHub: " + json.dumps(data["errors"]))
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [[{"date": d["date"], "weekday": d["weekday"], "count": d["contributionCount"],
              "level": LEVELS[d["contributionLevel"]]} for d in w["contributionDays"]] for w in weeks]


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclid(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


class Board:
    def __init__(self, weeks):
        self.weeks = weeks
        self.W = len(weeks)
        self.days = {(x, d["weekday"]): d for x, w in enumerate(weeks) for d in w}
        self.nbrs = {p: [((p[0] + dx, p[1] + dy), (dx, dy)) for dx, dy in DIRS if (p[0] + dx, p[1] + dy) in self.days]
                     for p in self.days}
        self.dist = {p: self._bfs(p) for p in self.days}

    def _bfs(self, src):
        dist = {src: 0}
        queue = [src]
        for p in queue:
            for q, _ in self.nbrs[p]:
                if q not in dist:
                    dist[q] = dist[p] + 1
                    queue.append(q)
        return dist

    def nearest(self, p):
        return min(self.days, key=lambda q: (manhattan(p, q), q))


def plan(board, start, targets):
    """Ordem dos quadrados a comer: vizinho mais próximo, melhorado com 2-opt e or-opt."""
    pts = [start] + sorted(targets)
    n = len(pts)
    if n == 1:
        return []
    cost = [[board.dist[a][b] + (TURN if a[0] != b[0] and a[1] != b[1] else 0.0) for b in pts] for a in pts]
    order = [0]
    left = set(range(1, n))
    while left:
        last = order[-1]
        j = min(left, key=lambda j: (cost[last][j], pts[j]))
        order.append(j)
        left.remove(j)

    def link(a, b):
        return cost[a][b] if b is not None else 0.0

    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                after = order[j + 1] if j + 1 < n else None
                old = cost[order[i - 1]][order[i]] + link(order[j], after)
                new = cost[order[i - 1]][order[j]] + link(order[i], after)
                if new < old - 1e-9:
                    order[i:j + 1] = order[i:j + 1][::-1]
                    improved = True
        for size in (1, 2, 3):
            i = 1
            while i + size <= n:
                seg = order[i:i + size]
                after = order[i + size] if i + size < n else None
                gain = cost[order[i - 1]][seg[0]] + link(seg[-1], after) - link(order[i - 1], after)
                rest = order[:i] + order[i + size:]
                best = None
                for k in range(1, len(rest) + 1):
                    if k == i:
                        continue
                    nxt = rest[k] if k < len(rest) else None
                    for piece in (seg, seg[::-1]):
                        add = cost[rest[k - 1]][piece[0]] + link(piece[-1], nxt) - link(rest[k - 1], nxt)
                        if add < gain - 1e-9 and (best is None or add < best[0]):
                            best = (add, k, piece)
                if best:
                    _, k, piece = best
                    order = rest[:k] + piece + rest[k:]
                    improved = True
                i += 1
    return [pts[k] for k in order[1:]]


def first_step(board, src, sdir, goal, blocked, danger):
    """Primeiro passo do caminho mais barato até goal, contando curvas e perigo."""
    if src == goal:
        return None
    seq = 0
    heap = [(0.0, 0, src, sdir, None)]
    best = {(src, sdir): 0.0}
    while heap:
        cost, _, p, d, first = heapq.heappop(heap)
        if p == goal:
            return first
        if cost > best.get((p, d), math.inf) + 1e-12:
            continue
        for q, nd in board.nbrs[p]:
            if first is None and q in blocked:
                continue
            step = 1.0 + danger.get(q, 0.0)
            if nd != d:
                step += 1.0 if (nd[0] == -d[0] and nd[1] == -d[1]) else TURN
            nc = cost + step
            if nc < best.get((q, nd), math.inf) - 1e-12:
                best[(q, nd)] = nc
                seq += 1
                heapq.heappush(heap, (nc, seq, q, nd, first or (q, nd)))
    return None


class Actor:
    def __init__(self, tile, speed, facing):
        self.tile = tile
        self.nxt = None
        self.prog = 0.0
        self.dir = facing
        self.speed = speed
        self.track = [(0.0, tile)]     # (tempo, posição): pontos por onde passa
        self.dirs = [(0.0, facing)]    # (tempo, direção), para os olhos dos fantasmas

    def pos(self):
        if self.nxt is None:
            return self.tile
        return (round(self.tile[0] + (self.nxt[0] - self.tile[0]) * self.prog, 6),
                round(self.tile[1] + (self.nxt[1] - self.tile[1]) * self.prog, 6))

    def near(self):
        return self.nxt if self.nxt is not None and self.prog > 0.5 else self.tile

    def mark(self, t):
        p = self.pos()
        lt, lp = self.track[-1]
        if not (abs(t - lt) < 1e-9 and lp == p):
            self.track.append((t, p))

    def turn(self, t, d):
        if d != self.dir:
            self.dir = d
            self.dirs.append((t, d))

    def advance(self, t0, dt, decide, arrive):
        left = dt
        while left > 1e-12:
            now = t0 + dt - left
            if self.nxt is None:
                nxt = decide(self, now)
                if nxt is None:
                    return
                self.mark(now)
                self.nxt = nxt
                self.turn(now, (nxt[0] - self.tile[0], nxt[1] - self.tile[1]))
            need = (1.0 - self.prog) / self.speed
            if need <= left:
                left -= need
                self.tile, self.nxt, self.prog = self.nxt, None, 0.0
                now = t0 + dt - left
                self.mark(now)
                arrive(self, now)
            else:
                self.prog += self.speed * left
                left = 0.0

    def reverse(self, t):
        self.mark(t)
        if self.nxt is not None:
            self.tile, self.nxt, self.prog = self.nxt, self.tile, 1.0 - self.prog
        self.turn(t, (-self.dir[0], -self.dir[1]))


class Ghost(Actor):
    def __init__(self, name, color, release, speed, home):
        super().__init__(home, speed, (-1, 0))
        self.name, self.color, self.release, self.base = name, color, release, speed
        self.home = home
        self.state = "house"
        self.look = [(0.0, "normal")]   # normal, fright, flash ou eyes

    def show(self, t, look):
        if self.look[-1][1] != look:
            self.look.append((t, look))


def pick_power(board, pellets, n=4, gap=8):
    """As pílulas de poder são os dias mais fortes, com pelo menos `gap` semanas entre elas.

    Ficam a partir de um terço do ano, onde o Pac-Man já encontrou os fantasmas.
    """
    if len(pellets) < 12:
        return set()
    d = board.days
    power = []
    for p in sorted(pellets, key=lambda p: (-d[p]["level"], -d[p]["count"], p)):
        if p[0] >= board.W / 3 and all(abs(p[0] - q[0]) >= gap for q in power):
            power.append(p)
            if len(power) == n:
                break
    return set(power)


class Game:
    def __init__(self, board, seed=1):
        self.board = board
        self.rng = random.Random(seed)
        self.pellets = {p for p, d in board.days.items() if d["level"] > 0}
        self.power = pick_power(board, self.pellets)
        start = board.nearest((0, 3))
        self.pac = Actor(start, 1.0, (1, 0))
        homes = sorted(board.days, key=lambda p: (manhattan(p, (board.W - 2, 3)), p[1], -p[0]))[:4]
        self.ghosts = [Ghost(n, c, r, s, h) for (n, c, r, s), h in zip(GHOSTS, homes)]
        self.order = plan(board, start, self.pellets)
        self.replan = False
        self.eaten = {}
        self.popups = []
        self.fright_until = -1.0
        self.combo = 0
        self.collisions = 0
        self.done = None
        self.t = 0.0

    # ---- Pac-Man

    def threats(self):
        blocked, danger = set(), {}
        for g in self.ghosts:
            if g.state not in ("house", "chase"):
                continue
            for c in {g.tile, g.nxt} - {None}:
                blocked.add(c)
                danger[c] = danger.get(c, 0.0) + 8.0
                for q, _ in self.board.nbrs[c]:
                    danger[q] = danger.get(q, 0.0) + 2.5
        return blocked, danger

    def pac_decide(self, pac, now):
        if not self.pellets:
            return None
        target = None
        if now < self.fright_until:
            # só caça perto, para não largar a região que está comendo
            reach = min((self.fright_until - now) * (1.0 - FRIGHT_SPEED) * 0.9, HUNT)
            prey = [(self.board.dist[pac.tile][g.near()], g.near()) for g in self.ghosts if g.state == "fright"]
            prey = [p for p in prey if p[0] <= reach]
            if prey:
                target = min(prey)[1]
                self.replan = True
        if target is None:
            if self.replan or not any(p in self.pellets for p in self.order):
                self.order = plan(self.board, pac.tile, self.pellets)
                self.replan = False
            while self.order[0] not in self.pellets:
                self.order.pop(0)
            target = self.order[0]
        if target == pac.tile:
            return None
        blocked, danger = self.threats()
        step = first_step(self.board, pac.tile, pac.dir, target, blocked, danger)
        return step[0] if step else None

    def pac_arrive(self, pac, now):
        if pac.tile in self.pellets:
            self.eat(pac.tile, now)
        if not self.pellets and self.done is None:
            self.done = now

    def eat(self, p, now):
        self.pellets.discard(p)
        self.eaten[p] = now
        if p in self.power:
            self.fright_until = now + FRIGHT / TICK
            self.combo = 0
            for g in self.ghosts:
                if g.state == "chase":
                    g.reverse(now)
                if g.state in ("chase", "fright"):
                    g.state = "fright"
                    g.show(now, "fright")

    # ---- fantasmas

    def target(self, g):
        p, d = self.pac.near(), self.pac.dir
        if g.name == "pinky":
            return (p[0] + 4 * d[0], p[1] + 4 * d[1])
        if g.name == "inky":
            b = next(x for x in self.ghosts if x.name == "blinky").pos()
            v = (p[0] + 2 * d[0], p[1] + 2 * d[1])
            return (2 * v[0] - b[0], 2 * v[1] - b[1])
        if g.name == "clyde" and euclid(g.tile, p) <= 8:
            return (0, 6)
        return p

    def safe(self, q):
        pac = self.pac
        return manhattan(q, pac.tile) >= 2 and (pac.nxt is None or manhattan(q, pac.nxt) >= 2)

    def ghost_decide(self, g, now):
        nbrs = self.board.nbrs[g.tile]
        if g.state == "house":
            if now < g.release:
                return None
            g.state = "chase"
        if g.state == "eyes":
            if g.tile != g.home:
                home = self.board.dist[g.home]
                return min(nbrs, key=lambda o: home[o[0]])[0]
            if not (self.safe(g.home) and manhattan(g.home, self.pac.tile) >= 3):
                return None
            g.state = "chase"
            g.show(now, "normal")
        back = (-g.dir[0], -g.dir[1])
        ahead = [o for o in nbrs if o[1] != back] or nbrs
        if g.state == "fright":
            pac = self.pac.pos()
            return max(ahead, key=lambda o: euclid(o[0], pac) + self.rng.random() * 2.0)[0]
        aim = self.target(g)
        options = [o for o in ahead if self.safe(o[0])] or [o for o in nbrs if self.safe(o[0])]
        if not options:
            return None
        return min(options, key=lambda o: euclid(o[0], aim))[0]

    def ghost_arrive(self, g, now):
        pass

    def speed(self, g):
        return {"fright": FRIGHT_SPEED, "eyes": EYES_SPEED}.get(g.state, g.base)

    # ---- laço principal

    def update(self, t):
        for g in self.ghosts:
            if g.state != "fright":
                continue
            if t >= self.fright_until and euclid(g.pos(), self.pac.pos()) >= 2.5:
                g.state = "chase"
                g.show(t, "normal")
            elif t >= self.fright_until - FLASH / TICK:
                g.show(t, "flash")

    def collide(self, t):
        for g in self.ghosts:
            if euclid(g.pos(), self.pac.pos()) >= 0.7:
                continue
            if g.state == "fright":
                g.state = "eyes"
                g.show(t, "eyes")
                self.popups.append((t, self.pac.pos(), 200 * 2 ** self.combo))
                self.combo += 1
            elif g.state in ("house", "chase"):
                self.collisions += 1

    def run(self):
        dt = 1.0 / SUB
        if self.pac.tile in self.pellets:
            self.eat(self.pac.tile, 0.0)
        if not self.pellets:
            self.done = 0.0
        while self.done is None and self.t < MAX_TICKS:
            self.update(self.t)
            self.pac.advance(self.t, dt, self.pac_decide, self.pac_arrive)
            if self.done is None:
                for g in self.ghosts:
                    g.speed = self.speed(g)
                    g.advance(self.t, dt, self.ghost_decide, self.ghost_arrive)
                self.collide(self.t + dt)
            self.t += dt
        if self.done is None:
            self.done = self.t
        self.t = self.done
        for a in [self.pac] + self.ghosts:
            a.track = [(t, p) for t, p in a.track if t <= self.done + 1e-9]
            a.dirs = [(t, d) for t, d in a.dirs if t <= self.done + 1e-9]
            a.track.append((self.done, a.pos()))
        return self


# ---- SVG

def px(p):
    return (p[0] * PITCH + CELL / 2, TOP + p[1] * PITCH + CELL / 2)


def num(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def rounded_path(points):
    """Caminho com curvas de raio CORNER e a posição (comprimento) de cada ponto."""
    n = len(points)
    unit, seg = [], []
    for a, b in zip(points, points[1:]):
        length = math.hypot(b[0] - a[0], b[1] - a[1])
        seg.append(length)
        unit.append(((b[0] - a[0]) / length, (b[1] - a[1]) / length))
    r = [0.0] * n
    for i in range(1, n - 1):
        u, v = unit[i - 1], unit[i]
        if abs(u[0] * v[0] + u[1] * v[1]) < 1e-9:
            r[i] = min(CORNER, seg[i - 1] / 2, seg[i] / 2)
    cmds = [f"M{num(points[0][0])} {num(points[0][1])}"]
    at = [0.0] * n
    end = 0.0
    for i in range(1, n):
        start = end + seg[i - 1] - r[i - 1] - r[i]
        x, y = points[i]
        u = unit[i - 1]
        if r[i] > 0:
            v = unit[i]
            sweep = 1 if u[0] * v[1] - u[1] * v[0] > 0 else 0
            cmds.append(f"L{num(x - u[0] * r[i])} {num(y - u[1] * r[i])}"
                        f"A{num(r[i])} {num(r[i])} 0 0 {sweep} {num(x + v[0] * r[i])} {num(y + v[1] * r[i])}")
            at[i] = start + r[i] * math.pi / 4
            end = start + r[i] * math.pi / 2
        else:
            straight = i < n - 1 and unit[i] == u
            if not straight:
                cmds.append(f"L{num(x)} {num(y)}")
            at[i] = end = start
    return "".join(cmds), at, end


class Clock:
    def __init__(self, ticks):
        self.D = READY + ticks * TICK + END

    def sec(self, t):
        return READY + t * TICK

    def key(self, s):
        return f"{min(max(s / self.D, 0.0), 1.0):.5f}".rstrip("0").rstrip(".") or "0"


def motion(actor, clock, rotate=False):
    pts = [px(p) for _, p in actor.track]
    geo, index = [pts[0]], []
    for p in pts:
        if math.hypot(p[0] - geo[-1][0], p[1] - geo[-1][1]) > 1e-6:
            geo.append(p)
        index.append(len(geo) - 1)
    x0, y0 = geo[0]
    if len(geo) == 1:
        return f'transform="translate({num(x0)} {num(y0)})"', ""
    path, at, total = rounded_path(geo)
    times = ["0"] + [clock.key(clock.sec(t)) for t, _ in actor.track] + ["1"]
    points = ["0"] + [f"{at[i] / total:.5f}" for i in index] + [f"{at[index[-1]] / total:.5f}"]
    rot = ' rotate="auto"' if rotate else ""
    return "", (f'<animateMotion dur="{clock.D:.3f}s" repeatCount="indefinite" calcMode="linear"{rot} '
                f'keyTimes="{";".join(times)}" keyPoints="{";".join(points)}" path="{path}"/>')


def discrete(attr, changes, clock, kind="animate", extra=""):
    """Animação discreta a partir de [(segundos, valor)]. Devolve (valor inicial, tag)."""
    values, keys = [], []
    for s, v in changes:
        k = clock.key(s)
        if values and values[-1] == v:
            continue
        if keys and float(k) <= float(keys[-1]):
            values[-1] = v
            continue
        values.append(v)
        keys.append(k if keys else "0")
    if len(values) == 1:
        return values[0], ""
    if keys[-1] != "1":
        values.append(values[-1])
        keys.append("1")
    return values[0], (f'<{kind} attributeName="{attr}"{extra} dur="{clock.D:.3f}s" repeatCount="indefinite" '
                       f'calcMode="discrete" values="{";".join(values)}" keyTimes="{";".join(keys)}"/>')


def pacman_d(angle):
    c, s = 9 * math.cos(angle), 9 * math.sin(angle)
    return f"M0 0L{num(c)} {num(s)}A9 9 0 1 1 {num(c)} {num(-s)}Z"


GHOST_A = "M-9 9L-9 0A9 9 0 0 1 9 0L9 9L6 6L3 9L0 6L-3 9L-6 6Z"
GHOST_B = "M-9 7L-9 0A9 9 0 0 1 9 0L9 7L7.5 9L4.5 6L1.5 9L-1.5 6L-4.5 9L-7.5 6Z"


def ghost_svg(g, game, clock):
    attr, anim = motion(g, clock)
    fade = clock.sec(game.done) + 0.6
    looks = []
    for i, (t, look) in enumerate(g.look):
        stop = g.look[i + 1][0] if i + 1 < len(g.look) else game.done
        if look == "flash":
            s = clock.sec(t)
            on = True
            while s < clock.sec(stop):
                looks.append((s, "flash-on" if on else "fright"))
                s += 0.2
                on = not on
        else:
            looks.append((clock.sec(t), look))
    looks = [(s, v) for s, v in looks if s < fade]
    body = {"normal": g.color, "fright": "#2121ff", "flash-on": "#ffffff", "eyes": g.color}
    face = {"fright": "#ffb8ae", "flash-on": "#ff0000"}
    fill0, fill = discrete("fill", [(s, body[v]) for s, v in looks], clock)
    bodyop0, bodyop = discrete("opacity", [(s, "0" if v == "eyes" else "1") for s, v in looks], clock)
    eyes0, eyes = discrete("opacity", [(s, "1" if v in ("normal", "eyes") else "0") for s, v in looks], clock)
    scared0, scared = discrete("opacity", [(s, "0" if v in ("normal", "eyes") else "1") for s, v in looks], clock)
    mouth0, mouth = discrete("stroke", [(s, face.get(v, "#ffb8ae")) for s, v in looks], clock)
    look0, look = discrete("transform", [(clock.sec(t), f"{num(d[0] * 1.4)} {num(d[1] * 1.4)}") for t, d in g.dirs],
                           clock, "animateTransform", ' type="translate"')
    gone0, gone = discrete("opacity", [(0.0, "1"), (fade, "0")], clock)
    return (f'<g {attr}>{anim}<g opacity="{gone0}">{gone}'
            f'<path d="{GHOST_A}" fill="{fill0}" opacity="{bodyop0}">'
            f'<animate attributeName="d" dur="0.3s" repeatCount="indefinite" calcMode="discrete" values="{GHOST_A};{GHOST_B}"/>'
            f'{fill}{bodyop}</path>'
            f'<g opacity="{eyes0}">{eyes}<ellipse cx="-3.5" cy="-1.5" rx="2.8" ry="3.4" fill="#fff"/>'
            f'<ellipse cx="3.5" cy="-1.5" rx="2.8" ry="3.4" fill="#fff"/>'
            f'<g transform="translate({look0})">{look}<circle cx="-3.5" cy="-1.5" r="1.6" fill="#1f3fff"/>'
            f'<circle cx="3.5" cy="-1.5" r="1.6" fill="#1f3fff"/></g></g>'
            f'<g opacity="{scared0}">{scared}<g fill="#ffb8ae"><rect x="-4.6" y="-3.6" width="2.4" height="2.4"/>'
            f'<rect x="2.2" y="-3.6" width="2.4" height="2.4"/></g>'
            f'<path d="M-6 4.5L-4.5 3L-3 4.5L-1.5 3L0 4.5L1.5 3L3 4.5L4.5 3L6 4.5" fill="none" stroke="{mouth0}" '
            f'stroke-width="1.2">{mouth}</path></g></g></g>')


def render(game, theme):
    board, th = game.board, THEMES[theme]
    clock = Clock(game.done)
    width = board.W * PITCH - 2
    height = TOP + 7 * PITCH + 2
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           f'<rect width="100%" height="100%" fill="{th["bg"]}"/>']

    labels, last = [], None
    for x, week in enumerate(board.weeks):
        if not week:
            continue
        month = date.fromisoformat(week[0]["date"]).month
        if month != last:
            labels.append((x, MONTHS[month - 1]))
            last = month
    if len(labels) > 1 and labels[1][0] - labels[0][0] < 3:
        labels.pop(0)
    for x, name in labels:
        out.append(f'<text x="{x * PITCH}" y="11" font-size="10" fill="{th["text"]}" '
                   f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">{name}</text>')

    empty = th["levels"][0]
    for (x, y), d in sorted(board.days.items()):
        color = th["levels"][d["level"]]
        rect = f'<rect x="{x * PITCH}" y="{TOP + y * PITCH}" width="{CELL}" height="{CELL}" rx="4" fill="{color}"'
        anims = ""
        if (x, y) in game.eaten:
            gone = clock.sec(max(game.eaten[(x, y)] - 0.3, 0.0))
            anims += discrete("fill", [(0.0, color), (gone, empty)], clock)[1]
            if (x, y) in game.power:
                blink, s, on = [], 0.0, True
                while s < gone:
                    blink.append((s, "1" if on else "0.35"))
                    s += 0.3
                    on = not on
                blink.append((gone, "1"))
                anims += discrete("opacity", blink, clock)[1]
        out.append(f"{rect}>{anims}</rect>" if anims else rect + "/>")

    attr, anim = motion(game.pac, clock, rotate=True)
    stroke = f' stroke="{th["pac_stroke"]}" stroke-width="0.8"' if th["pac_stroke"] else ""
    chomp = ";".join(pacman_d(a) for a in (0.75, 0.05, 0.75))
    out.append(f'<g {attr}>{anim}<path d="{pacman_d(0.75)}" fill="#ffcc00"{stroke}>'
               f'<animate attributeName="d" dur="0.24s" repeatCount="indefinite" values="{chomp}"/></path></g>')

    for g in game.ghosts:
        out.append(ghost_svg(g, game, clock))

    for t, p, points in game.popups:
        x, y = px(p)
        s = clock.sec(t)
        _, show = discrete("opacity", [(0.0, "0"), (s, "1"), (s + 0.9, "0")], clock)
        out.append(f'<text x="{num(x)}" y="{num(y + 3)}" text-anchor="middle" font-size="9" font-weight="bold" '
                   f'font-family="monospace" fill="#00e5ff" opacity="0">{points}{show}</text>')
    out.append("</svg>")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--user", help="usuário do GitHub (precisa de GITHUB_TOKEN)")
    ap.add_argument("--data", help="JSON com as semanas, no lugar de buscar no GitHub")
    ap.add_argument("--out", default="dist")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    if args.data:
        with open(args.data) as f:
            weeks = json.load(f)
    elif args.user:
        weeks = fetch(args.user, os.environ["GITHUB_TOKEN"])
    else:
        ap.error("informe --user ou --data")

    game = Game(Board(weeks), args.seed).run()
    os.makedirs(args.out, exist_ok=True)
    for theme, name in (("light", "pacman-contribution-graph.svg"), ("dark", "pacman-contribution-graph-dark.svg")):
        with open(os.path.join(args.out, name), "w") as f:
            f.write(render(game, theme))
    print(f"{len(game.eaten)} quadrados comidos, {len(game.power)} pílulas de poder, "
          f"{len(game.popups)} fantasmas comidos, {READY + game.done * TICK + END:.1f} s, "
          f"{len(game.pellets)} sobraram, {game.collisions} encostadas")


if __name__ == "__main__":
    main()
