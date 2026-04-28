---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-31
title: 首选项错误码：code:"401" err: Error: Parameter error. The type of 'value' must be ValueType. 如何排查问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 首选项错误码：code:"401" err: Error: Parameter error. The type of 'value' must be ValueType. 如何排查问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1f4102bcd71f741ffbd073cf89cae81d5fd7df1e798c5204e92e395d5c85ccd3
---

优先排查value长度。如果value值为字符串类型，请使用UTF-8编码格式。value值可以为空，不为空时长度不超过8192个字节。

Parameter error问题的原因包括：参数值超出有效范围、参数类型不匹配、必填参数缺失等。

* Mandatory parameters are not specified：未指定强制参数，未传入指定参数。
* 参数类型不正确：参数类型不匹配，需要检查并确保参数类型正确。
* 参数验证失败：参数无效或超出指定范围。
