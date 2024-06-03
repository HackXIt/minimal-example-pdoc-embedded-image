import os

__doc__ = """
A minimal example to reproduce an issue with pdoc not displaying embedded images properly.

**path written relative to the current file:**
![software-bug JPEG](../assets/software-bug.jpg)

**path written from the perspective of the root folder:**
![software-bug JPEG](./docs/assets/software-bug.jpg)
"""

def main():
    """
    A minimal example to reproduce an issue with pdoc not displaying embedded images properly.

    **path written relative to the current file:**
    ![software-bug JPEG](../assets/software-bug.jpg)

    **path written from the perspective of the root folder:**
    ![software-bug JPEG](./docs/assets/software-bug.jpg)
    """
    print(__doc__)

if __name__ == '__main__':
    main()