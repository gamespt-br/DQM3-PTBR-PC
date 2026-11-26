#!/usr/bin/env python3
"""Basic guardrail for files committed to this public documentation repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_SUFFIXES = {
    ".assets", ".bundle", ".unity3d", ".ress", ".resource",
    ".dll", ".exe", ".pak", ".dat", ".bin", ".zip", ".7z", ".rar",
    ".pdb", ".so", ".dylib",
}
MAX_FILE_BYTES = 15 * 1024 * 1024
SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]

errors = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    rel = path.relative_to(ROOT)
    if path.suffix.lower() in BLOCKED_SUFFIXES:
        errors.append(f"Extensão não permitida: {rel}")
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        errors.append(f"Arquivo excede 15 MiB: {rel} ({size} bytes)")
    # Scan textual files only. Screenshot formats are allowed but not scanned as text.
    if path.suffix.lower() in {".md", ".txt", ".py", ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg"}:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Arquivo textual não está em UTF-8: {rel}")
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possível credencial/segredo encontrado: {rel}")
                break

if errors:
    print("A validação do repositório público encontrou problemas:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validação concluída: nenhuma extensão proibida, arquivo acima do limite ou padrão comum de segredo encontrado.")
