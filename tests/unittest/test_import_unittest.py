import io
import unittest
from contextlib import redirect_stdout

import vw


@vw.tests_only
def method_that_prints__with_tests_only():
    print("Hello, world!")


@vw.no_op
def method_that_prints__with_no_op():
    print("Hello, world!")


class TestImports(unittest.TestCase):
    """Test class for import cases."""

    def test__no_op(self):
        f = io.StringIO()
        with redirect_stdout(f):
            method_that_prints__with_no_op()

        output = f.getvalue()
        self.assertEqual(output, "")

    def test__tests_only(self):
        f = io.StringIO()
        with redirect_stdout(f):
            method_that_prints__with_tests_only()

        output = f.getvalue()
        self.assertEqual(output, "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
