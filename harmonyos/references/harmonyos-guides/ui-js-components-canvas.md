---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas
title: Canvas对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Canvas对象
category: harmonyos-guides
scraped_at: 2026-10-11T07:21:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:dc43f17c92a3293cbfd389ed2bc0b0b6ca1a134234a78f3e85e7e0a5a028399e
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/nC1kk6QxQ1S2FRkIQF8KQA/zh-cn_image_0000002784662707.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Gxj29MfjT_aLsk1Ccs5I1w/zh-cn_image_0000002755023774.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/NVNQX42RSJWFBSPEBIJE4g/zh-cn_image_0000002755183662.gif)

**说明** 

画布不支持在onInit和onReady中进行创建。
