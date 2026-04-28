---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-metadatabinding
title: @ohos.multimodalAwareness.metadataBinding (记忆链接)
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > ArkTS API > @ohos.multimodalAwareness.metadataBinding (记忆链接)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a68dc0502c054d8213af9a4e431d5987029165fcb2a6d1ef105398ba49d71986
---

本模块提供记忆链接能力调用，包括编码内容传递、订阅事件和取消订阅事件。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTablet

```
1. import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## metadataBinding.submitMetadata

PhoneTablet

submitMetadata(metadata: string): void

第三方应用将需要编码的内容传递给MSDP，MSDP决定适时将内容传递给调用编码接口的系统应用或服务。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadata | string | 是 | 要嵌入图片中的信息。 |

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](errorcode-metadatabinding.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 32100001 | Internal handling failed. Set Meta data to screenshot app fail. |

**示例**：

```
1. import { metadataBinding } from '@kit.MultimodalAwarenessKit';

3. let metadata: string = "";
4. try {
5. metadataBinding.submitMetadata(metadata);
6. } catch (error) {
7. console.error("submit metadata error" + error);
8. }
```

## metadataBinding.on('operationSubmitMetadata')

PhoneTablet

on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void

订阅系统事件以获取编码内容，应用注册回调，事件发生时回传编码内容。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，type为‘operationSubmitMetadata’，表示系统应用获取编码内容。 |
| bundleName | string | 是 | 应用包名，标识注册应用的包名。 |
| callback | Callback<number> | 是 | 回调函数，用于返回编码内容。 |

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](errorcode-metadatabinding.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 32100001 | Internal handling failed. Service exception. |
| 32100004 | Subscribe Failed. Possible causes: 1. Abnormal system capability; 2. IPC communication abnormality; 3. Algorithm loading exception. |

**示例：**

```
1. import { metadataBinding } from '@kit.MultimodalAwarenessKit';

3. let bundleName: string = '';
4. try {
5. metadataBinding.on('operationSubmitMetadata', bundleName, (event: number) => {
6. if (event == 1) {
7. console.info("The screenshot request is intercepted and the app link is obtained");
8. }
9. });
10. } catch (error) {
11. console.error("register screenshot event error");
12. }
```

## metadataBinding.off('operationSubmitMetadata')

PhoneTablet

off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void

取消订阅系统获取编码内容的事件。取消注册回调接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，type为“operationSubmitMetadata”，表示系统应用获取编码内容。 |
| bundleName | string | 是 | 应用包名，标识注册应用的包名。 |
| callback | Callback<number> | 否 | 回调函数，返回编码内容。 |

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](errorcode-metadatabinding.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 32100001 | Internal handling failed. Service exception. |
| 32100005 | Unsubscribe Failed. Possible causes: 1. Abnormal system capability; 2. IPC communication abnormality. |

**示例**：

```
1. import { metadataBinding } from '@kit.MultimodalAwarenessKit';

3. let bundleName: string = '';
4. try {
5. metadataBinding.off('operationSubmitMetadata', bundleName, (event: number) => {
6. });
7. } catch (error) {
8. console.error("unsubscript screenshot event" + error);
9. }
```
