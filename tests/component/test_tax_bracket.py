from salary_calculator.brackets.bracket import TaxBracket


def test_number_in_tax_bracket():
    bracket = TaxBracket(0, 12.450, 0.2)

    assert 1 in bracket
