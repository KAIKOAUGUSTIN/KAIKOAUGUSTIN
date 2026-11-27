#!/usr/bin/env python3
"""Pac-Man na grade de contribuições do GitHub, como SVG animado.

O jogo inteiro é simulado antes, em tempo contínuo, e cada personagem vira um
<animateMotion> com a trajetória completa. Assim o movimento não anda aos
saltos, o Pac-Man olha para onde anda e as curvas são arredondadas.

- Labirinto: paredes azuis nos vãos entre os quadrados, espelhadas da esquerda
  para a direita como no jogo original. Todo quadrado continua alcançável e
  nenhum fica com menos de duas saídas, então não há beco sem saída.
- Pac-Man: come os quadrados verdes numa ordem planejada (caixeiro-viajante
  com 2-opt e or-opt) e anda pelo caminho com menos curvas, evitando os
  quadrados aonde um fantasma chegaria antes dele. Depois de uma pílula de
  poder, caça os fantasmas assustados que estiverem ao alcance.
- Fantasmas: a regra do jogo original. A cada quadrado escolhem, sem dar meia
  volta, a saída mais perto do alvo de cada um (Blinky persegue, Pinky mira 4
  quadrados à frente, Inky usa o Blinky de referência e Clyde foge quando
  chega perto), alternando perseguição com dispersão, quando cada um vai para
  o seu canto.
- Morte: o fantasma que encosta no Pac-Man mata. Tudo para, ele some com a
  animação do jogo original e todos voltam para o começo; o que já foi comido
  continua comido. São 3 vidas; quando acabam, aparece GAME OVER e a animação
  recomeça.

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
ROWS = 7
TOP = 18            # faixa dos nomes dos meses
TICK = 0.15         # segundos para o Pac-Man andar um quadrado
READY = 1.2         # pausa antes de começar (e depois de cada morte), em segundos
END = 2.5           # pausa no fim, antes de recomeçar
OVER = 3.5          # pausa no fim quando dá GAME OVER
FRIGHT = 6.0        # duração do susto depois de uma pílula de poder
FLASH = 2.0         # parte final do susto, com os fantasmas piscando
CORNER = 7.0        # raio das curvas, em px
SUB = 16            # passos de simulação por quadrado andado
TURN = 0.35         # custo de virar, para o Pac-Man preferir retas
HUNT = 7            # distância máxima, em quadrados, para caçar um fantasma assustado
MAX_TICKS = 6000

LIVES = 3           # vidas do Pac-Man
DEATH_FREEZE = 1.0  # segundos com tudo parado depois que um fantasma pega o Pac-Man
DEATH_ANIM = 1.5    # animação da morte
DEATH_FRAMES = 11
DEATH_GAP = 0.4     # tela sem personagens antes de todos voltarem ao começo
SAFE = 1.0          # folga, em quadrados: onde um fantasma chega antes disso, o Pac-Man não passa
WARY = 4.0          # até essa folga ele ainda prefere passar longe
LETHAL = 40.0       # custo de passar por um quadrado onde um fantasma chega antes
# segundos alternando dispersão e perseguição (como na fase 1 do original); depois, só perseguição
MODES = [7, 20, 7, 20, 5, 20, 5]

WALLS = 0.2         # fração das ligações entre quadrados que viram parede
WALL_TRIES = 8000
WALL_WIDTH = 3
# peças de parede: linhas entre cantos de quadrados, viradas e giradas ao acaso
SHAPES = [
    [[(0, 0), (1, 0)]],
    [[(0, 0), (2, 0)]],
    [[(0, 0), (3, 0)]],
    [[(0, 0), (4, 0)]],
    [[(0, 0), (0, 2)]],
    [[(0, 1), (0, 0), (2, 0)]],
    [[(0, 1), (0, 0), (3, 0)]],
    [[(0, 0), (2, 0)], [(1, 0), (1, 1)]],
    [[(0, 0), (4, 0)], [(2, 0), (2, 1)]],
    [[(0, 0), (2, 0)], [(1, -1), (1, 1)]],
    [[(0, 1), (0, 0), (3, 0), (3, 1)]],
]
TRANSFORMS = [(1, 0, 0, 1), (0, -1, 1, 0), (-1, 0, 0, -1), (0, 1, -1, 0),
              (-1, 0, 0, 1), (1, 0, 0, -1), (0, 1, 1, 0), (0, -1, -1, 0)]

DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]   # cima, esquerda, baixo, direita: o desempate do jogo original

THEMES = {
    "light": {"bg": "#ffffff", "text": "#57606a", "pac_stroke": "#c79a00", "wall": "#2121de",
              "levels": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]},
    "dark": {"bg": "#0d1117", "text": "#7d8590", "pac_stroke": None, "wall": "#2b2bff",
             "levels": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]},
}
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

# nome, cor, quando sai da casa (em quadrados andados pelo Pac-Man), velocidade
GHOSTS = [
    ("blinky", "#ff0000", 0, 0.93),
    ("pinky", "#ffb8ff", 8, 0.9),
    ("inky", "#00ffff", 20, 0.9),
    ("clyde", "#ffb852", 34, 0.9),
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


# ---- labirinto

def sides(seg):
    """Os dois quadrados que uma parede separa. Os cantos (i, j) ficam entre os quadrados."""
    (i, j), (k, l) = sorted(seg)
    if j == l:                          # parede deitada: separa o quadrado de cima do de baixo
        return (i, j - 1), (i, j)
    return (i - 1, j), (i, j)           # parede em pé: separa o da esquerda do da direita


def maze(W, rng):
    """Paredes nos vãos entre os quadrados, espelhadas da esquerda para a direita.

    Cada peça é uma árvore de segmentos que não encosta nas outras nem na borda,
    então o tabuleiro continua todo ligado, e nenhum quadrado fica com menos de
    duas saídas. As peças não chegam na primeira nem na última semana, que podem
    estar pela metade, e por isso o labirinto não muda de um dia para o outro.
    """
    cells = {(x, y) for x in range(W) for y in range(ROWS)}
    deg = {c: sum((c[0] + dx, c[1] + dy) in cells for dx, dy in DIRS) for c in cells}
    corners = [(i, j) for i in range(2, W - 1) for j in range(1, ROWS)]
    allowed = set(corners)
    goal = WALLS * sum(deg.values()) / 2
    used, walls = set(), set()
    for _ in range(WALL_TRIES):
        if len(walls) >= goal:
            break
        shape = rng.choice(SHAPES)
        a, b, c, d = rng.choice(TRANSFORMS)
        ax, ay = rng.choice(corners)
        segs = set()
        for line in shape:
            pts = [(ax + a * x + b * y, ay + c * x + d * y) for x, y in line]
            for p, q in zip(pts, pts[1:]):
                n = max(abs(q[0] - p[0]), abs(q[1] - p[1]))
                sx, sy = (q[0] - p[0]) // n, (q[1] - p[1]) // n
                for k in range(n):
                    u = (p[0] + sx * k, p[1] + sy * k)
                    segs.add(tuple(sorted((u, (u[0] + sx, u[1] + sy)))))
        segs |= {tuple(sorted(((W - u[0], u[1]), (W - v[0], v[1])))) for u, v in segs}
        pts = {p for s in segs for p in s}
        if not pts <= allowed or pts & used:
            continue
        root = {p: p for p in pts}

        def find(p):
            while root[p] != p:
                p = root[p]
            return p
        tree = True
        for u, v in segs:
            ru, rv = find(u), find(v)
            if ru == rv:
                tree = False
                break
            root[ru] = rv
        if not tree:
            continue
        lose = {}
        for s in segs:
            for cell in sides(s):
                lose[cell] = lose.get(cell, 0) + 1
        if any(deg[cell] - n < 2 for cell, n in lose.items()):
            continue
        for cell, n in lose.items():
            deg[cell] -= n
        used |= pts
        walls |= segs
    return sorted(walls)


class Board:
    def __init__(self, weeks, walls=()):
        self.weeks = weeks
        self.W = len(weeks)
        self.days = {(x, d["weekday"]): d for x, w in enumerate(weeks) for d in w}
        self.walls = [s for s in walls if all(c in self.days for c in sides(s))]
        cut = {frozenset(sides(s)) for s in self.walls}
        self.nbrs = {}
        for p in self.days:
            self.nbrs[p] = []
            for dx, dy in DIRS:
                q = (p[0] + dx, p[1] + dy)
                if q in self.days and frozenset((p, q)) not in cut:
                    self.nbrs[p].append((q, (dx, dy)))
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


def route(board, src, sdir, peril, goal=None):
    """Caminhos mais baratos a partir de src, contando curvas e perigo.

    peril[q] é o primeiro instante (em quadrados andados a partir de agora) em
    que um fantasma pode estar em q. Devolve, para cada quadrado alcançado,
    (custo, primeiro passo, se passa onde um fantasma chega antes). Com goal,
    para assim que chega nele.
    """
    out = {}
    seq = 0
    heap = [(0.0, 0, src, sdir, 0, None, False)]
    best = {(src, sdir): 0.0}
    while heap:
        cost, _, p, d, steps, first, hit = heapq.heappop(heap)
        if cost > best.get((p, d), math.inf) + 1e-12:
            continue
        if p not in out:
            out[p] = (cost, first, hit)
            if p == goal:
                break
        for q, nd in board.nbrs[p]:
            step = 1.0
            if nd != d:
                step += 1.0 if (nd[0] == -d[0] and nd[1] == -d[1]) else TURN
            slack = peril.get(q, math.inf) - (steps + 1)
            danger = hit
            if slack <= SAFE:
                step += LETHAL
                danger = True
            elif slack <= WARY:
                step += 2.0
            nc = cost + step
            if nc < best.get((q, nd), math.inf) - 1e-12:
                best[(q, nd)] = nc
                seq += 1
                heapq.heappush(heap, (nc, seq, q, nd, steps + 1, first or (q, nd), danger))
    return out


class Actor:
    def __init__(self, tile, speed, facing):
        self.speed = speed
        self.dir = facing
        self.dirs = [(0.0, facing)]    # (tempo, direção), para os olhos dos fantasmas
        self.parts = []                # trechos terminados: (começo, fim, trilha)
        self.place(tile, facing, 0.0)

    def place(self, tile, facing, t):
        """Põe o personagem em tile no instante t, começando um trecho novo."""
        self.tile, self.nxt, self.prog = tile, None, 0.0
        self.turn(t, facing)
        self.since = t
        self.track = [(t, tile)]       # (tempo, posição): pontos por onde passa

    def cut(self, t):
        """Termina o trecho atual: o personagem some em t."""
        self.mark(t)
        self.parts.append((self.since, t, self.track))
        self.track = None

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
        self.state = "house"            # house, chase (perseguição ou dispersão), fright ou eyes
        self.free_at = release
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
        self.start = board.nearest((0, 3))
        self.pac = Actor(self.start, 1.0, (1, 0))
        homes = sorted(board.days, key=lambda p: (manhattan(p, (board.W - 2, 3)), p[1], -p[0]))[:4]
        self.ghosts = [Ghost(n, c, r, s, h) for (n, c, r, s), h in zip(GHOSTS, homes)]
        W = board.W
        self.corners = {"blinky": (W + 2, -4), "pinky": (-3, -4), "inky": (W + 2, ROWS + 3), "clyde": (-3, ROWS + 3)}
        self.order = plan(board, self.start, self.pellets)
        self.replan = False
        self.eaten = {}
        self.popups = []
        self.fright_until = -1.0
        self.combo = 0
        self.mode = "scatter"
        self.mode_clock = 0.0
        self.lives = LIVES
        self.deaths = []         # (tempo, posição, direção)
        self.respawns = []       # (volta ao começo, recomeça a andar)
        self.resume = 0.0
        self.over = None         # quando aparece GAME OVER
        self.done = None
        self.t = 0.0

    # ---- Pac-Man

    def peril(self, now):
        """Para cada quadrado, o primeiro instante (a partir de agora) em que um fantasma pode matar ali."""
        soon = {}
        wait = max(self.fright_until - now, 0.0)
        for g in self.ghosts:
            if g.state == "eyes":
                continue
            src, extra = (g.tile, 0.0) if g.nxt is None else (g.nxt, 1.0 - g.prog)
            delay = max(g.free_at - now, 0.0) if g.state == "house" else 0.0
            for q, k in self.board.dist[src].items():
                k += extra
                if g.state == "fright":
                    slow = k / FRIGHT_SPEED
                    t = slow if slow <= wait else wait + (k - wait * FRIGHT_SPEED) / g.base
                    t = max(t, wait)
                else:
                    t = (0.0 if q == g.tile and g.nxt is None else delay) + k / g.base
                if t < soon.get(q, math.inf):
                    soon[q] = t
            if g.nxt is not None and g.state != "fright":
                soon[g.tile] = 0.0       # ainda está saindo dali
        return soon

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
        peril = self.peril(now)
        out = route(self.board, pac.tile, pac.dir, peril, target)
        if target in out and not out[target][2]:
            return out[target][1][0]
        # o caminho cruza um fantasma: vai para o quadrado verde seguro mais perto ou foge
        out = route(self.board, pac.tile, pac.dir, peril)
        safe = [p for p in self.pellets if p in out and not out[p][2]]
        if safe:
            goal = min(safe, key=lambda p: (out[p][0], p))
        else:
            away = [p for p in out if p != pac.tile and not out[p][2]]
            goal = max(away, key=lambda p: (out[p][0], p)) if away else target
        return out[goal][1][0] if goal in out and out[goal][1] else None

    def dodge(self, t):
        """Dá meia volta no meio do caminho se um fantasma vai chegar antes no quadrado da frente."""
        pac = self.pac
        if pac.nxt is None:
            return

        def threat(cell, other, time):
            for g in self.ghosts:
                if g.state not in ("house", "chase"):
                    continue
                if g.nxt is None and g.tile == cell:
                    return True
                if g.tile == cell and g.nxt == other:
                    return True
                if g.nxt == cell and g.tile != other and (1.0 - g.prog) / g.speed <= time + 0.8:
                    return True
            return False
        if threat(pac.nxt, pac.tile, 1.0 - pac.prog) and not threat(pac.tile, pac.nxt, pac.prog):
            pac.reverse(t)

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
                    g.reverse(self.t)    # os fantasmas ainda estão no começo deste passo
                if g.state in ("chase", "fright"):
                    g.state = "fright"
                    g.show(now, "fright")

    def die(self, t):
        """Um fantasma pegou o Pac-Man: tudo para, ele some e, se ainda tem vida, todos voltam ao começo."""
        self.lives -= 1
        pac = self.pac
        self.deaths.append((t, pac.pos(), pac.dir))
        freeze = t + DEATH_FREEZE / TICK
        gone = freeze + DEATH_ANIM / TICK
        pac.cut(t)
        for g in self.ghosts:
            g.mark(t)
            g.cut(freeze)
        self.fright_until = -1.0
        self.combo = 0
        if self.lives == 0:
            self.over = self.done = gone
            return
        back = gone + DEATH_GAP / TICK
        self.resume = back + READY / TICK
        self.respawns.append((back, self.resume))
        pac.place(self.start, (1, 0), back)
        for g in self.ghosts:
            g.place(g.home, (-1, 0), back)
            g.state = "house"
            g.free_at = self.resume + g.release
            g.show(back, "normal")
        self.mode, self.mode_clock = "scatter", 0.0
        self.replan = True

    # ---- fantasmas

    def target(self, g):
        if self.mode == "scatter":
            return self.corners[g.name]
        p, d = self.pac.near(), self.pac.dir
        if g.name == "pinky":
            return (p[0] + 4 * d[0], p[1] + 4 * d[1])
        if g.name == "inky":
            b = next(x for x in self.ghosts if x.name == "blinky").pos()
            v = (p[0] + 2 * d[0], p[1] + 2 * d[1])
            return (2 * v[0] - b[0], 2 * v[1] - b[1])
        if g.name == "clyde" and euclid(g.tile, p) <= 8:
            return self.corners["clyde"]
        return p

    def ghost_decide(self, g, now):
        nbrs = self.board.nbrs[g.tile]
        if g.state == "house":
            if now < g.free_at:
                return None
            g.state = "chase"
        if g.state == "eyes":
            if g.tile != g.home:
                home = self.board.dist[g.home]
                return min(nbrs, key=lambda o: home[o[0]])[0]
            if manhattan(g.home, self.pac.tile) < 3:
                return None
            g.state = "chase"
            g.show(now, "normal")
        back = (-g.dir[0], -g.dir[1])
        ahead = [o for o in nbrs if o[1] != back] or nbrs
        if g.state == "fright":
            pac = self.pac.pos()
            return max(ahead, key=lambda o: euclid(o[0], pac) + self.rng.random() * 2.0)[0]
        aim = self.target(g)
        return min(ahead, key=lambda o: euclid(o[0], aim))[0]

    def ghost_arrive(self, g, now):
        pass

    def speed(self, g):
        return {"fright": FRIGHT_SPEED, "eyes": EYES_SPEED}.get(g.state, g.base)

    # ---- laço principal

    def update(self, t, dt):
        for g in self.ghosts:
            if g.state != "fright":
                continue
            if t >= self.fright_until:
                g.state = "chase"
                g.show(t, "normal")
            elif t >= self.fright_until - FLASH / TICK:
                g.show(t, "flash")
        if t >= self.fright_until:       # o relógio da dispersão para durante o susto
            self.mode_clock += dt
        s, mode = self.mode_clock * TICK, "chase"
        for i, dur in enumerate(MODES):
            if s < dur:
                mode = "scatter" if i % 2 == 0 else "chase"
                break
            s -= dur
        if mode != self.mode:
            self.mode = mode
            for g in self.ghosts:
                if g.state == "chase":
                    g.reverse(t)

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
                self.die(t)
                return

    def run(self):
        dt = 1.0 / SUB
        if self.pac.tile in self.pellets:
            self.eat(self.pac.tile, 0.0)
        if not self.pellets:
            self.done = 0.0
        while self.done is None and self.t < MAX_TICKS:
            if self.t >= self.resume - 1e-9:
                self.update(self.t, dt)
                self.dodge(self.t)
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
            if a.track is None:
                continue
            a.track = [(t, p) for t, p in a.track if t <= self.done + 1e-9]
            a.track.append((self.done, a.pos()))
            a.parts.append((a.since, None, a.track))
            a.track = None
        return self


# ---- SVG

def px(p):
    return (p[0] * PITCH + CELL / 2, TOP + p[1] * PITCH + CELL / 2)


def corner_px(c):
    """Centro do vão entre os quadrados, no canto (i, j)."""
    gap = (PITCH - CELL) / 2
    return (c[0] * PITCH - gap, TOP + c[1] * PITCH - gap)


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
    def __init__(self, ticks, pause=END):
        self.D = READY + ticks * TICK + pause

    def sec(self, t):
        return READY + t * TICK

    def key(self, s):
        return f"{min(max(s / self.D, 0.0), 1.0):.5f}".rstrip("0").rstrip(".") or "0"


def motion(track, clock, rotate=False):
    pts = [px(p) for _, p in track]
    geo, index = [pts[0]], []
    for p in pts:
        if math.hypot(p[0] - geo[-1][0], p[1] - geo[-1][1]) > 1e-6:
            geo.append(p)
        index.append(len(geo) - 1)
    x0, y0 = geo[0]
    if len(geo) == 1:
        return f'transform="translate({num(x0)} {num(y0)})"', ""
    path, at, total = rounded_path(geo)
    times = ["0"] + [clock.key(clock.sec(t)) for t, _ in track] + ["1"]
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


def window(clock, start, end):
    """Opacidade que mostra um trecho só entre start e end (tempos da simulação; end None é até o fim)."""
    changes = [(0.0, "1" if start <= 0 else "0")]
    if start > 0:
        changes.append((clock.sec(start), "1"))
    if end is not None:
        changes.append((clock.sec(end), "0"))
    return discrete("opacity", changes, clock)


def pacman_d(angle):
    c, s = 9 * math.cos(angle), 9 * math.sin(angle)
    big = 1 if angle < math.pi / 2 else 0
    return f"M0 0L{num(c)} {num(s)}A9 9 0 {big} 1 {num(c)} {num(-s)}Z"


GHOST_A = "M-9 9L-9 0A9 9 0 0 1 9 0L9 9L6 6L3 9L0 6L-3 9L-6 6Z"
GHOST_B = "M-9 7L-9 0A9 9 0 0 1 9 0L9 7L7.5 9L4.5 6L1.5 9L-1.5 6L-4.5 9L-7.5 6Z"


def ghost_svg(g, game, clock):
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
    sprite = (f'<g opacity="{gone0}">{gone}'
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
              f'stroke-width="1.2">{mouth}</path></g></g>')
    out = []
    for start, end, track in g.parts:     # um trecho por vida: some quando o Pac-Man morre
        attr, anim = motion(track, clock)
        op0, op = window(clock, start, end)
        out.append(f'<g opacity="{op0}">{op}<g {attr}>{anim}{sprite}</g></g>')
    return "".join(out)


def death_svg(t, pos, facing, clock, stroke):
    """Pac-Man parado enquanto tudo congela e depois a boca abrindo até ele sumir, como no original."""
    x, y = px(pos)
    s0 = clock.sec(t)
    s1 = s0 + DEATH_FREEZE
    s2 = s1 + DEATH_ANIM
    angle = math.degrees(math.atan2(facing[1], facing[0]))
    still0, still = discrete("opacity", [(0.0, "0"), (s0, "1"), (s1, "0")], clock)
    dying0, dying = discrete("opacity", [(0.0, "0"), (s1, "1"), (s2, "0")], clock)
    frames = [(s1 + DEATH_ANIM * k / DEATH_FRAMES, pacman_d(0.25 + (math.pi - 0.4) * k / (DEATH_FRAMES - 1)))
              for k in range(DEATH_FRAMES)]
    shape0, shape = discrete("d", [(0.0, frames[0][1])] + frames, clock)
    return (f'<g transform="translate({num(x)} {num(y)})">'
            f'<g opacity="{still0}">{still}<path d="{pacman_d(0.45)}" transform="rotate({num(angle)})" '
            f'fill="#ffcc00"{stroke}/></g>'
            f'<g opacity="{dying0}">{dying}<path d="{shape0}" transform="rotate(-90)" fill="#ffcc00"{stroke}>'
            f'{shape}</path></g></g>')


def banner(text, color, spans, clock, th, x, y):
    """Texto no meio do tabuleiro (READY!, GAME OVER) nos intervalos de spans, em segundos."""
    changes = [(0.0, "0")]
    for a, b in spans:
        changes.append((a, "1"))
        if b is not None:
            changes.append((b, "0"))
    op0, op = discrete("opacity", changes, clock)
    return (f'<text x="{num(x)}" y="{num(y)}" dy="0.35em" text-anchor="middle" font-size="15" font-weight="bold" '
            f'letter-spacing="2" font-family="Consolas,Menlo,monospace" fill="{color}" stroke="{th["bg"]}" '
            f'stroke-width="4" stroke-linejoin="round" paint-order="stroke" opacity="{op0}">{op}{text}</text>')


def render(game, theme):
    board, th = game.board, THEMES[theme]
    clock = Clock(game.done, OVER if game.over is not None else END)
    width = board.W * PITCH - 2
    height = TOP + ROWS * PITCH + 2
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

    if board.walls:
        lines = []
        for a, b in board.walls:
            (x1, y1), (x2, y2) = corner_px(a), corner_px(b)
            lines.append(f"M{num(x1)} {num(y1)}L{num(x2)} {num(y2)}")
        out.append(f'<path d="{"".join(lines)}" fill="none" stroke="{th["wall"]}" stroke-width="{WALL_WIDTH}" '
                   f'stroke-linecap="round"/>')

    stroke = f' stroke="{th["pac_stroke"]}" stroke-width="0.8"' if th["pac_stroke"] else ""
    chomp = ";".join(pacman_d(a) for a in (0.75, 0.05, 0.75))
    for start, end, track in game.pac.parts:    # um trecho por vida
        attr, anim = motion(track, clock, rotate=True)
        op0, op = window(clock, start, end)
        out.append(f'<g opacity="{op0}">{op}<g {attr}>{anim}<path d="{pacman_d(0.75)}" fill="#ffcc00"{stroke}>'
                   f'<animate attributeName="d" dur="0.24s" repeatCount="indefinite" values="{chomp}"/></path></g></g>')
    for t, pos, facing in game.deaths:
        out.append(death_svg(t, pos, facing, clock, stroke))

    for g in game.ghosts:
        out.append(ghost_svg(g, game, clock))

    for t, p, points in game.popups:
        x, y = px(p)
        s = clock.sec(t)
        _, show = discrete("opacity", [(0.0, "0"), (s, "1"), (s + 0.9, "0")], clock)
        out.append(f'<text x="{num(x)}" y="{num(y + 3)}" text-anchor="middle" font-size="9" font-weight="bold" '
                   f'font-family="monospace" fill="#00e5ff" opacity="0">{points}{show}</text>')

    cx, cy = width / 2, TOP + (ROWS / 2) * PITCH - 1
    ready = [(0.0, READY)] + [(clock.sec(a), clock.sec(b)) for a, b in game.respawns]
    out.append(banner("READY!", "#ffff00", ready, clock, th, cx, cy))
    if game.over is not None:
        out.append(banner("GAME OVER", "#ff0000", [(clock.sec(game.over), None)], clock, th, cx, cy))
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

    board = Board(weeks, maze(len(weeks), random.Random(args.seed)))
    game = Game(board, args.seed).run()
    os.makedirs(args.out, exist_ok=True)
    for theme, name in (("light", "pacman-contribution-graph.svg"), ("dark", "pacman-contribution-graph-dark.svg")):
        with open(os.path.join(args.out, name), "w") as f:
            f.write(render(game, theme))
    clock = Clock(game.done, OVER if game.over is not None else END)
    print(f"{len(board.walls)} paredes, {len(game.eaten)} quadrados comidos, {len(game.power)} pílulas de poder, "
          f"{len(game.popups)} fantasmas comidos, {len(game.deaths)} mortes"
          f"{' (GAME OVER)' if game.over is not None else ''}, {len(game.pellets)} sobraram, {clock.D:.1f} s")


if __name__ == "__main__":
    main()
