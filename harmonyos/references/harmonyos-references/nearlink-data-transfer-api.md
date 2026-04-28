---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-data-transfer-api
title: dataTransfer（星闪数传能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > dataTransfer（星闪数传能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2729a04cdfbeb54038013bcae5b616f5306939b8e63cf5d333d8000bb0e25fd
---

本模块提供了星闪数据传输的功能。

**起始版本：** 5.1.0(18)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { dataTransfer } from '@kit.NearLinkKit';
```

## ConnectionState

PhonePC/2in1TabletTVWearable

type ConnectionState = [constant.ConnectionState](nearlink-constant.md#connectionstate)

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## createPort

PhonePC/2in1TabletTVWearable

createPort(uuid: string): void

注册端口通道。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uuid | string | 是 | 可填写16字节星闪服务UUID，或填写2字节支持数传的星闪标准服务UUID。UUID格式参考“[星闪标准服务标识](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)”。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700020 | The UUID is already registered |
| 1009700021 | Port is exceeds the upper limit |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID
6. dataTransfer.createPort(uuid);
7. console.info('create port success');
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## destroyPort

PhonePC/2in1TabletTVWearable

destroyPort(uuid: string): void

销毁端口通道。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uuid | string | 是 | 可填写16字节星闪服务UUID，或填写2字节支持数传的星闪标准服务UUID。UUID格式参考“[星闪标准服务](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)”。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700022 | The UUID is not registered |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID
6. dataTransfer.destroyPort(uuid);
7. console.info('destroy port success');
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connect

PhonePC/2in1TabletTVWearable

connect(params: ConnectionParams): Promise<void>

连接远端设备，建立端口通道。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionParams](nearlink-data-transfer-api.md#connectionparams) | 是 | 指明端口的连接参数。 |

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
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 构造端口通道建立的参数
6. let connectionParams:dataTransfer.ConnectionParams = {
7. address: '01:02:03:04:05:06', // 星闪远端设备地址
8. uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
9. mtu: 1024, // 期望发送数据包的字节大小,可选参数
10. };
11. dataTransfer.connect(connectionParams).then(()=>{
12. console.info('connect success');
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

## disconnect

PhonePC/2in1TabletTVWearable

disconnect(params: ConnectionParams): Promise<void>

断连远端设备，销毁端口通道。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionParams](nearlink-data-transfer-api.md#connectionparams) | 是 | 指明端口的连接参数。 |

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
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 构造端口通道建立的参数
6. let connectionParams:dataTransfer.ConnectionParams = {
7. address: '01:02:03:04:05:06', // 星闪远端设备地址
8. uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
9. mtu: 1024, // 期望发送数据包的字节大小，可选参数
10. };
11. dataTransfer.disconnect(connectionParams).then(()=>{
12. console.info('disconnect success');
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

## on('connectionStateChanged')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void

订阅端口通道连接状态变更事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChanged"字符串，表示端口通道连接状态变更事件。 |
| callback | Callback<[ConnectionResult](nearlink-data-transfer-api.md#connectionresult)> | 是 | 表示端口通道连接状态变化回调函数的入参，回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<dataTransfer.ConnectionResult> = (data: dataTransfer.ConnectionResult) => {
6. console.info('data: ' + JSON.stringify(data));
7. };
8. try {
9. dataTransfer.on('connectionStateChanged', callback);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## off('connectionStateChanged')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChanged', callback?: Callback<ConnectionResult>): void

取消订阅端口通道连接状态变更事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChanged"字符串，表示端口通道连接状态变更事件。 |
| callback | Callback<[ConnectionResult](nearlink-data-transfer-api.md#connectionresult)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. dataTransfer.off('connectionStateChanged');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## getConnectionState

PhonePC/2in1TabletTVWearable

getConnectionState(params: ConnectionStateParams): ConnectionState

获取与远端设备之间的端口通道连接状态。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionStateParams](nearlink-data-transfer-api.md#connectionstateparams) | 是 | 指明端口的连接参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的星闪端口通道连接状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported |
| 1009700003 | NearLink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let connectionStateParams:dataTransfer.ConnectionStateParams = {
6. address: '01:02:03:04:05:06', // 扫描获取到的远端设备地址
7. uuid: 'FFFFFFFF-FC70-11EA-B720-000078951234' // 星闪服务UUID示例
8. };
9. let state:dataTransfer.ConnectionState = dataTransfer.getConnectionState (connectionStateParams);
10. console.info('state:' + JSON.stringify(state));
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

## writeData

PhonePC/2in1TabletTVWearable

writeData(params: DataParams): Promise<void>

通过设备地址和uuid向远端设备发数据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [DataParams](nearlink-data-transfer-api.md#dataparams) | 是 | 指明发送数据的参数，包含远端设备地址、服务UUID以及发送的数据包。 |

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
| 1009700023 | Write data congest |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 构造发送数据参数
6. let transferValueBuffer: Uint8Array = new Uint8Array(4);
7. transferValueBuffer[0] = 1;
8. transferValueBuffer[1] = 2;
9. transferValueBuffer[2] = 3;
10. transferValueBuffer[3] = 4;
11. let dataParams: dataTransfer.DataParams = {
12. address: '01:02:03:04:05:06', // 星闪远端设备地址
13. uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
14. data: transferValueBuffer.buffer, // 星闪设备间传输的数据
15. };
16. dataTransfer.writeData(dataParams).then(() => {
17. console.info('writeData success');
18. });
19. } catch (err) {
20. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
21. }
```

## on('readData')

PhonePC/2in1TabletTVWearable

on(type: 'readData', callback: Callback<DataParams>): void

订阅端口通道数据接收事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"readData"字符串，表示端口通道数据接收事件。 |
| callback | Callback<[DataParams](nearlink-data-transfer-api.md#dataparams)> | 是 | 表示端口通道数据接收回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<dataTransfer.DataParams> = (data: dataTransfer.DataParams) => {
6. console.info('data: ' + JSON.stringify(data));
7. };
8. try {
9. dataTransfer.on('readData', callback);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## off('readData')

PhonePC/2in1TabletTVWearable

off(type: 'readData', callback?: Callback<DataParams>): void

取消订阅端口通道数据接收事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"readData"字符串，表示端口接收数据事件。 |
| callback | Callback<[DataParams](nearlink-data-transfer-api.md#dataparams)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { dataTransfer} from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. dataTransfer.off('readData');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## ConnectionParams

PhonePC/2in1TabletTVWearable

发起端口连接的参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| mtu | number | 否 | 是 | 期望发送数据的包长，单位为byte。范围[0, 65535]，默认值为512。 |
| transferMode | [TransferMode](nearlink-data-transfer-api.md#transfermode) | 否 | 是 | 表示和远端设备的数据传输模式。默认值是BASIC。 |

## DataParams

PhonePC/2in1TabletTVWearable

端口数据发送和接收的参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| data | ArrayBuffer | 否 | 否 | 发送的数据包。 |

## ConnectionResult

PhonePC/2in1TabletTVWearable

与远端设备端口连接参数的协商结果

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| mtu | number | 否 | 否 | 协商后的发送和接收数据的包长，单位为byte，范围[0, 65535]。 |
| state | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 与远端设备的连接状态。 |

## ConnectionStateParams

PhonePC/2in1TabletTVWearable

获取端口通道连接状态所需参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |

## TransferMode

PhonePC/2in1TabletTVWearable

表示和远端设备的数据传输模式，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC | 0 | 表示基础模式，无数据重传机制。 |
| RELIABLE | 1 | 表示可靠模式，有数据重传机制。 |
