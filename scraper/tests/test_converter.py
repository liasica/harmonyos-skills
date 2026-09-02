from pathlib import Path

from scripts.converter import (
    compute_content_hash,
    convert_api_html,
    render_with_frontmatter,
    rewrite_internal_links,
)
from scripts.paths import normalize_url, url_to_reference_relative


def test_convert_api_html_drops_title_h1_shifts_headings_and_fixes_links():
    html = (
        '<html><body><a name="TOPIC"></a><h1>应用模型</h1>'
        '<div class="section"><h4>概述</h4><p>正文</p><h5>细节</h5><h4>[h2]子节</h4>'
        '<div class="note"><img src="https://x/note_3.0-zh-cn.png?HW-CC-Sign=abc"><p>提示内容</p></div>'
        '<pre class="TypeScript">let a = 1;</pre>'
        '<video controls="controls"><source src="https://x/v.mp4?HW-CC-Sign=1&HW-CC-Date=2"></video>'
        '<p><a href="/consumer/cn/doc/harmonyos-guides/y">link</a>'
        ' <img src="https://x/a.png?HW-CC-Sign=1&k=v"></p></div></body></html>'
    )
    doc = convert_api_html(html, title="应用模型", breadcrumb="指南 > 应用模型", doc_updated_at="2026-08-29",
                           base_url="https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/x")
    md = doc.markdown
    assert "# 应用模型" not in md
    assert "## 概述" in md and "### 细节" in md
    assert "### 子节" in md and "[h2]" not in md
    assert "**说明**" in md and "note_3.0" not in md
    assert "[视频](https://x/v.mp4)" in md
    assert "```typescript" in md
    assert "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/y" in md
    assert "HW-CC-Sign" not in md and "https://x/a.png?k=v" in md
    assert doc.breadcrumb == "指南 > 应用模型" and doc.doc_updated_at == "2026-08-29"


def test_convert_api_html_uses_h1_when_title_missing():
    doc = convert_api_html("<html><body><h1>标题</h1><p>x</p></body></html>", title="", breadcrumb="",
                           doc_updated_at=None, base_url="https://developer.huawei.com/consumer/cn/doc/a/b")
    assert doc.title == "标题" and doc.markdown.strip() == "x"


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
