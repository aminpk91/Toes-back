from django.db import models
from Utils.Image_dir import model_image_directory_path, Subject_image_directory_path
from django.utils.translation import gettext as _


class Subjects(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن کامل پست')
    Photo = models.ImageField(upload_to=Subject_image_directory_path, verbose_name='عکس', null=True, default=None)
    active = models.BooleanField(default=False, verbose_name='فعال یا غیر فعال بودن')
    index_sidebar = models.BooleanField(default=False, verbose_name='نمایش در ساید بار (صفحه اول )')
    post_page = models.BooleanField(default=False, verbose_name='نمایش در پست ها(وب لاگ)')
    product = models.BooleanField(default=False, verbose_name='نمایش در لیست محصولات')

    class Meta:
        verbose_name = _('موضوع')
        verbose_name_plural = _('موضوعات')

    def __str__(self):
        return self.title


class Photo(models.Model):
    related_title = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='عنوان مرتبط با عکس')
    image = models.ImageField(upload_to=model_image_directory_path, verbose_name='عکس')

    class Meta:
        verbose_name = _('عکس')
        verbose_name_plural = _('عکس ها')

    def __str__(self):
        return self.related_title.__str__()
