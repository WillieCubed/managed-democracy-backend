from dataclasses import dataclass
from typing import Literal, Union

from fastapi import FastAPI
from pydantic import BaseModel

from .ai.generate_legislation import Legislation


app = FastAPI()


class Law(BaseModel):
    """A law that exists in some legal code.

    Args:
        title (str): A non-jargon title of the law. E.g. "An Act to amend the Criminal Code".
        reference (str): The reference of the law.
        full_text (str): The full text of the law.
        url (str): The URL where the law can be found.
    """

    title: str
    reference: str
    full_text: str
    pass_date: str
    url: str


class CourtPrecedent(BaseModel):
    """A court precedent that exists in some legal code.

    Args:
    """

    associated_case: str
    title: str
    reference: str
    full_text: str
    url: str


@dataclass
class StatusResponse:
    status: Union[Literal["online"], Literal["offline"]]


@app.get("/api/v1/health")
def health() -> StatusResponse:
    return {"status": "online"}


class LegislationGenerationRequest(BaseModel):
    prompt: str


@app.post("/api/v1/legislation")
def create_legislation(request: LegislationGenerationRequest) -> Legislation:
    return {"status": "complete"}


@app.get("/api/v1/legislation/{legislation_id}")
def get_legislation(legislation_id: int):
    pass


@app.post("/api/v1/public-perception")
def simulate_public_perception():
    pass


@app.get("/api/v1/precedents")
def get_precedents():
    pass


@app.get("/api/v1/reports/{report_id}")
def get_report(report_id: int):
    pass


# TODO: Implement endpoints
