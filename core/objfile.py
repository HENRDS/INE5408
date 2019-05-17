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
        TokenType.ID: r"\b[a-zA-Z]+\b",
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
        self.vertices = {
            "v": [],
            "vn": [],
            "vt": [],
            "vp": [],
        }
        self.objects = []

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
        for i, tk in enumerate(self.tokens[self.current:]):
            if tk.type == tok:
                self.current += i
                break

    def vertex(self):
        self.vertices["v"].append(Vertex(*self.match_interval(TokenType.NUM, 3, 4)))

    def points(self, name: tp.Optional[str]):
        if name is None:
            name = "Point"
        for i, v in enumerate(self.match_interval(TokenType.NUM, 1)):
            idx = int(v.value)
            vtx = self.vertices["v"][idx]
            nm = name + (str(i) if i > 0 else "")
            self.objects.append(Point(nm, *vtx.array[:3]))

    def lines(self, name: tp.Optional[str]):
        if name is None:
            name = "Line"
        match = self.match_interval(TokenType.NUM, 2)
        vertices = self.vertices["v"]
        for i, (p1, p2) in enumerate(zip(match[:-1], match[1:])):
            v1, v2 = vertices[int(p1.value)].array, vertices[int(p2.value)].array
            nm = name + (str(i) if i > 0 else "")
            self.objects.append(Line(nm, v1, v2))

    def parse_command(self, cmd: str):
        pass

    def parse(self):
        name: tp.Optional[str] = None
        while not self.is_at_end():
            cmd = self.match(TokenType.ID)
            if cmd is None:
                self.err("Expected command")
            if cmd.lexeme == "v":
                self.vertex()
            elif cmd.lexeme == "p":
                self.points(name)
            elif cmd.lexeme == "l":
                self.lines(name)
            elif cmd.lexeme == "o":
                tk = self.match(TokenType.ID)
                if tk is None:
                    self.err("Expected object name")
                name = tk.lexeme
                continue
            else:
                self.skip_until(TokenType.ID)
            name = None
