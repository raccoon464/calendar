import datetime
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponseRedirect
# from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
# from rest_framework_simplejwt.tokens import RefreshToken, Token
# from rest_framework_simplejwt.utils import datetime_from_epoch

from authentication.models import User, UserAvatar, UserSession, UserInteresting


class UserAvatarTabularInline(admin.TabularInline):
    model = UserAvatar


class UserSessionTabularInline(admin.TabularInline):
    model = UserSession


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserAvatarTabularInline, UserSessionTabularInline)
    fieldsets = (
        (
            "Personal",
            {
                "fields": (
                    "password",
                    "username",
                    "profile_username",
                    "birth_date",
                    "email",
                    "telegram_username",
                    "telegram_id",
                    "language_code",
                    "is_dark_theme",
                    "is_banned",
                    "is_paid",
                )
            },
        ),
        # (
        #     "Permissions",
        #     {
        #         "fields": (
        #             "is_active",
        #             "is_staff",
        #             "is_superuser",
        #             "is_tg_admin_mode",
        #             "is_account_activated",
        #             "groups",
        #             "user_permissions",
        #         ),
        #     },
        # ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "telegram_username",
                ),
            },
        ),
    )
    readonly_fields = ("last_login", "date_joined")

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not hasattr(instance, "created_by"):
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()

    def get_form(self, request, obj=None, **kwargs):
        # Disabled the ability for non-superusers to edit their own permissions
        # source: https://webdevblog.ru/chto-nuzhno-znat-chtoby-upravlyat-polzovatelyami-v-django-admin/
        form = super().get_form(request, obj, **kwargs)

        form.base_fields['email'].required = False
        form.base_fields['telegram_username'].required = False

        if not request.user.is_superuser:
            form.base_fields["is_staff"].disabled = True
            form.base_fields["is_superuser"].disabled = True
            form.base_fields["groups"].disabled = True
            form.base_fields["user_permissions"].disabled = True

        return form


# class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):
#     def has_add_permission(self, *args, **kwargs):
#         return True
#
#     def get_readonly_fields(self, *args, **kwargs):
#         return ["jti", "token", "created_at", "expires_at"]
#
#     def save_model(self, request, obj, form, change):
#         user = obj.user
#         obj.created_at = datetime.datetime.now()
#         token = RefreshToken.for_user(user)
#         token_obj = OutstandingToken.objects.get(jti=token["jti"])
#         token_obj.token = str(token.access_token)
#         token_obj.save()
#
#
admin.site.register(User, UserAdmin, )
admin.site.register(UserInteresting)
# admin.site.register(OutstandingToken, CustomOutstandingTokenAdmin, )

