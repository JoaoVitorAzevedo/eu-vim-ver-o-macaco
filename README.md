# 🐒 Eu Vim Ver o Macaco
### Análise Comparativa das Estratégias de Investimento mais Primatas Existentes

Neste projeto, utilizamos ciência de dados (e um pouco de loucura) para testar se um macaco jogando dardos realmente performa melhor que o investidor médio da Faria Lima. 

O objetivo é simular frameworks de "Stock Picking" que variam do puramente aleatório ao "pseudo-lógico" que todo iniciante já tentou uma vez.

---

## 📋 Quadro de Atividades (Kanban)

| Estratégia | Status | Descrição Curta |
| :--- | :---: | :--- |
| **🐒 Estratégia Macaco** | ✅ Finalizado | Puro caos e aleatoriedade (Random Walk). |
| **🔮 A Vidente** | ⏳ Aguardando | Probabilidade inversa à liquidez. |
| **🤡 O Pseudoholder** | ⏳ Aguardando | "Só é prejuízo se eu vender". |
| **👴 Warren Bufê** | ⏳ Aguardando | Valor e Renda Fixa (o benchmark racional). |
| **🚀 Geração Z** | ⏳ Aguardando | FOMO e reserva de emergência no IPO. |
| **🔫 38tão** | ⏳ Aguardando | 100% Bitcoin, o resto é o Diabo. |
| **🦈 Barsi, o Tubarão** | ⏳ Aguardando | Dividend Yield acima de tudo. |
| **💃 Xibom Bombom** | ⏳ Aguardando | "O de cima sobe e o de baixo desce". |
| **📉 Agregador de Loss** | ⏳ Aguardando | Se caiu 15% hoje, tá "barato". |
| **♎ Horóscopo Trader** | ⏳ Aguardando | Stock picking baseado no signo do CEO. |
| **🍺 Dica do Churrasco** | ⏳ Aguardando | O que o seu tio rico falou depois da 3ª Skol. |

---

## 🛠️ Detalhamento das Estratégias

### ✅ 🐒 Estratégia Macaco (The OG)
O macaco joga dardos em uma lista de ativos do IBOV e fica com os 5-10 que acertar primeiro. Sem viés, sem DRE, sem choro.

### 🔮 A Vidente
Seleciona ativos aleatoriamente, mas com peso maior para empresas com **baixíssima liquidez**. Se escolher uma empresa que ninguém conhece e ela subir, foi "visão". Se for PETR4, foi sorte.

### 🤡 Calma cara, deixa voltar pelo menos no meu preço médio (O Pseudoholder)
Seleciona 22 ativos (o número mágico do YouTube). Se um ativo cai 50%, ele não vende porque "o fundamento não mudou" (mesmo sem saber o que é um fundamento). Morre com a ação a R$ 0,00 mas morre com dignidade.

### 🔫 38tão (The Maximalist)
Ignora o mercado de ações. O framework consiste em ignorar o input `ALL_TICKERS` e comprar 100% em Bitcoin. "Você quer ser dependente ou independente? Hein!?".

### 📉 Agregador de Loss
Focado em "faca caindo". O algoritmo busca as 5 maiores quedas do último mês e aposta tudo nelas. "Uma hora tem que subir" é o lema oficial.

### ♎ Horóscopo Trader
Cruza a data de fundação da empresa (ou IPO) com o mapa astral do dia. Não investe em empresas de Mercúrio Retrógrado. 

### 🍺 Dica do Churrasco
Simula um modelo de "ruído". Seleciona ativos que tiveram picos de menções em redes sociais ou fóruns duvidosos nas últimas 48 horas.

---

## 🚀 Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o simulador:
   ```bash
   python main.py
   ```

## 📈 Roadmap de Implementação
- [x] Script base com integração `yfinance`.
- [x] Métricas básicas (Sharpe, Volatilidade, Retorno).
- [ ] Implementar motor de backtest para múltiplas estratégias simultâneas.
- [ ] Adicionar suporte a ativos brasileiros e americanos.
- [ ] Gerar gráficos comparativos (Macaco vs IBOV vs CDI).

---
*Disclaimer: Este projeto é puramente educacional e humorístico. Não siga as dicas do seu tio, nem do macaco, nem deste script.*
