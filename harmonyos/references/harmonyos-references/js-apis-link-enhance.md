---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-link-enhance
title: @ohos.distributedsched.linkEnhance (增强连接)
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > ArkTS API > @ohos.distributedsched.linkEnhance (增强连接)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44ed7fcd87ca1097de39c6a30c6a4bf0b164661728ef90e036febe502e1e9623
---

linkEnhance模块提供高效的蓝牙连接和数据传输功能，增强设备间连接的稳定性。使用多通道合并算法，增加设备间连接数，提升跨设备数据传输能力，改善用户使用体验。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
```

## linkEnhance.createServer

PhonePC/2in1TabletTVWearable

createServer(name: string): Server

在服务端设备上，应用创建服务。通过start()开启后，该设备可作为服务端被其他设备连接。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 自定义的非空字符串，标识应用的服务名，最大长度255字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Server](js-apis-link-enhance.md#server) | 创建成功的服务对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390203 | Duplicate server name. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. // 使用服务名构造Server
11. let server: linkEnhance.Server = linkEnhance.createServer(name);
12. } catch (err) {
13. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
14. (err as BusinessError).message);
15. }
```

## linkEnhance.createConnection

PhonePC/2in1TabletTVWearable

createConnection(deviceId: string, name: string): Connection

作为客户端的设备创建连接对象，以便后续向服务端设备发起连接。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 连接的目标设备的deviceId，即对端设备的BLE MAC地址。BLE MAC的获取方法，请参考[查找设备](../harmonyos-guides/ble-development-guide.md)。 |
| name | string | 是 | 连接的目标设备的服务名，非空字符串，最大长度255字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Connection](js-apis-link-enhance.md#connection) | 创建成功的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

在客户端设备上，应用需要主动调用createConnection()接口创建连接对象。

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. } catch (err) {
12. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
13. (err as BusinessError).message);
14. }
```

## Server

PhonePC/2in1TabletTVWearable

服务对象，提供启动服务、停止服务、关闭服务、注册/取消注册服务端回调等方法。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

以下方法，在服务端设备上执行。

### start()

PhonePC/2in1TabletTVWearable

start(): void

创建服务成功后，需要调用start()开启该服务，方可被客户端连接，最大服务个数为10。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390202 | The number of servers exceeds the limit. |
| 32390300 | Internal error. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. let server: linkEnhance.Server = linkEnhance.createServer(name);
11. server.start();
12. } catch (err) {
13. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
14. (err as BusinessError).message);
15. }
```

### stop()

PhonePC/2in1TabletTVWearable

stop(): void

使用完服务时，调用stop停止服务，停止后可以调用start重新开启服务。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. let server: linkEnhance.Server = linkEnhance.createServer(name);
11. server.start();
12. server.stop();
13. } catch (err) {
14. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
15. (err as BusinessError).message);
16. }
```

### close()

PhonePC/2in1TabletTVWearable

close(): void

当业务执行完毕，服务端清理资源时，调用close()方法，销毁Server对象，释放相关资源。之后如果再次与对端设备交互，需要重新创建Server对象。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. let server: linkEnhance.Server = linkEnhance.createServer(name);
11. server.start();
12. server.close();
13. } catch (err) {
14. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
15. (err as BusinessError).message);
16. }
```

### on('connectionAccepted')

PhonePC/2in1TabletTVWearable

on(type: 'connectionAccepted', callback: Callback<Connection>): void

创建服务成功后，注册connectionAccepted事件的回调监听，等待对端连接。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionAccepted'，收到对端连接，触发该事件。 |
| callback | Callback<[Connection](js-apis-link-enhance.md#connection)> | 是 | 注册的回调函数。[Connection](js-apis-link-enhance.md#connection)返回的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. // 使用服务名构造Server
11. let server: linkEnhance.Server = linkEnhance.createServer(name);

13. // 订阅服务接收事件
14. server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
15. hilog.info(0x0000, TAG, 'serverOnCallback = ' + JSON.stringify(connection));
16. });
17. // 启动服务
18. server.start();
19. } catch (err) {
20. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
21. (err as BusinessError).message);
22. }
```

### off('connectionAccepted')

PhonePC/2in1TabletTVWearable

off(type: 'connectionAccepted', callback?: Callback<Connection>): void

取消注册connectionAccepted事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionAccepted'，收到对端连接，触发该事件。 |
| callback | Callback<[Connection](js-apis-link-enhance.md#connection)> | 否 | 注册的回调函数。[Connection](js-apis-link-enhance.md#connection)返回的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. // 使用服务名构造Server
11. let server: linkEnhance.Server = linkEnhance.createServer(name);
12. server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
13. hilog.info(0x0000, TAG, 'accept new connection');
14. });
15. // 取消订阅服务接收
16. server.off('connectionAccepted', (connection: linkEnhance.Connection): void => {
17. hilog.info(0x0000, TAG, 'accept new connection');
18. });
19. } catch (err) {
20. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
21. (err as BusinessError).message);
22. }
```

