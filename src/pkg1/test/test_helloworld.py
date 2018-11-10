from pkg1 import helloworld
import io

test_main_expected_output = """\
Hello, World!
"""


def test_main():
    output = io.StringIO()
    try:
        helloworld.main(output)
        assert test_main_expected_output == output.getvalue()
    finally:
        output.close()
