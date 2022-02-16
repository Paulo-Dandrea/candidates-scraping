import pytest

from helpers import Candidate


def test_candidate_hygienizer():
    c1 = Candidate('  João  ', '  10  ', '/candidates-332.648.678-26')

    assert c1.get_cleaned_candidate(
    ) == {'name': 'joao', 'score': 10, 'cpf': '332.648.678-26'}

    c2 = Candidate('   ûBer Hängson    ', '  10.15  ',
                   '/candidates-332.648.678-26')
                   
    assert c2.get_cleaned_candidate(
    ) == {'name': 'uber hangson', 'score': 10.15, 'cpf': '332.648.678-26'}


def test_candidate_hygienizer_invalid_name():
    with pytest.raises(ValueError) as exp:
        Candidate(10, '10.15', '/candidates-332.648.678-26')

    assert str(exp.value) == 'Name must be a string'


def test_candidate_hygienizer_invalid_name():
    with pytest.raises(ValueError) as exp:
        Candidate('Paulo', 15, '/candidates-332.648.678-26')

    assert str(exp.value) == 'Score must come as string first'
