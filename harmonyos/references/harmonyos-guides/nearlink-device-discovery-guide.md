---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-device-discovery-guide
title: 发现星闪设备
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 发现星闪设备
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:d068cb49c3b5258c0e38877c028cdf2de37a238cc70f7041239efb150e4670c9
---

星闪设备发现包括广播与扫描两个环节：外围设备通过发送星闪广播宣告自身，中心设备通过发起星闪扫描发现正在广播的外围设备。广播与扫描可独立使用，也可配合实现设备间的发现与连接。

开发前需按[开发准备](nearlink-preparations-guide.md)完成权限声明与运行时申请，并确保设备已开启星闪（参见[开发准备 > 查询星闪开关状态](nearlink-preparations-guide.md#查询星闪开关状态)）。

## 发起星闪广播

发送星闪广播，广播数据可以被支持星闪能力的中心设备扫描到。

### 接口说明

发送星闪广播，完整的API说明以及示例代码请参考：[@ohos.nearlink.advertising (星闪广播能力)](../harmonyos-references/js-apis-nearlink-advertising.md)。

| 接口名 | 描述 |
| --- | --- |
| startAdvertising(advertisingParams: AdvertisingParams): Promise<number> | 启动星闪广播。使用Promise异步回调。 |
| stopAdvertising(advertisingId: number): Promise<void> | 停止星闪广播。使用Promise异步回调。 |
| onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void | 订阅星闪广播状态变化事件。使用callback异步回调。 |
| offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void | 取消订阅星闪广播状态变化事件。使用callback异步回调。 |

### 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { advertising } from '@kit.ConnectivityKit';
   ```
2. 订阅星闪广播状态变化事件。

   ```typescript
   try {
     advertising.onAdvertisingStateChange((data: advertising.AdvertisingStateChangeInfo) => {
       hilog.info(0x0000, 'testTag',
         `Advertising state changed: id=${data.advertisingId}, state=${data.state}`);
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 构造用户需要的广播参数及数据。广播中携带的服务UUID必须为自定义UUID，参见[星闪常见问题 > 标准UUID与自定义UUID有什么区别](nearlink-faq-guide.md#标准uuid与自定义uuid有什么区别)。

   ```typescript
   let manufacturerData = new Uint8Array([0x01, 0x02, 0x03, 0x04]);

   let serviceValueBuffer = new Uint8Array(4);
   serviceValueBuffer[0] = 0x0A;
   serviceValueBuffer[1] = 0x0B;
   serviceValueBuffer[2] = 0x0C;
   serviceValueBuffer[3] = 0x0D;

   let setting: advertising.AdvertisingSettings = {
     interval: 160,
     power: advertising.TxPowerMode.ADV_TX_POWER_MEDIUM,
     isConnectable: true
   };

   let manufactureDataUnit: advertising.ManufacturerData = {
     manufacturerId: 0x1234,
     manufacturerData: manufacturerData.buffer
   };

   let serviceDataUnit: advertising.ServiceData = {
     serviceUuid: 'FFFFFFFF-1234-5678-ABCD-000000001254',
     serviceData: serviceValueBuffer.buffer
   };

   let advData: advertising.AdvertisingData = {
     serviceUuids: ['FFFFFFFF-1234-5678-ABCD-000000001254'],
     manufacturerData: [manufactureDataUnit],
     serviceData: [serviceDataUnit],
     includeDeviceName: true
   };

   let advertisingParams: advertising.AdvertisingParams = {
     advertisingSettings: setting,
     advertisingData: advData
   };
   ```
4. 启动星闪广播，返回advId表示本次广播的ID。其中advertisingParams为第3步构造的广播参数。

   ```typescript
   try {
     let advId: number = await advertising.startAdvertising(advertisingParams);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
5. 停止星闪广播。其中advId为第4步启动广播时返回的广播ID。

   ```typescript
   try {
     await advertising.stopAdvertising(advId);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
6. 取消订阅星闪广播状态变化事件。

   ```typescript
   try {
     advertising.offAdvertisingStateChange();
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```

## 发起星闪扫描

发起星闪扫描，可以扫描到正在发送星闪广播的外围设备。

### 接口说明

发起星闪扫描，完整的API说明以及示例代码请参考：[@ohos.nearlink.scan (星闪扫描能力)](../harmonyos-references/js-apis-nearlink-scan.md)。

| 接口名 | 描述 |
| --- | --- |
| startScan(filters: Array<ScanFilters> | null, options?: ScanOptions): Promise<void> | 启动星闪扫描。使用Promise异步回调。 |
| stopScan(): Promise<void> | 停止星闪扫描。使用Promise异步回调。 |
| onDeviceFound(callback: Callback<Array<ScanResults>>): void | 订阅星闪扫描结果。使用callback异步回调。 |
| offDeviceFound(callback?: Callback<Array<ScanResults>>): void | 取消订阅星闪扫描结果。使用callback异步回调。 |

### 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { scan } from '@kit.ConnectivityKit';
   import { util } from '@kit.ArkTS';
   ```
2. 订阅扫描结果。为避免重复订阅，先调用[offDeviceFound()](../harmonyos-references/js-apis-nearlink-scan.md#scanoffdevicefound)取消已有订阅，再调用[onDeviceFound()](../harmonyos-references/js-apis-nearlink-scan.md#scanondevicefound)订阅扫描结果，当扫描到设备时将触发回调。回调中调用的parseScanResult解析方法在步骤3中定义。

   ```typescript
   try {
     scan.offDeviceFound();
     scan.onDeviceFound((data: scan.ScanResults[]) => {
       data.forEach((item) => {
         hilog.info(0x0000, 'testTag',
           `Scan result: addr=${item.address}, name=${item.deviceName}, rssi=${item.rssi}`);
         this.parseScanResult(item.data);
       });
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 解析扫描结果（广播数据）。扫描结果中的data字段为广播报文原始数据，采用TLV（类型-长度-值）格式组织，各数据类型定义参见[星闪标准](https://www.isla.org.cn/trial)《星闪无线通信系统 基础服务层 设备发现与服务管理》中设备公开信息的数据类型。通过解析可获取发现等级、服务数据、服务UUID列表、本地名称与厂商数据等信息：

   ```typescript
   const ADV_DATA_TYPE_DISCOVERY_LEVEL = 0x01; // 发现等级
   const ADV_DATA_TYPE_SERVICE_DATA_16_BIT_UUID = 0x03; // 标准服务数据信息
   const ADV_DATA_TYPE_SERVICE_DATA_128_BIT_UUID = 0x04; // 自定义服务数据信息
   const ADV_DATA_TYPE_COMPLETE_LIST_16_BIT_SERVICE_UUIDS = 0x05; // 完整标准服务标识列表
   const ADV_DATA_TYPE_COMPLETE_LIST_128_BIT_SERVICE_UUIDS = 0x06; // 完整自定义服务标识列表
   const ADV_DATA_TYPE_INCOMPLETE_LIST_16_BIT_SERVICE_UUIDS = 0x07; // 部分标准服务标识列表
   const ADV_DATA_TYPE_INCOMPLETE_LIST_128_BIT_SERVICE_UUIDS = 0x08; // 部分自定义服务标识列表
   const ADV_DATA_TYPE_SHORTENED_LOCAL_NAME = 0x0A; // 设备缩写本地名称
   const ADV_DATA_TYPE_COMPLETE_LOCAL_NAME = 0x0B; // 设备完整本地名称
   const ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA = 0xFF; // 厂商自定义信息

   const NEARLINK_UUID_16_BIT_LENGTH = 2;
   const NEARLINK_UUID_128_BIT_LENGTH = 16;
   const NEARLINK_MANUFACTURER_ID_LENGTH = 2;
   // 标准UUID的基础标识前缀（112比特）
   const STANDARD_UUID_BASE_PREFIX = '37BEA880-FC70-11EA-B720-00000000';

   // 广播报文数据的解析结果
   interface ScanResultData {
     discoveryLevel: number;
     serviceData: Record<string, Uint8Array>;
     standardServiceUuids: string[];
     customServiceUuids: string[];
     localName: string;
     manufacturerData: Record<number, Uint8Array>;
   }
   ```

   ```typescript
   parseScanResult(data: ArrayBuffer): ScanResultData {
     let advData = new Uint8Array(data);
     let result: ScanResultData = {
       discoveryLevel: -1,
       serviceData: {},
       standardServiceUuids: [],
       customServiceUuids: [],
       localName: '',
       manufacturerData: {}
     };
     if (advData.byteLength === 0) {
       hilog.info(0x0000, 'testTag', 'adv data length is 0');
       return result;
     }
     let curPos = 0;
     while (curPos < advData.byteLength) {
       // 每条数据由1字节类型、1字节长度和数据内容组成
       let dataType = advData[curPos++];
       let dataLength = advData[curPos++];
       if (dataLength === 0) {
         break; // 长度为0表示数据结束
       }
       switch (dataType) {
         case ADV_DATA_TYPE_DISCOVERY_LEVEL:
           result.discoveryLevel = advData[curPos];
           break;
         case ADV_DATA_TYPE_SERVICE_DATA_16_BIT_UUID:
           this.parseServiceData(NEARLINK_UUID_16_BIT_LENGTH, curPos, dataLength, advData, result.serviceData);
           break;
         case ADV_DATA_TYPE_SERVICE_DATA_128_BIT_UUID:
           this.parseServiceData(NEARLINK_UUID_128_BIT_LENGTH, curPos, dataLength, advData, result.serviceData);
           break;
         case ADV_DATA_TYPE_COMPLETE_LIST_16_BIT_SERVICE_UUIDS:
         case ADV_DATA_TYPE_INCOMPLETE_LIST_16_BIT_SERVICE_UUIDS:
           this.parseServiceUuids(NEARLINK_UUID_16_BIT_LENGTH, curPos, dataLength, advData,
             result.standardServiceUuids);
           break;
         case ADV_DATA_TYPE_COMPLETE_LIST_128_BIT_SERVICE_UUIDS:
         case ADV_DATA_TYPE_INCOMPLETE_LIST_128_BIT_SERVICE_UUIDS:
           this.parseServiceUuids(NEARLINK_UUID_128_BIT_LENGTH, curPos, dataLength, advData,
             result.customServiceUuids);
           break;
         case ADV_DATA_TYPE_SHORTENED_LOCAL_NAME:
         case ADV_DATA_TYPE_COMPLETE_LOCAL_NAME:
           let decoder = util.TextDecoder.create('utf-8');
           result.localName = decoder.decodeToString(advData.slice(curPos, curPos + dataLength));
           break;
         case ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA:
           this.parseManufacturerData(curPos, dataLength, advData, result.manufacturerData);
           break;
         default:
           break;
       }
       curPos += dataLength; // 移动到下一条数据
     }
     hilog.info(0x0000, 'testTag',
       `discoveryLevel: ${result.discoveryLevel}, serviceData: ${JSON.stringify(result.serviceData)}, ` +
       `standardServiceUuids: ${JSON.stringify(result.standardServiceUuids)}, ` +
       `customServiceUuids: ${JSON.stringify(result.customServiceUuids)}, ` +
       `localName: ${result.localName}, manufacturerData: ${JSON.stringify(result.manufacturerData)}`);
     return result;
   }

   parseServiceData(uuidLength: number, curPos: number, dataLength: number,
     advData: Uint8Array, serviceData: Record<string, Uint8Array>): void {
     let uuid = advData.slice(curPos, curPos + uuidLength);
     let value = advData.slice(curPos + uuidLength, curPos + dataLength);
     serviceData[this.getUuidFromUint8Array(uuidLength, uuid)] = value;
   }

   parseServiceUuids(uuidLength: number, curPos: number, dataLength: number,
     advData: Uint8Array, serviceUuids: string[]): void {
     while (dataLength > 0) {
       let uuid = advData.slice(curPos, curPos + uuidLength);
       serviceUuids.push(this.getUuidFromUint8Array(uuidLength, uuid));
       dataLength -= uuidLength;
       curPos += uuidLength;
     }
   }

   parseManufacturerData(curPos: number, dataLength: number,
     advData: Uint8Array, manufacturerData: Record<number, Uint8Array>): void {
     let manufacturerId = (advData[curPos + 1] << 8) + advData[curPos];
     let value = advData.slice(curPos + NEARLINK_MANUFACTURER_ID_LENGTH, curPos + dataLength);
     manufacturerData[manufacturerId] = value;
   }

   getUuidFromUint8Array(uuidLength: number, uuidData: Uint8Array): string {
     let hex = '';
     for (let i = uuidLength - 1; i > -1; i--) {
       hex += uuidData[i].toString(16).padStart(2, '0');
     }
     switch (uuidLength) {
       case NEARLINK_UUID_16_BIT_LENGTH:
         return STANDARD_UUID_BASE_PREFIX + hex;
       case NEARLINK_UUID_128_BIT_LENGTH:
         return `${hex.substring(0, 8)}-${hex.substring(8, 12)}-${hex.substring(12, 16)}-` +
           `${hex.substring(16, 20)}-${hex.substring(20, 32)}`;
       default:
         return '';
     }
   }
   ```
4. 配置扫描过滤器，设置期望的设备名称、地址等信息。过滤器至少携带一个过滤条件，可配置多个，多个过滤器之间的条件为或的关系，单个过滤器内的条件为与的关系。filters传null表示不过滤，传空数组或所有字段均为空的过滤器数组时，将返回[36100042 数组为空](../harmonyos-references/errorcode-nearlink-service.md#section36100042-数组为空)错误。

   ```typescript
   let deviceNameFilter: string = 'deviceName1';
   let addressFilter: string = '11:22:33:44:AA:BB';

   let filters: scan.ScanFilters[] = [];
   if (deviceNameFilter.length > 0) {
     filters.push({ deviceName: deviceNameFilter });
   }
   if (addressFilter.length > 0) {
     filters.push({ address: addressFilter });
   }
   ```
5. 启动星闪扫描。其中filters为第4步配置的扫描过滤器，scanOptions为扫描参数。

   ```typescript
   try {
     let scanOptions: scan.ScanOptions = {
       scanMode: scan.ScanMode.SCAN_MODE_LOW_POWER
     };
     await scan.startScan(filters, scanOptions);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
6. 停止星闪扫描。

   ```typescript
   try {
     await scan.stopScan();
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
7. 取消订阅扫描结果。

   ```typescript
   try {
     scan.offDeviceFound();
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
