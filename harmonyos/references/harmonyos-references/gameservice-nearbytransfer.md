---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-nearbytransfer
title: gameNearbyTransfer(游戏近场快传)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b1b95eef836e2f783951249ce5086240ded6b5fbd38a3e61097f7133db28e4cb
---

本模块提供接入Game Service Kit的游戏近场快传能力。

**起始版本：** 5.1.0(18)

## 导入模块

PhonePC/2in1Tablet

```
1. import { gameNearbyTransfer } from '@kit.GameServiceKit';
```

## CreateParameters

PhonePC/2in1Tablet

创建参数类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 否 | 模块名。字符长度范围：[1, 1024]。 |
| abilityName | string | 否 | 否 | Ability名称。字符长度范围：[1, 1024]。 |
| needShowSystemUI | boolean | 否 | 是 | 是否展示系统UI。  - true：展示  - false：不展示  默认为false。 |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 否 | 是 | UIAbility上下文，当needShowSystemUI为true时，该参数必传。 |
| mode | [Mode](gameservice-nearbytransfer.md#mode) | 否 | 是 | 接入模式。默认为API模式。  **起始版本：** 6.0.0(20)。 |
| contentType | [ContentType](gameservice-nearbytransfer.md#contenttype) | 否 | 是 | 内容类型。  默认值为RESOURCE\_PACKAGE。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 6.1.0(23)。 |
| gameLinking | string | 否 | 是 | 游戏链接，即App Linking或Deep Linking，仅当contentType为“INSTALLATION\_PACKAGE”类型时生效。如果接收端已安装该游戏，则将通过gameLinking启动该游戏。使用方式请参见使用[App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)和[使用Deep Linking实现应用间跳转](../harmonyos-guides/deep-linking-startup.md)。  字符长度范围：[0, 2048]。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 6.1.0(23)。 |

## ConnectNotification

PhonePC/2in1Tablet

连接通知类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| connectState | [ConnectState](gameservice-nearbytransfer.md#connectstate) | 否 | 否 | 连接状态。 |
| message | string | 否 | 是 | 连接结果消息。 |
| remoteDeviceName | string | 否 | 是 | 远端设备名。 |

## BindParameters

PhonePC/2in1Tablet

绑定参数类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID。字符长度范围：[1, 128]。 |
| networkId | string | 否 | 否 | 设备网络ID。字符长度范围：[1, 128]。 |

## NearbyGameDevice

PhonePC/2in1Tablet

近场快传设备类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceName | string | 否 | 否 | 设备名。 |
| deviceId | string | 否 | 否 | 设备ID。 |
| networkId | string | 否 | 否 | 设备网络ID。 |

## DiscoveryResult

PhonePC/2in1Tablet

发现结果类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nearbyGameDevices | Array<[NearbyGameDevice](gameservice-nearbytransfer.md#nearbygamedevice)> | 否 | 否 | 发现的设备列表。 |

## CreateResult

PhonePC/2in1Tablet

创建结果类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| localDeviceName | string | 否 | 否 | 本端设备名。 |
| linkingForInstallation | string | 否 | 是 | 安装包的传输链接，仅当传输类型为安装包传输时返回。字符长度范围：[0, 2048]。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 6.1.0(23)。 |

## TransferNotification

PhonePC/2in1Tablet

传输通知类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| transferState | [TransferState](gameservice-nearbytransfer.md#transferstate) | 否 | 否 | 传输状态。 |
| transferInfo | [TransferInfo](gameservice-nearbytransfer.md#transferinfo) | 否 | 否 | 传输信息。 |
| fileStoragePath | string | 否 | 是 | 接收端已接收文件的存储目录沙箱路径，详情请参见[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)，传输完成后返回。 |

## FileInfo

PhonePC/2in1Tablet

文件信息类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 文件路径，使用沙箱路径，详情请参见[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。字符长度范围：[1, 2048]。 |
| hash | string | 否 | 是 | 文件hash值。字符长度范围：[0, 256]。 |

## PackageInfo

PhonePC/2in1Tablet

包信息类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 包名。字符长度范围：[0, 2048]。 |
| version | string | 否 | 是 | 版本号，格式自定义。字符长度范围：[0, 256]。 |
| files | Array<[FileInfo](gameservice-nearbytransfer.md#fileinfo)> | 否 | 是 | 文件列表。最多10000条。 |
| extraData | string | 否 | 是 | 扩展数据。字符长度范围：[0, 2048]。 |

## PackageFile

PhonePC/2in1Tablet

传输包文件类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| srcPath | string | 否 | 否 | 源文件路径，为发送端应用沙箱路径，详情请参见[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。字符长度范围：[1, 2048]。完整路径。 |
| destPath | string | 否 | 否 | 目标文件路径，为接收端应用沙箱路径，详情请参见[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。字符长度范围：[1, 2048]。相对路径，完整路径为[fileStoragePath](gameservice-nearbytransfer.md#transfernotification)+destPath。 |

## PackageData

PhonePC/2in1Tablet

传输包数据类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 包名。字符长度范围：[0, 2048]。 |
| version | string | 否 | 是 | 版本号。字符长度范围：[0, 256]。 |
| files | Array<[PackageFile](gameservice-nearbytransfer.md#packagefile)> | 否 | 否 | 传输文件列表。  对于6.0.2(22)之前的版本，传输文件列表中的文件数量最多为10000条。  对于6.0.2(22)版本，文件数量最多为200000条。  对于6.0.2(22)之后的版本，文件数量最多为500000条。 |

## ReturnResult

PhonePC/2in1Tablet

返回结果类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 返回码。具体取值请参考[NearbyTransferErrorCode](gameservice-nearbytransfer.md#nearbytransfererrorcode)。 |
| message | string | 否 | 是 | 返回消息。 |

## PackageInfoResult

PhonePC/2in1Tablet

包信息对比结果类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| packageInfoResultCode | [PackageInfoResultCode](gameservice-nearbytransfer.md#packageinforesultcode) | 否 | 否 | 对比结果码值。 |
| message | string | 否 | 是 | 对比结果信息。 |

## TransferInfo

PhonePC/2in1Tablet

传输信息类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| expectedTime | number | 否 | 否 | 传输剩余时间，单位：s。 |
| transferredPackageSize | number | 否 | 否 | 已传输包大小，单位：Byte。 |
| totalPackageSize | number | 否 | 否 | 整包总大小，单位：Byte。 |
| rate | number | 否 | 否 | 传输速率，单位：Byte/s。 |

## RemoteInstallationInfo

PhonePC/2in1Tablet

安装信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.1.0(23)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| installed | boolean | 否 | 否 | 安装包在接收端是否已安装。  - true：已安装。  - false：未安装。  默认值为false。 |

## Mode

PhonePC/2in1Tablet

接入模式枚举对象。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| API | 1 | API模式，即使用游戏近场快传服务接口接入。 |
| KNOCK | 2 | 碰一碰模式。详情请参考[碰一碰分享](../harmonyos-guides/knock-share-between-phones-overview.md)。 |
| GESTURES | 3 | 隔空传送模式。详情请参考[隔空传送](../harmonyos-guides/gestures-share-overview.md)。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 6.1.0(23)。 |

## ConnectState

PhonePC/2in1Tablet

连接状态枚举对象。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| CONNECTED | 0 | 连接成功。 |
| DISCONNECTED | 1 | 连接断开。 |

## TransferState

PhonePC/2in1Tablet

传输状态枚举对象。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SEND\_START | 0 | 准备发送。 |
| SEND\_PROCESS | 1 | 发送进行。 |
| SEND\_FINISH | 2 | 发送完成。 |
| SEND\_ERROR | 3 | 发送错误。 |
| RECEIVE\_START | 4 | 接收开始。 |
| RECEIVE\_PROCESS | 5 | 接收进行。 |
| RECEIVE\_FINISH | 6 | 接收完成。 |
| RECEIVE\_ERROR | 7 | 接收错误。 |

## PackageInfoResultCode

PhonePC/2in1Tablet

包信息对比结果码值枚举对象。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ERROR | -1 | 对比错误。 |
| PACKAGE\_AVAILABLE\_COMPARED | 0 | 对比后可用。 |
| PACKAGE\_UNAVAILABLE\_COMPARED | 1 | 对比后不可用。 |

## ContentType

PhonePC/2in1Tablet

传输的内容类型枚举对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.1.0(23)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| RESOURCE\_PACKAGE | 1 | 资源包，用于在对方已安装游戏的情况下传输游戏内资源（例如游戏地图等）。 |
| INSTALLATION\_PACKAGE | 2 | 安装包，用于在对方未安装游戏的情况下传输游戏安装包。 |

## NearbyTransferErrorCode

PhonePC/2in1Tablet

错误码类。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| **名称** | 值 | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | 1018300001 | 内部通用错误。 |
| AUTH\_FAILED | 1018300002 | 鉴权失败。 |
| INVALID\_REQUEST | 1018300003 | 请求不合法。 |
| NO\_SERVICE\_AVAILABLE | 1018300004 | 服务不可用。 |
| WLAN\_BLUETOOTH\_MUST\_BE\_ON | 1018300005 | WLAN和蓝牙必须同时开启。 |
| PUBLISH\_FAILED | 1018300006 | 发布失败。 |
| DISCOVERY\_FAILED | 1018300007 | 发现失败。 |
| INVALID\_PARAMETER | 1018300008 | 非法参数。  **起始版本：** 6.0.0(20) |

## gameNearbyTransfer.on('connectNotify')

PhonePC/2in1Tablet

on(type: 'connectNotify', callback: Callback<ConnectNotification>): void

订阅连接通知事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'connectNotify'，建链操作完成后触发该事件。 |
| callback | Callback<[ConnectNotification](gameservice-nearbytransfer.md#connectnotification)> | 是 | 回调函数，返回连接通知对象。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 订阅连接通知事件
7. gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
8. } catch (error) {
9. // 订阅连接通知失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to subscribe connectNotify. Code: ${err.code}, message: ${err.message}`);
12. }

14. function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
15. // 获取连接状态
16. hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
17. }
```

## gameNearbyTransfer.off('connectNotify')

PhonePC/2in1Tablet

off(type: 'connectNotify', callback?: Callback<ConnectNotification>): void

取消订阅连接通知事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'connectNotify'，建链操作完成后触发该事件。 |
| callback | Callback<[ConnectNotification](gameservice-nearbytransfer.md#connectnotification)> | 否 | 回调函数，返回连接通知对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'connectNotify'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 取消订阅连接通知事件
7. gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
8. } catch (error) {
9. // 取消订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to unsubscribe connectNotify. Code: ${err.code}, message: ${err.message}`);
12. }

14. function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
15. // 获取连接状态
16. hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
17. }
```

## gameNearbyTransfer.on('discovery')

PhonePC/2in1Tablet

on(type: 'discovery', callback: Callback<DiscoveryResult>): void

订阅发现结果事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'discovery'，发现设备操作完成后触发该事件。 |
| callback | Callback<[DiscoveryResult](gameservice-nearbytransfer.md#discoveryresult)> | 是 | 回调函数，返回发现结果对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 订阅发现结果
7. gameNearbyTransfer.on('discovery', discoveryCallBack);
8. } catch (error) {
9. // 订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to subscribe discovery. Code: ${err.code}, message: ${err.message}`);
12. }

14. function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
15. // 获取到发现的设备 展示设备列表
16. callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
17. });
18. }
```

## gameNearbyTransfer.off('discovery')

PhonePC/2in1Tablet

off(type: 'discovery', callback?: Callback<DiscoveryResult>): void

取消订阅发现结果事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'discovery'，发现设备操作完成后触发该事件。 |
| callback | Callback<[DiscoveryResult](gameservice-nearbytransfer.md#discoveryresult)> | 否 | 回调函数，返回发现结果对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'discovery'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 取消订阅
7. gameNearbyTransfer.off('discovery', discoveryCallBack);
8. } catch (error) {
9. // 取消订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to unsubscribe discovery. Code: ${err.code}, message: ${err.message}`);
12. }

14. function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
15. // 获取到发现的设备 展示设备列表
16. callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
17. });
18. }
```

## gameNearbyTransfer.on('receivePackageInfo')

PhonePC/2in1Tablet

on(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void

订阅收到包信息事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'receivePackageInfo'，收到接收方发送的自身文件信息后触发该事件。 |
| callback | Callback<[PackageInfo](gameservice-nearbytransfer.md#packageinfo)> | 是 | 回调函数，返回包信息对象。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 订阅包信息事件
7. gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
8. } catch (error) {
9. // 订阅包信息事件失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to subscribe receivePackageInfo. Code: ${err.code}, message: ${err.message}`);
12. }
13. function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
14. // 获取对端包信息&版本号
15. hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
16. }
```

## gameNearbyTransfer.off('receivePackageInfo')

PhonePC/2in1Tablet

off(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void

取消订阅收到包信息事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'receivePackageInfo'，收到接收方发送的自身文件信息后触发该事件。 |
| callback | Callback<[PackageInfo](gameservice-nearbytransfer.md#packageinfo)> | 否 | 回调函数，返回包信息对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'receivePackageInfo'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 取消订阅包信息事件
7. gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
8. } catch (error) {
9. // 取消订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to unsubscribe receivePackageInfo. Code: ${err.code}, message: ${err.message}`);
12. }

