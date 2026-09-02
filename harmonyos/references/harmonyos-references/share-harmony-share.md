---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-harmony-share
title: harmonyShare（华为分享）
breadcrumb: API参考 > 应用服务 > Share Kit（分享服务） > ArkTS API > harmonyShare（华为分享）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:380f23363463f701194ab547ab0480042361b68ae637a00e4e6cb0bd9e9303a4
---

本模块提供华为分享的事件注册。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { harmonyShare } from '@kit.ShareKit';
```

## SharableErrorCode

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

拒绝沙箱接收回调时，提供拒绝原因，用户可收到系统通知消息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_RECEIVABLE\_ERROR | 1 | 用于当前无法接收数据的场景。 |

## ShareResultCode

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

华为分享事件触发后回调参数，可通过此参数跨端分享。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

### share

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

**示例：**

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 构造分享数据
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: '这是一段文本内容'
  });
  // 发起分享
  sharableTarget.share(shareData);
});
```

### reject

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

**示例：**

```typescript
import { harmonyShare } from '@kit.ShareKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 拒绝本次分享
  sharableTarget.reject(harmonyShare.SharableErrorCode.NO_CONTENT_ERROR);
});
```

### updateShareData

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

**示例：**

```typescript
import { harmonyShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  const uiContext: UIContext = this.getUIContext();
  const contextFaker: Context = uiContext.getHostContext() as Context;
  let updatedData: harmonyShare.UpdatedData = {
    thumbnailUri: fileUri.getUriFromPath(contextFaker.filesDir + '/exampleImage.jpg')
  };
  // 更新预览图
  sharableTarget.updateShareData(updatedData);
});
```

### clarifyNonShare

clarifyNonShare(info: SharableErrorInfo): Promise<void>

当开发者收到回调时，可通过此接口告知用户当前界面无可分享内容，并给出恰当的提示引导用户，使用Promise异步回调。

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

**示例：**

```typescript
import { harmonyShare } from '@kit.ShareKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 提示无内容分享
  sharableTarget.clarifyNonShare({ message: '请在支持碰一碰分享的界面再试' });
});
```

### getInfo

getInfo(): SharableTargetInfo

获取PC/2in1或Tablet设备作为发送端触发碰一碰事件时的相关信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SharableTargetInfo](share-harmony-share.md#sharabletargetinfo) | PC/2in1或Tablet设备作为发送端触发碰一碰事件时的相关信息，如轻碰屏幕位置的坐标信息等。 |

**示例：**

```typescript
import { harmonyShare } from '@kit.ShareKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 获取轻碰时的坐标信息
  let sharableTargetInfo = sharableTarget.getInfo();
  console.info('screenX is:', sharableTargetInfo.coordinate?.screenX);
  console.info('screenY is:', sharableTargetInfo.coordinate?.screenY);
});
```

## ReceivableTarget

沙箱接收事件触发后回调参数，可通过此参数进行沙箱接收。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

### receive

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

**示例：**

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { common } from '@kit.AbilityKit';

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
  capabilities: [{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }]
}
// 注册沙箱接收'dataReceive'监听事件
harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
  let uiContext: UIContext = this.getUIContext();
  let context = uiContext.getHostContext() as common.UIAbilityContext;
  receivableTarget.receive(context.filesDir, { // 此路径仅为示例 使用时请替换实际路径
    onDataReceived: (sharedData: systemShare.SharedData) => {
      let sharedRecords = sharedData.getRecords();
      sharedRecords.forEach((record: systemShare.SharedRecord) => {
        // 处理分享数据
      });
    },
    onResult(resultCode: harmonyShare.ShareResultCode) {
      if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
        // To do things.
      }
    }
  });
});
```

### reject

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

**示例：**

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { harmonyShare } from '@kit.ShareKit';

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
  capabilities: [{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }]
}
// 注册沙箱接收'dataReceive'监听事件
harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
  receivableTarget.reject(harmonyShare.ReceivableErrorCode.NO_RECEIVABLE_ERROR);
});
```

