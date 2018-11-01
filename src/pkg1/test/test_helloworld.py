from pkg1 import helloworld
import io

def test_main():
    output = io.StringIO()
    try:
        helloworld.main(output)
        assert "Hello, World!\n" == output.getvalue()
    finally:
        output.close()