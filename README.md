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


## 🔢 Algoritmos Implementados

### BFS — Busca em Largura
Explora a rede camada por camada a partir de um módulo escolhido. Útil para verificar a conectividade da rede e descobrir o menor número de saltos entre módulos.


### DFS — Busca em Profundidade
Explora a rede indo o mais fundo possível antes de retroceder. Utilizado internamente para detectar pontos críticos — módulos cuja falha desconectaria partes da infraestrutura.


### Dijkstra — Caminho Mínimo
Encontra a rota de menor distância entre dois módulos, garantindo a distribuição de energia pelo caminho mais eficiente. Usa fila de prioridade (`heapq`).


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
