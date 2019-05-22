# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from environments.models import Environment
from features.models import Feature
from projects.models import Project
from segments.models import Segment


class EnvironmentInline(admin.StackedInline):
    model = Environment
    extra = 0
    show_change_link = True


class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 0
    show_change_link = True


class SegmentInline(admin.StackedInline):
    model = Segment
    extra = 0
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    inlines = [
        EnvironmentInline,
        FeatureInline,
        SegmentInline
    ]
    list_display = ('name', 'organisation', 'created_date',)
    list_filter = ('created_date', 'organisation', 'environments',)
    list_select_related = ('organisation',)
    search_fields = ('organisation__name',)
