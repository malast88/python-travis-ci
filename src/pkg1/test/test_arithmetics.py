from pkg1 import arithmetics
import io

def test_main_1():
    output = io.StringIO()
    input = io.StringIO("2\n3")
    try:
        arithmetics.main(input, output)
        assert "5\n-1\n6\n" == output.getvalue()
    finally:
        input.close()
        output.close()

def test_main_2():
    output = io.StringIO()
    input = io.StringIO("7\n2")
    try:
        arithmetics.main(input, output)
        assert "9\n5\n14\n" == output.getvalue()
    finally:
        input.close()
        output.close()