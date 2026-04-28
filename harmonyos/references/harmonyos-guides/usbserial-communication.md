---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usbserial-communication
title: USB串口通信管理
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB串口通信服务 > USB串口通信管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8752cf3a16a16313e7f78a14e0436ae4deb5f6dc963d1da4a60c789287a4ed1d
---

## 简介

USB串口通信服务中通过Host设备的USB接口连接串口设备的串口进行串行数据传输，通信管理核心目标是实现设备间的高效、稳定数据传输与协同控制。主要使用在工业自动化与远程监控、物联网设备互联、医疗设备管理等场景。

## 环境准备

请参考USB串口通信服务开发概述[环境准备](usbserial-overview.md#环境准备)。

## 开发指导

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| getPortList(): Readonly<SerialPort>[] | 获取串口设备列表。 |
| hasSerialRight(portId: number): boolean | 检查应用程序是否具有访问串口设备的权限。 |
| requestSerialRight(portId: number): Promise<boolean> | 请求对串口设备的访问权限。 |
| open(portId: number): void | 打开串口设备。 |
| close(portId: number): void | 关闭串口设备。 |
| read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number> | 从串口设备读取数据，使用Promise异步返回。 |
| readSync(portId: number, buffer: Uint8Array, timeout?: number): number | 以同步方法从串口设备读取数据。 |
| write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number> | 往串口设备写入数据，使用Promise异步返回。 |
| writeSync(portId: number, buffer: Uint8Array, timeout?: number): number | 以同步方法往串口设备写入数据。 |

### 开发步骤

开发者可以通过上述接口读取和写入数据：

说明

以下示例代码只是串口数据传输的必要流程，需要放入具体的方法中执行。

1. 导入模块。

   ```
   1. // 导入usbManager模块
   2. import { serialManager } from '@kit.BasicServicesKit';
   3. import { BusinessError } from '@kit.BasicServicesKit'
   4. import { buffer } from '@kit.ArkTS';
   5. import { JSON } from '@kit.ArkTS';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L16-L23)
2. 获取设备列表。

   ```
   1. // 获取连接主设备的USB设备列表
   2. let portList: serialManager.SerialPort[] = serialManager.getPortList();
   3. console.info(`usbSerial portList: ${portList}`);
   4. this.logInfo_ += '\n[INFO] usbSerial portList: ' + JSON.stringify(portList);
   5. if (portList === undefined || portList.length === 0) {
   6. console.error('usbSerial portList is empty');
   7. this.logInfo_ += '\n[ERROR] usbSerial portList is empty';
   8. return;
   9. }
   10. this.portList_ = portList;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L32-L43)
3. 获取设备操作权限。

   ```
   1. if (this.portList_ === undefined || this.portList_.length === 0) {
   2. console.error('usbSerial portList is empty');
   3. this.logInfo_ += '\n[ERROR] usbSerial portList is empty';
   4. return;
   5. }
   6. let portList: serialManager.SerialPort[] = this.portList_;
   7. let portId: number = portList[0].portId;
   8. if (!serialManager.hasSerialRight(portId)) {
   9. serialManager.requestSerialRight(portId).then((result: boolean) => {
   10. console.info('serial device request right result: ' + result);
   11. this.logInfo_ += '\n[INFO] serial device request right result: ' + JSON.stringify(result);
   12. }).catch((error: BusinessError) => {
   13. console.error(`usb device request right failed : ${error}`);
   14. this.logInfo_ += '\n[ERROR] usb device request right failed: ' + JSON.stringify(error);
   15. });
   16. } else {
   17. console.info('serial device already request right');
   18. this.logInfo_ += '\n[INFO] serial device already request right';
   19. }
   20. this.portId_ = portId;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L47-L70)
4. 根据串口打开设备。

   ```
   1. let portId: number = this.portId_;
   2. try {
   3. serialManager.open(portId)
   4. console.info(`open usbSerial success, portId: ${portId}`);
   5. this.logInfo_ += '\n[INFO] open usbSerial success, portId: ' + JSON.stringify(portId);
   6. } catch (error) {
   7. console.error(`open usbSerial error： ${error}`);
   8. this.logInfo_ += '\n[ERROR] open usbSerial error: ' + JSON.stringify(error);
   9. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L74-L84)
