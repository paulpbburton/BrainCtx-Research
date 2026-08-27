#!/usr/bin/env python3
"""Repository self-check for the public research surface.

Three gates, all stdlib, run from the repository root:

  python3 tools/selfcheck.py

1. ANCHOR JOIN  — every anchor cited on a non-archive page as
   `(Anchor: `X`)` / `(Anchors: `X`, `Y`)` must have a row in
   PRIVATE_ANCHORS.md. This is the enforcement PRIVATE_ANCHORS.md's
   verification rule names.
2. LINK WALK    — every relative markdown link in the tree must resolve
   to a file that ships in the repository.
3. EXPOSURE     — generic identifier classes that must not appear in any
   shipped text file: credential/token shapes, home-directory paths,
   UUIDs, and email addresses. The shipped list is deliberately GENERIC:
   it contains no private name, identifier, or reconstructable fragment,
   so the check itself exposes nothing. Identity- and workload-specific
   patterns live in PRIVATE custody; point the check at them with
   `SELFCHECK_PRIVATE_PATTERNS=/path/to/file` (one regex per line, `#`
   comments) at release-review time. A green run without that variable
   claims only the generic classes.

   PUBLIC_IDENTITY_ALLOWLIST.txt (repository root, committed) lists the
   EXACT values that are deliberately published identity — the contact
   email, and nothing patterned. An exposure hit whose entire match is an
   allowlisted exact value counts as an authorized public-identity
   occurrence, reported separately; everything else remains a failure.
   The detector is never weakened and no file is exempted — the report
   distinguishes "authorized public identity occurrences: N" from
   "unintended exposure findings: 0" rather than pretending a repository
   with a public contact address contains no email-shaped strings.

Exit 0 with a per-gate summary, exit 1 naming every violation. A green
run claims exactly these joins — not semantic truth, not claim force,
not release approval.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GENERIC = [
    r"sk-[A-Za-z0-9]{16,}",
    r"ghp_[A-Za-z0-9]{16,}",
    r"AKIA[0-9A-Z]{16}",
    r"xox[baprs]-",
    r"BEGIN [A-Z ]*PRIVATE KEY",
    r"/home/[a-z][a-z0-9_-]*/",
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}",
]

ANCHOR_GROUP = re.compile(r"\(Anchors?:\s*([^)]+)\)")
ANCHOR_ID = re.compile(r"`([A-Z0-9-]+)`")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def allowlist() -> set[str]:
    f = ROOT / "PUBLIC_IDENTITY_ALLOWLIST.txt"
    if not f.exists():
        return set()
    return {l.strip() for l in f.read_text().splitlines()
            if l.strip() and not l.strip().startswith("#")}


def patterns() -> list[re.Pattern]:
    pats = [re.compile(p, re.I) for p in GENERIC]
    extra = os.environ.get("SELFCHECK_PRIVATE_PATTERNS")
    if extra:
        for line in Path(extra).read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                pats.append(re.compile(line, re.I))
        print(f"private pattern file loaded: {len(pats) - len(GENERIC)} extra pattern(s)")
    return pats


def texts():
    for f in sorted(ROOT.rglob("*")):
        if f.is_file() and ".git" not in f.parts and f.suffix in (".md", ".json", ".txt", ".py"):
            yield f


def main() -> int:
    failures: list[str] = []
    pats = patterns()
    allowed = allowlist()
    authorized: list[str] = []

    table = set(ANCHOR_ID.findall(
        "\n".join(l for l in (ROOT / "PRIVATE_ANCHORS.md").read_text().splitlines()
                  if l.startswith("| `"))))
    cited, links = set(), 0
    for f in texts():
        body = f.read_text(errors="ignore")
        rel = f.relative_to(ROOT)
        if f.suffix == ".md" and "archive" not in rel.parts:
            for grp in ANCHOR_GROUP.findall(body):
                cited |= set(ANCHOR_ID.findall(grp))
        if f.suffix == ".md":
            for m in LINK.finditer(body):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                links += 1
                if not (f.parent / target).resolve().exists():
                    failures.append(f"LINK {rel}: unresolvable -> {target}")
        for i, line in enumerate(body.splitlines(), 1):
            for p in pats:
                m = p.search(line)
                if m:
                    # Authorized iff the match's span lies inside a LITERAL
                    # occurrence of an allowlisted exact value on this line:
                    # a private substring pattern firing inside the published
                    # contact address is authorized; the same substring
                    # anywhere else still fails. Nothing non-literal ever
                    # authorizes, and the detectors are never weakened.
                    def _within_allowed(match) -> bool:
                        for v in allowed:
                            start = line.find(v)
                            while start != -1:
                                if start <= match.start() and match.end() <= start + len(v):
                                    return True
                                start = line.find(v, start + 1)
                        return False
                    if _within_allowed(m):
                        authorized.append(str(rel))
                        continue
                    failures.append(f"EXPOSURE {rel}:{i}: {line.strip()[:80]}")
                    break
    for a in sorted(cited - table):
        failures.append(f"ANCHOR {a}: cited on a current-era page, missing from PRIVATE_ANCHORS.md")

    print(f"anchor join: {len(cited)} cited, {len(table)} table rows, "
          f"{len(cited - table)} missing")
    print(f"link walk:   {links} relative links checked")
    print(f"authorized public identity occurrences: {len(authorized)}"
          + (f" ({', '.join(sorted(set(authorized)))})" if authorized else ""))
    print(f"unintended exposure findings: "
          f"{sum(1 for x in failures if x.startswith('EXPOSURE'))}")
    for f in failures:
        print("FAIL", f)
    print("RESULT:", "FAIL" if failures else "PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
