---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-image
title: 添加图片区域
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 添加图片区域
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2b4399ee823e93bf8d8d7c9a90beadc33c6a25cee506745c0c1a9863304f308d
---

添加图片区域通常用[image](../harmonyos-references/js-components-basic-image.md)组件来实现，使用的方法和[text](../harmonyos-references/js-components-basic-text.md)组件类似。

图片资源建议放在js\default\common目录下，common目录需自行创建，详细的目录结构见[目录结构](js-framework-file.md#目录结构)。代码示例如下：

```html
<!-- xxx.hml -->
<image class="img" src="{{middleImage}}"></image>
```

```css
/* xxx.css */
.img {
  margin-top: 30px;
  margin-bottom: 30px;
  height: 385px;
}
```

```js
// xxx.js
export default {
  data: {
    middleImage: '/common/ice.png',
  },
}
```
