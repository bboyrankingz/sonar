import unittest
from send_email import Email


class SonarTest(unittest.TestCase):

    def test_email(self):
        email = Email('Alert', 'foo@bar', 'bar@foo', 'localhost', 'password')
        email.send()

if __name__ == '__main__':
    unittest.main()
