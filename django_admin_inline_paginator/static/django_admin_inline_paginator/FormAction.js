//Script for cleaning action attr in form for Django-inline -paginator.
<script>
  (function ($) {
    $('form').removeAttr('action');
  })(django.jQuery);
</script>