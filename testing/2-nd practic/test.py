import unittest
from io import StringIO
import main  # Импортируйте ваш модуль main


class TestPasswordValidation(unittest.TestCase):

    def test_valid_password(self):
        input_values = ["12345", "abcdef1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcdef1")

    def test_password_length(self):
        input_values = ["1234", "abcdef"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcdef")

    def test_password_digit(self):
        input_values = ["abcdef", "12345"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "12345")

    def test_valid_password(self):
        input_values = ["12345", "abcdef1psjkvmp"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcdef1psjkvmp")

    def test_valid_password1(self):
        input_values = ["12345", "a1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "a1")

    def test_valid_password2(self):
        input_values = ["12345", "abcde1212f1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcde1212f1")

    def test_valid_password3(self):
        input_values = ["12345", "abcdef1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcd1")

    def test_valid_password4(self):
        input_values = ["12345", "abcd1fsdhbdeb"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcd1fsdhbdeb")

    def test_valid_password5(self):
        input_values = ["12345", "ab1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "ab1")

    def test_valid_password6(self):
        input_values = ["12345", "abcd1fgeg"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcd1fgeg")

    def test_valid_password7(self):
        input_values = ["12345", "abcd1wsgveve14141414"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcd1wsgveve14141414")

    def test_valid_password8(self):
        input_values = ["12345", "1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "1")

    def test_valid_password9(self):
        input_values = ["12345", "abcd1124dfhehn"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abcd1124dfhehn")

    def test_valid_password10(self):
        input_values = ["12345", "24"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "24")

    def test_valid_password11(self):
        input_values = ["12345", "fwfvojhj3134hi"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "fwfvojhj3134hi")

    def test_valid_password12(self):
        input_values = ["12345", "doujbvnwj2wskjbvc"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "doujbvnwj2wskjbvc")

    def test_valid_password13(self):
        input_values = ["12345", "1248lhlihcfg12"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "1248lhlihcfg12")

    def test_valid_password14(self):
        input_values = ["12345", "ef1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "ef1")

    def test_valid_password15(self):
        input_values = ["12345", "rgdegb123def1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "rgdegb123def1")

    def test_valid_password16(self):
        input_values = ["12345", "ab352525def1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "ab352525def1")

    def test_valid_password17(self):
        input_values = ["12345", "wgfwg32123bcdef1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "wgfwg32123bcdef1")

    def test_valid_password18(self):
        input_values = ["12345", ""]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "")

    def test_valid_password19(self):
        input_values = ["12345", "abef1"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "abef1")

    def test_valid_password20(self):
        input_values = ["12345", "1hjb34"]
        output = StringIO()
        with unittest.mock.patch("sys.stdin", StringIO("\n".join(input_values))), \
                unittest.mock.patch("sys.stdout", output):
            password = main.get_password_from_user()
        self.assertEqual(password, "1hjb34")


if __name__ == '__main__':
    unittest.main()
