---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode
title: qrcode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > qrcode
category: harmonyos-references
scraped_at: 2026-09-02T15:01:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2572267956dbc9d0e6b55d5c567fd269d1e20f8dffb0e0d3146263639a0c8f53
---

**说明** 

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

生成并显示二维码。

## 权限列表

无

## 子组件

不支持。

## 属性

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | string | - | 是 | 用来生成二维码的内容。 |
| type | string | rect | 否 | 二维码类型。可能选项有：  - rect：矩形二维码。  - circle：圆形二维码。 |

## 样式

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #000000 | 否 | 二维码颜色。 |
| background-color | <color> | #ffffff | 否 | 二维码背景颜色。 |

**说明** 

* width和height不一致时，取二者较小值作为二维码的边长。且最终生成的二维码居中显示。
* width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。
* 生成二维码不可用时，请参考[Scan Kit（统一扫码服务）](scan-api.md)。

## 事件

支持[通用事件](js-components-common-events.md)。

## 方法

支持[通用方法](js-components-common-methods.md)。

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <qrcode value="Hello World" type="{{qr_type}}"
  style="color: {{qr_col}};background-color: {{qr_bcol}};width: {{qr_size}};height: {{qr_size}};margin-bottom: 70px;"></qrcode>
  <text class="txt">Type</text>
  <switch showtext="true" checked="true" texton="rect" textoff="circle" onchange="setType"></switch>
  <text class="txt">Color</text>
  <select onchange="setCol">
    <option for="{{col_list}}" value="{{$item}}">{{$item}}</option>
  </select>
  <text class="txt">Background Color</text>
  <select onchange="setBCol">
    <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
  </select>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.txt {
  margin: 30px;
  color: orangered;
}
select{
  margin-top: 40px;
  margin-bottom: 40px;
}
```

```js
/* index.js */
export default {
  data: {
    qr_type: 'rect',
    qr_size: '300px',
    qr_col: '#87ceeb',
    col_list: ['#87ceeb','#fa8072','#da70d6','#80ff00ff','#00ff00ff'],
    qr_bcol: '#f0ffff',
    bcol_list: ['#f0ffff','#ffffe0','#d8bfd8']
  },
  setType(e) {
    if (e.checked) {
      this.qr_type = 'rect'
    } else {
      this.qr_type = 'circle'
    }
  },
  setCol(e) {
    this.qr_col = e.newValue
  },
  setBCol(e) {
    this.qr_bcol = e.newValue
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ByiGmaOvRiKN8waZkwMeBA/zh-cn_image_0000002706676454.gif)
