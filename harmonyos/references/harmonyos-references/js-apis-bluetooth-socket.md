---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket
title: @ohos.bluetooth.socket (蓝牙socket模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.socket (蓝牙socket模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:58+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:82f7d84b5db9366d432a84ef6f1583d03c2ec7843da906a55c49eea320a30a6d
---

本模块提供一种蓝牙套接字功能，可实现设备间连接和数据传输。当两个设备间进行蓝牙套接字通信交互时，依据设备功能的不同，可区分客户端与服务端。

支持的套接字链路类型包括[RFCOMM](../harmonyos-guides/terminology.md#rfcomm)和[L2CAP](../harmonyos-guides/terminology.md#l2cap)。

* RFCOMM链路类型也称为串口通信协议（Serial Port Profile, [SPP](../harmonyos-guides/terminology.md#spp)），适用于传统蓝牙（[BR](../harmonyos-guides/terminology.md#br)/[EDR](../harmonyos-guides/terminology.md#edr)）。
* L2CAP链路类型适用于传统蓝牙（BR/EDR）和低功耗蓝牙（[BLE](../harmonyos-guides/terminology.md#ble)）。

通过[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)创建客户端套接字并向服务端发起连接。

通过[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)创建服务端套接字并监听客户端的连接。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { socket } from '@kit.ConnectivityKit';
```

## socket.sppListen

PhonePC/2in1TabletTVWearable

sppListen(name: string, options: SppOptions, callback: AsyncCallback<number>): void

服务端使用，创建一个服务端监听套接字。使用Callback异步回调。

* 通过入参[socket.SppOptions](js-apis-bluetooth-socket.md#sppoptions)的type参数，可以创建不同链路类型的服务端套接字，适用于不同的场景。该操作会在蓝牙子系统中注册对应的服务，表示服务端支持的能力。
* 客户端可通过[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)向该服务端发起连接请求。
* 当应用不再需要该服务端套接字时，需通过[socket.sppCloseServerSocket](js-apis-bluetooth-socket.md#socketsppcloseserversocket)主动关闭创建时获取到的套接字，蓝牙子系统会删除此前注册的服务。如果此时客户端发起连接，就会连接失败。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 服务的名称，该字符串的字符个数范围为[0, 256]。 |
| options | [SppOptions](js-apis-bluetooth-socket.md#sppoptions) | 是 | 用于监听的套接字配置参数。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当创建服务端套接字成功，err为undefined，data为获取到的服务端套接字的ID，有效值为非负值；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let serverNumber = -1;
4. let serverSocket = (code: BusinessError, number: number) => {
5. if (code) {
6. console.error('sppListen error, code is ' + code);
7. return;
8. } else {
9. serverNumber = number;
10. console.info('sppListen success, serverNumber = ' + serverNumber);
11. }
12. }

14. // 以RFCOMM链路类型套接字为例
15. let sppOption:socket.SppOptions = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: socket.SppType.SPP_RFCOMM};
16. try {
17. socket.sppListen('server1', sppOption, serverSocket);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
```

## socket.getL2capPsm20+

PhonePC/2in1TabletTVWearable

getL2capPsm(serverSocket: number): number

获取服务端L2CAP链路类型套接字的协议/服务多路复用器值（Protocol/Service Multiplexer, [PSM](../harmonyos-guides/terminology.md#psm)），该值用于标识特定的服务数据传输通道。

说明

需要在服务端调用完[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)后调用该接口，且传入的链路类型[SppType](js-apis-bluetooth-socket.md#spptype)需是SPP\_L2CAP或SPP\_L2CAP\_BLE。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverSocket | number | 是 | 服务端套接字的ID。  该值是调用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)接口后，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回L2CAP链路类型套接字的psm值。  - [SppType](js-apis-bluetooth-socket.md#spptype)设置为SPP\_L2CAP\_BLE时，返回值的有效值范围为[0x01, 0xFF]。  - [SppType](js-apis-bluetooth-socket.md#spptype)设置为SPP\_L2CAP时，返回值的有效值范围为[0x0000, 0xFFFF]。  - 服务端通道建立异常或[SppType](js-apis-bluetooth-socket.md#spptype)非L2CAP链路类型时，返回-1。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 服务端获取客户端设备地址。
4. let serverNumber = 1; // 此处serverNumber需赋值为调用sppListen接口后，回调中得到的serverNumber。
5. try {
6. let l2capPsm: number = socket.getL2capPsm(serverNumber);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## socket.sppAccept

PhonePC/2in1TabletTVWearable

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端使用，接受客户端的套接字连接请求。使用Callback异步回调。

* 须在调用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)创建服务端套接字成功后，才能调用该接口监听客户端的连接请求。
* 客户端可通过[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)向该服务端发起连接请求。
* 连接建立成功后，即可通过[socket.sppWrite](js-apis-bluetooth-socket.md#socketsppwrite)、[socket.sppWriteAsync](js-apis-bluetooth-socket.md#socketsppwriteasync18)、[socket.sppReadAsync](js-apis-bluetooth-socket.md#socketsppreadasync18)等接口，同客户端进行数据传输。
* 当服务端不再需要已建立的连接时，可通过[socket.sppCloseClientSocket](js-apis-bluetooth-socket.md#socketsppcloseclientsocket)主动断开指定的客户端套接字连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverSocket | number | 是 | 服务端套接字的ID。  该值是调用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)接口后，通过其异步callback获取到的。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当收到客户端的连接请求且连接建立成功时，err为undefined，data是用于标识发起此次连接请求的客户端套接字ID，有效值为非负值；否则err为错误对象。 |
| **错误码**： |  |  |  |

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = -1;
4. let serverNumber = 1;
5. let acceptClientSocket = (code: BusinessError, number: number) => {
6. if (code) {
7. console.error('sppListen error, code is ' + code);
8. return;
9. } else {
10. clientNumber = number; // 获取的clientNumber用作客户端后续读/写操作socket的id。
11. console.info('sppListen success, clientNumber = ' + clientNumber);
12. }
13. }
14. try {
15. socket.sppAccept(serverNumber, acceptClientSocket); // serverNumber是sppListen回调中得到的serverNumber。
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
```

## socket.sppConnect

PhonePC/2in1TabletTVWearable

sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<number>): void

客户端使用，创建一个客户端套接字，并向服务端的特定服务发起连接请求。

* 通过[SppOptions](js-apis-bluetooth-socket.md#sppoptions)参数的type表示需要连接的服务类型。
* 需确保服务端设备已具备需要连接的服务。服务端可通过[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)注册并监听连接请求。
* 连接建立成功后，即可通过[socket.sppWrite](js-apis-bluetooth-socket.md#socketsppwrite)或[socket.sppWriteAsync](js-apis-bluetooth-socket.md#socketsppwriteasync18)接口，同服务端进行数据传输。
* 当客户端不再需要已建立的连接时，可通过[socket.sppCloseclientSocket](js-apis-bluetooth-socket.md#socketsppcloseclientsocket)主动断开连接。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| options | [SppOptions](js-apis-bluetooth-socket.md#sppoptions) | 是 | 客户端套接字连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当客户端发起连接成功，err为undefined，data为当前客户端套接字的ID，有效值为非负值；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientSocket = (code: BusinessError, number: number) => {
4. if (code) {
5. console.error('sppConnect error, code is ' + code);
6. return;
7. } else {
8. // 获取的number用作客户端后续读/写操作的socket id。
9. console.info('bluetooth clientSocket Number: ' + number);
10. }
11. }

13. // 以RFCOMM链路类型套接字为例
14. let sppOption:socket.SppOptions = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: socket.SppType.SPP_RFCOMM};
15. try {
16. socket.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

## socket.getDeviceId17+

PhonePC/2in1TabletTVWearable

getDeviceId(clientSocket: number): string

客户端和服务端均可使用，获取套接字连接中的对端设备蓝牙地址。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口后，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回对端设备地址。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 已配对的地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 服务端获取客户端设备地址。
4. let clientSocket = 1; // clientSocket是sppAccept回调中得到的，调用getDeviceId接口前需更新clientSocket。
5. try {
6. let deviceAddr: string = socket.getDeviceId(clientSocket);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }

11. // 客户端获取服务端设备地址。
12. // clientSocket是sppConnect回调中得到的，调getDeviceId接口前需更新clientSocket。
13. try {
14. let deviceAddr: string = socket.getDeviceId(clientSocket);
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
```

## socket.sppCloseServerSocket

PhonePC/2in1TabletTVWearable

sppCloseServerSocket(socket: number): void

服务端使用，删除指定的服务端套接字。

* 需先调用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)并获取到有效的服务端监听套接字标识符。
* 若服务端无需继续监听，可调用本接口以关闭监听套接字，蓝牙子系统会删除此前注册的服务。如果此时客户端发起连接，就会连接失败。
* 若服务端此时与其他客户端存在连接，该接口调用后，也会主动断开与客户端的连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 服务端监听套接字的ID。  该值是调用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)接口，通过其异步callback获取到的。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let serverNumber = 1; // 此处serverNumber需赋值为调用sppListen接口后，在回调中得到的serverNumber。
4. try {
5. socket.sppCloseServerSocket(serverNumber);
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## socket.sppCloseClientSocket

PhonePC/2in1TabletTVWearable

sppCloseClientSocket(socket: number): void

客户端和服务端均可使用，关闭指定的客户端套接字，并断开客户端和服务端之间的连接。

* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 当应用不再需要已建立好的套接字连接时，需主动调用该接口断开客户端和服务端之间的连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 客户端套接字的ID。  该值是调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = 1; // 入参clientNumber由sppAccept或sppConnect接口获取。
4. try {
5. socket.sppCloseClientSocket(clientNumber);
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## socket.sppWrite

PhonePC/2in1TabletTVWearable

sppWrite(clientSocket: number, data: ArrayBuffer): void

客户端和服务端均可使用，向对端设备发送数据。

* 仅在双方成功建立连接后，调用本接口才有效。
* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 若开发者需感知传输过程中异常断连等错误，建议使用[socket.sppWriteAsync](js-apis-bluetooth-socket.md#socketsppwriteasync18)。
* 按照蓝牙协议规范，数据通道在空闲状态需进入休眠模式以降低功耗。蓝牙子系统实现上，通道在5-7s内没有数据交互时会进入休眠模式，将导致下次调用此接口发送数据前，会耗费500ms左右退出休眠模式才开始发送数据。
* 若想减少每次发送数据前退出休眠模式的耗时，建议每3s左右可往数据通道上发送一次任意大小的心跳数据，对数据通道进行保活，可防止进入休眠模式，但同时也会提高设备功耗。
* 链路类型为[SPP\_L2CAP](js-apis-bluetooth-socket.md#spptype)或[SPP\_L2CAP\_BLE](js-apis-bluetooth-socket.md#spptype)时，单次发送数据大小存在限制，单位为Byte，超过限制范围的数据将被截断。链路类型为SPP\_L2CAP\_BLE时单次发送数据大小范围为[1, 65535]；链路类型为SPP\_L2CAP时服务端单次发送数据大小范围为[1, 4091]，客户端单次发送数据大小范围为[1, 8085]。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = 1; // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let arrayBuffer = new ArrayBuffer(8);
5. let data = new Uint8Array(arrayBuffer);
6. data[0] = 123;
7. try {
8. socket.sppWrite(clientNumber, arrayBuffer);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## socket.on('sppRead')

PhonePC/2in1TabletTVWearable

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

客户端和服务端均可使用，订阅套接字读请求事件。调用该接口后，当收到对端发送的数据会执行订阅的回调函数。

* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 不可以和API version 18开始支持的[socket.sppReadAsync](js-apis-bluetooth-socket.md#socketsppreadasync18)接口混用，同一路套接字连接只能使用socket.on('sppRead')接口或者[socket.sppReadAsync](js-apis-bluetooth-socket.md#socketsppreadasync18)接口。
* 若开发者需感知传输过程中异常断连等错误，建议使用[socket.sppReadAsync](js-apis-bluetooth-socket.md#socketsppreadasync18)。
* 链路类型为[SPP\_RFCOMM](js-apis-bluetooth-socket.md#spptype)时，当接收数据大小超过1024字节时，会自动分多次接收，每次接收数据大小范围为[1, 1024]。
* 链路类型为[SPP\_L2CAP](js-apis-bluetooth-socket.md#spptype)或[SPP\_L2CAP\_BLE](js-apis-bluetooth-socket.md#spptype)时，单次接收数据大小存在限制，需一次性读取全部数据，单位为Byte，超过最大接收数据大小限制将被截断。链路类型为SPP\_L2CAP\_BLE时单次接收数据大小范围为[1, 65535]；链路类型为SPP\_L2CAP时服务端和客户端单次接收数据大小范围为[1, 8087]。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'sppRead'，表示订阅spp读请求事件。  当收到了对端发送的数据时，触发该事件。 |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |
| callback | Callback<ArrayBuffer> | 是 | 指定订阅的回调函数，会返回读取到的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = 1; // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let dataRead = (dataBuffer: ArrayBuffer) => {
5. let data = new Uint8Array(dataBuffer);
6. console.info('bluetooth data length is: ' + data.byteLength);
7. }
8. try {
9. socket.on('sppRead', clientNumber, dataRead);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## socket.off('sppRead')

PhonePC/2in1TabletTVWearable

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅套接字读请求事件。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'sppRead'，表示取消订阅spp读请求事件。 |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |
| callback | Callback<ArrayBuffer> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[socket.on('sppRead')](js-apis-bluetooth-socket.md#socketonsppread)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = 1; // 入参clientNumber由sppAccept或sppConnect接口获取。
4. try {
5. socket.off('sppRead', clientNumber);
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## socket.sppWriteAsync18+

PhonePC/2in1TabletTVWearable

sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>

客户端和服务端均可使用，向对端设备发送数据。使用Promise异步回调。该接口支持断开连接时，会抛出错误码并返回。

* 仅在双方成功建立连接后，调用本接口才有效。
* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 按照蓝牙协议规范，数据通道在空闲状态需进入休眠模式以降低功耗。蓝牙子系统实现上，通道在5-7s内没有数据交互时会进入休眠模式，将导致下次调用此接口发送数据前，会耗费500ms左右退出休眠模式才开始发送数据。
* 若想减少每次发送数据前退休眠模式的耗时，建议每3s左右可往数据通道上发送一次任意大小的心跳数据，对数据通道进行保活，可防止进入休眠模式，但同时也会提高设备功耗。
* 链路类型为[SPP\_L2CAP](js-apis-bluetooth-socket.md#spptype)或[SPP\_L2CAP\_BLE](js-apis-bluetooth-socket.md#spptype)时，单次发送数据大小存在限制，单位为Byte，超过限制大小的数据将被截断。链路类型为SPP\_L2CAP\_BLE时单次发送数据大小范围为[1, 65535]；链路类型为SPP\_L2CAP时服务端单次发送数据大小范围为[1, 4091]，客户端单次发送数据大小范围为[1, 8085]。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = 1; // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let arrayBuffer = new ArrayBuffer(8);
5. let data = new Uint8Array(arrayBuffer);
6. try {
7. socket.sppWriteAsync(clientNumber, arrayBuffer).then(() => {
8. console.info("sppWrite success");
9. });
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## socket.sppReadAsync18+

PhonePC/2in1TabletTVWearable

sppReadAsync(clientSocket: number): Promise<ArrayBuffer>

客户端和服务端均可使用，读取对端发送数据的异步接口。使用Promise异步回调。该接口支持断开连接时，会抛出错误码并返回。

* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 不可以和API version 10开始支持的[socket.on('sppRead')](js-apis-bluetooth-socket.md#socketonsppread)接口混用，同一路socket只能使用[socket.on('sppRead')](js-apis-bluetooth-socket.md#socketonsppread)接口或者socket.sppReadAsync接口。
* 通过Promise异步返回读取的数据，建议在连接成功后循环调用去获取接收到的数据，若不及时调用会丢失接收的数据。
* 该接口为异步接口，需要等异步回调结果返回后才能进行下一次调用。
* 链路类型为[SPP\_RFCOMM](js-apis-bluetooth-socket.md#spptype)时，当接收数据大小超过1024字节时，会自动分多次接收，每次接收数据大小范围为[1, 1024]。
* 链路类型为[SPP\_L2CAP](js-apis-bluetooth-socket.md#spptype)或[SPP\_L2CAP\_BLE](js-apis-bluetooth-socket.md#spptype)时，单次接收数据大小存在限制，需一次性读取全部数据，单位为Byte，超过最大接收数据大小限制将被截断。链路类型为SPP\_L2CAP\_BLE时单次接收数据大小范围为[1, 65535]；链路类型为SPP\_L2CAP时服务端和客户端单次接收数据大小范围为[1, 8087]。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象。返回读取的数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 入参clientNumber由sppAccept或sppConnect接口获取。
4. async function readAsync(clientNumber: number) {
5. let flag = 1;
6. try {
7. while (flag) { // 该接口需业务循环调用读取，具体循环形式按业务需要来实现，这里只是示例。
8. let buffer = await socket.sppReadAsync(clientNumber); // 使用await确保顺序读取。
9. let data = new Uint8Array(buffer);
10. if (data) {
11. console.info('sppRead success, data length = ' + data.byteLength);
12. // 在此处理接收到的数据。
13. }
14. }
15. } catch (err) {
16. console.error('startSppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. socket.sppCloseClientSocket(clientNumber); // 发生错误时关闭连接。
18. }
19. }
```

## socket.getMaxReceiveDataSize22+

PhonePC/2in1TabletTVWearable

getMaxReceiveDataSize(clientSocket: number): number

客户端和服务端均可使用，获取当前套接字链路类型下最大接收数据的大小。

* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 若套接字链路类型为[SPP\_RFCOMM](js-apis-bluetooth-socket.md#spptype)时，最大接收数据大小无限制且返回值为0。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回最大接收数据的大小，单位：Byte。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let clientSocket = 1;
5. try {
6. let result: number = socket.getMaxReceiveDataSize(clientSocket);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## socket.getMaxTransmitDataSize22+

PhonePC/2in1TabletTVWearable

getMaxTransmitDataSize(clientSocket: number): number

客户端和服务端均可使用，获取套接字当前链路类型下最大发送数据的大小。

* 若客户端使用，需在调用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)后，且连接成功后使用。
* 若服务端使用，需在调用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)后，且连接成功后使用。
* 若套接字链路类型为[SPP\_RFCOMM](js-apis-bluetooth-socket.md#spptype)时，最大发送数据大小无限制且返回值为0。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回最大发送数据的大小，单位：Byte。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let clientSocket = 1;
5. try {
6. let result: number = socket.getMaxTransmitDataSize(clientSocket);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## socket.isConnected22+

PhonePC/2in1TabletTVWearable

isConnected(clientSocket: number): boolean

客户端和服务端均可使用，检查当前链路是否已连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端套接字的ID。  该值是调用[sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)或[sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 套接字链路是否已连接，true表示已连接，false表示未连接。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 入参clientNumber由sppAccept或sppConnect接口获取。
4. let clientSocket = 1;
5. try {
6. let result: boolean = socket.isConnected(clientSocket);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## SppOptions

PhonePC/2in1TabletTVWearable

描述套接字的配置参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uuid | string | 否 | 否 | RFCOMM套接字链路类型的服务UUID，例如"00001101-0000-1000-8000-00805F9B34FB"。  - 建议开发者使用自定义的服务UUID（可通过工具函数[util.generateRandomUUID](js-apis-util.md#utilgeneraterandomuuid9)生成），也可以使用标准协议定义的Serial Port UUID服务(00001101-0000-1000-8000-00805F9B34FB)。  - SppType设置为SPP\_RFCOMM时该参数必选。  - SppType设置为SPP\_L2CAP或SPP\_L2CAP\_BLE时设置为空字符串。 |
| secure | boolean | 否 | 否 | 是否是安全通道。true表示是安全通道，false表示非安全通道。 |
| type | [SppType](js-apis-bluetooth-socket.md#spptype) | 否 | 否 | 蓝牙套接字链路类型。 |
| psm20+ | number | 否 | 是 | 协议/服务多路复用器值，用于标识特定的服务数据传输通道。不填写该参数时默认值为-1。  对于客户端：  - SppType设置为SPP\_RFCOMM时，该参数不填。  - SppType设置为SPP\_L2CAP\_BLE或SPP\_L2CAP时，需和服务端的psm值保持一致。  对于服务端：  - SppType设置为SPP\_RFCOMM时，该参数不填。  - SppType设置为SPP\_L2CAP\_BLE时，psm值必须由系统自动分配，有效值范围为[0x01, 0xFF]。  - SppType设置为SPP\_L2CAP时，psm值可以主动设置或蓝牙子系统分配，若为主动设置，其有效范围为[0x00, 0xFFFF]，并且需要满足低位字节最低位必须为1，高位字节最低位必须为0；若为蓝牙子系统分配，该参数不填，可以通过[socket.getL2capPsm](js-apis-bluetooth-socket.md#socketgetl2cappsm20)接口获取psm值。 |

## SppType

PhonePC/2in1TabletTVWearable

枚举，蓝牙套接字链路类型。

* 不同类型的蓝牙设备需要选取不同的链路类型。
* 针对低功耗蓝牙（BLE）设备，必须使用L2CAP链路类型。
* 针对传统蓝牙（BR/EDR）设备，建议优先采用RFCOMM链路进行连接。其优势在于可通过UUID服务动态协商信道（即设备通过查询服务UUID自动确定通信频道的过程），同时具备更高的安全性和可靠性。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPP\_RFCOMM | 0 | 基于传统蓝牙（BR/EDR）的RFCOMM链路。 |
| SPP\_L2CAP20+ | 1 | 基于传统蓝牙（BR/EDR）的L2CAP链路。 |
| SPP\_L2CAP\_BLE20+ | 2 | 基于低功耗蓝牙（BLE）的L2CAP链路。 |
