
import re

match = re.search(r"\b[A-Z]{1}(\D{6})1+\b", "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111")

if match:
    print(match.group(1))  # ➜ Elzero