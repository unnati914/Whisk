import argparse
from .interpreter import Interpreter


def main():
    parser = argparse.ArgumentParser(description="Run a Whisk .fun file")
    parser.add_argument("file", help="Path to .fun file")
    parser.add_argument("--mood", default="default", help="Choose a mood: chill, clingy, sassy")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        code = f.read()

    interp = Interpreter(mood=args.mood)
    interp.check_time()
    interp.run(code)


if __name__ == "__main__":
    main()
