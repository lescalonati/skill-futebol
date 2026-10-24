---
name: "futebol-analise-tatica"
version: "1.0.0"
description: "Analisa o desempenho tático e estatístico de partidas de futebol, calculando eficiência ofensiva, defensiva e estimativas de gols esperados (xG)."
category: "esportes"
sport: "futebol"
triggers:
  - "quando o usuário solicitar análise tática de uma partida de futebol"
  - "ao calcular métricas de posse, finalizações e xG de um jogo"
  - "quando o usuário pedir resumo estruturado de desempenho de times de futebol"
author: "Comunidade Esportiva"
license: "MIT"
---

# Futebol: Análise Tática e de Desempenho

Esta skill orienta o assistente de IA a receber estatísticas brutas ou relatos de partidas de futebol e convertê-los em relatórios táticos estruturados, objetivos e fundamentados em métricas de eficiência moderna.

---

## 1. Objetivo e Cenários de Aplicação

- **Análise Pós-Jogo:** Avaliar se o resultado do placar refletiu o volume de jogo e as chances criadas.
- **Cálculo de Eficiência:** Medir pontaria de chutes, conversão de chances e controle territorial pela posse de bola.
- **Geração de Relatórios Padronizados:** Criar tabelas comparativas e pareceres táticos para analistas, jornalistas ou entusiastas esportivos.

---

## 2. Instruções Operacionais Passo a Passo

Ao receber uma partida para análise, siga a seguinte sequência:

1. **Extração das Estatísticas Básicas:**
   - Placar final (gols marcados por cada equipe).
   - Posse de bola (%) de cada lado.
   - Finalizações totais e finalizações no alvo.
   - Escanteios, faltas e cartões (se fornecidos).

2. **Processamento das Métricas Derivadas:**
   - Utilize o painel web interativo da skill: [`painel.html`](painel.html)
   - Ou execute a lógica do script [`scripts/calc_metricas.py`](scripts/calc_metricas.py):
     - **Pontaria (%):** `(Finalizações no Alvo / Finalizações Totais) * 100`
     - **Eficiência de Conversão (%):** `(Gols Marcados / Finalizações no Alvo) * 100`
     - **Estimativa de xG Simplificada:** ponderação de finalizações no alvo (~0.30 xG) e fora do alvo (~0.05 xG), caso o usuário não forneça dados avançados de coordenadas.

3. **Síntese Tática (Narrativa Estruturada):**
   - **Comportamento com a Bola:** Como o time que deteve a maior posse a utilizou (posse produtiva com infiltrações vs. posse estéril de passes laterais).
   - **Transições Rápidas e Contra-ataques:** Eficácia nas arrancadas e aproveitamento dos espaços deixados pelo adversário.
   - **Veredito de Justiça Estatística:** Concluir se o vencedor foi superior nas chances criadas ou se o resultado foi influenciado por eficácia isolada/desempenho de goleiros.

---

## 3. Padrão de Saída (Template)

A resposta deve ser formatada estritamente no seguinte padrão Markdown:

```markdown
# ⚽ Relatório Tático: [Time Mandante] [Placar A] x [Placar B] [Time Visitante]

### 📊 Painel Comparativo de Eficiência

| Métrica | [Time Mandante] | [Time Visitante] |
| :--- | :---: | :---: |
| **Posse de Bola** | X% | Y% |
| **Finalizações (No Alvo)** | X (A) | Y (B) |
| **Pontaria** | X% | Y% |
| **Eficiência de Conversão** | X% | Y% |
| **xG Estimado** | X.XX | Y.XX |

### 🔍 Diagnóstico Tático
- **Controle Territorial:** [Avaliação da ocupação de campo e posse]
- **Qualidade das Finalizações:** [Análise da periculosidade das chances]
- **Fase Defensiva:** [Comportamento na marcação e interceptações]

### ⚖️ Conclusão da Partida
[Síntese indicando se o resultado refletiu a produção ofensiva ou se decorreu de momentos isolados]
```

---

## 4. Fontes de Dados Homologadas

- Estatísticas oficiais das súmulas das federações (CBF, UEFA, CONMEBOL, FIFA).
- APIs esportivas públicas ou portais estatísticos de referência (ex.: Sofascore, WhoScored, FBref, ESPN Stats).
- **Aviso de Integridade:** Se algum dado específico (ex.: escanteios ou faltas) não tiver sido informado pelo usuário ou localizado nas fontes, o relatório deve marcar como `N/D` em vez de inventar números.

