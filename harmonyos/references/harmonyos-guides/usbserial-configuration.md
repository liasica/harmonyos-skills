---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usbserial-configuration
title: USB串口配置管理
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > USB服务 > 开发USB串口通信服务 > USB串口配置管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f4a9128f27e8355a13961c45f370b042f047fdc43991b0ecbb1d8c97f3276ca5
---

## 简介

USB串口配置管理中，波特率、数据位、校验位和停止位是串口通信协议的核心参数，它们共同定义了数据传输的格式和规则。通过合理配置这些参数，可以显著提升串口通信的可靠性和效率。

### 基本概念

在进行USB串口开发时，开发者应了解以下基本概念：

* 波特率（Baud Rate）

  波特率表示串口设备每秒传输的符号数（符号即二进制位，包括数据位、起始位、停止位、校验位），单位为Baud（波特），例如9600 Baud表示每秒传输9600个符号。收发双方必须使用相同的波特率，否则数据无法正确解析。
* 数据位（Data Bit）

  数据位表示每个数据包中实际传输的有效二进制位数，决定了单个字符的数据容量。常见的取值包括5位、6位、7位和8位。数据位决定单次传输的信息量，数据位越多，单次传输信息量越大，但需更多时间同步。
* 校验位（Parity Bit）

  校验位是附加在数据帧中的1位二进制值，根据数据位的内容按特定规则生成。常见的有，奇校验（Odd）数据位+校验位中“1”的总数为奇数，偶校验（Even）数据位+校验位中“1”的总数为偶数，无校验（None）不添加校验位。校验位通过验证数据位中“1”的数量，判断数据在传输过程中是否发生位翻转、噪声干扰等错误，增加校验位会略微降低传输效率，但能提高容错性。
* 停止位（Stop Bit）

  停止位位于数据帧末尾，是逻辑高电平信号，用于标识一个字符（数据包）传输的结束。典型长度有1位和2位（实际开发中1位最常用，2位多用于抗干扰场景）。其核心作用是为接收端提供时序同步容错空间，并确保数据完整性。

## 环境准备

请参考USB串口通信服务开发概述[环境准备](usbserial-overview.md#环境准备)。

## 开发指导

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| getAttribute(portId: number): Readonly<SerialAttribute> | 获取串口设备配置。 |
| setAttribute(portId: number, attribute: SerialAttribute): void | 设置串口设备配置。 |

### 开发步骤

开发者可以通过上述接口获取和设置串口的配置：

说明

以下示例代码只是获取和设置串口的配置的必要流程，需要放入具体的方法中执行。

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
5. 获取和修改串口配置。

   ```
   1. let portId: number = this.portId_;
   2. // 获取串口配置
   3. try {
   4. let attribute: serialManager.SerialAttribute = serialManager.getAttribute(portId);
   5. if (attribute === undefined) {
   6. console.error('getAttribute usbSerial error, attribute is undefined');
   7. this.logInfo_ += '\n[ERROR] getAttribute usbSerial error, attribute is undefined';
   8. } else {
   9. console.info(`getAttribute usbSerial success, attribute: ${attribute}`);
   10. this.logInfo_ += '\n[INFO] getAttribute usbSerial success, attribute: ' + JSON.stringify(attribute);
   11. }
   12. } catch (error) {
   13. console.error(`getAttribute usbSerial error: ${error}`);
   14. this.logInfo_ += '\n[ERROR] getAttribute usbSerial error: ' + JSON.stringify(error);
   15. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L140-L156)

   ```
   1. let portId: number = this.portId_;
   2. // 设置串口配置
   3. try {
   4. let attribute: serialManager.SerialAttribute = {
   5. baudRate: serialManager.BaudRates.BAUDRATE_9600,
   6. dataBits: serialManager.DataBits.DATABIT_8,
   7. parity: serialManager.Parity.PARITY_NONE,
   8. stopBits: serialManager.StopBits.STOPBIT_1
   9. }
   10. serialManager.setAttribute(portId, attribute);
   11. console.info(`setAttribute usbSerial success, attribute: ${attribute}`);
   12. this.logInfo_ += '\n[INFO] setAttribute usbSerial success, attribute: ' + JSON.stringify(attribute);
   13. } catch (error) {
   14. console.error(`setAttribute usbSerial error: ${error}`);
   15. this.logInfo_ += '\n[ERROR] setAttribute usbSerial error: ' + JSON.stringify(error);
   16. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/USB/USBManagerSerialSample/entry/src/main/ets/pages/Index.ets#L160-L177)

### 调测验证

1. 准备一根USB转串口线缆，线缆的USB接口连接到HarmonyOS设备USB端口（该端口需支持USB转串口），线缆的串口接口连接到目标设备的串口上。
2. 在HarmonyOS设备上执行上述示例。
3. 返回getAttribute usbSerial success和setAttribute usbSerial success表示相关接口调用成功，可以查看当前串口的配置。
