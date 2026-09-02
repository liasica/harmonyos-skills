---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-customizing-font
title: 自定义字体样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 自定义字体样式
category: harmonyos-references
scraped_at: 2026-09-02T15:01:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6576e6824ff491779fd29edf1d0d41c2ee6aa7508754bcc8872583f931bcc2ad
---

自定义字体可以是从项目中的字体文件中加载的字体，字体格式支持ttf和otf。

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 定义font-face

```js
/* xxx.css */
@font-face {
  font-family: font;
  src: url('/common/font.ttf');
}
```

**font-family：**

自定义字体的名称。

**src：**

自定义字体的来源，支持如下类别：

* 项目中的字体文件：通过url指定项目中的字体文件路径（只支持绝对路径，详情请参见[资源和文件访问规则](../harmonyos-guides/js-framework-file.md#文件访问规则)章节）。
* 不支持设置多个src。

## 使用font-face

可以在style中定义font-face，然后在font-family样式中指定该font-face的名称，从而应用font-face定义的字体。

**示例：**

页面布局：

```html
<!-- xxx.hml -->
<div>    
  <text class="demo-text">测试自定义字体</text>  
</div>
```

页面样式：

```css
/*xxx.css*/
@font-face {
  font-family: font;
  src: url("/common/font.ttf");
}
.demo-text {
  font-family: font;
}
```
