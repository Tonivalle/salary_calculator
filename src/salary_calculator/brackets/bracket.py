from dataclasses import dataclass
from typing import Any


@dataclass
class TaxBracket:
    low: int
    high: int
    percentage: float

    def __contains__(self, item: Any) -> bool:
        return self.low < item <= self.high
