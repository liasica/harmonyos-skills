---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg
title: svg
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > svg
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d153c736135a87ddfa5c41f7f588e0c73590d62d6e23964a635357d6acc2900
---

基础容器，主要作为svg的根节点使用，也可以在svg中嵌套使用。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* svg父组件或者svg组件需要定义宽高值，否则不进行绘制。

## 权限列表

无

## 子组件

支持[svg](js-components-svg.md)、[rect](js-components-svg-rect.md)、[circle](js-components-svg-circle.md)、[ellipse](js-components-svg-ellipse.md)、[path](js-components-svg-path.md)、[line](js-components-svg-line.md)、[polygon](js-components-svg-polygon.md)、[polyline](js-components-svg-polyline.md)、[text](js-components-svg-text.md)、[animate](js-components-svg-animate.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性，设置的通用属性会传递给子组件。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| width | <length>|<percentage> | - | 否 | 设置组件的宽度。 |
| height | <length>|<percentage> | - | 否 | 设置组件的高度。 |
| x | <length>|<percentage> | - | 否 | 设置当前svg的x轴坐标，根svg节点无效。 |
| y | <length>|<percentage> | - | 否 | 设置当前svg的y轴坐标，根svg节点无效。 |
| viewBox | string | - | 否 | 设置当前svg的视口。支持的格式为<number number number number>，4个参数分别表示min-x, min-y, width and height，viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <svg width="200" height="200" viewBox="0 0 100 100">
      <rect x="10" y="10" width="80" height="80" fill="#00FF00"></rect>
    </svg>
    <rect x="10" y="10" width="80" height="80" fill="red" ></rect>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 200 200">
      <rect x="10" y="10" width="80" height="80" fill="red"></rect>
    </svg>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 400 400">
      <rect x="10" y="10" width="80" height="80" fill="blue"></rect>
    </svg>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/jbXUMXpuS4KX4ciBozxf9A/zh-cn_image_0000002706676496.png)
