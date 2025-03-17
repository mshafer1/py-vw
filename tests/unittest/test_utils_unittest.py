import unittest

import vw._utils


def _get_stack_trace():
    return "\n".join(vw._utils.stack_trace())


class TestUtils(unittest.TestCase):
    """Unittest based testing of the utils module."""

    def test__detection(self):
        self.assertTrue(
            vw._utils.is_test_env(), msg=f"Test environment not detected - {_get_stack_trace()}."
        )
