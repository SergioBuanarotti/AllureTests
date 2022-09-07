from pydantic import BaseModel, Field
from pydantic.networks import IPv4Address

from config import HOST
from enums.model_enums import Connection


class ResponseHeaders(BaseModel):
    Date: str = Field(regex="[A-Z][a-z]+, \d+ [A-Z][a-z]+ \d+ \d\d:\d\d:\d\d [A-Z]+")
    Content_Type: str = Field(alias="Content-Type")
    Content_Length: int = Field(alias="Content-Length")
    Connection: Connection
    Server: str
    Access_Control_Allow_Origin: str = Field(alias="Access-Control-Allow-Origin")
    Access_Control_Allow_Credentials: bool = Field(alias="Access-Control-Allow-Credentials")


class MethodHeaders(BaseModel):
    Accept: str
    Accept_Encoding: str = Field(alias="Accept-Encoding")
    Host: str = Field(regex=f"{HOST}")
    User_Agent: str = Field(alias="User-Agent", regex="python-requests/2.28.1")


class GetMethodBody(BaseModel):
    args: dict
    headers: MethodHeaders
    origin: IPv4Address
    url: str = Field(regex=f"http://{HOST}/get")


class PostMethodBody(GetMethodBody):
    url: str = Field(regex=f"http://{HOST}/post")