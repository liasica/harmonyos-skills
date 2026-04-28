---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-text
title: 绘制文本
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 绘制文本
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d7554f5f8b7202c4790122333290a642d62aa561058b9870e1219e02d018c584
---

svg组件还可以绘制文本。

## 文本

说明

* 文本的展示内容需要写在元素标签text内，可嵌套tspan子元素标签分段。
* 只支持被父元素标签svg嵌套。
* 只支持默认字体sans-serif。

通过设置x（x轴坐标）、y（y轴坐标）、dx（文本x轴偏移）、dy（文本y轴偏移）、fill（字体填充颜色）、stroke（文本边框颜色）、stroke-width（文本边框宽度）等属性实现文本的不同展示样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text x="200" y="300" font-size="80px" fill="blue" >Hello World</text>    <text x="200" y="300" dx="20" dy="80" font-size="80px" fill="blue" fill-opacity="0.5" stroke="red" stroke-width="2">Hello World</text>
5. <text x="20" y="550" fill="#D2691E">
6. <tspan dx="40" fill="red" font-size="80" fill-opacity="0.4">Hello World </tspan>
7. </text>
8. </svg>
9. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/MDuLLD7KTY2xbtw-kLDwWA/zh-cn_image_0000002552798492.png?HW-CC-KV=V1&HW-CC-Date=20260427T234031Z&HW-CC-Expire=86400&HW-CC-Sign=C695BD26880E0409F7C8B27155ECCA081E577B8BFEACC321C533FB72374FC39C)

## 沿路径绘制文本

textpath文本内容沿着属性path中的路径绘制文本。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="#00FF00" x="100" y="400">
4. <path d="M40,360 Q360,360 360,180 Q360,20 200,20 Q40,40 40,160 Q40,280 180,180 Q180,180 200,100" stroke="red" fill="none"></path>
5. <text>
6. <textpath fill="blue" startOffset="20%" path="M40,360 Q360,360 360,180 Q360,20 200,20 Q40,40 40,160 Q40,280 180,180 Q180,180 200,100" font-size="30px">
7. This is textpath test.
8. </textpath>
9. </text>
10. </svg>
11. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/c9QxfJxzT0GjVy2Z0eMszw/zh-cn_image_0000002583438187.png?HW-CC-KV=V1&HW-CC-Date=20260427T234031Z&HW-CC-Expire=86400&HW-CC-Sign=008C51582184D6B0E8DD9DECE7DDB1BDE2A031636183C3EB1821F7CF54AEA678)
