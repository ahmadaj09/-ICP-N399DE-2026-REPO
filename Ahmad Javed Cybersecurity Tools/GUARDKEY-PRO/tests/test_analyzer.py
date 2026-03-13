import unittest
from src.password_analyzer import PasswordStrengthAnalyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = PasswordStrengthAnalyzer()

    def test_empty_password(self):
        res = self.analyzer.analyze_password("")
        self.assertEqual("Empty", res['strength'])
        self.assertEqual(0, res['score'])
        self.assertEqual({}, res['details'])

    def test_weak_password(self):
        res = self.analyzer.analyze_password("123")
        self.assertEqual("Very Weak", res['strength'])

    def test_strong_password(self):
        res = self.analyzer.analyze_password("P@ssw0rd!2025#Secure")
        self.assertIn(res['strength'], ["Strong", "Very Strong"])
        self.assertGreaterEqual(res['percentage'], 70)

    def test_common_password_detection(self):
        res = self.analyzer.analyze_password("password")
        self.assertTrue(res['details']['is_common'])
        self.assertIn("commonly used password", " ".join(res['feedback']).lower())

    def test_sequence_detection(self):
        res = self.analyzer.analyze_password("abcD123!")
        self.assertTrue(res['details']['has_sequence'])

    def test_repeated_detection(self):
        res = self.analyzer.analyze_password("AAAbbb111!!!")
        self.assertTrue(res['details']['has_repeats'])

    def test_keyboard_pattern_detection(self):
        res = self.analyzer.analyze_password("Qwerty!23A")
        self.assertTrue(res['details']['has_keyboard_pattern'])

    def test_entropy_increases_with_complexity(self):
        weak = self.analyzer.analyze_password("aaaaaaaa")
        strong = self.analyzer.analyze_password("A9!kP2@xL7#q")
        self.assertGreater(strong['details']['entropy'], weak['details']['entropy'])

    def test_recommendations_for_weak_password(self):
        analysis = self.analyzer.analyze_password("password")
        rec = self.analyzer.generate_recommendations(analysis)
        joined = " ".join(rec).lower()
        self.assertIn("uppercase", joined)
        self.assertIn("numbers", joined)
        self.assertIn("special", joined)
        self.assertIn("avoid common passwords", joined)

if __name__ == '__main__':
    unittest.main()