14. function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
15. // 获取对端包信息&版本号
16. hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
17. }
```

## gameNearbyTransfer.on('transferNotify')

PhonePC/2in1Tablet

on(type: 'transferNotify', callback: Callback<TransferNotification>): void

订阅传输通知事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'transferNotify'，文件传输过程中触发该事件。 |
| callback | Callback<[TransferNotification](gameservice-nearbytransfer.md#transfernotification)> | 是 | 回调函数，返回传输通知对象。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 订阅传输通知事件
7. gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
8. } catch (error) {
9. // 订阅传输通知失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to subscribe transferNotify. Code: ${err.code}, message: ${err.message}`);
12. }

14. function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
15. // 获取传输状态
16. hilog.info(0x0000, 'nearby', `transferNotify. transferState: ${callback.transferState}`);
17. }
```

## gameNearbyTransfer.off('transferNotify')

PhonePC/2in1Tablet

off(type: 'transferNotify', callback?: Callback<TransferNotification>): void

取消订阅传输通知事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'transferNotify'，文件传输过程中触发该事件。 |
| callback | Callback<[TransferNotification](gameservice-nearbytransfer.md#transfernotification)> | 否 | 回调函数，返回传输通知对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'transferNotify'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 取消订阅传输通知事件
7. gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
8. } catch (error) {
9. // 取消订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to unsubscribe transferNotify. Code: ${err.code}, message: ${err.message}`);
12. }

