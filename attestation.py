import logging

logging.basicConfig(filename='calculator.log', level=logging.ERROR)

def recursive_calculator(expression):
    try:
        # реализация рекурсивного калькулятора
        pass
    except Exception as e:
        logging.error(f"Error in recursive_calculator: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Recursive Calculator")
    parser.add_argument("expression", type=str, help="Mathematical expression to evaluate")

    args = parser.parse_args()

    try:
        result = recursive_calculator(args.expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Error during command-line execution: {e}")

