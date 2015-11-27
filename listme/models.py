from django.db import models

class List(models.Model):
    owner = models.ForeignKey('auth.User', related_name='lists')
    name = models.CharField(max_length=100, blank=True, default='')
    score = models.IntegerField(default=0)
    show_list = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)

    def __repr__(self):
        return self.id

class ListElement(models.Model):
    list = models.ForeignKey('List', default=None, related_name='list_elements')
    text = models.CharField(max_length=100, blank=True, default='')
    completed = models.BooleanField(default=False)
    show_element = models.BooleanField(default=True)
    completed_time = models.DateTimeField(default=None)

    def __repr__(self):
        return self.id

# class Subscriptions(models.Model):
#     user