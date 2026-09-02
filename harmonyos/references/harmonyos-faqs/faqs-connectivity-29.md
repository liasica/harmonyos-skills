---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-29
title: 蓝牙on('bondStateChange')监听取消输入PIN码回调有延迟
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙on('bondStateChange')监听取消输入PIN码回调有延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:946b2a3530354423b2afe25913b7ba8b3fea46ba77d55d8f6f71f0129322d3bc
---

## 问题现象

在蓝牙扫描到后进行连接，连接成功后30s内再次扫描该设备，会获取到该设备广播数据，然后使用拿到的PIN码在PIN码输入框，取消输入PIN码需要提示用户，点击取消输入后，等待十几秒后才会触发取消的监听。

## 解决方案

蓝牙connection中PIN码配对状态可以通过[connection.on('bondStateChange')](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbondstatechange)监听，点击取消之后会将拒绝配对的消息发给对端，收到对端回复后才能认为这次bond的流程结束，等待回调的过程中会有一定的时间差，具体回调的状态可以参考文档[配对失败原因](../harmonyos-references/js-apis-bluetooth-connection.md#unbondcause12)。
