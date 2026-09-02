---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-xcomponent
title: ArkUI_NodeAttributeType（XComponent组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（XComponent组件相关属性）
category: harmonyos-references
scraped_at: 2026-09-02T14:51:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dfd426ba29a4feb1de5416c19266ea3b3310e8f2abf1bd46ffab40d59fdb7825
---

```c
enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置或获取的XComponent组件相关属性集合，包括组件ID、组件类型、Surface宽高、Surface显示区域以及是否支持图像分析等属性，适用于需要在Native侧对XComponent组件的渲染区域和行为进行自定义配置与获取的场景。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_XCOMPONENT\_ID

```c
NODE_XCOMPONENT_ID = MAX_NODE_SCOPE_NUM * ARKUI_NODE_XCOMPONENT = 12000
```

XComponent组件的ID，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | XComponent组件的ID内容，用于唯一标识该组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | XComponent组件的ID内容，用于唯一标识该组件。 |

## NODE\_XCOMPONENT\_TYPE

```c
NODE_XCOMPONENT_TYPE = 12001
```

XComponent组件的类型，仅支持属性获取接口。

XComponent组件的类型需要在组件创建时通过[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)中的ARKUI\_NODE\_XCOMPONENT或者ARKUI\_NODE\_XCOMPONENT\_TEXTURE明确，不允许后续修改。

使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改XComponent组件的类型时会发生绘制内容异常。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | XComponent组件的类型，参数类型为[ArkUI\_XComponentType](capi-xcomponent-h.md#arkui_xcomponenttype)，具体枚举值及其与数字的对应关系请参见该枚举定义。 |

## NODE\_XCOMPONENT\_SURFACE\_SIZE

```c
NODE_XCOMPONENT_SURFACE_SIZE = 12002
```

XComponent组件所持有的Surface的宽高，仅支持属性获取接口。

使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改Surface的宽高时，该设置不会生效。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 宽度数值，单位为px。 |
| .value[1].u32 | 高度数值，单位为px。 |

## NODE\_XCOMPONENT\_SURFACE\_RECT

```c
NODE_XCOMPONENT_SURFACE_RECT = 12003
```

XComponent组件所持有的Surface显示区域，支持属性设置和属性获取接口。适用于需要在XComponent组件内指定局部区域进行渲染的场景，例如视频画面裁剪显示、画中画局部渲染等。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位为px。 |
| .value[1].i32 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位为px。 |
| .value[2].i32 | Surface显示区域的宽度，单位为px，取值必须为正整数。传入0或负数时设置不生效。 |
| .value[3].i32 | Surface显示区域的高度，单位为px，取值必须为正整数。传入0或负数时设置不生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位为px。 |
| .value[1].i32 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位为px。 |
| .value[2].i32 | Surface显示区域的宽度，单位为px，取值应为非负整数。 |
| .value[3].i32 | Surface显示区域的高度，单位为px。 |

## NODE\_XCOMPONENT\_ENABLE\_ANALYZER

```c
NODE_XCOMPONENT_ENABLE_ANALYZER = 12004
```

XComponent组件是否支持图像分析的属性，支持属性设置和属性获取接口。开启后可对组件中显示的图像进行内容识别分析，适用于相机预览实时识别、图像内容理解等场景。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析，默认值：0。传入非0和非1的值时按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析。 |
