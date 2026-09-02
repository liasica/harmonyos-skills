---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-kit-new-00001
title: 其他厂商设备与HarmonyOS设备媒体控制的实现方式
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 其他厂商设备与HarmonyOS设备媒体控制的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:55abf5a96e5b36be40fb91712c8a57800202206a5f40e301eaa57e44fd4f5988
---

## 问题现象

如何实现其他厂商设备与HarmonyOS设备的媒体控制？融合短距中需要伙伴设备应用实现PartnerAgentExtensionAbility，具体场景为其他厂商设备（如手表）控制HarmonyOS设备（如手机）的媒体播放或暂停。

## 背景知识

[融合短距](../harmonyos-guides/fusion-connectivity-overview.md#概述)服务是Connectivity Kit提供的短距通信服务，支持伙伴设备与HarmonyOS设备之间的互通。伙伴设备需通过[PartnerAgentExtensionAbility](../harmonyos-guides/partneragent-life-application-guide.md#partneragentextensionability实现)实现与HarmonyOS设备的配对注册。媒体播控方面，HarmonyOS设备侧可通过[AVSession](../harmonyos-guides/avsession-overview.md) Kit提供的接口进行媒体会话管理。

## 解决方案

通过融合短距和AVSession实现跨设备媒体控制

步骤一：设备配对注册。通过[PartnerAgentExtensionAbility](../harmonyos-guides/partneragent-life-application-guide.md#partneragentextensionability实现)实现伙伴设备与HarmonyOS设备的配对注册流程。此功能不需要在伙伴设备侧构建HarmonyOS代码，伙伴设备只需按照融合短距协议完成配对注册即可。

步骤二：设备间通信。配对注册完成后，伙伴设备与HarmonyOS设备之间自行通信，传输控制命令和状态信息。HarmonyOS设备端需要有对应的控制应用来接收和处理这些命令。

步骤三：媒体播控。HarmonyOS设备侧应用参考[AVSession](../harmonyos-guides/avsession-overview.md) Kit相关接口进行媒体播控。首先调用[avSession.getAllSessionDescriptors](../harmonyos-references/arkts-apis-avsession-f.md#avsessiongetallsessiondescriptors23)接口获取当前所有媒体会话描述符，从描述符中获取对应的sessionId，然后通过avSession.createController(sessionId)创建AVSessionController，最后调用控制器的play()或pause()方法来控制媒体播放或暂停。
