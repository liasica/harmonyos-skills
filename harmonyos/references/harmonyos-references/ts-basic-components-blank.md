---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank
title: Blank
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 空白与分隔 > Blank
category: harmonyos-references
scraped_at: 2026-09-05T06:17:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62a0dec7dd122d94d49d8140a3994d4ce2e58cf24a2d15bf0e0e757fa8b614ff
---

空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。仅当父组件为[Row](ts-container-row.md)/[Column](ts-container-column.md)/[Flex](ts-container-flex.md)时生效。

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

不支持设置子组件。

## 接口

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

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

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

支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（占满空余空间）

Blank组件在横竖屏占满空余空间效果。

```ts
// xxx.ets
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.width('100%').backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })
    }.backgroundColor(0xEFEFEF).padding(20)
  }
}
```

竖屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Os6h_ipiSmSPOrtsXZlnaw/zh-cn_image_0000002742125259.gif)

横屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nxJTCFLNSN6cUTSd18Sh_g/zh-cn_image_0000002712246352.gif)

### 示例2（填充固定宽度）

Blank组件的父组件未设置宽度时，min参数的使用效果。

```ts
// xxx.ets
@Entry
@Component
struct BlankExample {
  build() {
    Column({ space: 20 }) {
      // Blank父组件不设置宽度时，Blank失效，可以通过设置min最小宽度填充固定宽度
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank().color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

      Row() {
        Text('Bluetooth').fontSize(18)
        // 设置最小宽度为160
        Blank('160').color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

Blank父组件未设置宽度时，子组件间无空白填充，使用min参数设置填充尺寸

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/X5DZFAAPQ4a53Uqmwq0_Eg/zh-cn_image_0000002742005301.png)
