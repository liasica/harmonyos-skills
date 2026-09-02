---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicemanager
title: USB设备管理
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB设备管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0259311c69409c7a8f1ebad33d31fa516dbc812af5260dc6821fbc9a8bcfebb8
---

## 场景介绍

当有USB设备插入时，可以通过usbManager获取一些USB设备的基本信息，如设备类型、支持的功能等。 Host侧主要通过封装的pipe来完成和USB设备的通信。在HarmonyOS系统中，USB管理服务是核心组件，负责管理与USB设备的连接和通信。通过USB管理服务，应用程序可以检测USB设备的连接与断开，管理USB设备的权限请求和设备配置，以及进行数据传输和设备控制。

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

USB设备管理主要提供的功能有：查询USB设备列表、USB设备权限控制、设置USB设备配置等。

USB类开放能力如下，具体请查阅[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)。

**表1** USB类的开放能力接口

| 接口名 | 描述 |
| --- | --- |
| hasRight(deviceName: string): boolean | 判断是否有权访问该设备。 |
| requestRight(deviceName: string): Promise<boolean> | 请求软件包的临时权限以访问设备。使用Promise异步回调。 |
| removeRight(deviceName: string): boolean | 移除软件包对设备的访问权限。 |
| connectDevice(device: USBDevice): Readonly<USBDevicePipe> | 根据getDevices()返回的设备信息打开USB设备。 |
| getDevices(): Array<Readonly<USBDevice>> | 获取接入主设备的USB设备列表。如果没有设备接入，那么将会返回一个空的列表。 |
| setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number | 设置设备的配置。 |
| setInterface(pipe: USBDevicePipe, iface: USBInterface): number | 设置设备的接口。 |
| claimInterface(pipe: USBDevicePipe, iface: USBInterface, force ?: boolean): number | 注册通信接口。 |
| closePipe(pipe: USBDevicePipe): number | 关闭设备消息控制通道。 |
| releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number | 释放注册过的通信接口。 |
| getFileDescriptor(pipe: USBDevicePipe): number | 获取文件描述符。 |
| getRawDescriptor(pipe: USBDevicePipe): Uint8Array | 获取原始的USB描述符。 |

### 开发步骤

USB设备可作为Host连接Device进行设备管理，开发示例如下：

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
4. 打开Device设备。

   ```typescript
   if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
     console.error('deviceList_ is empty');
     this.logInfo_ += '\n[ERROR] deviceList is empty';
     return;
   }
   let deviceList: usbManager.USBDevice[] = this.deviceList_;
   try {
     if (!usbManager.hasRight(deviceList[0]?.name)) {
       console.error('permission denied');
       this.logInfo_ += '\n[ERROR] permission denied';
       return;
     }
     // 打开设备，获取数据传输通道。
     let pipe: usbManager.USBDevicePipe = usbManager.connectDevice(deviceList[0]);
     if (!deviceList?.[0]?.configs?.[0]?.interfaces?.[0]) {
       console.error('invalid interface');
       this.logInfo_ += '\n[ERROR] invalid interface';
       return;
     }
     let interface1: usbManager.USBInterface = deviceList?.[0]?.configs?.[0]?.interfaces?.[0];
     /*
       打开对应接口，在设备信息（deviceList）中选取对应的interface。
       interface1为设备配置中的一个接口。
      */
     usbManager.claimInterface(pipe, interface1, true);
     this.pipe_ = pipe;
     this.interface_ = interface1;
     console.info('open device success');
     this.logInfo_ += '\n[INFO] open device success';
   } catch (error) {
     console.error(`USB hasRight failed: ${error}`);
     this.logInfo_ += '\n[ERROR] USB hasRight failed: ' + JSON.stringify(error);
   }
   ```
5. 释放接口，关闭设备。

   ```typescript
   if (this.pipe_ === undefined || this.interface_ === undefined) {
     console.error('pipe_ or interface_ is null');
     this.logInfo_ += '\n[ERROR] pipe_ or interface_ is null';
     return;
   }
   let pipe: usbManager.USBDevicePipe = this.pipe_;
   let interface1: usbManager.USBInterface = this.interface_;
   try {
     usbManager.releaseInterface(pipe, interface1);
     usbManager.closePipe(pipe);
   } catch (error) {
     console.error(`failed: ${error}`);
     this.logInfo_ += '\n[ERROR] failed: ' + JSON.stringify(error);
   }

   this.pipe_ = undefined;
   this.interface_ = undefined;
   console.info('close device success');
   this.logInfo_ += '\n[INFO] close device success';
   ```
