---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-introduction
title: 文本概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3858568862ad3f99f5af13c4eb8a1f24e044079482788d6f13fef539393db215
---

文本包含用户输入的信息、呈现的文本内容和小图标，这些元素共同构建了用户与系统间的交互界面，提升了操作的便捷性与信息展示的直观性。

开发者可根据实际应用场景选择合适的文本组件进行页面开发。

## 文本显示

主要用于显示静态文本。开发者可以使用Text组件配合Span组件创建文本节点，也可以使用属性字符串（[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)/[MutableStyledString](../harmonyos-references/ts-universal-styled-string.md#mutablestyledstring)）节点生成文本信息并接入Text组件。参考[文本显示 (Text/Span)](arkts-common-components-text-display.md)章节。

## 文本输入

当需要在单行输入框（TextInput）或多行输入框（TextArea）中输入纯文本时，应优先考虑使用此文本组件。参考[文本输入 (TextInput/TextArea/Search)](arkts-common-components-text-input.md)章节。

## 富文本

当需要在编辑框内插入图片或者自定义图标等需求时，应优先考虑使用此文本组件。参考[富文本编辑 (RichEditor)](arkts-common-components-richeditor.md)章节。

## 图标小符号

当需要显示小图标时，应优先考虑使用此图标组件。参考[图标小符号 (SymbolGlyph/SymbolSpan)](arkts-common-components-symbol.md)章节。

## 属性字符串

当需要在字符或者段落级别设置文本样式，包括调整字号、添加字体颜色、使文本具备可点击性，以及通过自定义方式绘制文本等场景时，应优先考虑使用属性字符串。参考[属性字符串 (StyledString/MutableStyledString)](arkts-styled-string.md)章节。

## 图文混排

当需要图片和文字混排的场景，可以使用Span和ImageSpan实现。若需要样式多样的混排效果，可以选择属性字符串实现。参考[图文混排](arkts-text-image-layout.md)章节。

## 管理软键盘

当需要控制文本输入组件的软键盘行为，包括弹出、收起键盘时，可以使用软键盘管理功能。参考[管理软键盘](arkts-manage-keyboard.md)章节。
