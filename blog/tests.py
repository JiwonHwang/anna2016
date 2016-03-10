from django.test import TestCase

from django.utils import timezone
# from tinymce.models import HTLMField - Need it too?

from .models import Post


class PostMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is in the future.
		"""
		# To do 
		# 1. migrate 
		# 2. check bug in terminal 
		# 3. revise tests.py here 