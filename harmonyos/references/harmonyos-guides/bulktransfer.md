---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bulktransfer
title: USB批量传输
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB批量传输
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:443dd6edebde35360c47a252adb48122a3783b8d97f8f1555358d916a327a305
---

## 场景介绍

批量传输主要应用在传输和接收大量数据同时又没有带宽和间隔时间要求的情况下，例如传输文件、图像等场景，打印机和扫描仪等设备属于这种类型的设备。

## 环境准备

### 环境要求

* 开发工具及配置：

  DevEco Studio作为驱动开发工具，是进行驱动开发必备条件之一，开发者可以使用该工具进行开发、调试、打包等操作。请[下载安装](https://developer.huawei.com/consumer/cn/download/)该工具，并参考[DevEco Studio使用指南](ide-tools-overview.md)中的[创建工程及运行](ide-create-new-project.md)进行基本的操作验证，保证DevEco Studio可正常运行。
* SDK版本配置：

  扩展外设管理提供的ArkTS接口，所需SDK版本为API 16及以上才可使用。
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
| bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout ?: number): Promise<number> | 批量传输。 |

更多关于设备管理和传输模式的详细接口介绍，请查阅[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)。

### 开发步骤

主机（Host）连接设备（Device），通过bulkTransfer接口进行数据传输。以下步骤描述了如何使用批量传输方式来传输数据：

说明

以下示例代码只是使用批量传输方式来传输数据的必要流程，需要放入具体的方法中执行。在实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

1. 导入模块。

   ```
   1. // 导入usbManager模块
   2. import { usbManager } from '@kit.BasicServicesKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { JSON } from '@kit.ArkTS';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L16-L22)
2. 获取设备列表。

   说明

   批量传输只能在[传输类型](../harmonyos-references/js-apis-usbmanager.md#usbendpointtransfertype18)为2的端点上进行，若不匹配会返回IO错误。

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
4. 打开设备。

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
5. 数据传输。

   说明

   在数据传输前建议先获取interface所属endpoint的type，通过type判断interface是否支持所需的传输类型。

   若调用传输接口失败，请先确认设备interface是否支持[模式切换](../harmonyos-references/js-apis-usbmanager.md#usbinterface)。若alternateSetting支持切换设置，可在传输前调用[usbManager.setInterface](../harmonyos-references/js-apis-usbmanager.md#usbmanagersetinterface)重新设置interface，使端点和传输类型匹配，保证端点正常通信。

   ```
   1. if (this.pipe_ === undefined || this.interface_ === undefined) {
   2. console.error('pipe_ or interface_ is null');
   3. this.logInfo_ += '\n[ERROR] pipe_ or interface_ is null';
   4. return;
   5. }
   6. let pipe: usbManager.USBDevicePipe = this.pipe_;
   7. let interface1: usbManager.USBInterface = this.interface_;
   8. /*
   9. 读取数据，在device信息中选取对应数据接收的endpoint来做数据传输
   10. （endpoint.direction == 0x80）；dataUint8Array是要读取的数据，类型为Uint8Array。
   11. */
   12. let inEndpoint: usbManager.USBEndpoint = interface1.endpoints?.[1];
   13. let outEndpoint: usbManager.USBEndpoint = interface1.endpoints?.[0];
   14. let dataUint8Array: Uint8Array = new Uint8Array(1024);
   15. if (inEndpoint !== undefined && inEndpoint.direction === 0x80) {
   16. usbManager.bulkTransfer(pipe, inEndpoint, dataUint8Array, 15000).then((dataLength: number) => {
   17. if (dataLength >= 0) {
   18. console.info(`usb readData result Length : ${dataLength}`);
   19. this.logInfo_ += '\n[INFO] usb readData result Length: ' + JSON.stringify(dataLength);
   20. } else {
   21. console.error('usb readData failed');
   22. this.logInfo_ += '\n[ERROR] usb readData failed';
   23. }
   24. }).catch((error: BusinessError) => {
   25. console.error(`usb readData error : ${error}`);
   26. this.logInfo_ += '\n[ERROR] usb readData error: ' + JSON.stringify(error);
   27. });
   28. }

   30. // 发送数据，在device信息中选取对应数据发送的endpoint来做数据传输。（endpoint.direction == 0）
   31. if (outEndpoint !== undefined && outEndpoint.direction === 0) {
   32. usbManager.bulkTransfer(pipe, outEndpoint, dataUint8Array, 15000).then((dataLength: number) => {
   33. if (dataLength >= 0) {
   34. console.info(`usb writeData result write length : ${dataLength}`);
   35. this.logInfo_ += '\n[INFO] usb writeData result write length: ' + JSON.stringify(dataLength);
   36. } else {
   37. console.error('usb writeData failed');
   38. this.logInfo_ += '\n[ERROR] usb writeData failed';
   39. }
   40. }).catch((error: BusinessError) => {
   41. console.error(`usb writeData error : ${error}`);
   42. this.logInfo_ += '\n[ERROR] usb writeData error: ' + JSON.stringify(error);
   43. });
   44. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L151-L196)
6. 释放接口，关闭设备。

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
