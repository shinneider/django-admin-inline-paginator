import unittest
from django_admin_inline_paginator.meta import VERSION


class TestMetaFormat(unittest.TestCase):

    def test_version_format(self):
        """
            This project use format major.minor.patch
        """
        ver = str(VERSION).split('.')
        self.assertEqual(isinstance(ver, list), True)
        self.assertEqual(len(ver), 3)
        self.assertEqual(all([x.isnumeric() for x in ver]), True)
