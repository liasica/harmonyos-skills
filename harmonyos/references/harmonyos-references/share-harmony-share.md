---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-harmony-share
title: harmonyShare（华为分享）
breadcrumb: API参考 > 应用服务 > Share Kit（分享服务） > ArkTS API > harmonyShare（华为分享）
category: harmonyos-references
scraped_at: 2026-04-29T14:09:20+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4b83aa7397a9c5f1993609e56398ec7decf6a86d01c0fba32f803219680ae678
---

本模块提供华为分享的事件注册。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { harmonyShare } from '@kit.ShareKit';
```

## SharableErrorCode

PhonePC/2in1Tablet

拒绝分享回调时，提供拒绝原因，用户可收到系统通知消息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.3(15)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_CONTENT\_ERROR | 1 | 用于无内容分享场景。 |
| NO\_INTERNET\_ERROR | 2 | 用于无网络场景。 |
| DOWNLOAD\_ERROR | 3 | 用于下载失败场景。 |

## ReceivableErrorCode

PhonePC/2in1Tablet

拒绝沙箱接收回调时，提供拒绝原因，用户可收到系统通知消息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_RECEIVABLE\_ERROR | 1 | 用于当前无法接收数据的场景。 |

## ShareResultCode

PhonePC/2in1Tablet

沙箱接收结果通知成功或失败原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHARE\_SUCCESS | 0 | 沙箱接收成功。 |
| SEND\_FAILED | 1 | 数据传输失败。 |
| CANCEL\_BY\_SENDER | 2 | 发送端取消发送。 |
| CANCEL\_BY\_RECEIVER | 3 | 接收端取消接收。 |

## SharableTarget

PhonePC/2in1Tablet

华为分享事件触发后回调参数，可通过此参数跨端分享。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

### share

PhonePC/2in1Tablet

share(data: systemShare.SharedData): Promise<void>

跨端分享，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [systemShare.SharedData](share-system-share.md#shareddata) | 是 | 分享数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

### reject

PhonePC/2in1Tablet

reject(error: SharableErrorCode): Promise<void>

当开发者收到回调时，由于某些原因无法继续分享时，可选择拒绝本次分享，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [SharableErrorCode](share-harmony-share.md#sharableerrorcode) | 是 | 拒绝本次分享的原因。通过系统弹窗提示用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

### updateShareData

PhonePC/2in1Tablet

updateShareData(data: UpdatedData): Promise<void>

在分享数据未发送前，开发者可通过此接口更新预览图，使用Promise异步回调。

仅支持碰一碰分享功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [UpdatedData](share-harmony-share.md#updateddata) | 是 | 需要更新的数据信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

### clarifyNonShare

PhonePC/2in1Tablet

clarifyNonShare(info: SharableErrorInfo): Promise<void>

当开发者收到回调时，可通过此接口告知用户当前界面无可分享内容，并给出恰当的提示引导用户。

仅支持碰一碰分享功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [SharableErrorInfo](share-harmony-share.md#sharableerrorinfo) | 是 | 提示信息，用于告知用户无法分享的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

## ReceivableTarget

PhonePC/2in1Tablet

沙箱接收事件触发后回调参数，可通过此参数进行沙箱接收。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

### receive

PhonePC/2in1Tablet

receive(receiveUri: string, callback: ReceiveCallback): Promise<void>

提供沙箱接收目录uri，接收的文件将保存至此目录下，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiveUri | string | 是 | 沙箱接收时，存放数据的目录（必须真实存在）。  **说明：** Share Kit会在传输开始前获取此目录的授权，在数据传输完成后自动撤销授权，建议使用已存在的空文件夹，保护信息安全。 |
| callback | [ReceiveCallback](share-harmony-share.md#receivecallback) | 是 | 沙箱接收的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

### reject

PhonePC/2in1Tablet

reject(error: ReceivableErrorCode): Promise<void>

当开发者收到回调时，由于某些原因无法继续接收分享内容时，可选择拒绝本次接收，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [ReceivableErrorCode](share-harmony-share.md#receivableerrorcode) | 是 | 拒绝本次沙箱接收的原因。通过系统弹窗提示用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

## UpdatedData

PhonePC/2in1Tablet

华为分享事件发送的数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| thumbnailUri | string | 否 | 是 | 预览图的uri。 |

## BaseCapabilityRegistry

PhonePC/2in1Tablet

华为分享事件注册基础配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowId | number | 否 | 否 | 窗口id。 |

## SendCapabilityRegistry

PhonePC/2in1Tablet

华为分享事件窗口注册配置项。继承[BaseCapabilityRegistry](share-harmony-share.md#basecapabilityregistry)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sendOnly | boolean | 否 | 是 | 设置是否仅支持发送数据。默认值：false，表示可同时接收分享数据。当双端设备均设置为true时，双向分享会被拦截。  说明：仅支持碰一碰分享功能。 |

## RecvCapability

PhonePC/2in1Tablet

设置沙箱接收支持的能力范围（可接收的文件类型及最大数量限制）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| utd | string | 否 | 否 | 统一数据类型，参考[@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](js-apis-data-uniformtypedescriptor.md)。 |
| maxSupportedCount | number | 否 | 否 | 可接收文件的最大数量限制，仅允许设置大于0的整数。 |

## RecvCapabilityRegistry

PhonePC/2in1Tablet

沙箱接收事件窗口注册配置项。继承[BaseCapabilityRegistry](share-harmony-share.md#basecapabilityregistry)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| capabilities | [RecvCapability](share-harmony-share.md#recvcapability)[] | 否 | 否 | 沙箱接收能力设置，用于设置可接收的数据类型和数量。 |

## TransferBaseResults

PhonePC/2in1Tablet

沙箱接收时，文件数据传输完成的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onResult | Callback<[ShareResultCode](share-harmony-share.md#shareresultcode)> | 否 | 是 | 传输完成的回调函数。用于通知传输结果。 |

## ReceiveCallback

PhonePC/2in1Tablet

沙箱接收传输完成后回调函数。可用此方法监听完成事件，并处理接收后的数据。继承[TransferBaseResults](share-harmony-share.md#transferbaseresults)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onDataReceived | Callback<[systemShare.SharedData](share-system-share.md#shareddata)> | 否 | 否 | 沙箱接收传输完成后回调函数。用于接收已保存至沙箱路径下的文件列表。 |

## SharableErrorInfo

PhonePC/2in1Tablet

提示信息，用于告知用户无法分享的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | 否 | 是 | 提示文案。 |

## on('knockShare')

PhonePC/2in1Tablet

on(event: 'knockShare', callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 事件回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';

4. // 注册设备轻贴'knockShare'监听事件
5. harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
6. // 构造分享数据
7. let shareData: systemShare.SharedData = new systemShare.SharedData({
8. utd: utd.UniformDataType.PLAIN_TEXT,
9. content: '这是一段文本内容'
10. });
11. // 发起分享
12. sharableTarget.share(shareData);
13. });
```

