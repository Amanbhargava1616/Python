from string import digits, punctuation, ascii_uppercase, ascii_lowercase


class PasswordChecker:
    def __init__(self, password: str) -> None:
        self._password = password

    @staticmethod
    def _has_repeated_characters(text: str) -> bool:
        return any(text[i] == text[i + 1] == text[i + 2] for i in range(len(text) - 2))

    def find_errors(self) -> list[str]:
        errors: list[str] = []

        if len(self._password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if self._has_repeated_characters(text=self._password):
            errors.append("Password can't contain more than 2 sequential characters.")

        if not any(char in digits for char in self._password):
            errors.append(f"Password should contain at least 1 digit.")

        if not any(char in ascii_uppercase for char in self._password):
            errors.append(f"Password should contain at least 1 uppercase character.")

        if not any(char in ascii_lowercase for char in self._password):
            errors.append(f"Password should contain at least 1 lowercase character.")

        if not any(char in punctuation for char in self._password):
            errors.append(f"Password should contain at least 1 special case character from {punctuation}")

        return errors


password_list = [
    "@Seedlingchamp08",
    "@Seeedlingchamp08",
    "Seedlingchamp08",
    "@Seedlingchamp",
    "@Seedlingchamp0",
    "@seedlingchamp08",
    "@seed",
    "@SEEDLINGCHAMP08",
]

for password in password_list:
    pass_checker = PasswordChecker(password)
    errors = pass_checker.find_errors()
    print("=" * 10, password, "=" * 10)
    if errors:
        for txt in errors:
            print(f"==> {txt}")
    else:
        print("You are good to go!...")
    print("\n")
