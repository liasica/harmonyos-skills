---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-tag
title: js标签配置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > js标签配置
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:66e7637faaa294666dc3424fd6d17e333bd2fccaeced506c826ef0845d82a065
---

js标签中包含了实例名称、页面路由信息。

| 标签 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| name | string | default | 是 | 标识JS实例的名字。 |
| pages | Array | - | 是 | 路由信息，详见“[pages](js-lite-framework-js-tag.md#pages)”。 |

**说明** 

name、pages标签配置需在配置文件中的“js”标签中完成设置。

## pages

定义每个页面的路由信息，每个页面由页面路径和页面名组成，页面的文件名即为页面名，例如：

```json
{
  // ...
  "pages": [
    "pages/index/index",
    "pages/detail/detail"
  ]
  // ...
}
```

**说明** 

* 应用首页固定为"pages/index/index"。
* 页面文件名不能使用组件名称，比如：text.hml、button.hml等。

## 示例

```json
{
  "app": {
    "bundleName": "com.example.player",
    "version": {
        "code": 1,
        "name": "1.0"
    },
    "vendor": "example"
  },
  "module": {
    // ...
    "js": [
      {
        "name": "default",
        "pages": [
          "pages/index/index",
          "pages/detail/detail"
        ]
      }
    ],
    "abilities": [
      {
        // ...
      }
    ]
  }
}
```
