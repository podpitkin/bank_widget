import pytest
from src.widget import mask_account_card
from widget import get_date


@pytest.mark.parametrize("bank_name, expected",[
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361")
])
def test_mask_bank(bank_name, expected):
    assert mask_account_card(bank_name) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"