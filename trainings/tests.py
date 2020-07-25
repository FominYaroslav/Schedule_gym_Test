import datetime
from django.test import TestCase
from django.urls import reverse

from .models import Training


class TrainModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Training.objects.create(name = 'crossfit', time = datetime.datetime.now())

    def testname_max_length(self):
        training = Training.objects.get(id = 1)
        max_length = training._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_object_name_is_name_and_date(self):
        training = Training.objects.get(id = 1)
        expected_object_name = "{0} [{1}.{2}]".format(training.name, training.time.day, training.time.month)
        self.assertEquals(expected_object_name,str(training))


class TrainingListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_trainings = 10
        for training_num in range(1, number_of_trainings):
            Training.objects.create(name='fitness', time = datetime.datetime.now().replace(day = training_num))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/schedule')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedule.html')
