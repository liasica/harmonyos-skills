from scripts.discover import flatten_tree


def test_flatten_tree_collects_docs_with_breadcrumb_and_dedupes():
    tree = [
        {"nodeName": "入门", "children": [
            {"nodeName": "导读", "relateDocument": "guide", "children": []},
            {"nodeName": "子目录", "children": [
                {"nodeName": "深层", "relateDocument": "deep", "children": []},
            ]},
            {"nodeName": "重复", "relateDocument": "guide", "children": []},
        ]},
        {"nodeName": "纯目录", "children": []},
    ]
    docs = flatten_tree(tree, "指南")
    assert [d["object_id"] for d in docs] == ["guide", "deep"]
    assert docs[0]["title"] == "导读"
    assert docs[0]["breadcrumb"] == "指南 > 入门 > 导读"
    assert docs[1]["breadcrumb"] == "指南 > 入门 > 子目录 > 深层"
