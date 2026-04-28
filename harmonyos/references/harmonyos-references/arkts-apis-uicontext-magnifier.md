---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-magnifier
title: Class (Magnifier)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (Magnifier)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:018c903c2cc53006575856bba3132a9bd8ca3a85d05d148fbf8725d5dd936c0c
---

提供控制放大镜的显示与隐藏的能力，放大镜会对组件内容进行放大显示，便于查看组件细节。

说明

* 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 22开始支持。
* 以下API需先使用UIContext中的[getMagnifier()](arkts-apis-uicontext-uicontext.md#getmagnifier22)方法获取Magnifier实例，再通过此实例调用对应方法。
* 与文本类组件自带的放大镜能力互不影响，文本类组件推荐使用自带的放大镜能力。

## bind

PhonePC/2in1TabletTVWearable

bind(id: string): void

绑定放大镜与指定id的组件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件id，可通过通用属性[id](ts-universal-attributes-component-id.md#id)或[key](ts-universal-attributes-component-id.md#key12)设置。当组件id为空字符串或未找到匹配id的组件时，不显示放大镜。 |

**示例：**

该示例通过监听onTouch事件控制放大镜对图片进行放大显示。

```
1. import { Magnifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MagnifierExample {
6. private magnifier: Magnifier = this.getUIContext().getMagnifier();

8. build() {
9. Column() {
10. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
11. Image($r('app.media.startIcon'))
12. .draggable(false)
13. .width(200)
14. .height(200)
15. .margin(50)
16. .id('image')
17. .onTouch((event?: TouchEvent) => {
18. if (event && event.sourceTool === SourceTool.Finger) {
19. if (event.type === TouchType.Down) {
20. this.magnifier.bind('image')
21. } else if (event.type === TouchType.Move) {
22. let x = event.touches[0].x
23. let y = event.touches[0].y
24. this.magnifier.show(x, y)
25. } else if (event.type === TouchType.Up) {
26. this.magnifier.unbind()
27. } else if (event.type === TouchType.Cancel) {
28. this.magnifier.unbind()
29. }
30. }
31. })
32. }
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/WrD44__fQ3ysoC9jVh6uZQ/zh-cn_image_0000002552959410.png?HW-CC-KV=V1&HW-CC-Date=20260428T000023Z&HW-CC-Expire=86400&HW-CC-Sign=4D074D59BB8D170A654181984C9D06EE7B0AF1B66F831269380996A7CC5E8734)

## show

PhonePC/2in1TabletTVWearable

show(x: number, y: number): void

设置放大镜显示的组件内容相对于组件左上角的位置，设置成功后放大镜会对以该坐标点为中心的区域内容进行放大显示。

说明

当与放大镜绑定的组件自身内容发生变化时，放大镜显示内容不会自动更新，需要主动调用show接口对放大镜显示内容进行更新。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 放大镜显示的组件内容相对组件水平方向坐标，单位为vp。当坐标值大于组件宽度或小于0时不显示放大镜；将值设为undefined时保持放大镜的当前显示状态。 |
| y | number | 是 | 放大镜显示的组件内容相对组件垂直方向坐标，单位为vp。当坐标值大于组件高度或小于0时不显示放大镜；将值设为undefined时保持放大镜的当前显示状态。 |

**示例：**

请参考[bind](arkts-apis-uicontext-magnifier.md#bind)示例。

## unbind

PhonePC/2in1TabletTVWearable

unbind(): void

解除放大镜与当前组件的绑定。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[bind](arkts-apis-uicontext-magnifier.md#bind)示例。
