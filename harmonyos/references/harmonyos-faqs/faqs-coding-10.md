---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-10
title: 关于BuildProfile自定义字段报错:Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
breadcrumb: FAQ > DevEco Studio > 代码编辑 > 关于BuildProfile自定义字段报错:Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba5ae0a6bca11cd29a035ae9ecbf5f7d7b55a984cea6be331c232f30cffaf9e5
---

**问题描述**

项目编译时，关于 BuildProfile 的自定义字段报错如下：

```text
Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
```

**解决措施**

获取构建参数并生成BuildProfile类文件后，在HSP中可以通过以下方式引入该文件：

```screen
import BuildProfile from '${packageName}/BuildProfile';
```

可参考[在代码中获取构建参数](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md#section195881502412)。
