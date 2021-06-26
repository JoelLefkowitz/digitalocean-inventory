import os
import sys

sys.path.extend(
    [
        os.path.abspath(os.path.normpath(os.path.join(__file__, "..", *path)))
        for path in [(".."), ("..", "src")]
    ]
)
