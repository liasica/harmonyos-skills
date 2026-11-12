---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-textpath
title: textPath
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > textPath
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-16
content_hash: sha256:0c74740bfc611fa0530b09a1bda8841b25e2da2c004bae29a32ae92fe6ad326d
---

沿路径绘制文本。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 按指定的路径绘制文本，可嵌套子标签tspan分段。
* 只支持被父元素标签text嵌套。

## 权限列表

无

## 子组件

[tspan](js-components-svg-tspan.md)。

## 属性

支持以下表格中的属性。

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| id | string | - | 组件的唯一标识。 |
| path | string | - | 设置路径的形状。  字母指令表示的意义如下：  - M = moveto  - L = lineto  - H = horizontal lineto  - V = vertical lineto  - C = curveto  - S = smooth curveto  - Q = quadratic Bezier curve  - T = smooth quadratic Bezier curveto  - A = elliptical Arc  - Z = closepath |
| startOffset | <length>|<percentage> | 0 | 设置文本沿path绘制的起始偏移。  默认值：0 |
| font-size | <length> | 30px | 设置文本的尺寸。  默认值：30px |
| fill | <color> | black | 字体填充颜色。  默认值：black |
| by | number | - | 相对被指定动画的属性偏移值，from默认为原属性值。 |
| opacity | number | 1 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。  默认值：1 |
| fill-opacity | number | 1.0 | 字体填充透明度。  默认值：1.0 |
| stroke | <color> | black | 绘制字体描边并指定颜色。  默认值：black |
| stroke-width | number | 1 | 字体描边宽度。  默认值：1，单位px。 |
| stroke-opacity | number | 1.0 | 字体描边透明度。  默认值：1.0 |

## 示例

textPath属性示例，textpath文本内容沿着属性path中的路径绘制文本，起点偏移20%的path长度。（绘制的元素<path>曲线仅做参照）

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00" x="50">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none"></path>
    <text>
      <textpath fill="blue" startOffset="20%" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px">
        This is textpath test.
      </textpath>
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
    height: 1200px;
    width: 600px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/1EZKEEZvT5CUPSXdGTTBog/zh-cn_image_0000002815561229.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A73F89CA56877F7B0976B87020B3AD85A5142683E445DE370CFAFBE53DD75D46)

textpath与tspan组合示例与效果图

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00" x="50">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none"></path>
      <text>
        <textpath fill="blue" startOffset="20%" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="15px">
          <tspan dx="-50px" fill="red">This is tspan onTextPath.</tspan>
          <tspan font-size="25px">Let's play.</tspan>
          <tspan font-size="30px" fill="#00FF00">12345678912354567891234567891234567891234567891234567890</tspan>
        </textpath>
      </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/KXu_HOv6TMa0BK81qARRhw/zh-cn_image_0000002815401313.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC9C67122224BDA4970C27438FA95D496947F9BC8782C9EFC7A6C1545C230C7E)

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00" x="50">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none"></path>
    <text>
      <textpath fill="#D2691E" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px" stroke="black" stroke-width="1" >
        This is TextPath.
        <tspan font-size="20px" fill="red">This is tspan onTextPath.</tspan>
        <tspan font-size="30px">Let's play.</tspan>
        <tspan font-size="40px" fill="#00FF00"  stroke="blue" stroke-width="2">12345678912354567891234567891234567891234567891234567890
        </tspan>
      </textpath>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/rhan6qe_TlCcIY7UcrTyog/zh-cn_image_0000002786521738.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=545E30ED511BF74FE768DBE0D54F1447D1228FE3ADED8659BA9E472786B8C49F)

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00" x="50">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none">
    </path>
    <!--      数值百分比    -->
    <text>
      <textpath fill="#D2691E" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px">
        This is TextPath.
        <tspan x="50" fill="blue">This is first tspan.</tspan>
        <tspan x="50%">This is second tspan.</tspan>
        <tspan dx="10%">12345678912354567891234567891234567891234567891234567890</tspan>
      </textpath>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/8ap2vON0SomKj3nWJr7Agw/zh-cn_image_0000002786361810.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B4CBED05BD4C117C03469CAF1214340F96F12E98B83A5C9E61B78BF2680514F)

