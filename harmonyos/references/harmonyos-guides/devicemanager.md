---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicemanager
title: USB设备管理
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB设备管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f3c142c9bf04c4df14ac6e7228ebba6fc9a6102868512a4a6289879526b647b4
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

   ```
   1. // 导入usbManager模块
   2. import { usbManager } from '@kit.BasicServicesKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { JSON } from '@kit.ArkTS';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L16-L22)
2. 获取设备列表。

   ```
   1. // 获取设备列表。
   2. let deviceList: usbManager.USBDevice[] = usbManager.getDevices();
   3. console.info(`deviceList: ${deviceList}`);
   4. this.logInfo_ += '\n[INFO] deviceList: ' + JSON.stringify(deviceList);
   5. if (deviceList === undefined || deviceList.length === 0) {
   6. console.error('deviceList is empty');
   7. this.logInfo_ += '\n[ERROR] deviceList is empty';
   8. return;
   9. }
   10. /*
   11. deviceList结构示例
   12. [
   13. {
   14. name: '1-1',
   15. serial: '',
   16. manufacturerName: '',
   17. productName: '',
   18. version: '',
   19. vendorId: 7531,
   20. productId: 2,
   21. clazz: 9,
   22. subClass: 0,
   23. protocol: 1,
   24. devAddress: 1,
   25. busNum: 1,
   26. configs: [
   27. {
   28. id: 1,
   29. attributes: 224,
   30. isRemoteWakeup: true,
   31. isSelfPowered: true,
   32. maxPower: 0,
   33. name: '1-1',
   34. interfaces: [
   35. {
   36. id: 0,
   37. protocol: 0,
   38. clazz: 9,
   39. subClass: 0,
   40. alternateSetting: 0,
   41. name: '1-1',
   42. endpoints: [
   43. {
   44. address: 129,
   45. attributes: 3,
   46. interval: 12,
   47. maxPacketSize: 4,
   48. direction: 128,
   49. number: 1,
   50. type: 3,
   51. interfaceId: 0,
   52. }
   53. ]
   54. }
   55. ]
   56. }
   57. ]
   58. }
   59. ]
   60. */
   61. this.deviceList_ = deviceList;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L32-L94)
3. 获取设备操作权限。

   ```
   1. if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
   2. console.error('deviceList is empty');
   3. this.logInfo_ += '\n[ERROR] deviceList is empty';
   4. return;
   5. }
   6. let deviceList: usbManager.USBDevice[] = this.deviceList_;
   7. let deviceName: string = deviceList[0].name;
   8. // 申请操作指定的device的操作权限。
   9. usbManager.requestRight(deviceName).then((hasRight: boolean) => {
   10. console.info('usb device request right result: ' + hasRight);
   11. this.logInfo_ += '\n[INFO] usb device request right result: ' + JSON.stringify(hasRight);
   12. }).catch((error: BusinessError) => {
   13. console.error(`usb device request right failed : ${error}`);
   14. this.logInfo_ += '\n[ERROR] usb device request right failed: ' + JSON.stringify(error);
   15. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L98-L114)
4. 打开Device设备。

   ```
   1. if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
   2. console.error('deviceList_ is empty');
   3. this.logInfo_ += '\n[ERROR] deviceList is empty';
   4. return;
   5. }
   6. let deviceList: usbManager.USBDevice[] = this.deviceList_;
   7. if (!usbManager.hasRight(deviceList[0]?.name)) {
   8. console.error('permission denied');
   9. this.logInfo_ += '\n[ERROR] permission denied';
   10. return;
   11. }
   12. // 打开设备，获取数据传输通道。
   13. let pipe: usbManager.USBDevicePipe = usbManager.connectDevice(deviceList[0]);
   14. if (!deviceList?.[0]?.configs?.[0]?.interfaces?.[0]) {
   15. console.error('invalid interface');
   16. this.logInfo_ += '\n[ERROR] invalid interface';
   17. return;
   18. }
   19. let interface1: usbManager.USBInterface = deviceList?.[0]?.configs?.[0]?.interfaces?.[0];
   20. /*
   21. 打开对应接口，在设备信息（deviceList）中选取对应的interface。
   22. interface1为设备配置中的一个接口。
   23. */
   24. usbManager.claimInterface(pipe, interface1, true);
   25. this.pipe_ = pipe;
   26. this.interface_ = interface1;
   27. console.info('open device success');
   28. this.logInfo_ += '\n[INFO] open device success';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L118-L147)
5. 释放接口，关闭设备。

   ```
   1. if (this.pipe_ === undefined || this.interface_ === undefined) {
   2. console.error('pipe_ or interface_ is null');
   3. this.logInfo_ += '\n[ERROR] pipe_ or interface_ is null';
   4. return;
   5. }
   6. let pipe: usbManager.USBDevicePipe = this.pipe_;
   7. let interface1: usbManager.USBInterface = this.interface_;
   8. usbManager.releaseInterface(pipe, interface1);
   9. usbManager.closePipe(pipe);
   10. this.pipe_ = undefined;
   11. this.interface_ = undefined;
   12. console.info('close device success');
   13. this.logInfo_ += '\n[INFO] close device success';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L420-L434)
