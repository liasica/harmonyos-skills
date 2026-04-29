---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg
title: SVG标签说明
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > SVG标签说明
category: harmonyos-references
scraped_at: 2026-04-29T13:52:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:318bf6f7a473d942ae969c929cf90c720169e1e3faad65f81a44f303757f6685
---

SVG（Scalable Vector Graphics）是可缩放矢量图形，它是一种基于XML（可扩展标记语言）的图形格式，用于描述二维图形和图像。[Image](ts-basic-components-image.md)组件支持的SVG范围，为SVG1.1规范的部分功能。支持的标签以及属性如下：

## 基础形状

基础形状标签包括：<rect>、<circle>、<ellipse>、<line>、<polyline>、<polygon>和<path>。

说明

基础标签支持[通用属性](js-components-svg-common-attributes.md)：id、fill、fill-rule、fill-opacity、stroke、stroke-dasharray、stroke-dashoffset、stroke-opacity、stroke-width、stroke-linecap、stroke-linejoin、stroke-miterlimit、opacity、transform、clip-path、clip-rule，其中transform属性只支持平移。

从API version 21开始，当[Image](ts-basic-components-image.md)组件的[supportSvg2](ts-basic-components-image.md#supportsvg221)属性设置为true时，transform属性支持平移、旋转、缩放、倾斜、矩阵变换，详细请参考[SVG标签解析能力增强](ts-image-svg2-capabilities.md)。

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <rect> | 矩形 | x：x轴方向偏移分量；  y：y轴方向偏移分量；  width：宽度；  height：高度；  rx：圆角x轴半径；  ry：圆角y轴半径。 |
| <circle> | 圆形 | cx：圆心x轴坐标；  cy：圆心y轴坐标；  r：圆形半径。 |
| <ellipse> | 椭圆 | cx：x轴坐标；  cy：y轴坐标；  rx：x轴半径；  ry：y轴半径。 |
| <line> | 线 | x1：起点x轴坐标；  y1：起点y轴坐标；  x2：终点x轴坐标；  y2：终点y轴坐标。 |
| <polyline> | 折线 | points：顶点坐标。 |
| <polygon> | 多边形 | points：顶点坐标。 |
| <path> | 路径 | d：路径。 |

SVG基础形状标签与支持的通用属性的示例如下。

```
1. <!-- svg01.svg -->
2. <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" style="background:#f0f0f0">
3. <!-- 1. <rect> 矩形 -->
4. <rect x="50" y="50" width="100" height="60"
5. id="myRect"
6. fill="#4CAF50"
7. stroke="#333"
8. stroke-width="4"
9. stroke-dasharray="10,5"
10. stroke-linecap="round"
11. opacity="0.9"
12. transform="translate(1,0)"/>

14. <!-- 2. <circle> 圆形 -->
15. <circle cx="200" cy="100" r="50"
16. id="myCircle"
17. fill="none"
18. stroke="#FF5722"
19. stroke-width="6"
20. stroke-linejoin="bevel"
21. fill-opacity="0.7"
22. stroke-opacity="0.9"
23. transform="translate(30,0)"/>

25. <!-- 3. <ellipse> 椭圆 -->
26. <ellipse cx="350" cy="100" rx="70" ry="40"
27. id="myEllipse"
28. fill="#2196F3"
29. fill-rule="evenodd"
30. stroke="#000"
31. stroke-width="3"
32. opacity="0.8"
33. transform="translate(20,0)"/>

35. <!-- 4. <line> 直线 -->
36. <line x1="50" y1="200" x2="350" y2="200"
37. stroke="#9C27B0"
38. stroke-width="5"
39. stroke-dasharray="8,4"
40. stroke-linecap="square"
41. transform="translate(0,100)"/>

43. <!-- 5. <polyline> 折线（开放路径） -->
44. <polyline points="50,250 100,220 150,270 200,240 250,280"
45. fill="none"
46. stroke="#FFC107"
47. stroke-width="4"
48. stroke-linejoin="round"
49. opacity="0.9"
50. transform="translate(0,100)"/>

52. <!-- 6. <polygon> 多边形（闭合路径） -->
53. <polygon points="400,100 450,50 500,100 450,150"
54. id="myPolygon"
55. fill="#E91E63"
56. fill-rule="nonzero"
57. stroke="#333"
58. stroke-width="3"
59. stroke-dasharray="6,3"
60. fill-opacity="0.8"
61. transform="translate(-350,80)"/>

63. <!-- 7. <path> 路径（复杂图形） -->
64. <path d="M550,100 C600,50 700,50 750,100 S800,150 750,200 Z"
65. fill="#00BCD4"
66. fill-rule="evenodd"
67. stroke="#009688"
68. stroke-width="4"
69. stroke-opacity="0.7"
70. transform="translate(-300,90)"/>
71. </svg>
```

```
1. //xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. // $r('app.media.svg01')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.svg01'))
9. .objectFit(ImageFit.None)
10. .width('100%')
11. .height('100%')
12. }.width('100%').height('100%')
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/FOo_SGRlTx2-v8me-qLecg/zh-cn_image_0000002558606714.png?HW-CC-KV=V1&HW-CC-Date=20260429T055214Z&HW-CC-Expire=86400&HW-CC-Sign=8BADFB0B8DE544D42A0F2B24A7DCB6F202904E9AC857A7226BC25B16F4C5FDE2)

## 图形效果

### 滤镜

滤镜标签包括：<filter>、<feOffset>、<feGaussianBlur>、<feBlend>、<feComposite>、<feColorMatrix>、<feFlood>。其中，<filter>定义滤镜范围，其它标签定义滤镜效果。

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <filter> | 定义滤镜 | x：滤镜区域x轴偏移分量，默认值为0；  y：滤镜区域y轴偏移分量，默认值为0；  width：滤镜区域宽；  height：滤镜区域高。  **说明**：从API version 21开始，当Image组件的[supportSvg2](ts-basic-components-image.md#supportsvg221)属性设置为true时，默认值参考[filter参数异常时默认效果变更](ts-image-svg2-capabilities.md#filter参数异常时默认效果变更)。 |
| <feOffset> | 定义沿x、y方向偏移距离 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）;  result：经过滤镜处理之后的输出，可以作为下一个滤镜的输入，dx和dy。 |
| <feGaussianBlur> | 定义高斯模糊效果 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）;  result：经过滤镜处理之后的输出，可以作为下一个滤镜的输入，edgemode和stddeviation。 |
| <feBlend> | 定义两张输入图像混合模式 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）;  result：经过滤镜处理之后的输出，可以作为下一个滤镜的输入；  in2：第二图源（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result），mode。 |
| <feComposite> | 定义两张输入图像合成方式，  算法：result = k1 \* in \* in2 + k2 \* in + k3 \* in2 + k4 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）；  in2：第二图源（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result），operator( over | in | out | atop | xor | lighter | arithmetic )，k1，k2，k3，k4。 |
| <feColorMatrix> | 基于转换矩阵对颜色进行变换 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）；  result：经过滤镜处理之后的输出，可以作为下一个滤镜的输入；  type ( matrix | saturate | hueRotate)、 values。 |
| <feFlood> | 定义填充颜色和透明度 | in：滤镜原始输入（仅支持SourceGraphic、SourceAlpha、其它滤镜效果的result）；  result：经过滤镜处理之后的输出，可以作为下一个滤镜的输入；flood-color和flood-opacity。 |

### 遮罩

遮罩标签：<mask>

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <mask> | 定义遮罩 | x：遮罩区域x轴偏移分量；  y：遮罩区域y轴偏移分量；  width：遮罩区域宽；  height：遮罩区域高。  **说明**：从API version 21开始，当Image组件的[supportSvg2](ts-basic-components-image.md#supportsvg221)属性设置为true时，默认值参考[mask参数异常时默认效果变更](ts-image-svg2-capabilities.md#mask参数异常时默认效果变更)。 |

### 裁剪

裁剪标签：<clippath>

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <clippath> | 定义一条剪切路径 | x：裁剪区域x轴偏移分量；  y：裁剪区域y轴偏移分量；  width：裁剪区域宽；  height：裁剪区域高。 |

### 图案

图案标签：<pattern>

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <pattern> | 定义填充图案 | x：填充区域x轴偏移分量；  y：填充区域y轴偏移分量；  width：填充区域宽；  height：填充区域高。 |

### 渐变色

渐变色相关的标签包括：<linearGradient>、<radialGradient>、<stop>

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <linearGradient> | 线性渐变 | x1、y1、x2、y2 |
| <radialGradient> | 放射渐变 | fx、fy、cx、cy、r |
| <stop> | 色阶 | offset、stop-color |

## 静态图片

图片标签：<image>

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <image> | 用于图像显示 | x：图像x轴偏移；  y：图像y轴偏移；  width：图像宽；  height：图像高；  href：目标图片(支持：jpg、jpeg、png、bmp、webp、heic、base64，不支持svg)。 |

## 动画

动画标签：<animate>、<animateTransform>

说明

当前仅支持单个元素的属性动画或者变形动画，不支持元素间动画嵌套。

| 元素 | 说明 | 特有属性 |
| --- | --- | --- |
| <animate> | 定义元素属性动画 | attributeName：定义动画属性，取值：( cx | cy | r | fill | stroke | fill-opacity | stroke-opacity | stroke-miterlimit )；  begin：定义动画起始时间；  dur：定义动画持续时间；  from：定义起始值；  to：定义结束值；  fill：定义动画结尾状态；  calcMode：定义插值；  keyTimes：设置关键帧动画的开始时间，值为0~1之间的数值用分号隔开，比如0;0.3;0.8;1。keyTimes、keySplines、values组合设置关键帧动画。keyTimes和values的个数保持一致。keySplines个数为keyTimes个数减一。  values：设置一组动画的变化值。格式为value1;value2;value3。  keySplines：与keyTimes相关联的一组贝塞尔控制点。定义每个关键帧的贝塞尔曲线，曲线之间用分号隔开。曲线内的两个控制点格式为x1 y1 x2 y2。比如0.5 0 0.5 1; 0.5 0 0.5 1;0.5 0 0.5 1 |
| <animateTransform> | 定义元素变形动画 | attributeName：定义动画属性，取值：transform；  type：属性定义转换类型取值：( translate | scale | rotate | skewX | skewY )；  begin：定义动画起始时间；  dur：定义动画持续时间；  from：定义起始值；  to：定义结束值；  fill：定义动画结尾状态；  calcMode：定义插值；  keyTimes：设置关键帧动画的开始时间，值为0~1之间的数值用分号隔开，比如0;0.3;0.8;1。keyTimes、keySplines、values组合设置关键帧动画。keyTimes和values的个数保持一致。keySplines个数为keyTimes个数减一。  values：设置一组动画的变化值。格式为value1;value2;value3。  keySplines：与keyTimes相关联的一组贝塞尔控制点。定义每个关键帧的贝塞尔曲线，曲线之间用分号隔开。曲线内的两个控制点格式为x1 y1 x2 y2。比如0.5 0 0.5 1; 0.5 0 0.5 1;0.5 0 0.5 1 |

## 其它

除了标识图形图像效果的标签，还支持分组等标签，分别有<svg>、<g>、<use>和<defs>。

说明

当前支持的颜色值格式包括#rgb、#rrggbb、rgb()、rgba()，以及常用颜色关键字（如red、black、blue等）。

| 元素 | 说明 | 特有属性 | 通用属性 |
| --- | --- | --- | --- |
| <svg> | 容器，定义个svg片段 | x：x轴偏移分量；  y：y轴偏移分量；  width：宽度；  height：高度；  viewBox：视口 | fill、fill-rule、fill-opacity、stroke、stroke-dasharray、stroke-dashoffset、stroke-opacity、stroke-width、stroke-linecap、stroke-linejoin、stroke-miterlimit、transform |
| <g> | 分组 | x：x轴偏移分量；  y：y轴偏移分量；  width：宽度；  height：高度 | fill、fill-rule、fill-opacity、stroke、stroke-dasharray、stroke-dashoffset、stroke-opacity、stroke-width、stroke-linecap、stroke-linejoin、stroke-miterlimit、transform |
| <use> | 复用已有元素 | x：x轴偏移分量；  y：y轴偏移分量；  href：目标元素 | fill、fill-rule、fill-opacity、stroke、stroke-dasharray、stroke-dashoffset、stroke-opacity、stroke-width、stroke-linecap、stroke-linejoin、stroke-miterlimit、transform |
| <defs> | 定义可复用对象 | 无特有属性 | fill、fill-rule、fill-opacity、stroke、stroke-dasharray、stroke-dashoffset、stroke-opacity、stroke-width、stroke-linecap、stroke-linejoin、stroke-miterlimit、transform |
