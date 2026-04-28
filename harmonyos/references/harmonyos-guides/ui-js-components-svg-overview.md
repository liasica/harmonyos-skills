---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-overview
title: 基础知识
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 基础知识
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:722121b6d40ec892119cf51e20eab75d76f2ca9497d091cd3c92c433d2ea2e33
---

svg组件主要作为svg画布的根节点使用，也可以在svg中嵌套使用。具体用法请参考[svg](../harmonyos-references/js-components-svg.md)。

说明

svg父组件或者svg组件需要定义宽高值，否则不进行绘制。

## 创建svg组件

在pages/index目录下的hml文件中创建一个svg组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">  </svg>
4. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. svg{
11. background-color: blue;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/SlJPfulOQ2WP0xm-W5-qkA/zh-cn_image_0000002552798490.png?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=FA7DD483A1455933E0D29862A498AAF2559C96D6A016116EBE97C4F1ADBA1CAA)

## 设置属性

通过设置width、height、x、y和viewBox属性为svg设置宽度、高度、x轴坐标、y轴坐标和svg视口。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400" viewBox="0 0 100 100">
4. <svg class="rect" width="100" height="100" x="20" y="10">
5. </svg>
6. </svg>
7. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. svg{
11. background-color: yellow;
12. }
13. .rect{
14. background-color: red;
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/8ilZ6KIgQBG7A5cu0ap46g/zh-cn_image_0000002583438185.png?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=D69ABBD975B775323780B0A7BE0D953F5F0DAC7B529D0C9BF4C57B8A8FFC0DCF)

说明

* x和y设置的是当前svg的x轴和y轴坐标，如果当前svg为根节点，x轴和y轴属性无效。
* viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。
