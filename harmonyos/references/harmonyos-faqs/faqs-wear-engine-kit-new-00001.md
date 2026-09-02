---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-kit-new-00001
title: 获取穿戴设备SN号作为设备唯一标识的实现方式
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > 获取穿戴设备SN号作为设备唯一标识的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:ede83d723dac3b8bb2ead000aa3006f18281f2cce01fcdbedb5b39dec0e1be4b
---

## 问题现象

运动表GT系列如何获取设备ID？

## 背景知识

穿戴设备不支持OAID、AAID等设备唯一标识。

## 解决方案

当前没有直接获取穿戴设备唯一ID的接口。可通过手机获取连接穿戴设备的SN号，调用[wearengine\_api#getSerialNumber](../harmonyos-references/wearengine_api.md#getserialnumber)接口实现。
