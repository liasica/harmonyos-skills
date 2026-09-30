---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-data-transfer-guide
title: 使用星闪传输数据
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 使用星闪传输数据
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:04af973a4bc919c49f0d141db5f9fd2a23ec2d14f7d5519f51447f479023d20f
---

提供星闪数据传输相关的端口通道建立和数据收发等功能，同一设备可以同时承担数据发送端和接收端的角色。

## 场景介绍

在星闪设备间已建立起逻辑链路的基础上，支持应用基于星闪技术进行设备间的数据传输。逻辑链路是星闪接入层的逻辑信道，为设备间的数据传输提供承载，由系统在设备连接过程中建立，开发者无需直接管理。

开发前需按[开发准备](nearlink-preparations-guide.md)完成权限声明与运行时申请，并确保设备已开启星闪（参见[开发准备 > 查询星闪开关状态](nearlink-preparations-guide.md#查询星闪开关状态)）；端口UUID必须为自定义UUID（参见[星闪常见问题 > 标准UUID与自定义UUID有什么区别](nearlink-faq-guide.md#标准uuid与自定义uuid有什么区别)），发送端与接收端UUID必须相同。

**说明** 

1. 端口通道不保证链路加密。如需加密数据传输，需先进行配对流程，通过[startPairing()](../harmonyos-references/js-apis-nearlink-remote-device.md#startpairing)接口发起。
2. 链路是否加密可通过[getAcbState()](../harmonyos-references/js-apis-nearlink-remote-device.md#getacbstate)接口查询，ENCRYPTED状态表示链路已加密。

## 接口说明

使用星闪传输数据，完整的API说明以及示例代码请参考：[@ohos.nearlink.dataTransfer (星闪数据传输能力)](../harmonyos-references/js-apis-nearlink-data-transfer-api.md)。

| 接口名 | 描述 |
| --- | --- |
| createPort(uuid: string): void | 注册端口通道。 |
| destroyPort(uuid: string): void | 销毁端口通道。 |
| connect(params: ConnectionParams): Promise<void> | 连接远端设备，建立端口通道。使用Promise异步回调。 |
| disconnect(params: ConnectionParams): Promise<void> | 断开端口通道连接。使用Promise异步回调。 |
| writeData(params: DataParams): Promise<void> | 通过设备地址和UUID向远端设备发数据。使用Promise异步回调。 |
| onConnectionStateChanged(callback: Callback<ConnectionResult>): void | 订阅端口通道连接状态变更事件。使用callback异步回调。 |
| onReadData(callback: Callback<DataParams>): void | 订阅端口通道数据接收事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { dataTransfer } from '@kit.ConnectivityKit';
   ```
2. 定义端口UUID与设备地址变量，供后续步骤使用。

   ```typescript
   let serviceUuid: string = 'FFFFFFFF-1234-5678-ABCD-000000001244';
   let chosenDeviceAddr: string;
   ```
3. 注册端口通道，发送端和接收端均需注册。

   ```typescript
   try {
     dataTransfer.createPort(serviceUuid);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
4. 订阅端口通道连接状态变更事件。不再需要订阅事件时，调用[offConnectionStateChanged()](../harmonyos-references/js-apis-nearlink-data-transfer-api.md#datatransferoffconnectionstatechanged)取消订阅。

   ```typescript
   try {
     dataTransfer.onConnectionStateChanged((data: dataTransfer.ConnectionResult) => {
       hilog.info(0x0000, 'testTag', `Connection state: ${JSON.stringify(data)}`);
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
5. 订阅端口通道数据接收事件。不再需要订阅事件时，调用[offReadData()](../harmonyos-references/js-apis-nearlink-data-transfer-api.md#datatransferoffreaddata)取消订阅。

   ```typescript
   try {
     dataTransfer.onReadData((data: dataTransfer.DataParams) => {
       hilog.info(0x0000, 'testTag', `Data received: ${JSON.stringify(data)}`);
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
6. 连接远端设备，建立端口通道。其中chosenDeviceAddr为从[发起星闪扫描](nearlink-device-discovery-guide.md#发起星闪扫描)结果中选择的设备地址，UUID需与步骤3中注册的保持一致。

   ```typescript
   try {
     let params: dataTransfer.ConnectionParams = {
       address: chosenDeviceAddr,
       uuid: serviceUuid,
       transferMode: dataTransfer.TransferMode.BASIC
     };
     await dataTransfer.connect(params);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
7. 通过设备地址和UUID向远端设备发数据。

   **说明** 

   连续多次调用writeData可能导致发送队列拥塞而发送失败。建议通过setInterval设置数据发送时间间隔，推荐间隔为10ms（参见[星闪常见问题 > 连续调用writeData为什么会发送失败](nearlink-faq-guide.md#连续调用writedata为什么会发送失败)）。

   ```typescript
   try {
     // 使用固定示例数据填充负载，实际开发中替换为业务数据
     let dataBuffer = new ArrayBuffer(4);
     let data = new Uint8Array(dataBuffer);
     data[0] = 0x01;
     data[1] = 0x02;
     data[2] = 0x03;
     data[3] = 0x04;

     let params: dataTransfer.DataParams = {
       address: chosenDeviceAddr,
       uuid: serviceUuid,
       data: dataBuffer
     };
     await dataTransfer.writeData(params);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
8. 断开端口通道连接。

   ```typescript
   try {
     let params: dataTransfer.ConnectionParams = {
       address: chosenDeviceAddr,
       uuid: serviceUuid
     };
     await dataTransfer.disconnect(params);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
9. 销毁端口。数据传输完成后，应用销毁端口，释放端口通道及相关资源。

   ```typescript
   try {
     dataTransfer.destroyPort(serviceUuid);
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
     // ...
   }
   ```
