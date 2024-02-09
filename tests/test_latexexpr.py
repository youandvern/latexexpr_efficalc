from latexexpr_efficalc import Expression, Variable, Operation


def test_variable():
    v1 = Variable('H_{ello}', 3.25, 'm')
    assert str(v1) == 'H_{ello} =  3.25 \\ \\mathrm{m}'


def test_expression():
    v1 = Variable('H_{ello}', 3.25, 'm')
    v2 = Variable('W^{orld}', 5.63, 'm')
    e1 = Expression('E_{xample}', v1 + v2, 'm')
    assert str(e1) == 'E_{xample} = {H_{ello}} + {W^{orld}} =  3.25 \ \mathrm{m} +  5.63 \ \mathrm{m} =  8.88 \ \mathrm{m}'


def test_operation_with_rdiv_for_py3():
    v1 = Variable('H_{ello}', 3.25, 'm')
    v2 = Variable('W^{orld}', 5.63, 'm')
    e1 = Expression('E_{xample}', v1 + v2, 'm')
    o1 = (v1 - v2) / e1
    o2 = 2 / o1
    assert o1.strResult() == r'\left(-0.268\right)'