### on('serverStopped')

PhonePC/2in1TabletTVWearable

on(type: 'serverStopped', callback: Callback<number>): void

在创建服务成功后，注册serverStopped回调，监听服务异常停止。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serverStopped'，底层服务异常时，触发该事件。 |
| callback | Callback<number> | 是 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. // 使用服务名构造Server
11. let server: linkEnhance.Server = linkEnhance.createServer(name);

13. // 订阅服务停止
14. server.on('serverStopped', (reason: number): void => {
15. hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
16. });
17. // 启动服务
18. server.start();
19. } catch (err) {
20. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
21. (err as BusinessError).message);
22. }
```

### off('serverStopped')

PhonePC/2in1TabletTVWearable

off(type: 'serverStopped', callback?: Callback<number>): void

取消注册serverStopped事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serverStopped'，底层服务异常时触发。 |
| callback | Callback<number> | 否 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let name: string = "demo";
9. hilog.info(0x0000, TAG, 'start server name = ' + name);
10. // 使用服务名构造Server
11. let server: linkEnhance.Server = linkEnhance.createServer(name);
12. server.on('serverStopped', (reason: number): void => {
13. hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
14. });
15. // 取消订阅服务停止
16. server.off('serverStopped', (reason: number): void => {
17. hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
18. });
19. } catch (err) {
20. hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
21. (err as BusinessError).message);
22. }
```

## ConnectResult

PhonePC/2in1TabletTVWearable

客户端调用connect()后，返回的连接结果。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端设备ID，成功返回对端设备的deviceId，失败返回空字符串。 |
| success | boolean | 否 | 否 | 连接结果，true表示连接成功，false表示连接失败。 |
| reason | number | 否 | 否 | 连接成功返回0，连接失败返回错误码：  - 32390200：表示客户端连接超时。  - 32390201：表示服务端服务未启动。  - 32390300：表示内部错误。  更多关于错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。 |

## Connection

PhonePC/2in1TabletTVWearable

连接对象，提供连接、断连、获取对端设备ID、发送数据、注册/取消注册回调等方法。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

### connect()

PhonePC/2in1TabletTVWearable

connect(): void

在客户端执行，向服务端设备发起连接，最大连接个数限制为10。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390204 | The number of connection exceeds the limit. |
| 32390300 | Internal error. |

**示例：**

客户端设备上的应用在创建Connection对象成功后，调用connect()方法连接目标设备（即服务端）。

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. // 订阅连接结果
12. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
13. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
14. });
15. // 发起连接
16. connection.connect();
17. } catch (err) {
18. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
19. (err as BusinessError).message);
20. }
```

### disconnect()

PhonePC/2in1TabletTVWearable

disconnect(): void

业务执行完毕后，双端任意设备可调用该接口断开连接。创建的connection对象仍有效，需要时可调用connect()重新连接。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
12. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
13. if (result.success) {
14. connection.disconnect();
15. }
16. });
17. connection.connect();
18. } catch (err) {
19. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
20. (err as BusinessError).message);
21. }
```

### close()

PhonePC/2in1TabletTVWearable

close(): void

业务执行完毕后，任意设备可调用该接口销毁connection对象，释放资源。若需再次与对端设备交互，必须重新创建connection对象并调用connect()发起连接。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
12. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
13. if (result.success) {
14. connection.close();
15. }
16. });
17. connection.connect();
18. } catch (err) {
19. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
20. (err as BusinessError).message);
21. }
```

### getPeerDeviceId()

PhonePC/2in1TabletTVWearable

getPeerDeviceId(): string

获取对端设备的deviceId，作为对端设备的标识符，连接成功后或者被连接成功后调用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对端设备的deviceId，即对端设备的BLE MAC地址。如果获取失败返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.getPeerDeviceId();
12. hilog.info(0x0000, TAG, "peerDeviceId=%{public}s" + connection.getPeerDeviceId());
13. } catch (err) {
14. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
15. (err as BusinessError).message);
16. }
```

### sendData()

PhonePC/2in1TabletTVWearable

