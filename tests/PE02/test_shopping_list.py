import pytest
from shopping_list import main

def test_main_execution():
    try:
        main()
        execution_success = True
    except:
        execution_success = False

    assert execution_success
