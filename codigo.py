# ============================================================
#   SIGIC – Sistema Inteligente de Gerenciamento da
#           Infraestrutura da Colônia Aurora Siger
# ============================================================
# Disciplinas integradas:
#   • Grafos e algoritmos de redes (BFS, DFS, Dijkstra)
#   • Estruturas de dados em Python (listas, matrizes,
#     tuplas, dicionários)
#   • Modelagem matemática e otimização
#   • Sustentabilidade e governança ESG
# ============================================================

import heapq
import math

# ============================================================
# 1. ESTRUTURAS DE DADOS
# ============================================================

# --- DICIONÁRIO: dados principais de cada módulo -----------
# Justificativa: acesso O(1) por nome do módulo;
# ideal para consultas rápidas durante operação da colônia.
modulos = {
    "Habitação":                {"consumo": 45,  "prioridade": 1, "status": "Ativo"},
    "Centro de Controle":       {"consumo": 60,  "prioridade": 1, "status": "Ativo"},
    "Armazenamento de Energia": {"consumo": 10,  "prioridade": 1, "status": "Ativo"},
    "Agricultura":              {"consumo": 35,  "prioridade": 2, "status": "Ativo"},
    "Laboratório Científico":   {"consumo": 50,  "prioridade": 2, "status": "Ativo"},
    "Comunicação":              {"consumo": 40,  "prioridade": 1, "status": "Ativo"},
    "Suporte Médico":           {"consumo": 55,  "prioridade": 1, "status": "Ativo"},
    "Produção de Oxigênio":     {"consumo": 70,  "prioridade": 1, "status": "Ativo"},
}

# --- LISTA: vértices (módulos) na ordem definida -----------
# Justificativa: mantém ordem e permite indexação numérica
# para a matriz de adjacência.
vertices = [
    "Habitação",
    "Centro de Controle",
    "Armazenamento de Energia",
    "Agricultura",
    "Laboratório Científico",
    "Comunicação",
    "Suporte Médico",
    "Produção de Oxigênio",
]

N = len(vertices)  # número de módulos = 8

# Mapa nome → índice (auxiliar)
IDX = {nome: i for i, nome in enumerate(vertices)}

# --- TUPLAS: arestas fixas da rede (topologia imutável) ----
# Formato: (origem, destino, distância_metros)
# Justificativa: tuplas são imutáveis — a topologia física
# não muda em tempo de execução.
# 16 conexões conforme documentação; hub central = AE.
arestas = (
    ("Armazenamento de Energia", "Centro de Controle",       15),
    ("Armazenamento de Energia", "Produção de Oxigênio",     20),
    ("Armazenamento de Energia", "Habitação",                25),
    ("Armazenamento de Energia", "Suporte Médico",           30),
    ("Armazenamento de Energia", "Comunicação",              12),
    ("Armazenamento de Energia", "Laboratório Científico",   35),
    ("Armazenamento de Energia", "Agricultura",              40),
    ("Centro de Controle",       "Habitação",                20),
    ("Centro de Controle",       "Comunicação",              15),
    ("Centro de Controle",       "Laboratório Científico",   20),
    ("Centro de Controle",       "Suporte Médico",           25),
    ("Habitação",                "Suporte Médico",           18),
    ("Habitação",                "Produção de Oxigênio",     22),
    ("Comunicação",              "Laboratório Científico",   18),
    ("Agricultura",              "Laboratório Científico",   15),
    ("Suporte Médico",           "Produção de Oxigênio",     20),
)

# --- LISTA DE ADJACÊNCIA: grafo não-direcionado ponderado --
# Justificativa: eficiente para grafos esparsos;
# usada diretamente nos algoritmos BFS, DFS e Dijkstra.
def _construir_grafo():
    grafo = {v: [] for v in vertices}
    for origem, destino, peso in arestas:
        grafo[origem].append((destino, peso))
        grafo[destino].append((origem, peso))
    return grafo

grafo = _construir_grafo()

# --- MATRIZ DE ADJACÊNCIA ----------------------------------
# Justificativa: visualização clara; acesso direto por índice.
def gerar_matriz_adjacencia():
    """Retorna matriz N×N com os pesos das arestas (0 = sem conexão)."""
    matriz = [[0] * N for _ in range(N)]
    for origem, destino, peso in arestas:
        i, j = IDX[origem], IDX[destino]
        matriz[i][j] = peso
        matriz[j][i] = peso
    return matriz


# ============================================================
# 2. ALGORITMOS DE REDES
# ============================================================

