---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-slider
title: slider开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > slider开发指导
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:48+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:49075165e5d5cadd43c21e19d3cef6fd5a56c686ab416ed9c28aa64ddb7c14d0
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/psFKBrJHQpaLY77TqKHFvQ/zh-cn_image_0000002791565380.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014657Z&HW-CC-Expire=31536000000&HW-CC-Sign=A00EEE6C849A14D802B6337DFAE270FF4B6C4C9DF3CAB2DEAE1A6FAD2E96D26D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Ms0LpD2CQgKC-tPNqspg7w/zh-cn_image_0000002820525333.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014657Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCD2D880D641AF343F24F7D30DBE923CA458C7CF60F23B9210DC88A3389CA34D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/X4PbRyFESW6PMQq868e5bA/zh-cn_image_0000002820405333.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014657Z&HW-CC-Expire=31536000000&HW-CC-Sign=199CF7FCDE64E4C97FFC64DAE747C7515C65F91D4883D00DF620ED321125BBB0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/BW-E-Zq9TKe62SNaxtSMLQ/zh-cn_image_0000002791725354.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014657Z&HW-CC-Expire=31536000000&HW-CC-Sign=873686C91837CEB9756C3C788A4930880CF991FB43EE85ED3836A2F5FF6A70BC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/OXbGRq0jT6SgwIeZYJm7lQ/zh-cn_image_0000002791565382.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014657Z&HW-CC-Expire=31536000000&HW-CC-Sign=8348898519E06E67CC51C7FC2F769961210F24B3EB880BAA0616BA817640480B)
