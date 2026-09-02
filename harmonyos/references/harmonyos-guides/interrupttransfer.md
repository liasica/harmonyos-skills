---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interrupttransfer
title: USB中断传输
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB中断传输
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:771014600d217a5cbe92dd15b0c0c8fdefb918a37e711a4ee2a141dc0a3e6ff7
---

## 场景介绍

中断传输主要用于主机（Host）接收设备（Device）发送的数据包。设备的端点模式决定了接口支持中断读或中断写，这种传输方式适用于少量的、分散的、不可预测的数据类型的传输，鼠标、键盘和操纵杆等设备均属于这种类型，且此类设备的端点一般只支持中断读操作。

## 环境准备

### 环境要求

* 开发工具及配置：

  DevEco Studio作为驱动开发工具，是进行驱动开发必备条件之一，开发者可以使用该工具进行开发、调试、打包等操作。请[下载安装](https://developer.huawei.com/consumer/cn/download/)该工具，并参考[DevEco Studio使用指南](ide-tools-overview.md)中的[创建工程及运行](ide-create-new-project.md)进行基本的操作验证，保证DevEco Studio可正常运行。
* SDK版本配置：

  扩展外设管理提供的ArkTS接口，所需SDK版本为API16及以上才可使用。
* HDC配置：

  HDC（HarmonyOS Device Connector）是为开发人员提供的用于调试的命令行工具，通过该工具可以在Windows/Linux/Mac系统上与真实设备或者模拟器进行交互，详细参考[HDC配置](hdc.md)。

### 搭建环境

* 在PC上安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，要求版本在4.1及以上。
* 将public-SDK更新到API 16或以上。
* PC安装HDC工具，通过该工具可以在Windows/Linux/Mac系统上与真实设备或者模拟器进行交互。
* 用USB线缆将搭载HarmonyOS的设备连接到PC。

## 开发指导

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| usbSubmitTransfer(transfer: UsbDataTransferParams): void | 异步传输接口（支持实时、批量、中断传输）。 |
| usbCancelTransfer(transfer: UsbDataTransferParams): void | 取消已提交的异步传输。 |

更多关于设备管理和传输模式的详细接口介绍，请查阅[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)。

### 开发步骤

主机（Host）连接设备（Device），通过usbSubmitTransfer接口进行数据传输。以下步骤描述了如何使用中断传输方式来传输数据：

**说明** 

以下示例代码只是使用中断传输方式来传输数据的必要流程，需要放入具体的方法中执行。在实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

1. 导入模块。

   ```typescript
   // 导入usbManager模块
   import { usbManager } from '@kit.BasicServicesKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { JSON } from '@kit.ArkTS';
   ```
2. 获取设备列表。

   ```typescript
   // 获取设备列表。
   let deviceList: usbManager.USBDevice[] = [];
   try {
     deviceList = usbManager.getDevices();
   } catch (error) {
       console.error(`USB getDevices failed: ${error}`);
       this.logInfo_ += '\n[ERROR] USB getDevices failed: ' + JSON.stringify(error);
   }

   console.info(`deviceList: ${deviceList}`);
   this.logInfo_ += '\n[INFO] deviceList: ' + JSON.stringify(deviceList);
   if (deviceList === undefined || deviceList.length === 0) {
     console.error('deviceList is empty');
     this.logInfo_ += '\n[ERROR] deviceList is empty';
     return;
   }
   /*
     deviceList结构示例
     [
       {
         name: '1-1',
         serial: '',
         manufacturerName: '',
         productName: '',
         version: '',
         vendorId: 7531,
         productId: 2,
         clazz: 9,
         subClass: 0,
         protocol: 1,
         devAddress: 1,
         busNum: 1,
         configs: [
           {
             id: 1,
             attributes: 224,
             isRemoteWakeup: true,
             isSelfPowered: true,
             maxPower: 0,
             name: '1-1',
             interfaces: [
               {
                 id: 0,
                 protocol: 0,
                 clazz: 9,
                 subClass: 0,
                 alternateSetting: 0,
                 name: '1-1',
                 endpoints: [
                   {
                     address: 129,
                     attributes: 3,
                     interval: 12,
                     maxPacketSize: 4,
                     direction: 128,
                     number: 1,
                     type: 3,
                     interfaceId: 0,
                   }
                 ]
               }
             ]
           }
         ]
       }
     ]
    */
   this.deviceList_ = deviceList;
   ```
3. 获取设备操作权限。

   ```typescript
   if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
     console.error('deviceList is empty');
     this.logInfo_ += '\n[ERROR] deviceList is empty';
     return;
   }
   let deviceList: usbManager.USBDevice[] = this.deviceList_;
   let deviceName: string = deviceList[0].name;
   // 申请操作指定的device的操作权限。
   usbManager.requestRight(deviceName).then((hasRight: boolean) => {
     console.info('usb device request right result: ' + hasRight);
     this.logInfo_ += '\n[INFO] usb device request right result: ' + JSON.stringify(hasRight);
   }).catch((error: BusinessError) => {
     console.error(`usb device request right failed : ${error}`);
     this.logInfo_ += '\n[ERROR] usb device request right failed: ' + JSON.stringify(error);
   });
   ```
4. 获取通过中断传输读取数据的端点。

   ```typescript
   if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
     console.error('deviceList_ is empty');
     this.logInfo_ += '\n[ERROR] deviceList_ is empty';
     return;
   }
   let usbDevice: usbManager.USBDevice = this.deviceList_[0];
   try {
     if (!usbManager.hasRight(usbDevice.name)) {
       console.error('permission denied');
       this.logInfo_ += '\n[ERROR] permission denied';
       return;
     }
   } catch (error) {
     console.error(`USB hasRight failed: ${error}`);
     this.logInfo_ += '\n[ERROR] USB hasRight failed: ' + JSON.stringify(error);
     return;
   }

   let devicePipe: usbManager.USBDevicePipe;
   try {
     devicePipe = usbManager.connectDevice(usbDevice);
   } catch (error) {
     console.error(`USB connectDevice failed: ${error}`);
     this.logInfo_ += '\n[ERROR] USB connectDevice failed: ' + JSON.stringify(error);
     return;
   }

   let usbConfigs: usbManager.USBConfiguration[] = usbDevice.configs;
   let usbInterfaces: usbManager.USBInterface[] = [];
   let usbInterface: usbManager.USBInterface | undefined = undefined;
   let usbEndpoints: usbManager.USBEndpoint[] = [];
   let usbEndpoint: usbManager.USBEndpoint | undefined = undefined;
   for (let i = 0; i < usbConfigs?.length; i++) {
     usbInterfaces = usbConfigs[i]?.interfaces;
     for (let j = 0; j < usbInterfaces?.length; j++) {
       usbEndpoints = usbInterfaces[j]?.endpoints;
       usbEndpoint = usbEndpoints?.find((value) => {
         return value.direction === 128 && value.type === usbManager.UsbEndpointTransferType.TRANSFER_TYPE_INTERRUPT;
       })
       if (usbEndpoint !== undefined) {
         usbInterface = usbInterfaces[j];
         break;
       }
     }
   }
   if (usbEndpoint === undefined) {
     console.error(`get usbEndpoint error`)
     this.logInfo_ += '\n[ERROR] get usbEndpoint error';
     return;
   }
   ```
5. 连接设备，注册通信接口。

   ```typescript
   // 注册通信接口，注册成功返回0，注册失败返回其他错误码。
   try {
     let claimInterfaceResult: number = usbManager.claimInterface(devicePipe, usbInterface, true);
     if (claimInterfaceResult !== 0) {
       console.error(`claimInterface error = ${claimInterfaceResult}`)
       this.logInfo_ += '\n[ERROR] claimInterface error = ' + JSON.stringify(claimInterfaceResult);
       return;
     }
   } catch (error) {
     console.error(`USB claimInterface failed: ${error}`);
     this.logInfo_ += '\n[ERROR] USB claimInterface failed: ' + JSON.stringify(error);
     return;
   }
   ```
6. 传输数据。

   ```typescript
   let transferParams: usbManager.UsbDataTransferParams | undefined = undefined;
   try {
     // 通信接口注册成功，传输数据
     transferParams = {
       devPipe: devicePipe,
       flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
       endpoint: usbEndpoint.address,
       type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_INTERRUPT,
       timeout: 2000,
       length: 10,
       callback: () => {
       },
       userData: new Uint8Array(10),
       buffer: new Uint8Array(10),
       isoPacketCount: 2,
     };

     transferParams.callback = (err: Error, callBackData: usbManager.SubmitTransferCallback) => {
       console.info(`callBackData = ${callBackData}`);
       this.logInfo_ += '\n[INFO] callBackData = ' + JSON.stringify(callBackData);
       console.info(`transfer success,result = ${transferParams?.buffer}`);
       this.logInfo_ += '\n[INFO] transfer success,result = ' + JSON.stringify(transferParams?.buffer);
     }
     usbManager.usbSubmitTransfer(transferParams);
     console.info('USB transfer request submitted.');
     this.logInfo_ += '\n[INFO] USB transfer request submitted.';
   } catch (error) {
     console.error(`USB transfer failed: ${error}`);
     this.logInfo_ += '\n[ERROR] USB transfer failed: ' + JSON.stringify(error);
   }
   ```
7. 取消传输，释放接口，关闭设备消息控制通道。

   ```typescript
   try {
     usbManager.usbCancelTransfer(transferParams);
     usbManager.releaseInterface(devicePipe, usbInterface);
     usbManager.closePipe(devicePipe);
   } catch (error) {
     console.error(`release failed: ${error}`);
     this.logInfo_ += '\n[ERROR] release failed: ' + JSON.stringify(error);
   }
   ```

### 调测验证

1. 主机端通过USB接口连接支持中断传输的终端设备（鼠标、键盘等）。
2. 执行上述代码。
3. log中搜索关键字transfer success，表示中断传输接口调用成功。
