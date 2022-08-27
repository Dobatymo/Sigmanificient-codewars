"""Kata url: https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e."""


def encode(string: str) -> str:
    return ''.join(
        ''.join(c * 3 for c in f'{ord(char):0>8b}')
        for char in string
    )


def decode(bits: str) -> str:
    bits = ''.join(
        '01'[bits[i:i + 3].count('1') > 1]
        for i in range(0, len(bits), 3)
    )

    return ''.join(
        chr(int(bits[i:i + 8], 2))
        for i in range(0, len(bits), 8)
    )


def test_encode():
    assert encode("hey") == (
        "0001111110001110000000000001111110000001110001110001111111111110000001"
        "11"
    )

    assert encode("The Sensei told me that i can do this kata") == (
        "0001110001110001110000000001111110001110000000000001111110000001110001"
        "1100000011100000000000000000011100011100000011111100011111100000011100"
        "0111000111111000111111111000000111111111000000111111000111111000000111"
        "0001110001111110001110000001110000001110000000000000000001111111110001"
        "1100000000011111100011111111111100011111100011111100000000011111100000"
        "0111000000000000111000000000000000000111111000111111000111000111111000"
        "0001110001110000001110000000000000000001111111110001110000000001111110"
        "0011100000000000011111100000000000011100011111111100011100000000000011"
        "1000000000000000000111111000111000000111000000111000000000000000000111"
        "1110000000001111110001111110000000000001110001111110001111111110000000"
        "0011100000000000000000011111100000011100000000011111100011111111111100"
        "0000111000000000000000000111111111000111000000000111111000111000000000"
        "0001111110001110000001110001111111110000001111110000001110000000000000"
        "0000011111100011100011111100011111100000000000011100011111111100011100"
        "0000000111111000000000000111"
    )

    assert encode("T3st") == (
        "0001110001110001110000000000001111110000001111110001111111110000001111"
        "11000111111111000111000000"
    )
    assert encode("T?st!%") == (
        "0001110001110001110000000000001111111111111111110001111111110000001111"
        "1100011111111100011100000000000011100000000000011100000011100000011100"
        "0111"
    )


def tests_decode():
    assert decode(
        "1001111110001110010000100001111110000001110011110001111101101110000101"
        "11"
    ) == "hey"

    assert decode(
        "0001110001110001110001000001111110001110000010000001111110000101110001"
        "1100010011100000000000010000011100011100000011111100011111100000011100"
        "0111000111111000111111111000000111111111000000111111000110111000000111"
        "0001110001111110001110000001110000001110000000000000000001111111110001"
        "1100000000011111100011111111111100011111100011111100000000011111100000"
        "0111000001000000111000000000001000000111111000111111000111000111111000"
        "0001110001110000001110000000000000000001111111110001110000000001111110"
        "0011100000000000011111100000001000011100011111111100011100000000010011"
        "1000000000000000000111111000111000000111000000111000000000000000000111"
        "1110000000001111110001111110000000000001110001111110001111111110000000"
        "0011100000000000001000011111100000011100000000011111100011111111011100"
        "0000111000000000000000000111111111000111000000000111111000111000000000"
        "0001111110001110000001110001111111110000001111110000001110000000000000"
        "0000011111100011100011111100011111100000000000011100011111111100011100"
        "0000000111111000000000000111"
    ) == "The Sensei told me that i can do this kata"

    assert decode(
        "0001110001110001110000100000001111110000001111110001111111110000001111"
        "11000111111111000111010000"
    ) == "T3st"

    assert decode(
        "0001110001110001110000010000001111111101111111110001111111110000001111"
        "1100011111111100011100000000000011100000000000011100000011100000011100"
        "0111"
    ) == "T?st!%"