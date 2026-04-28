---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interrupttransfer
title: USB中断传输
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB服务 > USB Host模式开发 > USB中断传输
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6391223302c9198090802f633721f126631b3bf82bbec2ae2b1020022f33eaa4
---

## 场景介绍

中断传输主要用于主机（Host）接收设备（Device）发送的数据包。设备的端点模式决定了接口支持中断读或中断写，这种传输方式适用于少量的、分散的、不可预测的数据类型的传输，鼠标、键盘和操纵杆等设备均属于这种类型，且此类设备的端点一般只支持中断读操作。

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
| usbSubmitTransfer(transfer: UsbDataTransferParams): void | 异步传输接口（支持实时、批量、中断传输）。 |
| usbCancelTransfer(transfer: UsbDataTransferParams): void | 取消已提交的异步传输。 |

更多关于设备管理和传输模式的详细接口介绍，请查阅[@ohos.usbManager](../harmonyos-references/js-apis-usbmanager.md)。

### 开发步骤

主机（Host）连接设备（Device），通过usbSubmitTransfer接口进行数据传输。以下步骤描述了如何使用中断传输方式来传输数据：

说明

以下示例代码只是使用中断传输方式来传输数据的必要流程，需要放入具体的方法中执行。在实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

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
4. 获取通过中断传输读取数据的端点。

   ```
   1. if (this.deviceList_ === undefined || this.deviceList_.length === 0) {
   2. console.error('deviceList_ is empty');
   3. this.logInfo_ += '\n[ERROR] deviceList_ is empty';
   4. return;
   5. }
   6. let usbDevice: usbManager.USBDevice = this.deviceList_[0];
   7. if (!usbManager.hasRight(usbDevice.name)) {
   8. console.error('permission denied');
   9. this.logInfo_ += '\n[ERROR] permission denied';
   10. return;
   11. }
   12. let devicePipe: usbManager.USBDevicePipe = usbManager.connectDevice(usbDevice);
   13. let usbConfigs: usbManager.USBConfiguration[] = usbDevice.configs;
   14. let usbInterfaces: usbManager.USBInterface[] = [];
   15. let usbInterface: usbManager.USBInterface | undefined = undefined;
   16. let usbEndpoints: usbManager.USBEndpoint[] = [];
   17. let usbEndpoint: usbManager.USBEndpoint | undefined = undefined;
   18. for (let i = 0; i < usbConfigs?.length; i++) {
   19. usbInterfaces = usbConfigs[i]?.interfaces;
   20. for (let j = 0; j < usbInterfaces?.length; j++) {
   21. usbEndpoints = usbInterfaces[j]?.endpoints;
   22. usbEndpoint = usbEndpoints?.find((value) => {
   23. return value.direction === 128 && value.type === usbManager.UsbEndpointTransferType.TRANSFER_TYPE_INTERRUPT;
   24. })
   25. if (usbEndpoint !== undefined) {
   26. usbInterface = usbInterfaces[j];
   27. break;
   28. }
   29. }
   30. }
   31. if (usbEndpoint === undefined) {
   32. console.error(`get usbEndpoint error`)
   33. this.logInfo_ += '\n[ERROR] get usbEndpoint error';
   34. return;
   35. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L227-L263)
5. 连接设备，注册通信接口。

   ```
   1. // 注册通信接口，注册成功返回0，注册失败返回其他错误码。
   2. let claimInterfaceResult: number = usbManager.claimInterface(devicePipe, usbInterface, true);
   3. if (claimInterfaceResult !== 0) {
   4. console.error(`claimInterface error = ${claimInterfaceResult}`)
   5. this.logInfo_ += '\n[ERROR] claimInterface error = ' + JSON.stringify(claimInterfaceResult);
   6. return;
   7. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L264-L272)
6. 传输数据。

   ```
   1. let transferParams: usbManager.UsbDataTransferParams | undefined = undefined;
   2. try {
   3. // 通信接口注册成功，传输数据
   4. transferParams = {
   5. devPipe: devicePipe,
   6. flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
   7. endpoint: usbEndpoint.address,
   8. type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_INTERRUPT,
   9. timeout: 2000,
   10. length: 10,
   11. callback: () => {
   12. },
   13. userData: new Uint8Array(10),
   14. buffer: new Uint8Array(10),
   15. isoPacketCount: 2,
   16. };

   18. transferParams.callback = (err: Error, callBackData: usbManager.SubmitTransferCallback) => {
   19. console.info(`callBackData = ${callBackData}`);
   20. this.logInfo_ += '\n[INFO] callBackData = ' + JSON.stringify(callBackData);
   21. console.info(`transfer success,result = ${transferParams?.buffer}`);
   22. this.logInfo_ += '\n[INFO] transfer success,result = ' + JSON.stringify(transferParams?.buffer);
   23. }
   24. usbManager.usbSubmitTransfer(transferParams);
   25. console.info('USB transfer request submitted.');
   26. this.logInfo_ += '\n[INFO] USB transfer request submitted.';
   27. } catch (error) {
   28. console.error(`USB transfer failed: ${error}`);
   29. this.logInfo_ += '\n[ERROR] USB transfer failed: ' + JSON.stringify(error);
   30. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L273-L304)
7. 取消传输，释放接口，关闭设备消息控制通道。

   ```
   1. try {
   2. usbManager.usbCancelTransfer(transferParams);
   3. usbManager.releaseInterface(devicePipe, usbInterface);
   4. usbManager.closePipe(devicePipe);
   5. } catch (error) {
   6. console.error(`release failed: ${error}`);
   7. this.logInfo_ += '\n[ERROR] release failed: ' + JSON.stringify(error);
   8. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSample/entry/src/main/ets/pages/Index.ets#L305-L314)

### 调测验证

1. 主机端通过USB接口连接支持中断传输的终端设备（鼠标、键盘等）。
2. 执行上述代码。
3. log中搜索关键字transfer success，表示中断传输接口调用成功。
