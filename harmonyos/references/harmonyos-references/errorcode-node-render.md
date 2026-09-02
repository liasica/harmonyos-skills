---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render
title: 渲染节点错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 渲染节点错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:77db55d9860ee32cbc5662cd24859480b77ad7af5d454248a2b894815ce86823
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 106401 当前节点不是自定义节点

**错误信息**

The node type is not custom node.

**错误描述**

当前操作的节点不是 NDK 侧的自定义节点。

**可能原因**

开发者传入的 ArkUI\_NodeHandle 指针对应的节点类型非 ARKUI\_NODE\_CUSTOM 类型。

**处理步骤**

接入渲染节点流程时，创建一个 ARKUI\_NODE\_CUSTOM 类型的 NDK 节点作为渲染节点的根节点。

## 106402 当前节点已存在子节点

**错误信息**

Node already has children.

**错误描述**

当前操作的自定义节点已存在子节点。

**可能原因**

开发者构造渲染树时，作为根节点的自定义节点已挂载子 FrameNode 或 RenderNode。

**处理步骤**

接入渲染节点流程时，使用未挂载子节点的自定义节点作为根节点；如果目标自定义节点已存在子节点，先移除其子节点。

## 106403 当前渲染节点存在父节点

**错误信息**

RenderNode parent is existed.

**错误描述**

当前操作的渲染节点已有父节点，无法挂载至相应自定义组件下。

**可能原因**

开发者传入的 ArkUI\_RenderNodeHandle 指针对应的节点已挂载至其他组件下。

**处理步骤**

接入渲染节点流程时，使用未挂载至其他组件的 RenderNode；如果目标 RenderNode 已有父节点，先将其从原父节点移除。

## 106404 未找到对应的渲染子节点

**错误信息**

RenderNode child is not exist.

**错误描述**

无法查找到对应的渲染子节点。

**可能原因**

开发者传入的 ArkUI\_RenderNodeHandle 指针对应的渲染节点无法查询到对应下标的子节点。

**处理步骤**

确认 ArkUI\_RenderNodeHandle 指针对应的渲染节点存在子节点，并将传入的下标调整到该节点的有效子节点索引范围内。

## 106405 参数值超出范围

**错误信息**

Param is out of range.

**错误描述**

入参值超出接口接收值的范围。

**可能原因**

开发者传入的参数超出该接口的边界。

**处理步骤**

检查接口允许的入参范围，并将参数值调整到该范围内。

## 106406 当前渲染节点从FrameNode中获取

**错误信息**

The RenderNode is obtained from a FrameNode.

**错误描述**

该 RenderNode 是从 FrameNode 获取的，此类节点不允许执行当前操作。

**可能原因**

该 RenderNode 是从 FrameNode 获取的，除作为子节点上下树外，不允许其他操作。

**处理步骤**

当前节点仅可作为子节点上下树；执行其他操作时，请跳过该节点。

## 106407 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁

**错误信息**

The RenderNode is obtained from a FrameNode, and its corresponding FrameNode is no longer in the adopted state.

**错误描述**

该 RenderNode 是从 FrameNode 获取的，其对应的 FrameNode 已经被取消接纳或销毁。

**可能原因**

从被接纳的 FrameNode 上获取 RenderNode 后，该 FrameNode 被取消接纳或者析构。

**处理步骤**

如果通过[OH\_ArkUI\_NativeModule\_RemoveAdoptedChild](capi-native-node-h.md#oh_arkui_nativemodule_removeadoptedchild)取消接纳被接纳的FrameNode，或销毁该FrameNode，应调用[OH\_ArkUI\_RenderNodeUtils\_DisposeNode](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenode)释放此前通过[OH\_ArkUI\_RenderNodeUtils\_GetRenderNode](capi-native-render-h.md#oh_arkui_rendernodeutils_getrendernode)获取的RenderNode。

## 106408 当前节点不处于被接纳状态

**错误信息**

The node is not adopted.

**错误描述**

该节点未被接纳，不能获取其 RenderNode。

**可能原因**

调用 OH\_ArkUI\_RenderNodeUtils\_GetRenderNode 前，未通过 OH\_ArkUI\_NativeModule\_AdoptChild 将该节点接纳为附属节点。

**处理步骤**

先通过 [OH\_ArkUI\_NativeModule\_AdoptChild](capi-native-node-h.md#oh_arkui_nativemodule_adoptchild) 接口使当前节点被其他节点接纳，然后再获取其 RenderNode。
