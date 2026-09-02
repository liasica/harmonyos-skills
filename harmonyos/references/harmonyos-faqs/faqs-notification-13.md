---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-13
title: 录屏已结束，通知栏仍显示录屏
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 录屏已结束，通知栏仍显示录屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77806529ec99185255831743ce89a6388795a29427d595b4dbb0018f310ce58b
---

## 问题现象

进入应用后，点击开始录屏，通知栏会显示应用正在录屏。点击系统胶囊按钮结束录屏，下拉查看通知栏，仍显示应用正在录屏。

## 背景知识

使用[Notification Kit](../harmonyos-guides/notification-overview.md)可以将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

## 问题定位

1. 点击开始录屏后，分别尝试在应用外点击系统按钮关闭录屏和在应用内点击关闭录屏，发现若通过应用内按钮关闭录屏，则通知栏的通知会被同步取消，判断是取消录屏通知的操作只放在了应用内按钮的点击事件内。
2. 当用户通过系统胶囊按钮结束录屏时会触发[screenCapture.on('stateChange')](../harmonyos-references/arkts-apis-media-avscreencapturerecorder.md#onstatechange12)事件的media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER回调。排查代码，查看该场景下是否有调用[notificationManager.cancel](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagercancel)方法主动关闭通知。

## 分析结论

应用只在内部按钮的点击事件中设置关闭通知，导致当用户通过系统胶囊按钮取消录屏时，通知栏仍提示正在录屏。

## 修改建议

录屏结束触发的回调类型可以参考[AVScreenCaptureStateCode](../harmonyos-references/arkts-apis-media-e.md#avscreencapturestatecode12)。当录屏结束时，在screenCapture.on('stateChange')事件中判断录屏结束的原因，并添加notificationManager.cancel来主动关闭通知。
