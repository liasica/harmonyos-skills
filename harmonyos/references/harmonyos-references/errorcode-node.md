---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node
title: 自定义节点错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 自定义节点错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:00ba3d2a52e1b9fc5cf597f65483152d7681bca593ef31fc4fd738ac637f3ed4
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 100021 FrameNode节点不可修改

**错误信息**

The FrameNode is not modifiable.

**错误描述**

当前FrameNode节点不可修改，无法对其进行当前的操作。可能触发的操作有设置属性、增删子节点、绑定控制器。

**可能原因**

开发者尝试对声明式节点进行修改性操作，例如，设置属性、增删子节点、绑定控制器。

**处理步骤**

避免对不可修改的节点进行修改性操作。可通过try-catch捕获并处理错误，避免影响其他逻辑。

## 100022 FrameNode节点的组件类型不支持调整跨语言的通用属性设置权限

**错误信息**

The FrameNode cannot be set whether to support cross-language common attribute setting.

**错误描述**

当前FrameNode节点的组件类型不支持调整跨语言通用属性设置权限。

**可能原因**

开发者尝试调整目标FrameNode节点的跨语言通用属性设置权限。

**处理步骤**

避免对不支持设置跨ArkTS语言访问选项的FrameNode节点调用[setCrossLanguageOptions](js-apis-arkui-framenode.md#setcrosslanguageoptions15)接口调整跨语言访问权限。可参考setCrossLanguageOptions接口说明，确认目标节点类型是否支持设置跨ArkTS语言访问选项。

## 100023 参数错误

**错误信息**

Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined.

**错误描述**

当前接口传入的参数错误。

**可能原因**

1. 传入的节点参数的组件类型不正确。
2. 传入的节点参数为null或undefined。
3. 传入的控制器参数为null或undefined。

**处理步骤**

确认传入的节点参数组件类型正确，并在调用接口前判断节点参数或控制器参数是否为null或undefined。

## 100024 节点没有公共祖先节点

**错误信息**

The current FrameNode and the target FrameNode do not have a common ancestor node.

**错误描述**

当前节点和目标节点没有公共祖先节点。

**可能原因**

找不到当前节点和目标节点的公共祖先节点。

**处理步骤**

传入与当前节点存在公共祖先节点的目标节点。

## 100025 传入参数不符合要求

**错误信息**

The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'targetNode' is invalid: it cannot be disposed."

**错误描述**

参数无效。错误信息中包含无效参数及其原因的详细信息。例如：“参数‘targetNode’无效：该参数不能是已销毁的节点。”

**可能原因**

传入的参数为null、undefined或其他无效值，具体原因可查看错误信息。

**处理步骤**

1. 当报错信息显示传入参数为null，改为传入一个非空的FrameNode对象。
2. 当报错信息显示找不到公共祖先节点时，传入目标节点前判断目标节点是否为离屏节点，并传入与当前节点存在公共祖先节点的目标节点。
3. 根据错误信息中指明的无效参数及原因，修改对应参数。

## 100026 调用接口的实例对象已与后端实体节点解绑

**错误信息**

The current FrameNode has been disposed.

**错误描述**

当前调用接口的实例对象已与后端实体节点解绑。

**可能原因**

开发者在当前接口调用前，使用该实例对象调用了[dispose](js-apis-arkui-framenode.md#dispose12)接口，例如：item.dispose()。

**处理步骤**

1. 如果还需要使用该实例对象，请勿对其执行dispose操作。
2. 如果不确定当前实例对象是否可用，可以调用isDisposed接口进行判断。

## 100027 当前节点已被接纳为附属节点

**错误信息**

The current node has been adopted.

**错误描述**

当前节点已经被接纳为附属节点，不支持当前操作。

**可能原因**

当前节点已经被接纳为附属节点，不支持当前操作。

**处理步骤**

取消当前节点被接纳为附属节点的状态后，再执行当前操作。

## 100028 当前节点不在主节点树上

**错误信息**

The current FrameNode is not on the main tree.

**错误描述**

当前节点不在主节点树上。

**可能原因**

当前节点不在主节点树上。

**处理步骤**

将当前节点挂载到主节点树上，再执行当前操作。

## 100029 BuilderNode中，状态管理V2尚未支持组件复用功能

**错误信息**

Reuse/Recycle not implemented for ViewV2, yet.

**错误描述**

BuilderNode中，[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)暂不支持[reuse](js-apis-arkui-buildernode.md#reuse12)。

**可能原因**

BuilderNode中，状态管理V2暂不支持组件复用。

**处理步骤**

使用状态管理V2时，不在BuilderNode节点上使用组件复用相关功能。从API版本26.0.0开始，BuilderNode中的自定义组件支持V2组件复用。

## 106103 对应的操作不支持ArkTS创建的节点

**错误信息**

The corresponding operation does not support nodes created by ArkTS.

**错误描述**

对应的操作不支持ArkTS创建的节点。

**可能原因**

当前操作不支持ArkTS创建的节点。

**处理步骤**

传入非ArkTS创建的节点。

## 106203 传入的节点未挂载到组件树上

**错误信息**

The node not mounted to component tree.

**错误描述**

传入的节点未挂载到组件树上。

**可能原因**

当前传入的节点未挂载到组件树上。

**处理步骤**

调整函数调用时机，确保传入的节点已挂载到组件树上。

## 106204 不支持在非UI线程操作传入的节点

**错误信息**

Operations on the provided node are not supported on non-UI threads.

**错误描述**

不支持在非UI线程操作传入的节点。

**可能原因**

1. 接口只支持在UI线程调用。
2. 接口支持多线程调用，但是接口操作的节点处于Attached状态。

**处理步骤**

1. 调整函数调用时机，确保接口在UI线程调用。
2. 确认节点是由多线程[createNode](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建的。
3. 参考[多线程NDK接口调用规范](../harmonyos-guides/ndk-build-on-multi-thread.md#多线程ndk接口调用规范)，将组件所在组件树中所有不可转换的Attached组件移除。
