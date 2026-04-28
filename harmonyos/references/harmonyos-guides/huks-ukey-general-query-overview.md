---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-general-query-overview
title: 通用查询介绍及规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 通用查询介绍及规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:34+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:8b5080c4a8588dc942ed2456dbb47d72b51e3185802c0f1127206a0e5621b5ce
---

HUKS提供属性查询接口，支持从外部密钥管理执行通用查询操作，例如Ukey设备信息、PIN码信息等。

说明

1. [OH\_Huks\_GetProperty](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getproperty)接口和[getProperty](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetproperty)接口的resourceId是提供者的资源ID，用于标识要查询的远程资源，长度必须介于1-1024字节。接口的属性ID采用定义在 GMT 0016-2023 标准中的SKF函数名称，长度必须介于 1-100 字节。
2. 输出参数通过[HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)携带，应用可以提取该查询出的属性数据，并按照和驱动应用（外部密钥管理扩展能力提供方）的约定，解析数据。

## 支持的属性函数名称（示例）

下列为部分属性函数名称示例，供实现方参考（更多详细且权威的函数名请参考 GMT 0016-2023 标准）：

| 函数名 | 说明 |
| --- | --- |
| SKF\_GetDevInfo | 获取设备信息。 |
| SKF\_EnumDev | 枚举设备。 |
| SKF\_EnumContainer | 枚举容器。 |
| SKF\_EnumApplication | 枚举应用。 |

说明

实际实现应与 GMT 0016-2023 中规定的函数名保持一致。各方（调用端和CryptoExtension实现）需约定使用的函数名集合及其参数/返回格式。
