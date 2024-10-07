from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from app1.models import Document


class TestDocument(TestCase):
    def test_save_file(self):
        file_name = "this.is.a.very.l" + "o" * 100 + ".txt"
        Document.objects.create(file=SimpleUploadedFile(name=file_name, content=b"test"))