## off('knockShare')

PhonePC/2in1Tablet

off(event: 'knockShare', callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，取消设备轻贴的事件监听。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```
1. // 取消设备轻贴'knockShare'监听事件
2. harmonyShare.off('knockShare');
```

## on('knockShare')

PhonePC/2in1Tablet

on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 事件回调。 |

**示例：**

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';

4. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
5. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
6. }
7. // 注册设备轻贴'knockShare'监听事件
8. harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
9. // 构造分享数据
10. let shareData: systemShare.SharedData = new systemShare.SharedData({
11. utd: utd.UniformDataType.PLAIN_TEXT,
12. content: '这是一段文本内容'
13. });
14. // 发起分享
15. sharableTarget.share(shareData);
16. });
```

## off('knockShare')

PhonePC/2in1Tablet

off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，取消设备轻贴的事件监听。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```
1. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
2. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
3. }
4. // 取消设备轻贴'knockShare'监听事件
5. harmonyShare.off('knockShare', capabilityRegistry);
```

## on('gesturesShare')

PhonePC/2in1Tablet

on(event: 'gesturesShare', callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 事件回调。 |

**示例：**

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';

4. // 注册隔空传送'gesturesShare'监听事件
5. harmonyShare.on('gesturesShare', (sharableTarget: harmonyShare.SharableTarget) => {
6. // 构造分享数据
7. let shareData: systemShare.SharedData = new systemShare.SharedData({
8. utd: utd.UniformDataType.PLAIN_TEXT,
9. content: '这是一段文本内容'
10. });
11. // 发起分享
12. sharableTarget.share(shareData);
13. });
```

