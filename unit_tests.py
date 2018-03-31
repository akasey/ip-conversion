import unittest
from ip_conversion import IPv4_utils


class Test_IPv4_to_Dec(unittest.TestCase):
    def test_invalid_ip_1(self):
        with self.assertRaises(ValueError):
            IPv4_utils.ipv4_to_decimal("apple")

    def test_invalid_ip_2(self):
        with self.assertRaises(ValueError):
            IPv4_utils.ipv4_to_decimal("123")

    def test_invalid_ip_3(self):
        with self.assertRaises(ValueError):
            IPv4_utils.ipv4_to_decimal("12.234.12")

    def test_invalid_ip_4(self):
        with self.assertRaises(ValueError):
            IPv4_utils.ipv4_to_decimal("10.1.256.0")

    def test_invalid_ip_5(self):
        with self.assertRaises(ValueError):
            IPv4_utils.ipv4_to_decimal("10.0001.255.0")

    def compare(self, ip, decimal):
        number = IPv4_utils.ipv4_to_decimal(ip)
        self.assertEqual(number, decimal, "%s != %d" % (ip, decimal) )

    def test_ip_to_dec_1(self):
        self.compare("0.0.0.0", 0)

    def test_ip_to_dec_2(self):
        self.compare("0.0.0.1", 1)

    def test_ip_to_dec_3(self):
        self.compare("0.0.0.255", 255)

    def test_ip_to_dec_4(self):
        self.compare("0.0.255.1", 65281)

    def test_ip_to_dec_5(self):
        self.compare("0.255.0.0", 16711680)

    def test_ip_to_dec_6(self):
        self.compare("255.0.0.0", 4278190080)

    def test_ip_to_dec_7(self):
        self.compare("192.168.12.14", 3232238606)

class Test_Dec_to_IPv4(unittest.TestCase):
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            IPv4_utils.decimal_to_ipv4("-1")

    def test_not_integer(self):
        with self.assertRaises(ValueError):
            IPv4_utils.decimal_to_ipv4("apple")

    def test_value_out_of_range(self):
        with self.assertRaises(ValueError):
            IPv4_utils.decimal_to_ipv4(9999999999)

    def compare(self, ip, decimal):
        string = IPv4_utils.decimal_to_ipv4(decimal)
        self.assertEqual(string, ip, "%d != %s" % (decimal, ip) )

    def test_first_octet_1(self):
        self.compare("0.0.0.255", 255)

    def test_first_octet_2(self):
        self.compare("0.0.0.0", 0)

    def test_second_octet_1(self):
        self.compare("0.0.1.0", 256)

    def test_second_octet_2(self):
        self.compare("0.0.254.0", 65024)

    def test_third_octet(self):
        self.compare("0.123.1.1", 8061185)

    def test_arbitrary_1(self):
        self.compare("192.168.1.20", 3232235796)

    def test_arbitrary_2(self):
        self.compare("10.123.32.98", 175841378)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_IPv4_to_Dec)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Dec_to_IPv4))
    unittest.TextTestRunner(verbosity=2).run(suite)