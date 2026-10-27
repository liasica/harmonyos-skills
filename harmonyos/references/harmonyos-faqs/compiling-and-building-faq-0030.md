---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0030
title: 项目工程Native版本配置常见问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 项目工程Native版本配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3fc38cad086705cac07a88fb943e50d1ec6d11a5592ab36883c4eb6ca91565e2
---

**Q：项目工程中怎样配置Native的版本？**

**A**：在工程级build-profile.json5的app.products中如下进行配置：

```json
"products": [
  {
    "name": "default",
    "signingConfig": "default",
    "compatibleSdkVersion": "26.0.0",
    "targetSdkVersion": "26.0.0",
    "runtimeOS": "HarmonyOS",
  }
],
```
