from latexexpr_efficalc import Variable


def test_none_value():
    assert Variable("a", None).value is None
    assert Variable("a", None).isSymbolic() is True
    assert Variable("a", None).strResult() == "{a}"
    assert Variable("a", None).strSymbolic() == "{a}"


def test_result():
    assert Variable("a", 0).result() == 0.0
    assert Variable("a", 3.9, "in").result() == 3.9
    assert Variable("a", 10 ** 9, "in").result() == 10 ** 9


def test_str_result():
    assert Variable("a", 0).strResult() == " 0"
    assert Variable("a", 3.9, "in").strResult() == " 3.9"
    assert Variable("a", 10 ** 9, "in").strResult() == " 1000000000"


def test_str_result_with_unit():
    assert Variable("a", 0).strResultWithUnit() == " 0 \ \mathrm{}"
    assert Variable("a", 3.9, "in").strResultWithUnit() == " 3.9 \ \mathrm{in}"
    assert Variable("a", 10 ** 9, "m^2").strResultWithUnit() == " 1000000000 \ \mathrm{m^2}"


def test_str_symbolic():
    assert Variable("a", 0).strSymbolic() == "{a}"
    assert Variable("a_2", 3.9, "in").strSymbolic() == "{a_2}"
    assert Variable("a_{ref}", 10 ** 9, "m^2").strSymbolic() == "{a_{ref}}"


def test_str_substituted():
    assert Variable("a", 0).strResultWithUnit() == " 0 \ \mathrm{}"
    assert Variable("a", 3.9, "in").strResultWithUnit() == " 3.9 \ \mathrm{in}"
    assert Variable("a", 10 ** 9, "m^2").strResultWithUnit() == " 1000000000 \ \mathrm{m^2}"


def test_number_format():
    assert Variable("a", 0.0000000).strResult() == " 0"
    assert Variable("a", 3.987654321, "in").strResult() == " 3.988"
    assert Variable("a", 123456789.123456, "in").strResult() == " 123456789"
