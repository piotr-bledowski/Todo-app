from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORIES = [
    ('SC', 'School'),
    ('WK', 'Work'),
    ('SP', 'Sport'),
    ('ER', 'Errands'),
    ('FD', 'Food'),
    ('MISC', 'Miscelaneous'),
]


class Task(models.Model):
    content = models.CharField(max_length=256, blank=False)
    importance = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    category = models.CharField(
        choices=CATEGORIES, default='MISC', max_length=16)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'category': self.category,
            'completed': self.completed,
            'timestamp': self.timestamp
        }
