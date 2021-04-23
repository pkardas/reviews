from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class Review:
    header: str
    content: Optional[str]
    rating: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "header": self.header,
            "content": self.content,
            "rating": self.rating
        }
