---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient
title: CanvasGradient对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasGradient对象
category: harmonyos-references
scraped_at: 2026-04-29T13:53:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8e0e0d05071ace687bac70cffaf3348b04715fd27ed47638c427f20a44d69359
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

渐变对象。

## addColorStop

PhonePC/2in1TabletTVWearable

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| offset | number | 设置渐变点距离起点的位置占总体长度的比例，范围为0到1。 |
| color | string | 设置渐变的颜色。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. const gradient = ctx.createLinearGradient(50, 0, 300, 100);
7. gradient.addColorStop(0.0, '#ff0000')
8. gradient.addColorStop(0.5, '#ffffff')
9. gradient.addColorStop(1.0, '#00ff00')
10. ctx.fillStyle = gradient
11. ctx.fillRect(0, 0, 300, 300)
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/dTZAmbDPScqokRBlArOavQ/zh-cn_image_0000002589246565.png?HW-CC-KV=V1&HW-CC-Date=20260429T055330Z&HW-CC-Expire=86400&HW-CC-Sign=5782BD35B0DB2170A454ECED059A84E424CC79F1E85A0AD7334734FBC91D8A53)
