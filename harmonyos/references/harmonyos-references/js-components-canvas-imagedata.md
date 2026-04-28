---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata
title: ImageData对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > ImageData对象
category: harmonyos-references
scraped_at: 2026-04-28T08:03:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4913302b0907ee5f1d13c6cae3c231024d0303425b1fa3014ab045807c6bcd1b
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

ImageData对象可以存储[canvas组件](js-components-canvas-canvas.md)渲染的像素数据。

## 属性

PhonePC/2in1TabletTVWearable

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | number | 矩形区域实际像素宽度。 |
| height | number | 矩形区域实际像素高度。 |
| data | <Uint8ClampedArray> | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. onShow() {
5. const el =this.$refs.canvas;
6. const ctx = el.getContext('2d');
7. ctx.fillRect(0,0,200,200);
8. var imageData = ctx.createImageData(1,1);
9. promptAction.showToast({
10. message:imageData,
11. duration:5000
12. })
13. }
14. }
```
