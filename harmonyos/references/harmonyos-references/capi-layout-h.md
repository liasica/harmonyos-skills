---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-layout-h
title: layout.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > layout.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ba0316a2b2a4e9ee68c0829eeb95e60709f640f46d59affd330273887b4956d
---

## 概述

定义布局相关的枚举和接口。

**引用文件：** <arkui/node\_attributes/layout.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [LayoutSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/LayoutSample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md) | ArkUI\_AlignmentRuleOption | 指定设置在相对容器中子组件的对齐规则。 |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md) | ArkUI\_GuidelineOption | Guideline配置选项结构体，用于定义Guideline（RelativeContainer容器内的辅助线）的id、方向和位置。 |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md) | ArkUI\_BarrierOption | barrier选项，用于定义barrier的id、方向和生成时所依赖的组件。 |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md) | ArkUI\_PixelRoundPolicy | 定义组件的像素取整策略结构体。 |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md) | ArkUI\_PositionEdges | 相对容器内容区边界的位置参数。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_Alignment](capi-layout-h.md#arkui_alignment) | ArkUI\_Alignment | 定义布局对齐枚举值。 |
| [ArkUI\_ItemAlignment](capi-layout-h.md#arkui_itemalignment) | ArkUI\_ItemAlignment | 设置子组件在父容器交叉轴的对齐格式枚举值。 |
| [ArkUI\_FlexAlignment](capi-layout-h.md#arkui_flexalignment) | ArkUI\_FlexAlignment | 定义垂直方向对齐方式。 |
| [ArkUI\_FlexDirection](capi-layout-h.md#arkui_flexdirection) | ArkUI\_FlexDirection | 定义Flex容器的主轴方向。 |
| [ArkUI\_FlexWrap](capi-layout-h.md#arkui_flexwrap) | ArkUI\_FlexWrap | 定义Flex行列布局模式。 |
| [ArkUI\_Direction](capi-layout-h.md#arkui_direction) | ArkUI\_Direction | 设置容器元素内主轴方向上的布局枚举值。 |
| [ArkUI\_Axis](capi-layout-h.md#arkui_axis) | ArkUI\_Axis | 定义方向或List组件排列方向枚举值。 |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) | ArkUI\_VerticalAlignment | 定义垂直对齐方式。 |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) | ArkUI\_HorizontalAlignment | 定义语言方向对齐方式。 |
| [ArkUI\_BarrierDirection](capi-layout-h.md#arkui_barrierdirection) | ArkUI\_BarrierDirection | 定义屏障线的方向。 |
| [ArkUI\_RelativeLayoutChainStyle](capi-layout-h.md#arkui_relativelayoutchainstyle) | ArkUI\_RelativeLayoutChainStyle | 定义链的风格。 |
| [ArkUI\_SafeAreaEdge](capi-layout-h.md#arkui_safeareaedge) | ArkUI\_SafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| [ArkUI\_LayoutSafeAreaType](capi-layout-h.md#arkui_layoutsafeareatype) | ArkUI\_LayoutSafeAreaType | 定义扩展安全区域的枚举值。 |
| [ArkUI\_LayoutSafeAreaEdge](capi-layout-h.md#arkui_layoutsafeareaedge) | ArkUI\_LayoutSafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| [ArkUI\_LocalizedAlignment](capi-layout-h.md#arkui_localizedalignment) | ArkUI\_LocalizedAlignment | 定义Stack容器中子组件的对齐规则。 |
| [ArkUI\_LayoutPolicy](capi-layout-h.md#arkui_layoutpolicy) | ArkUI\_LayoutPolicy | 布局策略枚举。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy) | ArkUI\_PixelRoundCalcPolicy | 定义像素取整计算策略枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption\* OH\_ArkUI\_GuidelineOption\_Create(int32\_t size)](capi-layout-h.md#oh_arkui_guidelineoption_create) | 创建RelativeContainer容器内的辅助线信息。 |
| [void OH\_ArkUI\_GuidelineOption\_Dispose(ArkUI\_GuidelineOption\* guideline)](capi-layout-h.md#oh_arkui_guidelineoption_dispose) | 销毁辅助线信息。 |
| [void OH\_ArkUI\_GuidelineOption\_SetId(ArkUI\_GuidelineOption\* guideline, const char\* value, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_setid) | 设置辅助线的Id。 |
| [void OH\_ArkUI\_GuidelineOption\_SetDirection(ArkUI\_GuidelineOption\* guideline, ArkUI\_Axis value, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_setdirection) | 设置辅助线的方向。 |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionStart(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_setpositionstart) | 设置距离容器左侧或者顶部的距离。 |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionEnd(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_setpositionend) | 设置距离容器右侧或者底部的距离。 |
| [const char\* OH\_ArkUI\_GuidelineOption\_GetId(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_getid) | 获取辅助线的Id。 |
| [ArkUI\_Axis OH\_ArkUI\_GuidelineOption\_GetDirection(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_getdirection) | 获取辅助线的方向。 |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionStart(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_getpositionstart) | 获取辅助线距离容器左侧或者顶部的距离。 |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionEnd(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-layout-h.md#oh_arkui_guidelineoption_getpositionend) | 获取辅助线距离容器右侧或者底部的距离。 |
| [ArkUI\_BarrierOption\* OH\_ArkUI\_BarrierOption\_Create(int32\_t size)](capi-layout-h.md#oh_arkui_barrieroption_create) | 创建RelativeContainer容器内的屏障信息。 |
| [void OH\_ArkUI\_BarrierOption\_Dispose(ArkUI\_BarrierOption\* barrierStyle)](capi-layout-h.md#oh_arkui_barrieroption_dispose) | 销毁屏障信息。 |
| [void OH\_ArkUI\_BarrierOption\_SetId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_setid) | 设置屏障的Id。 |
| [void OH\_ArkUI\_BarrierOption\_SetDirection(ArkUI\_BarrierOption\* barrierStyle, ArkUI\_BarrierDirection value, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_setdirection) | 设置屏障的方向。 |
| [void OH\_ArkUI\_BarrierOption\_SetReferencedId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_setreferencedid) | 设置屏障的依赖的组件。 |
| [const char\* OH\_ArkUI\_BarrierOption\_GetId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_getid) | 获取屏障的Id。 |
| [ArkUI\_BarrierDirection OH\_ArkUI\_BarrierOption\_GetDirection(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_getdirection) | 获取屏障的方向。 |
| [const char\* OH\_ArkUI\_BarrierOption\_GetReferencedId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index , int32\_t referencedIndex)](capi-layout-h.md#oh_arkui_barrieroption_getreferencedid) | 获取屏障的依赖的组件。 |
| [int32\_t OH\_ArkUI\_BarrierOption\_GetReferencedIdSize(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-layout-h.md#oh_arkui_barrieroption_getreferencedidsize) | 获取屏障的依赖的组件的个数。 |
| [ArkUI\_AlignmentRuleOption\* OH\_ArkUI\_AlignmentRuleOption\_Create()](capi-layout-h.md#oh_arkui_alignmentruleoption_create) | 创建相对容器中子组件的对齐规则信息。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_Dispose(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_dispose) | 销毁相对容器中子组件的对齐规则信息。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetStart(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_setstart) | 设置相对布局的左对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetEnd(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_setend) | 设置相对布局的右对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_setcenterhorizontal) | 设置相对布局的横向居中对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetTop(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_settop) | 设置相对布局的顶部对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBottom(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_setbottom) | 设置相对布局的底部对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-layout-h.md#oh_arkui_alignmentruleoption_setcentervertical) | 设置相对布局的纵向居中对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option, float horizontal)](capi-layout-h.md#oh_arkui_alignmentruleoption_setbiashorizontal) | 设置组件在锚点约束下的水平方向上偏移参数。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical(ArkUI\_AlignmentRuleOption\* option, float vertical)](capi-layout-h.md#oh_arkui_alignmentruleoption_setbiasvertical) | 设置组件在锚点约束下的垂直方向上偏移参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetStartId(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getstartid) | 获取左对齐参数的Id。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getstartalignment) | 获取左对齐参数的对齐方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetEndId(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getendid) | 获取右对齐参数。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getendalignment) | 获取右对齐参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getcenteridhorizontal) | 获取横向居中对齐方式的参数。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getcenteralignmenthorizontal) | 获取横向居中对齐方式的参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetTopId(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_gettopid) | 获取顶部对齐的参数。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_gettopalignment) | 获取顶部对齐的参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetBottomId(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getbottomid) | 获取底部对齐的参数。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getbottomalignment) | 获取底部对齐的参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getcenteridvertical) | 获取纵向居中对齐方式的参数。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getcenteralignmentvertical) | 获取纵向居中对齐方式的参数。 |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getbiashorizontal) | 获取水平方向上的bias值。 |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical(ArkUI\_AlignmentRuleOption\* option)](capi-layout-h.md#oh_arkui_alignmentruleoption_getbiasvertical) | 获取垂直方向上的bias值。 |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Create()](capi-layout-h.md#oh_arkui_positionedges_create) | 创建PositionEdges属性对象。 |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Copy(const ArkUI\_PositionEdges\* edges)](capi-layout-h.md#oh_arkui_positionedges_copy) | 深拷贝PositionEdges属性对象。 |
| [void OH\_ArkUI\_PositionEdges\_Dispose(ArkUI\_PositionEdges\* edges)](capi-layout-h.md#oh_arkui_positionedges_dispose) | 销毁PositionEdges属性对象。 |
| [void OH\_ArkUI\_PositionEdges\_SetTop(ArkUI\_PositionEdges\* edges, float value)](capi-layout-h.md#oh_arkui_positionedges_settop) | 设置PositionEdges属性对象的上方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetTop(ArkUI\_PositionEdges\* edges, float\* value)](capi-layout-h.md#oh_arkui_positionedges_gettop) | 获取PositionEdges属性对象的上方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetLeft(ArkUI\_PositionEdges\* edges, float value)](capi-layout-h.md#oh_arkui_positionedges_setleft) | 设置PositionEdges属性对象的左方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetLeft(ArkUI\_PositionEdges\* edges, float\* value)](capi-layout-h.md#oh_arkui_positionedges_getleft) | 获取PositionEdges属性对象的左方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetBottom(ArkUI\_PositionEdges\* edges, float value)](capi-layout-h.md#oh_arkui_positionedges_setbottom) | 设置PositionEdges属性对象的下方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetBottom(ArkUI\_PositionEdges\* edges, float\* value)](capi-layout-h.md#oh_arkui_positionedges_getbottom) | 获取PositionEdges属性对象的下方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetRight(ArkUI\_PositionEdges\* edges, float value)](capi-layout-h.md#oh_arkui_positionedges_setright) | 设置PositionEdges属性对象的右方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetRight(ArkUI\_PositionEdges\* edges, float\* value)](capi-layout-h.md#oh_arkui_positionedges_getright) | 获取PositionEdges属性对象的右方向值。 |
| [ArkUI\_PixelRoundPolicy\* OH\_ArkUI\_PixelRoundPolicy\_Create()](capi-layout-h.md#oh_arkui_pixelroundpolicy_create) | 创建PixelRoundPolicy属性对象。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_Dispose(ArkUI\_PixelRoundPolicy\* policy)](capi-layout-h.md#oh_arkui_pixelroundpolicy_dispose) | 释放PixelRoundPolicy属性对象。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_settop) | 设置PixelRoundPolicy属性对象的上部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_gettop) | 获取PixelRoundPolicy属性对象的上部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_setstart) | 设置PixelRoundPolicy属性对象的前部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_getstart) | 获取PixelRoundPolicy属性对象的前部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_setbottom) | 设置PixelRoundPolicy属性对象的下部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_getbottom) | 获取PixelRoundPolicy属性对象的下部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_setend) | 设置PixelRoundPolicy属性对象的尾部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-layout-h.md#oh_arkui_pixelroundpolicy_getend) | 获取PixelRoundPolicy属性对象的尾部方向值。 |

## 枚举类型说明

### ArkUI\_Alignment

```c
enum ArkUI_Alignment
```

**描述**

定义布局对齐枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ALIGNMENT\_TOP\_START = 0 | 顶部起始，该值为默认值。 |
| ARKUI\_ALIGNMENT\_TOP | 顶部居中。 |
| ARKUI\_ALIGNMENT\_TOP\_END | 顶部尾端。 |
| ARKUI\_ALIGNMENT\_START | 起始端纵向居中。 |
| ARKUI\_ALIGNMENT\_CENTER | 横向和纵向居中。 |
| ARKUI\_ALIGNMENT\_END | 尾端纵向居中。 |
| ARKUI\_ALIGNMENT\_BOTTOM\_START | 底部起始端。 |
| ARKUI\_ALIGNMENT\_BOTTOM | 底部横向居中。 |
| ARKUI\_ALIGNMENT\_BOTTOM\_END | 底部尾端。 |

### ArkUI\_ItemAlignment

```c
enum ArkUI_ItemAlignment
```

**描述**

设置子组件在父容器交叉轴的对齐格式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ITEM\_ALIGNMENT\_AUTO = 0 | 使用Flex容器中默认配置，该值为默认值。 |
| ARKUI\_ITEM\_ALIGNMENT\_START | 元素在Flex容器中，交叉轴方向首部对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_CENTER | 元素在Flex容器中，交叉轴方向居中对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_END | 元素在Flex容器中，交叉轴方向底部对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_STRETCH | 元素在Flex容器中，交叉轴方向拉伸填充。 |
| ARKUI\_ITEM\_ALIGNMENT\_BASELINE | 元素在Flex容器中，交叉轴方向文本基线对齐。 |

### ArkUI\_FlexAlignment

```c
enum ArkUI_FlexAlignment
```

**描述**

定义垂直方向对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_ALIGNMENT\_START = 1 | 主轴方向首端对齐，该值为默认值。 |
| ARKUI\_FLEX\_ALIGNMENT\_CENTER = 2 | 主轴方向中心对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_END = 3 | 主轴方向尾部对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_BETWEEN = 6 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素行首对齐，最后的元素行尾对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_AROUND = 7 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素到行首的距离是相邻元素间距离的一半。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_EVENLY = 8 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离、第一个元素到行首的距离和最后的元素到行尾的距离均相等。 |

### ArkUI\_FlexDirection

```c
enum ArkUI_FlexDirection
```

**描述**

定义Flex容器的主轴方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_DIRECTION\_ROW = 0 | 主轴与行方向一致，该值为默认值。 |
| ARKUI\_FLEX\_DIRECTION\_COLUMN | 主轴与列方向一致。 |
| ARKUI\_FLEX\_DIRECTION\_ROW\_REVERSE | 主轴与行方向相反。 |
| ARKUI\_FLEX\_DIRECTION\_COLUMN\_REVERSE | 主轴与列方向相反。 |

### ArkUI\_FlexWrap

```c
enum ArkUI_FlexWrap
```

**描述**

定义Flex行列布局模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_WRAP\_NO\_WRAP = 0 | 单行/单列布局，子项不能超出容器，该值为默认值。 |
| ARKUI\_FLEX\_WRAP\_WRAP | 多行/多列布局，子项允许超出容器。 |
| ARKUI\_FLEX\_WRAP\_WRAP\_REVERSE | 反向多行/多列布局，子项允许超出容器。 |

### ArkUI\_Direction

```c
enum ArkUI_Direction
```

**描述**

设置容器元素内主轴方向上的布局枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DIRECTION\_LTR = 0 | 元素从左到右布局，该值为默认值。 |
| ARKUI\_DIRECTION\_RTL | 元素从右到左布局。 |
| ARKUI\_DIRECTION\_AUTO = 3 | 使用系统布局方向。 |

### ArkUI\_Axis

```c
enum ArkUI_Axis
```

**描述**

定义方向或[List](ts-container-list.md)组件排列方向枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_AXIS\_VERTICAL = 0 | 竖直方向，或者仅支持竖直方向滚动，该值为默认值。 |
| ARKUI\_AXIS\_HORIZONTAL | 水平方向，或者仅支持水平方向滚动。 |

### ArkUI\_VerticalAlignment

```c
enum ArkUI_VerticalAlignment
```

**描述**

定义垂直对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_VERTICAL\_ALIGNMENT\_TOP = 0 | 顶部对齐。 |
| ARKUI\_VERTICAL\_ALIGNMENT\_CENTER | 居中对齐，默认对齐方式。 |
| ARKUI\_VERTICAL\_ALIGNMENT\_BOTTOM | 底部对齐。 |

### ArkUI\_HorizontalAlignment

```c
enum ArkUI_HorizontalAlignment
```

**描述**

定义语言方向对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_START = 0 | 按照语言方向起始端对齐。 |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER | 居中对齐，默认对齐方式。 |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_END | 按照语言方向末端对齐。 |

### ArkUI\_BarrierDirection

```c
enum ArkUI_BarrierDirection
```

**描述**

定义屏障线的方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BARRIER\_DIRECTION\_START = 0 | 屏障在其所有referencedId的最左侧。 |
| ARKUI\_BARRIER\_DIRECTION\_END | 屏障在其所有referencedId的最右侧。 |
| ARKUI\_BARRIER\_DIRECTION\_TOP | 屏障在其所有referencedId的最上方。 |
| ARKUI\_BARRIER\_DIRECTION\_BOTTOM | 屏障在其所有referencedId的最下方。 |

### ArkUI\_RelativeLayoutChainStyle

```c
enum ArkUI_RelativeLayoutChainStyle
```

**描述**

定义链的风格。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD = 0 | 组件在约束锚点间均匀分布，该值为默认值。 |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD\_INSIDE | 除首尾2个子组件的其他组件在约束锚点间均匀分布。 |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_PACKED | 链内子组件无间隙。 |

### ArkUI\_SafeAreaEdge

```c
enum ArkUI_SafeAreaEdge
```

**描述**

定义扩展安全区域的方向的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SAFE\_AREA\_EDGE\_TOP = 1 | 上方区域，该值为默认值。 |
| ARKUI\_SAFE\_AREA\_EDGE\_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI\_SAFE\_AREA\_EDGE\_START = 1 << 2 | 前部区域。 |
| ARKUI\_SAFE\_AREA\_EDGE\_END = 1 << 3 | 尾部区域。 |

### ArkUI\_LayoutSafeAreaType

```c
enum ArkUI_LayoutSafeAreaType
```

**描述**

定义扩展安全区域的枚举值。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUT\_SAFE\_AREA\_TYPE\_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏。 |

### ArkUI\_LayoutSafeAreaEdge

```c
enum ArkUI_LayoutSafeAreaEdge
```

**描述**

定义扩展安全区域的方向的枚举值。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP = 1 | 上方区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_START = 1 << 2 | 前部区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_END = 1 << 3 | 尾部区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_VERTICAL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM | 垂直区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_HORIZONTAL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_START | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_END | 水平区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_ALL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_VERTICAL | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_HORIZONTAL | 全部区域。 |

### ArkUI\_LocalizedAlignment

```c
enum ArkUI_LocalizedAlignment
```

**描述**

定义Stack容器中子组件的对齐规则。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP\_START = 0 | 顶部起始。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP | 顶部居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP\_END | 顶部尾端。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_START | 起始端纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_CENTER | 横向和纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_END | 尾端纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM\_START | 底部起始端。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM | 底部横向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM\_END | 底部尾端。 |

### ArkUI\_LayoutPolicy

```c
enum ArkUI_LayoutPolicy
```

**描述**

布局策略枚举。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUTPOLICY\_MATCHPARENT = 0 | 组件自适应父组件布局。 |
| ARKUI\_LAYOUTPOLICY\_WRAPCONTENT | 组件自适应子组件（内容），且其大小受父组件内容区大小约束。 |
| ARKUI\_LAYOUTPOLICY\_FIXATIDEALSIZE | 组件自适应子组件（内容），且其大小不受父组件内容区大小约束。 |

### ArkUI\_PixelRoundCalcPolicy

```c
enum ArkUI_PixelRoundCalcPolicy
```

**描述**

定义像素取整计算策略枚举。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PIXELROUNDCALCPOLICY\_NOFORCEROUND = 0 | 非取整计算。 |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCECEIL | 向上取整计算。 |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCEFLOOR | 向下取整计算。 |

## 函数说明

### OH\_ArkUI\_GuidelineOption\_Create()

```c
ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size)
```

**描述**

创建RelativeContainer容器内的辅助线信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t size | 辅助线数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GuidelineOption\*](capi-arkui-nativemodule-arkui-guidelineoption.md) | 辅助线信息。 |

### OH\_ArkUI\_GuidelineOption\_Dispose()

```c
void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline)
```

**描述**

销毁辅助线信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |

### OH\_ArkUI\_GuidelineOption\_SetId()

```c
void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index)
```

**描述**

设置辅助线的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| const char\* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetDirection()

```c
void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index)
```

**描述**

设置辅助线的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| [ArkUI\_Axis](capi-layout-h.md#arkui_axis) value | 方向。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetPositionStart()

```c
void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

**描述**

设置距离容器左侧或者顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| float value | 距离容器左侧或者顶部的距离。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetPositionEnd()

```c
void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

**描述**

设置距离容器右侧或者底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| float value | 距离容器右侧或者底部的距离。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_GetId()

```c
const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述**

获取辅助线的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | Id。 |

### OH\_ArkUI\_GuidelineOption\_GetDirection()

```c
ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述**

获取辅助线的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Axis](capi-layout-h.md#arkui_axis) | 方向。 |

### OH\_ArkUI\_GuidelineOption\_GetPositionStart()

```c
float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述**

获取辅助线距离容器左侧或者顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器左侧或者顶部的距离。单位为vp。 |

### OH\_ArkUI\_GuidelineOption\_GetPositionEnd()

```c
float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述**

获取辅助线距离容器右侧或者底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器右侧或者底部的距离。单位为vp。 |

### OH\_ArkUI\_BarrierOption\_Create()

```c
ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size)
```

**描述**

创建RelativeContainer容器内的屏障信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t size | 屏障数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_BarrierOption\*](capi-arkui-nativemodule-arkui-barrieroption.md) | 屏障信息。 |

### OH\_ArkUI\_BarrierOption\_Dispose()

```c
void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle)
```

**描述**

销毁屏障信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |

### OH\_ArkUI\_BarrierOption\_SetId()

```c
void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

**描述**

设置屏障的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| const char\* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_SetDirection()

```c
void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index)
```

**描述**

设置屏障的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| [ArkUI\_BarrierDirection](capi-layout-h.md#arkui_barrierdirection) value | 方向。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_SetReferencedId()

```c
void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

**描述**

设置屏障的依赖的组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| const char\* value | 依赖的组件的Id。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_GetId()

```c
const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述**

获取屏障的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 屏障的Id。 |

### OH\_ArkUI\_BarrierOption\_GetDirection()

```c
ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述**

获取屏障的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_BarrierDirection](capi-layout-h.md#arkui_barrierdirection) | 屏障的方向。 |

### OH\_ArkUI\_BarrierOption\_GetReferencedId()

```c
const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex)
```

**描述**

获取屏障的依赖的组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |
| int32\_t referencedIndex | 依赖的组件Id索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 屏障的依赖的组件。 |

### OH\_ArkUI\_BarrierOption\_GetReferencedIdSize()

```c
int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述**

获取屏障的依赖的组件的个数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 屏障的依赖的组件的个数。 |

### OH\_ArkUI\_AlignmentRuleOption\_Create()

```c
ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create()
```

**描述**

创建相对容器中子组件的对齐规则信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption\*](capi-arkui-nativemodule-arkui-alignmentruleoption.md) | 对齐规则信息。 |

### OH\_ArkUI\_AlignmentRuleOption\_Dispose()

```c
void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option)
```

**描述**

销毁相对容器中子组件的对齐规则信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetStart()

```c
void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述**

设置相对布局的左对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 左对齐锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetEnd()

```c
void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述**

设置相对布局的右对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 右对齐锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal()

```c
void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述**

设置相对布局的横向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 横向居中锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetTop()

```c
void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述**

设置相对布局的顶部对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 顶部对齐锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBottom()

```c
void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述**

设置相对布局的底部对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 底部对齐锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical()

```c
void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述**

设置相对布局的纵向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 纵向居中锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal()

```c
void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal)
```

**描述**

设置组件在锚点约束下的水平方向上偏移参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| float horizontal | 水平方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical()

```c
void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical)
```

**描述**

设置组件在锚点约束下的垂直方向上偏移参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| float vertical | 垂直方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetStartId()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取左对齐参数的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 锚点的组件的id值。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment()

```c
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取左对齐参数的对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) | 参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetEndId()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取右对齐参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 右对齐参数id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment()

```c
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取右对齐参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) | 右对齐参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取横向居中对齐方式的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 横向居中对齐方式的参数的id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal()

```c
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取横向居中对齐方式的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-layout-h.md#arkui_horizontalalignment) | 横向居中对齐方式的参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetTopId()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取顶部对齐的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 顶部对齐的参数id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment()

```c
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取顶部对齐的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) | 顶部对齐的参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBottomId()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取底部对齐的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 底部对齐的参数的id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment()

```c
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取底部对齐的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) | 底部对齐的参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical()

```c
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取纵向居中对齐方式的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 纵向居中对齐方式的参数的id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical()

```c
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取纵向居中对齐方式的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-layout-h.md#arkui_verticalalignment) | 纵向居中对齐方式的参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal()

```c
float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取水平方向上的bias值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 水平方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical()

```c
float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option)
```

**描述**

获取垂直方向上的bias值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 垂直方向上的bias值。 |

### OH\_ArkUI\_PositionEdges\_Create()

```c
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create()
```

**描述**

创建PositionEdges属性对象。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PositionEdges\*](capi-arkui-nativemodule-arkui-positionedges.md) | 指向PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_Copy()

```c
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges)
```

**描述**

深拷贝PositionEdges属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PositionEdges\*](capi-arkui-nativemodule-arkui-positionedges.md) | 指向新PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_Dispose()

```c
void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges)
```

**描述**

销毁PositionEdges属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_SetTop()

```c
void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value)
```

**描述**

设置PositionEdges属性对象的上方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetTop()

```c
int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value)
```

**描述**

获取PositionEdges属性对象的上方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetLeft()

```c
void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value)
```

**描述**

设置PositionEdges属性对象的左方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetLeft()

```c
int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value)
```

**描述**

获取PositionEdges属性对象的左方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetBottom()

```c
void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value)
```

**描述**

设置PositionEdges属性对象的下方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetBottom()

```c
int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value)
```

**描述**

获取PositionEdges属性对象的下方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetRight()

```c
void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value)
```

**描述**

设置PositionEdges属性对象的右方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetRight()

```c
int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value)
```

**描述**

获取PositionEdges属性对象的右方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_Create()

```c
ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create()
```

**描述**

创建PixelRoundPolicy属性对象。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy\*](capi-arkui-nativemodule-arkui-pixelroundpolicy.md) | 指向PixelRoundPolicy对象的指针。 |

### OH\_ArkUI\_PixelRoundPolicy\_Dispose()

```c
void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy)
```

**描述**

释放PixelRoundPolicy属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向要释放的PixelRoundPolicy对象的指针。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetTop()

```c
void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述**

设置PixelRoundPolicy属性对象的上部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetTop()

```c
int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述**

获取PixelRoundPolicy属性对象的上部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetStart()

```c
void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述**

设置PixelRoundPolicy属性对象的前部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetStart()

```c
int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述**

获取PixelRoundPolicy属性对象的前部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetBottom()

```c
void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述**

设置PixelRoundPolicy属性对象的下部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetBottom()

```c
int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述**

获取PixelRoundPolicy属性对象的下部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetEnd()

```c
void OH_ArkUI_PixelRoundPolicy_SetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述**

设置PixelRoundPolicy属性对象的尾部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetEnd()

```c
int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述**

获取PixelRoundPolicy属性对象的尾部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-layout-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数无效。 |
