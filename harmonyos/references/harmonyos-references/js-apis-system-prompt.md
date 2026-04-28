---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-prompt
title: @system.prompt (弹窗)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.prompt (弹窗)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:44476486ddca009f0f43ad282b12451c61d38f9c36adfb375972a8a7def010e1
---

创建并显示文本提示框、对话框和操作菜单。

说明

* 从API version 8 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](js-apis-promptaction.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import prompt from '@system.prompt';
```

## prompt.showToast

PhonePC/2in1TabletTVWearable

showToast(options: ShowToastOptions): void

显示文本弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-system-prompt.md#showtoastoptions) | 是 | 定义ShowToast的选项。 |

**示例：**

```
1. import prompt from '@system.prompt';
2. class A{
3. showToast() {
4. prompt.showToast({
5. message: 'Message Info',
6. duration: 2000
7. });
8. }
9. }
10. export default new A()
```

## prompt.showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions): void

显示对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-system-prompt.md#showdialogoptions) | 是 | 定义显示对话框的选项。 |

**示例：**

```
1. import prompt from '@system.prompt';
2. class B{
3. showDialog() {
4. prompt.showDialog({
5. title: 'Title Info',
6. message: 'Message Info',
7. buttons: [
8. {
9. text: 'button',
10. color: '#666666'
11. },
12. ],
13. success: (data)=> {
14. console.info('dialog success callback，click button : ' + data.index);
15. },
16. cancel: ()=> {
17. console.info('dialog cancel callback');
18. },
19. });
20. }
21. }
22. export default new B()
```

## prompt.showActionMenu6+

PhonePC/2in1TabletTVWearable

showActionMenu(options: ShowActionMenuOptions): void

显示操作菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowActionMenuOptions](js-apis-system-prompt.md#showactionmenuoptions6) | 是 | 定义ShowActionMenu的选项。 |

**示例：**

```
1. import prompt from '@system.prompt';
2. class C{
3. showActionMenu() {
4. prompt.showActionMenu({
5. title: 'Title Info',
6. buttons: [
7. {
8. text: 'item1',
9. color: '#666666'
10. },
11. {
12. text: 'item2',
13. color: '#000000'
14. },
15. ],
16. success: (tapIndex)=> {
17. console.info('dialog success callback，click button : ' + tapIndex);
18. },
19. fail: (errMsg)=> {
20. console.info('dialog fail callback' + errMsg);
21. },
22. });
23. }
24. }
25. export default new C()
```

## ShowToastOptions

PhonePC/2in1TabletTVWearable

定义ShowToast的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，建议区间：1500ms-10000ms。若小于1500ms则取默认值，最大取值为10000ms。 |
| bottom5+ | string|number | 否 | 设置弹窗边框距离屏幕底部的位置。 |

## Button

PhonePC/2in1TabletTVWearable

定义按钮的提示信息。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 定义按钮信息。 |
| color | string | 是 | 定义按钮颜色。 |

## ShowDialogSuccessResponse

PhonePC/2in1TabletTVWearable

定义ShowDialog的响应。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 定义数据的索引信息。 |

## ShowDialogOptions

PhonePC/2in1TabletTVWearable

定义显示对话框的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 文本内容。 |
| buttons | [[Button](js-apis-system-prompt.md#button), [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |
| success | (data: [ShowDialogSuccessResponse](js-apis-system-prompt.md#showdialogsuccessresponse)) => void | 否 | 接口调用成功的回调函数。 |
| cancel | (data: string, code: string) => void | 否 | 接口调用失败的回调函数。 |
| complete | (data: string) => void | 否 | 接口调用结束的回调函数。 |

## ShowActionMenuOptions6+

PhonePC/2in1TabletTVWearable

定义ShowActionMenu的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](js-apis-system-prompt.md#button), [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?] | 是 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。 |
| success | (tapIndex: number, errMsg: string) => void | 否 | 弹出对话框时调用。 |
| fail | (errMsg: string) => void | 否 | 接口调用失败的回调函数。 |
| complete | (data: string) => void | 否 | 关闭对话框时调用。 |
