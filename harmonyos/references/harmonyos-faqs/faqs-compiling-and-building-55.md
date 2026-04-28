---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-55
title: 项目工程中怎样配置Native的版本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 项目工程中怎样配置Native的版本
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f5ff0a8ce230982947560c361a846fcfcaf9cffafb0a23a4ae2c1e4ebda4644a
---

在工程级build-profile.json5的app.products中如下进行配置：

```
1. "products": [
2. {
3. "name": "default",
4. "signingConfig": "default",
5. "compatibleSdkVersion": "5.0.5(17)",
6. "targetSdkVersion": "5.0.5(17)",
7. "runtimeOS": "HarmonyOS",
8. }
9. ],
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/build-profile.json5#L5-L13)
