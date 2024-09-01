from pathlib import Path

from ..bracket import TaxBracket


class BaseBracketReader:
    def read(self, filepath: Path) -> list[TaxBracket]:
        raise NotImplementedError
