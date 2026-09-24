---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-common-type-h
title: common_type.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > common_type.h
category: harmonyos-references
scraped_at: 2026-09-25T07:10:29+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:35c1a32d5ddd55beefea69dc8f7f5686b06bce210a5534e4d5b2929b15de0b5d
---

## 概述

定义ArkUI Native API的公共类型。

**引用文件：** <arkui/common\_type.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ContextCallback](capi-arkui-nativemodule-arkui-contextcallback.md) | ArkUI\_ContextCallback | 事件回调类型，用于定义回调函数及其用户自定义数据。使用该类型的接口触发回调时，会调用callback，并将userData作为参数传入。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) | ArkUI\_NumberValue | ArkUI在Native侧使用的数字类型，用于通过统一类型承载浮点、有符号整型和无符号整型数值。 |
| [ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) | ArkUI\_AttributeItem | 定义[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)函数的通用入参结构。各个属性设置接口可选择使用其中的成员变量来存储特定类型的参数数据。 |
| [ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md) | ArkUI\_Rect | 定义遮罩屏蔽区域的范围结构体。 |
| [ArkUI\_IntSize](capi-arkui-nativemodule-arkui-intsize.md) | ArkUI\_IntSize | 尺寸类型，用于描述组件的宽高。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md) | ArkUI\_IntOffset | 偏移量，用于描述当前组件相对于父组件的位置。 |
| [ArkUI\_Node\*](capi-arkui-nativemodule-arkui-node8h.md) | ArkUI\_NodeHandle | 定义ArkUI Native组件实例对象指针，用于在ArkUI Native接口中标识和传递组件实例，例如创建、挂载、移除或销毁组件节点。 |
| [ArkUI\_NodeContent\*](capi-arkui-nativemodule-arkui-nodecontent8h.md) | ArkUI\_NodeContentHandle | 定义ArkUI\_NodeContent在Native侧的实例对象指针，用于在Native接口中引用和传递NodeContent实例。 |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md) | ArkUI\_LayoutConstraint | 布局约束，用于组件布局时进行尺寸范围限制。支持设置最小尺寸和最大尺寸约束，约束值为非负浮点数，在组件布局时，系统会根据约束值限定组件的最终尺寸范围，确保布局结果符合约束条件。适用于自定义布局容器时控制子组件的尺寸范围，如瀑布流布局中限制图片卡片的高度、网格布局中限制单元格尺寸，以及需要限制组件尺寸上下限的场景，如图片展示组件限制最大宽度防止拉伸、响应式布局中限制最小尺寸保证可读性。防止组件尺寸超出预期范围，实现更精确的布局控制，提高布局的可预测性和稳定性，增强界面的可控性。 |
| [ArkUI\_DrawContext](capi-arkui-nativemodule-arkui-drawcontext.md) | ArkUI\_DrawContext | 定义组件绘制上下文的结构体类型，用于在自定义组件绘制过程中提供绘制上下文信息，可获取用于绘制的Canvas指针和可绘制区域大小。 |
| [ArkUI\_Context](capi-arkui-nativemodule-arkui-context.md) | ArkUI\_Context | native UI的上下文实例对象。 |
| [ArkUI\_Context\*](capi-arkui-nativemodule-arkui-context8h.md) | ArkUI\_ContextHandle | ArkUI在Native侧的上下文实例对象指针，用于表示组件所在页面的UIContext。开发者可通过[OH\_ArkUI\_GetContextByNode](capi-native-node-h.md#oh_arkui_getcontextbynode)或[OH\_ArkUI\_GetContextFromNapiValue](capi-native-node-napi-h.md#oh_arkui_getcontextfromnapivalue)获取该指针，并将其作为UI任务调度、动画、焦点控制等接口的上下文入参。 |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md) | ArkUI\_NodeEvent | 定义组件事件的通用结构类型，用于在组件事件处理流程中传递事件信息。 |
