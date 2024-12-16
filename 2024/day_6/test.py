from collections.abc import Iterable
from dataclasses import dataclass
from typing import override

@dataclass
class Point(Iterable):
    x: int
    y: int

    @override
    def __iter__(self):
        for val in (self.x, self.y):
            yield val

p = Point(1, 2)
print(p)
x, y = p
print(x, y)
