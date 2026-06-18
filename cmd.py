# engine.py

import time

class SymbolEngine:
    def __init__(self):
        # Initialize symbol states
        self.symbols = {'.': 0, ',': 0, ':': 0}
        # History stream for tracking
        self.history = []

    def update_symbol(self, symbol):
        if symbol in self.symbols:
            self.symbols[symbol] += 1
            self.history.append(symbol)
            print(f"Updated '{symbol}': {self.symbols[symbol]}")
        else:
            print(f"Invalid symbol: {symbol}")

    def get_state(self):
        return self.symbols

    def get_history(self):
        return self.history

    def run(self):
        print("ayosoftalpha engine started.")
        print("Type '.', ',', ':' to update symbols. Type 'exit' to quit.")
        while True:
            user_input = input(">> ").strip()
            if user_input.lower() == 'exit':
                print("Exiting engine.")
                break
            elif user_input in self.symbols:
                self.update_symbol(user_input)
            else:
                print("Unknown input. Please type '.', ',', or ':'.")

    def display_state(self):
        print("Current symbol counts:")
        for symbol, count in self.symbols.items():
            print(f"{symbol}: {count}")
        print("History:", ''.join(self.history))