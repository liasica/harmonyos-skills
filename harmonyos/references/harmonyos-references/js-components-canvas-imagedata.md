---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata
title: ImageData对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > ImageData对象
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc790f414a47fe2d3c76b9118e4b18969d81cd0654c881b301745b1ab8eed1d6
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

ImageData对象可以存储[canvas组件](js-components-canvas-canvas.md)渲染的像素数据。

## 属性

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | number | 矩形区域实际像素宽度。 |
| height | number | 矩形区域实际像素高度。 |
| data | <Uint8ClampedArray> | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |

## 示例

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(0, 0, 200, 200);
    var imageData = ctx.createImageData(1, 1);
    promptAction.showToast({
      message: imageData,
      duration: 5000
    })
  }
}
```
