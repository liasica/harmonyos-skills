---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-overview
title: 基础知识
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 基础知识
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1bf91aede0a55bbf38bf0d6ed0c42f8da556a6b5e8c591a9233ac62ae6979ef7
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/bweW-bjFQKSBfTY6pEuO4g/zh-cn_image_0000002558764630.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/DrCaFZNGQgGFgQWsQ3ruWw/zh-cn_image_0000002558604974.png)

说明

* x和y设置的是当前svg的x轴和y轴坐标，如果当前svg为根节点，x轴和y轴属性无效。
* viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。
