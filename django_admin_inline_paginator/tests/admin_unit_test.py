import unittest
from unittest.mock import Mock, MagicMock

import requests_mock
from django.contrib.admin.views.main import ChangeList

from django_admin_inline_paginator.admin import InlineChangeList, PaginationFormSetBase
from django_mock_queries.query import MockSet, MockModel


class TestInlineChangeList(unittest.TestCase):
    """Test cases for InlineChangeList admin"""
    def test_default_values(self):
        """Test case to check if the default was a value set"""
        self.assertEqual(InlineChangeList.can_show_all, True)
        self.assertEqual(InlineChangeList.multi_page, True)
        self.assertEqual(InlineChangeList.get_query_string, ChangeList.__dict__['get_query_string'])

    def test_init_values(self):
        """Test case for correct initialization class"""
        pass
    #     cl = InlineChangeList(request, page_num, paginator)
    #     cl.page_num = page_num
    #     cl.paginator = paginator
    #     cl.result_count = paginator.count

    #     cl.show_all = 'all' in request.GET
    #     cl.params = dict(request.GET.items())


class TestPaginationFormSetBase(unittest.TestCase):
    """Test cases for PaginationFormSetBase admin"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.qs = MockSet(
            MockModel(pk=1, mock_name='first'),
            MockModel(pk=2, mock_name='second'),
            MockModel(pk=3, mock_name='third'),
        )

    def test_default_values(self):
        """Test case to check if the default was a value set"""
        self.assertEqual(PaginationFormSetBase.queryset, None)
        self.assertEqual(PaginationFormSetBase.request, None)
        self.assertEqual(PaginationFormSetBase.per_page, 20)

    def test_get_page_num(self):
        """Test case to check correct getting page number"""
        pass

    def test_get_page(self):
        """Test case to check correct getting page"""
        pass

    def test_mount_paginator(self):
        """Test case for method mount_paginator"""
        pass

    @requests_mock.Mocker()
    def test_mount_paginator_unordered(self, mocked_request: Mock):
        """Test case for method mount_paginator with unordered QuerySet"""
        mocked_request.get('http://test.com')
        setattr(mocked_request, "GET", {"page": "1"})
        paginator_form_set = PaginationFormSetBase
        self.qs.order_by = MagicMock()
        setattr(paginator_form_set, "queryset", self.qs)
        setattr(paginator_form_set, "request", mocked_request)
        paginator_form_set()
        paginator_form_set.queryset.order_by.assert_called()

    def test_mount_queryset(self):
        """Test case for method mount_queryset"""
        pass

    def test_init(self):
        """Test case for correct initialization class"""
        pass