14. function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
15. // 获取传输状态
16. hilog.info(0x0000, 'nearby', `transferNotify. transferState: ${callback.transferState}`);
17. }
```

## gameNearbyTransfer.on('error')

PhonePC/2in1Tablet

on(type: 'error', callback: Callback<ReturnResult>): void

订阅错误事件。使用callback回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'error'，内部错误时触发该事件。 |
| callback | Callback<[ReturnResult](gameservice-nearbytransfer.md#returnresult)> | 是 | 回调函数，返回结果信息对象。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 订阅异常事件通知
7. gameNearbyTransfer.on('error', errorCallBack);
8. } catch (error) {
9. // 订阅异常事件通知失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to subscribe error. Code: ${err.code}, message: ${err.message}`);
12. }

14. function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
15. hilog.warn(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
16. }
```

## gameNearbyTransfer.off('error')

PhonePC/2in1Tablet

off(type: 'error', callback?: Callback<ReturnResult>): void

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'error'。 |
| callback | Callback<[ReturnResult](gameservice-nearbytransfer.md#returnresult)> | 否 | 回调函数，返回结果信息对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'error'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // 取消订阅异常事件通知
7. gameNearbyTransfer.off('error', errorCallBack);
8. } catch (error) {
9. // 取消订阅失败
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `Failed to unsubscribe errorCallBack. Code: ${err.code}, message: ${err.message}`);
12. }

14. function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
15. hilog.warn(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
16. }
```

