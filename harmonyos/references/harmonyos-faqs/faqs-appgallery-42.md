---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-42
title: 如何解决关闭开发者模式时应用无法打开的问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何解决关闭开发者模式时应用无法打开的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fdf8fe8db97db374e8788755adb51b0e5af4d8d58391bde6507ce7cb6022be1a
---

## 问题现象

开发者应用上架后，通过应用市场下载出来的APP无法打开，但是打开设备的开发者模式后能打开，该问题如何定位解决？

## 背景知识

[FaultLog](../harmonyos-guides/ide-fault-log.md)：当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

## 问题定位

1. 首先观察应用无法打开的现象，可以看出是出现了“闪退”的情况。
2. 应用闪退后会存在FaultLog日志，可以在DevEco Studio[查看设备历史抛出的FaultLog日志](../harmonyos-guides/ide-fault-log.md#section4692114071018)。
3. 观察到出现了JS Crash日志：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/qHbiE_kUSBGCyN6LpFzw6Q/zh-cn_image_0000002658913823.png "点击放大")
4. 根据JS Crash日志可以定位到错误的代码行，然后根据报错修改。

## 分析结论

根据代码可以看出问题出在[usbManager.getDevices](../harmonyos-references/js-apis-usbmanager.md#usbmanagergetdevices)上，根据文档说明：

在USB主机模式未开启、USB服务未正确初始化、USB服务连接失败（如开发者模式关闭）、权限不足或其他系统错误时，接口会返回undefined，注意需要对接口返回值做判空处理。

而开发者没有对undefined进行处理，故出现应用打不开的问题。

## 修改建议

增加对usbManager.getDevices返回值可能为undefined的情况的处理即可。
