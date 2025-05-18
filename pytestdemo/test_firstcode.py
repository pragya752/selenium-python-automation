import pytest

@pytest.mark.smoke
def test_fisrtmethod():
    msg="hello"
    assert msg== "hii","test failed string do not match"

@pytest.mark.skip
def test_secondmethod():
    a=2
    b=5
    assert a+4==6, "addition not matched"


