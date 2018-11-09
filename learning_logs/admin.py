from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.
admin.site.register(Topic) #Umozliwia zarzadanie modelem z poziomu witryny admin
admin.site.register(Entry)


