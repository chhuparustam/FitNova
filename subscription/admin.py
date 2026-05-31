from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "days",
        "price",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = ("name",)

    ordering = ("-created_at",)

    list_editable = (
        "price",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


from django.contrib import admin
from .models import GymMemberShip


@admin.register(GymMemberShip)
class GymMemberShipAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "member",
        "trainer",
        "subsrciption",
        "days",
        "price",
        "created_at",
    )

    list_filter = (
        "trainer",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)