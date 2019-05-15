import typing as tp
from pathlib import Path
from enum import Enum
from dataclasses import dataclass
from io import TextIOWrapper

PathLike = tp.Union[Path, str]


class CommandType(Enum):
    VERTEX = 0


@dataclass
class SourcePosition:
    line: int
    column: int


@dataclass
class Token:
    type: CommandType
    position: SourcePosition


class Lexer:
    _TOKEN_TYPES = {"v", "vt"}

    def __init__(self):
        self.current = 0

    def reset(self):
        if self.file is None:
            raise IOError(f"{self.filename} is not opened.")
        if not self.file.seekable():
            raise IOError(f"{self.filename} is not seekable.")
        self.file.tell()
        self.current

    def __enter__(self):
        if self.file is not None:
            self.file.close()
        self.file = self.filename.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def tokenize(filename: PathLike):
    with filename.open() as file:
        file.readline()


class ObjectFile:
    def __init__(self, filename: PathLike, mode='r'):
        if isinstance(filename, str):
            filename = Path(filename)
        self.filename: Path = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        if self.file is not None:
            self.file.close()
        self.file = self.filename.open(self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
