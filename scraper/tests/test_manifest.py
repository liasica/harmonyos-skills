import json

from scripts.manifest import Manifest, EntryStatus


def test_empty_manifest_creates_with_defaults(tmp_path):
    path = tmp_path / "manifest.json"
    m = Manifest.load(path)
    assert m.entries == {}
    assert m.schema_version == 1


def test_upsert_new_entry_marks_new(tmp_path):
    m = Manifest.load(tmp_path / "manifest.json")
    e = m.upsert(
        url="https://developer.huawei.com/consumer/cn/doc/x",
        title="X",
        category="harmonyos-guides",
        local_path="data/docs/consumer/cn/doc/x.md",
        content_hash="sha256:abc",
        doc_updated_at="2026-04-01",
        now="2026-04-27T04:00:00+08:00",
    )
    assert e.status == EntryStatus.NEW
    assert e.first_scraped_at == "2026-04-27T04:00:00+08:00"
    assert e.last_changed_at == "2026-04-27T04:00:00+08:00"
    assert e.last_checked_at == "2026-04-27T04:00:00+08:00"


def test_upsert_unchanged_only_updates_checked_at(tmp_path):
    m = Manifest.load(tmp_path / "manifest.json")
    m.upsert(
        url="https://x.test/a",
        title="A",
        category="c",
        local_path="p",
        content_hash="sha256:abc",
        doc_updated_at="2026-04-01",
        now="2026-04-26T04:00:00+08:00",
    )
    e = m.upsert(
        url="https://x.test/a",
        title="A",
        category="c",
        local_path="p",
        content_hash="sha256:abc",
        doc_updated_at="2026-04-01",
        now="2026-04-27T04:00:00+08:00",
    )
    assert e.status == EntryStatus.OK
    assert e.last_checked_at == "2026-04-27T04:00:00+08:00"
    assert e.last_changed_at == "2026-04-26T04:00:00+08:00"


def test_upsert_changed_updates_changed_at(tmp_path):
    m = Manifest.load(tmp_path / "manifest.json")
    m.upsert(url="u", title="t", category="c", local_path="p",
             content_hash="sha256:old", doc_updated_at="2026-04-01",
             now="2026-04-26T04:00:00+08:00")
    e = m.upsert(url="u", title="t", category="c", local_path="p",
                 content_hash="sha256:new", doc_updated_at="2026-04-15",
                 now="2026-04-27T04:00:00+08:00")
    assert e.last_changed_at == "2026-04-27T04:00:00+08:00"
    assert e.content_hash == "sha256:new"
    assert e.doc_updated_at == "2026-04-15"


def test_mark_stale_for_urls_not_seen(tmp_path):
    m = Manifest.load(tmp_path / "manifest.json")
    m.upsert(url="u1", title="t", category="c", local_path="p",
             content_hash="h", doc_updated_at=None, now="2026-04-26T00:00:00+08:00")
    m.upsert(url="u2", title="t", category="c", local_path="p",
             content_hash="h", doc_updated_at=None, now="2026-04-26T00:00:00+08:00")
    m.mark_stale_except(seen={"u1"})
    assert m.entries["u1"].status != EntryStatus.STALE
    assert m.entries["u2"].status == EntryStatus.STALE


def test_save_and_load_roundtrip(tmp_path):
    p = tmp_path / "manifest.json"
    m = Manifest.load(p)
    m.upsert(url="u", title="t", category="c", local_path="p",
             content_hash="h", doc_updated_at="2026-04-01",
             now="2026-04-27T04:00:00+08:00")
    m.last_full_sync_at = "2026-04-27T04:30:00+08:00"
    m.save()

    raw = json.loads(p.read_text(encoding="utf-8"))
    assert raw["last_full_sync_at"] == "2026-04-27T04:30:00+08:00"
    assert "u" in raw["entries"]

    m2 = Manifest.load(p)
    assert m2.entries["u"].title == "t"
