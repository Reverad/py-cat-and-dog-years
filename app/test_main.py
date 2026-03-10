import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="cat & dog ages = 0"
        ),
        pytest.param(
            14, 15, [0, 1],
            id="cat/dog ages = 14/15"
        ),
        pytest.param(
            24, 23, [2, 1],
            id="cat & dog ages = 24/23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="cat & dog ages = 28/28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="cat & dog ages = 100/100"
        )
    ]
)
def test_get_human_age(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result
