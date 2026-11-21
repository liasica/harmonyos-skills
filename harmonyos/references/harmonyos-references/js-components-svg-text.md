---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text
title: text
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > text
category: harmonyos-references
scraped_at: 2026-11-21T09:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c935ad345e9ba6e016ea50b44c905eab9075dfece27afff3f10e8ac201e567a3
---

文本，用于呈现一段信息。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 文本的展示内容需要写在元素标签内，可嵌套tspan子元素标签分段，可嵌套textPath子元素标签按指定路径绘制。
* 只支持被父元素标签svg嵌套。
* 只支持默认字体sans-serif。

## 权限列表

无

## 子组件

支持[tspan](js-components-svg-tspan.md)、[textPath](js-components-svg-textpath.md)、[animate](js-components-svg-animate.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| x | <length>|<percentage> | 0 | 否 | 设置组件左上角x轴坐标。 |
| y | <length>|<percentage> | 0 | 否 | 设置组件左上角y轴坐标。 |
| dx | <length>|<percentage> | 0 | 否 | 设置文本x轴偏移。 |
| dy | <length>|<percentage> | 0 | 否 | 设置文本y轴偏移。 |
| rotate | number | 0 | 否 | 文本以左下角为圆心旋转角度，正数顺时针，负数逆时针。 |
| font-size | <length> | 30px | 否 | 设置文本的尺寸。 |
| fill | <color> | black | 否 | 文本填充颜色。 |
| fill-opacity | number | 1.0 | 否 | 文本填充透明度。 |
| opacity | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。 |
| stroke | <color> | black | 否 | 绘制文本描边并指定颜色。 |
| stroke-width | number | 1 | 否 | 文本描边宽度。  默认单位：px |
| stroke-opacity | number | 1.0 | 否 | 文本描边透明度。 |

## 示例

```css
/* xxx.css */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 1000px;
    width: 1080px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20px" y="0px" font-size="30" fill="blue">test x|y</text>
    <text x="150" y="15" font-size="30" fill="blue">test x|y</text>
    <text x="300" y="30" font-size="30" fill="blue" opacity="0.1">test opacity</text>
    <text dx="20" y="30" dy="50" fill="blue" font-size="30">test dx|dy|fill|font-size</text>
    <text x="20" y="150" fill="blue" font-size="30" fill-opacity="0.2">test fill-opacity</text>
    <text x="20" y="200" fill="red" font-size="40">test 0123456789</text>
    <text x="20" y="250" fill="red" font-size="40" fill-opacity="0.2">test 中文</text>
    <text x="20" y="300" rotate="30" fill="red" font-size="40">test rotate</text>
    <text x="20" y="350" fill="blue" font-size="40" stroke="red" stroke-width="2">test stroke</text>
    <text x="20" y="400" fill="white" font-size="40" stroke="red" stroke-width="2" stroke-opacity="0.5">test stroke-opacity</text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-MGG09OFRfSOF0NIaEJjIA/zh-cn_image_0000002821759453.png?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F3594590EA4D202AFFBA5A514CE61A68E13234F989BE7960687EC24EC61F021)

属性动画示例

```css
/* xxx.css  */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 3000px;
    width: 1080px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text y="50" font-size="30" fill="blue">
        text attribute x|opacity|rotate
      <animate attributeName="x" from="100" by="400" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/eQcWtpaTQ-2EGm7fKdc_yA/zh-cn_image_0000002793039524.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=D029A61FA2EC519C6EE507C91C8C3E6BF3CE8FB27D8AB391DDBA0C91BB7F1A8F)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="200" fill="blue">
      text attribute font-size
      <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite">
      </animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/cu_y3Bh0RI2wB37Ji1Auig/zh-cn_image_0000002792879550.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=14379AD85998985C3DB20E5436C533FDB6345247ECD9B0E8ABDC0349F838DF58)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="250" font-size="25" fill="blue" stroke="red">
      text attribute stroke
      <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
    </text>
    <text x="300" y="250" font-size="25" fill="white" stroke="red">
      text attribute stroke-width-opacity
      <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/dRxnHEs5S9yHcQHvcfvOhA/zh-cn_image_0000002821839457.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B62DAA1F09FB1B3ADE35AA227F3361761F951E7A3BB6738AAC05AEE1FC01623)
