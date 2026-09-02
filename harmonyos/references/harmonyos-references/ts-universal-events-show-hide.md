---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide
title: 挂载卸载事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 组件变化事件 > 挂载卸载事件
category: harmonyos-references
scraped_at: 2026-09-02T15:00:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a32684c423541b7cfdb68a06627280527ada876332e4c524257761cf21cd87a5
---

挂载卸载事件指组件从组件树上挂载、卸载时触发的事件，可用于监听组件挂载与卸载过程中的生命周期变化，并在相应时机执行相关业务处理。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## onAttach12+

onAttach(callback: Callback<void>): T

组件挂载到组件树时触发此回调。由于以下说明中的限制，建议使用[onAppear](ts-universal-events-show-hide.md#onappear)替代此接口。

**说明** 

* 回调在组件布局渲染前调用。
* 不允许在回调中对组件树进行变更，例如启动动画或使用if-else变更组件树结构。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | onAttach事件的回调函数，表示组件已经挂载至组件树。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## onDetach12+

onDetach(callback: Callback<void>): T

组件从组件树卸载时触发此回调。建议使用[onDisAppear](ts-universal-events-show-hide.md#ondisappear)替代此接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | onDetach事件的回调函数，表示组件已经从组件树卸载。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## onAppear

onAppear(event: () => void): T

组件挂载后触发此回调。

**说明** 

回调的调用时机有可能发生在组件布局渲染后。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | onAppear事件的回调函数，表示组件已挂载显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## onDisAppear

onDisAppear(event: () => void): T

组件从组件树卸载时触发此回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | onDisAppear事件的回调函数，表示组件已卸载消失。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## 示例

该示例通过按钮控制组件的挂载和卸载，触发onAttach和onDetach事件。

```ts
// xxx.ets
@Entry
@Component
struct AppearExample {
  @State isShow: boolean = true;
  @State changeAppear: string = '点我卸载挂载组件';
  private myText: string = 'Text for onAppear';

  build() {
    Column() {
      Button(this.changeAppear)
        .onClick(() => {
          this.isShow = !this.isShow;
        }).margin(15)
      if (this.isShow) {
        Text(this.myText).fontSize(26).fontWeight(FontWeight.Bold)
          .onAttach(() => {
            this.getUIContext().getPromptAction().showToast({
              message: 'The text is shown',
              duration: 2000,
              bottom: 500
            })
          })
          .onDetach(() => {
            this.getUIContext().getPromptAction().showToast({
              message: 'The text is hidden',
              duration: 2000,
              bottom: 500
            })
          })
      }
    }.padding(30).width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/0VHli6xYSwiOikaUdRr_Yg/zh-cn_image_0000002706835606.gif)
