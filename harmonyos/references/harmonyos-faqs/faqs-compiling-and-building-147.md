---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-147
title: 编译报错“File 'string.json' is missing the required property 'string'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“File 'string.json' is missing the required property 'string'.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5328186dc76784d862768db2a7c5d7bdc72557950e791e51dcaca18f87e6aa11
---

**错误描述**

资源文件“string.json”缺少必需属性“string”。

**可能原因**

hap模块依赖的hsp或har包中的资源文件string.json缺少必需的属性“string”。

**解决措施**

确保hsp或har文件中的“string.json”包含“string”属性。

示例：

```
1. {
2. "string": [
3. {
4. "name": "shared_desc",
5. "value": "description"
6. }
7. ]
8. }
```
