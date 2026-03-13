import math
import re

class EntropyCalculator:
    CHARSETS = {'lowercase':26,'uppercase':26,'digits':10,'symbols':33}

    @staticmethod
    def calculate_charset_size(password):
        size = 0
        if re.search(r'[a-z]', password):
            size += 26
        if re.search(r'[A-Z]', password):
            size += 26
        if re.search(r'\d', password):
            size += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password):
            size += 33
        return size

    @staticmethod
    def calculate_entropy(password):
        charset = EntropyCalculator.calculate_charset_size(password)
        if charset == 0:
            return 0
        return round(len(password) * math.log2(charset), 2)

    @staticmethod
    def estimate_crack_time(entropy, guesses_per_second=1e9):
        seconds = 2**entropy / guesses_per_second
        intervals = [('seconds',60),('minutes',60),('hours',24),('days',30),
                     ('months',12),('years',100),('centuries',None)]
        value = seconds
        unit = 'seconds'
        for next_unit, multiplier in intervals:
            if multiplier and value > multiplier:
                value /= multiplier
                unit = next_unit
            else:
                break
        return round(value,2), unit
