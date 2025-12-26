# Algorithmic Trading Strategies

This repository contains two independent algorithmic trading strategies, organized by team.  
Each team follows a different trading logic, allowing strategy comparison, experimentation, and performance evaluation.

---

## Team 1 – Strategy Description

**Objective:**  
Identify high-probability trade entries using technical indicators and trend confirmation, while maintaining strict risk management.

**Strategy Flow:**
1. Fetch historical and/or live market data (price, volume, OHLC)
2. Calculate technical indicators (e.g. Moving Averages, RSI, MACD)
3. Generate trade signals:
   - **Buy** when bullish conditions align
   - **Sell / Short** when bearish conditions align
4. Apply risk management:
   - predefined position sizing
   - stop-loss and take-profit levels
   - maximum loss per trade
5. Execute trades via exchange or broker API

**Use Case:**  
Trend-following or momentum-based trading in liquid markets.


## Team 2 – Strategy Description

**Objective:**  
Capture trading opportunities using an alternative market edge such as mean reversion, breakouts, or volatility-based setups.

**Strategy Flow:**
1. Collect market price data
2. Identify trading setups:
   - mean reversion from overbought/oversold levels
   - price breakouts from key support/resistance
   - volatility expansion or contraction patterns
3. Validate signals using filters (volume, time-based rules, market conditions)
4. Apply advanced risk controls:
   - dynamic stop-loss and trailing take-profit
   - trade cooldown to prevent overtrading
5. Execute and log trades for performance analysis

**Use Case:**  
Strategy diversification and comparison against Team 1’s approach.

---

## Risk Management (Common to Both Teams)

- Fixed or percentage-based position sizing
- Stop-loss on every trade
- Take-profit or trailing exit logic
- Maximum daily loss limit (optional)
- Trade logging for evaluation and backtesting

---
This project is for **educational and research purposes only**.  
It does not constitute financial advice. Use at your own risk.
