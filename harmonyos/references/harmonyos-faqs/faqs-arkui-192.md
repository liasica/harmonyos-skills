---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-192
title: 如何判断JS对象中是否存在某个值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何判断JS对象中是否存在某个值
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6bdc98d50e54283679c6077aa420d3a9ef8d88d3127d940b3988852c1afc3292
---

Object.values(对象名).indexOf(待检测值)，若返回-1表示不包含对应值；返回值不等于-1则表示包含。

```
1. var res = array.indexOf(val)
```

[DetermineValue.js](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DetermineValue.js#L7-L7)
