---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient
title: CanvasGradient对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasGradient对象
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2514906f64b95e60437bab8d29d51fb687290f006aee8bdd5f588303545f6fea
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

渐变对象。

## addColorStop

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| offset | number | 设置渐变点距离起点的位置占总体长度的比例，范围为0到1。 |
| color | string | 设置渐变的颜色。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    const gradient = ctx.createLinearGradient(50, 0, 300, 100);
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 300, 300);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-nX-c6KxQHy22S-luo0POA/zh-cn_image_0000002815401295.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=845F40F90145C691FC3BCC02AE2D4C34331CC7A6501B9043638C1ED2BDF17C1E)
