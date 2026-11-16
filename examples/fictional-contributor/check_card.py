#!/usr/bin/env python3
"""Reproducible documentary check of preceptoros.agent-card/1 (F0). Not served code: an offline checker.

    python3 -I examples/fictional-contributor/check_card.py          # from the repository root

Exit 0: every case PASS. Exit 1: a case FAILED. Exit 2: NO_DATA (cause printed), e.g. jsonschema not installed.
Never reports a skipped check as a pass.
"""
import copy
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CARD = ROOT / "examples/fictional-contributor/agents/lantern.json"
TEXTS = ("AGENT_CARD.md", "agent-card.schema.json", "companions/template/agents/README.md",
         "examples/fictional-contributor/README.md", "examples/fictional-contributor/ACCEPTANCE.md",
         "examples/fictional-contributor/VALIDATION.md", "examples/fictional-contributor/lab/sample-document.md",
         "examples/fictional-contributor/agents/lantern.json", "examples/fictional-contributor/check_card.py")
FORBIDDEN = re.compile(r"\b(" + "|".join(("ora" + "cle", "nota" + "ry", "de" + "pin", "to" + "ken", "co" + "in",
                                         "clear" + "ing", "ma" + "gic")) + r")\w*", re.I)
SCRUB = re.compile(r"(\b\d{1,3}(\.\d{1,3}){3}\b|/ho" + r"me/|~/\.|[a-z0-9._-]+@[a-z0-9-]+\.[a-z]{2,})", re.I)


def unique(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError("duplicate key " + k)
        out[k] = v
    return out


def no_constant(name):
    raise ValueError("non-finite number " + name)


def main():
    try:
        import jsonschema
    except ImportError:
        print("NO_DATA: jsonschema (Draft 2020-12) is not installed; nothing was checked")
        return 2
    schema = json.loads((ROOT / "agent-card.schema.json").read_text("utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)

    def check(raw):
        if len(raw) >= 1024:
            return "size"
        try:
            obj = json.loads(raw.decode("utf-8", "strict"), object_pairs_hook=unique, parse_constant=no_constant)
        except (ValueError, UnicodeError):
            return "json"
        return "schema" if any(True for _ in validator.iter_errors(obj)) else "OK"

    raw = CARD.read_bytes()
    base = json.loads(raw)
    cases = [("lantern_valid", raw, "OK")]

    def mutate(name, change, expect="schema"):
        card = copy.deepcopy(base)
        change(card)
        cases.append((name, json.dumps(card, separators=(",", ":")).encode("utf-8"), expect))

    mutate("real_without_key", lambda c: c.__setitem__("fixture", False))
    mutate("reserved_voice_soberano", lambda c: c["agent"].__setitem__("id", "soberano"))
    mutate("unknown_capability", lambda c: c["requests"].append("memory.write"))
    mutate("grant_claim_in_authority", lambda c: c.__setitem__("authority", "granted"))
    mutate("extra_field_grants", lambda c: c.__setitem__("grants", ["talk.write"]))
    mutate("duplicate_request", lambda c: c["requests"].append("talk.read"))
    mutate("empty_requests", lambda c: c.__setitem__("requests", []))
    mutate("fixture_with_key", lambda c: c.__setitem__(
        "key", {"alg": "ed25519", "public_hex": "0" * 64, "registry": "babel registry/keys/example.pub"}))
    cases.append(("oversize_padded", raw.rstrip() + b" " * (1024 - len(raw.rstrip())), "size"))
    cases.append(("duplicate_key", raw.replace(b'"fixture":true', b'"fixture":true,"fixture":true', 1), "json"))

    failed = 0
    for name, data, expect in cases:
        got = check(data)
        ok = got == expect
        failed += not ok
        print("PASS" if ok else "FAIL", name, "->", got)
    for rel in TEXTS:
        text = (ROOT / rel).read_text("utf-8")
        for rx, tag in ((FORBIDDEN, "vocabulary"), (SCRUB, "scrub")):
            hits = sorted({m.group(0) for m in rx.finditer(text)})
            if hits:
                failed += 1
                print("FAIL", tag, rel, hits)
    print("PASS" if not failed else "FAIL", "text scans over", len(TEXTS), "files")
    print("ALL", "PASS" if not failed else "FAIL", len(cases), "card cases")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
