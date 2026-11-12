---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-text
title: 绘制文本
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 绘制文本
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:13d4f7dc8ab6f4c8d85b67234ff48819c08788044ab04c319a85217776672fde
---

svg组件还可以绘制文本。

## 文本

**说明** 

* 文本的展示内容需要写在元素标签text内，可嵌套tspan子元素标签分段。
* 只支持被父元素标签svg嵌套。
* 只支持默认字体sans-serif。

通过设置x（x轴坐标）、y（y轴坐标）、dx（文本x轴偏移）、dy（文本y轴偏移）、fill（字体填充颜色）、stroke（文本边框颜色）、stroke-width（文本边框宽度）等属性实现文本的不同展示样式。

```html
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="200" y="300" font-size="80px" fill="blue" >Hello World</text>    <text x="200" y="300" dx="20" dy="80" font-size="80px" fill="blue" fill-opacity="0.5" stroke="red" stroke-width="2">Hello World</text>
    <text x="20" y="550" fill="#D2691E">
      <tspan dx="40" fill="red" font-size="80" fill-opacity="0.4">Hello World </tspan>
    </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/oTeyr9E-Smi-Gs98ag7CsQ/zh-cn_image_0000002815398851.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=078E54D54296E58F383923DAA885D3F04E2CD5E1177583E808308A8A93E297EC)

## 沿路径绘制文本

textpath文本内容沿着属性path中的路径绘制文本。

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="#00FF00" x="100" y="400">
    <path d="M40,360 Q360,360 360,180 Q360,20 200,20 Q40,40 40,160 Q40,280 180,180 Q180,180 200,100" stroke="red" fill="none"></path>
      <text>
        <textpath fill="blue" startOffset="20%" path="M40,360 Q360,360 360,180 Q360,20 200,20 Q40,40 40,160 Q40,280 180,180 Q180,180 200,100" font-size="30px">
          This is textpath test.
        </textpath>
      </text>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/UpWuBJWaQ2-sd5JDLUqLzA/zh-cn_image_0000002786519276.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=58C3B3504372AC7D4172091CB782AFBCF8BFAF1323DAEF56F4AA094C279347A0)
