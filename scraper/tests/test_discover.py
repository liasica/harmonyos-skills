from pathlib import Path

from scripts.discover import extract_links_from_html


FIXTURE = Path(__file__).parent / "fixtures" / "sidebar.html"


def test_extract_links_filters_to_allowed_prefix():
    html = FIXTURE.read_text(encoding="utf-8")
    selectors = {
        "link_candidates": ["aside a[href]", ".sidebar a[href]"],
    }
    base_url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide"
    allow_prefixes = ["https://developer.huawei.com/consumer/cn/doc/"]
    links = extract_links_from_html(html, base_url, selectors, allow_prefixes)

    urls = {l["url"] for l in links}
    assert "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide" in urls
    assert "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-models" in urls
    assert "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilities" in urls
    assert not any("example.com" in u for u in urls)
    assert not any("anchor-only" in u for u in urls)
    assert not any("/consumer/cn/other/" in u for u in urls)


def test_extract_links_returns_titles():
    html = FIXTURE.read_text(encoding="utf-8")
    base_url = "https://developer.huawei.com/consumer/cn/doc/x"
    links = extract_links_from_html(
        html, base_url,
        {"link_candidates": [".sidebar a[href]"]},
        ["https://developer.huawei.com/consumer/cn/doc/"],
    )
    titles = {l["title"]: l["url"] for l in links}
    assert "应用开发指南" in titles
    assert "应用模型" in titles
