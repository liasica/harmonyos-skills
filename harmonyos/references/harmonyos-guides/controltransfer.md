---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/controltransfer
title: USB控制传输
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB控制传输
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47ff7ede7361fb0ab8f11f9f9b1a2646c13152756b8a4e44efad12723b05fb7e
---

## 场景介绍

控制传输主要用于主机（Host）和设备（Device）进行设备状态的获取和设置，进行设备属性状态的控制。根据设备支持的端点类型支持控制传输读和写。

## 环境准备

### 环境要求

* 开发工具及配置：

  DevEco Studio作为驱动开发工具，是进行驱动开发必备条件之一，开发者可以使用该工具进行开发、调试、打包等操作。请[下载安装](https://developer.huawei.com/consumer/cn/download/)该工具，并参考[DevEco Studio使用指南](ide-tools-overview.md)中的[创建工程及运行](ide-create-new-project.md)进行基本的操作验证，保证DevEco Studio可正常运行。
* SDK版本配置：

  扩展外设管理提供的ArkTs接口，所需SDK版本为API16及以上才可使用。
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
| usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number> | 控制传输。 |

更多关于设备管理和传输模式的详细接口介绍，请查阅[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)。

### 开发步骤

主机（Host）连接设备（Device），通过usbControlTransfer接口进行数据传输。以下步骤描述了如何使用控制传输方式来传输数据：

说明

以下示例代码只是使用控制传输方式来传输数据的必要流程，需要放入具体的方法中执行。在实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

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

   ```
   1. if (this.pipe_ === undefined) {
   2. console.error('pipe_ is null');
   3. this.logInfo_ += '\n[ERROR] pipe_ is null';
   4. return;
   5. }
   6. let pipe: usbManager.USBDevicePipe = this.pipe_;
   7. /*
   8. 构造控制传输参数
   9. */
   10. let param: usbManager.USBDeviceRequestParams = {
   11. bmRequestType: 0x80, // 0x80指一次由设备到主机的标准请求命令
   12. bRequest: 0x06, // 0x06指获取描述符
   13. wValue: 0x01 << 8 | 0, // 该值为2个字节，高字节指描述符类型，此处0x01指设备描述符；低字节指描述符索引，设备描述符不涉及，填0
   14. wIndex: 0, // 索引值，可填0
   15. wLength: 18, // 描述符的长度，此处18表示设备描述符长度，最大支持1024
   16. data: new Uint8Array(18)
   17. };

   19. usbManager.usbControlTransfer(pipe, param).then((ret: number) => {
   20. console.info(`usbControlTransfer = ${ret}`);
   21. this.logInfo_ += '\n[INFO] usbControlTransfer = ' + JSON.stringify(ret);
   22. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L200-L223)
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
