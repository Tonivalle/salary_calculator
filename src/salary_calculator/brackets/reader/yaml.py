from pathlib import Path

import yaml

from salary_calculator.brackets.bracket import TaxBracket

from .base import BaseBracketReader

DEFAULT_LOADER = yaml.SafeLoader


class YamlBracketReader(BaseBracketReader):
    def read(self, filepath: Path) -> list[TaxBracket]:
        parsed_yml = self._read_yaml(filepath)
        return [
            TaxBracket(low=bracket["low"], high=bracket["high"], percentage=bracket["percentage"])
            for bracket in parsed_yml["brackets"]
        ]

    def _read_yaml(self, filepath):
        with open(filepath, "r") as file:
            return yaml.load(file, Loader=DEFAULT_LOADER)
