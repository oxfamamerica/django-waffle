from django.contrib import admin
from django.dispatch import receiver

from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from waffle.models import AbstractBaseFlag


class WaffleAdmin(ModelAdmin):
    model = AbstractBaseFlag 
    menu_label = "Waffle Flags"  
    menu_icon = "pick" 
    menu_order = 200 
    list_display = ("name","everyone", "percent", "testing", "rollout")
    list_filter = ("name",)
    search_fields = ("name",)

modeladmin_register(WaffleAdmin)


