from pathlib import Path

from salary_calculator.brackets.bracket import TaxBracket
from salary_calculator.brackets.reader.yaml import YamlBracketReader


def test_brackets_yml_reader():
    reader = YamlBracketReader()
    filepath = Path(__file__).parent / "resources/sample.yml"

    brackets = reader.read(filepath)

    assert brackets == [TaxBracket(0, 100, 0.2), TaxBracket(100, 200, 0.2)]
