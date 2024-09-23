import unittest
from unittest.mock import patch, Mock
from tools.weather import get_weather

class TestWeather(unittest.TestCase):

    @patch('tools.weather.requests.get')
    def test_get_weather_success(self, mock_get):
        # Mock a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = '''
        <html>
            <span id="wob_tm">25</span>
            <span id="wob_dc">Sunny</span>
        </html>
        '''
        mock_get.return_value = mock_response

        result = get_weather("New York")
        self.assertEqual(result, "The current weather in New York is Sunny with a temperature of 25°C")

    @patch('tools.weather.requests.get')
    def test_get_weather_no_weather_info(self, mock_get):
        # Mock a response with missing weather information
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = '''
        <html>
        </html>
        '''
        mock_get.return_value = mock_response

        result = get_weather("New York")
        self.assertEqual(result, "Weather information not found")

    @patch('tools.weather.requests.get')
    def test_get_weather_failed_request(self, mock_get):
        # Mock a failed response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_weather("New York")
        self.assertEqual(result, "Failed to retrieve the webpage. Status code: 404")

    def test_get_weather_no_mock(self):
        result = get_weather("New York")
        self.assertIn("The current weather in New York", result)

if __name__ == '__main__':
    unittest.main()
