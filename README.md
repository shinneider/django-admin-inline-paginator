# Django Admin Inline Paginator

The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin

If you use or like the project, click `Star` and `Watch` to generate metrics and i evaluate project continuity.

# Install:

    pip install django-admin-inline-paginator

# Usage:

1. Add to your INSTALLED_APPS, in settings.py:

   ```
   INSTALLED_APPS = [
       ...
       'django_admin_inline_paginator',
       ...
   ]
   ```

1. Create your model inline:

   ```
   from django_admin_inline_paginator.admin import TabularInlinePaginated

   class ModelWithFKAdminInline(TabularInlinePaginated):
       fields = (...)
       per_page = 1
       model = ModelWithFK
   ```

1. Create main model admin and use inline:
   ```
   @register(YourModel)
   class YourModelAdmin(ModelAdmin):
       fields = (...)
       inlines = (ModelWithFKAdminInline, )
       model = YourModel
   ```
