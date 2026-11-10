import hashlib
import unittest
from verification_runtime import verify_exact_match


class VerificationTests(unittest.TestCase):
    def test_normalization_preserves_raw_input_identity(self):
        result = verify_exact_match(subject_id="case", candidate=" 4\n", reference="4")
        self.assertTrue(result.accepted)
        self.assertEqual(result.candidate_sha256, hashlib.sha256(b" 4\n").hexdigest())
        self.assertNotEqual(result.candidate_sha256, result.reference_sha256)
        self.assertEqual(result.verifier, "exact_match/v1")

    def test_rejection_and_missing_reference(self):
        self.assertFalse(verify_exact_match(subject_id="case", candidate="5", reference="4").accepted)
        missing = verify_exact_match(subject_id="case", candidate="4", reference=None)
        self.assertFalse(missing.accepted)
        self.assertIsNone(missing.reference_sha256)

    def test_subject_and_input_types_are_explicit(self):
        for args in (dict(subject_id="", candidate="4", reference="4"),
                     dict(subject_id="case", candidate=4, reference="4"),
                     dict(subject_id="case", candidate="4", reference=4)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                verify_exact_match(**args)


if __name__ == "__main__":
    unittest.main()
