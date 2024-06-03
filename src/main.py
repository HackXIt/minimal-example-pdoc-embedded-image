import os

__doc__ = """
A minimal example to reproduce an issue with pdoc not displaying embedded images properly.

![software-bug JPEG](./assets/software-bug.jpg)
![software-bug PNG](./assets/software-bug.png)
"""

def main():
    """
    A minimal example to reproduce an issue with pdoc not displaying embedded images properly.

    ![software-bug JPEG](./assets/software-bug.jpg)
    ![software-bug PNG](./assets/software-bug.png)
    """
    print(__doc__)

if __name__ == '__main__':
    main()