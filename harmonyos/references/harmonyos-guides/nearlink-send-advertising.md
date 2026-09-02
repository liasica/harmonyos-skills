---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-send-advertising
title: 发送星闪广播
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 发送星闪广播
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8a9d1e3c9f1b5be21c74625f0b67cdb3ce7501f9cf50783c1f19dbc70dd10fe3
---

## 场景介绍

发送星闪广播，广播数据可以被支持星闪能力的中心设备扫描到。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [startAdvertising](../harmonyos-references/nearlink-advertising.md#startadvertising)(advertisingParams: AdvertisingParams): Promise<number> | 启动星闪广播。使用Promise异步回调。 |
| [stopAdvertising](../harmonyos-references/nearlink-advertising.md#stopadvertising)(advertisingId: number): Promise<void> | 停止星闪广播。使用Promise异步回调。 |
| [on](../harmonyos-references/nearlink-advertising.md#on-advertisingstatechange)(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void | 订阅星闪广播状态变化事件。使用callback异步回调。 |
| [off](../harmonyos-references/nearlink-advertising.md#off-advertisingstatechange)(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void | 取消订阅星闪广播状态变化事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { advertising } from '@kit.NearLinkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 订阅星闪广播状态变化事件。

   ```typescript
   let onAdvertisingStateChangeCallback:(data: advertising.AdvertisingStateChangeInfo)
     => void = (data: advertising.AdvertisingStateChangeInfo) => {
     hilog.info(this.domainId, this.logTag, `advertisingId: ${data.advertisingId}`);
     hilog.info(this.domainId, this.logTag, `advertisingState: ${data.state}`);
     // ...
   };
   try {
     advertising.on('advertisingStateChange', onAdvertisingStateChangeCallback);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 构造用户需要的广播参数及数据。

   ```typescript
   let manufactureValueBuffer = new Uint8Array(4);
   manufactureValueBuffer[0] = 1;
   manufactureValueBuffer[1] = 2;
   manufactureValueBuffer[2] = 3;
   manufactureValueBuffer[3] = 4;
   let serviceValueBuffer = new Uint8Array(4);
   serviceValueBuffer[0] = 4;
   serviceValueBuffer[1] = 6;
   serviceValueBuffer[2] = 7;
   serviceValueBuffer[3] = 8;
   hilog.info(this.domainId, this.logTag, `manufactureValueBuffer = ${JSON.stringify(manufactureValueBuffer)}`);
   hilog.info(this.domainId, this.logTag, `serviceValueBuffer = ${JSON.stringify(serviceValueBuffer)}`);
   let setting: advertising.AdvertisingSettings = {
     interval: 160,
     power: advertising.TxPowerMode.ADV_TX_POWER_MEDIUM
   };
   let manufactureDataUnit: advertising.ManufacturerData = {
     manufacturerId: 4567,
     manufacturerData: manufactureValueBuffer.buffer
   };
   let serviceDataUnit: advertising.ServiceData = {
     serviceUuid: 'FFFFFFFF-1234-5678-ABCD-000000001234',
     serviceData: serviceValueBuffer.buffer
   };
   let advData: advertising.AdvertisingData = {
     serviceUuids: ['FFFFFFFF-1234-5678-ABCD-000000001234'],
     manufacturerData: [manufactureDataUnit],
     serviceData: [serviceDataUnit],
     includeDeviceName : true
   };
   let advertisingParams: advertising.AdvertisingParams = {
     advertisingSettings: setting,
     advertisingData: advData
   };
   ```
4. 开启星闪广播，返回advertisingId表示当前广播索引。

   ```typescript
   let advId: number = -1;
   try {
     advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
       advId = advertisingId;
       hilog.info(this.domainId, this.logTag, `advertising id: ${JSON.stringify(advId)}`);
     }).catch ((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
5. 停止星闪广播，其中advId是步骤4开启广播后返回的advertisingId。

   ```typescript
   try {
     advertising.stopAdvertising(advId).then(() => {
       hilog.info(this.domainId, this.logTag, `Stop advertising success`);
     }).catch((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
6. 取消订阅星闪广播状态变化事件。

   ```typescript
   try {
     advertising.off('advertisingStateChange');
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```

## 示例代码

星闪广播场景可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/MainPage.ets中的实现方法。
