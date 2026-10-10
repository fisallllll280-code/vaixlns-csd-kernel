# CSD Kernel validation v1

The LNS root is a declarative architecture source. This document defines executable validation obligations without changing language semantics.

## Validation obligations

1. Every entity resolves to a declared domain.
2. Every dependency target exists.
3. Relations resolve to existing entities.
4. Sovereignty rules remain explicit rather than inferred.
5. Dependency graph is acyclic.
6. Genesis metadata is immutable for a given root version.

The next implementation step is a parser/validator that consumes VAIXLNS_ROOT.lns and emits deterministic diagnostics.
