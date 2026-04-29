---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt
title: @ohos.prompt (弹窗)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @ohos.prompt (弹窗)
category: harmonyos-references
scraped_at: 2026-04-29T13:51:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5bf828ee2cf687e1fca0fba894d11c25fd670be7bcb7e5c779ded04a5719d9ad
---

创建并显示文本提示框、对话框和操作菜单。

说明

从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](js-apis-promptaction.md)。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import prompt from '@ohos.prompt'
```

## prompt.showToast

PhonePC/2in1TabletTVWearable

showToast(options: ShowToastOptions): void

创建并显示文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-prompt.md#showtoastoptions) | 是 | 文本弹窗选项。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showToast({
3. message: 'Message Info',
4. duration: 2000
5. });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/4idmK20gQlKCwp055DgLTQ/zh-cn_image_0000002589325851.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055058Z&HW-CC-Expire=86400&HW-CC-Sign=64075094EF9A67CD4A53C7BA8B861719D0CB9FA5AFAA2FD7DD1EB3D4FDFE7E05)

## ShowToastOptions

PhonePC/2in1TabletTVWearable

文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。 |
| bottom | string| number | 否 | 设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。 |

## prompt.showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框响应后同步返回结果。

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

```
1. import prompt from '@ohos.prompt'
2. prompt.showDialog({
3. title: 'Title Info',
4. message: 'Message Info',
5. buttons: [
6. {
7. text: 'button1',
8. color: '#000000'
9. },
10. {
11. text: 'button2',
12. color: '#000000'
13. }
14. ],
15. })
16. .then(data => {
17. console.info('showDialog success, click button: ' + data.index);
18. })
19. .catch((err:Error) => {
20. console.info('showDialog error: ' + err);
21. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/z4cs7W0ASX-6dpXuZUP2Dw/zh-cn_image_0000002589325815.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055058Z&HW-CC-Expire=86400&HW-CC-Sign=2BBCCE57A232478D30D1B5CC85A3A112BB0EF1F0DB0EAA2643C065B1E85ABECB)

## prompt.showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-prompt.md#showdialogoptions) | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback<[ShowDialogSuccessResponse](js-apis-prompt.md#showdialogsuccessresponse)> | 是 | 对话框响应结果回调。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showDialog({
3. title: 'showDialog Title Info',
4. message: 'Message Info',
5. buttons: [
6. {
7. text: 'button1',
8. color: '#000000'
9. },
10. {
11. text: 'button2',
12. color: '#000000'
13. }
14. ]
15. }, (err, data) => {
16. if (err) {
17. console.info('showDialog err: ' + err);
18. return;
19. }
20. console.info('showDialog success callback, click button: ' + data.index);
21. });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/dJ3uc8_gR1GLpyvYgPE14Q/zh-cn_image_0000002589245757.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055058Z&HW-CC-Expire=86400&HW-CC-Sign=5E4597C161522BE6AC91C6F3A9CD437646E962954FAE3EC88E7E4EA1324ADC22)

## ShowDialogOptions

PhonePC/2in1TabletTVWearable

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 内容文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。其中第一个为positiveButton，第二个为negativeButton，第三个为neutralButton。 |

## ShowDialogSuccessResponse

PhonePC/2in1TabletTVWearable

对话框的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引。 |

## prompt.showActionMenu

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果异步返回。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-prompt.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[ActionMenuSuccessResponse](js-apis-prompt.md#actionmenusuccessresponse)> | 是 | 菜单响应结果回调。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showActionMenu({
3. title: 'Title Info',
4. buttons: [
5. {
6. text: 'item1',
7. color: '#666666'
8. },
9. {
10. text: 'item2',
11. color: '#000000'
12. },
13. ]
14. }, (err, data) => {
15. if (err) {
16. console.info('showActionMenu err: ' + err);
17. return;
18. }
19. console.info('showActionMenu success callback, click button: ' + data.index);
20. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/DmqLZ7OxRU6k44L_l5TCKQ/zh-cn_image_0000002589325817.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055058Z&HW-CC-Expire=86400&HW-CC-Sign=434BD3955FB98F6DAB8E8D70F61A9C2EFAB2A3276C43BA70AF96659F9ADBDBEC)

## prompt.showActionMenu

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后同步返回结果。

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

```
1. import prompt from '@ohos.prompt'
2. prompt.showActionMenu({
3. title: 'showActionMenu Title Info',
4. buttons: [
5. {
6. text: 'item1',
7. color: '#666666'
8. },
9. {
10. text: 'item2',
11. color: '#000000'
12. },
13. ]
14. })
15. .then(data => {
16. console.info('showActionMenu success, click button: ' + data.index);
17. })
18. .catch((err:Error) => {
19. console.info('showActionMenu error: ' + err);
20. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/dxEKdPJPSAiGqhQWUD1dlg/zh-cn_image_0000002558765948.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055058Z&HW-CC-Expire=86400&HW-CC-Sign=172649AF577BF6D1E918430361D89B60A41D0FA5C3BE217284053E74D7F12396)

## ActionMenuOptions

PhonePC/2in1TabletTVWearable

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 是 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |

## ActionMenuSuccessResponse

PhonePC/2in1TabletTVWearable

操作菜单的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引，从0开始。 |

## Button

PhonePC/2in1TabletTVWearable

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 按钮文本内容。 |
| color | string | 是 | 按钮文本颜色。 |
