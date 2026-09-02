---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-8
title: 代码层面如何判断当前设备支持防窥保护功能
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 代码层面如何判断当前设备支持防窥保护功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ec6ebbf07086b395a5caf8a29ac98f156c347ae531c02a41cbcbebb17914f761
---

## 问题现象

在公共场合使用HarmonyOS设备时，存在被他人窥视屏幕导致隐私泄露的风险（如支付记录、聊天内容等）。

## 背景知识

[防窥保护](../harmonyos-guides/devicesecurity-dlpantipeep.md)：支持应用根据屏幕窥视状态保护机主隐私，如拉起系统级蒙层遮盖窗口，非机主状态下不进行个性化推荐，隐藏浏览记录、支付记录、收藏记录等敏感信息。其中系统使用智能判断将长期通过人脸解锁手机的人作为防窥保护的机主。

## 解决方案

1. 先使用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)判断当前设备是否支持防窥保护能力，传参为：SystemCapability.Security.DlpAntiPeep。
2. 当第一步返回True时则表示当前设备支持防窥保护，则继续调用[isDlpAntiPeepSwitchOn](../harmonyos-references/devicesecurity-dlpantipeep-api.md#isdlpantipeepswitchon)接口，若返回801，代表当前手机由于硬件规格等限制不支持防窥保护，若正常返回执行第3步。
3. 第二步正常返回True，则表示当前应用开启了防窥保护，可以调用相关API。
