---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-introduction
title: Device Security Kit简介
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > Device Security Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f41ddb9b348b21486c81af974cf1110d34ffc054ac8e28509b36a353db513af5
---

Device Security Kit（设备安全服务）提供应用设备状态检测（DeviceVerify）、安全检测（SafetyDetect）、可信应用服务（TrustedAppService）、数字盾服务（TrustedAuthentication）、业务风险检测（BusinessRiskIntelligentDetection）、安全审计（SecurityAudit）、反诈选择器（AntifraudPicker）、防窥保护（DlpAntiPeep）、病毒防护服务管理（VirusProtectionServiceManager）和超级隐私模式（SuperPrivacyMode），可以保护应用程序免受安全威胁和保证应用的数据安全。

## 场景介绍

* 应用设备状态检测（DeviceVerify）场景：对应用在某台设备上的使用状态进行管理和检测，包括判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等的状态检测，以支撑业务进行新用户营销活动。
* 安全检测（SafetyDetect）场景：判断设备环境是否安全，比如是否被越狱、非真实设备等，可基于结果评估如何响应；判断用户访问的URL是否为恶意网址，对于恶意网址，由您评估提示或拦截用户的访问风险。
* 可信应用服务（TrustedAppService）场景：提供数据的安全证明服务，旨在为安全摄像头和安全地理位置功能提供基础的安全证明能力，确保图像或位置数据未被篡改。
* 数字盾服务（TrustedAuthentication）场景：提供基于TUI PIN认证和TUI界面交易信息确认的安全能力，旨在为金融应用在数字盾交易场景下提供金融安全保护。
* 业务风险检测（BusinessRiskIntelligentDetection）场景：提供基于场景（防作弊、反欺诈）的业务风险决策能力。
* 安全审计（SecurityAudit）场景：为应用提供获取当前设备上的审计数据（窗口截屏、移动存储插拔、剪切板复制粘贴等）能力，支撑审计相关业务。
* 反诈选择器（AntifraudPicker）场景：为反诈应用提供获取诈骗消息、诈骗通话记录和诈骗应用的能力，支撑反诈相关业务。
* 防窥保护（DlpAntiPeep）场景：支持应用根据窥视状态保护用户隐私，如非机主状态下不进行个性化推荐，隐藏浏览记录、支付记录、收藏记录等敏感信息。
* 病毒防护服务管理（VirusProtectionServiceManager）场景：支持应用向设备提交自身软件信息、查询设备中防病毒软件信息列表、启停设备自带的安全防护服务。
* 超级隐私模式（SuperPrivacyMode）场景：支持应用查询和监听超级隐私模式状态。

## 基本概念

* DeviceToken：由Device Security Kit生成并用于标识设备和应用身份的Token。该Token用于应用服务器与Device Security服务器通信，从而获得当前设备的状态。
* nonce：由开发者生成，并且在系统完整性检测结果中会包含这个nonce值，调用者通过校验这个nonce值来确定检测结果没有被重放攻击。
* 安全证明：可信应用服务模块提供的一种服务，用于验证数据的真实性和完整性，确保数据在生成、传输和存储过程中没有被篡改。
* 证明密钥：安全证明服务中生成的加密密钥，用于生成和验证数据的数字签名。安全摄像头和安全地理位置共用同一个证明密钥。
* 证明会话：安全证明服务的上下文，在使用安全摄像头或安全地理位置功能前需要创建对应的证明会话，用于验证证明密钥的有效性。

## 与其他Kit的关系

[数字盾服务](devicesecurity-trustedauth-service.md)联合[Universal Keystore Kit（密钥管理服务）](huks-kit.md)、[User Authentication Kit（用户认证服务）](user-authentication-kit.md)共同为金融应用数字盾开发提供可信UI、可信认证、可信签名能力。

业务关联如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/X-ffilxmS7qwkY3mEm5JIw/zh-cn_image_0000002558605222.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053126Z&HW-CC-Expire=86400&HW-CC-Sign=E4E28CAF7F49E92F89DCC6791ACA879287F25836BF033359AC45611943A48E40)

## 约束与限制

### 支持的国家/地区

| 场景 | 国家/地区 |
| --- | --- |
| 应用设备状态检测 | 请参见[支持的国家/地区](devicesecurity-appendix-region.md)。 |
| 安全检测-系统完整性检测 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 安全检测-URL检测 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 安全检测-本地系统完整性检测 | 请参见[支持的国家/地区](devicesecurity-appendix-region.md)。 |
| 安全检测-系统完整性增强检测 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 可信应用服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 数字盾服务 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 安全审计 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 业务风险检测 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 反诈选择器 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 防窥保护 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 病毒防护服务管理 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 超级隐私模式 | 只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |

### 支持的设备

| 场景 | 支持设备 |
| --- | --- |
| 应用设备状态检测 | Phone、Tablet、PC/2in1、Wearable、TV。 |
| 安全检测 | Phone、Tablet、PC/2in1、Wearable。 |
| 安全摄像头（可信应用服务） | Phone、PC/2in1。 |
| 安全地理位置（可信应用服务） | Phone、Tablet。 |
| 安全图像压缩、裁剪（可信应用服务） | Phone、PC/2in1。 |
| 数字盾服务 | Phone。 |
| 安全审计 | PC/2in1。 |
| 业务风险检测 | Phone、Tablet。 |
| 反诈选择器 | Phone、Tablet。 |
| 防窥保护 | Phone。 |
| 病毒防护服务管理 | PC/2in1。 |
| 超级隐私模式 | Phone、Tablet、PC/2in1、Wearable、TV。 |

## 模拟器支持情况

本Kit暂不支持模拟器。
