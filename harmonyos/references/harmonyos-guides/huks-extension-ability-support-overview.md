---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-support-overview
title: CryptoExtensionAbility扩展能力介绍
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 驱动HAP ExtensionAbility适配指导 > CryptoExtensionAbility扩展能力介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:310e06661cb8129651bd92172fdbeaac27d0d3cef02883d52996b6a2e9f28d16
---

CryptoExtensionAbility是Stage模型中扩展组件[ExtensionAbility](extensionability-overview.md)的派生类。

CryptoExtensionAbility给驱动厂商提供外部密钥管理扩展能力所需接口定义，包括打开/关闭资源、PIN码认证、签名验签、导出证书等接口。

CryptoExtensionAbility可以隔离底层硬件（Ukey驱动）厂商实现差异。

三方驱动HAP应用如需定义自身外部密钥管理扩展能力：

首先，需继承CryptoExtensionAbility并完成相关的接口实现。其次，通过Provider注册接口[registerProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)完成能力注册。最后，由HUKS和证书管理将对应的密钥管理扩展能力开放给应用。

## 核心能力实现

CryptoExtensionAbility主要实现以下能力：

1. 设备管理，支持单个ExtensionAbility连接多个Ukey。
   * 单个ExtensionAbility最多支持连接10个Ukey设备。
   * 需实现设备热插拔检测和管理机制，确保在Ukey插入/拔出时，能及时通知ExtensionAbility。
   * 需实现设备级别的资源隔离，确保每个Ukey设备的资源对其他Ukey设备是不可见的。
2. 句柄管理，针对同一个Ukey资源（例如容器下的密钥），支持应用维度句柄资源管理，通过[onOpenResource](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityonopenresource)打开资源，通过[onCloseResource](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityoncloseresource)关闭资源。
   * 单个ExtensionAbility最多支持打开100个Ukey密钥资源句柄。
   * 打开资源时需打开底层Ukey句柄，并映射为新的句柄返回给HUKS。
   * 关闭资源时需关闭底层Ukey句柄，并释放缓存的句柄映射。
   * 支持多个HarmonyOS应用，打开/关闭同一个Ukey密钥资源。例如：HarmonyOS应用1，打开容器A后， HarmonyOS应用2，也可以再次打开容器A。
   * 支持多个HarmonyOS应用，操作同一个Ukey密钥资源。例如：HarmonyOS应用1操作容器A中的私钥签名后，HarmonyOS应用2也验证PIN码后，也可以操作容器A中的私钥进行签名，两者互不影响。
3. 密钥会话管理，支持三段式密钥管理操作，单次签名验签需通过[onInitSession](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityoninitsession)/[onUpdateSession](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityonupdatesession)/[onFinishSession](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityonfinishsession)三个函数三步配合完成，需支持会话管理，缓存密钥会话状态。
   * init操作，初始化密钥会话，并返回会话句柄信息。
   * update操作，传入分组数据，对分组数据进行密码操作，更新密钥会话信息后，将中间数据（如果有）返回。
   * finish操作，对传入最后一段分组数据，进行密钥返回操作，并结束密钥会话，将最终结果返回。
4. 认证状态管理，支持应用维度的认证状态管理（认证/查询/重置）。针对同一个Ukey中的应用A，HarmonyOS应用1验证Ukey应用A的PIN码后，HarmonyOS应用2如果要访问Ukey应用A，也需要进行PIN码认证操作。
5. 证书查询，支持根据证书类型，枚举所有证书或查询单个容器中的证书。
6. 通用查询，支持通用查询操作，为上层业务应用提供Ukey设备信息、PIN码信息、公钥信息等查询能力。接口的属性ID采用定义在GMT 0016-2023 标准中的SKF函数名称，长度必须介于 1-100 字节。调用端和ExtensionAbility实现需约定使用的函数名集合及其参数/返回格式。
