# math/fraction_to_recurring_decimal.py

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        integer_part = n // d
        rem = n % d
        if rem == 0:
            return sign + str(integer_part)

        frac_parts = []
        seen = {}  # maps remainder -> index in frac_parts

        idx = 0
        while rem != 0:
            if rem in seen:
                start = seen[rem]
                non_rep = "".join(frac_parts[:start])
                rep = "".join(frac_parts[start:])
                return sign + f"{integer_part}." + non_rep + "(" + rep + ")"
            seen[rem] = idx

            rem *= 10
            digit = rem // d
            frac_parts.append(str(digit))
            rem = rem % d
            idx += 1

        return sign + f"{integer_part}." + "".join(frac_parts)
