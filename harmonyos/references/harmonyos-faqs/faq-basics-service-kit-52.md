---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-52
title: USB批量传输报错“-1”
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > USB批量传输报错“-1”
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:146f85b4b9c8de4756e0d6a5d4836fe8a256912c0b443e8c51bfff68410d26c3
---

## 问题现象

插有存储卡的OTG（USB3.0）的读卡器，usbManager.getDevices()获取设备列表正常、usbManager.requestRight()申请操作权限正常、usbManager.connectDevice()连接设备接口正常、通过usbManager.bulkTransfer()进行读取和写入数据时，返回的number类型的数据，报错“-1”。

## 背景知识

[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)模块是HarmonyOS操作系统中用于管理USB设备的一个功能模块。它提供了多种功能，包括查询USB设备列表、批量数据传输、控制命令传输、权限控制等。

* **设备查询**：可以获取接入主设备的USB设备列表。如果没有任何设备接入，该功能将返回一个空列表。需要注意的是，在开发者模式关闭且没有设备接入时，可能会返回undefined，因此需要对返回值做判空处理。
* **数据传输**：支持批量数据传输和控制命令传输，使得数据交换更加灵活和高效。
* **权限控制**：允许对USB设备的访问和操作进行权限控制，保证系统的安全性。
* **使用示例**：在TypeScript中，可以这样使用@ohos.usbManager模块来获取USB设备列表：

  ```screen
  import { usbManager } from '@kit.BasicServicesKit';

  // 获取USB设备列表
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  console.info(`devicesList = ${devicesList}`);
  ```

## 问题定位

* 检查接口调用是否遗漏。
* 检查端点和传输类型是否匹配。

## 分析结论

根据问题描述是未在bulkTransfer前调用claimInterface所导致，除此之外还需调用setInterface接口。

## 修改建议

使用批量传输方式来传输数据：参考[开发步骤](../harmonyos-guides/bulktransfer.md#开发步骤)。

**说明** 

确认设备interface是否支持模式切换，若[alternateSetting](../harmonyos-references/js-apis-usbmanager.md#usbinterface)支持切换设置，可在传输前调用usbManager.setInterface重新设置interface，使端点和传输类型匹配，保证端点正常通信。

## 常见FAQ

Q：在claimInterface注册通信接口后，是否还需要setInterface设置设备的接口？

A：需要，使用bulkTransfer批量传输，如果不调用setInterface设置通信接口，发送数据失败会return -1。
