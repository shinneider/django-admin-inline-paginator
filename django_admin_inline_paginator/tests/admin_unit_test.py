import unittest
from django.contrib.admin.views.main import ChangeList

from django_admin_inline_paginator.admin import InlineChangeList, PaginationFormSetBase, PaginationInline


class TestInlineChangeList(unittest.TestCase):

    def test_default_values(self):
        self.assertEqual(InlineChangeList.can_show_all, True)
        self.assertEqual(InlineChangeList.multi_page, True)
        self.assertEqual(InlineChangeList.get_query_string, ChangeList.__dict__['get_query_string'])

    def test_init_values(self):
        pass
    #     cl = InlineChangeList(request, page_num, paginator)
    #     cl.page_num = page_num
    #     cl.paginator = paginator
    #     cl.result_count = paginator.count

    #     cl.show_all = 'all' in request.GET
    #     cl.params = dict(request.GET.items())


class TestPaginationFormSetBase(unittest.TestCase):

    def test_default_values(self):
        self.assertEqual(PaginationFormSetBase.queryset, None)
        self.assertEqual(PaginationFormSetBase.request, None)
        self.assertEqual(PaginationFormSetBase.per_page, 20)

    def test_get_page_num(self):
        pass

    def test_get_page(self):
        pass

    def test_mount_paginator(self):
        pass

    def test_mount_queryset(self):
        pass

    def test_init(self):
        pass


class TestPaginationInline(unittest.TestCase):

    def test_default_values(self):
        self.assertEqual(PaginationInline.template, 'admin/edit_inline/tabular_paginated.html')
        self.assertEqual(PaginationInline.per_page, 20)
        self.assertEqual(PaginationInline.extra, 0)
        self.assertEqual(PaginationInline.can_delete, False)

    def test_get_formset(self):
        pass