# --- BFS: Busca em Largura — O(V + E) ----------------------
def bfs(inicio):
    """
    Percorre a rede camada a camada a partir de 'inicio'.
    Retorna a lista de módulos visitados em ordem de descoberta.
    Uso na colônia: verifica módulos alcançáveis e menor nº de saltos.
    """
    visitados = []
    visitado_set = {inicio}
    fila = [inicio]

    while fila:
        atual = fila.pop(0)
        visitados.append(atual)
        for vizinho, _ in grafo.get(atual, []):
            if vizinho not in visitado_set:
                visitado_set.add(vizinho)
                fila.append(vizinho)
    return visitados


# --- DFS: Busca em Profundidade — O(V + E) -----------------
def dfs(inicio, _visitado=None):
    """
    Percorre a rede em profundidade a partir de 'inicio'.
    Retorna a lista de módulos visitados na ordem de visita.
    Uso na colônia: detectar pontos críticos de falha.
    """
    if _visitado is None:
        _visitado = set()
    _visitado.add(inicio)
    resultado = [inicio]
    for vizinho, _ in grafo.get(inicio, []):
        if vizinho not in _visitado:
            resultado += dfs(vizinho, _visitado)
    return resultado


# --- DIJKSTRA: Caminho Mínimo — O((V+E) log V) -------------
def dijkstra(inicio, fim):
    """
    Calcula a rota de menor distância entre 'inicio' e 'fim'.
    Usa fila de prioridade (heap binário) para otimizar a busca.
    Retorna (distância_total, [caminho]).
    Uso na colônia: distribuição de energia pelo caminho mais eficiente.
    """
    dist = {v: math.inf for v in vertices}
    dist[inicio] = 0
    anterior = {v: None for v in vertices}
    heap = [(0, inicio)]

    while heap:
        d_atual, atual = heapq.heappop(heap)
        if atual == fim:
            break
        if d_atual > dist[atual]:
            continue
        for vizinho, peso in grafo.get(atual, []):
            nova_dist = d_atual + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                anterior[vizinho] = atual
                heapq.heappush(heap, (nova_dist, vizinho))

    # Reconstrói caminho
    caminho = []
    no = fim
    while no is not None:
        caminho.insert(0, no)
        no = anterior[no]

    if dist[fim] == math.inf:
        return None, []
    return dist[fim], caminho


# --- Dijkstra a partir do Armazenamento de Energia ---------
def dijkstra_de_ae():
    """
    Calcula rotas mínimas do Armazenamento de Energia
    para todos os demais módulos.
    Retorna lista de dicionários ordenada por distância.
    """
    origem = "Armazenamento de Energia"
    resultados = []
    for destino in vertices:
        if destino == origem:
            continue
        dist, caminho = dijkstra(origem, destino)
        resultados.append({
            "destino":    destino,
            "distancia":  dist,
            "caminho":    caminho,
        })
    resultados.sort(key=lambda x: x["distancia"])
    return resultados


# --- Detecção de pontes (conexões críticas) — DFS ----------
def detectar_pontes():
    """
    Identifica arestas cuja remoção desconectaria a rede.
    Retorna lista de tuplas (módulo_a, módulo_b).
    Uso na colônia: apontar conexões que precisam de redundância.
    """
    visitado  = {}
    low       = {}
    pai       = {}
    pontes    = []
    timer     = [0]

    def _dfs(u):
        visitado[u] = low[u] = timer[0]
        timer[0] += 1
        for v, _ in grafo.get(u, []):
            if v not in visitado:
                pai[v] = u
                _dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > visitado[u]:
                    pontes.append((u, v))
            elif v != pai.get(u):
                low[u] = min(low[u], visitado[v])

    for modulo in vertices:
        if modulo not in visitado:
            pai[modulo] = None
            _dfs(modulo)

    return pontes


# ============================================================
# 3. MODELAGEM MATEMÁTICA E OTIMIZAÇÃO
# ============================================================

# --- Modelo 1: Crescimento Exponencial do Consumo ----------
# Fórmula: E(n) = E0 × (1 + r)^n
# E0 = consumo base de um módulo (50 kW)
# r  = taxa de crescimento por módulo adicional (8% = 0,08)
# n  = número de módulos ativos
def modelo_crescimento_exponencial(n_max=8):
    """
    Projeta o consumo energético conforme novos módulos são adicionados.
    Retorna lista de (n_módulos, consumo_kW).
    """
    E0 = 50.0   # consumo base (kW)
    r  = 0.08   # taxa de 8% por módulo adicional
    resultado = []
    for n in range(1, n_max + 1):
        en = E0 * ((1 + r) ** n)
        resultado.append((n, round(en, 2)))
    return resultado


