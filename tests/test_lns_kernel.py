from pathlib import Path

from lns_kernel.compiler import compile_file, compile_source
from lns_kernel.parser import tokenize


ROOT = Path(__file__).resolve().parents[1]


def test_tokenizer_accepts_root_syntax():
    source = 'vaixlns_root { meta { id "VAIXLNS://ROOT/GENESIS/1.0" } }'
    tokens = tokenize(source)
    assert tokens[0].value == "vaixlns_root"
    assert any(token.value == "VAIXLNS://ROOT/GENESIS/1.0" for token in tokens)


def test_compile_root_fixture_deterministically():
    first = compile_file(ROOT / "VAIXLNS_ROOT.lns")
    second = compile_file(ROOT / "VAIXLNS_ROOT.lns")
    assert first["ir_version"] == "VAIXLNS-LNS-IR-1"
    assert first["source_hash"] == second["source_hash"]
    assert first["ast_hash"] == second["ast_hash"]
    assert first["ast"]["vaixlns_root"]["meta"]["name"] == "VAIXLNS Civilization Root"


def test_relations_are_explicit():
    compiled = compile_source(
        'root { relations { link a -> b link b -> c } }'
    )
    assert compiled["ast"]["root"]["relations"]["links"] == [
        {"from": "a", "to": "b"},
        {"from": "b", "to": "c"},
    ]
