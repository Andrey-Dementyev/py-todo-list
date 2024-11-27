from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    class Meta:
        ordering = ["-creation_time"]

    def __str__(self):
        return (
            f"{self.content} (created at {self.creation_time}, have done {self.done})"
        )