# --- Modelo 2: Eficiência da Rede de Distribuição ----------
# Fórmula: η = (E_útil / E_total) × 100
# Perda por conexão = distância × 0,2% por metro
def modelo_eficiencia_rede():
    """
    Calcula a eficiência da rede somando perdas em todas as arestas.
    Retorna dicionário com E_útil, perda_total e eficiência.
    """
    e_util = sum(m["consumo"] for m in modulos.values())  # 365 kW
    perda_total = 0.0
    for _, _, dist in arestas:
        perda_total += dist * 0.002  # 0,2% por metro → fração de kW

    e_total    = e_util + perda_total
    eficiencia = (e_util / e_total) * 100

    return {
        "e_util_kW":     round(e_util, 2),
        "perda_total_kW": round(perda_total, 4),
        "e_total_kW":    round(e_total, 4),
        "eficiencia_pct": round(eficiencia, 2),
    }


def perda_conexao(distancia_m):
    """Estima perda percentual de uma conexão: dist × 0,2%/m."""
    return round(distancia_m * 0.002, 4)


# ============================================================
# 4. SUSTENTABILIDADE E GOVERNANÇA ESG
# ============================================================

def relatorio_esg():
    """
    Gera relatório ESG com base no estado atual da colônia,
    conforme diretrizes da documentação complementar.
    """
    eff   = modelo_eficiencia_rede()
    pontes = detectar_pontes()

    criticos    = [n for n, m in modulos.items() if m["prioridade"] == 1]
    importantes = [n for n, m in modulos.items() if m["prioridade"] == 2]

    linhas = [
        "=" * 62,
        "  RELATÓRIO ESG — Aurora Siger",
        "=" * 62,

        "\n[E — AMBIENTAL]",
        f"  Consumo total (E_útil)  : {eff['e_util_kW']} kW",
        f"  Perda total na rede     : {eff['perda_total_kW']} kW",
        f"  Eficiência da rede      : {eff['eficiencia_pct']}%",
        "",
        "  Ações propostas:",
        "  • Módulos de prioridade 2 entram em modo de espera (10%",
        "    do consumo) quando armazenamento cai abaixo de 20%.",
        "  • Novos módulos devem ser posicionados a ≤ 30 m do",
        "    Armazenamento de Energia para limitar perdas.",
        "  • Painéis solares com margem de 20% acima do consumo",
        "    projetado para suportar expansões e emergências.",

        "\n[S — SOCIAL]",
        f"  Módulos críticos (prioridade 1)  : {len(criticos)}",
    ]
    for n in criticos:
        linhas.append(f"      ★ {n}")
    linhas += [
        f"  Módulos importantes (prioridade 2): {len(importantes)}",
    ]
    for n in importantes:
        linhas.append(f"      ◆ {n}")
    linhas += [
        "",
        "  Garantia social:",
        "  • Módulos de prioridade 1 NUNCA são desligados sem",
        "    protocolo de emergência aprovado pelo Centro de Controle.",

        "\n[G — GOVERNANÇA]",
        f"  Conexões críticas detectadas (pontes): {len(pontes)}",
    ]
    if pontes:
        for p in pontes:
            linhas.append(f"      ⚠  {p[0]}  ↔  {p[1]}")
        linhas.append("  → Criar rotas redundantes para essas conexões.")
    else:
        linhas.append("  ✓ Rede com redundância adequada — nenhuma ponte.")
    linhas += [
        "",
        "  Diretrizes de governança tecnológica:",
        "  • Decisões de desligamento automatizadas passam por",
        "    aprovação do Centro de Controle, com log de auditoria.",
        "  • Alertas automáticos para desvios de consumo > 15%",
        "    do esperado em qualquer módulo.",
        "  • Auditorias semanais de status e consumo.",
        "=" * 62,
    ]
    return "\n".join(linhas)


# ============================================================
# 5. FUNÇÕES DE EXIBIÇÃO
# ============================================================

def exibir_modulos():
    print("\n" + "=" * 62)
    print("  MÓDULOS DA COLÔNIA AURORA SIGER")
    print("=" * 62)
    print(f"  {'#':<3} {'Módulo':<28} {'kW':>6} {'Prior':>6} {'Status'}")
    print("  " + "-" * 55)
    for i, nome in enumerate(vertices):
        m = modulos[nome]
        prior_txt = "1-Crítico" if m["prioridade"] == 1 else "2-Importante"
        icone = "★" if m["prioridade"] == 1 else "◆"
        print(f"  {i:<3} {nome:<28} {m['consumo']:>6} {icone} {prior_txt:<14} {m['status']}")


