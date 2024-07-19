import sys

import pytest

import plainish_renderer


def test_FileNotFoundError(capsys):
    plainish_renderer.getFile("this file doesnt exist.ptxt")
    captured = capsys.readouterr()
    expected = "File not found\n"
    assert expected == captured.out


def test_FileNotOfCorrectTypeError(capsys):
    plainish_renderer.getFile("Test-Texts/doesnotendwith.ptxt.whatever")
    captured = capsys.readouterr()
    expected = "File does not end with .ptxt. Require a .ptxt file\n"
    assert expected == captured.out

