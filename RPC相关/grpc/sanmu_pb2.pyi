from typing import ClassVar as _ClassVar, Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor


class Request(_message.Message):
    __slots__ = ["a", "b"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int

    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...


class Response(_message.Message):
    __slots__ = ["c"]
    C_FIELD_NUMBER: _ClassVar[int]
    c: int

    def __init__(self, c: _Optional[int] = ...) -> None: ...
