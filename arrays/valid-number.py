class Solution:
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False

        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True  # will check after seeing e

        for i, ch in enumerate(s):
            if ch.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True

            elif ch in ['+', '-']:
                # sign is only valid at start or just after e
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # dot can appear only once and not after e
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif ch in ['e', 'E']:
                # e can only appear once, must follow a number
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False  # must see digits after e

            else:
                return False

        return num_seen and num_after_e