5. 通过串口读取数据。

   ```
   1. let portId: number = this.portId_;
   2. // 异步读取
   3. let readBuffer: Uint8Array = new Uint8Array(64);
   4. serialManager.read(portId, readBuffer, 2000).then((size: number) => {
   5. console.info(`readAsync usbSerial success, readAsyncBuffer: ${readBuffer}`);
   6. this.logInfo_ += '\n[INFO] readAsync usbSerial success, readAsyncBuffer: ' + JSON.stringify(readBuffer);
   7. }).catch((error: Error) => {
   8. console.error(`readAsync usbSerial error: ${error}`);
   9. this.logInfo_ += '\n[ERROR] readAsync usbSerial error: ' + JSON.stringify(error);
   10. })

   12. // 同步读取
   13. let readSyncBuffer: Uint8Array = new Uint8Array(64);
   14. try {
   15. serialManager.readSync(portId, readSyncBuffer, 2000);
   16. console.info(`readSync usbSerial success, readSyncBuffer: ${readSyncBuffer}`);
   17. this.logInfo_ += '\n[INFO] readSync usbSerial success, readSyncBuffer: ' + JSON.stringify(readSyncBuffer);
   18. } catch (error) {
   19. console.error(`readSync usbSerial error: ${error}`);
   20. this.logInfo_ += '\n[ERROR] readSync usbSerial error: ' + JSON.stringify(error);
   21. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L88-L110)
6. 通过串口写入数据。

   ```
   1. let portId: number = this.portId_;
   2. // 异步写入
   3. let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
   4. serialManager.write(portId, writeBuffer, 2000).then((size: number) => {
   5. console.info(`writeAsync usbSerial success, writeAsyncBuffer: ${writeBuffer}`);
   6. this.logInfo_ += '\n[INFO] writeAsync usbSerial success, writeAsyncBuffer: ' + JSON.stringify(writeBuffer);
   7. }).catch((error: Error) => {
   8. console.error(`writeAsync usbSerial error: ${error}`);
   9. this.logInfo_ += '\n[ERROR] writeAsync usbSerial error: ' + JSON.stringify(error);
   10. })

   12. // 同步写入
   13. let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
   14. try {
   15. serialManager.writeSync(portId, writeSyncBuffer, 2000);
   16. console.info(`writeSync usbSerial success, writeSyncBuffer: ${writeSyncBuffer}`);
   17. this.logInfo_ += '\n[INFO] writeSync usbSerial success, writeSyncBuffer: ' + JSON.stringify(writeSyncBuffer);
   18. } catch (error) {
   19. console.error(`writeSync usbSerial error: ${error}`);
   20. this.logInfo_ += '\n[ERROR] writeSync usbSerial error: ' + JSON.stringify(error);
   21. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L114-L136)
7. 关闭串口设备。

   ```
   1. let portId: number = this.portId_;
   2. try {
   3. serialManager.close(portId);
   4. console.info(`close usbSerial success, portId: ${portId}`);
   5. this.logInfo_ += '\n[INFO] close usbSerial success, portId: ' + JSON.stringify(portId);
   6. } catch (error) {
   7. console.error(`close usbSerial error: ${error}`);
   8. this.logInfo_ += '\n[ERROR] close usbSerial error: ' + JSON.stringify(error);
   9. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L181-L191)

### 调测验证

1. 准备一根USB转串口线缆，线缆的USB接口连接到HarmonyOS设备USB端口（该端口需支持USB转串口），线缆的串口接口连接到目标设备的串口上。
2. 在HarmonyOS设备上执行上述示例。
3. 返回usbSerial success，表示相关接口调用成功，设备串口通信能力正常；返回usbSerial error，表示接口调用失败。
