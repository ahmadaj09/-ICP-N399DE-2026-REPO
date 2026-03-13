import re
from .entropy_calculator import EntropyCalculator

class PasswordStrengthAnalyzer:
    def __init__(self):
        self.common_passwords = [
            'password','123456','12345678','1234','qwerty','12345','dragon',
            'baseball','football','monkey','letmein','696969','mustang','michael',
            'shadow','master','jennifer','111111','2000','jordan','superman',
            'harley','1234567','fuckyou','trustno1','ranger','buster','thomas',
            'tigger','robert','soccer','fuckme','batman','test','pass'
        ]
        self.entropy_calculator = EntropyCalculator()

    def analyze_password(self, password):
        if not password:
            return {'strength':'Empty','score':0,'feedback':[],'details':{}}
        score = 0
        feedback = []
        details = {}

        length = len(password)
        details['length'] = length
        if length < 8:
            feedback.append("Password is too short (minimum 8 characters)")
        elif length < 12:
            score += 1
            feedback.append("Good length, but could be longer")
        elif length < 16:
            score += 2
            feedback.append("Good length")
        else:
            score += 3
            feedback.append("Excellent length")

        details['has_lower'] = bool(re.search(r'[a-z]', password))
        details['has_upper'] = bool(re.search(r'[A-Z]', password))
        details['has_digit'] = bool(re.search(r'\d', password))
        details['has_symbol'] = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password))

        variety = sum([details['has_lower'], details['has_upper'], details['has_digit'], details['has_symbol']])
        score += variety
        if variety == 4:
            feedback.append("Excellent character variety")
        elif variety == 3:
            feedback.append("Good character variety")
        elif variety == 2:
            feedback.append("Consider adding more character types")
        else:
            feedback.append("Poor character variety - use a mix")

        details['is_common'] = password.lower() in self.common_passwords
        if details['is_common']:
            score = max(0, score-3)
            feedback.append("This is a commonly used password - easily guessable")

        details['has_sequence'] = self._check_sequential(password)
        if details['has_sequence']:
            score = max(0, score-1)
            feedback.append("Contains sequential characters (like '123' or 'abc')")

        details['has_repeats'] = self._check_repeated(password)
        if details['has_repeats']:
            score = max(0, score-1)
            feedback.append("Contains repeated characters")

        details['has_keyboard_pattern'] = self._check_keyboard_pattern(password)
        if details['has_keyboard_pattern']:
            score = max(0, score-1)
            feedback.append("Contains keyboard pattern (like 'qwerty')")

        details['entropy'] = self.entropy_calculator.calculate_entropy(password)
        crack_time, unit = self.entropy_calculator.estimate_crack_time(details['entropy'])
        details['crack_time'] = f"{crack_time} {unit}"

        if details['entropy'] < 30:
            feedback.append("Very low entropy - extremely weak")
            score = max(0, score - 2)
        elif details['entropy'] < 50:
            feedback.append("Low entropy - could be stronger")
            score += 0
        elif details['entropy'] < 70:
            feedback.append("Moderate entropy - reasonably secure")
            score += 1
        elif details['entropy'] < 90:
            feedback.append("High entropy - secure")
            score += 2
        else:
            feedback.append("High entropy - very secure")
            score += 3

        max_score = 10
        score = min(max_score, max(0, score))
        percentage = (score / max_score) * 100
        if percentage >= 85:
            strength = "Very Strong"
        elif percentage >= 70:
            strength = "Strong"
        elif percentage >= 50:
            strength = "Moderate"
        elif percentage >= 30:
            strength = "Weak"
        else:
            strength = "Very Weak"

        return {
            'strength': strength,
            'score': score,
            'max_score': max_score,
            'percentage': percentage,
            'feedback': feedback,
            'details': details
        }

    def generate_recommendations(self, analysis):
        rec = []
        d = analysis['details']
        if d['length'] < 12:
            rec.append(f"Increase length to at least 12 (currently {d['length']})")
        if not d['has_upper']:
            rec.append("Add uppercase letters")
        if not d['has_lower']:
            rec.append("Add lowercase letters")
        if not d['has_digit']:
            rec.append("Add numbers")
        if not d['has_symbol']:
            rec.append("Add special characters (!@#$%^&*)")
        if d.get('is_common'):
            rec.append("Avoid common passwords")
        if d.get('has_sequence'):
            rec.append("Avoid sequential characters")
        if d.get('has_repeats'):
            rec.append("Avoid repeated characters")
        if d.get('has_keyboard_pattern'):
            rec.append("Avoid keyboard patterns")
        if d['entropy'] < 60:
            rec.append(f"Increase entropy (currently {d['entropy']} bits)")
        return rec

    def _check_sequential(self, p):
        p = p.lower()
        seq = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for i in range(len(seq)-2):
            if seq[i:i+3] in p:
                return True
        return False

    def _check_repeated(self, p):
        for i in range(len(p)-2):
            if p[i] == p[i+1] == p[i+2]:
                return True
        return False

    def _check_keyboard_pattern(self, p):
        p = p.lower()
        patterns = ['qwerty','asdfgh','zxcvbn','qwert','asdf','zxcv']
        for pat in patterns:
            if pat in p:
                return True
        return False