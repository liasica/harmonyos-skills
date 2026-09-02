---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-3
title: 端云项目启动时crash报错问题
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 端云项目启动时crash报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ccff9836f65694234171bb5b41d4750b7c0c0cba7d343cce7766ed73c225f494
---

## 问题现象

端云项目启动时报错：“Error message:Cannot read property DatabaseObject of undefined”，是什么原因？

## 背景知识

* [端云一体化开发](../harmonyos-guides/agc-harmonyos-clouddevguide.md)：为丰富HarmonyOS对云端开发的支持、实现端云联动，DevEco Studio以Cloud Foundation Kit（云开发服务）为底座、在传统的“端开发”基础上新增“云开发”能力：开发者选择云开发工程模板，可创建一个同时包含端侧工程与云侧工程的端云一体化工程。之后，开发者在云侧工程对云函数或者云数据库等服务进行开发、调试和部署，而后在端侧工程通过Cloud Foundation Kit调用部署的云端服务。
* 端云一体化支持的签名方式参考：[支持的签名方式](../harmonyos-guides/agc-harmonyos-clouddev-overview.md#section10621955124720)。
* 端云一体化模拟器支持情况参考：[模拟器支持情况](../harmonyos-guides/agc-harmonyos-clouddev-overview.md#section1093520211139)。

## 问题定位

1. 排查云数据库使用方式是否正确，参考指南：[云数据库](../harmonyos-guides/cloudfoundation-database-service.md)。
2. 排查签名方式是否正确。参考：[支持的签名方式](../harmonyos-guides/agc-harmonyos-clouddev-overview.md#section10621955124720)，目前支持[关联注册应用进行自动签名](../harmonyos-guides/ide-signing.md#section20943184413328)和[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)两种方式，报错有可能是因为使用了不支持的签名方式。
3. 排查运行环境是否正常。从6.0.0(20) Beta5版本开始支持模拟器开发，但与真机存在部分能力差异，详情请参见[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)，报错有可能是使用了低版本的模拟器。

## 分析结论

云数据库使用方式不正确、签名方式不正确、使用低版本模拟器都有可能会导致该问题。

## 修改建议

1. 参考指南：[云数据库](../harmonyos-guides/cloudfoundation-database-service.md)，按照指导步骤进行云数据库开发。
2. 使用支持的签名方式，如[关联注册应用进行自动签名](../harmonyos-guides/ide-signing.md#section20943184413328)和[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。
3. 使用真机或者高于6.0.0(20) Beta5版本的模拟器进行调试。
