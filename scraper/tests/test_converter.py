from pathlib import Path

import pytest

from scripts.converter import (
    ExtractedDoc,
    ExtractionError,
    compute_content_hash,
    extract_and_convert,
    render_with_frontmatter,
    rewrite_internal_links,
)
from scripts.paths import normalize_url, url_to_reference_relative


FIXTURE = Path(__file__).parent / "fixtures" / "article.html"


def test_extract_and_convert_returns_doc():
    html = FIXTURE.read_text(encoding="utf-8")
    selectors = {
        "title_candidates": ["article h1"],
        "body_candidates": ["article"],
        "updated_at_candidates": [".update-time"],
        "breadcrumb_candidates": [".breadcrumb"],
    }
    doc = extract_and_convert(html, selectors)
    assert isinstance(doc, ExtractedDoc)
    assert doc.title == "应用模型开发指导"
    assert doc.doc_updated_at == "2026-03-15"
    assert "指南 > 应用框架" in doc.breadcrumb
    md = doc.markdown
    assert "# 应用模型开发指导" in md
    assert "**Stage 模型**" in md
    assert "```typescript" in md
    assert "EntryAbility" in md
    assert "更新时间：2026-03-15" not in md


def test_render_markdown_with_frontmatter_includes_required_fields():
    out = render_with_frontmatter(
        markdown="# X\n\nbody",
        url="https://x/u",
        title="X",
        breadcrumb="A > B",
        category="harmonyos-guides",
        scraped_at="2026-04-27T04:00:00+08:00",
        doc_updated_at="2026-03-15",
        content_hash="sha256:abc",
    )
    assert out.startswith("---\n")
    assert "url: https://x/u" in out
    assert "title: X" in out
    assert "doc_updated_at: 2026-03-15" in out
    assert "content_hash: sha256:abc" in out
    assert out.rstrip().endswith("body")


def test_compute_content_hash_is_stable_across_whitespace():
    a = compute_content_hash("# Title\n\nbody\n")
    b = compute_content_hash("# Title\nbody")
    assert a == b


def test_extraction_failure_raises():
    selectors = {
        "title_candidates": [".does-not-exist"],
        "body_candidates": [".does-not-exist"],
        "updated_at_candidates": [],
        "breadcrumb_candidates": [],
    }
    with pytest.raises(ExtractionError):
        extract_and_convert("<html><body><p>no article</p></body></html>", selectors)


def test_extract_and_convert_resolves_relative_links_with_base_url():
    selectors = {
        "title_candidates": ["h1"],
        "body_candidates": ["article"],
        "updated_at_candidates": [],
        "breadcrumb_candidates": [],
    }
    html = """<html><body><article>
        <h1>X</h1>
        <p><a href="/consumer/cn/doc/harmonyos-guides/y">link</a></p>
        <p><a href="https://example.com/external">外部</a></p>
    </article></body></html>"""
    base = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/x"
    doc = extract_and_convert(html, selectors, base_url=base)
    assert "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/y" in doc.markdown
    assert "https://example.com/external" in doc.markdown


def test_rewrite_internal_links_converts_whitelisted_to_relative():
    refs = Path("harmonyos/references")
    from_md = refs / "harmonyos-guides" / "x.md"
    md = (
        "see [target](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/y) "
        "and [external](https://example.com/foo) here"
    )
    out = rewrite_internal_links(
        md,
        from_md_path=from_md,
        references_root=refs,
        allow_prefixes=["https://developer.huawei.com/consumer/cn/doc/"],
        url_normalizer=normalize_url,
        url_to_relative=url_to_reference_relative,
    )
    assert "[target](y.md)" in out
    assert "[external](https://example.com/foo)" in out


def test_rewrite_internal_links_preserves_fragment():
    refs = Path("harmonyos/references")
    from_md = refs / "harmonyos-guides" / "x.md"
    md = "[t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api#section)"
    out = rewrite_internal_links(
        md,
        from_md_path=from_md,
        references_root=refs,
        allow_prefixes=["https://developer.huawei.com/consumer/cn/doc/"],
        url_normalizer=normalize_url,
        url_to_relative=url_to_reference_relative,
    )
    assert "../harmonyos-references/api.md#section" in out
