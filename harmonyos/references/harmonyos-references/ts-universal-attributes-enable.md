---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable
title: 禁用控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 禁用控制
category: harmonyos-references
scraped_at: 2026-04-29T13:51:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5ba7c13c9d0801c743235efe90ae6912ff2dae218148de7d010581db15e701fc
---

组件可交互状态下响应[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[按键事件](ts-universal-events-key.md)、[焦点事件](ts-universal-focus-event.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)、[手势事件](ts-gesture-settings.md)、[焦点轴事件](ts-universal-events-focus_axis.md)和[表冠事件](ts-universal-events-crown.md)。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

禁用控制属性仅在按下时生效，交互过程中更改enabled属性无效。

## enabled

PhonePC/2in1TabletTVWearable

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
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过enabled设置按钮可交互性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct EnabledExample {
5. build() {
6. Flex({ justifyContent: FlexAlign.SpaceAround }) {
7. // 点击时无响应
8. Button('disable').enabled(false).backgroundColor(0x317aff).opacity(0.4)
9. Button('enable').backgroundColor(0x317aff)
10. }
11. .width('100%')
12. .padding({ top: 5 })
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/-cWtFkLtSS-JrZC95z0BrA/zh-cn_image_0000002589245857.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055123Z&HW-CC-Expire=86400&HW-CC-Sign=1A63E8788FDE68F81DF5F383A12403345AAF211320AE1388CDBDB8F070CC6E22)
