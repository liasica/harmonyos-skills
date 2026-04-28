---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot
title: ContentSlot
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义占位组件 > ContentSlot
category: harmonyos-references
scraped_at: 2026-04-28T08:02:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0c0bbe41ccb3444d148197599b508d09d9fd3511ac21fbd4a57a281b7d0c3fdf
---

用于渲染并管理Native层使用C-API创建的组件。

支持混合模式开发，当容器是ArkTS组件，子组件在Native侧创建时，推荐使用ContentSlot占位组件。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 接口

PhonePC/2in1TabletTVWearable

ContentSlot(content: Content)

当内容添加到占位符组件时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [Content](ts-components-contentslot.md#content) | 是 | Content作为ContentSlot的管理器，通过Native侧提供的接口，可以注册并触发ContentSlot的上下树事件回调以及管理ContentSlot的子组件。 |

## Content

PhonePC/2in1TabletTVWearable

type Content = Content

定义ComponentContent和NodeContent的基类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Content](js-apis-arkui-content.md) | 定义ComponentContent和NodeContent的基类。 |

## 示例

PhonePC/2in1TabletTVWearable

下面的示例展示了ContentSlot的基本用法。

```
1. import { nativeNode } from 'libNativeNode.so'; // 开发者自己实现的so
2. import { NodeContent } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Parent {
7. private nodeContent: Content = new NodeContent();

9. aboutToAppear() {
10. // 通过C-API创建节点，并添加到管理器nodeContent上
11. nativeNode.createNativeNode(this.nodeContent);
12. }

14. build() {
15. Column() {
16. // 显示nodeContent管理器里存放的Native侧的组件
17. ContentSlot(this.nodeContent)
18. }
19. }
20. }
```

上述代码中so的实现可参考[Native XComponent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/NativeXComponent)。
