from django.test import TestCase

from django.utils import timezone
# from tinymce.models import HTLMField - Need it too?

from .models import Post


class PostMethodTests(TestCase):

	def test_was_published_recently_with_future_post(self):
		"""
		was_published_recently() should return False for posts whose
		pubblished_date is in the future.
		"""
		time = timezone.now() + deltatime.timedelta(days=30)
		future_post = Post(published_date=time)
		self.assertEqual(future_post.was_published_recently(), False)
