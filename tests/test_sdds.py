from eleganttools import SDDS


def test_as_dict(demo_sdds):
    dct = SDDS(demo_sdds).as_dict()
    assert dct["ShortP"] == 1
    assert dct["CharacterP"] == "a"


def test_as_dataframe(demo_sdds):
    df = SDDS(demo_sdds).as_dict()
    assert df["ShortP"] == 1
    assert df["CharacterP"] == "a"
