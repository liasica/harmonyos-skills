---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-192
title: 如何判断JS对象中是否存在某个值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何判断JS对象中是否存在某个值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4cbec73a34a8d7da2a6c494ca25dd9f275e9fd1984bf0ac27686a91702fc5ad2
---

Object.values(对象名).indexOf(待检测值)，若返回-1表示不包含对应值；返回值不等于-1则表示包含。

```screen
var res = array.indexOf(val)
```
