# Multi-Source Sentiment Alpha Strategy

An automated trading algorithm that uses Natural Language Processing (NLP) to generate stock signals from financial news.


This strategy employs a **dual-model scoring system**:
1. **FinBERT (BERT-based):** Specialized transformer for financial context.
2. **NLTK VADER:** Lexicon-based fallback for robust headline scoring.

## 📈 Strategy Performance
- **Strategy Return:** 14.18%
- **Benchmark (SPY):** 20.74%
- **Current BUY Signals:** GS, MSFT, NVDA

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Transformers, PyTorch, NLTK, Pandas, YFinance
- **Environment:** Google Colab / Pro

## 🚀 Operational Logic
The algorithm fetches live news via NewsAPI, aggregates sentiment per ticker, and uses **Inverse Volatility Weighting** to construct a risk-parity portfolio.
