class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            # Si el valor actual es menor que el siguiente, se resta
            if i < len(s) - 1 and valores[s[i]] < valores[s[i + 1]]:
                total -= valores[s[i]]
            else:
                total += valores[s[i]]

        return total