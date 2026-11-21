---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient
title: CanvasGradient对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasGradient对象
category: harmonyos-references
scraped_at: 2026-11-21T09:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:98014e824eff5ce9c7cdb1e573a7b9ce48707d71f99e4dc4796122b65c055427
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/nuYDqGd5RJC4xIwB2VMojA/zh-cn_image_0000002792879536.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D985765B06248515CE9815FED3BFE39D6FF825CEFFA5DE18A31FADECFAB395B)
