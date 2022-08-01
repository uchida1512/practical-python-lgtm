# test_core.py はテスト用
import unittest


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())


# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ python -m unittest -v
# test_lgtm (tests.test_core.LgtmTest) ... ok
# ----------------------------------------------------------------------
# Ran 1 test in 0.015s
#
# OK