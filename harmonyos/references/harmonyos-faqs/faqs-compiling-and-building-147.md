---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-147
title: 编译报错“File 'string.json' is missing the required property 'string'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“File 'string.json' is missing the required property 'string'.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4069b248022c2944627059da298d3af38d41a22950824099b6a6c8b95537e38e
---

**错误描述**

资源文件“string.json”缺少必需属性“string”。

**可能原因**

hap模块依赖的hsp或har包中的资源文件string.json缺少必需的属性“string”。

**解决措施**

确保hsp或har文件中的“string.json”包含“string”属性。

示例：

```json
{
  "string": [
    {
      "name": "shared_desc",
      "value": "description"
    }
  ]
}
```
