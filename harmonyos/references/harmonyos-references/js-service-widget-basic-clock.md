---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-clock
title: clock
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 基础组件 > clock
category: harmonyos-references
scraped_at: 2026-04-29T13:54:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c073b21edcc99f8bbb46ebbe0b50caf1a4afd3c93ff83c827968bc46e57dd794
---

时钟组件，用于提供时钟表盘界面。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| clockconfig | ClockConfig | - | 是 | Clock的图片资源和样式设置，包括日间时段（6:00-18:00）和夜间时段（18:00-次日6:00）两套资源和样式设置。  其中每套资源和样式包括表盘资源、时针指针资源、分针指针资源、秒针指针资源四张图和相应时间段的表盘数字颜色。  日间资源为必填项。夜间资源可不填，不填时默认会复用日间资源用作夜间时段的显示。  仅支持动态更新整个Object，不支持动态更新Object里的内容。  建议使用PNG资源作为Clock组件的图片资源。  不支持使用SVG资源作为Clock组件的图片资源。 |
| showdigit | boolean | true | 否 | 是否由Clock组件绘制表盘数字。  true表示由Clock组件绘制表盘数字，false表示不由Clock组件绘制表盘数字。  该属性为true时，请留意clockconfig中digitRadiusRatio和digitSizeRatio参数与表盘的匹配情况。  由Clock组件绘制的表盘数字支持国际化。 |
| hourswest | number | - | 否 | 时钟的时区偏移值，时区为标准时区减去hourswest。  有效范围为[-12, 12]，其中负值范围表示东时区，比如东八区对应的是-8。不设置默认采用系统时间所在的时区。 |

**表1** ClockConfig

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| face | <string> | - | 是 | 日间时段的表盘资源路径。  表盘资源须为包含时钟刻度的正方形图片，表盘区域（圆形）为该图片的内切圆或内切圆的同心圆。如果表盘区域为表盘资源内切圆的同心圆的话，请相应调整digitRadiusRatio和digitSizeRatio参数。 |
| hourHand | <string> | - | 是 | 日间时段的时针资源路径。  - 时针图片的高度须与表盘资源高度相同。  - 时针图片的宽高比建议在0.062。  - 时针图片上指针的旋转中心须处于时针图片的中心（对角线交点）。  - 夜间时段的时针资源请调整hourHandNight参数。 |
| minuteHand | <string> | - | 是 | 日间时段的分针资源路径。  - 分针图片的高度须与表盘资源高度相同。  - 分针图片的宽高比建议在0.062。  - 分针图片上指针的旋转中心须处于分针图片的中心（对角线交点）。  - 夜间时段的分针资源请调整minuteHandNight参数。 |
| secondHand | <string> | - | 是 | 日间时段的秒针资源路径。  - 秒针图片的高度须与表盘资源高度相同。  - 秒针图片的宽高比建议在0.062。  - 秒针图片上指针的旋转中心须处于秒针图片的中心（对角线交点）。  - 夜间时段的秒针资源请调整secondHandNightSrc参数。 |
| digitColor | <color> | #FF000000 | 否 | 日间时段（6:00-18:00）的表盘文本颜色。 |
| digitColorNight | <color> | 与digitColor保持一致 | 否 | 夜间时段（18:00-次日6:00）的表盘文本颜色。  - 该属性未设置时，取digitColor的值作为digitColorNight的值（digitColor被设置时，取digitColor被设置的值）。  - 请注意缺省状态下使用digitColor的值作为digitColorNight的值时，夜间时段表盘文本颜色与夜间时段表盘背景（faceNight）的颜色配合问题。 |
| faceNight | <string> | - | 否 | 夜间时段的表盘资源路径。  未设置时使用face的资源路径作为夜间时段的表盘资源路径。 |
| hourHandNight | <string> | - | 否 | 夜间时段的时针资源路径。  未设置时使用hourHand的资源路径作为夜间时段的时针资源路径。 |
| minuteHandNight | <string> | - | 否 | 夜间时段的分针资源路径。  未设置时使用minuteHand的资源路径作为夜间时段的分针资源路径。 |
| secondHandNight | <string> | - | 否 | 夜间时段的秒针资源路径。  未设置时使用secondHand的资源路径作为夜间时段的秒针资源路径。 |
| digitRadiusRatio | number | 0.7 | 否 | 表盘数字中心到表盘中心距离 / 表盘资源边长的一半。  - 有效范围为(0, 1]。  - 该参数用于计算表盘数字在表盘上距离圆心的位置。  - 该参数可以保证同一套表盘资源在不同组件尺寸下都有同样的相对位置，而不需要针对每个组件尺寸都重新调整数字位置。  - 该参数设为1时数字会有部分区域超出表盘，建议结合表盘区域合理设置digitRadiusRatio。 |
| digitSizeRatio | number | 0.08 | 否 | 表盘数字尺寸/表盘资源边长。  - 有效范围为(0, 0.142]。  - 该参数用于计算表盘数字相对表盘尺寸的大小。  - 该参数可以保证同一套表盘资源在不同组件尺寸下都有同样的相对大小，而不需要针对每个组件尺寸都重新调整字号。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/nX51wP3QTXCowae19e83kQ/zh-cn_image_0000002558766956.png?HW-CC-KV=V1&HW-CC-Date=20260429T055401Z&HW-CC-Expire=86400&HW-CC-Sign=1714881B852455F40244BC8D7F4208E91E1FE522EDE573ACE76382C50C07F5EF)

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-service-widget-common-styles.md)之外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| font-family | <string> | sans-serif | 否 | 表盘数字的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过2.1.6 自定义字体样式指定的字体，会被选中作为文本的字体。 |

说明

clock组件会保持显示区域的宽高比为1，最终正方形显示区域的边长为min(width, height)，在width \* height的组件区域中居中显示。

## 事件

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| hour | {hour: number} | 每个整点触发该事件 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="row">
4. <clock class="clk" style="font-family:Courier;" hourswest="-8" clockconfig="{{clockconfig}}">
5. </clock>
6. <clock class="clk" style="font-family:Courier;" hourswest="4" clockconfig="{{clockconfig}}">
7. </clock>
8. </div>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction:column;
4. align-items:center;
5. }
6. .clk {
7. width:350px;
8. height:350px;
9. }
10. .row {
11. flex-direction:row;
12. align-items:center;
13. justify-content: space-around;
14. border-radius: 40px;
15. padding-top: 20px;
16. padding-bottom: 20px;
17. background-color: #4169E1;
18. }
```

```
1. {
2. "data": {
3. "clockconfig": {
4. "digitRadiusRatio": 0.7,
5. "digitSizeRatio": 0.08,
6. "face": "common/clock_widget.png",
7. "hourHand": "common/clock_widget_hour.png",
8. "minuteHand": "common/clock_widget_minute.png",
9. "secondHand": "common/clock_widget_second.png",
10. "faceNight": "common/black_clock_widget.png",
11. "hourHandNight": "common/black_clock_widget_hour.png",
12. "minuteHandNight": "common/black_clock_widget_minute.png",
13. "digitColor": "#000000",
14. "digitColorNight": "#FFFFFF"
15. }
16. }
17. }
```

**2\*4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/4OZJxjC3RlSCR06p-Tml6Q/zh-cn_image_0000002558607296.png?HW-CC-KV=V1&HW-CC-Date=20260429T055401Z&HW-CC-Expire=86400&HW-CC-Sign=5A492BB7B7448D3D0639383DB975DC80C6DA0B0E298F5FEC4269577A43F37F99)
