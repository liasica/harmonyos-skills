---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-scan
title: 发起星闪扫描
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 发起星闪扫描
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7a17fd313af630a1a9ebada87f2350df0a702c228610c2fddd04bd1f90caa861
---

## 场景介绍

发起星闪扫描，可以扫描到正在发送星闪广播的外围设备。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [startScan](../harmonyos-references/nearlink-scan.md#startscan)(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void> | 启动星闪扫描。使用Promise异步回调。 |
| [stopScan](../harmonyos-references/nearlink-scan.md#stopscan)(): Promise<void> | 停止星闪扫描。 |
| [on](../harmonyos-references/nearlink-scan.md#on-devicefound)(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void | 订阅扫描结果。使用callback异步回调。 |
| [off](../harmonyos-references/nearlink-scan.md#off-devicefound)(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void | 取消订阅扫描结果。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { scan } from '@kit.NearLinkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { util } from '@kit.ArkTS';
   ```
2. 定义扫描结果回调，解析扫描结果。

   ```typescript
   const SLE_ADV_DATA_TYPE_DISCOVERY_LEVEL = 0x01;
   const SLE_ADV_DATA_TYPE_SERVICE_DATA_16BIT_UUID = 0x03;
   const SLE_ADV_DATA_TYPE_SERVICE_DATA_128BIT_UUID = 0x04;
   const SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_16BIT_SERVICE_UUIDS = 0x05;
   const SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_128BIT_SERVICE_UUIDS = 0x06;
   const SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_16BIT_SERVICE_UUIDS = 0x07;
   const SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_128BIT_SERVICE_UUIDS = 0x08;
   const SLE_ADV_DATA_TYPE_SHORTENED_LOCAL_NAME = 0x0A;
   const SLE_ADV_DATA_TYPE_COMPLETE_LOCAL_NAME = 0x0B;
   const SLE_ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA = 0xFF;

   const NEARLINK_UUID_16_BIT_LENGTH = 2;
   const NEARLINK_UUID_128_BIT_LENGTH = 16;

   const NEARLINK_MANUFACTURE_ID_LENGTH = 2;
   // ...
   parseScanResult(data: ArrayBuffer) {
     let advData = new Uint8Array(data);
     if (advData.byteLength == 0) {
       hilog.info(this.domainId, this.logTag, `Nothing, adv data length is 0`);
       return;
     }
     hilog.info(this.domainId, this.logTag, `advData: ${JSON.stringify(advData)}`);

     let discoveryLevel: number = -1;
     let serviceData: Record<string, Uint8Array> = {};
     let standardUuids: string[] = [];
     let specificUuids: string[] = [];
     let localName: string = '';
     let manufactureSpecificData: Record<number, Uint8Array> = {};

     let curPos: number= 0;
     while (curPos < advData.byteLength) {
       let advDataType: number = advData[curPos++];
       let advDataLength: number = advData[curPos++];
       if (advDataLength == 0) {
         break;
       }
       switch (advDataType) {
         case SLE_ADV_DATA_TYPE_DISCOVERY_LEVEL: // Discovery level
           discoveryLevel = advData[curPos];
           break;
         case SLE_ADV_DATA_TYPE_SERVICE_DATA_16BIT_UUID: // Standard service data information
           this.parseServiceData(NEARLINK_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, serviceData);
           break;
         case SLE_ADV_DATA_TYPE_SERVICE_DATA_128BIT_UUID: // Customized service data information
           this.parseServiceData(NEARLINK_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, serviceData);
           break;
         case SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_16BIT_SERVICE_UUIDS: // Complete standard service list
         case SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_16BIT_SERVICE_UUIDS: // Incomplete standard service list
           this.parseServiceUuid(NEARLINK_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, standardUuids);
           break;
         case SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_128BIT_SERVICE_UUIDS: // Complete customized service list
         case SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_128BIT_SERVICE_UUIDS: // Incomplete customized service list
           this.parseServiceUuid(NEARLINK_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, specificUuids);
           break;
         case SLE_ADV_DATA_TYPE_SHORTENED_LOCAL_NAME: // Incomplete device local name
         case SLE_ADV_DATA_TYPE_COMPLETE_LOCAL_NAME: // Complete device local name
           let tmpName: Uint8Array = advData.slice(curPos, curPos + advDataLength);
           let decoder = util.TextDecoder.create('utf-8');
           localName = decoder.decodeToString(new Uint8Array(tmpName));
           break;
         case SLE_ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA: // Manufacturer specific data
           this.parseManufactureData(curPos, advDataLength, advData, manufactureSpecificData);
           break;
         default:
           break;
       }
       hilog.info(this.domainId, this.logTag, `discoveryLevel: ${discoveryLevel},
         serviceData: ${JSON.stringify(serviceData)}, standardUuids: ${serviceData}, specificUuids: ${specificUuids},
         localName: ${localName}, manufactureSpecificData: ${JSON.stringify(manufactureSpecificData)}`);
       curPos += advDataLength;
     }
   }

   parseServiceData (uuidLength: number, curPos: number, advDataLength: number,
     advData: Uint8Array, serviceData: Record<string, Uint8Array>) {
     let tmpUuid: Uint8Array = advData.slice(curPos, curPos + uuidLength);
     let uuidStr: string = this.getUuidFromUint8Array(uuidLength, tmpUuid);
     let tmpValue: Uint8Array = advData.slice(curPos + uuidLength, curPos + advDataLength);
     serviceData[uuidStr] = tmpValue;
   }

   parseServiceUuid (uuidLength: number, curPos: number, advDataLength: number,
     advData: Uint8Array, serviceUuids: string[]) {
     while (advDataLength > 0) {
       let tmpData: Uint8Array = advData.slice(curPos, curPos + uuidLength);
       serviceUuids.push(this.getUuidFromUint8Array(uuidLength, tmpData));
       advDataLength -= uuidLength;
       curPos += uuidLength;
     }
   }

   parseManufactureData(curPos: number, advDataLength: number,
     advData: Uint8Array, manufactureSpecificData: Record<number, Uint8Array>) {
     let manufactureId: number = (advData[curPos + 1] << 8) + advData[curPos];
     let tmpValue: Uint8Array = advData.slice(curPos + NEARLINK_MANUFACTURE_ID_LENGTH, curPos + advDataLength);
     manufactureSpecificData[manufactureId] = tmpValue;
   }

   getUuidFromUint8Array(uuidLength: number, uuidData: Uint8Array): string {
     let uuid: string = '';
     let temp: string = '';
     for (let i = uuidLength - 1; i > -1; i--) {
       temp += uuidData[i].toString(16).padStart(2, '0');
     }
     switch (uuidLength) {
       case NEARLINK_UUID_16_BIT_LENGTH:
         uuid = `FFFFFFFF-1234-5678-ABCD-00000000${temp}`;
         break;
       case NEARLINK_UUID_128_BIT_LENGTH:
         uuid = `${temp.substring(0, 8)}-${temp.substring(8, 12)}-${temp.substring(12, 16)}-${temp.substring(16,
           20)}-${temp.substring(20, 32)}`;
         break;
       default:
         break;
     }
     return uuid;
   }
   ```
3. 订阅扫描结果。

   ```typescript
   let onScanResultsCallback:(data: Array<scan.ScanResults>) => void = (data: Array<scan.ScanResults>) => {
     for (let index = 0; index < data.length; index++) {
       hilog.info(this.domainId, this.logTag,
         `Scan result addr: ${data[index].address} name: ${data[index].deviceName}`);
       this.parseScanResult(data[index].data);
     }
     AppStorage.setOrCreate('scanResults', data);
   };
   try {
     scan.on('deviceFound', onScanResultsCallback);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
4. 配置扫描参数，扫描过滤器配置期望的设备名称、地址等信息。

   **注意** 

   1. 扫描过滤器至少携带一个过滤条件，否则扫描过滤器无效。
   2. 过滤器可以配置多组，组之间的条件是或的关系，如步骤5所示。
   3. 一组过滤器内的条件是与的关系，如下示例：address和deviceName同时满足才会上报。

   ```typescript
   @State remoteDeviceName: string = 'deviceName1';
   @State address: string = '11:22:33:44:AA:BB';
   let scanFilter1: scan.ScanFilters = {
     deviceName: this.remoteDeviceName
   };
   let scanFilter2: scan.ScanFilters = {
     address: this.address
   };
   let scanOptions: scan.ScanOptions = {
     scanMode: scan.ScanMode.SCAN_MODE_LOW_POWER
   };
   ```
5. 开启星闪扫描，参数配置在步骤4中构造。

   ```typescript
   try {
     scan.startScan([scanFilter1, scanFilter2], scanOptions).then(() => {
       hilog.info(this.domainId, this.logTag, `Start scan success`);
     }).catch ((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
6. 停止星闪扫描。

   ```typescript
   try {
     scan.stopScan().then(() => {
       hilog.info(this.domainId, this.logTag, `Stop scan success`);
     }).catch ((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
7. 取消订阅扫描结果，其中onReceiveEvent是在步骤3中注册的回调函数。

   ```typescript
   try {
     scan.off('deviceFound');
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```

## 示例代码

星闪扫描场景可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/ScanConfigPage.ets中的实现方法。
