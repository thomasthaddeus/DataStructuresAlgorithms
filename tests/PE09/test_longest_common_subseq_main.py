import pytest
from longest_common_subseq_main import main
from longest_common_subseq import LCSClass

def test_LCSClass():
    lcs = LCSClass()

    assert lcs.find("abccefa", "abca") == 4
    assert lcs.find("abcdef", "adf") == 3
    assert lcs.find("aeebbefc", "ebcf") == 4
    assert lcs.find("asdf", "vc") == 0

def test_main(capsys):
    main()
    captured = capsys.readouterr()

    assert "LCS length: 3\n" in captured.out
    assert "LCS length: 4\n" in captured.out
    assert "LCS length: 0\n" in captured.out
