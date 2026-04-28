---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-image
title: 添加图片区域
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 添加图片区域
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cfae91a40e4a9c63396847c6f8f1c0fb5693e2596f1596433f4ac490e9f68ea0
---

添加图片区域通常用[image](../harmonyos-references/js-components-basic-image.md)组件来实现，使用的方法和[text](../harmonyos-references/js-components-basic-text.md)组件类似。

图片资源建议放在js\default\common目录下，common目录需自行创建，详细的目录结构见[目录结构](js-framework-file.md#目录结构)。代码示例如下：

```
1. <!-- xxx.hml -->
2. <image class="img" src="{{middleImage}}"></image>
```

```
1. /* xxx.css */
2. .img {
3. margin-top: 30px;
4. margin-bottom: 30px;
5. height: 385px;
6. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. middleImage: '/common/ice.png',
5. },
6. }
```
