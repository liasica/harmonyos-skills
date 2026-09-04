---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable
title: 禁用控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 禁用控制
category: harmonyos-references
scraped_at: 2026-09-05T06:17:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:36f978fb955981ff5080bd011b624def935ac81b81b443fc483a90c5e491a3f2
---

禁用控制用于设置组件是否可交互。组件可交互状态下可以响应[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[按键事件](ts-universal-events-key.md)、[焦点事件](ts-universal-focus-event.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)、[手势事件](ts-gesture-settings.md)、[焦点轴事件](ts-universal-events-focus_axis.md)和[表冠事件](ts-universal-events-crown.md)；组件不可交互状态下不响应上述操作，适用于需要临时阻止用户交互的场景。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

禁用控制属性仅在按下时生效，交互过程中更改enabled属性无效。

## enabled

enabled(value: boolean): T

设置组件是否可交互。当未设置enabled时，组件默认可交互。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 值为true表示组件可交互，响应点击等操作。  值为false表示组件不可交互，不响应点击等操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，支持链式调用。 |

## 示例

该示例通过enabled设置按钮是否可交互。

```ts
// xxx.ets
@Entry
@Component
struct EnabledExample {
  build() {
    Flex({ justifyContent: FlexAlign.SpaceAround }) {
      // 点击时无响应
      Button('disable').enabled(false).backgroundColor(0x317aff).opacity(0.4)
      Button('enable').backgroundColor(0x317aff)
    }
    .width('100%')
    .padding({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/2XwdhfvzTme06YvJaa8dlA/zh-cn_image_0000002712245908.gif)
