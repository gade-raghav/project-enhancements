from django.contrib import admin
from .models import *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    fields = [
        'project_id',
        'project_title',
        'project_description',
        'github_link',
        'status',
        'date_created',

    ]
    readonly_fields= [
        'project_id',
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

    ]
    readonly_fields= [
        'date_created',
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

admin.site.register(Project,ProjectAdmin)
admin.site.register(Feature,FeatureAdmin)
admin.site.register(Progress,ProgressAdmin)
admin.site.register(Feedback,FeedbackAdmin)