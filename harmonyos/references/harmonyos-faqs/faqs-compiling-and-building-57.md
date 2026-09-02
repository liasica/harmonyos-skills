---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-57
title: 怎样在编译配置中设置excludes文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 怎样在编译配置中设置excludes文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a51b1c831a3f28206cb4f2a98e7671d64ead504c2b046eb246fb8faba0ceca3b
---

在模块级build-profile.json5中如下进行配置：

```json
"nativeLib": {
  "debugSymbol": {
    "strip": true,
    "exclude": [
      "**/3.so"
    ]
  }
},
```
