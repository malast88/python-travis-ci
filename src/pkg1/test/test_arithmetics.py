from pkg1 import arithmetics
import io

test_main_1_input = """\
2
3"""

test_main_1_expected_output = """\
5
-1
6
"""


def test_main_1():
    test_output = io.StringIO()
    test_input = io.StringIO(test_main_1_input)
    try:
        arithmetics.main(test_input, test_output)
        assert test_main_1_expected_output == test_output.getvalue()
    finally:
        test_input.close()
        test_output.close()


test_main_2_input = """\
7
2"""

test_main_2_expected_output = """\
9
5
14
"""


def test_main_2():
    test_output = io.StringIO()
    test_input = io.StringIO(test_main_2_input)
    try:
        arithmetics.main(test_input, test_output)
        assert test_main_2_expected_output == test_output.getvalue()
    finally:
        test_input.close()
        test_output.close()
