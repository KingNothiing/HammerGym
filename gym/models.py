from django.db import models


class ContactRequest(models.Model):
    BRANCH_CHOICES = [
        ('any', 'Не выбрано'),
        ('larionova', 'Тирасполь, ул. Ларионова'),
        ('oscar', 'Оскар на Балке'),
    ]

    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES, default='any')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return f'{self.full_name} - {self.get_branch_display()}'
