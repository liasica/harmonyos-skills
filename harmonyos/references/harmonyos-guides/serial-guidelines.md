---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serial-guidelines
title: 串口通信开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 串口通信服务 > 开发串口通信服务 > 串口通信开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:90afa5eaf395da8abb6aa39b6329354591da499f08840cf1c0bb7cef2b97c3d1
---

## 场景介绍

串口通信模块（@ohos.busManager.serial）提供面向对象的串口管理能力，支持获取设备可用串口列表、打开/关闭串口、数据读写、硬件信号控制（RTS/CTS、DTR/DSR）、断开事件监听以及流控配置等功能。该模块适用于工业自动化、物联网设备互联、嵌入式设备调试、GPS模块通信等需要通过串口进行数据交换的场景。

## 基本概念

在进行串口通信开发时，开发者应了解以下基本概念：

* **串口**

  即串行接口或串行通信接口，是采用串行通信方式的扩展接口。串行接口中数据是一位一位地顺序传送。串口特点是通信线路简单，只要一对传输线就可以实现双向通信，适用于远距离通信。
* **波特率（Baud Rate）**

  表示每秒钟传送的比特数，是衡量串口通信速率的指标。常用波特率有9600、19200、38400、57600、115200等。通信双方必须使用相同的波特率才能正确收发数据。
* **数据位（Data Bits）**

  表示通信中实际数据位的位数，通常可设置为5、6、7或8位。最常用的数据位长度为8位。
* **校验位（Parity）**

  用于检验数据传输正确性的位。支持无校验（NONE）、奇校验（ODD）、偶校验（EVEN）、标记校验（MARK）和空格校验（SPACE）等模式。
* **停止位（Stop Bits）**

  用于标识一个数据包的结束，可设置为1位或2位。最常用的停止位长度为1位。
* **流控（Flow Control）**

  用于控制数据传输速率，防止数据丢失。常见的流控方式包括硬件流控（RTS/CTS）和软件流控（XON/XOFF）。

## 实现原理

串口通信服务的核心流程如下：

1. **获取串口列表**：系统枚举当前可用的串口设备，返回串口对象列表。
2. **打开串口**：选择目标串口，配置波特率、数据位、校验位、停止位等通信参数并打开。首次打开时系统会弹窗请求用户授权，用户同意后方可访问串口设备；用户拒绝则接口抛出35700007错误码。
3. **数据收发**：通过写入接口发送数据，通过注册数据回调监听接收数据。
4. **硬件信号控制**：通过RTS/CTS、DTR/DSR等信号线进行硬件流控和状态检测。
5. **断开事件监听**：通过注册断开事件回调，监听USB虚拟串口的拔出等断开事件。
6. **关闭串口**：通信结束后关闭串口，释放资源。

串口通信数据流

```txt
应用层写入数据 → 串口驱动发送 → 物理串口线 → 对端串口设备
                                              ↓
应用层读取数据 ← 串口驱动缓冲 ← 物理串口线 ← 对端串口设备
```

## 约束和限制

* 使用串口通信功能前，需要确保设备已正确连接串口硬件。
* 写入数据长度范围为(0, 4096]字节。
* 若开发者未主动设置配置参数，则使用默认配置参数（波特率：115200bps，数据位：8，停止位：1，校验位：无，硬件自动流控：关闭，软件流控：关闭）。
* 同一串口同一时间只能被一个应用打开。
* 用户授权在以下场景下会失效，再次访问串口需重新授权：USB虚拟串口拔出、系统切换用户、整机重启。

## 环境准备

### 环境要求

