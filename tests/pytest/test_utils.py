import vw._utils


def _get_stack_trace():
    return "\n".join(vw._utils.stack_trace())


def test__detection():
    assert vw._utils.is_test_env(), f"Test environment not detected - {_get_stack_trace()}."
