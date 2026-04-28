---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide
title: 挂载卸载事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 组件变化事件 > 挂载卸载事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c52fe19fa78e63e7e04e02f28d3f6d036998387edfef64ad526ab4ea25c2fdd3
---

挂载卸载事件指组件从组件树上挂载、卸载时触发的事件。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## onAttach12+

PhonePC/2in1TabletTVWearable

onAttach(callback: Callback<void>): T

组件挂载到组件树时触发此回调。由于以下说明中的限制，建议使用[onAppear](ts-universal-events-show-hide.md#onappear)替代此接口。

说明

* 回调在组件布局渲染前调用。
* 不允许在回调中对组件树进行变更，例如启动动画或使用if-else变更组件树结构。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | onAttach事件的回调函数，表示组件已经挂载至组件树。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDetach12+

PhonePC/2in1TabletTVWearable

onDetach(callback: Callback<void>): T

组件从组件树卸载时触发此回调。建议使用[onDisAppear](ts-universal-events-show-hide.md#ondisappear)替代此接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | 是 | onDetach事件的回调函数，表示组件已经从组件树卸载。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onAppear

PhonePC/2in1TabletTVWearable

onAppear(event: () => void): T

组件挂载后触发此回调。

说明

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
| T | 返回当前组件。 |

## onDisAppear

PhonePC/2in1TabletTVWearable

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
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过按钮控制组件的挂载和卸载，触发onAttach和onDetach事件。

```
1. // xxx.ets
2. import { promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct AppearExample {
7. @State isShow: boolean = true;
8. @State changeAppear: string = '点我卸载挂载组件';
9. private myText: string = 'Text for onAppear';

11. build() {
12. Column() {
13. Button(this.changeAppear)
14. .onClick(() => {
15. this.isShow = !this.isShow
16. }).margin(15)
17. if (this.isShow) {
18. Text(this.myText).fontSize(26).fontWeight(FontWeight.Bold)
19. .onAttach(() => {
20. this.getUIContext().getPromptAction().showToast({
21. message: 'The text is shown',
22. duration: 2000,
23. bottom: 500
24. })
25. })
26. .onDetach(() => {
27. this.getUIContext().getPromptAction().showToast({
28. message: 'The text is hidden',
29. duration: 2000,
30. bottom: 500
31. })
32. })
33. }
34. }.padding(30).width('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/vSWEUlSoRGa16ojb3GSupQ/zh-cn_image_0000002583439519.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000057Z&HW-CC-Expire=86400&HW-CC-Sign=F8F8387C883FCA8276D557AAC39DF06597511F61EA72C2147F4E4940652FA4DC)
