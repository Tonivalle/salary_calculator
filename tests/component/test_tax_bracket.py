import pytest

from salary_calculator.brackets.bracket import TaxBracket


@pytest.mark.parametrize(
    ("low", "high", "number"),
    [
        (0, 12_450, 0),
        (0, 12_450, 50.5),
        (12_450, 24_000, 20_000),
    ],
)
def test_number_in_bracket(low, high, number):
    bracket = TaxBracket(low=low, high=high, percentage=0.2)

    assert number in bracket


@pytest.mark.parametrize(
    ("low", "high", "number"),
    [
        (0, 12_450, 20_000),
        (0, 12_450, 12_450),
        (12_450, 24_000, 0),
    ],
)
def test_number_not_in_bracket(low, high, number):
    bracket = TaxBracket(low=low, high=high, percentage=0.2)

    assert number not in bracket
