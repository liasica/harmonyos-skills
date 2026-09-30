---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-cdsm-information-guide
title: 获取星闪合作设备集合信息
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 获取星闪合作设备集合信息
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:18c2ec0879518510407f3616fa624824ca9ef0f2f656353e0b6a2b8c35751724
---

## 场景介绍

合作设备集合（Coordinated Devices Set，CDS）是由多个成员设备协同提供特定服务的整体，例如一副星闪耳机包含左右两个耳机单元。当配对的外围设备属于某个合作设备集合时，通过[getPairedDevices()](../harmonyos-references/js-apis-nearlink-manager.md#managergetpaireddevices)接口仅能获取该集合中首个配对的成员设备，无法直接获取其他成员设备信息。作为集合使用者，可通过合作设备集合管理（Coordinated Devices Set Management，CDSM）能力，以主动查询或订阅通知的方式，获取该合作设备集合内所有成员设备的完整信息。

开发前需按[开发准备](nearlink-preparations-guide.md)完成权限声明与运行时申请，并确保设备已开启星闪（参见[开发准备 > 查询星闪开关状态](nearlink-preparations-guide.md#查询星闪开关状态)），且已配对设备属于某个合作设备集合，已通过[getPairedDevices()](../harmonyos-references/js-apis-nearlink-manager.md#managergetpaireddevices)获取集合中成员设备的地址。

## 接口说明

提供获取合作设备集合信息的方式，主动查询和订阅信息变化，完整的API说明以及示例代码请参考：[@ohos.nearlink.cdsm (星闪合作设备集合管理能力)](../harmonyos-references/js-apis-nearlink-cdsm.md)。

| 接口名 | 描述 |
| --- | --- |
| createCdsmClient(address: string): CdsmClient | 创建合作设备集合客户端实例。 |
| getCdsmInfo(): CdsmInfo | 主动查询合作设备集合里所有成员设备的信息。 |
| onCdsmInfoChange(callback: Callback<CdsmInfo>): void | 订阅远端设备合作设备集合信息变化事件。使用callback异步回调。 |
| offCdsmInfoChange(callback?: Callback<CdsmInfo>): void | 取消订阅远端设备合作设备集合信息变化事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { cdsm } from '@kit.ConnectivityKit';
   ```
2. 定义CDSM客户端变量与设备地址变量，供后续步骤使用。其中deviceAddress是通过[getPairedDevices()](../harmonyos-references/js-apis-nearlink-manager.md#managergetpaireddevices)获取的设备地址，且该设备是合作设备集合的成员设备。

   ```typescript
   let cdsmClient: cdsm.CdsmClient;
   let deviceAddress: string;
   ```
3. 创建合作设备集合客户端实例。

   ```typescript
   try {
     cdsmClient = cdsm.createCdsmClient(deviceAddress);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
4. 主动查询合作设备集合里所有成员设备的信息。

   ```typescript
   try {
     let cdsmInfo: cdsm.CdsmInfo = cdsmClient.getCdsmInfo();
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
5. 通过注册的方式订阅合作设备集合成员设备的信息变化。

   ```typescript
   try {
     cdsmClient.onCdsmInfoChange((data: cdsm.CdsmInfo) => {
       hilog.info(0x0000, 'testTag', `CDSM info changed: ${JSON.stringify(data)}`);
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
6. 取消订阅合作设备集合成员设备的信息变化。

   ```typescript
   try {
     cdsmClient.offCdsmInfoChange();
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
