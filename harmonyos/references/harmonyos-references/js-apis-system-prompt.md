---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-prompt
title: "@system.prompt (弹窗)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.prompt (弹窗)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:759cf351513c1ec21884e693731049b1bd003d58f854900067fd8d2ab5cb9865
---

创建并显示文本提示框、对话框和操作菜单。

**说明** 

* 从API version 8 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](js-apis-promptaction.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import prompt from '@system.prompt';
```

## prompt.showToast

showToast(options: ShowToastOptions): void

显示文本弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-system-prompt.md#showtoastoptions) | 是 | 定义ShowToast的选项。 |

**示例：**

```ts
import prompt from '@system.prompt';
class A{
  showToast() {
    prompt.showToast({
      message: 'Message Info',
      duration: 2000
    });
  }
}
export default new A()
```

## prompt.showDialog

showDialog(options: ShowDialogOptions): void

显示对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-system-prompt.md#showdialogoptions) | 是 | 定义显示对话框的选项。 |

**示例：**

```ts
import prompt from '@system.prompt';
class B{
  showDialog() {
    prompt.showDialog({
      title: 'Title Info',
      message: 'Message Info',
      buttons: [
        {
          text: 'button',
          color: '#666666'
        },
      ],
      success: (data)=> {
        console.info('dialog success callback，click button : ' + data.index);
      },
      cancel: ()=> {
        console.info('dialog cancel callback');
      },
    });
  }
}
export default new B()
```

## prompt.showActionMenu6+

showActionMenu(options: ShowActionMenuOptions): void

显示操作菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowActionMenuOptions](js-apis-system-prompt.md#showactionmenuoptions6) | 是 | 定义ShowActionMenu的选项。 |

**示例：**

```ts
import prompt from '@system.prompt';
class C{
  showActionMenu() {
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
      ],
      success: (tapIndex)=> {
        console.info('dialog success callback，click button : ' + tapIndex);
      },
      fail: (errMsg)=> {
        console.info('dialog fail callback' + errMsg);
      },
    });
  }
}
export default new C()
```

## ShowToastOptions

定义ShowToast的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，建议区间：1500ms-10000ms。若小于1500ms则取默认值，最大取值为10000ms。 |
| bottom5+ | string|number | 否 | 设置弹窗边框距离屏幕底部的位置。 |

## Button

定义按钮的显示信息。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 定义按钮文本。 |
| color | string | 是 | 定义按钮颜色。 |

## ShowDialogSuccessResponse

定义ShowDialog的响应。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 被点击按钮的索引值。 |

## ShowDialogOptions

定义显示对话框的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 文本内容。 |
| buttons | [[Button](js-apis-system-prompt.md#button), [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。大于3个按钮时弹窗不显示。 |
| success | (data: [ShowDialogSuccessResponse](js-apis-system-prompt.md#showdialogsuccessresponse)) => void | 否 | 接口调用成功的回调函数。 |
| cancel | (data: string, code: string) => void | 否 | 接口调用取消的回调函数。 |
| complete | (data: string) => void | 否 | 接口调用结束的回调函数。 |

## ShowActionMenuOptions6+

定义ShowActionMenu的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](js-apis-system-prompt.md#button), [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?, [Button](js-apis-system-prompt.md#button)?] | 是 | 操作菜单中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。 |
| success | (tapIndex: number, errMsg: string) => void | 否 | 操作菜单选择成功的回调函数。 |
| fail | (errMsg: string) => void | 否 | 接口调用失败的回调函数。 |
| complete | (data: string) => void | 否 | 接口调用结束的回调函数。 |
