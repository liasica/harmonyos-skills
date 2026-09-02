---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-cdsm-information
title: 获取星闪合作设备集合信息
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 获取星闪合作设备集合信息
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:395598ecdd3ad1e7528ca8638cddac74dc9e34c9fea7aa515266464010ae82a9
---

## 场景介绍

从6.1.1(24)开始支持获取星闪合作设备集合信息。

合作设备集合是由多个成员设备协同提供特定服务的整体，例如一副星闪耳机包含左右两个耳机单元。当配对的外设属于某个合作设备集合时，通过[getPairedDevices](../harmonyos-references/nearlink-manager.md#getpaireddevices)接口仅能获取该集合中首个配对的成员设备，无法直接获取其他成员设备信息。作为集合使用者，可通过主动查询或订阅通知的方式，获取该合作设备集合内所有成员设备的完整信息。

更多技术细节可参考[星闪标准](https://www.isla.org.cn/trial)《星闪无线通信系统 基础应用层 合作设备集合管理》。

## 接口说明

提供获取合作设备集合信息的方式，主动查询和订阅信息变化。

| 接口名 | 描述 |
| --- | --- |
| [createCdsmClient](../harmonyos-references/nearlink-cdsm.md#createcdsmclient)(address: string): [CdsmClient](../harmonyos-references/nearlink-cdsm.md#cdsmclient) | 创建合作设备集合客户端实例。 |
| [getCdsmInfo](../harmonyos-references/nearlink-cdsm.md#getcdsminfo)(): [CdsmInfo](../harmonyos-references/nearlink-cdsm.md#cdsminfo) | 主动查询合作设备集合里所有成员设备的信息。 |
| [onCdsmInfoChange](../harmonyos-references/nearlink-cdsm.md#oncdsminfochange)(callback: Callback<CdsmInfo>): void | 订阅远端设备合作设备集合信息变化事件。使用callback异步回调。 |
| [offCdsmInfoChange](../harmonyos-references/nearlink-cdsm.md#offcdsminfochange)(callback?: Callback<CdsmInfo>): void | 取消订阅远端设备合作设备集合信息变化事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { cdsm, manager, remoteDevice } from '@kit.NearLinkKit';
   ```
2. 创建合作设备集合客户端实例，参数addr是通过[getPairedDevices](../harmonyos-references/nearlink-manager.md#getpaireddevices)获取的设备地址，并且此设备是合作设备集合的成员设备。

   ```typescript
   @State deviceAddress: string = '00:11:22:33:AA:FF';
   cdsmClient: cdsm.CdsmClient | null = null;
   // ...
   try {
     this.cdsmClient = cdsm.createCdsmClient(this.deviceAddress);
     hilog.info(this.domainId, this.logTag, `Create CDSM client: ${JSON.stringify(this.cdsmClient)}`);
     // ...
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 主动查询合作设备集合里所有成员设备的信息。

   ```typescript
   try {
     if (this.cdsmClient) {
       let cdsmInformation: cdsm.CdsmInfo = this.cdsmClient.getCdsmInfo();
       hilog.info(this.domainId, this.logTag, `CDSM info: ${JSON.stringify(cdsmInformation)}`);
       // ...
     }
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
4. 通过注册的方式订阅合作设备集合成员设备的信息变化。

   ```typescript
   let cdsmCallback: (data: cdsm.CdsmInfo) => void = (data: cdsm.CdsmInfo) => {
     hilog.info(this.domainId, this.logTag, `CDSM info changed: ${JSON.stringify(data)}`);
     // ...
   };
   try {
     if (this.cdsmClient) {
       this.cdsmClient.onCdsmInfoChange(cdsmCallback);
       // ...
     }
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
5. 取消订阅合作设备集合成员设备的信息变化。

   ```typescript
   try {
     if (this.cdsmClient) {
       this.cdsmClient.offCdsmInfoChange();
       // ...
     }
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
