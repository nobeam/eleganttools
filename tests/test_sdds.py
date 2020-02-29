from eleganttools import sdds


def test_as_dict(demo_sdds):
    dct = sdds.as_dict(demo_sdds)
    assert dct["ShortPA"] == 1
    assert dct["CharacterP"] == "a"


def test_as_dataframe(demo_sdds):
    df = sdds.as_dataframe(demo_sdds)
    assert df.ShortPA == 1
    assert df.CharacterP == "a"
