---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-other
title: ArkUI_NodeAttributeType（其他）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（其他）
category: harmonyos-references
scraped_at: 2026-09-02T14:51:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c51438e00a5030bb01456bbcf14bc58762c694cc87c56bf6e79f8ded8a2d9321
---

```c
enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的其他属性样式集合，包含组件交互、获焦、离屏渲染和点击距离等属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_ENABLED

```c
NODE_ENABLED = 6
```

设置组件是否可交互，支持属性设置、属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示不可交互，1表示可交互。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 返回值为0表示不可交互，返回值为1表示可交互。 |

## NODE\_FOCUSABLE

```c
NODE_FOCUSABLE = 39
```

设置组件是否可获焦，支持属性设置、属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 取值为0或1，参数值为1表示可获焦，为0表示不可获焦。默认为不可获焦。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 返回值为1表示可获焦，为0表示不可获焦。 |

## NODE\_RENDER\_GROUP

```c
NODE_RENDER_GROUP = 80
```

设置当前组件和子组件是否先整体离屏渲染绘制后再与父控件融合绘制，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数值为1表示当前组件与子组件需要先整体离屏渲染绘制后再与父控件融合绘制，参数值为0表示不需要整体离屏渲染绘制后再与父控件融合绘制。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 返回值为1表示当前组件与子组件完成整体离屏渲染绘制，返回值为0表示当前组件与子组件未完成整体离屏渲染绘制。 |

## NODE\_CLICK\_DISTANCE

```c
NODE_CLICK_DISTANCE = 97
```

设置组件点击手势的移动距离限制，支持属性设置。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示识别点击手势时允许手指在设定的距离阈值内移动，取值范围为[0, +∞)，单位为vp。 |

## NODE\_ALLOW\_FORCE\_DARK

```c
NODE_ALLOW_FORCE_DARK = 108
```

设置组件是否启用反色能力，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 反色能力；参数取值为0或1，取值为0表示不启用反色能力，取值为1表示启用反色能力。 |