def exibir_rede():
    print("\n" + "=" * 62)
    print("  REDE DA COLÔNIA — Lista de Adjacência")
    print("=" * 62)
    for nome in vertices:
        print(f"\n  [{nome}]")
        for vizinho, dist in grafo[nome]:
            print(f"      → {vizinho}  ({dist} m)")


def exibir_arestas():
    print("\n" + "=" * 62)
    print("  ARESTAS DA REDE (Tuplas imutáveis)")
    print("=" * 62)
    print(f"  {'#':<4} {'Origem':<28} {'Destino':<28} {'Dist(m)':>7}")
    print("  " + "-" * 70)
    for i, (o, d, p) in enumerate(arestas):
        print(f"  {i:<4} {o:<28} {d:<28} {p:>7}")
    print(f"\n  Total: {len(arestas)} conexões")


def exibir_matriz():
    matriz = gerar_matriz_adjacencia()
    print("\n" + "=" * 62)
    print("  MATRIZ DE ADJACÊNCIA (distâncias em metros)")
    print("=" * 62)
    # Abreviações para caber na tela
    abrev = ["HAB", "CC", "AE", "AGR", "LAB", "COM", "SM", "PO"]
    header = "           " + "".join(f"{a:>6}" for a in abrev)
    print(header)
    for i, linha in enumerate(matriz):
        print(f"  {abrev[i]:<8}  " + "".join(f"{v:>6}" for v in linha))
    print("\n  Legenda: HAB=Habitação  CC=Centro de Controle")
    print("           AE=Armazenamento de Energia  AGR=Agricultura")
    print("           LAB=Lab.Científico  COM=Comunicação")
    print("           SM=Suporte Médico  PO=Produção de Oxigênio")


def exibir_bfs(inicio):
    resultado = bfs(inicio)
    print(f"\n  BFS a partir de '{inicio}':")
    print(f"  Complexidade: O(V + E)")
    for i, m in enumerate(resultado):
        print(f"    Passo {i+1}: {m}")


def exibir_dfs(inicio):
    resultado = dfs(inicio)
    print(f"\n  DFS a partir de '{inicio}':")
    print(f"  Complexidade: O(V + E)")
    for i, m in enumerate(resultado):
        print(f"    Passo {i+1}: {m}")


def exibir_dijkstra_ae():
    resultados = dijkstra_de_ae()
    print("\n" + "=" * 62)
    print("  DIJKSTRA — Rotas a partir do Armazenamento de Energia")
    print("=" * 62)
    print(f"  Complexidade: O((V+E) log V)")
    print(f"\n  {'Destino':<28} {'Dist(m)':>7}  Caminho")
    print("  " + "-" * 70)
    for r in resultados:
        caminho_str = " → ".join(
            v.replace("Armazenamento de Energia", "AE")
             .replace("Centro de Controle", "CC")
             .replace("Habitação", "HAB")
             .replace("Suporte Médico", "SM")
             .replace("Comunicação", "COM")
             .replace("Laboratório Científico", "LAB")
             .replace("Agricultura", "AGR")
             .replace("Produção de Oxigênio", "PO")
            for v in r["caminho"]
        )
        print(f"  {r['destino']:<28} {r['distancia']:>7}  {caminho_str}")


def exibir_dijkstra_personalizado(origem, destino):
    dist, caminho = dijkstra(origem, destino)
    if dist is None:
        print(f"\n  ✗ Sem caminho entre '{origem}' e '{destino}'.")
        return
    perda = perda_conexao(dist)
    print(f"\n  Rota mínima: {origem}  →  {destino}")
    print(f"  Caminho    : {' → '.join(caminho)}")
    print(f"  Distância  : {dist} m")
    print(f"  Perda est. : {perda * 100:.2f}%  ({perda:.4f} kW por kW transportado)")


def exibir_pontes():
    pontes = detectar_pontes()
    print("\n  Conexões críticas (pontes) detectadas:")
    if pontes:
        for p in pontes:
            print(f"    ⚠  {p[0]}  ↔  {p[1]}")
        print("  → Essas conexões precisam de rotas redundantes.")
    else:
        print("  ✓ Nenhuma ponte — a rede possui redundância adequada.")


