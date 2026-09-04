---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas
title: Canvas对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Canvas对象
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:06+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:1bd15b979c8d842f2d555c16b0a18464951f3ddb35df95d845c4cd5aaf6c2755
---

Canvas组件提供画布，用于自定义绘制图形。具体用法请参考[CanvasRenderingContext2D对象](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md)。

## 创建Canvas组件

在pages/index目录下的hml文件中创建一个Canvas组件。

```html
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
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

canvas {
    background-color: #00ff73;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ZoYAewmfQUexagmJxW6ZiQ/zh-cn_image_0000002742003153.png)

**说明** 

* Canvas组件默认背景色与父组件的背景色一致。
* Canvas默认宽高为width: 300px，height: 150px。

## 添加样式

Canvas组件设置宽（width）、高（height）、背景色（background-color）及边框样式（border）。

```html
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
</div>
```

```css
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
    width: 100%;
    height: 100%;
}

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/wT0aJoakQI-d3sGRfP6NAA/zh-cn_image_0000002712404166.png)

## 添加事件

Canvas添加长按事件，长按后可获取Canvas组件的dataUrl值（toDataURL方法返回的图片信息），打印在下方文本区域内。

**说明** 

promptAction相关接口参考[弹窗](../harmonyos-references/js-apis-promptaction.md)。

```html
<!-- xxx.hml -->
<div class="container">
    <canvas ref="canvas1" onlongpress="getUrl"></canvas>
    <text>dataURL</text>
    <text class="content">{{ dataURL }}</text>
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

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
    margin-bottom: 50px;
}

.content {
    border: 5px solid blue;
    padding: 10px;
    width: 90%;
    height: 400px;
    overflow: scroll;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';

export default {
    data: {
        dataURL: null,
    },
    onShow() {
        let el = this.$refs.canvas1;
        let ctx = el.getContext("2d");
        ctx.strokeRect(100, 100, 300, 300);
    },
    getUrl() {
        let el = this.$refs.canvas1;
        let dataUrl = el.toDataURL();
        this.dataURL = dataUrl;
        promptAction.showToast({ duration: 2000, message: "long press,get dataURL" });
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/7eM_CwF2Ti2rm--YS961sQ/zh-cn_image_0000002742123115.gif)

**说明** 

画布不支持在onInit和onReady中进行创建。
