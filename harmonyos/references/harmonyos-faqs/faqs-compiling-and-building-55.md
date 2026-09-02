---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-55
title: 项目工程中怎样配置Native的版本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 项目工程中怎样配置Native的版本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b16893ec39c3b87826e8a50b813ad0ee471b5fb5b8d73338335f472abc9efd77
---

在工程级build-profile.json5的app.products中如下进行配置：

```json
"products": [
  {
    "name": "default",
    "signingConfig": "default",
    "compatibleSdkVersion": "5.0.5(17)",
    "targetSdkVersion": "5.0.5(17)",
    "runtimeOS": "HarmonyOS",
  }
],
```
