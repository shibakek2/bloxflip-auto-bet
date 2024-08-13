# Bloxflip Auto Bet Script

## Overview

This Python script automates betting on the Bloxflip platform. It fetches your current balance and places bets with a specified amount at regular intervals. It supports various response encodings and provides error handling for different API responses.

## Features

- Fetches current balance from the Bloxflip API.
- Places bets with a specified amount.
- Supports gzip, deflate, and Brotli encodings.
- Provides detailed error handling and messages.

## Requirements

- Python 3.6 or higher
- `requests` library
- `brotlicffi` library
- `zlib` library (usually included with Python)

Install the required Python libraries using pip:

```bash
pip install requests brotlicffi
```

## Configuration
API Tokens
Before running the script, you need to configure your API tokens. Open the script file and set your API tokens as follows:


```python
token = "YOUR_API_TOKEN" # Replace with your Bloxflip API token
```
```python
xtoken = "YOUR_CSRF_TOKEN" # Replace with your CSRF token
```

## Script Parameters
- `bet_amount`: This is the amount to bet each time the script places a bet. You will be prompted to input this amount when you start the script.

## Adjusting Parameters
You may want to adjust the following parameters based on your needs:

time.sleep(15): The interval between bets (in seconds). Adjust this value if you want to place bets more or less frequently.


## Usage
Clone this repository to your local machine:

Copy code
git clone https://github.com/shibakek2/bloxflip-auto-bet.git
cd bloxflip-auto-bet
