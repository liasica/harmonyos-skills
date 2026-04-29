---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hover-effect
title: 悬浮态效果
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 悬浮态效果
category: harmonyos-references
scraped_at: 2026-04-29T13:51:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2553f4de45b31635c3f65dce92888abf136e08809b8f381ac9c02555e0e57d83
---

设置组件的鼠标悬浮态显示效果。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## hoverEffect

PhonePC/2in1TabletTVWearable

hoverEffect(value: HoverEffect): T

设置组件的鼠标悬浮态显示效果。当未设置hoverEffect时，组件默认鼠标悬浮态效果为HoverEffect.Auto。对于应用了悬浮态效果的组件，当鼠标悬浮于组件上并按下时，悬浮态效果会消失；当鼠标松开时，悬浮态效果会恢复。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HoverEffect](ts-appendix-enums.md#hovereffect8) | 是 | 设置当前组件悬浮态下的悬浮效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过hoverEffect设置组件的鼠标悬浮态显示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct HoverExample {
5. @State isHoverVal: boolean = false

7. build() {
8. Column({ space: 5 }) {
9. Column({ space: 5 }) {
10. Text('Scale').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 80 })
11. Column()
12. .width('80%')
13. .height(200)
14. .backgroundColor(Color.Gray)
15. .position({ x: 40, y: 120 })
16. .hoverEffect(HoverEffect.Scale)
17. .onHover((isHover?: boolean) => {
18. console.info(`Scale isHover: ${isHover}`)
19. this.isHoverVal = isHover as boolean
20. })

22. Text('Board').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 380 })
23. Column()
24. .width('80%')
25. .height(200)
26. .backgroundColor(Color.Yellow)
27. .hoverEffect(HoverEffect.Highlight)
28. .position({ x: 40, y: 420 })
29. .onHover((isHover?: boolean) => {
30. console.info(`Highlight isHover: ${isHover}`)
31. this.isHoverVal = isHover as boolean
32. })
33. }
34. .hoverEffect(HoverEffect.None)
35. .width('100%')
36. .height('100%')
37. .border({ width: 1 })
38. .onHover((isHover?: boolean) => {
39. console.info('HoverEffect.None')
40. this.isHoverVal = isHover as boolean
41. })
42. }
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/oOomFIE0T26SLVI_iWB4kg/zh-cn_image_0000002558766064.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055122Z&HW-CC-Expire=86400&HW-CC-Sign=92AFCC3195AFB19EB4B8F355758865F990BC47673F693B0C1872988B613A701D)
