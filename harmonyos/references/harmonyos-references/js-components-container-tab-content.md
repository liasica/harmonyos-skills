---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tab-content
title: tab-content
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > tab-content
category: harmonyos-references
scraped_at: 2026-04-28T08:02:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:36c91ff7a2d20c56eed2fcfec3a01aa9e1d185fbf214410e8bc5e4f3a4b6c7c7
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

<[tabs](js-components-container-tabs.md)>的子组件，用来展示tab的内容区，高度默认充满tabs剩余空间，子组件排列方式为横向排列，当作为容器组件的子元素时在主轴方向需要设置tab-content的确定长度，否则无法显示。tab-content组件不支持内容过长时页面的滑动，如需页面滑动，可嵌套List使用。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| scrollable | boolean | 否 | 是否可以通过左右滑动进行页面切换。默认为true，设置为false后，页面的切换只能通过tab-bar的点击实现。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-components-common-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

详见[tabs示例](js-components-container-tabs.md#示例)。