## off('gesturesShare')

PhonePC/2in1Tablet

off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，取消隔空传送的事件监听。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```
1. // 取消隔空传送'gesturesShare'监听事件
2. harmonyShare.off('gesturesShare');
```

## on('gesturesShare')

PhonePC/2in1Tablet

on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 事件回调。 |

**示例：**

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';

4. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
5. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
6. }
7. // 注册隔空传送'gesturesShare'监听事件
8. harmonyShare.on('gesturesShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
9. // 构造分享数据
10. let shareData: systemShare.SharedData = new systemShare.SharedData({
11. utd: utd.UniformDataType.PLAIN_TEXT,
12. content: '这是一段文本内容'
13. });
14. // 发起分享
15. sharableTarget.share(shareData);
16. });
```

## off('gesturesShare')

PhonePC/2in1Tablet

off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，取消隔空传送的事件监听。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```
1. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
2. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
3. }
4. // 取消隔空传送'gesturesShare'监听事件
5. harmonyShare.off('gesturesShare', capabilityRegistry);
```

## on('dataReceive')

PhonePC/2in1Tablet

on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void

注册沙箱接收事件监听。仅支持文件类型数据。文本（包含链接）类型的数据保持原有接收逻辑。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**设备行为差异：** 对于API version 22及之前的版本，该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。从API version 23开始，该接口在PC/2in1、Tablet中均可正常使用，在其他设备类型中无响应。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'dataReceive'，当手机设备轻贴PC/2in1、Tablet设备屏幕时，触发该事件。 |
| capability | [RecvCapabilityRegistry](share-harmony-share.md#recvcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[ReceivableTarget](share-harmony-share.md#receivabletarget)> | 是 | 事件回调。 |

**示例：**

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';
3. import { common } from '@kit.AbilityKit';

5. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
6. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
7. capabilities: [{
8. utd: utd.UniformDataType.IMAGE,
9. maxSupportedCount: 1
10. }]
11. }
12. // 注册沙箱接收'dataReceive'监听事件
13. harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
14. let uiContext: UIContext = this.getUIContext();
15. let context = uiContext.getHostContext() as common.UIAbilityContext;
16. receivableTarget.receive(context.filesDir, { // 此路径仅为示例 使用时请替换实际路径
17. onDataReceived: (sharedData: systemShare.SharedData) => {
18. let sharedRecords = sharedData.getRecords();
19. sharedRecords.forEach((record: systemShare.SharedRecord) => {
20. // 处理分享数据
21. });
22. },
23. onResult(resultCode: harmonyShare.ShareResultCode) {
24. if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
25. // To do things.
26. }
27. }
28. });
29. });
```

## off('dataReceive')

PhonePC/2in1Tablet

off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void

取消沙箱接收的事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**设备行为差异：** 对于API version 22及之前的版本，该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。从API version 23开始，该接口在PC/2in1、Tablet中均可正常使用，在其他设备类型中无响应。

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'dataReceive'，取消沙箱接收的事件监听。 |
| capability | [RecvCapabilityRegistry](share-harmony-share.md#recvcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[ReceivableTarget](share-harmony-share.md#receivabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```
1. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
2. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
3. capabilities: [{
4. utd: utd.UniformDataType.IMAGE,
5. maxSupportedCount: 1
6. }]
7. }
8. // 取消沙箱接收'dataReceive'监听事件
9. harmonyShare.off('dataReceive', capabilityRegistry);
```
