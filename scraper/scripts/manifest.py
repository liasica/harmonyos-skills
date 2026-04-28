"""manifest.json 读写、增量 diff、生命周期管理"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict, field
from enum import Enum
from pathlib import Path
from typing import Iterable, Optional


SCHEMA_VERSION = 1


class EntryStatus(str, Enum):
    NEW = "new"
    OK = "ok"
    STALE = "stale"
    ERROR = "error"


@dataclass
class Entry:
    url: str
    title: str
    category: str
    local_path: str
    content_hash: str
    doc_updated_at: Optional[str]
    first_scraped_at: str
    last_checked_at: str
    last_changed_at: str
    status: EntryStatus = EntryStatus.OK
    error: Optional[str] = None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["status"] = self.status.value
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Entry":
        d = {**d}
        d["status"] = EntryStatus(d.get("status", "ok"))
        return cls(**d)


@dataclass
class Manifest:
    path: Path
    schema_version: int = SCHEMA_VERSION
    last_full_sync_at: Optional[str] = None
    entries: dict[str, Entry] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "Manifest":
        if not path.exists():
            return cls(path=path)
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            path=path,
            schema_version=raw.get("schema_version", SCHEMA_VERSION),
            last_full_sync_at=raw.get("last_full_sync_at"),
            entries={u: Entry.from_dict(e) for u, e in raw.get("entries", {}).items()},
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": self.schema_version,
            "last_full_sync_at": self.last_full_sync_at,
            "stats": self._stats(),
            "entries": {u: e.to_dict() for u, e in sorted(self.entries.items())},
        }
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def _stats(self) -> dict:
        total = len(self.entries)
        new = sum(1 for e in self.entries.values() if e.status == EntryStatus.NEW)
        stale = sum(1 for e in self.entries.values() if e.status == EntryStatus.STALE)
        error = sum(1 for e in self.entries.values() if e.status == EntryStatus.ERROR)
        return {"total": total, "new": new, "stale": stale, "error": error}

    def upsert(
        self,
        *,
        url: str,
        title: str,
        category: str,
        local_path: str,
        content_hash: str,
        doc_updated_at: Optional[str],
        now: str,
        error: Optional[str] = None,
    ) -> Entry:
        existing = self.entries.get(url)
        if existing is None:
            entry = Entry(
                url=url, title=title, category=category, local_path=local_path,
                content_hash=content_hash, doc_updated_at=doc_updated_at,
                first_scraped_at=now, last_checked_at=now, last_changed_at=now,
                status=EntryStatus.ERROR if error else EntryStatus.NEW,
                error=error,
            )
        else:
            changed = existing.content_hash != content_hash
            entry = Entry(
                url=url, title=title, category=category, local_path=local_path,
                content_hash=content_hash,
                doc_updated_at=doc_updated_at if doc_updated_at else existing.doc_updated_at,
                first_scraped_at=existing.first_scraped_at,
                last_checked_at=now,
                last_changed_at=now if changed else existing.last_changed_at,
                status=EntryStatus.ERROR if error else EntryStatus.OK,
                error=error,
            )
        self.entries[url] = entry
        return entry

    def mark_stale_except(self, seen: Iterable[str]) -> None:
        seen_set = set(seen)
        for url, entry in self.entries.items():
            if url not in seen_set and entry.status != EntryStatus.STALE:
                entry.status = EntryStatus.STALE
