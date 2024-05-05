from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


@dataclass
class Section:
    title: str
    full_text: str


class Legislation(BaseModel):
    title: str
    full_text: str
    sections: List[Section]


def generate_legislation(prompt: str) -> Legislation:
    """Generate a law based on a prompt."""
    return Legislation(
        title="An Act to amend the Criminal Code",
        full_text="This law amends the Criminal Code to include new offenses and penalties.",
        sections=[
            Section(
                title="Section 1",
                full_text="This section creates a new offense of cyberbullying.",
            ),
            Section(
                title="Section 2",
                full_text="This section increases the penalties for drug trafficking.",
            ),
        ],
    )
