from django.contrib import admin
from .models import *
# Register your models here.

#class SerieAdmin(admin.TabularInline):
#    model = Serie
#    extra = 2

#class PreacherAdmin(admin.TabularInline):
#    model = Preacher
#    extra = 1

#class TopicSectionAdmin(admin.TabularInline):
#    model = TopicSection
#    extra = 2

class MessageAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['topic']}),
            ('File URL', {'fields':['fileLink']}),
            ('Date of Upload',{'fields':['dateAndTime']}),
            ('Topic Sections', {'fields':['topicSection']}),
            ('Preacher', {'fields':['preacher']}),
            ('Message Series',{'fields':['series']})
            ]
    list_display = ['topic','preacher','series','fileLink','dateAndTime']
    #inlines =[SerieAdmin, PreacherAdmin]
admin.site.register(Message, MessageAdmin)
admin.site.register(TopicSection)
admin.site.register(Preacher)
admin.site.register(Serie)