# Currency Converter Desktop App

This is a desktop app built with Python and `tkinter`  
that library is designed for creating GUI in Python.  
Also, this app uses `ExchangeRate-API` - free API  
that makes it possible to convert currencies.

## Features
- Convert one currency to another
- All currencies in the world
- Quick qurrency search

## Conditions
- Python 3.6 and above versions installed on your PC
- API token. You can get it for free without card details [ExchangeRate-API](https://www.exchangerate-api.com/)

## Getting Started

1. **Clone this repository:**
    ```bash
   git clone https://github.com/JuicingNow/Converter-App.git

2. **Install dependencies:**
    ```bash
   cd converter
   pip install requests
   pip install python-dotenv

3. **Create `.env` file:**  
   Create a `.env` file in the root directory of the project.
   This file will store your API key.  
   Open the `.env` file and add the following line:  
   `API_KEY = "<YOUR_API_KEY>""`

4. **Start the app:**

   ```bash
   python main.py