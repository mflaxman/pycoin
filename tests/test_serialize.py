# python modules
import unittest

# local modules
from pycoin.serialize import h2b, h2b_rev, b2h, b2h_rev


class SerializeTest(unittest.TestCase):

    def test_h2b(self):
        # TODO: delete this test? It belongs in pycoin, not itcoin
        h = "000102"
        b = b"\x00\x01\x02"
        self.assertEqual(h2b(h), b)
        self.assertEqual(b2h(b), h)
        self.assertEqual(h2b_rev(h), b[::-1])
        self.assertEqual(b2h_rev(b), "020100")


if __name__ == '__main__':
    unittest.main()