sendData(data: ArrayBuffer): void

客户端连接成功后，可以向服务端发送数据。服务端接收到连接回调时，也可以向客户端发送数据。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [ArrayBuffer](../harmonyos-guides/arraybuffer-object.md) | 是 | 需要发送的数据，最大发送长度为1024字节。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390205 | Connection is not ready. |
| 32390206 | Invalid parameter. |
| 32390300 | Internal error. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
12. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
13. if (result.success) {
14. let len = 1;
15. let arraybuffer = new ArrayBuffer(len); // 创建需要发送的数据
16. connection.sendData(arraybuffer);
17. hilog.info(0x0000, TAG, "sendData data connection peerDeviceId=%{public}s" + connection.getPeerDeviceId());
18. connection.disconnect();
19. }
20. });
21. connection.connect();
22. } catch (err) {
23. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
24. (err as BusinessError).message);
25. }
```

### on('connectResult')

PhonePC/2in1TabletTVWearable

on(type: 'connectResult', callback: Callback<ConnectResult>): void

注册connect事件的回调监听，通过回调函数获取连接结果。使用callback进行异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectResult'，完成connect()调用，触发该事件。 |
| callback | Callback<[ConnectResult](js-apis-link-enhance.md#connectresult)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. // 订阅连接结果
12. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
13. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
14. });

16. // 发起连接
17. connection.connect();
18. } catch (err) {
19. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
20. (err as BusinessError).message);
21. }
```

### off('connectResult')

PhonePC/2in1TabletTVWearable

off(type: 'connectResult', callback?: Callback<ConnectResult>): void

取消connect事件的回调监听，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectResult'，完成connect()调用，触发该事件。 |
| callback | Callback<[ConnectResult](js-apis-link-enhance.md#connectresult)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
12. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
13. });
14. // 取消订阅连接结果
15. connection.off('connectResult', (result: linkEnhance.ConnectResult): void => {
16. hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
17. });
18. } catch (err) {
19. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
20. (err as BusinessError).message);
21. }
```

### on('disconnected')

PhonePC/2in1TabletTVWearable

on(type: 'disconnected', callback: Callback<number>): void

注册disconnected事件的回调监听，连接被动断开或者底层异常断开时触发该事件。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnected'，连接被动断开或底层异常断开时，触发该事件。 |
| callback | Callback<number> | 是 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. // 订阅断连通知
12. connection.on('disconnected', (number: number) => {
13. hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
14. });
15. } catch (err) {
16. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
17. (err as BusinessError).message);
18. }
```

### off('disconnected')

PhonePC/2in1TabletTVWearable

off(type: 'disconnected', callback?: Callback<number>): void

取消注册disconnected事件的回调监听。连接被动断开或底层异常断开时触发该事件，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnected'，连接被动断开或底层异常断开时，触发该事件。 |
| callback | Callback<number> | 否 | 注册的回调函数。number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. connection.on('disconnected', (number: number) => {
12. hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
13. });
14. // 取消订阅断连通知
15. connection.off('disconnected', (number: number) => {
16. hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
17. });
18. } catch (err) {
19. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
20. (err as BusinessError).message);
21. }
```

### on('dataReceived')

PhonePC/2in1TabletTVWearable

on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void

注册dataReceived事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'dataReceived'，收到数据时，触发该事件。 |
| callback | Callback<[ArrayBuffer](../harmonyos-guides/arraybuffer-object.md)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. // 发起连接
12. connection.connect();
13. // 订阅数据接收通知
14. connection.on('dataReceived', (data: ArrayBuffer) => {
15. hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
16. });
17. } catch (err) {
18. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
19. (err as BusinessError).message);
20. }
```

### off('dataReceived')

PhonePC/2in1TabletTVWearable

off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void

取消dataReceived事件的回调监听，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**模型约束**：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'dataReceived'，收到数据时，触发该事件。 |
| callback | Callback<[ArrayBuffer](../harmonyos-guides/arraybuffer-object.md)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](errorcode-link-enhance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```
1. import { linkEnhance } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "testDemo";

7. try {
8. let peerDeviceId: string = "00:11:22:33:44:55";
9. hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
10. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
11. // 订阅数据接收通知
12. connection.on('dataReceived', (data: ArrayBuffer) => {
13. hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
14. });
15. // 取消数据接收通知
16. connection.off('dataReceived', (data: ArrayBuffer) => {
17. hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
18. });
19. } catch (err) {
20. hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
21. (err as BusinessError).message);
22. }
```
