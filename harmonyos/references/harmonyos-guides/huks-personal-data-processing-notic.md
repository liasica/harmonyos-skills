---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-personal-data-processing-notic
title: 个人数据处理说明
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a3d5970194539b5af409bb3d88b5f61c044dd43df8b17ecb48b7eb106948a0e
---

华为是数据处理者，不是数据控制者，数据使用目的和方式由开发者决定。

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单
* 指导开发者如何帮助最终用户实现对数据的控制

## 华为处理的个人数据清单

| 个人数据清单 | 使用目的 | 留存期 |
| --- | --- | --- |
| **身份信息** | 开发者在调用签名接口时，在ArkTs接口中添加HuksSecureSignType参数并指定其值为[HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO](../harmonyos-references/js-apis-huks.md#hukssecuresigntype9)，或在NDK接口中添加HuksSecureSignType参数并指定其值为[OH\_HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO](../harmonyos-references/capi-native-huks-api-h.md)，Huks会将待签名的数据添加身份信息后进行签名，并将身份信息返回给开发者。身份信息的使用目的由开发者决定，开发者需在隐私声明中补充对此身份信息的使用目的、留存策略和销毁方式。 | 由开发者根据实际处理在隐私声明中补充。 |

## 指导开发者如何帮助最终用户实现对数据的控制

开发者通过HUKS获取的用户数据，需要开发者自行提供对应的数据主体权利。