startOffset属性动画，文本绘制时起点偏移从10%运动到40%，不绘制超出path长度范围的文本。

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

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none"></path>
    <text>
      <textpath fill="blue" startOffset="10%" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="15px">
        <tspan dx="-50px" fill="red">This is tspan onTextPath.</tspan>
        <tspan font-size="25px">Let's play.</tspan>
        <tspan font-size="30px" fill="#00FF00">12345678912354567891234567891234567891234567891234567890</tspan>
        <animate attributeName="startOffset" from="10%" to="40%" dur="3s" repeatCount="indefinite"></animate>
      </textpath>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/87byUFsxSMK6WMsUmf0oJw/zh-cn_image_0000002815561231.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D5430596E291B95D44117E1365B0F69D7E4A46C5C2B58E881C3E7CC93DD50D5)

textpath与tspan组合属性动画与效果图

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red" fill="none">
    </path>
    <text>
      <textpath fill="#D2691E" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px">
        This is TextPath.
        <tspan x="50" fill="blue">
          tspan attribute x|rotate
          <animate attributeName="x" from="50" to="100" dur="5s" repeatCount="indefinite"></animate>
          <animate attributeName="rotate" from="0" to="360" dur="5s" repeatCount="indefinite"></animate>
        </tspan>
        <tspan x="30%">tspan static.</tspan>
        <tspan>
          tspan attribute dx|opacity
          <animate attributeName="dx" from="0%" to="30%" dur="3s" repeatCount="indefinite"></animate>
          <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
        </tspan>
        <tspan dx="5%">tspan move</tspan>
      </textpath>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/pZWYJ63yTWWRfmRwbxfXvw/zh-cn_image_0000002815401315.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B20E5A980577EABAE9D78D9A3D34A94B1A3D87C248A556B5B5CBD131F1CA4F56)

(1) "tspan attribute x|rotate" 文本绘制起点偏移从50px运动到100px，顺时针旋转0度到360度。

(2) "tspan attribute dx|opacity" 在 "tspan static." 绘制结束后再开始绘制，向后偏移量从0%运动到30%，透明度从浅到深变化。

(3) "tspan move" 在上一段tspan绘制完成后，向后偏移5%的距离进行绘制，呈现跟随前一段tspan移动的效果。

textpath与tspan组合属性动画与效果图

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red"
      fill="none">
    </path>
    <text>
      <textpath fill="#D2691E" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px">
        This is TextPath.
        <tspan dx="20" fill="blue">
          tspan attribute fill|fill-opacity
          <animate attributeName="fill" from="blue" to="red" dur="3s" repeatCount="indefinite"></animate>
          <animate attributeName="fill-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
        </tspan>
        <tspan dx="20" fill="blue">
          tspan attribute font-size
          <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite"></animate>
        </tspan>
      </textpath>
        <tspan font-size="30">Single tspan</tspan>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/QY5nyW7fQIm8EhiQGo3n1w/zh-cn_image_0000002786521740.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=30FEAAED2CBFF27F687578C94309C1C1A72DA3F0978F6AB1C267620180683D85)

(1) "This is TextPath." 在path上无偏移绘制第一段文本内容，大小30px，颜色"#D2691E"。

(2) "tspan attribute fill|fill-opacity" 相对上一段文本结束后偏移20px，颜色从蓝到红，透明度从浅到深。

(3) "tspan attribute font-size" 绘制起点相对上一段结束后偏移20px，起点静止，字体大小从10px到50px，整体长度持续拉长。

(4) "Single tspan" 在上一段的尾部做水平绘制，呈现跟随上一段运动的效果。

textpath与tspan组合属性动画与效果图

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00">
    <path d="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" stroke="red"
      fill="none">
    </path>
    <text>
      <textpath fill="#D2691E" path="M40,360 Q360,360 360,180 Q360,40 200,40 Q40,40 40,160 Q40,280 180,280 Q280,280 300,200" font-size="30px">
          This is TextPath.
          <tspan dx="20" fill="blue">
            tspan attribute stroke
            <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
          </tspan>
          <tspan dx="20" fill="white" stroke="red">
            tspan attribute stroke-width-opacity
            <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
            <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
          </tspan>
      </textpath>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/4rzktXs7QAaNGJ_llcr6eA/zh-cn_image_0000002786361812.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C259F90456E6718710E27404BAAC39C95413D8E2144F9A913F1A9A88402DF06)

(1) "tspan attribute stroke" 轮廓颜色从红色逐渐转变成绿色。

(2) "tspan attribute stroke-width-opacity" 轮廓宽度从细1px转变粗5px，透明度从浅到深。
