from dataclasses import dataclass, asdict


@dataclass
class UserData:
    user_name: str
    location: str

    def to_dict(self):
        return asdict(self)
