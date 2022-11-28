from django.contrib import admin
from .models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ["message",
                    "created_at",
                    "updated_at",
                    "created_by",
                    ]


admin.site.register(Message, MessageAdmin)
