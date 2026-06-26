# 🚀 SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia

## 👥 Equipe

| Nome | RM |
|------|----|
| Ana Gabriela     | rm571312 |
| Kaique           | rm570533 |
| Miguel Antunes   | rm573643 |
| Miguel Gonçalves | rm573793 |

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
## ▶️ Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa é necessária para o sistema principal

 Windows:

```bash
python codigo.py
```

---

## 🖥️ Menu do Sistema

Ao executar o arquivo principal, o seguinte menu estará disponível:

```
============================================================
  SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia
============================================================

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

## 🎥 Vídeo de Apresentação

O link do vídeo de apresentação está disponível no arquivo `[video](https://youtu.be/FLWwIds0gMw)`.

---

## 📚 Conteúdos Aplicados

- Grafos e algoritmos de redes (BFS, DFS, Dijkstra)
- Matrizes e listas de adjacência
- Estruturas de dados em Python (listas, matrizes, tuplas, dicionários)
- Modelagem matemática e cálculo diferencial aplicado
- Otimização computacional
- Sustentabilidade e governança ESG
