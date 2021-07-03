from django.test import TestCase, Client

from django.urls import reverse
from converter.utils.test_utils import get_random_number


class TestLengthConversion(TestCase):
    """Class to store the length conversion tests"""

    def setUp(self):
        """This method excecutes before each test case"""
        self.client = Client()
        self.url = reverse("length:convert")

    def test_centimetre_to_metre_conversion(self):
        """Tests the conversion from centimetre to metre"""
        input_value = get_random_number()
        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": input_value,
        }

        res = self.client.post(self.url, data)
        self.assertContains(res, round(input_value / 100, 3))

    def test_metre_to_centimetre_conversion(self):
        """Tests the conversion from metre to centimetre"""
        input_value = get_random_number()
        data = {
            "input_unit": "metre",
            "output_unit": "centimetre",
            "input_value": input_value,
        }

        res = self.client.post(self.url, data)
        self.assertContains(res, round(input_value * 100, 3))

    def test_centimetre_to_mile_conversion(self):
        """Test the conversion from centimetre to mile"""
        input_value = get_random_number(100, 100000)
        data = {
            "input_unit": "centimetre",
            "output_unit": "mile",
            "input_value": input_value,
        }
        # Convert to metres and then multitply by the equivalent in miles
        expected = round(input_value * 0.01 * 0.000621371, 3)
        response = self.client.post(self.url, data)
        self.assertContains(response, expected)

    def test_mile_to_meter_conversion(self):
        """Test the conversion from mile to meter"""
        # Distance to the moon in miles
        input_value = get_random_number(238855.086, 238855.087)
        data = {
            "input_unit": "mile",
            "output_unit": "metre",
            "input_value": input_value,
        }
        expected = round(input_value * 1609.34, 3)
        response = self.client.post(self.url, data)
        self.assertContains(response, expected)
