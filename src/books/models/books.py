from typing import Tuple
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20, )
    date_of_birth = models.DateField(null=True, blank=True, )
    date_of_died = models.DateField('died', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    OPTIONS = (
        ('Literature', (
            ('11', 'Fiction',),
            ('12', 'Novel',),
            ('13', 'Poetry',),
            ('14', 'Rendering',),
            ('15', 'Essays',),
            ('16', 'Short Story',),
            ('17', 'Drama',),

        )),
        ('Academic', (
            ('21', 'Computer Science and Engineering',),
            ('22', 'Electrical & Electronics Engineering',),
            ('23', 'Bachelor of Business Administration',),
            ('24', 'Law and Justice',),
            ('25', 'PHARMACY',),
            ('26', 'Anthropology',),
            ('27', 'History',),
            ('28', 'Philosophy',),
            ('29', 'Economics',),
            ('30', 'Political Science',),
            ('31', 'Psychology',),
            ('32', 'Sociology',),
            ('33', 'Physics',),
            ('34', 'Bio-Chemistry',),
            ('35', 'Zoology',),

        )),

    )

    isbn = models.CharField('ISBN', primary_key=True, max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international'
                                      '.org/content/what-isbn '
                                      '">ISBN number</a>')
    book_name = models.CharField(max_length=50, )
    author = models.ForeignKey('books.Author', related_name='books', on_delete=models.CASCADE, )
    edition = models.CharField(max_length=30, )
    summary = models.TextField(max_length=1000, default='write summary of book', help_text="Enter a brief description "
                                                                                           "of the book")
    genre = models.CharField(max_length=20, choices=OPTIONS, blank=True, help_text="Select a book genre",
                             default='12', )
    language = models.CharField(max_length=50, default='Bangle',
                                help_text="Enter the book's natural language (e.g. English, French, "
                                          "Japanese etc.)")

    AVAILABLE = 'available'
    BORROWED = 'borrowed'
    ARCHIVED = 'archived'
    STATUS = [
        (AVAILABLE, _('Available to borrow')),
        (BORROWED, _('Borrowed by someone')),
        (ARCHIVED, _('Archived - not available anymore')),
    ]

    status = models.CharField(max_length=32, choices=STATUS, default=AVAILABLE, )

    class Meta:
        db_table = 'book'
        ordering = ['isbn']

    def __str__(self):
        return self.book_name
