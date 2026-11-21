---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt
title: "@ohos.prompt (弹窗)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @ohos.prompt (弹窗)
category: harmonyos-references
scraped_at: 2026-11-21T09:13:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6cdf795230f76d155834947df46a7b5e738435bf1f110aa9bbb9cc23538f048
---

创建并显示文本提示框、对话框和操作菜单。

**说明** 

从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](js-apis-promptaction.md)。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import prompt from '@ohos.prompt'
```

## prompt.showToast

showToast(options: ShowToastOptions): void

创建并显示文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-prompt.md#showtoastoptions) | 是 | 文本弹窗选项。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
  duration: 2000
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/8OYkQ3m3T5O7GWHzYhzcMQ/zh-cn_image_0000002793038636.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011358Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA9BAC77E574BD0DFB893F1283728DEBF349C89B0C8970ED25B5AC551532BF42)

## ShowToastOptions

文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。 |
| bottom | string| number | 否 | 设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。 |

## prompt.showDialog

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-prompt.md#showdialogoptions) | 是 | 对话框选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShowDialogSuccessResponse](js-apis-prompt.md#showdialogsuccessresponse)> | 对话框响应结果。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showDialog error: ' + err);
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/N6ON_j3aRu-ewubxa8VnGQ/zh-cn_image_0000002821838533.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011358Z&HW-CC-Expire=31536000000&HW-CC-Sign=32FAA3A3A6E23FA308102D051F27B56021E3953913AC714A66D0675223352467)

## prompt.showDialog

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-prompt.md#showdialogoptions) | 是 | 对话框选项。 |
| callback | AsyncCallback<[ShowDialogSuccessResponse](js-apis-prompt.md#showdialogsuccessresponse)> | 是 | 对话框响应结果回调。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'showDialog Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ]
}, (err, data) => {
  if (err) {
    console.info('showDialog err: ' + err);
    return;
  }
  console.info('showDialog success callback, click button: ' + data.index);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/tSSuDwL0RZ-Z9J1wJAf_9g/zh-cn_image_0000002821758535.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011358Z&HW-CC-Expire=31536000000&HW-CC-Sign=79CF1F2485BF87D17CC4CB8EA427D27F98EFEB6AEC667C6F6506ABA060C2EB06)

## ShowDialogOptions

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 内容文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。其中第一个为positiveButton，第二个为negativeButton，第三个为neutralButton。 |

## ShowDialogSuccessResponse

对话框的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引。 |

## prompt.showActionMenu

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果异步返回。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-prompt.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[ActionMenuSuccessResponse](js-apis-prompt.md#actionmenusuccessresponse)> | 是 | 菜单响应结果回调。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
}, (err, data) => {
  if (err) {
    console.info('showActionMenu err: ' + err);
    return;
  }
  console.info('showActionMenu success callback, click button: ' + data.index);
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/LSwF2NrJSTeasOJ1wm66nw/zh-cn_image_0000002821838535.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011358Z&HW-CC-Expire=31536000000&HW-CC-Sign=966DA16A14657FB315B0B07CB69D2D8991F63C40904686F4DB184D7E1B8F3804)

## prompt.showActionMenu

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-prompt.md#actionmenuoptions) | 是 | 操作菜单选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ActionMenuSuccessResponse](js-apis-prompt.md#actionmenusuccessresponse)> | 菜单响应结果。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showActionMenu error: ' + err);
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/JE5APWGqS8eIGOEf72dPTQ/zh-cn_image_0000002793038600.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011358Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3AC27DEEE2C9CC665F07B2C87FA286FAFB0FE22630D98FE0C3EAE95CD975C17)

## ActionMenuOptions

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 是 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |

## ActionMenuSuccessResponse

操作菜单的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引，从0开始。 |

## Button

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 按钮文本内容。 |
| color | string | 是 | 按钮文本颜色。 |
