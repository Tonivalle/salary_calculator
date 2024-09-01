from dataclasses import dataclass
from typing import Any


@dataclass
class TaxBracket:
    """
    Represents a tax bracket.

    The salary between `low` and `high` gets taxed `percentage` amount.
    """

    low: int
    """
    Lowest amount included in this bracket (inclusive).
    """
    high: int
    """
    Highers amount in the bracket (exclusive).
    """
    percentage: float
    """
    Percentage of the salary in that bracket that is taken as taxes.
    """

    def __contains__(self, item: Any) -> bool:
        return self.low <= item < self.high
