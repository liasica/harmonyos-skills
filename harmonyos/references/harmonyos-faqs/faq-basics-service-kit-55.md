---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-55
title: 如何解决使用剪贴板接口阻塞主线程问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何解决使用剪贴板接口阻塞主线程问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59031b64552b791f2294cce4ae172ade27dd88126565ec4928344e60f5dc160e
---

## 问题现象

在获取剪贴板内容前，先调用getDataSync判断剪贴板内是否有内容，然后出现了应用卡顿现象。

## 背景知识

* getData，读取系统剪贴板内容，此接口为异步接口，参考链接：[getData](../harmonyos-references/js-apis-pasteboard.md#getdata14)。
* getDataSync，读取系统剪贴板内容，此接口为同步接口，参考链接：[getDataSync](../harmonyos-references/js-apis-pasteboard.md#getdatasync11)。

## 问题定位

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/bA67nLZCT32Q2idFZw5L6g/zh-cn_image_0000002658853203.png "点击放大")

日志显示THREAD\_BLOCK\_6S卡死由主线程调用getDataSync时锁阻塞引起，同时子线程在剪贴板服务阻塞4s，导致主线程无法响应。

## 分析结论

getData是异步接口，getDataSync是同步接口，应用按需使用，若影响主线程，可使用异步接口getData，或应用自己起一个异步线程调用同步接口getDataSync。

## 修改建议

将getDataSync替换成getData，或者开启异步线程调用getDataSync。
