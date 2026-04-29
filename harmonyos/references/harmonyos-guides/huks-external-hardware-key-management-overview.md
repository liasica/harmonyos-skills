---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-external-hardware-key-management-overview
title: 外部密钥管理扩展简介
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 外部密钥管理扩展简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:986c51c1bf06dea31a0b33e2c0b204692ccc730a4137e118fbbaa5de6b769de4
---

HUKS提供统一的Ability扩展接口，驱动HAP可基于此实现外部密钥管理扩展，注册、注销自定义的硬件密钥管理模块，满足金融领域Ukey证书的浏览器双向SSL认证等场景的身份认证需求。

Ukey：USB key，基于USB接口的硬件设备，可用于存储用户私钥、证书及身份认证等信息。

本指南将介绍应用如何基于Ukey证书的浏览器双向SSL认证等场景，完成身份认证的过程。

## 运作机制

应用调用接口进行身份认证的流程可参考下图，图中流程请参见图后的标注。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/gRQCWElfQX2Hk_wc5TlgPg/zh-cn_image_0000002558605258.png?HW-CC-KV=V1&HW-CC-Date=20260429T053216Z&HW-CC-Expire=86400&HW-CC-Sign=77D5FD3456F507FB8FB8C4B4D5819791179DBFDDCAC677B56DF1C479FA60F50B)

* 标注1：Ukey设备插入。
* 标注2：驱动HAP通过Provider管理接口，注册外部密钥管理扩展能力（Ukey Extension）。

  通过Provider管理能力，驱动HAP可注册、注销外部密钥管理扩展能力。具体参考[Provider管理](huks-provider-management-overview.md)。
* 标注3：应用拉起证书授权选择弹框，弹框中展示证书列表，由用户进行选择。

  3.1：通过IPC调用从Ukey硬件中读取证书信息。
* 标注4：应用层向HUKS发起查询，获取证书详细信息。

  4.1：通过IPC调用从Ukey硬件中读取证书信息。
* 标注5：用户选择具体证书后，应用将获取到证书索引标识KeyUri（即资源ID resourceId），用于打开资源、查询PIN码认证状态。

  HUKS提供PIN码认证能力和认证状态查询能力。应用PIN码认证之前，可以先查询认证状态。具体参考[Ukey PIN码认证](huks-ukey-pin-authentication-management-overview.md)。

  5.1：如果资源未认证，即PIN码未认证，应用需要调用证书管理能力，拉起PIN码认证弹窗，由用户输入PIN码完成认证。完成认证后，进入5的流程，调用HUKS统一接口，执行对应操作。
* 标注6：应用通过调用HUKS提供的统一接口，执行资源管理、签名验签等操作。如：

  + 打开与关闭资源：[资源管理](huks-resource-management-overview.md)。
  + 验证消息内容以及消息发送者身份的真实性：[签名验签](huks-ukey-signing-signature-verification-overview.md)。

  除此以外，HUKS支持应用查询Ukey的密钥相关属性，具体参考[通用查询](huks-ukey-general-query-overview.md)。
* 标注7：在HUKS SA层执行证书查询、资源管理、PIN码认证及签名等核心操作。

在应用基于Ukey发起身份认证前，三方驱动HAP需完成：

* 根据业务场景设计并开发应用自身的外部密钥管理扩展能力。

  驱动HAP需继承HUKS提供的CryptoExtensionAbility，并完成能力接口实现。具体参考[CryptoExtensionAbility扩展能力](huks-extension-ability-support-overview.md)。

  CryptoExtensionAbility是Stage模型中扩展组件[ExtensionAbility](extensionability-overview.md)的派生类。开发者可以通过继承CryptoExtensionAbility并实现自定义接口，实现定制化的外部硬件密钥管理功能，包括：调用外部硬件密钥管理的资源打开与关闭接口、外部硬件密钥管理的PIN认证实现、调用外部硬件密钥管理的通用接口等，可以参考[CryptoExtensionAbility适配开发指导](huks-extension-ability-support-dev.md)。
* 将密钥管理扩展能力注册到系统HUKS服务中。

  CryptoExtensionAbility可以隔离不同的Ukey驱动厂商实现的差异。驱动HAP实现的能力将通过HUKS和[证书管理](certmanager-overview.md)的SDK开放给应用使用。

如此，浏览器等应用才能通过HUKS和[证书管理](certmanager-overview.md)提供的API去使用驱动HAP提供的外部密钥管理能力，包括证书查询、PIN码认证、签名验签等操作。
