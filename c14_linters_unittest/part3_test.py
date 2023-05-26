import json
import unittest
from unittest.mock import patch, MagicMock

from c14_linters_unittest.part3 import time_getter
from part3 import my_func

output = ['Africa/Abidjan', 'Africa/Accra']


class TestTimeGetter(unittest.TestCase):
    @patch("c14_linters_unittest.part3.requests.get")
    def test_content(self, get_mock):
        get_mock.return_value = MagicMock(text=json.dumps(output))
        self.assertEqual(time_getter(), output)


#


if __name__ == '__main__':
    unittest.main()
