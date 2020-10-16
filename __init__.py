import sys


PY37 = sys.version_info >= (3, 7)
PY38 = sys.version_info >= (3, 8)

if not PY37:
    from pep562 import Pep562

    Pep562(__name__)
