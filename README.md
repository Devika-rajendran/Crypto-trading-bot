# Crypto Trading Bot

## Description
This project is a Python-based **Crypto Trading Bot** developed as part of the *Junior Python Developer – Crypto Trading Bot* assignment.  
The goal of the project is to design and implement the core structure of a trading bot that can interact with a cryptocurrency exchange, execute trades based on predefined strategies, and maintain proper logging.

Due to an issue with **API key creation on the exchange platform**, live trading execution could not be fully completed. However, the application architecture, strategy logic, and logging workflow are implemented and ready for live testing once valid API keys are available.

---

## Project Scope
- Design a modular and readable trading bot structure
- Prepare the system for exchange API integration
- Implement strategy-based order execution logic
- Log trading activity and errors for monitoring and debugging
- Follow secure coding practices by excluding sensitive credentials

---

## Key Features
- Modular Python codebase
- Strategy-ready design (Market / TWAP logic)
- Centralized logging for bot activity and errors
- Configuration-based setup for API credentials
- Secure handling of sensitive data (no hardcoded keys)

---

## Technologies Used
- Python 3
- Streamlit (for UI and visualization)
- REST API–based exchange integration (design-ready)
- Python logging module
- Git and GitHub for version control

---

## Project Structure
crypto-trading-bot/
├── bot.py              # Core trading bot logic
├── cli.py              # Command-line interface to run the bot
├── strategies.py       # Trading strategies (Market / TWAP logic)
├── logger.py           # Centralized logging configuration
├── ui.py               # Streamlit-based user interface
├── logs/
│   └── bot.log         # Bot execution logs (shared separately if required)
├── README.md           # Project documentation
└── .gitignore          # Ignored files and sensitive data


---

## Limitation
Live order placement could not be tested because **API key creation was unsuccessful on the exchange platform** during development.  
No API keys are included in this repository for security reasons.

Once valid API credentials are provided, the bot can be connected to the exchange without major code changes.

---