* **开发工具及配置**：

  DevEco Studio作为开发工具，是进行串口通信开发必备条件之一，开发者可以使用该工具进行开发、调试、打包等操作。请[下载安装](https://developer.huawei.com/consumer/cn/download/)该工具，并参考[DevEco Studio使用指南](ide-tools-overview.md)中的[创建工程及运行](ide-create-new-project.md)进行基本的操作验证，保证DevEco Studio可正常运行。
* **SDK版本配置**：

  本模块提供的ArkTS接口需要SDK版本为API 26.0.0及以上。

### 搭建环境

* 在PC上安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，要求版本在6.1及以上。
* 将public-SDK更新到API 26.0.0或以上。
* 准备串口连接线缆，将HarmonyOS设备的串口端口与目标设备的串口正确连接。

## 开发指导

### 接口说明

串口通信主要接口如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [SerialPort.getSerialPortList](../harmonyos-references/js-apis-busmanager-serial.md#serialgetserialportlist)(): Promise<[SerialPort](../harmonyos-references/js-apis-busmanager-serial.md#serialport)[]> | 查询串口设备列表，返回[SerialPort](../harmonyos-references/js-apis-busmanager-serial.md#serialport)对象数组。使用Promise异步回调。 |
| [SerialPort.open](../harmonyos-references/js-apis-busmanager-serial.md#open)(config?: [SerialConfigs](../harmonyos-references/js-apis-busmanager-serial.md#serialconfigs)): Promise<void> | 打开串口设备。首次打开时系统会弹窗请求用户授权访问目标串口，用户拒绝则抛出35700007错误码。授权在USB虚拟串口拔出、系统切换用户、整机重启后失效，需重新授权。使用Promise异步回调。 |
| [SerialPort.close](../harmonyos-references/js-apis-busmanager-serial.md#close)(): Promise<void> | 关闭串口设备。使用Promise异步回调。 |
| [SerialPort.write](../harmonyos-references/js-apis-busmanager-serial.md#write)(data: Uint8Array, timeout?: number): Promise<number> | 向串口设备发送数据，每次发送数据长度范围：(0, 4096]。使用Promise异步回调。 |
| [SerialPort.onDataRead](../harmonyos-references/js-apis-busmanager-serial.md#ondataread)(callback: Callback<Uint8Array>): void | 监听串口接收数据事件。使用callback异步回调返回接收到的数据。调用[close](../harmonyos-references/js-apis-busmanager-serial.md#close)后，所有回调将被清除。 |
| [SerialPort.offDataRead](../harmonyos-references/js-apis-busmanager-serial.md#offdataread)(callback?: Callback<Uint8Array>): void | 取消监听串口接收数据事件。使用callback异步回调。 |
| [SerialPort.flush](../harmonyos-references/js-apis-busmanager-serial.md#flush)(): Promise<void> | 清空串口缓冲区，包括读缓冲区和写缓冲区，缓冲区中的数据将被直接丢弃，不再发送或读取。使用Promise异步回调。 |
| [SerialPort.drain](../harmonyos-references/js-apis-busmanager-serial.md#drain)(): Promise<void> | 等待所有写请求完成。使用Promise异步回调。 |
| [SerialPort.setRts](../harmonyos-references/js-apis-busmanager-serial.md#setrts)(enable: boolean): Promise<void> | 设置RTS（请求发送）信号状态。使用Promise异步回调。 |
| [SerialPort.getCts](../harmonyos-references/js-apis-busmanager-serial.md#getcts)(): Promise<boolean> | 获取CTS（清除发送）信号状态。使用Promise异步回调。 |
| [SerialPort.sendBrk](../harmonyos-references/js-apis-busmanager-serial.md#sendbrk)(): Promise<void> | 发送BRK（中断）信号。使用Promise异步回调。 |
| [SerialPort.setDtr](../harmonyos-references/js-apis-busmanager-serial.md#setdtr)(enable: boolean): Promise<void> | 设置DTR（数据终端就绪）信号状态。使用Promise异步回调。 |
| [SerialPort.getDsr](../harmonyos-references/js-apis-busmanager-serial.md#getdsr)(): Promise<boolean> | 获取DSR（数据设备就绪）信号状态。使用Promise异步回调。 |
| [SerialPort.onDisconnect](../harmonyos-references/js-apis-busmanager-serial.md#ondisconnect)(callback: Callback<void>): void | 监听串口断开事件。使用callback异步回调。 |
| [SerialPort.offDisconnect](../harmonyos-references/js-apis-busmanager-serial.md#offdisconnect)(callback?: Callback<void>): void | 取消监听串口断开事件。 |

[SerialConfigs](../harmonyos-references/js-apis-busmanager-serial.md#serialconfigs)配置参数说明：

| 参数名 | 类型 | 必填 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| baudRate | number | 否 | 115200 | 波特率。 |
| dataBits | [DataBits](../harmonyos-references/js-apis-busmanager-serial.md#databits) | 否 | DataBits.EIGHT | 数据位。 |
| stopBits | [StopBits](../harmonyos-references/js-apis-busmanager-serial.md#stopbits) | 否 | StopBits.ONE | 停止位。 |
| parity | [Parity](../harmonyos-references/js-apis-busmanager-serial.md#parity) | 否 | Parity.NONE | 校验位。 |
| rtscts | boolean | 否 | false | 检查是否启用RTS/CTS硬件自动流控。true表示启用，false表示未启用。 |
| xon | boolean | 否 | false | 检查是否启用XON软件流控。true表示启用，false表示未启用。 |
| xoff | boolean | 否 | false | 检查是否启用XOFF软件流控。true表示启用，false表示未启用。 |
| xany | boolean | 否 | false | 检查是否启用任意字符重启软件流控。true表示启用，false表示未启用。 |

### 开发步骤

**说明** 

以下示例代码只是串口通信的必要流程，需要放入具体的方法中执行。

1. 导入模块。

   ```typescript
   import { serial, BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取串口设备列表。

   ```typescript
   try {
     const portList = await serial.getSerialPortList();
     console.info(`${TAG} getSerialPortList success, count: ${portList.length}`);
     portList.forEach((port: serial.SerialPort, index: number) => {
       console.info(`${TAG}   [${index}] portName=${port.portInfo.portName}, vendorId=${port.portInfo.vendorId}, productId=${port.portInfo.productId}`);
     });
     if (portList.length > 0) {
       this.port = portList[0];
     }
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} getSerialPortList failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
3. 打开串口设备。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     const config: serial.SerialConfigs = {
       baudRate: 115200,
       dataBits: serial.DataBits.EIGHT,
       stopBits: serial.StopBits.ONE,
       parity: serial.Parity.NONE
     };
     await this.port.open(config);
     console.info(`${TAG} open success`);
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} open failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
4. 注册数据接收回调，监听串口数据。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     this.dataCallback = (data: Uint8Array) => {
       console.info(`${TAG} onDataRead: ${Array.from(data).join(', ')}`);
     };
     this.port.onDataRead(this.dataCallback);
     console.info(`${TAG} onDataRead registered`);
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} onDataRead failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
5. 通过串口写入数据。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     const data = new Uint8Array([0x48, 0x65, 0x6C, 0x6C, 0x6F]);
     const writeLen = await this.port.write(data);
     console.info(`${TAG} write success, length: ${writeLen}`);
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} write failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
6. 刷新缓冲区与等待发送完成。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     await this.port.flush();
     console.info(`${TAG} flush success`);
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} flush failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
7. 硬件信号控制。

   * 设置RTS信号为高电平。

     ```typescript
     try {
       if (!this.port) {
         console.error(`${TAG} No serial port found, please call getSerialPortList first`);
         return;
       }
       await this.port.setRts(true);
       console.info(`${TAG} setRts(true) success`);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`${TAG} setRts failed, code: ${e.code}, message: ${e.message}`);
     }
     ```
   * 获取CTS信号状态。

     ```typescript
     try {
       if (!this.port) {
         console.error(`${TAG} No serial port found, please call getSerialPortList first`);
         return;
       }
       const ctsStatus = await this.port.getCts();
       console.info(`${TAG} getCts success, CTS: ${ctsStatus}`);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`${TAG} getCts failed, code: ${e.code}, message: ${e.message}`);
     }
     ```
   * 发送break信号。

     ```typescript
     try {
       if (!this.port) {
         console.error(`${TAG} No serial port found, please call getSerialPortList first`);
         return;
       }
       await this.port.sendBrk();
       console.info(`${TAG} sendBrk success`);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`${TAG} sendBrk failed, code: ${e.code}, message: ${e.message}`);
     }
     ```
   * 设置DTR信号为高电平。

     ```typescript
     try {
       if (!this.port) {
         console.error(`${TAG} No serial port found, please call getSerialPortList first`);
         return;
       }
       await this.port.setDtr(true);
       console.info(`${TAG} setDtr(true) success`);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`${TAG} setDtr failed, code: ${e.code}, message: ${e.message}`);
     }
     ```
   * 获取DSR信号状态。

     ```typescript
     try {
       if (!this.port) {
         console.error(`${TAG} No serial port found, please call getSerialPortList first`);
         return;
       }
       const dsrStatus = await this.port.getDsr();
       console.info(`${TAG} getDsr success, DSR: ${dsrStatus}`);
     } catch (err) {
       const e = err as BusinessError;
       console.error(`${TAG} getDsr failed, code: ${e.code}, message: ${e.message}`);
     }
     ```
8. 监听串口断开事件。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     this.disconnectedCallback = () => {
       console.info(`${TAG} onDisconnect: serial port disconnected`);
     };
     this.port.onDisconnect(this.disconnectedCallback);
     console.info(`${TAG} onDisconnect registered`);
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} onDisconnect failed, code: ${e.code}, message: ${e.message}`);
   }
   ```
9. 注销数据接收回调和关闭串口设备。

   ```typescript
   try {
     if (!this.port) {
       console.error(`${TAG} No serial port found, please call getSerialPortList first`);
       return;
     }
     await this.port.close();
     console.info(`${TAG} close success`);
     this.port = null;
   } catch (err) {
     const e = err as BusinessError;
     console.error(`${TAG} close failed, code: ${e.code}, message: ${e.message}`);
   }
   ```

### 调测验证

1. 准备串口连接线缆，将HarmonyOS设备的串口端口与目标设备的串口正确连接。
2. 在HarmonyOS设备上执行上述示例代码。
3. 返回success日志，表示相关接口调用成功，设备串口通信能力正常；返回failed或error日志，表示接口调用失败，请检查硬件连接和配置参数。
4. 可通过回环测试（将串口的TX和RX短接）验证数据的自发自收功能是否正常。
