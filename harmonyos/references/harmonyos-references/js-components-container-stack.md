---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack
title: stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > stack
category: harmonyos-references
scraped_at: 2026-09-05T06:17:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:332472f9ed6e3a2ce50cd37143978ca321933d4c22b12ca663eb1484119b275d
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 权限列表

无

## 子组件

支持。

## 属性

支持[通用属性](js-components-common-attributes.md)。

## 样式

支持[通用样式](js-components-common-styles.md)。

## 事件

支持[通用事件](js-components-common-events.md)。

## 方法

支持[通用方法](js-components-common-methods.md)。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/zcYsrjttR0WjjjRXdInAnw/zh-cn_image_0000002742125593.png)
