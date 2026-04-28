---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap
title: ssap（星闪SSAP连接能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > ssap（星闪SSAP连接能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:77d0d323dd6b36c8688a5ffc417a40299a180897660870678e3c568651c54aac
---

本模块提供了SSAP（SparkLink Service Access Protocol）连接功能。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ssap } from '@kit.NearLinkKit';
```

## ConnectionState

PhonePC/2in1TabletTVWearable

type ConnectionState = [constant.ConnectionState](nearlink-constant.md#connectionstate)

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## createClient

PhonePC/2in1TabletTVWearable

createClient(address: string): Client

创建ssap客户端实例。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 远端服务端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Client](nearlink-ssap.md#client) | ssap客户端实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr);
8. console.info('client: ' + JSON.stringify(client));
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## createServer

PhonePC/2in1TabletTVWearable

createServer(): Server

创建ssap服务端实例。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Server](nearlink-ssap.md#server) | ssap服务端实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let server: ssap.Server;
5. try {
6. server = ssap.createServer();
7. console.info('server: ' + JSON.stringify(server));
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## Client

PhonePC/2in1TabletTVWearable

说明

提供和远端设备ssap数据交互操作方法，使用前需要使用[ssap.createClient](nearlink-ssap.md#createclient)方法创建一个[Client](nearlink-ssap.md#client)实例。

一个应用针对一个远端设备只需要创建一次实例。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

### connect

PhonePC/2in1TabletTVWearable

connect(): Promise<void>

向服务端发起连接。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info("connect success");
10. });
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### disconnect

PhonePC/2in1TabletTVWearable

disconnect(): Promise<void>

向服务端发起断连，断开已有连接或者终止正在建立的连接。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info("connect success"); // 建立连接
10. });
11. client.disconnect().then(() => {
12. console.info("disconnect success"); // 断开连接
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

### close

PhonePC/2in1TabletTVWearable

close(): void

关闭客户端。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.close();
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### getServices

PhonePC/2in1TabletTVWearable

getServices(): Promise<Array<Service>>;

获取服务端支持的服务列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise‌<‌Array‌<‌[Service](nearlink-ssap.md#service)‌>‌> | Promise对象，返回服务端支持的服务列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info('connect success');
10. });
11. // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
12. setTimeout(() => {
13. client.getServices().then((result: Array<ssap.Service>) => {
14. console.info('getServices successfully:' + JSON.stringify(result));
15. });
16. }, 3000);
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### readProperty

PhonePC/2in1TabletTVWearable

readProperty(property: Property): Promise<Property>

读取服务端属性。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [Property](nearlink-ssap.md#property) | 是 | 服务端属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Property](nearlink-ssap.md#property)> | Promise对象，返回服务端属性。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info('connect success');
10. });
11. // 创建property,实际开发时需要通过getServices接口从服务端获取
12. let arrayBufferC = new ArrayBuffer(8);
13. let properV = new Uint8Array(arrayBufferC);
14. properV[0] = 1;
15. let property: ssap.Property = {
16. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
17. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
18. value: arrayBufferC
19. };
20. // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
21. setTimeout(()=>{
22. client.readProperty(property).then((result: ssap.Property) => {
23. console.info('readProperty successfully:' + JSON.stringify(result));
24. });
25. }, 3000);
26. } catch (err) {
27. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
28. }
```

### writeProperty

PhonePC/2in1TabletTVWearable

writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>

写入服务端property值。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [Property](nearlink-ssap.md#property) | 是 | 服务端属性。 |
| writeType | [PropertyWriteType](nearlink-ssap.md#propertywritetype) | 是 | 写类型，支持服务端回复响应和不回复响应两种方式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info('connect success');
10. });
11. // 创建property,实际开发时需要通过getServices接口从服务端获取
12. let arrayBufferC = new ArrayBuffer(8);
13. // 期望写入的property值
14. let properV = new Uint8Array(arrayBufferC);
15. properV[0] = 1;
16. let property: ssap.Property = {
17. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
18. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
19. value: arrayBufferC
20. };
21. // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
22. setTimeout(()=>{
23. client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
24. console.info('writeProperty success');
25. });
26. }, 3000);
27. } catch (err) {
28. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
29. }
```

### setPropertyNotification

PhonePC/2in1TabletTVWearable

setPropertyNotification(property: Property, enable: boolean): Promise<void>

设置Property变化通知。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [Property](nearlink-ssap.md#property) | 是 | 服务端属性。 |
| enable | boolean | 是 | true: 打开通知功能。false: 关闭通知功能。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info('connect success');
10. });
11. // 创建property,实际开发时需要通过getServices接口从服务端获取
12. let arrayBufferC = new ArrayBuffer(8);
13. // 期望写入的property值
14. let properV = new Uint8Array(arrayBufferC);
15. properV[0] = 1;
16. let property: ssap.Property = {
17. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
18. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
19. value: arrayBufferC
20. };
21. // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
22. setTimeout(()=>{
23. client.setPropertyNotification(property, true).then(() => {
24. console.info('setPropertyNotification success');
25. });
26. }, 3000);
27. } catch (err) {
28. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
29. }
```