### getInfo

getInfo(): ReceivableTargetInfo

获取PC/2in1或Tablet设备作为接收端触发碰一碰事件时的相关信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReceivableTargetInfo](share-harmony-share.md#receivabletargetinfo) | PC/2in1或Tablet设备作为接收端触发碰一碰事件时的相关信息，如轻碰屏幕位置的坐标信息等。 |

**示例：**

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { common } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
  capabilities: [{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }]
}
// 注册沙箱接收'dataReceive'监听事件
harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
  let uiContext: UIContext = this.getUIContext();
  let context = uiContext.getHostContext() as common.UIAbilityContext;
  let sandboxUri = fileUri.getUriFromPath(context.filesDir);
  let receivableTargetInfo = receivableTarget.getInfo();
  console.info('screenX is:', receivableTargetInfo.coordinate?.screenX);
  console.info('screenY is:', receivableTargetInfo.coordinate?.screenY);
  receivableTarget.receive(sandboxUri, {
    onDataReceived: (sharedData: systemShare.SharedData) => {
      let sharedRecords = sharedData.getRecords();
      sharedRecords.forEach((record: systemShare.SharedRecord) => {
        // 处理分享数据
      });
    },
    onResult(resultCode: harmonyShare.ShareResultCode) {
      if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
        // To do things.
      }
    }
  });
});
```

## UpdatedData

华为分享事件发送的数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| thumbnailUri | string | 否 | 是 | 预览图的uri。 |

## BaseCapabilityRegistry

华为分享事件注册基础配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowId | number | 否 | 否 | 窗口id。 |

## SendCapabilityRegistry

华为分享事件窗口注册配置项。继承[BaseCapabilityRegistry](share-harmony-share.md#basecapabilityregistry)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sendOnly | boolean | 否 | 是 | 设置是否仅支持发送数据。默认值：false，表示可同时接收分享数据。当双端设备均设置为true时，双向分享会被拦截。  说明：仅支持碰一碰分享功能。 |

## RecvCapability

设置沙箱接收支持的能力范围（可接收的文件类型及最大数量限制）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| utd | string | 否 | 否 | 统一数据类型，参考[@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](js-apis-data-uniformtypedescriptor.md)。 |
| maxSupportedCount | number | 否 | 否 | 可接收文件的最大数量限制，仅允许设置大于0的整数。 |

## RecvCapabilityRegistry

沙箱接收事件窗口注册配置项。继承[BaseCapabilityRegistry](share-harmony-share.md#basecapabilityregistry)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| capabilities | [RecvCapability](share-harmony-share.md#recvcapability)[] | 否 | 否 | 沙箱接收能力设置，用于设置可接收的数据类型和数量。 |

## TransferBaseResults

沙箱接收时，文件数据传输完成的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onResult | Callback<[ShareResultCode](share-harmony-share.md#shareresultcode)> | 否 | 是 | 传输完成的回调函数。用于通知传输结果。 |

## ReceiveCallback

沙箱接收传输完成后回调函数。可用此方法监听完成事件，并处理接收后的数据。继承[TransferBaseResults](share-harmony-share.md#transferbaseresults)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onDataReceived | Callback<[systemShare.SharedData](share-system-share.md#shareddata)> | 否 | 否 | 沙箱接收传输完成后回调函数。用于接收已保存至沙箱路径下的文件列表。 |

## SharableErrorInfo

提示信息，用于告知用户无法分享的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | 否 | 是 | 提示文案。 |

## CoordinateInfo

手机与PC/2in1或Tablet设备碰一碰触发时，轻碰屏幕位置的坐标信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| screenX | number | 否 | 否 | 碰一碰事件触发时，以屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数。单位：px。 |
| screenY | number | 否 | 否 | 碰一碰事件触发时，以屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数。单位：px。 |

## SharableTargetInfo

PC/2in1或Tablet设备作为发送端，触发碰一碰时的相关信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| coordinate | [CoordinateInfo](share-harmony-share.md#coordinateinfo) | 否 | 是 | 碰一碰事件触发时，轻碰屏幕位置的坐标信息。 |

## ReceivableTargetInfo

PC/2in1或Tablet设备作为接收端，触发碰一碰时的相关信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| coordinate | [CoordinateInfo](share-harmony-share.md#coordinateinfo) | 否 | 是 | 碰一碰事件触发时，轻碰屏幕位置的坐标信息。 |

## on('knockShare')

on(event: 'knockShare', callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 回调函数。返回分享发送对象，用于完成分享内容发送。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
private tipsListening() {
  if (!this.tipsStatus) {
    harmonyShare.on('knockShare', this.sendOnlyCallback);
    this.tipsStatus = true;
  } else {
    try {
      const uiContext: UIContext = this.getUIContext();
      uiContext.getPromptAction().showToast({ message: $r('app.string.knock_close_other') });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
}
```

