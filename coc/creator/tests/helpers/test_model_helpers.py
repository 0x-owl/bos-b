from creator.helpers.model_helpers import renamer, roller_stats
from creator.tests.helpers.constants import FILE_NAME, FakePortrait, Portrait


def test_renamer_investigator_positive():
    result = renamer(Portrait(), FILE_NAME)
    assert 'testinvestigatoruuid' in result

def test_renamer_investigator_negative():
    result = renamer(FakePortrait(), FILE_NAME)
    assert 'testinvestigatoruuid' not in result

def test_renamer_item_positive():
    result = renamer(FakePortrait(), FILE_NAME)
    assert 'testitemuuid' in result

def test_renamer_item_negative():
    result = renamer(Portrait(), FILE_NAME)
    assert 'testitemuuid' not in result

def test_roller_stats_positive():
    result = roller_stats(2)
    assert result % 5 == 0

def test_roller_stats_arguments_negative():
    try:
        roller_stats('test')
    except TypeError:
        pass
    else:
        assert False

