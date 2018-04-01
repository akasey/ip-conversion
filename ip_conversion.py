import re

class IPv4_utils:
    @staticmethod
    def ipv4_to_decimal(ip):
        """
        Converts the string ipv4 address to decimal equivalent.

        Usage:
        ```python
            dec = IPv4_utils.ipv4_to_decimal("192.168.1.1") # 3232235777
        ```
        Args:
            ip: IPv4 address (str)
        Returns:
            Integer representing decimal equivalent of provided IPv4 address.
        Raises:
            ValueError: for providing incorrect IPv4 address

        """
        if not type(ip) is str:
            raise ValueError("Provided parameter is not string.")

        ipv4_pattern = re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        if not ipv4_pattern.match(ip):
            raise ValueError("Provided parameter is not IPv4 address.")

        int_octets = [int(x) for x in ip.split(".")]

        dec = 0
        for idx, x in enumerate(reversed(int_octets)):
            dec =  dec | x << 8*idx
        return dec

    @staticmethod
    def decimal_to_ipv4(decimal):
        """
        Converts decimal representation of IPv4 address to string IP.

        Usage:
        ```python
            ip = IPv4_utils.decimal_to_ipv4(3232235777) # 192.168.1.1
        ```

        Args:
            decimal: Integer value for IPv4 address.
        Returns:
            String equivalent of the address provided.
        Raises:
            ValueError: for providing `decimal` not in 0 <= `decimal` < 2^{32}
        """
        if not type(decimal) is int:
            raise ValueError("Argument decimal isn't of type integer: %s" % str(decimal))
        if decimal > 2**32 -1 or decimal<0:
            raise ValueError("Provided number doesn't represent IPv4 address: %d" % decimal)

        octets = []
        while decimal > 0 or len(octets) != 4:
            octet = decimal & 0xff
            octets.append(str(octet))
            decimal = decimal >> 8

        return ".".join(reversed(octets))