## off('knockShare')

off(event: 'knockShare', callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。使用callback异步回调。

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

```typescript
private tipsDisablingListening() {
  harmonyShare.off('knockShare', this.sendOnlyCallback);
  this.tipsStatus = true;
}
```

## on('knockShare')

on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。推荐在PC/2in1和Tablet上使用此方法，通过设置windowId参数指定可轻贴的窗口。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 回调函数。返回分享发送对象，用于完成分享内容发送。 |

**示例：**

```typescript
private sendOnlyListening() {
  if (!this.sendOnlyStatus) {
    if (this.windowId) {
      let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
        windowId: this.windowId,
        sendOnly: true,
      }
      harmonyShare.on('knockShare', capabilityRegistry, this.sendOnlyCallback);
      this.sendOnlyStatus = true;
    }
  } else {
    try {
      const uiContext: UIContext = this.getUIContext();
      uiContext.getPromptAction().showToast({ message: $r('app.string.knock_close_other') });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
}
```

## off('knockShare')

off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。推荐在PC/2in1和Tablet上使用此方法，通过设置windowId参数指定可轻贴的窗口。使用callback异步回调。

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

```typescript
private sendOnlyDisablingListening() {
  if (this.windowId) {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: this.windowId,
      sendOnly: true,
    }
    harmonyShare.off('knockShare', capabilityRegistry, this.sendOnlyCallback);
    this.sendOnlyStatus = false;
  }
}
```

## on('gesturesShare')

on(event: 'gesturesShare', callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 回调函数。返回分享发送对象，用于完成分享内容发送。 |

**示例：**

```typescript
private immersiveListening() {
  if (this.isNoListening()) {
    harmonyShare.on('gesturesShare', this.immersiveCallback);
    this.immersiveStatus = true;
  } else {
    try {
      const uiContext: UIContext = this.getUIContext();
      uiContext.getPromptAction().showToast({ message: $r('app.string.gesture_close_other') });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
}
```

## off('gesturesShare')

off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，取消隔空传送的事件监听。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```typescript
private immersiveDisablingListening() {
  harmonyShare.off('gesturesShare', this.immersiveCallback);
  this.immersiveStatus = false;
}
```

## on('gesturesShare')

on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。 |
| capability | [SendCapabilityRegistry](share-harmony-share.md#sendcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[SharableTarget](share-harmony-share.md#sharabletarget)> | 是 | 回调函数。返回分享发送对象，用于完成分享内容发送。 |

**示例：**

```typescript
private purityListening() {
  if (this.isNoListening()) {
    if (this.windowId) {
      let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
        windowId: this.windowId,
      }
      harmonyShare.on('gesturesShare', capabilityRegistry, this.purityCallback);
      this.purityStatus = true;
    }
  } else {
    try {
      const uiContext: UIContext = this.getUIContext();
      uiContext.getPromptAction().showToast({ message: $r('app.string.gesture_close_other') });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
}
```

## off('gesturesShare')

off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。使用callback异步回调。

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

```typescript
private purityDisablingListening() {
  if (this.windowId) {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: this.windowId,
    }
    harmonyShare.off('gesturesShare', capabilityRegistry, this.purityCallback);
    this.purityStatus = false;
  }
}
```

## on('dataReceive')

on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void

注册沙箱接收事件监听。仅支持文件类型数据。文本（包含链接）类型的数据保持原有接收逻辑。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**设备行为差异：** 对于6.0.2(22)及之前的版本，该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。从6.1.0(23)开始，该接口在PC/2in1、Tablet中均可正常使用，在其他设备类型中无响应。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'dataReceive'，当手机设备轻贴PC/2in1、Tablet设备屏幕时，触发该事件。 |
| capability | [RecvCapabilityRegistry](share-harmony-share.md#recvcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[ReceivableTarget](share-harmony-share.md#receivabletarget)> | 是 | 回调函数。返回分享接收对象，用于完成分享内容接收。 |

**示例：**

```typescript
private dataReceiveCallback = (receivableTarget: harmonyShare.ReceivableTarget) => {
  let uiContext: UIContext = this.getUIContext();
  let context = uiContext.getHostContext() as common.UIAbilityContext;
  let sandboxUri = fileUri.getUriFromPath(context.filesDir);
  receivableTarget.receive(sandboxUri, {
    onDataReceived: (sharedData: systemShare.SharedData) => {
      let sharedRecords = sharedData.getRecords();
      sharedRecords.forEach((record: systemShare.SharedRecord) => {
        this.dataReceiveUri = record.uri;
      });
    },
    onResult: (resultCode: harmonyShare.ShareResultCode) => {
      if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
        try {
          const uiContext: UIContext = this.getUIContext();
          uiContext.getPromptAction().showToast({ message: $r('app.string.success_supported') });
        } catch (error) {
          hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
        }
      }
    }
  });
}

private isNoListening() {
  return !this.dataReceiveStatus;
}

private dataReceiveListening() {
  if (this.isNoListening()) {
    if (this.windowId) {
      let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
        windowId: this.windowId,
        capabilities: [{
          utd: utd.UniformDataType.IMAGE,
          maxSupportedCount: 1,
        }]
      }
      harmonyShare.on('dataReceive', capabilityRegistry, this.dataReceiveCallback);
      this.dataReceiveStatus = true;
    }
  } else {
    try {
      const uiContext: UIContext = this.getUIContext();
      uiContext.getPromptAction().showToast({ message: $r('app.string.knock_close_other') });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
}
```

## off('dataReceive')

off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void

取消沙箱接收的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.HarmonyShare

**设备行为差异：** 对于6.0.2(22)及之前的版本，该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。从6.1.0(23)开始，该接口在PC/2in1、Tablet中均可正常使用，在其他设备类型中无响应。

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，取值为'dataReceive'，取消沙箱接收的事件监听。 |
| capability | [RecvCapabilityRegistry](share-harmony-share.md#recvcapabilityregistry) | 是 | 事件属性。 |
| callback | Callback<[ReceivableTarget](share-harmony-share.md#receivabletarget)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**示例：**

```typescript
private dataReceiveDisablingListening() {
  try {
    if (this.windowId) {
      let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
        windowId: this.windowId,
        capabilities: [{
          utd: utd.UniformDataType.IMAGE,
          maxSupportedCount: 1,
        }]
      }
      harmonyShare.off('dataReceive', capabilityRegistry, this.dataReceiveCallback);
      this.dataReceiveStatus = false;
    }
  } catch (error) {
    hilog.error(DOMAIN, 'testTag', 'error message: %s', error?.message ?? 'unknown error');
  }
}
```
