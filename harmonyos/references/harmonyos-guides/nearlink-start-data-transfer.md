---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-data-transfer
title: 使用星闪传输数据
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 使用星闪传输数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d730a293836cfe6e2734ca6642fb456b1a82a746859194914f552f11ff56a966
---

提供星闪数传相关的端口通道建立和数据传输等功能，同一设备可以同时承担数据发送端和接收端的角色。

## 场景介绍

从5.1.0(18)开始支持星闪数据传输，包括端口注册、建立连接、读写数据等能力。

星闪设备间已建立起逻辑链路基础上，支持应用基于NearLink技术进行设备间的数据传输。

**说明** 

1. 数据传输通道不保证链路加密。如需加密数传，需先进行配对流程，通过[startPairing](../harmonyos-references/nearlink-remote-device.md#startpairing)接口发起。
2. 链路是否加密可通过[getAcbState](../harmonyos-references/nearlink-remote-device.md#getacbstate)接口查询，ENCRYPTED状态表示链路已加密。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [createPort](../harmonyos-references/nearlink-data-transfer-api.md#createport)(uuid: string): void | 注册端口服务。 |
| [connect](../harmonyos-references/nearlink-data-transfer-api.md#connect)(params: ConnectionParams): Promise<void> | 连接远端设备，建立端口通道。使用Promise异步回调。 |
| [writeData](../harmonyos-references/nearlink-data-transfer-api.md#writedata)(params: DataParams): Promise<void> | 通过设备地址和UUID向远端设备发数据。使用Promise异步回调。 |
| [on](../harmonyos-references/nearlink-data-transfer-api.md#onconnectionstatechanged)(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void | 订阅端口通道连接状态变更事件。使用callback异步回调。 |
| [on](../harmonyos-references/nearlink-data-transfer-api.md#onreaddata)(type: 'readData', callback: Callback<DataParams>): void | 订阅端口通道数据接收事件。使用callback异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { scan, ssap, dataTransfer, constant, remoteDevice } from '@kit.NearLinkKit';
   ```
2. 与远端设备配对加密（可选，如需加密数传，则需执行此步骤）。该步骤执行后，将依据本端与远端设备的输入输出能力标识弹出不同类型的弹窗，需使用者进一步确认。目前支持免输入配对弹窗、数字比较弹窗与通行码鉴权弹窗。

   ```typescript
   @State chosenDeviceAddr: string = '00:11:22:33:AA:FF';
   // ...
   let device: remoteDevice.RemoteDevice;
   try {
     device = remoteDevice.createRemoteDevice(this.chosenDeviceAddr);
     device.startPairing().then(()=>{
       hilog.info(this.domainId, this.logTag, `start pairing success`);
       // ...
     }).catch ((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 注册端口通道，发送端和接收端均需注册，并需保证发送端和接收端UUID相同。

   ```typescript
   const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
   try {
     dataTransfer.createPort(SERVICE_UUID);
     hilog.info(this.domainId, this.logTag, `Create port finished`);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
4. 订阅端口通道连接状态变更事件。

   ```typescript
   let onReceiveConnectionStateEvent:(data: dataTransfer.ConnectionResult) => void =
     (data: dataTransfer.ConnectionResult) => {
     hilog.info(this.domainId, this.logTag, `Port connection state: ${JSON.stringify(data)}`);
     // ...
   };
   try {
     dataTransfer.on('connectionStateChanged', onReceiveConnectionStateEvent);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
5. 订阅端口通道数据接收事件。

   ```typescript
   let onReceiveReadDataEvent:(data: dataTransfer.DataParams) => void = (data: dataTransfer.DataParams) => {
     hilog.info(this.domainId, this.logTag, `Port read data: ${JSON.stringify(data)}`);
   };
   try {
     dataTransfer.on('readData', onReceiveReadDataEvent);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
6. 连接远端设备，建立端口通道。其中UUID要与步骤3中注册的UUID相同。

   ```typescript
   let connectionParams: dataTransfer.ConnectionParams = {
     address: this.chosenDeviceAddr,
     uuid: SERVICE_UUID,
     mtu: 1024
   };
   try {
     dataTransfer.connect(connectionParams).then(() => {
       hilog.info(this.domainId, this.logTag, `Connect port finished`);
     }).catch((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
7. 通过设备地址和UUID向远端设备发数据。其中UUID要与步骤3中注册的UUID相同。

   ```typescript
   let transferValueBuffer: Uint8Array = new Uint8Array(4);
   transferValueBuffer[0] = 1;
   transferValueBuffer[1] = 2;
   transferValueBuffer[2] = 3;
   transferValueBuffer[3] = 4;
   let dataParams: dataTransfer.DataParams = {
     address: this.chosenDeviceAddr,
     uuid: SERVICE_UUID,
     data: transferValueBuffer.buffer
   };
   try {
     dataTransfer.writeData(dataParams).then(() => {
       hilog.info(this.domainId, this.logTag, `Port data write: ${JSON.stringify(dataParams)}`);
       // ...
     }).catch((err: BusinessError) => {
       hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
     });
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```

## 示例代码

数据传输功能可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/SsapClientPage.ets中的实现方法。
