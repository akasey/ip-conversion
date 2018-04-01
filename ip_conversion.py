
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
            raise ValueError("Provided parameter isn't string.")

        splits = ip.split(".")
        if len(splits) != 4:
            raise ValueError("Provided parameter isn't IPv4 address.")
        try:
            def validate(octet):
                if len(octet) >3:
                    raise ValueError("%s isn't valid octet" % octet)
                int_octet = int(octet)
                if int_octet >= 0 and int_octet < 256:
                    return int_octet
                raise ValueError("%d isn't valid octet" % int_octet )

            int_splits = [validate(x) for x in splits]
        except ValueError as e:
            raise ValueError("Provided parameter isn't IPv4 address: %s :: %s" % (ip, str(e)) )

        dec = 0
        for idx, x in enumerate(reversed(int_splits)):
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