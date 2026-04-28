---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-20
title: 401 参数检查失败的可能原因和解决办法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 401 参数检查失败的可能原因和解决办法
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe1a287fdae3c0d33330c3a4e061b03e0b1d7e452694c576070e2c5ae60f7b32
---

**问题现象**

调用接口报错401 参数检查失败。

**可能原因**

1. 必选参数没有传入。
2. 参数类型错误 (Type Error)。
3. 参数数量错误 (Argument Count Error)。
4. 空参数错误 (Null Argument Error)。
5. 参数格式错误 (Format Error)。
6. 参数值范围错误 (Value Range Error)。
7. client\_id配置错误。
8. 未使用手动签名。

**解决措施**

1. 请检查必选参数是否传入，传入的参数类型是否错误，以及传入的参数是否符合规格约束。
2. 检查module type为entry的模块下module.json5中的client\_id配置的值是否正确，请参考[配置Client ID](account-client-id.md)。
3. 请使用手动签名方式配置签名，请参考[配置签名和指纹](account-sign-fingerprints.md)。
