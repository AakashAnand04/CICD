import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.maths_operation import add


def test():
    assert add(4, 9) == 13
    assert add(-1, 1) == 0
    print("All tests passed!")


if __name__ == "__main__":
    test()
