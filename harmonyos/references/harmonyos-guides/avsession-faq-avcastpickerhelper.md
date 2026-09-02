---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-faq-avcastpickerhelper
title: 使用AVCastPickerHelper接口常见问题
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > AVSession Kit常见问题 > 使用AVCastPickerHelper接口常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d363ee6e5012d241b77390b82377f32ca66d8755411e40692933a0e52f3897b8
---

本文汇总音视频应用在使用[AVCastPickerHelper](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md)接口过程中遇到的典型问题及其定位与解决方法。开发者可结合[媒体会话管理错误码](../harmonyos-references/errorcode-avsession.md)和HiLog日志进一步定位问题。

## pickerStateChange监听回调被重复触发

**问题现象**

注册了多次[on('pickerStateChange')](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#onpickerstatechange14)，每次状态变化都收到多个回调。

**可能原因**

若未先注销旧监听而重复调用[on('pickerStateChange')](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#onpickerstatechange14)，新旧监听均会触发回调。

**解决措施**

若只需执行最新监听，请先调用[off('pickerStateChange')](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#offpickerstatechange14)注销已有监听后，再重新注册。
