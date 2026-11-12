---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing
title: 配置调试签名
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 配置调试签名
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b176c1e66af860ade39015aeaec823701b5bfceb51f8af9988967fec9d46ce60
---

针对开发调试场景，DevEco Studio提供[自动签名](ide-signing-auto.md)和[手动签名](ide-signing-manual.md)两种调试签名方式，帮助开发者高效进行应用调试。

自动签名适用于大部分调试场景，但部分调试场景须使用手动签名，具体为跨设备调试、跨应用交互调试、断网情况下调试、多用户共同开发且需要共享密钥、kit需要配置指纹。

26.0.1之前版本，签名配置信息存放在工程级build-profile.json5的“signingConfigs”字段中。

从26.0.1版本开始，签名信息变更如下：

* 新增的签名配置信息默认会存放至工程目录下的.sign/sign-config.json5文件中，build-profile.json5中原有的签名信息仍生效。
* 签名方案名称（${default}）下会显示签名信息所在文件为build-profile.json5或sign-config.json5。
* 若sign-config.json5和build-profile.json5存在同名[签名方案](ide-hvigor-build-profile-app.md#section153288223224)时，sign-config.json5优先级高于build-profile.json5。
* sign-config.json5和build-profile.json5两文件独立互不影响。

* **[自动签名](ide-signing-auto.md)**
* **[手动签名](ide-signing-manual.md)**