### requestMtuSize

PhonePC/2in1TabletTVWearable

requestMtuSize(mtu: number): Promise<void>

发起MTU协商请求。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | MTU参数，范围22~512字节。默认值为256字节 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let client: ssap.Client;
6. try {
7. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
8. client.connect().then(() => {
9. console.info('connect success');
10. });
11. // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
12. setTimeout(()=>{
13. client.requestMtuSize(128).then(() => {
14. console.info('requestMtuSize success');
15. });
16. }, 3000);
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### on( 'propertyChange')

PhonePC/2in1TabletTVWearable

on(type: 'propertyChange', callback: Callback<Property>): void

订阅Property变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyChange"字符串，表示Property变化事件。 |
| callback | Callback<[Property](nearlink-ssap.md#property)> | 是 | 表示星闪Property变化事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.on('propertyChange', onPropertyChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

### off( 'propertyChange')

PhonePC/2in1TabletTVWearable

off(type: 'propertyChange', callback?: Callback<Property>): void

取消订阅Property变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyChange"字符串，表示Property变化事件。 |
| callback | Callback<[Property](nearlink-ssap.md#property)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.off('propertyChange', onPropertyChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

### on( 'connectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionChangeState](nearlink-ssap.md#connectionchangestate)> | 是 | 表示连接状态变化事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.on('connectionStateChange', onConnectionStateChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

### off( 'connectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void

取消订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionChangeState](nearlink-ssap.md#connectionchangestate)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.off('connectionStateChange', onConnectionStateChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

### on( 'mtuChange')

PhonePC/2in1TabletTVWearable

on(type: 'mtuChange', callback: Callback<number>): void

订阅MTU变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"mtuChange"字符串，表示MTU变化事件。 |
| callback | Callback<number> | 是 | 表示MTU变化事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onMtuChange:(data: number) => void = (data: number) => {
5. console.info('data:'+ data);
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.on('mtuChange', onMtuChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

### off( 'mtuChange')

PhonePC/2in1TabletTVWearable

off(type: 'mtuChange', callback?: Callback<number>): void

取消订阅MTU变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"mtuChange"字符串，表示MTU变化事件。 |
| callback | Callback<number> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onMtuChange:(data: number) => void = (data: number) => {
5. console.info('data:'+ data);
6. }
7. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
8. let client: ssap.Client;
9. try {
10. client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
11. client.off('mtuChange', onMtuChange);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

## Server

PhonePC/2in1TabletTVWearable

说明

提供和远端设备ssap数据交互操作方法，使用前需要使用createServer方法创建一个Server实例。

一个应用针对一个远端设备只需要创建一次实例。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

### addService

PhonePC/2in1TabletTVWearable

addService(service: Service): void

服务端添加服务。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | [Service](nearlink-ssap.md#service) | 是 | 服务端提供的服务信息，支持添加多个服务，根据不同的UUID区分。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 构造descriptor
5. let descriptorsArray: Array<ssap.PropertyDescriptor> = [];
6. let arrayBuffer = new ArrayBuffer(8);
7. let descValue = new Uint8Array(arrayBuffer);
8. descValue[0] = 11;
9. descValue[1] = 22;
10. let descriptor: ssap.PropertyDescriptor = {
11. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
12. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
13. value: arrayBuffer,
14. descriptorType: ssap.PropertyDescriptorType.PROPERTY,
15. isWriteable: true
16. };
17. descriptorsArray[0] = descriptor;
18. // 构造properties
19. let propertiesArray: Array<ssap.Property> = [];
20. let arrayBufferProperty = new ArrayBuffer(8);
21. let properValue = new Uint8Array(arrayBufferProperty);
22. properValue[0] = 1;
23. let property1: ssap.Property = {
24. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
25. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
26. value: arrayBufferProperty,
27. descriptors:descriptorsArray
28. };
29. let property2: ssap.Property = {
30. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
31. propertyUuid: '37bea880-fc70-11ea-b720-000000003421',
32. value: arrayBufferProperty,
33. descriptors:descriptorsArray,
34. operation:12
35. };
36. propertiesArray[0] = property1;
37. propertiesArray[1] = property2;
38. // 构造服务
39. let Service: ssap.Service = {
40. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
41. properties:propertiesArray
42. };
43. let server: ssap.Server;
44. try {
45. server = ssap.createServer();
46. server.addService(Service);
47. } catch (err) {
48. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
49. }
```

### removeService

PhonePC/2in1TabletTVWearable

removeService(serviceUuid: string): void

服务端删除服务。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 服务UUID，用户添加服务时的UUID号，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let server: ssap.Server;
5. try {
6. server = ssap.createServer();
7. // 服务已通过addService添加，可以通过指定UUID进行删除
8. let serviceUuid = '37bea880-fc70-11ea-b720-000000004386';
9. server.removeService(serviceUuid);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### close

PhonePC/2in1TabletTVWearable

close(): void

关闭服务端。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let server: ssap.Server;
5. try {
6. server = ssap.createServer();
7. server.close();
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

### notifyPropertyChanged

PhonePC/2in1TabletTVWearable

notifyPropertyChanged(address: string, property: Property): Promise<void>

通知客户端property值更新。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| property | [Property](nearlink-ssap.md#property) | 是 | 发生值变化的Property。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 构造descriptor
5. let descriptorsArray: Array<ssap.PropertyDescriptor> = [];
6. let arrayBuffer = new ArrayBuffer(8);
7. let descValue = new Uint8Array(arrayBuffer);
8. descValue[0] = 11;
9. descValue[1] = 22;
10. let descriptor: ssap.PropertyDescriptor = {
11. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
12. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
13. value: arrayBuffer,
14. descriptorType:ssap.PropertyDescriptorType.PROPERTY,
15. isWriteable:true
16. };
17. descriptorsArray[0] = descriptor;
18. // 构造properties
19. let arrayBufferProperty = new ArrayBuffer(8);
20. let properValue = new Uint8Array(arrayBufferProperty);
21. properValue[0] = 123; // 本次更新后的值
22. let property: ssap.Property = {
23. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
24. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
25. value: arrayBufferProperty,
26. descriptors:descriptorsArray
27. };
28. let server: ssap.Server;
29. try {
30. server = ssap.createServer();
31. // 地址是服务端缓存的已连接的客户端设备
32. server.notifyPropertyChanged('00:11:22:33:AA:FF', property).then(() => {
33. console.info('notifyPropertyChanged success');
34. });
35. } catch (err) {
36. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
37. }
```

### sendResponse

PhonePC/2in1TabletTVWearable

sendResponse(response: ServerResponse): void

回复客户端读写请求。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | [ServerResponse](nearlink-ssap.md#serverresponse) | 是 | 回复客户端的响应数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 订阅客户端的读写请求，收到请求后通过该接口回复
5. let arrayBuffer = new ArrayBuffer(8);
6. let descValue = new Uint8Array(arrayBuffer);
7. descValue[0] = 11;
8. descValue[1] = 22;
9. let resp: ssap.ServerResponse = {
10. address: '00:11:22:33:AA:FF', // 请求方的客户端地址
11. requestId: 1, // 请求方传入
12. value: arrayBuffer // 回复的数据
13. };
14. let server: ssap.Server;
15. try {
16. server = ssap.createServer();
17. // 地址是服务端缓存的已连接的客户端设备
18. server.sendResponse(resp);
19. } catch (err) {
20. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
21. }
```

### on('connectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionChangeState](nearlink-ssap.md#connectionchangestate)> | 是 | 表示连接状态变化事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.on('connectionStateChange', onConnectionStateChange);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### off( 'connectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void

取消订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionChangeState](nearlink-ssap.md#connectionchangestate)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.off('connectionStateChange', onConnectionStateChange);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### on( 'propertyRead')

PhonePC/2in1TabletTVWearable

on(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void

订阅客户端的读请求事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyRead"字符串，表示读请求事件。 |
| callback | Callback<[PropertyReadRequest](nearlink-ssap.md#propertyreadrequest)> | 是 | 表示读请求事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.on('propertyRead', onPropertyReadRequest);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### off( 'propertyRead')

PhonePC/2in1TabletTVWearable

off(type: 'propertyRead', callback?: Callback<PropertyReadRequest>): void

取消订阅客户端的读请求事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyRead"字符串，表示读请求事件。 |
| callback | Callback<[PropertyReadRequest](nearlink-ssap.md#propertyreadrequest)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.off('propertyRead', onPropertyReadRequest);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### on( 'propertyWrite')

PhonePC/2in1TabletTVWearable

on(type: 'propertyWrite', callback: Callback<PropertyWriteRequest>): void

订阅客户端的写请求事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyWrite"字符串，表示写请求事件。 |
| callback | Callback<[PropertyWriteRequest](nearlink-ssap.md#propertywriterequest)> | 是 | 表示写请求事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.on('propertyWrite', onPropertyWriteRequest);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### off( 'propertyWrite')

PhonePC/2in1TabletTVWearable

off(type: 'propertyWrite', callback?: Callback<PropertyWriteRequest>): void

取消订阅客户端的写请求事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"propertyWrite"字符串，表示写请求事件。 |
| callback | Callback<[PropertyWriteRequest](nearlink-ssap.md#propertywriterequest)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
5. console.info('data:'+ JSON.stringify(data));
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.off('propertyWrite', onPropertyWriteRequest);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### on( 'mtuChange')

PhonePC/2in1TabletTVWearable

on(type: 'mtuChange', callback: Callback<number>): void

订阅MTU（Maximum Transmission Unit）变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"mtuChange"字符串，表示MTU变化事件。 |
| callback | Callback<number> | 是 | 表示MTU变化事件回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onMtuChange:(data: number) => void = (data: number) => {
5. console.info('data:'+ data);
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.on('mtuChange', onMtuChange);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### off( 'mtuChange')

PhonePC/2in1TabletTVWearable

off(type: 'mtuChange', callback?: Callback<number>): void

取消订阅MTU变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"mtuChange"字符串，表示MTU变化事件。 |
| callback | Callback<number> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { ssap } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onMtuChange:(data: number) => void = (data: number) => {
5. console.info('data:'+ data);
6. }
7. let server: ssap.Server;
8. try {
9. server = ssap.createServer();
10. server.off('mtuChange', onMtuChange);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

## Service

PhonePC/2in1TabletTVWearable

表示星闪服务。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| properties | Array<[Property](nearlink-ssap.md#property)> | 否 | 否 | 表示服务的Property列表。 |

## Property

PhonePC/2in1TabletTVWearable

表示服务的Property。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示Property的数据值。 |
| descriptors | Array<[PropertyDescriptor](nearlink-ssap.md#propertydescriptor)> | 否 | 是 | 表示当前Property的描述符列表。若未配置则默认不携带该字段。 |
| operation | number | 否 | 是 | 表示Property支持的操作方式，默认值为0，即不支持操作。如要使属性支持相应的操作，需要对该字段赋值，例如赋值为：READABLE|WRITE\_NO\_RESPONSE。取值范围[0, 15]，各比特位对应的操作方式详见[Operation](nearlink-ssap.md#operation)。 |

## PropertyDescriptor

PhonePC/2in1TabletTVWearable

表示Property的描述符。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示描述符的数据值。 |
| descriptorType | [PropertyDescriptorType](nearlink-ssap.md#propertydescriptortype) | 否 | 否 | 表示Property的描述符类型。 |
| isWriteable | boolean | 否 | 是 | 表示描述符是否是可写的。true：可写，false：不可写。默认值为true。 |

## PropertyReadRequest

PhonePC/2in1TabletTVWearable

表示客户端的Property读请求参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| requestId | number | 否 | 否 | 表示请求ID。取值范围[0, 65535]。 |

## PropertyWriteRequest

PhonePC/2in1TabletTVWearable

表示客户端的Property写请求参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示客户端写入的值。 |
| requestId | number | 否 | 否 | 表示客户端的写请求ID，服务端回复响应时需携带该ID。取值范围[0, 65535]。 |
| writeType | [PropertyWriteType](nearlink-ssap.md#propertywritetype) | 否 | 否 | 表示客户端写Property类型。 |

## ServerResponse

PhonePC/2in1TabletTVWearable

表示回复客户端请求的响应。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| requestId | number | 否 | 否 | 表示请求ID。取值范围[0, 65535]。 |
| value | ArrayBuffer | 否 | 否 | 表示回复的数据值。 |

## ConnectionChangeState

PhonePC/2in1TabletTVWearable

表示连接状态上报参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示远端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| state | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 表示和远端设备的连接状态。 |

## PropertyDescriptorType

PhonePC/2in1TabletTVWearable

表示Property的描述符类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROPERTY | 1 | 表示Property。 |
| CLIENT\_PROPERTY\_CONFIG | 2 | 表示客户端Property配置。 |
| SERVER\_PROPERTY\_CONFIG | 3 | 表示服务端Property配置。 |
| PROPERTY\_FORMAT | 4 | 表示Property格式。 |
| TYPE\_VENDOR | 255 | 表示厂商自定义字段。 |

## Operation

PhonePC/2in1TabletTVWearable

表示Property支持的操作类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READABLE | 0x01 | 表示可读。 |
| WRITE\_NO\_RESPONSE | 0x02 | 表示支持无响应的写请求。 |
| WRITE\_WITH\_RESPONSE | 0x04 | 表示支持有响应的写请求。 |
| NOTIFY | 0x08 | 表示支持通知。 |

## PropertyWriteType

PhonePC/2in1TabletTVWearable

表示Property支持的写类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WRITE | 1 | 表示写请求并等待服务端响应回复。 |
| WRITE\_NO\_RESPONSE | 2 | 表示写请求，无需服务端响应回复。 |
