---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-36
title: 应用使用蓝牙功能时闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用使用蓝牙功能时闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dcb8b5cfa6341a14116b1dee5e4a7d094001901cfd9ddfae0f1f017d26e5be6b
---

## 问题现象

使用蓝牙添加其他设备时，关闭蓝牙并退出页面，应用闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。

## 问题定位

1. 从faultlogger目录下获取到应用的JsCrash故障日志，故障原因是Error，故障信息为BusinessError 2900003: Bluetooth disabled，蓝牙开关已关闭。

   ```screen
   Error name:Error
   Error message:BusinessError 2900003: Bluetooth disabled.
   Error code:2900003
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
   at closeScan (default|@ohos/common|1.0.0|src/main/ets/bluetooth/Scan.ts:40:40)
   at aboutToDisappear (default|device|1.0.0|src/main/ets/components/BTScan.ts:62:62)
   ```
2. 从堆栈中看出，在退出界面时，应用调用了closeScan函数，执行了关闭蓝牙扫描操作。对于停止蓝牙扫描接口，例如[ble.stopBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestopblescan)，如果在蓝牙已关闭的情况下调用，就会出现Bluetooth disabled异常。

## 分析结论

应用在蓝牙已关闭的情况下，调用了停止蓝牙扫描的接口，导致上报了JsCrash故障并闪退。

## 修改建议

因为用户在扫描过程中关闭了蓝牙，扫描已经终止，所以只需使用try-catch捕获停止扫描接口抛出的蓝牙未开启异常即可。

推荐使用API version 15开始支持的多路扫描方式，详情参考[低功耗蓝牙](../harmonyos-guides/bluetooth-ble.md)。
