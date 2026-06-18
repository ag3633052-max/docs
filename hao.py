# engine.py

import time

class SymbolEngine:
    def __init__(self):
        # Initialize symbol states
        self.symbols = {'.': 0, ',': 0, ':': 0}
        # History stream for tracking
        self.history = []
        # Perturbation pattern based on binary sequence
        self.perturb_pattern = '011011011011'
        self.perturb_index = 0

    def update_symbol(self, symbol):
        if symbol in self.symbols:
            self.symbols[symbol] += 1
            self.history.append(symbol)
            print(f"Updated '{symbol}': {self.symbols[symbol]}")
        else:
            print(f"Invalid symbol: {symbol}")

    def apply_perturbation(self):
        """
        Apply permutation rotation based on the binary pattern.
        This will simulate admin control over mod cycles.
        """
        # Rotate through perturb pattern
        pattern_char = self.perturb_pattern[self.perturb_index]
        self.perturb_index = (self.perturb_index + 1) % len(self.perturb_pattern)

        # If pattern bit is '1', perform a perturbation
        if pattern_char == '1':
            # Example perturbation: add 1 to each symbol count
            for key in self.symbols:
                self.symbols[key] += 1
            print("Perturbation applied based on pattern.")
        else:
            print("No perturbation this cycle.")

    def get_state(self):
        return self.symbols

    def get_history(self):
        return self.history

    def run(self):
        print("ayosoftalpha engine started.")
        print("Type '.', ',', ':' to update symbols.")
        print("Type 'perturb' to apply admin perturbation.")
        print("Type 'exit' to quit.")
        while True:
            user_input = input(">> ").strip()
            if user_input.lower() == 'exit':
                print("Exiting engine.")
                break
            elif user_input.lower() == 'perturb':
                self.apply_perturbation()
            elif user_input in self.symbols:
                self.update_symbol(user_input)
            else:
                print("Unknown input. Please type '.', ',', ':', or 'perturb'.")

    def display_state(self):
        print("Current symbol counts:")
        for symbol, count in self.symbols.items():
            print(f"{symbol}: {count}")
        print("History:", ''.join(self.history))