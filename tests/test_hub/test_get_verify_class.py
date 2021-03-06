from __future__ import absolute_import
import hashlib
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import kojihub
from koji import GenericError
from koji.util import adler32_constructor


class TestGetVerifyClass(unittest.TestCase):

    def test_get_verify_class_generic_error(self):
        with self.assertRaises(GenericError):
            kojihub.get_verify_class('not_a_real_value')

    def test_get_verify_class_is_none(self):
        kojihub.get_verify_class(None) is None

    def test_get_verify_class_is_md5(self):
        kojihub.get_verify_class('md5') is hashlib.md5

    def test_get_verify_class_is_adler32(self):
        kojihub.get_verify_class('adler32') is adler32_constructor
