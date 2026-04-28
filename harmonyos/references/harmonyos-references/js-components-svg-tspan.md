---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-tspan
title: tspan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > tspan
category: harmonyos-references
scraped_at: 2026-04-28T08:03:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3360042c8d2af93575c1fe1c0c58f79a5dbd9cced11e563ea91c897d1c69873d
---

添加文本样式。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 文本的展示内容需要写在元素标签内，可嵌套子元素标签tspan分段。
* 文本分段，只支持被父元素标签svg嵌套。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持[tspan](js-components-svg-tspan.md)。

支持以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| x | <length>|<percentage> | 0 | 否 | 设置组件左上角x轴坐标。 |
| y | <length>|<percentage> | 0 | 否 | 设置组件左上角y轴坐标。作为textpath子组件时失效。 |
| dx | <length>|<percentage> | 0 | 否 | 设置文本x轴偏移。 |
| dy | <length>|<percentage> | 0 | 否 | 设置文本y轴偏移。作为textpath子组件时失效。 |
| rotate | number | 0 | 否 | 字体以左下角为圆心旋转角度，正数顺时针，负数逆时针。 |
| font-size | <length> | 30px | 否 | 设置文本的尺寸。 |
| fill | <color> | black | 否 | 字体填充颜色。 |
| opacity | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。 |
| fill-opacity | number | 1.0 | 否 | 字体填充透明度。 |
| stroke | <color> | black | 否 | 绘制字体边框并指定颜色。 |
| stroke-width | number | 1 | 否 | 字体边框宽度。  默认单位：px |
| stroke-opacity | number | 1.0 | 否 | 字体边框透明度。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg >
4. <text x="20" y="500" fill="#D2691E" font-size="20">
5. zero text.
6. <tspan>first span.</tspan>
7. <tspan fill="red" font-size="35">second span.</tspan>
8. <tspan fill="#D2691E" font-size="40" rotate="10">third span.</tspan>
9. </text>
10. <text x="20" y="550" fill="#D2691E" font-size="20">
11. <tspan dx="-5" fill-opacity="0.2">first span.</tspan>
12. <tspan dx="5" fill="red" font-size="25" fill-opacity="0.4">second span.</tspan>
13. <tspan dy="-5" fill="#D2691E" font-size="35" rotate="-10" fill-opacity="0.6">third span.</tspan>
14. <tspan fill="#blue" font-size="40" rotate="10" fill-opacity="0.8" stroke="#00FF00" stroke-width="1px">forth span.</tspan>
15. </text>
16. </svg>
17. </div>
```

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/O9TinI-YRJq2YAn4cUraaw/zh-cn_image_0000002552960246.png?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=CF7EA6B347FE667E0D3BE260018D333BE89B77D03E29ECEFCEABE80A3AD5E935)

属性动画示例

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text y="300" font-size="30" fill="blue">
5. <tspan>
6. tspan attribute x|opacity|rotate
7. <animate attributeName="x" from="-100" to="400" dur="3s" repeatCount="indefinite"></animate>
8. <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
9. <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
10. </tspan>
11. </text>

13. <text y="350" font-size="30" fill="blue">
14. <tspan>
15. tspan attribute dx
16. <animate attributeName="dx" from="-100" to="400" dur="3s" repeatCount="indefinite"></animate>
17. </tspan>
18. </text>
19. </svg>
20. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: row;
4. justify-content: flex-start;
5. align-items: flex-start;
6. height: 3000px;
7. width: 1080px;
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/xXmYUQIDSBytY0HjFD2hsA/zh-cn_image_0000002583480247.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=0384DE3C23CFD1387DD9430D394F10C3E0784723D644B5D6D6091FFCBD3EC90F)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text>
5. <tspan x="0" y="550" font-size="30">
6. tspan attribute fill|fill-opacity
7. <animate attributeName="fill" from="blue" to="red" dur="3s" repeatCount="indefinite"></animate>
8. <animate attributeName="fill-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
9. </tspan>
10. </text>
11. </svg>
12. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/E9YM-Xa8S5q9ZXKkPu2jCQ/zh-cn_image_0000002552800598.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=CDCF33EB298C0923F6FD3E701671E5021CB8482847811B986F5172EA41887339)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text>
5. <tspan x="20" y="600" fill="red">
6. tspan attribute font-size
7. <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite"></animate>
8. </tspan>
9. </text>
10. </svg>
11. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/FI-W1COVRGOVqF_N2cG4cg/zh-cn_image_0000002583440293.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=7BF82A91F39898B8F4556EF42BD92F897B383B93F266F0C98D1131053684E432)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text>
5. <tspan x="20" y="650" font-size="25" fill="blue" stroke="red">
6. tspan attribute stroke
7. <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
8. </tspan>
9. </text>
10. <text>
11. <tspan x="300" y="650" font-size="25" fill="white" stroke="red">
12. tspan attribute stroke-width-opacity
13. <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
14. <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
15. </tspan>
16. </text>
17. </svg>
18. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/UWU1msWpTuWNdVaJucbOuA/zh-cn_image_0000002552960248.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=3CB6CCA3AD77120BAB7134D317D64ACA0431AEEC12F947F24CD814AD9B65B1D0)
