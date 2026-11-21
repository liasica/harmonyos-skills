---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-tspan
title: tspan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > tspan
category: harmonyos-references
scraped_at: 2026-11-21T09:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6f8a074a510200997d47ff50765bcb3c481b1e6661cae97242b6eece7e71ad68
---

添加文本样式。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 文本的展示内容需要写在元素标签内，可嵌套子元素标签tspan分段。
* 文本分段，只支持被父元素标签text嵌套。

## 权限列表

无

## 子组件

支持[tspan](js-components-svg-tspan.md)。

## 属性

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

```html
<!-- xxx.hml -->
<div class="container">
  <svg >
    <text x="20" y="500" fill="#D2691E" font-size="20">
      zero text.
      <tspan>first span.</tspan>
      <tspan fill="red" font-size="35">second span.</tspan>
      <tspan fill="#D2691E" font-size="40" rotate="10">third span.</tspan>
    </text>
    <text x="20" y="550" fill="#D2691E" font-size="20">
      <tspan dx="-5" fill-opacity="0.2">first span.</tspan>
      <tspan dx="5" fill="red" font-size="25" fill-opacity="0.4">second span.</tspan>
      <tspan dy="-5" fill="#D2691E" font-size="35" rotate="-10" fill-opacity="0.6">third span.</tspan>
      <tspan fill="blue" font-size="40" rotate="10" fill-opacity="0.8" stroke="#00FF00" stroke-width="1px">fourth span.</tspan>
    </text>
  </svg>
</div>
```

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/GqhYcmnHT4CbhpIngbtW_Q/zh-cn_image_0000002821759455.png?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEAE270E7FCD558443DBAB5BFF0F3B26FE5895D4C6829237ACFB5D928DA52AF2)

属性动画示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text y="300" font-size="30" fill="blue">
      <tspan>
        tspan attribute x|opacity|rotate
        <animate attributeName="x" from="-100" to="400" dur="3s" repeatCount="indefinite"></animate>
        <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
        <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
      </tspan>
    </text>

    <text y="350" font-size="30" fill="blue">
      <tspan>
        tspan attribute dx
        <animate attributeName="dx" from="-100" to="400" dur="3s" repeatCount="indefinite"></animate>
      </tspan>
    </text>
  </svg>
</div>
```

```css
/* xxx.css */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 3000px;
    width: 1080px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/9LUZjGO5RTe5t_k14cDFeA/zh-cn_image_0000002793039526.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5B96F3119CCA946D7B6F1BDBFBC609F7526C3B57AE3188809E836FE66FA924D)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text>
      <tspan x="0" y="550" font-size="30">
        tspan attribute fill|fill-opacity
        <animate attributeName="fill" from="blue" to="red" dur="3s" repeatCount="indefinite"></animate>
        <animate attributeName="fill-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
      </tspan>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/gcRzPBCnQqm_GZBngPZdGw/zh-cn_image_0000002792879552.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=23421E93E307A631FD9B01E44DF013B96DA1A4E59E96E473B9314183A7DE8ABC)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
     <text>
       <tspan x="20" y="600" fill="red">
         tspan attribute font-size
         <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite"></animate>
       </tspan>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/ud58gbFKRgGCJNUt1VQd3w/zh-cn_image_0000002821839459.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=89942C123071F5EE62E26DC27797EA5A30DF3BCEC15EBD33EAB0C1CB1DAE14E6)

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text>
      <tspan x="20" y="650" font-size="25" fill="blue" stroke="red">
        tspan attribute stroke
        <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
      </tspan>
    </text>
    <text>
      <tspan x="300" y="650" font-size="25" fill="white" stroke="red">
        tspan attribute stroke-width-opacity
        <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
        <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
      </tspan>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ZffF62AFQ-yvdbmopr3qmg/zh-cn_image_0000002821759457.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1C7EEA6F1A60F107B63BF2235CB260FAE0C74368ACC94AADE5756C2CB1BD2F7)
