# main.py

from engine import SymbolEngine

def main():
    engine = SymbolEngine()
    engine.run()
    print("Final State:")
    engine.display_state()

if __name__ == "__main__":
    main()