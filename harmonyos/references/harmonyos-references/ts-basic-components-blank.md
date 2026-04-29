---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank
title: Blank
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 空白与分隔 > Blank
category: harmonyos-references
scraped_at: 2026-04-29T13:52:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a066a6628166d35c5b808cf5d41acbad225bbbd6e510250b44d4d9d10ed3c462
---

空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。仅当父组件为[Row](ts-container-row.md)/[Column](ts-container-column.md)/[Flex](ts-container-flex.md)时生效。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持设置子组件。

## 接口

PhonePC/2in1TabletTVWearable

Blank(min?: number | string)

创建空白填充组件。

从API version 10开始：

* Blank在父容器[Row](ts-container-row.md)、[Column](ts-container-column.md)、[Flex](ts-container-flex.md)主轴方向上未设置大小时会自动拉伸、压缩，设置了大小或容器自适应子节点大小时不会自动拉伸、压缩。
* Blank设置主轴方向大小（size）与min时约束关系为max(min, size)。
* Blank在父容器交叉轴上设置大小时不会撑满父容器交叉轴，交叉轴不设置大小时alignSelf默认值为ItemAlign.Stretch，会撑满容器交叉轴。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| min | number | string | 否 | 空白填充组件在容器主轴上的最小大小。  默认值：0，number类型单位为vp，string类型可以显式指定[像素单位](ts-pixel-units.md)，如'10px'。不指定像素单位时，默认单位vp，如'10'，等同于10vp。  非法值：按默认值处理。  **说明：**  不支持设置百分比。负值使用默认值。当最小值大于容器可用空间时，使用最小值作为自身大小并超出容器。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(value: ResourceColor)

设置空白填充的填充颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 空白填充的填充颜色。  默认值：Color.Transparent  非法值：按默认值处理。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（占满空余空间）

Blank组件在横竖屏占满空余空间效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BlankExample {
5. build() {
6. Column() {
7. Row() {
8. Text('Bluetooth').fontSize(18)
9. Blank()
10. Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
11. }.width('100%').backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })
12. }.backgroundColor(0xEFEFEF).padding(20)
13. }
14. }
```

竖屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/iUjUOKGzQEiKskteFvuNuQ/zh-cn_image_0000002589326315.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055222Z&HW-CC-Expire=86400&HW-CC-Sign=A723E00ED9BA7EEDB991698404FEFFA2AFCCCDEB591D29DD8C8EA29C283EA87C)

横屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/sTeeyj2pQKOvJiVRY9yrVQ/zh-cn_image_0000002589246257.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055222Z&HW-CC-Expire=86400&HW-CC-Sign=5E871E44338A6C921D2B70330526D27C4E325764FACF395B3CBE4202A44695AB)

### 示例2（填充固定宽度）

Blank组件的父组件未设置宽度时，min参数的使用效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BlankExample {
5. build() {
6. Column({ space: 20 }) {
7. // Blank父组件不设置宽度时，Blank失效，可以通过设置min最小宽度填充固定宽度
8. Row() {
9. Text('Bluetooth').fontSize(18)
10. Blank().color(Color.Yellow)
11. Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
12. }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

14. Row() {
15. Text('Bluetooth').fontSize(18)
16. // 设置最小宽度为160
17. Blank('160').color(Color.Yellow)
18. Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
19. }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

21. }.backgroundColor(0xEFEFEF).padding(20).width('100%')
22. }
23. }
```

Blank父组件未设置宽度时，子组件间无空白填充，使用min参数设置填充尺寸

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/rd-TCwUiRtWKbNwiOqLGsA/zh-cn_image_0000002558766450.png?HW-CC-KV=V1&HW-CC-Date=20260429T055222Z&HW-CC-Expire=86400&HW-CC-Sign=F639440C5AD0EE9B041098D64921391489D3A8F1E7064E438FC5C50DAEB9BD31)
