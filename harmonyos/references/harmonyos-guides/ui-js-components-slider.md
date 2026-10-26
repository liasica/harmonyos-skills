---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-slider
title: slider开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > slider开发指导
category: harmonyos-guides
scraped_at: 2026-10-27T07:38:54+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:b85d8a54c1f6682f303c9a80279e869d8ca22403143670a84a49919fd51506b3
---

slider为滑动条组件，用来快速调节音量、亮度等。具体用法请参考[slider](../harmonyos-references/js-components-basic-slider.md)。

## 创建slider组件

在pages/index目录下的hml文件中创建一个slider组件。

```html
<!-- xxx.hml -->
<div class="container">
  <slider></slider>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  background-color: #F1F3F5;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/v-wcMDoKRyKLlJFxvDMeDQ/zh-cn_image_0000002801105299.gif)

## 设置样式和属性

slider组件通过color、scrollbar-color、background-color样式分别为滑动条设置背景颜色、滚动条颜色和背景颜色。

```html
<!-- xxx.hml -->
<div class="container">
  <slider class= "sli"></slider>
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
  background-color: #F1F3F5;
}
.sli{
  color: #fcfcfc;
  scrollbar-color: aqua;
  background-color: #b7e3f3;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/fu2kp85HQEy2B500S7GZJw/zh-cn_image_0000002771665520.gif)

通过添加min、max、value、step、mode属性分别为滑动条设置最小值、最大值、初始值、滑动步长和滑动条样式。

```html
<!-- xxx.hml -->
<div class="container">
  <slider min="0" max="100" value="1" step="2" mode="inset" showtips="true"></slider>
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
  background-color: #F1F3F5;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/H7qB7eDiRxKYdxs10gr2mQ/zh-cn_image_0000002800985377.gif)

**说明** 

mode属性为滑动条样式，可选值为：

* outset：滑块在滑杆上。
* inset：滑块在滑杆内。

## 绑定事件

向slider组件添加change事件，添加时需要传入ChangeEvent参数。

```html
<!-- xxx.hml -->
<div class="container">
  <text>slider start value is {{startValue}}</text>
  <text>slider current value is {{currentValue}}</text>
  <text>slider end value is {{endValue}}</text>
  <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
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
  background-color: #F1F3F5;
}
```

```js
// xxx.js
export default {
  data: {
    value: 0,
    startValue: 0,
    currentValue: 0,
    endValue: 0,
  },
  setValue(e) {
    if (e.mode === "start") {
      this.value = e.value;
      this.startValue = e.value;
    } else if (e.mode === "move") {
      this.value = e.value;
      this.currentValue = e.value;
    } else if (e.mode === "end") {
      this.value = e.value;
      this.endValue = e.value;
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/mGI0udx5QPSXNm-I6ijLEg/zh-cn_image_0000002771825488.gif)

## 场景示例

开发者可以通过调整滑动条的值来改变图片大小，并且动态打印当前图片的宽和高。

```html
<!-- xxx.hml -->
<div class="container">
  <image src="common/landscape3.jpg" style=" width: {{WidthVal}}px;height:{{HeightVal}}px;margin-top: -150px;"></image>
  <div class="text">
    <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
    <text>The width of this picture is {{WidthVal}}</text>
    <text>The height of this picture is {{HeightVal}}</text>
  </div>
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
  background-color: #F1F3F5;
}
.text{
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 65%;
}
.text{
  margin-top: 30px;
}
```

```js
// xxx.js
export default{
  data: {
    value: 0,
    WidthVal: 200,
    HeightVal: 200
  },
  setValue(e) {
    this.WidthVal = 200 + e.value;
    this.HeightVal = 200 + e.value;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/eZrK7_nMSL2r2dOixFp90Q/zh-cn_image_0000002801105301.gif)
