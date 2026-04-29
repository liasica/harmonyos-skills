---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-geometrytransition
title: 组件内隐式共享元素转场 (geometryTransition)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 组件内隐式共享元素转场 (geometryTransition)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:43+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:adbcdf53e0d69f01a6317b42aae1e1a758889cad6eb4ae7b43094f9600f1a1f4
---

在视图切换过程中提供丝滑的上下文传承过渡。通用transition机制提供了opacity、scale等转场效果，geometryTransition通过安排绑定的in/out组件（in指新视图、out指旧视图）的frame、position使得原本独立的transition动画在空间位置上发生联系，将视觉焦点由旧视图位置引导到新视图位置。

说明

从API version 7开始支持，从API version 10开始生效。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[geometryTransition](ts-transition-animation-geometrytransition.md)必须配合[animateTo](arkts-apis-uicontext-uicontext.md#animateto)使用才有动画效果，动效时长、曲线跟随[animateTo](arkts-apis-uicontext-uicontext.md#animateto)中的配置，不支持[animation](ts-animatorproperty.md)动画。

## geometryTransition

PhonePC/2in1TabletTVWearable

geometryTransition(id: string): T

组件内隐式共享元素转场。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 用于设置绑定关系，id置空字符串清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## geometryTransition11+

PhonePC/2in1TabletTVWearable

geometryTransition(id: string, options?: GeometryTransitionOptions): T

组件内隐式共享元素转场。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 用于设置绑定关系，id置空字符串清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |
| options | [GeometryTransitionOptions](ts-transition-animation-geometrytransition.md#geometrytransitionoptions11) | 否 | 组件内共享元素转场动画参数。  默认值为 { follow: false }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## GeometryTransitionOptions11+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| follow | boolean | 否 | 是 | 仅用于if范式下标记始终在组件树上的组件是否跟随做共享动画。true代表跟随做共享动画，false代表不跟随做共享动画。  默认值：false |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State isShow: boolean = false;

7. build() {
8. Stack({ alignContent: Alignment.Center }) {
9. if (this.isShow) {
10. // 图片使用Resource资源，需用户自定义
11. Image($r('app.media.pic'))
12. .autoResize(false)
13. .clip(true)
14. .width(300)
15. .height(400)
16. .offset({ y: 100 })
17. .geometryTransition("picture", { follow: false })
18. .transition(TransitionEffect.OPACITY)
19. } else {
20. // geometryTransition此处绑定的是容器，那么容器内的子组件需设为相对布局跟随父容器变化，
21. // 套多层容器为了说明相对布局约束传递
22. Column() {
23. Column() {
24. // 图片使用Resource资源，需用户自定义
25. Image($r('app.media.icon'))
26. .width('100%').height('100%')
27. }.width('100%').height('100%')
28. }
29. .width(80)
30. .height(80)
31. // geometryTransition会同步圆角，但仅限于geometryTransition绑定处，此处绑定的是容器
32. // 则对容器本身有圆角同步而不会操作容器内部子组件的borderRadius
33. .borderRadius(20)
34. .clip(true)
35. .geometryTransition("picture")
36. // transition保证组件离场不被立即析构，可设置其他转场效果
37. .transition(TransitionEffect.OPACITY)
38. }
39. }
40. .onClick(() => {
41. this.getUIContext().animateTo({ duration: 1000 }, () => {
42. this.isShow = !this.isShow;
43. });
44. })
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/tNjzuKHbRvS8rijwpwSWwg/zh-cn_image_0000002558606894.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=531F92DBE9E3AB589620022CFD351D17C77EF5B7107098C9DE1A31D4FA412BA0)
