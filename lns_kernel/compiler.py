"""Deterministic compiler from LNS source to JSON-compatible semantic IR."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json

from .parser import parse


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def compile_source(source: str) -> dict[str, Any]:
    ast = parse(source)
    canonical_ast = _canonical(ast)
    return {
        "ir_version": "VAIXLNS-LNS-IR-1",
        "source_hash": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "ast_hash": hashlib.sha256(canonical_ast.encode("utf-8")).hexdigest(),
        "ast": ast,
    }


def compile_file(path: str | Path) -> dict[str, Any]:
    return compile_source(Path(path).read_text(encoding="utf-8"))
