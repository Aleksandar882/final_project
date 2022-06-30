from django.contrib import admin
from .models import Topic, Quiz, Badge
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    
        def has_add_permission(self, request, obj=None):
                return True

        def has_change_permission(self, request, obj=None):
                return True        

        def has_delete_permission(self, request, obj=None):
                return True   
        
admin.site.register(Topic,TopicAdmin)

class QuizAdmin(admin.ModelAdmin):

        def has_add_permission(self, request, obj=None):
                return True

        def has_change_permission(self, request, obj=None):
                return True        

        def has_delete_permission(self, request, obj=None):
                return True

admin.site.register(Quiz,QuizAdmin)


class BadgeAdmin(admin.ModelAdmin):

        def has_add_permission(self, request, obj=None):
                return True

        def has_change_permission(self, request, obj=None):
                return True        

        def has_delete_permission(self, request, obj=None):
                return True

admin.site.register(Badge,BadgeAdmin)