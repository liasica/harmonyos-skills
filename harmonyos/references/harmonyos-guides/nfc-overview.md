---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-overview
title: NFC服务开发概述
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > NFC > NFC服务开发概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b50b9c67873f9792c1d9924e55b690c1887209d0bf607f800ed85a363b722460
---

## 概述

NFC英文全称Near Field Communication，是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。NFC服务提供NFC开关控制、NFC标签读写、NFC卡模拟等业务功能。

## 模块介绍

### NFC开关模块

NFC开关模块，提供了打开NFC和关闭NFC功能。打开或关闭NFC的应用程序，需要声明权限"ohos.permission.MANAGE\_SECURE\_SETTINGS"，该权限只有系统应用才能声明。因此，只有系统应用才能打开或关闭NFC。详情请参考[@ohos.nfc.controller API参考](../harmonyos-references/js-apis-nfccontroller.md)。

### NFC标签读写模块

NFC标签读写模块，提供了NFC标签的发现和分发给应用程序，以及应用程序通过NFC标签读写接口访问NFC标签的能力。应用程序需要按照规定的格式来声明NFC标签读写能力，只有声明后应用程序才能收到NFC标签的分发。详情请参考[@ohos.nfc.tag API参考](../harmonyos-references/js-apis-nfctag.md)。

### NFC卡模拟模块

NFC卡模拟模块，提供了NFC的刷卡业务，电子设备和读卡器触碰完成刷卡。应用程序需要按照规定的格式来声明NFC卡模拟能力，只有声明后应用程序才能够具备刷卡能力。详情请参考[@ohos.nfc.cardEmulation API参考](../harmonyos-references/js-apis-cardemulation.md)。

## 模拟器支持情况

NFC模块暂不支持模拟器。
