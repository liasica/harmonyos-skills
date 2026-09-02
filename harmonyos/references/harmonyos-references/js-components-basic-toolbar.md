---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar
title: toolbar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > toolbar
category: harmonyos-references
scraped_at: 2026-09-02T15:01:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6a26404e301777ebd110309042afada9268abf8cf16e46b3c83234c1f4357a5
---

**说明** 

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

工具栏。放在界面底部，用于展示针对当前界面的操作选项。

## 权限列表

无

## 子组件

支持<toolbar-item>子组件。

**说明** 

工具栏最多可以展示5个toolbar-item子组件，如果存在6个及以上toolbar-item子组件，则保留前面4个子组件，后续的子组件收纳到工具栏上的更多项中，通过点击更多项弹窗展示剩下的子组件，更多项展示的组件样式采用系统默认样式，toolbar-item上设置的自定义样式不生效。

## 属性

支持[通用属性](js-components-common-attributes.md)。

## 样式

支持[通用样式](js-components-common-styles.md)。

**说明** 

不支持height样式，高度固定为56px。

## 事件

不支持。

## 方法

不支持。

## 示例

详见[toolbar-item示例](js-components-basic-toolbar-item.md)。
