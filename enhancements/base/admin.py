from django.contrib import admin
from .models import *

from mdeditor.widgets import MDEditorWidget

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    fields = [
        'project_id',
        'project_title',
        'project_description',
        'github_link',
        'status',
        'date_created',
        'updated_at',
        'features',

    ]
    readonly_fields= [
        'project_id',
        'updated_at',
        'date_created',
    ]

class FeatureAdmin(admin.ModelAdmin):
    fields = [
        'feature_id',
        'tracking_id',
        'feature_name',
        'feature_description',
        'status',
        'date_created',
        'updated_at',

    ]
    readonly_fields= [
        'date_created',
        'updated_at',
        'tracking_id',
    ]

class ProgressAdmin(admin.ModelAdmin):
    fields = [
        'tracking',
        'trackerid',
        'tracker_title',
        'tracker_description',
        'date_created',

    ]
    readonly_fields= [
        'date_created',
        'trackerid',
    ]


class FeedbackAdmin(admin.ModelAdmin):
    fields = [
        'choice1',
        'choice2',
        'other',
        'choice3',
        'email',
        'feedback',
    ]

    readonly_fields = [
        'choice1',
        'choice2',
        'other',
        'choice3',
        'email',
        'feedback',
    ]



class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(Project,ProjectAdmin)
admin.site.register(Feature,FeatureAdmin)
admin.site.register(Progress,ProgressAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(ExampleModel,ExampleModelAdmin)