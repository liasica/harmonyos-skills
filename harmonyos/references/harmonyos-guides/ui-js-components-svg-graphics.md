---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-graphics
title: 绘制图形
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 绘制图形
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a862c230e55c5bf9b1e017c80058817d6824fa9f3a17ff3bbd7949bd93e7c5d8
---

svg组件可以用来绘制常见图形和线段，如矩形（<rect>）、圆形（<circle>）、线条(<line>）等，具体支持图形样式还请参考[svg](../harmonyos-references/js-components-svg.md)组件。

在本场景中，绘制各种图形拼接成一个小房子。

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="1000" height="1000">
    <polygon points="100,400 300,200 500,400" fill="red"></polygon>     //屋顶
    <polygon points="375,275 375,225 425,225 425,325" fill="orange"></polygon>   //烟囱
    <rect width="300" height="300" x="150" y="400" fill="orange">      //房子
    </rect>
    <rect width="100" height="100" x="180" y="450" fill="white">    //窗户
    </rect>
    <line x1="180" x2="280" y1="500" y2="500" stroke-width="4" fill="white" stroke="black"></line>     //窗框
    <line x1="230" x2="230" y1="450" y2="550" stroke-width="4" fill="white" stroke="black"></line>     //窗框
    <polygon points="325,700 325,550 400,550 400,700" fill="red"></polygon>     //门
    <circle cx="380" cy="625" r="20" fill="black"></circle>      //门把手
  </svg>
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
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/D4ZKTSeKT_isqQQCAcamag/zh-cn_image_0000002706833970.png)
