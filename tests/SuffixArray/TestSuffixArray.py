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

    def testBuildCompressedSuffixArray(self):
        testCases = [("bannanna", [7, 4, 1, 0, 6, 3, 5, 2]),
                     ("camel", [1, 0, 3, 4, 2]),
                     ("azaza", [4, 2, 0, 3, 1]),
                     ("banana", [5, 3, 1, 0, 4, 2]),
                     ("abab", [2, 0, 3, 1])]

        for S, expected_sa in testCases:
            with self.subTest(S=S, expected=expected_sa):
                actual_sa = SuffixArray.buildCompressedSuffixArray(S)
                self.assertListEqual(actual_sa, expected_sa)

    def testBuildLCPArray(self):
        testCases = [("bannanna", [7, 4, 1, 0, 6, 3, 5, 2], [1, 4, 0, 0, 2, 1, 3, 0]),
                     ("camel", [1, 0, 3, 4, 2], [0, 0, 0, 0, 0]),
                     ("azaza", [4, 2, 0, 3, 1], [1, 3, 0, 2, 0]),
                     ("banana", [5, 3, 1, 0, 4, 2], [1, 3, 0, 0, 2, 0]),
                     ("abab", [2, 0, 3, 1], [2, 0, 1, 0])]

        for S, suffix_array, expected_lcp in testCases:
            with self.subTest(S=S, suffix_array=suffix_array, expected_lcp=expected_lcp):
                actual_lcp = SuffixArray.buildLCPArray(suffix_array, S)
                self.assertListEqual(actual_lcp, expected_lcp)


if __name__ == "__main__":
    unittest.main()
