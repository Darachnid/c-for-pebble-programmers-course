from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass(frozen=True)
class OllamaConfig:
    base_url: str = "http://127.0.0.1:11434"
    model: str = "llama3.2"
    timeout_s: float = 120.0

    @classmethod
    def from_env(cls) -> OllamaConfig:
        base = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
        model = os.environ.get("ASSESSOR_OLLAMA_MODEL", "llama3.2")
        timeout = float(os.environ.get("ASSESSOR_OLLAMA_TIMEOUT", "120"))
        return cls(base_url=base, model=model, timeout_s=timeout)


def ollama_available(config: OllamaConfig) -> bool:
    try:
        req = urllib.request.Request(f"{config.base_url}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=5):
            return True
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def chat_json(config: OllamaConfig, system: str, user: str) -> dict:
    payload = {
        "model": config.model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "format": "json",
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{config.base_url}/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=config.timeout_s) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise SystemExit(
            f"Ollama request failed ({config.base_url}, model={config.model}): {exc}\n"
            "Start Ollama locally and pull a model, e.g.: ollama pull llama3.2"
        ) from exc

    content = body.get("message", {}).get("content", "")
    if not content:
        raise SystemExit("Ollama returned empty response.")
    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Ollama response was not valid JSON:\n{content[:500]}") from exc
