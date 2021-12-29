from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORIES = [
    ('school', 'School'),
    ('coding', 'Coding'),
    ('work', 'Work'),
    ('sport', 'Sport'),
    ('errands', 'Errands'),
    ('diet', 'diet'),
    ('miscelaneous', 'Miscelaneous'),
]


class Task(models.Model):
    content = models.CharField(max_length=256, blank=False)
    importance = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    category = models.CharField(
        choices=CATEGORIES, default='miscelaneous', max_length=16)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'importance': self.importance,
            'category': self.category,
            'completed': self.completed,
            'timestamp': self.timestamp
        }
