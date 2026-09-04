---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-overview
title: 基础知识
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > svg开发指导 > 基础知识
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cd629ba37626a2e358176a10d1100ade4db984ca083240ed3ce4d8827341dc0e
---

svg组件主要作为svg画布的根节点使用，也可以在svg中嵌套使用。具体用法请参考[svg](../harmonyos-references/js-components-svg.md)。

**说明** 

svg父组件或者svg组件需要定义宽高值，否则不进行绘制。

## 创建svg组件

在pages/index目录下的hml文件中创建一个svg组件。

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">  </svg>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
svg{
  background-color: blue;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/nmeaZJPUSBiyYwg9s9R3jg/zh-cn_image_0000002712404174.png)

## 设置属性

通过设置width、height、x、y和viewBox属性为svg设置宽度、高度、x轴坐标、y轴坐标和svg视口。

```html
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400" viewBox="0 0 100 100">    
    <svg class="rect" width="100" height="100" x="20" y="10">    
    </svg>  
  </svg>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
svg{
  background-color: yellow;
}
.rect{
  background-color: red;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/i8_HOXGUQoGtomcQSTylmQ/zh-cn_image_0000002742123123.png)

**说明** 

* x和y设置的是当前svg的x轴和y轴坐标，如果当前svg为根节点，x轴和y轴属性无效。
* viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。
