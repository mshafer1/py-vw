"""This file exists for running validation outside of a test framework."""

import io
from contextlib import redirect_stdout

import vw


@vw.no_op
def method_that_prints_with_no_op():
    """Test method that prints but is decorated to no-op under test environments."""
    print("Hello!")


@vw.tests_only
def method_that_prints_with_tests_only():
    """Test method that prints but is decorated to only operate under test environments."""
    print("Hello!")


def validate_no_op():
    """Validate the no_op decorator."""
    # method_that_prints_with_no_op()
    f = io.StringIO()
    with redirect_stdout(f):
        method_that_prints_with_no_op()

    output = f.getvalue()
    assert output == "Hello!\n", (
        f"Error, it should have printed. "
        f"Got:\n{output}\nVW thinks it is test mode: {vw.is_test_env()}. "
        "Stack trace is below:\n" + ("\n".join(vw._utils.stack_trace()))
    )


def validate_tests_only():
    """Validate the tests_only."""
    f = io.StringIO()
    with redirect_stdout(f):
        method_that_prints_with_tests_only()

    output = f.getvalue()
    assert output == ""


if __name__ == "__main__":
    validate_no_op()
    validate_tests_only()
    print("Validation passed.")
