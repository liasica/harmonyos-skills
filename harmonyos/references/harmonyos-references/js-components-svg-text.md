---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text
title: text
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > text
category: harmonyos-references
scraped_at: 2026-04-28T08:03:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1c34f990f016ae975753afd172354550eadcd7fac86a2200c92c19d4582c1f75
---

文本，用于呈现一段信息。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 文本的展示内容需要写在元素标签内，可嵌套tspan子元素标签分段，可嵌套textPath子元素标签按指定路径绘制。
* 只支持被父元素标签svg嵌套。
* 只支持默认字体sans-serif。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持[tspan](js-components-svg-tspan.md)、[textPath](js-components-svg-textpath.md)、[animate](js-components-svg-animate.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

PhonePC/2in1TabletTVWearable

支持以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| x | <length>|<percentage> | 0 | 否 | 设置组件左上角x轴坐标。 |
| y | <length>|<percentage> | 0 | 否 | 设置组件左上角y轴坐标。 |
| dx | <length>|<percentage> | 0 | 否 | 设置文本x轴偏移。 |
| dy | <length>|<percentage> | 0 | 否 | 设置文本y轴偏移。 |
| rotate | number | 0 | 否 | 字体以左下角为圆心旋转角度，正数顺时针，负数逆时针。 |
| font-size | <length> | 30px | 否 | 设置文本的尺寸。 |
| fill | <color> | black | 否 | 字体填充颜色。 |
| fill-opacity | number | 1.0 | 否 | 字体填充透明度。 |
| opacity | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。 |
| stroke | <color> | black | 否 | 绘制字体边框并指定颜色。 |
| stroke-width | number | 1 | 否 | 字体边框宽度。  默认单位：px |
| stroke-opacity | number | 1.0 | 否 | 字体边框透明度。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. /* xxx.css */
2. .container {
3. flex-direction: row;
4. justify-content: flex-start;
5. align-items: flex-start;
6. height: 1000px;
7. width: 1080px;
8. }
```

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text x="20px" y="0px" font-size="30" fill="blue">test x|y</text>
5. <text x="150" y="15" font-size="30" fill="blue">test x|y</text>
6. <text x="300" y="30" font-size="30" fill="blue" opacity="0.1">test opacity</text>
7. <text dx="20" y="30" dy="50" fill="blue" font-size="30">test dx|dy|fill|font-size</text>
8. <text x="20" y="150" fill="blue" font-size="30" fill-opacity="0.2">test fill-opacity</text>
9. <text x="20" y="200" fill="red" font-size="40">test 0123456789</text>
10. <text x="20" y="250" fill="red" font-size="40" fill-opacity="0.2">test 中文</text>
11. <text x="20" y="300" rotate="30" fill="red" font-size="40">test rotate</text>
12. <text x="20" y="350" fill="blue" font-size="40" stroke="red" stroke-width="2">test stroke</text>
13. <text x="20" y="400" fill="white" font-size="40" stroke="red" stroke-width="2" stroke-opacity="0.5">test stroke-opacity</text>
14. </svg>
15. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/dIZ9qe8nTsmokzDEivxm5A/zh-cn_image_0000002552960244.png?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=A74AE15FE38C43711672CCD7B09A86469C7C913B525A4997FDE64FAD94554C1B)

属性动画示例

```
1. /* xxx.css  */
2. .container {
3. flex-direction: row;
4. justify-content: flex-start;
5. align-items: flex-start;
6. height: 3000px;
7. width: 1080px;
8. }
```

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text y="50" font-size="30" fill="blue">
5. text attribute x|opacity|rotate
6. <animate attributeName="x" from="100" by="400" dur="3s" repeatCount="indefinite"></animate>
7. <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
8. <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
9. </text>
10. </svg>
11. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/J5ZEOJ2ISo-KqtI8Onh7CQ/zh-cn_image_0000002583480245.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=ACE8EB66460C6B6B9FF3F1F18F5B20629F65431EDEEE8C7B07587BDAFF10B032)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text x="20" y="200" fill="blue">
5. text attribute font-size
6. <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite">
7. </animate>
8. </text>
9. </svg>
10. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/14o2r7psSbODi2PBpY5LWQ/zh-cn_image_0000002552800596.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=327112FADCB741DC2A5B200BAD64F7353022B262F3E752D7F5D830A923ACB468)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text x="20" y="250" font-size="25" fill="blue" stroke="red">
5. text attribute stroke
6. <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
7. </text>
8. <text x="300" y="250" font-size="25" fill="white" stroke="red">
9. text attribute stroke-width-opacity
10. <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
11. <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
12. </text>
13. </svg>
14. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/NKqqWaZySjmY5hmzdapNeQ/zh-cn_image_0000002583440291.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=0D744AD99720C1E7957CFEC91C831FF4FB473C672226BAE741055597EA3FC30B)
