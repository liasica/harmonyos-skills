from pathlib import Path

from scripts.paths import (
    normalize_url,
    url_to_local_path,
    url_to_reference_relative,
    is_in_whitelist,
)


def test_url_to_local_path_strips_doc_prefix():
    url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide"
    assert url_to_local_path(url, root=Path("harmonyos/references")) == Path(
        "harmonyos/references/harmonyos-guides/application-dev-guide.md"
    )


def test_url_to_local_path_trailing_slash_becomes_index():
    url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/"
    assert url_to_local_path(url, root=Path("harmonyos/references")) == Path(
        "harmonyos/references/harmonyos-releases/index.md"
    )


def test_url_to_local_path_strips_query_and_fragment():
    url = "https://developer.huawei.com/consumer/cn/doc/x/y?lang=cn#section"
    assert url_to_local_path(url, root=Path("harmonyos/references")) == Path(
        "harmonyos/references/x/y.md"
    )


def test_normalize_url_strips_fragment_and_trailing_slash_consistency():
    a = normalize_url("https://developer.huawei.com/consumer/cn/doc/x#a")
    b = normalize_url("https://developer.huawei.com/consumer/cn/doc/x")
    assert a == b == "https://developer.huawei.com/consumer/cn/doc/x"


def test_normalize_url_keeps_meaningful_query():
    u = normalize_url("https://developer.huawei.com/consumer/cn/doc/x?id=1&utm_source=foo")
    assert "utm_source" not in u
    assert "id=1" in u


def test_is_in_whitelist():
    prefixes = ["https://developer.huawei.com/consumer/cn/doc/"]
    assert is_in_whitelist("https://developer.huawei.com/consumer/cn/doc/x", prefixes)
    assert not is_in_whitelist("https://example.com/", prefixes)


def test_url_to_reference_relative_in_whitelist():
    refs = Path("harmonyos/references")
    from_md = refs / "harmonyos-guides" / "application-dev-guide.md"
    target = "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api"
    rel = url_to_reference_relative(target, from_md, refs,
                                    ["https://developer.huawei.com/consumer/cn/doc/"])
    assert rel == "../harmonyos-references/development-intro-api.md"


def test_url_to_reference_relative_keeps_fragment():
    refs = Path("harmonyos/references")
    from_md = refs / "harmonyos-guides" / "x.md"
    target = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/y#section1"
    rel = url_to_reference_relative(target, from_md, refs,
                                    ["https://developer.huawei.com/consumer/cn/doc/"])
    assert rel == "y.md#section1"


def test_url_to_reference_relative_outside_whitelist_returns_none():
    refs = Path("harmonyos/references")
    from_md = refs / "x.md"
    rel = url_to_reference_relative("https://example.com/foo", from_md, refs,
                                    ["https://developer.huawei.com/consumer/cn/doc/"])
    assert rel is None
