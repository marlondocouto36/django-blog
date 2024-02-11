from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post
import datetime
import utc
# needed to change it since latest version of Django doesn't seem like having timezone.utc


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        """set up"""
        self.now = datetime.datetime.now(datetime.UTC) # needed to change this for a timezone-aware object instead of utcnow()
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_details_only_published(self):
        """test"""
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)


class PostTestCase(TestCase):
    """class for tests"""
    fixtures = ['blogging_test_fixture.json']

    def setUp(self):
        """class for setting up"""
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        """class for testing the representation of a string"""
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
