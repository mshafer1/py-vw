import pytest

import vw


@vw.lazy.tests_only
def method_that_prints__with_tests_only():
    print("Hello, world!")


@vw.lazy.no_op
def method_that_prints__with_no_op():
    print("Hello, world!")


def test__no_op(capsys: pytest.CaptureFixture):
    method_that_prints__with_no_op()

    captured = capsys.readouterr()
    assert captured.out == ""


def test__tests_only(capsys: pytest.CaptureFixture):
    method_that_prints__with_tests_only()

    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
