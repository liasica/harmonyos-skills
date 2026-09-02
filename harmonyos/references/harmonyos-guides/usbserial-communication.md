---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usbserial-communication
title: USB串口通信管理
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB串口通信服务 > USB串口通信管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d903906274f52bd2b5ed4e37aecbef617f97e31a29d21653a80682952fb8480c
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

**说明** 

以下示例代码只是串口数据传输的必要流程，需要放入具体的方法中执行。

1. 导入模块。

   ```typescript
   // 导入serialManager模块
   import { serialManager } from '@kit.BasicServicesKit';
   import { BusinessError } from '@kit.BasicServicesKit'
   import { buffer } from '@kit.ArkTS';
   import { JSON } from '@kit.ArkTS';
   ```
2. 获取设备列表。

   ```typescript
   // 获取连接主设备的USB设备列表
   let portList: serialManager.SerialPort[] = serialManager.getPortList();
   console.info(`usbSerial portList: ${portList}`);
   this.logInfo_ += '\n[INFO] usbSerial portList: ' + JSON.stringify(portList);
   if (portList === undefined || portList.length === 0) {
     console.error('usbSerial portList is empty');
     this.logInfo_ += '\n[ERROR] usbSerial portList is empty';
     return;
   }
   this.portList_ = portList;
   ```
3. 获取设备操作权限。

   ```typescript
   if (this.portList_ === undefined || this.portList_.length === 0) {
     console.error('usbSerial portList is empty');
     this.logInfo_ += '\n[ERROR] usbSerial portList is empty';
     return;
   }
   let portList: serialManager.SerialPort[] = this.portList_;
   let portId: number = portList[0].portId;
   if (!serialManager.hasSerialRight(portId)) {
     serialManager.requestSerialRight(portId).then((result: boolean) => {
       console.info('serial device request right result: ' + result);
       this.logInfo_ += '\n[INFO] serial device request right result: ' + JSON.stringify(result);
     }).catch((error: BusinessError) => {
       console.error(`usb device request right failed : ${error}`);
       this.logInfo_ += '\n[ERROR] usb device request right failed: ' + JSON.stringify(error);
     });
   } else {
     console.info('serial device already request right');
     this.logInfo_ += '\n[INFO] serial device already request right';
   }
   this.portId_ = portId;
   ```
4. 根据串口打开设备。

   ```typescript
   let portId: number = this.portId_;
   try {
     serialManager.open(portId)
     console.info(`open usbSerial success, portId: ${portId}`);
     this.logInfo_ += '\n[INFO] open usbSerial success, portId: ' + JSON.stringify(portId);
   } catch (error) {
     console.error(`open usbSerial error： ${error}`);
     this.logInfo_ += '\n[ERROR] open usbSerial error: ' + JSON.stringify(error);
   }
   ```
5. 通过串口读取数据。

   ```typescript
   let portId: number = this.portId_;
   // 异步读取
   let readBuffer: Uint8Array = new Uint8Array(64);
   serialManager.read(portId, readBuffer, 2000).then((size: number) => {
     console.info(`readAsync usbSerial success, readAsyncBuffer: ${readBuffer}`);
     this.logInfo_ += '\n[INFO] readAsync usbSerial success, readAsyncBuffer: ' + JSON.stringify(readBuffer);
   }).catch((error: Error) => {
     console.error(`readAsync usbSerial error: ${error}`);
     this.logInfo_ += '\n[ERROR] readAsync usbSerial error: ' + JSON.stringify(error);
   })

   // 同步读取
   let readSyncBuffer: Uint8Array = new Uint8Array(64);
   try {
     serialManager.readSync(portId, readSyncBuffer, 2000);
     console.info(`readSync usbSerial success, readSyncBuffer: ${readSyncBuffer}`);
     this.logInfo_ += '\n[INFO] readSync usbSerial success, readSyncBuffer: ' + JSON.stringify(readSyncBuffer);
   } catch (error) {
     console.error(`readSync usbSerial error: ${error}`);
     this.logInfo_ += '\n[ERROR] readSync usbSerial error: ' + JSON.stringify(error);
   }
   ```
6. 通过串口写入数据。

   ```typescript
   let portId: number = this.portId_;
   // 异步写入
   let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
   serialManager.write(portId, writeBuffer, 2000).then((size: number) => {
     console.info(`writeAsync usbSerial success, writeAsyncBuffer: ${writeBuffer}`);
     this.logInfo_ += '\n[INFO] writeAsync usbSerial success, writeAsyncBuffer: ' + JSON.stringify(writeBuffer);
   }).catch((error: Error) => {
     console.error(`writeAsync usbSerial error: ${error}`);
     this.logInfo_ += '\n[ERROR] writeAsync usbSerial error: ' + JSON.stringify(error);
   })

   // 同步写入
   let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
   try {
     serialManager.writeSync(portId, writeSyncBuffer, 2000);
     console.info(`writeSync usbSerial success, writeSyncBuffer: ${writeSyncBuffer}`);
     this.logInfo_ += '\n[INFO] writeSync usbSerial success, writeSyncBuffer: ' + JSON.stringify(writeSyncBuffer);
   } catch (error) {
     console.error(`writeSync usbSerial error: ${error}`);
     this.logInfo_ += '\n[ERROR] writeSync usbSerial error: ' + JSON.stringify(error);
   }
   ```
7. 关闭串口设备。

   ```typescript
   let portId: number = this.portId_;
   try {
     serialManager.close(portId);
     console.info(`close usbSerial success, portId: ${portId}`);
     this.logInfo_ += '\n[INFO] close usbSerial success, portId: ' + JSON.stringify(portId);
   } catch (error) {
     console.error(`close usbSerial error: ${error}`);
     this.logInfo_ += '\n[ERROR] close usbSerial error: ' + JSON.stringify(error);
   }
   ```

### 调测验证

1. 准备一根USB转串口线缆，线缆的USB接口连接到HarmonyOS设备USB端口（该端口需支持USB转串口），线缆的串口接口连接到目标设备的串口上。
2. 在HarmonyOS设备上执行上述示例。
3. 返回usbSerial success，表示相关接口调用成功，设备串口通信能力正常；返回usbSerial error，表示接口调用失败。
