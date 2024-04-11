from django.db import models

class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'suggestions'