def exibir_modelagem():
    print("\n" + "=" * 62)
    print("  MODELAGEM MATEMÁTICA")
    print("=" * 62)

    # Modelo 1
    print("\n  Modelo 1 — Crescimento Exponencial do Consumo")
    print("  Fórmula: E(n) = E0 × (1 + r)^n")
    print("  E0 = 50 kW  |  r = 8% por módulo adicional")
    print(f"\n  {'n (módulos)':<14} {'E(n) kW':>10}  {'Crescimento':>12}")
    print("  " + "-" * 40)
    projecao = modelo_crescimento_exponencial()
    prev = None
    for n, en in projecao:
        delta = f"+{en - prev:.1f} kW" if prev is not None else "—"
        print(f"  {n:<14} {en:>10.2f}  {delta:>12}")
        prev = en
    print("\n  Interpretação: Função exponencial crescente.")
    print("  O sistema de armazenamento deve ter margem de 20%")
    print("  acima do consumo projetado para emergências.")

    # Modelo 2
    eff = modelo_eficiencia_rede()
    print("\n  Modelo 2 — Eficiência da Rede de Distribuição")
    print("  Fórmula: η = (E_útil / E_total) × 100")
    print("  Perda por conexão = distância × 0,2%/m")
    print(f"\n  E_útil      : {eff['e_util_kW']} kW")
    print(f"  Perda total : {eff['perda_total_kW']} kW")
    print(f"  E_total     : {eff['e_total_kW']} kW")
    print(f"  Eficiência  : {eff['eficiencia_pct']}%")
    print("\n  Otimização: reduzir distância entre módulos críticos")
    print("  aumenta eficiência. AE→SM (30 m) é mais eficiente")
    print("  do que AE→CC→HAB→SM (43 m) — ligação direta confirmada.")


def selecionar_modulo(prompt="  Número do módulo: "):
    for i, nome in enumerate(vertices):
        print(f"    {i} – {nome}")
    try:
        idx = int(input(prompt))
        if 0 <= idx < N:
            return vertices[idx]
    except ValueError:
        pass
    print("  Opção inválida.")
    return None


# ============================================================
# 6. MENU PRINCIPAL
# ============================================================

def menu():
    print("\n" + "=" * 62)
    print("  SIGIC — Sistema Inteligente de Gerenciamento")
    print("          da Infraestrutura da Colônia")
    print("          Aurora Siger  🚀")
    print("=" * 62)

    while True:
        print("\n  ── MENU PRINCIPAL ──────────────────────────────────")
        print("   [ 1] Visualizar módulos da colônia")
        print("   [ 2] Visualizar rede (lista de adjacência)")
        print("   [ 3] Visualizar arestas (tuplas)")
        print("   [ 4] Visualizar matriz de adjacência")
        print("   [ 5] BFS — Busca em Largura")
        print("   [ 6] DFS — Busca em Profundidade")
        print("   [ 7] Dijkstra — Rotas a partir do Armazenamento")
        print("   [ 8] Dijkstra — Rota personalizada")
        print("   [ 9] Detectar conexões críticas (pontes)")
        print("   [10] Modelagem matemática")
        print("   [11] Relatório ESG")
        print("   [ 0] Sair")
        print("  ─────────────────────────────────────────────────────")

        escolha = input("  Opção: ").strip()

        if escolha == "0":
            print("\n  Encerrando SIGIC. Boa sorte, tripulação! 🛸\n")
            break

        elif escolha == "1":
            exibir_modulos()

        elif escolha == "2":
            exibir_rede()

        elif escolha == "3":
            exibir_arestas()

        elif escolha == "4":
            exibir_matriz()

        elif escolha == "5":
            print("\n  BFS — módulo de início:")
            inicio = selecionar_modulo()
            if inicio:
                exibir_bfs(inicio)

        elif escolha == "6":
            print("\n  DFS — módulo de início:")
            inicio = selecionar_modulo()
            if inicio:
                exibir_dfs(inicio)

        elif escolha == "7":
            exibir_dijkstra_ae()

        elif escolha == "8":
            print("\n  DIJKSTRA — módulo de ORIGEM:")
            origem = selecionar_modulo()
            if origem:
                print("\n  DIJKSTRA — módulo de DESTINO:")
                destino = selecionar_modulo()
                if destino and destino != origem:
                    exibir_dijkstra_personalizado(origem, destino)
                elif destino == origem:
                    print("  Origem e destino são iguais.")

        elif escolha == "9":
            exibir_pontes()

        elif escolha == "10":
            exibir_modelagem()

        elif escolha == "11":
            print(relatorio_esg())

        else:
            print("  Opção inválida. Tente novamente.")

        input("\n  Pressione Enter para continuar...")


# ============================================================
# 7. PONTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    menu()
