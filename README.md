# 🚀 SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia

## 📋 Descrição do Projeto

O **SIGIC** é um sistema desenvolvido em Python que representa computacionalmente a infraestrutura da base marciana **Aurora Siger**. Ele modela a rede de módulos da colônia usando grafos e implementa algoritmos clássicos de teoria de redes para otimizar a distribuição de energia e a operação da base.

---

## 🏗️ Módulos da Colônia

| Módulo | Consumo (kW) | Prioridade |
|---|---|---|
| Habitação | 45 | 1 - Crítico |
| Centro de Controle | 60 | 1 - Crítico |
| Armazenamento de Energia | 10 | 1 - Crítico |
| Agricultura | 35 | 2 - Importante |
| Laboratório Científico | 50 | 2 - Importante |
| Comunicação | 40 | 1 - Crítico |
| Suporte Médico | 55 | 1 - Crítico |
| Produção de Oxigênio | 70 | 1 - Crítico |

---

## SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia

  [1]  Visualizar rede da colônia (conexões)
  [2]  Visualizar matriz de adjacência
  [3]  Consultar módulos da colônia
  [4]  Executar BFS (Busca em Largura)
  [5]  Executar DFS (Busca em Profundidade)
  [6]  Executar Dijkstra (Caminho Mínimo)
  [7]  Detectar pontos críticos da rede
  [8]  Modelagem matemática e eficiência
  [9]  Sustentabilidade e Governança ESG
  [10] Simular falha de módulo
  [0]  Sair do sistema
```

---

## 🔢 Algoritmos Implementados

### BFS — Busca em Largura
Explora a rede camada por camada a partir de um módulo escolhido. Útil para verificar a conectividade da rede e descobrir o menor número de saltos entre módulos.

**Complexidade:** O(V + E)

### DFS — Busca em Profundidade
Explora a rede indo o mais fundo possível antes de retroceder. Utilizado internamente para detectar pontos críticos — módulos cuja falha desconectaria partes da infraestrutura.

**Complexidade:** O(V + E)

### Dijkstra — Caminho Mínimo
Encontra a rota de menor distância entre dois módulos, garantindo a distribuição de energia pelo caminho mais eficiente. Usa fila de prioridade (`heapq`).

**Complexidade:** O((V + E) log V)

---

## 🗂️ Estruturas de Dados

| Estrutura | Onde é usada | Por que foi escolhida |
|---|---|---|
| `dict` (dicionário) | `modulos` — dados de cada módulo | Acesso O(1) por nome |
| `list` (lista) | `vertices` — lista de módulos | Mantém ordem, permite indexação |
| `tuple` (tupla) | `arestas` — conexões da rede | Imutável; topologia não muda |
| Matriz (lista de listas) | Matriz de adjacência | Visualização clara das conexões |
| Lista de adjacência | `grafo` usado nos algoritmos | Eficiente para grafos esparsos |

---

## 📐 Modelagem Matemática

### Modelo 1 — Crescimento do Consumo Energético

```
E(n) = E₀ × (1 + r)ⁿ
```

- **E(n):** consumo total com n módulos ativos
- **E₀:** consumo base de um módulo (50 kW)
- **r:** taxa de crescimento por módulo (8%)
- **n:** número de módulos ativos

Função exponencial crescente — cada módulo adicional aumenta o consumo em ~8%, exigindo planejamento de capacidade para expansões futuras.

### Modelo 2 — Eficiência da Rede

```
η = (E_útil / E_total) × 100
```

- **η:** eficiência da rede (%)
- **E_útil:** soma do consumo dos módulos
- **E_total:** E_útil + perdas nas conexões (0,2% por metro)

A rede Aurora Siger opera com eficiência acima de **99%**, com perdas mínimas devido às distâncias relativamente curtas entre módulos.

---

## ♻️ Sustentabilidade e Governança ESG

- **Uso sustentável de energia:** módulos de prioridade 2 entram em modo de espera quando o armazenamento cai abaixo de 30%
- **Expansão organizada:** novos módulos devem ser posicionados a no máximo 30m do Armazenamento de Energia
- **Sistemas críticos:** módulos de prioridade 1 nunca são desligados em situações de emergência
- **Governança:** decisões de desligamento passam pelo Centro de Controle com log de auditoria
- **Redução de desperdícios:** alertas automáticos para desvios de consumo acima de 15%

---

## 🎥 Vídeo de Apresentação

O link do vídeo de apresentação está disponível no arquivo `link_video.txt`.

---

## 📚 Conteúdos Aplicados

- Grafos e algoritmos de redes (BFS, DFS, Dijkstra)
- Matrizes e listas de adjacência
- Estruturas de dados em Python (listas, matrizes, tuplas, dicionários)
- Modelagem matemática e cálculo diferencial aplicado
- Otimização computacional
- Sustentabilidade e governança ESG
