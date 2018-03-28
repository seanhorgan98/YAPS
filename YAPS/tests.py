from django.test import TestCase
from rango.models import Podcast,
from django.core.urlresolvers import reverse

class PodcastMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        pod = Podcast(title='test',views=-1)
        pod.save()
        self.assertEqual((pod.views >= 0), True)


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):

        add_pod('test1',1)
        add_pod('test2',1)
        add_pod('test3',1)
        add_pod('test4',1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test4")
        num_pods =len(response.context['podcasts'])
        self.assertEqual(num_pods , 13)

def add_pod(title, views):
    c = Podcast.objects.get_or_create(title=title)[0]
    c.views = views
    c.save()