## gameNearbyTransfer.onRemoteInstallationInfoNotify

PhonePC/2in1Tablet

onRemoteInstallationInfoNotify(callback: Callback<RemoteInstallationInfo>): void

订阅近场快传远程安装包信息通知事件。使用callback回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | Callback<[RemoteInstallationInfo](gameservice-nearbytransfer.md#remoteinstallationinfo)> | 是 | 回调函数，返回远程安装包结果信息对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. gameNearbyTransfer.onRemoteInstallationInfoNotify(remoteCallBack);
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'nearby', `Failed to subscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
10. }

12. function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
13. // 对端是否已安装
14. hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
15. }
```

## gameNearbyTransfer.offRemoteInstallationInfoNotify

PhonePC/2in1Tablet

offRemoteInstallationInfoNotify(callback?: Callback<RemoteInstallationInfo>): void

取消订阅近场快传远程安装包信息通知事件。使用callback回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | Callback<[RemoteInstallationInfo](gameservice-nearbytransfer.md#remoteinstallationinfo)> | 否 | 回调函数，返回远程安装包结果信息对象。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'offRemoteInstallationInfoNotify'事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. gameNearbyTransfer.offRemoteInstallationInfoNotify(remoteCallBack);
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'nearby', `Failed to unsubscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
10. }

12. function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
13. // 对端是否已安装
14. hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
15. }
```

## gameNearbyTransfer.create

PhonePC/2in1Tablet

create(createParameters: CreateParameters): Promise<CreateResult>

创建游戏近场快传服务。使用Promise异步回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| createParameters | [CreateParameters](gameservice-nearbytransfer.md#createparameters) | 是 | 创建参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CreateResult](gameservice-nearbytransfer.md#createresult)> | Promise对象。返回创建结果的Promise对象。 |

**错误码：**

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300002 | Authentication failed. |

**资源包传输示例**：

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { gameNearbyTransfer } from "@kit.GameServiceKit";
4. import { BusinessError } from "@kit.BasicServicesKit";

6. @Component
7. struct Create {
8. create() {
9. // 创建资源包传输
10. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
11. let initParam: gameNearbyTransfer.CreateParameters = {
12. abilityName: context.abilityInfo.name,
13. context: context,
14. moduleName: context.abilityInfo.moduleName,
15. needShowSystemUI: false // 是否显示系统UI
16. };

18. try {
19. gameNearbyTransfer.create(initParam).then((createResult) => {
20. hilog.info(0x0000, 'nearby', `create success localDeviceName ${createResult.localDeviceName}`);
21. }).catch((err: BusinessError) => {
22. hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
23. })
24. } catch (error) {
25. let err = error as BusinessError;
26. hilog.error(0x0000, 'nearby', `create exception. Code: ${err.code}, message: ${err.message}`);
27. }
28. }

30. build() {
31. }
32. }
```

**安装包传输示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { gameNearbyTransfer } from "@kit.GameServiceKit";
4. import { BusinessError } from "@kit.BasicServicesKit";

6. @Component
7. struct Create {
8. async create() {
9. // 创建安装包传输
10. let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
11. let initParam: gameNearbyTransfer.CreateParameters = {
12. abilityName: uiAbilityContext.abilityInfo.name,
13. moduleName: uiAbilityContext.abilityInfo.moduleName,
14. contentType: gameNearbyTransfer.ContentType.INSTALLATION_PACKAGE, // 指定传输类型为安装包
15. gameLinking: "nearbytransfer://com.huawei.nearbytransferdemo?type=nearbyTransfer" // 安装包场景需要传入游戏Deeplink
16. };

18. try {
19. let createResult = await gameNearbyTransfer.create(initParam);
20. hilog.info(0x0000, '[nearby]', `create success linking: ${createResult.linkingForInstallation}`);
21. } catch (error) {
22. let err = error as BusinessError;
23. hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
24. }
25. }

27. build() {
28. }
29. }
```

## gameNearbyTransfer.publishNearbyGame

PhonePC/2in1Tablet

publishNearbyGame(): Promise<void>

发布近场快传服务。使用Promise异步回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300006 | Publishing failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. try {
6. gameNearbyTransfer.publishNearbyGame().then(() => {
7. hilog.info(0x0000, 'nearby', `publishNearbyGame success`);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'nearby', `publishNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
10. })
11. } catch (error) {
12. let err = error as BusinessError;
13. hilog.error(0x0000, 'nearby', `publishNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
14. }
```

## gameNearbyTransfer.discoveryNearbyGame

PhonePC/2in1Tablet

discoveryNearbyGame(): Promise<void>

发送端执行发现附近设备。使用Promise异步回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300007 | Discovery failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. try {
6. gameNearbyTransfer.discoveryNearbyGame().then(() => {
7. hilog.info(0x0000, 'nearby', `discoveryNearbyGame success.`);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'nearby', `discoveryNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
10. })
11. } catch (error) {
12. let err = error as BusinessError;
13. hilog.error(0x0000, 'nearby', `discoveryNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
14. }
```

## gameNearbyTransfer.bindNearbyGame

PhonePC/2in1Tablet

bindNearbyGame(bindParameters: BindParameters): Promise<void>

发送端绑定指定近场快传服务。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| bindParameters | [BindParameters](gameservice-nearbytransfer.md#bindparameters) | 是 | 绑定参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300008 | Invalid parameter. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. let bindInfo: gameNearbyTransfer.BindParameters = {
6. deviceId: 'deviceId',
7. networkId: 'networkId'
8. };
9. try {
10. gameNearbyTransfer.bindNearbyGame(bindInfo).then(() => {
11. hilog.info(0x0000, 'nearby', `bindNearbyGame success`);
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'nearby', `bindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
14. })
15. } catch (error) {
16. let err = error as BusinessError;
17. hilog.error(0x0000, 'nearby', `bindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
18. }
```

## gameNearbyTransfer.autoBindNearbyGame

PhonePC/2in1Tablet

autoBindNearbyGame(): Promise<void>

自动绑定近场快传服务。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300007 | Discovery failed. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. try {
6. // 自动绑定近场快传服务
7. gameNearbyTransfer.autoBindNearbyGame().then(() => {
8. hilog.info(0x0000, 'nearby', `autoBindNearbyGame success`);
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'nearby', `autoBindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
11. })
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'nearby', `autoBindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
15. }
```

## gameNearbyTransfer.acceptCollaboration

PhonePC/2in1Tablet

acceptCollaboration(acceptParameters: Record<string, object>): Promise<void>

接受协同。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| acceptParameters | Record<string, object> | 是 | 设置接受参数。Record数量范围：[1, 1024]。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

**示例**：

```
1. import { gameNearbyTransfer } from "@kit.GameServiceKit";
2. import { AbilityConstant, UIAbility } from "@kit.AbilityKit";
3. import { hilog } from "@kit.PerformanceAnalysisKit";

5. export default class EntryAbility extends UIAbility {
6. // 协同回调
7. onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
8. try {
9. // 接受协同
10. gameNearbyTransfer.acceptCollaboration(wantParam).catch((err: BusinessError) => {
11. hilog.error(0x0000, 'nearby', `acceptCollaboration failed. Code: ${err.code}, message: ${err.message}`);
12. })
13. } catch (error) {
14. let err = error as BusinessError;
15. hilog.error(0x0000, 'nearby', `acceptCollaboration exception. Code: ${err.code}, message: ${err.message}`);
16. }
17. return AbilityConstant.CollaborateResult.ACCEPT;
18. }
19. }
```

## gameNearbyTransfer.sendPackageInfo

PhonePC/2in1Tablet

sendPackageInfo(packageInfo: PackageInfo): Promise<void>

接收端发送自身文件信息。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| packageInfo | [PackageInfo](gameservice-nearbytransfer.md#packageinfo) | 是 | 包信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. let packageInfo: gameNearbyTransfer.PackageInfo = {
6. name: 'xxxx',
7. files: [],
8. version: '1.1.0', // 应用版本
9. extraData: 'extraData' // 自定义信息
10. };
11. let fileInfo: gameNearbyTransfer.FileInfo = {
12. path: "/xxx/xxxx/files/data.zip",
13. hash: 'fileHash' // 可选
14. };
15. packageInfo.files?.push(fileInfo);
16. try {
17. gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
18. hilog.info(0x0000, 'nearby', `sendPackageInfo success`);
19. }).catch((err: BusinessError) => {
20. hilog.error(0x0000, 'nearby', `sendPackageInfo failed. Code: ${err.code}, message: ${err.message}`);
21. })
22. } catch (error) {
23. let err = error as BusinessError;
24. hilog.error(0x0000, 'nearby', `sendPackageInfo exception. Code: ${err.code}, message: ${err.message}`);
25. }
```

## gameNearbyTransfer.replyPackageInfoResult

PhonePC/2in1Tablet

replyPackageInfoResult(packageInfoResult: PackageInfoResult): Promise<void>

发送端向近场快传服务上报包信息对比结果。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| packageInfoResult | [PackageInfoResult](gameservice-nearbytransfer.md#packageinforesult) | 是 | 包信息对比结果。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
6. packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE_AVAILABLE_COMPARED
7. };
8. try {
9. // 上报包信息对比结果
10. gameNearbyTransfer.replyPackageInfoResult(packageInfoResult).then(() => {
11. hilog.info(0x0000, 'nearby', `replyPackageInfoResult success`);
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'nearby', `replyPackageInfoResult failed. Code: ${err.code}, message: ${err.message}`);
14. })
15. } catch (error) {
16. let err = error as BusinessError;
17. hilog.error(0x0000, 'nearby', `replyPackageInfoResult exception. Code: ${err.code}, message: ${err.message}`);
18. }
```

## gameNearbyTransfer.transferPackageData

PhonePC/2in1Tablet

transferPackageData(packageData: PackageData): Promise<void>

开始传输包数据。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| packageData | [PackageData](gameservice-nearbytransfer.md#packagedata) | 是 | 待传输的包数据信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. let packageData: gameNearbyTransfer.PackageData = {
6. name: 'xxx',
7. version: '1.0.1',
8. files: []
9. };
10. packageData.files.push({ srcPath: "/xxx/xxxx/a.db", destPath: "xxxx/b.db" });
11. try {
12. // 开始传输包数据
13. gameNearbyTransfer.transferPackageData(packageData).then(() => {
14. hilog.info(0x0000, 'nearby', `transferPackageData success`);
15. }).catch((err: BusinessError) => {
16. hilog.error(0x0000, 'nearby', `transferPackageData failed. Code: ${err.code}, message: ${err.message}`);
17. })
18. } catch (error) {
19. let err = error as BusinessError;
20. hilog.error(0x0000, 'nearby', `transferPackageData exception. Code: ${err.code}, message: ${err.message}`);
21. }
```

## gameNearbyTransfer.destroy

PhonePC/2in1Tablet

destroy(): Promise<void>

不再使用时，销毁游戏近场快传服务。使用Promise异步回调。

**系统能力：** SystemCapability.GameService.GameNearby

**起始版本：** 5.1.0(18)

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { gameNearbyTransfer } from "@kit.GameServiceKit";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. // 销毁服务
6. try {
7. gameNearbyTransfer.destroy().then(() => {
8. hilog.info(0x0000, 'nearby', `destroy success`);
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
11. })
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
15. }
```
