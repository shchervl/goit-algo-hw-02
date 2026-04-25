import io
import readline
import sys
from collections import deque

if isinstance(sys.stdin, io.TextIOWrapper):
    sys.stdin.reconfigure(encoding="utf-8")
if isinstance(sys.stdout, io.TextIOWrapper):
    sys.stdout.reconfigure(encoding="utf-8")


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    dq = deque(cleaned)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    print("Перевірка паліндромів.\n")
    while True:
        try:
            text = input("Введіть рядок (або Ctrl+C для виходу): ")
            if not text.strip():
                continue
            if is_palindrome(text):
                print(f"'{text}' — паліндром\n")
            else:
                print(f"'{text}' — не паліндром\n")
        except KeyboardInterrupt:
            print("\nДо побачення!")
            break
