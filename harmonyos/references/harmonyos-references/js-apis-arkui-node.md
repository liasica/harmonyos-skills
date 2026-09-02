---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node
title: "@ohos.arkui.node (自定义节点)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.node (自定义节点)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a7ceebd5281fbb94081171a77a1df896a4017903f06fbddd74c3cdada5a4134
---

Node将自定义节点的二级模块API组织在一起，方便开发者导出使用。自定义节点支持开发者灵活地创建、挂载和管理组件树节点，适用于需要动态构建、复用和扩展UI组件的场景。

**说明** 

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 当前不支持在预览器中使用自定义节点。

## BuilderNode

[BuilderNode](js-apis-arkui-buildernode.md)模块提供能够挂载系统组件的自定义节点BuilderNode，适用于需要在自定义节点中嵌入并复用系统组件的场景。不建议将BuilderNode作为子节点挂载到其他自定义节点上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## FrameNode

[FrameNode](js-apis-arkui-framenode.md)模块提供自定义节点FrameNode，表示组件树的实体节点，适用于需要直接操作和管理组件树实体节点的场景。[NodeController](js-apis-arkui-nodecontroller.md)可通过[BuilderNode](js-apis-arkui-buildernode.md)持有的FrameNode挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上，也可通过FrameNode获取[RenderNode](js-apis-arkui-rendernode.md)，并将RenderNode挂载到其他FrameNode上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NodeController

[NodeController](js-apis-arkui-nodecontroller.md)模块提供NodeController，用于实现自定义节点的创建、显示、更新等操作，并负责将自定义节点挂载到[NodeContainer](ts-basic-components-nodecontainer.md)上，适用于需要动态管理自定义节点生命周期及显示状态的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Graphics

[Graphics](js-apis-arkui-graphics.md)模块提供自定义节点属性设置的定义，用于对自定义节点的图形外观和渲染属性进行配置，适用于需要精细控制节点绘制效果的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RenderNode

[RenderNode](js-apis-arkui-rendernode.md)模块提供自绘制渲染节点RenderNode，支持开发者进行自定义绘制，适用于需要自绘制图形内容（如自定义图表、游戏画面、手绘动画等）的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## XComponentNode

[XComponentNode](js-apis-arkui-xcomponentnode.md)模块提供XComponent节点XComponentNode，表示组件树中的XComponent组件，用于EGL/OpenGLES和媒体数据写入，并支持动态修改节点渲染类型，适用于需要在自定义节点中嵌入图形渲染或媒体数据处理的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## UIContext获取方法

1. 使用ohos.window中的[getUIContext()](arkts-apis-window-window.md#getuicontext10)方法获取UIContext实例。
2. 通过自定义组件内置方法[getUIContext()](ts-custom-component-api.md#getuicontext)获取UIContext实例。
3. 在[NodeController](js-apis-arkui-nodecontroller.md)的[makeNode](js-apis-arkui-nodecontroller.md#makenode)回调方法中通过回调入参获取UIContext实例。
