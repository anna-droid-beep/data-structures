from SuffixArray import SuffixArray
import unittest


class TestSuffixArray(unittest.TestCase):
    def testBuildSuffixArray(self):
        testCases = [("camel", ["amel", "camel", "el", "l", "mel"]),
                     ("azaza", ["a", "aza", "azaza", "za", "zaza"]),
                     ("banana", ["a", "ana", "anana", "banana", "na", "nana"]),
                     ("abab", ["ab", "abab", "b", "bab"])]

        for S, expected_sa in testCases:
            with self.subTest(S=S, expected=expected_sa):
                actual_sa = SuffixArray.buildSuffixArray(S)
                self.assertListEqual(actual_sa, expected_sa)


if __name__ == "__main__":
    unittest.main()
