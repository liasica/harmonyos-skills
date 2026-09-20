---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack
title: stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 容器组件 > stack
category: harmonyos-references
scraped_at: 2026-09-21T06:21:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e485cd8f10628cc4c91d845030cf04596966d26d929b322c7b084ea4717a9ec
---

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

**说明** 

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持。

## 属性

支持[通用属性](js-service-widget-common-attributes.md)。

## 样式

支持[通用样式](js-service-widget-common-styles.md)。

## 事件

支持[通用事件](js-service-widget-common-events.md)。

## 示例

```html
<!-- xxx.hml -->
<stack class="stack-parent">
  <div class="back-child bd-radius"></div>
  <div class="positioned-child bd-radius"></div>
  <div class="front-child bd-radius"></div>
</stack>
```

```css
/* xxx.css */
.stack-parent {
  width: 400px;
  height: 400px;
  margin: 50px;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
}
.back-child {
  width: 300px;
  height: 300px;
  background-color: #3f56ea;
}
.front-child {
  width: 100px;
  height: 100px;
  background-color: #00bfc9;
}
.positioned-child {
  width: 100px;
  height: 100px;
  left: 50px;
  top: 50px;
  background-color: #47cc47;
}
.bd-radius {
  border-radius: 16px;
}
```

**4×4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/p-aUYWyKQ3-Xs8bk4JWNog/zh-cn_image_0000002762836559.png)
