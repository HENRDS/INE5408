import typing as tp
import re
from itertools import takewhile, islice
from pathlib import Path
from enum import Enum
from dataclasses import dataclass
from shapes import Point, Line
import numpy as np

PathLike = tp.Union[Path, str]


class TokenType(Enum):
    ERROR = 0
    ID = 1
    NUM = 2
    WS = 3
    COMMENT = 4
    NEWLINE = 5
    IDX = 6


@dataclass
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int
    value: tp.Optional[int]


class Lexer:
    _TOKEN_SPEC = {
        TokenType.ID: r"\b[a-zA-Z]\w+\b",
        TokenType.NUM: r"[-+]?\d+\.\d+",
        TokenType.IDX: r"[-+]?\d+",
        TokenType.WS: r"[\t ]+",
        TokenType.NEWLINE: r"\\?\r?\n",
        TokenType.COMMENT: r"#[^\n]*",
        TokenType.ERROR: r"."
    }
    _KEYWORDS = {"l", "p", "o", "v", ""}
    _TOKENS_IGNORE = {TokenType.COMMENT, TokenType.WS, TokenType.NEWLINE}

    def __init__(self, file: tp.TextIO):
        self.token_regex = re.compile("|".join(f"(?P<{typ.name}>{regx})" for typ, regx in self._TOKEN_SPEC.items()))
        self.code = "".join(file.readlines())
        self.line = 1
        self.line_start = 0

    def __iter__(self) -> tp.Generator[Token, None, None]:
        self.line = 1
        self.line_start = 0
        for match in self.token_regex.finditer(self.code):
            kind = TokenType[match.lastgroup]
            lexeme = match.group()
            column = match.start() - self.line_start
            value = None
            if kind == TokenType.NEWLINE:
                self.line_start = match.end()
                self.line += 1

            if kind in self._TOKENS_IGNORE:
                continue

            if kind == TokenType.NUM:
                value = float(lexeme)
            elif kind == TokenType.IDX:
                value = int(lexeme)
            elif kind == TokenType.ERROR:
                raise RuntimeError(f"Invalid token '{lexeme}' at [{self.line}: {column}]")

            yield Token(kind, lexeme, self.line, column, value)


class Vertex:
    def __init__(self, *tokens: Token):
        self.tokens = tokens
        self.array = np.array(tk.value for tk in tokens)


class Parser:
    def __init__(self, lexer: Lexer):
        self.tokens = [tk for tk in lexer]
        self.current = 0
        self.vertices = []
        self.objects = []

    def current_obj(self):
        return self.objects[-1] if self.objects else None

    def err(self, msg, tk=...) -> tp.NoReturn:
        if tk is ...:
            tk = self.tokens[-1 if self.is_at_end() else self.current]
        raise RuntimeError(f"{msg} at [{tk.line}, {tk.column}].")

    def is_at_end(self):
        return self.current >= len(self.tokens)

    def current_token(self):
        return None if self.is_at_end() else self.tokens[self.current]

    def match(self, typ: TokenType):
        tk = self.current_token()
        if tk is not None and tk.type == typ:
            self.current += 1
            return tk
        return None

    def match_interval(self, typ: TokenType, min_count: tp.Optional[int] = None, max_count: tp.Optional[int] = None):
        stop = None if max_count is None else self.current + max_count
        tokens = list(takewhile(lambda tk: tk.type == typ, islice(self.tokens, self.current, stop)))
        found = len(tokens)
        self.current += found
        if min_count is not None and found < min_count:
            self.err(f"Expected at least {min_count} {typ.name}, found only {found}")
        return tokens

    def skip_until(self, tok: TokenType):
        i = 0
        for tk in self.tokens[self.current:]:
            if tk.type == tok:
                break
            i += 1
        self.current += i

    def vertex(self):
        v = Vertex(*self.match_interval(TokenType.NUM, 3, 4))
        self.vertices.append(v)
        if self.current_obj() is not None:
            self.current_obj()["points"].append(v)
        return v

    def parse(self):
        while not self.is_at_end():
            cmd = self.match(TokenType.ID)
            if cmd is None:
                self.err("Expected command")
            if cmd.lexeme == "v":
                self.vertex()
            elif cmd.lexeme == "o":
                tk = self.match(TokenType.ID)
                if tk is None:
                    self.err("Expected object name")
                obj = {"name": tk.lexeme, "points": []}
                self.objects.append(obj)
                continue
            else:
                print(f"Warning: Unknown command '{self.current_token().type.name}'.")
                self.skip_until(TokenType.ID)
        return self.objects


def load(path: str):
    objects = []
    with open(path) as file:
        parser = Parser(Lexer(file))
        for obj in parser.parse():
            name = obj["name"]
            points = obj["points"]
            n = len(obj["points"])
            if n == 1:
                x, y, z, *_ = points[0].array
                objects.append(Point(name, x, y, z))
            elif n == 2:
                pass


def save():
    pass
