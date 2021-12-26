Django Admin Inline Paginator
=============================

The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin

If you use or like the project, click `Star` and `Watch` to generate metrics and i evaluate project continuity.

# Install:

```
pip install django-admin-inline-paginator
```

# Usage:

1. Add to your INSTALLED_APPS, in settings.py:

   ```
   INSTALLED_APPS = [
       ...
       'django_admin_inline_paginator',
       ...
   ]
   ```
2. Create your model inline:

   ```
   from django_admin_inline_paginator.admin import TabularInlinePaginated

   class ModelWithFKAdminInline(TabularInlinePaginated):
       fields = (...)
       per_page = 1
       model = ModelWithFK
   ```
3. Create main model admin and use inline:

    ```
    @register(YourModel)
    class YourModelAdmin(ModelAdmin):
        fields = (...)
        inlines = (ModelWithFKAdminInline, )
        model = YourModel
    ```

# Advanced Usage:

1. Paginate multiples inlines:
    
    ```
    class ModelWithFKInline(TabularInlinePaginated):
    fields = ('name', 'active')
    per_page = 2
    model = ModelWithFK
    pagination_key = 'page-model'  # make sure it's unique for page inline

    class AnotherModelWithFKInline(TabularInlinePaginated):
    fields = ('name', 'active')
    per_page = 2
    model = AnotherModelWithFK
    pagination_key = 'page-another-model'  # make sure it's unique for page inline
    ```

2. Use previous inlines
    
    ```
    @register(YourModel)
    class YourModelAdmin(ModelAdmin):
        fields = (...)
        inlines = (ModelWithFKAdminInline, AnotherModelWithFKInline)
        model = YourModel
    ```

# Images:

![image](https://user-images.githubusercontent.com/30196992/98023167-706ca880-1dfe-11eb-89fe-c056741f0d5b.png)

# Need a Maintainer
 In the last months i don't have much time, health problemas, change of country and others problems.  
 i have some surgeries for first part of 2022, and all of my current project don't use django-admin.  
 for these reasons, i need a help for a project continuation!!
