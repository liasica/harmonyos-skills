---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-render-h
title: native_render.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_render.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0e3539584131cf5e42ddfcfd6ae9e8d80953ed0a1c6440a485337dd1620e9f9
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeRender接口的类型定义。更多详细介绍请参考[构建渲染节点](../harmonyos-guides/ndk-embed-render-components.md)。

**引用文件：** <arkui/native\_render.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**相关模块：** [ArkUI\_RenderNodeUtils](capi-arkui-rendernodeutils.md)

**相关示例：** [NativeRenderNodeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeRenderNodeSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_RenderNode\*](capi-arkui-nativemodule-arkui-rendernodehandle.md) | ArkUI\_RenderNodeHandle | 渲染节点指针。 |
| [ArkUI\_RenderContentModifier\*](kui-nativemodule-arkui-rendercontentmodifierhandle.md) | ArkUI\_RenderContentModifierHandle | 内容修改器指针。 |
| [ArkUI\_FloatProperty\*](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) | ArkUI\_FloatPropertyHandle | 浮点数属性指针。 |
| [ArkUI\_Vector2Property\*](api-arkui-nativemodule-arkui-vector2propertyhandle.md) | ArkUI\_Vector2PropertyHandle | 二维向量属性指针。 |
| [ArkUI\_ColorProperty\*](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) | ArkUI\_ColorPropertyHandle | 颜色属性指针。 |
| [ArkUI\_FloatAnimatableProperty\*](i-nativemodule-arkui-floatanimatablepropertyhandle.md) | ArkUI\_FloatAnimatablePropertyHandle | 可动画的浮点数属性指针。 |
| [ArkUI\_Vector2AnimatableProperty\*](nativemodule-arkui-vector2animatablepropertyhandle.md) | ArkUI\_Vector2AnimatablePropertyHandle | 可动画的二维向量属性指针。 |
| [ArkUI\_ColorAnimatableProperty\*](i-nativemodule-arkui-coloranimatablepropertyhandle.md) | ArkUI\_ColorAnimatablePropertyHandle | 可动画的颜色属性指针。 |
| [ArkUI\_RectShape](capi-arkui-nativemodule-arkui-rectshapeoption.md) | ArkUI\_RectShapeOption | 范围形状结构体。 |
| [ArkUI\_NodeBorderStyle](api-arkui-nativemodule-arkui-nodeborderstyleoption.md) | ArkUI\_NodeBorderStyleOption | 边框样式配置项。 |
| [ArkUI\_NodeBorderWidth](api-arkui-nativemodule-arkui-nodeborderwidthoption.md) | ArkUI\_NodeBorderWidthOption | 边框宽度配置项。 |
| [ArkUI\_NodeBorderColor](api-arkui-nativemodule-arkui-nodebordercoloroption.md) | ArkUI\_NodeBorderColorOption | 边框颜色配置项。 |
| [ArkUI\_NodeBorderRadius](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md) | ArkUI\_NodeBorderRadiusOption | 边框弧度配置项。 |
| [ArkUI\_CircleShape](capi-arkui-nativemodule-arkui-circleshapeoption.md) | ArkUI\_CircleShapeOption | 圆形形状配置项。 |
| [ArkUI\_RoundRectShape](capi-arkui-nativemodule-arkui-roundrectshapeoption.md) | ArkUI\_RoundRectShapeOption | 圆角矩形形状配置项。 |
| [ArkUI\_CommandPath](capi-arkui-nativemodule-arkui-commandpathoption.md) | ArkUI\_CommandPathOption | 自定义路径配置项。 |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | ArkUI\_RenderNodeMaskOption | 节点遮罩配置项。 |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md) | ArkUI\_RenderNodeClipOption | 节点裁剪配置项。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AddRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)](capi-native-render-h.md#oh_arkui_rendernodeutils_addrendernode) | - | 向父自定义节点添加子渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)](capi-native-render-h.md#oh_arkui_rendernodeutils_removerendernode) | - | 从父节点移除指定的子渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearRenderNodeChildren(ArkUI\_NodeHandle node)](capi-native-render-h.md#oh_arkui_rendernodeutils_clearrendernodechildren) | - | 清除父节点内的子渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_Invalidate(ArkUI\_NodeHandle node)](capi-native-render-h.md#oh_arkui_rendernodeutils_invalidate) | - | 标记目标节点，触发其生命周期和子节点的重新渲染。 |
| [ArkUI\_RenderNodeHandle OH\_ArkUI\_RenderNodeUtils\_CreateNode()](capi-native-render-h.md#oh_arkui_rendernodeutils_createnode) | - | 创建渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_DisposeNode(ArkUI\_RenderNodeHandle node)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenode) | - | 销毁渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AddChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)](capi-native-render-h.md#oh_arkui_rendernodeutils_addchild) | - | 向目标父渲染节点上添加子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_InsertChildAfter(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child, ArkUI\_RenderNodeHandle sibling)](capi-native-render-h.md#oh_arkui_rendernodeutils_insertchildafter) | - | 向父节点的目标子节点后添加子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)](capi-native-render-h.md#oh_arkui_rendernodeutils_removechild) | - | 从指定渲染节点中移除子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearChildren(ArkUI\_RenderNodeHandle node)](capi-native-render-h.md#oh_arkui_rendernodeutils_clearchildren) | - | 清空指定渲染节点的所有子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChild(ArkUI\_RenderNodeHandle node, int32\_t index, ArkUI\_RenderNodeHandle\* child)](capi-native-render-h.md#oh_arkui_rendernodeutils_getchild) | - | 获取指定索引位置的子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFirstChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* child)](capi-native-render-h.md#oh_arkui_rendernodeutils_getfirstchild) | - | 获取指定渲染节点的第一个子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetNextSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)](capi-native-render-h.md#oh_arkui_rendernodeutils_getnextsibling) | - | 获取指定节点的下一个兄弟节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPreviousSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)](capi-native-render-h.md#oh_arkui_rendernodeutils_getprevioussibling) | - | 获取指定节点的上一个兄弟节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildren(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\*\* children, int32\_t\* count)](capi-native-render-h.md#oh_arkui_rendernodeutils_getchildren) | - | 获取父渲染节点的所有子渲染节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildrenCount(ArkUI\_RenderNodeHandle node, int32\_t\* count)](capi-native-render-h.md#oh_arkui_rendernodeutils_getchildrencount) | - | 获取指定渲染节点的子渲染节点数量。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t color)](capi-native-render-h.md#oh_arkui_rendernodeutils_setbackgroundcolor) | - | 为渲染节点设置背景颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)](capi-native-render-h.md#oh_arkui_rendernodeutils_getbackgroundcolor) | - | 获取渲染节点的背景颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t clipToFrame)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcliptoframe) | - | 设置是否对当前渲染节点裁剪。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t\* clipToFrame)](capi-native-render-h.md#oh_arkui_rendernodeutils_getcliptoframe) | - | 获取是否对当前渲染节点裁剪。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t clipToBounds)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcliptobounds) | - | 设置是否对当前渲染节点边界裁剪。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t\* clipToBounds)](capi-native-render-h.md#oh_arkui_rendernodeutils_getcliptobounds) | - | 获取是否对当前渲染节点边界裁剪。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetOpacity(ArkUI\_RenderNodeHandle node, float opacity)](capi-native-render-h.md#oh_arkui_rendernodeutils_setopacity) | - | 为渲染节点设置不透明度值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetOpacity(ArkUI\_RenderNodeHandle node, float\* opacity)](capi-native-render-h.md#oh_arkui_rendernodeutils_getopacity) | - | 获取渲染节点的不透明度值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetSize(ArkUI\_RenderNodeHandle node, int32\_t width, int32\_t height)](capi-native-render-h.md#oh_arkui_rendernodeutils_setsize) | - | 为渲染节点设置尺寸。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetSize(ArkUI\_RenderNodeHandle node, int32\_t\* width, int32\_t\* height)](capi-native-render-h.md#oh_arkui_rendernodeutils_getsize) | - | 获取渲染节点的尺寸。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPosition(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setposition) | - | 为渲染节点设置位置坐标。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPosition(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getposition) | - | 获取渲染节点的位置坐标。该坐标是渲染节点布局后相对父节点的位置偏移，单位为px。该坐标是父节点对该节点进行布局之后的结果，因此布局之后生效的offset属性和不参与布局的position属性不影响该坐标。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPivot(ArkUI\_RenderNodeHandle node, float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setpivot) | - | 为渲染节点的变换设置中心点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPivot(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getpivot) | - | 获取渲染节点的中心点坐标。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetScale(ArkUI\_RenderNodeHandle node, float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setscale) | - | 为渲染节点设置缩放因子。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetScale(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getscale) | - | 获取渲染节点的缩放因子。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTranslation(ArkUI\_RenderNodeHandle node, float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_settranslation) | - | 为渲染节点设置平移偏移量。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetTranslation(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_gettranslation) | - | 获取渲染节点的平移偏移量。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetRotation(ArkUI\_RenderNodeHandle node, float x, float y, float z)](capi-native-render-h.md#oh_arkui_rendernodeutils_setrotation) | - | 为渲染节点设置旋转角度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetRotation(ArkUI\_RenderNodeHandle node, float\* x, float\* y, float\* z)](capi-native-render-h.md#oh_arkui_rendernodeutils_getrotation) | - | 获取渲染节点的旋转角度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTransform(ArkUI\_RenderNodeHandle node, float\* matrix)](capi-native-render-h.md#oh_arkui_rendernodeutils_settransform) | - | 为渲染节点设置变换矩阵。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t color)](capi-native-render-h.md#oh_arkui_rendernodeutils_setshadowcolor) | - | 为渲染节点设置阴影颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)](capi-native-render-h.md#oh_arkui_rendernodeutils_getshadowcolor) | - | 获取渲染节点的阴影颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setshadowoffset) | - | 为渲染节点设置阴影偏移量。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getshadowoffset) | - | 获取渲染节点的阴影偏移量。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowAlpha(ArkUI\_RenderNodeHandle node, float alpha)](capi-native-render-h.md#oh_arkui_rendernodeutils_setshadowalpha) | - | 为渲染节点设置阴影透明度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowAlpha(ArkUI\_RenderNodeHandle node, float\* alpha)](capi-native-render-h.md#oh_arkui_rendernodeutils_getshadowalpha) | - | 获取渲染节点的阴影透明度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowElevation(ArkUI\_RenderNodeHandle node, float elevation)](capi-native-render-h.md#oh_arkui_rendernodeutils_setshadowelevation) | - | 为渲染节点设置阴影高度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowElevation(ArkUI\_RenderNodeHandle node, float\* elevation)](capi-native-render-h.md#oh_arkui_rendernodeutils_getshadowelevation) | - | 获取渲染节点的阴影高度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowRadius(ArkUI\_RenderNodeHandle node, float radius)](capi-native-render-h.md#oh_arkui_rendernodeutils_setshadowradius) | - | 为渲染节点设置阴影半径。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowRadius(ArkUI\_RenderNodeHandle node, float\* radius)](capi-native-render-h.md#oh_arkui_rendernodeutils_getshadowradius) | - | 获取渲染节点的阴影半径。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\* borderStyle)](capi-native-render-h.md#oh_arkui_rendernodeutils_setborderstyle) | - | 为渲染节点设置边框样式。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\*\* borderStyle)](capi-native-render-h.md#oh_arkui_rendernodeutils_getborderstyle) | - | 获取渲染节点的边框样式。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\* borderWidth)](capi-native-render-h.md#oh_arkui_rendernodeutils_setborderwidth) | - | 为渲染节点设置边框宽度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\*\* borderWidth)](capi-native-render-h.md#oh_arkui_rendernodeutils_getborderwidth) | - | 获取渲染节点的边框宽度。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\* borderColor)](capi-native-render-h.md#oh_arkui_rendernodeutils_setbordercolor) | - | 为渲染节点设置边框颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\*\* borderColor)](capi-native-render-h.md#oh_arkui_rendernodeutils_getbordercolor) | - | 获取渲染节点的边框颜色。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\* borderRadius)](capi-native-render-h.md#oh_arkui_rendernodeutils_setborderradius) | - | 为渲染节点设置边框角半径。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\*\* borderRadius)](capi-native-render-h.md#oh_arkui_rendernodeutils_getborderradius) | - | 获取渲染节点的边框角半径。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMask(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeMaskOption\* mask)](capi-native-render-h.md#oh_arkui_rendernodeutils_setmask) | - | 使用遮罩配置为渲染节点应用遮罩。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClip(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeClipOption\* clip)](capi-native-render-h.md#oh_arkui_rendernodeutils_setclip) | - | 使用裁剪配置为渲染节点应用裁剪。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMarkNodeGroup(ArkUI\_RenderNodeHandle node, bool markNodeGroup)](capi-native-render-h.md#oh_arkui_rendernodeutils_setmarknodegroup) | - | 标记是否优先绘制该节点及其子节点。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBounds(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y, int32\_t width, int32\_t height)](capi-native-render-h.md#oh_arkui_rendernodeutils_setbounds) | - | 为渲染节点设置边界。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBounds(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y, int32\_t\* width, int32\_t\* height)](capi-native-render-h.md#oh_arkui_rendernodeutils_getbounds) | - | 获取渲染节点的边界。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetDrawRegion(ArkUI\_RenderNodeHandle node, float x, float y, float w, float h)](capi-native-render-h.md#oh_arkui_rendernodeutils_setdrawregion) | - | 为渲染节点设置绘制区域。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier(ArkUI\_RenderNodeHandle node, ArkUI\_RenderContentModifierHandle modifier)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachcontentmodifier) | - | 为渲染节点添加内容修改器。 |
| [ArkUI\_RenderContentModifierHandle OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier()](capi-native-render-h.md#oh_arkui_rendernodeutils_createcontentmodifier) | - | 创建内容修改器。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeContentModifier(ArkUI\_RenderContentModifierHandle modifier)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposecontentmodifier) | - | 释放内容修改器。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatPropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachfloatproperty) | - | 为目标内容修改器附加浮点属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2Property(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2PropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachvector2property) | - | 为目标内容修改器附加二维向量属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorPropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachcolorproperty) | - | 为目标内容修改器附加颜色属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatAnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachfloatanimatableproperty) | - | 为目标内容修改器附加可动画的浮点属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2AnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachvector2animatableproperty) | - | 为目标内容修改器附加可动画的二维向量属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorAnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_attachcoloranimatableproperty) | - | 为目标内容修改器附加可动画的颜色属性。 |
| [ArkUI\_FloatPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatProperty(float value)](capi-native-render-h.md#oh_arkui_rendernodeutils_createfloatproperty) | - | 创建浮点属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float value)](capi-native-render-h.md#oh_arkui_rendernodeutils_setfloatpropertyvalue) | - | 设置浮点属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float\* value)](capi-native-render-h.md#oh_arkui_rendernodeutils_getfloatpropertyvalue) | - | 获取浮点属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatProperty(ArkUI\_FloatPropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposefloatproperty) | - | 释放浮点属性。 |
| [ArkUI\_Vector2PropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2Property(float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_createvector2property) | - | 创建二维向量属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setvector2propertyvalue) | - | 设置二维向量属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float\* x, float\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getvector2propertyvalue) | - | 获取二维向量属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2Property(ArkUI\_Vector2PropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposevector2property) | - | 释放二维向量属性。 |
| [ArkUI\_ColorPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorProperty(uint32\_t value)](capi-native-render-h.md#oh_arkui_rendernodeutils_createcolorproperty) | - | 创建颜色属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t value)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcolorpropertyvalue) | - | 设置颜色属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t\* value)](capi-native-render-h.md#oh_arkui_rendernodeutils_getcolorpropertyvalue) | - | 获取颜色属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeColorProperty(ArkUI\_ColorPropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposecolorproperty) | - | 释放颜色属性。 |
| [ArkUI\_FloatAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty(float value)](capi-native-render-h.md#oh_arkui_rendernodeutils_createfloatanimatableproperty) | - | 创建可动画的浮点属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float value)](capi-native-render-h.md#oh_arkui_rendernodeutils_setfloatanimatablepropertyvalue) | - | 设置可动画的浮点属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float\* value)](capi-native-render-h.md#oh_arkui_rendernodeutils_getfloatanimatablepropertyvalue) | - | 获取可动画的浮点属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatAnimatableProperty(ArkUI\_FloatAnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposefloatanimatableproperty) | - | 释放可动画的浮点属性。 |
| [ArkUI\_Vector2AnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty(float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_createvector2animatableproperty) | - | 创建可动画的二维向量属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float x, float y)](capi-native-render-h.md#oh_arkui_rendernodeutils_setvector2animatablepropertyvalue) | - | 设置可动画的二维向量属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float\* x, float\* y)](capi-native-render-h.md#oh_arkui_rendernodeutils_getvector2animatablepropertyvalue) | - | 获取可动画的二维向量属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2AnimatableProperty(ArkUI\_Vector2AnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposevector2animatableproperty) | - | 释放可动画的二维向量属性。 |
| [ArkUI\_ColorAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty(uint32\_t value)](capi-native-render-h.md#oh_arkui_rendernodeutils_createcoloranimatableproperty) | - | 创建可动画的颜色属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t value)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcoloranimatablepropertyvalue) | - | 设置可动画的颜色属性的值。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t\* value)](capi-native-render-h.md#oh_arkui_rendernodeutils_getcoloranimatablepropertyvalue) | - | 获取可动画的颜色属性的值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeColorAnimatableProperty(ArkUI\_ColorAnimatablePropertyHandle property)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposecoloranimatableproperty) | - | 释放可动画的颜色属性。 |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw(ArkUI\_RenderContentModifierHandle modifier, void\* userData, void (callback)(ArkUI\_DrawContext\* context, void userData))](capi-native-render-h.md#oh_arkui_rendernodeutils_setcontentmodifierondraw) | - | 设置内容修改器的onDraw函数。 |
| [ArkUI\_RectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRectShapeOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createrectshapeoption) | - | 创建矩形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRectShapeOption(ArkUI\_RectShapeOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposerectshapeoption) | - | 释放矩形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRectShapeOptionEdgeValue(ArkUI\_RectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setrectshapeoptionedgevalue) | - | 设置矩形形状的边缘值。 |
| [ArkUI\_NodeBorderStyleOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createnodeborderstyleoption) | - | 创建节点边框样式。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption(ArkUI\_NodeBorderStyleOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenodeborderstyleoption) | - | 释放节点边框样式。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle(ArkUI\_NodeBorderStyleOption\* option, ArkUI\_BorderStyle edgeStyle, ArkUI\_EdgeDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setnodeborderstyleoptionedgestyle) | - | 设置节点边框样式的边缘值。 |
| [ArkUI\_NodeBorderWidthOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createnodeborderwidthoption) | - | 创建节点边框宽度。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption(ArkUI\_NodeBorderWidthOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenodeborderwidthoption) | - | 释放节点边框宽度。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth(ArkUI\_NodeBorderWidthOption\* option, float edgeWidth, ArkUI\_EdgeDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setnodeborderwidthoptionedgewidth) | - | 设置节点边框宽度的边缘值。 |
| [ArkUI\_NodeBorderColorOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createnodebordercoloroption) | - | 创建节点边框颜色。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption(ArkUI\_NodeBorderColorOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenodebordercoloroption) | - | 释放节点边框颜色。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor(ArkUI\_NodeBorderColorOption\* option, uint32\_t edgeColor, ArkUI\_EdgeDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setnodebordercoloroptionedgecolor) | - | 设置节点边框颜色的边缘值。 |
| [ArkUI\_NodeBorderRadiusOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderRadiusOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createnodeborderradiusoption) | - | 创建节点边框半径。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderRadiusOption(ArkUI\_NodeBorderRadiusOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenodeborderradiusoption) | - | 释放节点边框半径。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderRadiusOptionCornerRadius(ArkUI\_NodeBorderRadiusOption\* option, uint32\_t cornerRadius, ArkUI\_CornerDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setnodeborderradiusoptioncornerradius) | - | 设置节点边框半径的边缘值。 |
| [ArkUI\_CircleShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCircleShapeOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createcircleshapeoption) | - | 创建圆形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeCircleShapeOption(ArkUI\_CircleShapeOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposecircleshapeoption) | - | 释放圆形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterX(ArkUI\_CircleShapeOption\* option, float centerX)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcircleshapeoptioncenterx) | - | 设置圆形形状的圆心x轴坐标值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterY(ArkUI\_CircleShapeOption\* option, float centerY)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcircleshapeoptioncentery) | - | 设置圆形形状的圆心y轴坐标值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionRadius(ArkUI\_CircleShapeOption\* option, float radius)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcircleshapeoptionradius) | - | 设置圆形形状的半径值。 |
| [ArkUI\_RoundRectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRoundRectShapeOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createroundrectshapeoption) | - | 创建圆角矩形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRoundRectShapeOption(ArkUI\_RoundRectShapeOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposeroundrectshapeoption) | - | 释放圆角矩形形状。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionEdgeValue(ArkUI\_RoundRectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setroundrectshapeoptionedgevalue) | - | 设置圆角矩形形状的边缘值。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionCornerXY(ArkUI\_RoundRectShapeOption\* option, float x, float y, ArkUI\_CornerDirection direction)](capi-native-render-h.md#oh_arkui_rendernodeutils_setroundrectshapeoptioncornerxy) | - | 设置目标角的坐标值。 |
| [ArkUI\_CommandPathOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCommandPathOption()](capi-native-render-h.md#oh_arkui_rendernodeutils_createcommandpathoption) | - | 创建自定义绘制路径。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeCommandPathOption(ArkUI\_CommandPathOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposecommandpathoption) | - | 释放自定义绘制路径。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCommandPathOptionCommands(ArkUI\_CommandPathOption\* option, char\* commands)](capi-native-render-h.md#oh_arkui_rendernodeutils_setcommandpathoptioncommands) | - | 设置自定义绘制路径的命令值。 |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRectShape(ArkUI\_RectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodemaskoptionfromrectshape) | - | 从矩形形状创建遮罩。 |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodemaskoptionfromroundrectshape) | - | 从圆角矩形形状创建遮罩。 |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodemaskoptionfromcircleshape) | - | 从圆形形状创建遮罩。 |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodemaskoptionfromovalshape) | - | 从椭圆形形状创建遮罩。 |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCommandPath(ArkUI\_CommandPathOption\* path)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodemaskoptionfromcommandpath) | - | 从自定义绘制路径创建遮罩。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeMaskOption(ArkUI\_RenderNodeMaskOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposerendernodemaskoption) | - | 释放渲染节点遮罩。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionFillColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t fillColor)](capi-native-render-h.md#oh_arkui_rendernodeutils_setrendernodemaskoptionfillcolor) | - | 设置渲染节点遮罩的填充颜色。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t strokeColor)](capi-native-render-h.md#oh_arkui_rendernodeutils_setrendernodemaskoptionstrokecolor) | - | 设置渲染节点遮罩的描边颜色。 |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeWidth(ArkUI\_RenderNodeMaskOption\* mask, float strokeWidth)](capi-native-render-h.md#oh_arkui_rendernodeutils_setrendernodemaskoptionstrokewidth) | - | 设置渲染节点遮罩的描边宽度。 |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRectShape(ArkUI\_RectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodeclipoptionfromrectshape) | - | 从矩形形状创建裁剪。 |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodeclipoptionfromroundrectshape) | - | 从圆角矩形形状创建裁剪。 |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodeclipoptionfromcircleshape) | - | 从圆形形状创建裁剪。 |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodeclipoptionfromovalshape) | - | 从椭圆形形状创建裁剪。 |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCommandPath(ArkUI\_CommandPathOption\* path)](capi-native-render-h.md#oh_arkui_rendernodeutils_createrendernodeclipoptionfromcommandpath) | - | 从自定义绘制路径创建裁剪。 |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeClipOption(ArkUI\_RenderNodeClipOption\* option)](capi-native-render-h.md#oh_arkui_rendernodeutils_disposerendernodeclipoption) | - | 释放渲染节点裁剪。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_RenderNodeUtils\_AddRenderNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AddRenderNode(ArkUI_NodeHandle node, ArkUI_RenderNodeHandle child)
```

**描述：**

向父自定义节点添加子渲染节点。

父节点仅支持[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)中ARKUI\_NODE\_CUSTOM类型的节点，每个自定义节点只能挂载一个ArkUI\_RenderNodeHandle，customNode无法挂载其他ArkUI\_NodeHandle。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标父节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) child | 待添加的子渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点非自定义节点。  [ARKUI\_ERROR\_CODE\_CHILD\_EXISTED](capi-native-type-h.md#arkui_errorcode) 目标节点已存在子节点。  [ARKUI\_ERROR\_CODE\_RENDER\_PARENT\_EXISTED](capi-native-type-h.md#arkui_errorcode) 目标渲染节点存在父节点。  [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_RemoveRenderNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_RemoveRenderNode(ArkUI_NodeHandle node, ArkUI_RenderNodeHandle child)
```

**描述：**

从父节点移除指定的子渲染节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标父节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) child | 移除的目标子渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点非自定义节点。 |

### OH\_ArkUI\_RenderNodeUtils\_ClearRenderNodeChildren()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_ClearRenderNodeChildren(ArkUI_NodeHandle node)
```

**描述：**

清除父节点内的子渲染节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标父节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点非自定义节点。 |

### OH\_ArkUI\_RenderNodeUtils\_Invalidate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_Invalidate(ArkUI_NodeHandle node)
```

**描述：**

标记目标节点，触发其生命周期和子节点的重新渲染。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeHandle OH_ArkUI_RenderNodeUtils_CreateNode()
```

**描述：**

创建渲染节点。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) | 目标渲染节点。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_DisposeNode(ArkUI_RenderNodeHandle node)
```

**描述：**

销毁渲染节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AddChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AddChild(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle child)
```

**描述：**

向目标父渲染节点上添加子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) child | 目标添加子渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。  [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_InsertChildAfter()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_InsertChildAfter(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle child, ArkUI_RenderNodeHandle sibling)
```

**描述：**

向父节点的目标子节点后添加子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) child | 待添加的子渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) sibling | 目标子节点，用于确定插入位置的参考兄弟渲染节点。若该节点不在node的当前子节点列表中，则将child追加到末尾。 |
| **返回：** |  |

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。  [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_RemoveChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_RemoveChild(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle child)
```

**描述：**

从指定渲染节点中移除子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) child | 目标被移除子渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_ClearChildren()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_ClearChildren(ArkUI_RenderNodeHandle node)
```

**描述：**

清空指定渲染节点的所有子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetChild(ArkUI_RenderNodeHandle node, int32_t index, ArkUI_RenderNodeHandle* child)
```

**描述：**

获取指定索引位置的子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| int32\_t index | 子节点的从零开始的索引。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\* child | 用于接收子节点的渲染节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](capi-native-type-h.md#arkui_errorcode) 未找到对应的渲染子节点。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetFirstChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetFirstChild(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle* child)
```

**描述：**

获取指定渲染节点的第一个子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\* child | 用于接收第一个子节点的渲染节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](capi-native-type-h.md#arkui_errorcode) 未找到对应的渲染子节点。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetNextSibling()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetNextSibling(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle* sibling)
```

**描述：**

获取指定节点的下一个兄弟节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 参考节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\* sibling | 用于接收下一个兄弟节点的渲染节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](capi-native-type-h.md#arkui_errorcode) 未找到对应的渲染子节点。 |

### OH\_ArkUI\_RenderNodeUtils\_GetPreviousSibling()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetPreviousSibling(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle* sibling)
```

**描述：**

获取指定节点的上一个兄弟节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 参考节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\* sibling | 用于接收上一个兄弟节点的渲染节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](capi-native-type-h.md#arkui_errorcode) 未找到对应的渲染子节点。 |

### OH\_ArkUI\_RenderNodeUtils\_GetChildren()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetChildren(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeHandle** children, int32_t* count)
```

**描述：**

获取父渲染节点的所有子渲染节点，调用者负责释放返回的子节点数组。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\*\* children | 用于存储所有子渲染节点的指针数组。 |
| int32\_t\* count | 用于存储获取到的子节点数量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetChildrenCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetChildrenCount(ArkUI_RenderNodeHandle node, int32_t* count)
```

**描述：**

获取指定渲染节点的子渲染节点数量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标父渲染节点。 |
| int32\_t\* count | 用于存储子节点数量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBackgroundColor(ArkUI_RenderNodeHandle node, uint32_t color)
```

**描述：**

为渲染节点设置背景颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| uint32\_t color | ARGB 颜色值（32 位无符号整数）。  默认值：0x00000000。  **颜色字节布局说明：**  - 位24-31：Alpha通道（0x00完全透明，0xFF完全不透明）。  - 位16-23：红色通道。  - 位8-15：绿色通道。  - 位0-7：蓝色通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBackgroundColor(ArkUI_RenderNodeHandle node, uint32_t* color)
```

**描述：**

获取渲染节点的背景颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| uint32\_t\* color | 用于存储获取到的 RGBA 颜色值的整数指针。  默认值：0x00000000。  **颜色字节布局说明：**  - 位24-31：Alpha通道（0x00完全透明，0xFF完全不透明）。  - 位16-23：红色通道。  - 位8-15：绿色通道。  - 位0-7：蓝色通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetClipToFrame()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetClipToFrame(ArkUI_RenderNodeHandle node, int32_t clipToFrame)
```

**描述：**

设置是否对当前渲染节点裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t clipToFrame | 整数（1 = 裁剪到框架，0 = 不裁剪）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数值超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetClipToFrame()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetClipToFrame(ArkUI_RenderNodeHandle node, int32_t* clipToFrame)
```

**描述：**

获取是否对当前渲染节点裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* clipToFrame | 用于接收裁剪状态（1 或 0）的整数指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetClipToBounds()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetClipToBounds(ArkUI_RenderNodeHandle node, int32_t clipToBounds)
```

**描述：**

设置是否对当前渲染节点边界裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t clipToBounds | 裁剪标志（1：裁剪到边界，0：不裁剪）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数值超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetClipToBounds()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetClipToBounds(ArkUI_RenderNodeHandle node, int32_t* clipToBounds)
```

**描述：**

获取是否对当前渲染节点边界裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* clipToBounds | 整数指针（1 = 根据边界裁剪，0 = 不裁剪）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetOpacity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetOpacity(ArkUI_RenderNodeHandle node, float opacity)
```

**描述：**

为渲染节点设置不透明度值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float opacity | 不透明度值（0.0-1.0）。  默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数值超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetOpacity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetOpacity(ArkUI_RenderNodeHandle node, float* opacity)
```

**描述：**

获取渲染节点的不透明度值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* opacity | 用于接收不透明度值（0.0-1.0）的指针。  默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetSize(ArkUI_RenderNodeHandle node, int32_t width, int32_t height)
```

**描述：**

为渲染节点设置尺寸。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t width | 宽度值（以像素为单位）。  默认值：0，单位：px。取值大于等于0，传入负值时返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)。 |
| int32\_t height | 高度值（以像素为单位）。  默认值：0，单位：px。取值大于等于0，传入负值时返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数值超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetSize(ArkUI_RenderNodeHandle node, int32_t* width, int32_t* height)
```

**描述：**

获取渲染节点的尺寸。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* width | 用于接收宽度值（以像素为单位）的指针。  默认值：0，单位：px。 |
| int32\_t\* height | 用于接收高度值（以像素为单位）的指针。  默认值：0，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetPosition(ArkUI_RenderNodeHandle node, int32_t x, int32_t y)
```

**描述：**

为渲染节点设置位置坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t x | X坐标值（以像素为单位）。  默认值：0，单位：px。 |
| int32\_t y | Y坐标值（以像素为单位）。  默认值：0，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetPosition(ArkUI_RenderNodeHandle node, int32_t* x, int32_t* y)
```

**描述：**

获取渲染节点的位置坐标。该坐标是渲染节点布局后相对父节点的位置偏移，单位为px。该坐标是父节点对该节点进行布局之后的结果，因此布局之后生效的offset属性和不参与布局的position属性不影响该坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* x | 用于接收X坐标值（以像素为单位）的指针。  默认值：0，单位：px。 |
| int32\_t\* y | 用于接收Y坐标值（以像素为单位）的指针。  默认值：0，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetPivot()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetPivot(ArkUI_RenderNodeHandle node, float x, float y)
```

**描述：**

为渲染节点的变换设置中心点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float x | 中心点的X坐标（标准取值范围：0.0-1.0）。  默认值：0.5。 |
| float y | 中心点的Y坐标（标准取值范围：0.0-1.0）。  默认值：0.5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetPivot()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetPivot(ArkUI_RenderNodeHandle node, float* x, float* y)
```

**描述：**

获取渲染节点的中心点坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* x | 用于接收中心点X坐标的指针。  默认值：0.5。 |
| float\* y | 用于接收中心点Y坐标的指针。  默认值：0.5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetScale()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetScale(ArkUI_RenderNodeHandle node, float x, float y)
```

**描述：**

为渲染节点设置缩放因子。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float x | 水平缩放因子。  默认值：1。 |
| float y | 垂直缩放因子。  默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetScale()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetScale(ArkUI_RenderNodeHandle node, float* x, float* y)
```

**描述：**

获取渲染节点的缩放因子。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* x | 用于接收水平缩放因子的指针。  默认值：1。 |
| float\* y | 用于接收垂直缩放因子的指针。  默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetTranslation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetTranslation(ArkUI_RenderNodeHandle node, float x, float y)
```

**描述：**

为渲染节点设置平移偏移量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float x | 水平平移量（以像素为单位）。  默认值：0。 |
| float y | 垂直平移量（以像素为单位）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetTranslation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetTranslation(ArkUI_RenderNodeHandle node, float* x, float* y)
```

**描述：**

获取渲染节点的平移偏移量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* x | 用于接收水平平移量的指针。  默认值：0。 |
| float\* y | 用于接收垂直平移量的指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRotation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetRotation(ArkUI_RenderNodeHandle node, float x, float y, float z)
```

**描述：**

为渲染节点设置旋转角度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float x | 绕X轴的旋转角度（以度为单位）。  默认值：0。 |
| float y | 绕Y轴的旋转角度（以度为单位）。  默认值：0。 |
| float z | 绕Z轴的旋转角度（以度为单位）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetRotation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetRotation(ArkUI_RenderNodeHandle node, float* x, float* y, float* z)
```

**描述：**

获取渲染节点的旋转角度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* x | 用于接收绕X轴旋转角度（以度为单位）的指针。  默认值：0。 |
| float\* y | 用于接收绕Y轴旋转角度（以度为单位）的指针。  默认值：0。 |
| float\* z | 用于接收绕Z轴旋转角度（以度为单位）的指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetTransform()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetTransform(ArkUI_RenderNodeHandle node, float* matrix)
```

**描述：**

为渲染节点设置变换矩阵。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* matrix | 4x4 变换矩阵的浮点数数组（16 个连续值）。 |

变换矩阵应作为 16 个连续的浮点值以行优先顺序提供：

[m00, m01, m02, m03,

m10, m11, m12, m13,

m20, m21, m22, m23,

m30, m31, m32, m33]

其中矩阵表示为：

| m00 m01 m02 m03 |

| m10 m11 m12 m13 |

| m20 m21 m22 m23 |

| m30 m31 m32 m33 |

矩阵组件：

| 矩阵单元 | 描述 |
| --- | --- |
| m00 | x轴的缩放值。单位矩阵的默认值为1。 |
| m01 | 第二个值，受 x、y、z 轴的旋转或倾斜影响。 |
| m02 | 第三个值，受 x、y、z 轴的旋转影响。 |
| m03 | 第四个值，受透视投影影响。 |
| m10 | 第五个值，受 x、y、z 轴的旋转或倾斜影响。 |
| m11 | y轴的缩放值。单位矩阵的默认值为1。 |
| m12 | 第七个值，受 x、y、z 轴的旋转影响。 |
| m13 | 第八个值，受透视投影影响。 |
| m20 | 第九个值，受 x、y、z 轴的旋转影响。 |
| m21 | 第十个值，受 x、y、z 轴的旋转影响。 |
| m22 | z轴的缩放值。单位矩阵的默认值为1。 |
| m23 | 第 12 个值，受透视投影影响。 |
| m30 | x轴的平移值（以 px 为单位）。单位矩阵的默认值为0。 |
| m31 | y轴的平移值（以 px 为单位）。单位矩阵的默认值为0。 |
| m32 | z轴的平移值（以 px 为单位）。单位矩阵的默认值为0。 |
| m33 | 在齐次坐标中有效，呈现透视投影效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetShadowColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetShadowColor(ArkUI_RenderNodeHandle node, uint32_t color)
```

**描述：**

为渲染节点设置阴影颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| uint32\_t color | ARGB 颜色值（32位无符号整数）。  默认值：0x00000000。  **颜色字节布局说明：**  - 位24-31：Alpha通道（0x00完全透明，0xFF完全不透明）。  - 位16-23：红色通道。  - 位8-15：绿色通道。  - 位0-7：蓝色通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetShadowColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetShadowColor(ArkUI_RenderNodeHandle node, uint32_t* color)
```

**描述：**

获取渲染节点的阴影颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| uint32\_t\* color | 用于存储获取到的RGBA颜色值的整数指针。  默认值：0xFF000000。  **颜色字节布局说明：**  - 位24-31：Alpha通道（0x00完全透明，0xFF完全不透明）。  - 位16-23：红色通道。  - 位8-15：绿色通道。  - 位0-7：蓝色通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetShadowOffset()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetShadowOffset(ArkUI_RenderNodeHandle node, int32_t x, int32_t y)
```

**描述：**

为渲染节点设置阴影偏移量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t x | 水平偏移值（以像素为单位）。  默认值：0。 |
| int32\_t y | 垂直偏移值（以像素为单位）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetShadowOffset()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetShadowOffset(ArkUI_RenderNodeHandle node, int32_t* x, int32_t* y)
```

**描述：**

获取渲染节点的阴影偏移量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* x | 用于接收水平偏移值的指针。  默认值：0，单位：px。 |
| int32\_t\* y | 用于接收垂直偏移值的指针。  默认值：0，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetShadowAlpha()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetShadowAlpha(ArkUI_RenderNodeHandle node, float alpha)
```

**描述：**

为渲染节点设置阴影透明度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float alpha | 阴影 Alpha 值（0.0-1.0）。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetShadowAlpha()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetShadowAlpha(ArkUI_RenderNodeHandle node, float* alpha)
```

**描述：**

获取渲染节点的阴影透明度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* alpha | 用于接收阴影 Alpha 值的指针。  默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetShadowElevation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetShadowElevation(ArkUI_RenderNodeHandle node, float elevation)
```

**描述：**

为渲染节点设置阴影高度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float elevation | 高度值。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetShadowElevation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetShadowElevation(ArkUI_RenderNodeHandle node, float* elevation)
```

**描述：**

获取渲染节点的阴影高度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* elevation | 用于接收高度值的指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetShadowRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetShadowRadius(ArkUI_RenderNodeHandle node, float radius)
```

**描述：**

为渲染节点设置阴影半径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float radius | 半径值。  默认值：0。取值大于等于0，传入负值时返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetShadowRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetShadowRadius(ArkUI_RenderNodeHandle node, float* radius)
```

**描述：**

获取渲染节点的阴影半径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float\* radius | 用于接收半径值的指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBorderStyle(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderStyleOption* borderStyle)
```

**描述：**

为渲染节点设置边框样式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderStyleOption](api-arkui-nativemodule-arkui-nodeborderstyleoption.md)\* borderStyle | 边框样式的指针。  结构体指针内默认值：[ARKUI\_BORDER\_STYLE\_SOLID](capi-native-type-h.md#arkui_borderstyle)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBorderStyle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBorderStyle(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderStyleOption** borderStyle)
```

**描述：**

获取渲染节点的边框样式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderStyleOption](api-arkui-nativemodule-arkui-nodeborderstyleoption.md)\*\* borderStyle | 用于接收边框样式的指针。  结构体指针内默认值：[ARKUI\_BORDER\_STYLE\_SOLID](capi-native-type-h.md#arkui_borderstyle)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBorderWidth(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderWidthOption* borderWidth)
```

**描述：**

为渲染节点设置边框宽度，边框宽度需小于节点尺寸。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderWidthOption](api-arkui-nativemodule-arkui-nodeborderwidthoption.md)\* borderWidth | 边框宽度的指针。  结构体指针内默认值：0。单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBorderWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBorderWidth(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderWidthOption** borderWidth)
```

**描述：**

获取渲染节点的边框宽度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderWidthOption](api-arkui-nativemodule-arkui-nodeborderwidthoption.md)\*\* borderWidth | 用于接收边框宽度的指针。  结构体指针内默认值：0。单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBorderColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBorderColor(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderColorOption* borderColor)
```

**描述：**

为渲染节点设置边框颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderColorOption](api-arkui-nativemodule-arkui-nodebordercoloroption.md)\* borderColor | 边框颜色的指针。  结构体指针内默认值：0x00000000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBorderColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBorderColor(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderColorOption** borderColor)
```

**描述：**

获取渲染节点的边框颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderColorOption](api-arkui-nativemodule-arkui-nodebordercoloroption.md)\*\* borderColor | 用于接收边框颜色的指针。  结构体指针内默认值：0x00000000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBorderRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBorderRadius(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderRadiusOption* borderRadius)
```

**描述：**

为渲染节点设置边框角半径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderRadiusOption](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md)\* borderRadius | 边框半径的指针。  结构体指针内默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBorderRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBorderRadius(ArkUI_RenderNodeHandle node, ArkUI_NodeBorderRadiusOption** borderRadius)
```

**描述：**

获取渲染节点的边框角半径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_NodeBorderRadiusOption](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md)\*\* borderRadius | 用于接收边框半径的指针。  结构体指针内默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetMask()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetMask(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeMaskOption* mask)
```

**描述：**

使用遮罩配置为渲染节点应用遮罩。

遮罩创建方式如下：

1. 给遮罩图层增加亮度和线性颜色滤镜。
2. 在该滤镜下绘制遮罩图形。
3. 将原节点图像作为源颜色，遮罩图形为目标颜色，通过[BlendMode.SRC\_IN](arkts-apis-graphics-drawing-e.md#blendmode)方式混合成Mask图像。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md)\* mask | 遮罩配置的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetClip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetClip(ArkUI_RenderNodeHandle node, ArkUI_RenderNodeClipOption* clip)
```

**描述：**

使用裁剪配置为渲染节点应用裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* clip | 裁剪配置的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetMarkNodeGroup()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetMarkNodeGroup(ArkUI_RenderNodeHandle node, bool markNodeGroup)
```

**描述：**

标记是否优先绘制该节点及其子节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| bool markNodeGroup | 布尔值，是否优先绘制该节点及其子节点。  true：优先绘制节点及其子节点；false：不优先绘制节点及其子节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetBounds()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetBounds(ArkUI_RenderNodeHandle node, int32_t x, int32_t y, int32_t width, int32_t height)
```

**描述：**

为渲染节点设置边界。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t x | 边界左上角的X坐标（以像素为单位）。  默认值：0。 |
| int32\_t y | 边界左上角的Y坐标（以像素为单位）。  默认值：0。 |
| int32\_t width | 边界的宽度（以像素为单位）。  默认值：0。取值大于等于0，传入负值时返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)。 |
| int32\_t height | 边界的高度（以像素为单位）。  默认值：0。取值大于等于0，传入负值时返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 参数超出范围。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_GetBounds()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetBounds(ArkUI_RenderNodeHandle node, int32_t* x, int32_t* y, int32_t* width, int32_t* height)
```

**描述：**

获取渲染节点的边界。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| int32\_t\* x | 用于接收边界左上角X坐标（以像素为单位）的指针。  默认值：0。 |
| int32\_t\* y | 用于接收边界左上角Y坐标（以像素为单位）的指针。  默认值：0。 |
| int32\_t\* width | 用于接收边界宽度（以像素为单位）的指针。  默认值：0。 |
| int32\_t\* height | 用于接收边界高度（以像素为单位）的指针。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_SetDrawRegion()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetDrawRegion(ArkUI_RenderNodeHandle node, float x, float y, float w, float h)
```

**描述：**

为渲染节点设置绘制区域，该绘制区域主要用于超出边界导致的绘制问题，建议根据实际绘制范围设置大小。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| float x | 边界左上角的X坐标（以像素为单位）。 |
| float y | 边界左上角的Y坐标（以像素为单位）。 |
| float w | 边界的宽度（以像素为单位）。 |
| float h | 边界的高度（以像素为单位）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachContentModifier(ArkUI_RenderNodeHandle node, ArkUI_RenderContentModifierHandle modifier)
```

**描述：**

为渲染节点添加内容修改器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) node | 目标渲染节点。 |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 内容修改器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](capi-native-type-h.md#arkui_errorcode) 目标节点是从一个FrameNode获取的。从API version 22开始支持。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderContentModifierHandle OH_ArkUI_RenderNodeUtils_CreateContentModifier()
```

**描述：**

创建内容修改器。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) | 内容修改器。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeContentModifier()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeContentModifier(ArkUI_RenderContentModifierHandle modifier)
```

**描述：**

释放内容修改器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 内容修改器。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachFloatProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachFloatProperty(ArkUI_RenderContentModifierHandle modifier, ArkUI_FloatPropertyHandle property)
```

**描述：**

为目标内容修改器附加浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置浮点属性。 |
| [ArkUI\_FloatPropertyHandle](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) property | 浮点属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachVector2Property()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachVector2Property(ArkUI_RenderContentModifierHandle modifier, ArkUI_Vector2PropertyHandle property)
```

**描述：**

为目标内容修改器附加二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置二维向量属性。 |
| [ArkUI\_Vector2PropertyHandle](api-arkui-nativemodule-arkui-vector2propertyhandle.md) property | 二维向量属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachColorProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachColorProperty(ArkUI_RenderContentModifierHandle modifier, ArkUI_ColorPropertyHandle property)
```

**描述：**

为目标内容修改器附加颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置颜色属性。 |
| [ArkUI\_ColorPropertyHandle](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) property | 颜色属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachFloatAnimatableProperty(ArkUI_RenderContentModifierHandle modifier, ArkUI_FloatAnimatablePropertyHandle property)
```

**描述：**

为目标内容修改器附加可动画的浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置可动画的浮点属性。 |
| [ArkUI\_FloatAnimatablePropertyHandle](i-nativemodule-arkui-floatanimatablepropertyhandle.md) property | 可动画的浮点属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachVector2AnimatableProperty(ArkUI_RenderContentModifierHandle modifier, ArkUI_Vector2AnimatablePropertyHandle property)
```

**描述：**

为目标内容修改器附加可动画的二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置可动画的二维向量属性。 |
| [ArkUI\_Vector2AnimatablePropertyHandle](nativemodule-arkui-vector2animatablepropertyhandle.md) property | 可动画的二维向量属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_AttachColorAnimatableProperty(ArkUI_RenderContentModifierHandle modifier, ArkUI_ColorAnimatablePropertyHandle property)
```

**描述：**

为目标内容修改器附加可动画的颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 为目标内容修改器设置可动画的颜色属性。 |
| [ArkUI\_ColorAnimatablePropertyHandle](i-nativemodule-arkui-coloranimatablepropertyhandle.md) property | 可动画的颜色属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateFloatProperty()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_FloatPropertyHandle OH_ArkUI_RenderNodeUtils_CreateFloatProperty(float value)
```

**描述：**

创建浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_FloatPropertyHandle](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) | 浮点属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetFloatPropertyValue(ArkUI_FloatPropertyHandle property, float value)
```

**描述：**

设置浮点属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatPropertyHandle](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) property | 浮点属性。 |
| float value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetFloatPropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetFloatPropertyValue(ArkUI_FloatPropertyHandle property, float* value)
```

**描述：**

获取浮点属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatPropertyHandle](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) property | 浮点属性。 |
| float\* value | 用于接收属性值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeFloatProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeFloatProperty(ArkUI_FloatPropertyHandle property)
```

**描述：**

释放浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatPropertyHandle](capi-arkui-nativemodule-arkui-floatpropertyhandle.md) property | 浮点属性。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateVector2Property()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_Vector2PropertyHandle OH_ArkUI_RenderNodeUtils_CreateVector2Property(float x, float y)
```

**描述：**

创建二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float x | 属性的X坐标值。 |
| float y | 属性的Y坐标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Vector2PropertyHandle](api-arkui-nativemodule-arkui-vector2propertyhandle.md) | 二维向量属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetVector2PropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetVector2PropertyValue(ArkUI_Vector2PropertyHandle property, float x, float y)
```

**描述：**

设置二维向量属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2PropertyHandle](api-arkui-nativemodule-arkui-vector2propertyhandle.md) property | 二维向量属性。 |
| float x | 属性的X坐标值。 |
| float y | 属性的Y坐标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetVector2PropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetVector2PropertyValue(ArkUI_Vector2PropertyHandle property, float* x, float* y)
```

**描述：**

获取二维向量属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2PropertyHandle](api-arkui-nativemodule-arkui-vector2propertyhandle.md) property | 二维向量属性。 |
| float\* x | 用于接收属性X坐标值的指针。 |
| float\* y | 用于接收属性Y坐标值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeVector2Property()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeVector2Property(ArkUI_Vector2PropertyHandle property)
```

**描述：**

释放二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2PropertyHandle](api-arkui-nativemodule-arkui-vector2propertyhandle.md) property | 二维向量属性。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateColorProperty()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ColorPropertyHandle OH_ArkUI_RenderNodeUtils_CreateColorProperty(uint32_t value)
```

**描述：**

创建颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ColorPropertyHandle](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) | 颜色属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetColorPropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetColorPropertyValue(ArkUI_ColorPropertyHandle property, uint32_t value)
```

**描述：**

设置颜色属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorPropertyHandle](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) property | 颜色属性。 |
| uint32\_t value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetColorPropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetColorPropertyValue(ArkUI_ColorPropertyHandle property, uint32_t* value)
```

**描述：**

获取颜色属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorPropertyHandle](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) property | 颜色属性。 |
| uint32\_t\* value | 用于接收属性值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeColorProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeColorProperty(ArkUI_ColorPropertyHandle property)
```

**描述：**

释放颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorPropertyHandle](capi-arkui-nativemodule-arkui-colorpropertyhandle.md) property | 颜色属性。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_FloatAnimatablePropertyHandle OH_ArkUI_RenderNodeUtils_CreateFloatAnimatableProperty(float value)
```

**描述：**

创建可动画的浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_FloatAnimatablePropertyHandle](i-nativemodule-arkui-floatanimatablepropertyhandle.md) | 可动画的浮点属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetFloatAnimatablePropertyValue(ArkUI_FloatAnimatablePropertyHandle property, float value)
```

**描述：**

设置可动画的浮点属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatAnimatablePropertyHandle](i-nativemodule-arkui-floatanimatablepropertyhandle.md) property | 可动画的浮点属性。 |
| float value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetFloatAnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetFloatAnimatablePropertyValue(ArkUI_FloatAnimatablePropertyHandle property, float* value)
```

**描述：**

获取可动画的浮点属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatAnimatablePropertyHandle](i-nativemodule-arkui-floatanimatablepropertyhandle.md) property | 可动画的浮点属性。 |
| float\* value | 用于接收属性值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeFloatAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeFloatAnimatableProperty(ArkUI_FloatAnimatablePropertyHandle property)
```

**描述：**

释放可动画的浮点属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_FloatAnimatablePropertyHandle](i-nativemodule-arkui-floatanimatablepropertyhandle.md) property | 可动画的浮点属性。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_Vector2AnimatablePropertyHandle OH_ArkUI_RenderNodeUtils_CreateVector2AnimatableProperty(float x, float y)
```

**描述：**

创建可动画的二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float x | 属性的X坐标值。 |
| float y | 属性的Y坐标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Vector2AnimatablePropertyHandle](nativemodule-arkui-vector2animatablepropertyhandle.md) | 可动画的二维向量属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetVector2AnimatablePropertyValue(ArkUI_Vector2AnimatablePropertyHandle property, float x, float y)
```

**描述：**

设置可动画的二维向量属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2AnimatablePropertyHandle](nativemodule-arkui-vector2animatablepropertyhandle.md) property | 可动画的二维向量属性。 |
| float x | 属性的X坐标值。 |
| float y | 属性的Y坐标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetVector2AnimatablePropertyValue(ArkUI_Vector2AnimatablePropertyHandle property, float* x, float* y)
```

**描述：**

获取可动画的二维向量属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2AnimatablePropertyHandle](nativemodule-arkui-vector2animatablepropertyhandle.md) property | 可动画的二维向量属性。 |
| float\* x | 用于接收属性X坐标值的指针。 |
| float\* y | 用于接收属性Y坐标值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeVector2AnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeVector2AnimatableProperty(ArkUI_Vector2AnimatablePropertyHandle property)
```

**描述：**

释放可动画的二维向量属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Vector2AnimatablePropertyHandle](nativemodule-arkui-vector2animatablepropertyhandle.md) property | 可动画的二维向量属性。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ColorAnimatablePropertyHandle OH_ArkUI_RenderNodeUtils_CreateColorAnimatableProperty(uint32_t value)
```

**描述：**

创建可动画的颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ColorAnimatablePropertyHandle](i-nativemodule-arkui-coloranimatablepropertyhandle.md) | 可动画的颜色属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetColorAnimatablePropertyValue(ArkUI_ColorAnimatablePropertyHandle property, uint32_t value)
```

**描述：**

设置可动画的颜色属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorAnimatablePropertyHandle](i-nativemodule-arkui-coloranimatablepropertyhandle.md) property | 可动画的颜色属性。 |
| uint32\_t value | 属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetColorAnimatablePropertyValue(ArkUI_ColorAnimatablePropertyHandle property, uint32_t* value)
```

**描述：**

获取可动画的颜色属性的值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorAnimatablePropertyHandle](i-nativemodule-arkui-coloranimatablepropertyhandle.md) property | 可动画的颜色属性。 |
| uint32\_t\* value | 用于接收属性值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeColorAnimatableProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeColorAnimatableProperty(ArkUI_ColorAnimatablePropertyHandle property)
```

**描述：**

释放可动画的颜色属性。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ColorAnimatablePropertyHandle](i-nativemodule-arkui-coloranimatablepropertyhandle.md) property | 可动画的颜色属性。 |

### OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_SetContentModifierOnDraw(ArkUI_RenderContentModifierHandle modifier, void* userData, void (*callback)(ArkUI_DrawContext* context, void* userData))
```

**描述：**

设置内容修改器的onDraw函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderContentModifierHandle](kui-nativemodule-arkui-rendercontentmodifierhandle.md) modifier | 目标内容修改器。 |
| void\* userData | 要传递给回调的自定义数据。 |
| void (callback)([ArkUI\_DrawContext](capi-arkui-nativemodule-arkui-drawcontext.md) context, void\* userData) | 绘制事件接收回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRectShapeOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RectShapeOption* OH_ArkUI_RenderNodeUtils_CreateRectShapeOption()
```

**描述：**

创建矩形形状。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RectShapeOption](capi-arkui-nativemodule-arkui-rectshapeoption.md)\* | 指向矩形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeRectShapeOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeRectShapeOption(ArkUI_RectShapeOption* option)
```

**描述：**

释放矩形形状。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption](capi-arkui-nativemodule-arkui-rectshapeoption.md)\* option | 指向矩形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRectShapeOptionEdgeValue()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRectShapeOptionEdgeValue(ArkUI_RectShapeOption* option, float edgeValue, ArkUI_EdgeDirection direction)
```

**描述：**

设置矩形形状的边缘值。当设置左边界和上边界为负数时，因显示涉及到图层叠加效果，会导致部分超出节点内容部分无法绘制。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption](capi-arkui-nativemodule-arkui-rectshapeoption.md)\* option | 指向矩形形状的指针。 |
| float edgeValue | 矩形形状的边缘值。 |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) direction | 要设置边缘值的矩形方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeBorderStyleOption* OH_ArkUI_RenderNodeUtils_CreateNodeBorderStyleOption()
```

**描述：**

创建节点边框样式。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeBorderStyleOption](api-arkui-nativemodule-arkui-nodeborderstyleoption.md)\* | 指向节点边框样式的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeNodeBorderStyleOption(ArkUI_NodeBorderStyleOption* option)
```

**描述：**

释放节点边框样式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderStyleOption](api-arkui-nativemodule-arkui-nodeborderstyleoption.md)\* option | 指向节点边框样式的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetNodeBorderStyleOptionEdgeStyle(ArkUI_NodeBorderStyleOption* option, ArkUI_BorderStyle edgeStyle, ArkUI_EdgeDirection direction)
```

**描述：**

设置节点边框样式的边缘值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderStyleOption](api-arkui-nativemodule-arkui-nodeborderstyleoption.md)\* option | 指向节点边框样式的指针。 |
| [ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle) edgeStyle | 节点边框样式的边缘边框样式值。 |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) direction | 边缘的方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeBorderWidthOption* OH_ArkUI_RenderNodeUtils_CreateNodeBorderWidthOption()
```

**描述：**

创建节点边框宽度。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeBorderWidthOption](api-arkui-nativemodule-arkui-nodeborderwidthoption.md)\* | 指向节点边框宽度的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeNodeBorderWidthOption(ArkUI_NodeBorderWidthOption* option)
```

**描述：**

释放节点边框宽度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderWidthOption](api-arkui-nativemodule-arkui-nodeborderwidthoption.md)\* option | 指向节点边框宽度的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetNodeBorderWidthOptionEdgeWidth(ArkUI_NodeBorderWidthOption* option, float edgeWidth, ArkUI_EdgeDirection direction)
```

**描述：**

设置节点边框宽度的边缘值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderWidthOption](api-arkui-nativemodule-arkui-nodeborderwidthoption.md)\* option | 指向节点边框宽度的指针。 |
| float edgeWidth | 节点边框宽度的边缘宽度值。  取值范围：[0, +∞) |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) direction | 边缘的方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeBorderColorOption* OH_ArkUI_RenderNodeUtils_CreateNodeBorderColorOption()
```

**描述：**

创建节点边框颜色。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeBorderColorOption](api-arkui-nativemodule-arkui-nodebordercoloroption.md)\* | 指向节点边框颜色的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeNodeBorderColorOption(ArkUI_NodeBorderColorOption* option)
```

**描述：**

释放节点边框颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderColorOption](api-arkui-nativemodule-arkui-nodebordercoloroption.md)\* option | 指向节点边框颜色的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetNodeBorderColorOptionEdgeColor(ArkUI_NodeBorderColorOption* option, uint32_t edgeColor, ArkUI_EdgeDirection direction)
```

**描述：**

设置节点边框颜色的边缘值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderColorOption](api-arkui-nativemodule-arkui-nodebordercoloroption.md)\* option | 指向节点边框颜色的指针。 |
| uint32\_t edgeColor | 节点边框颜色的边缘颜色值。 |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) direction | 边缘的方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderRadiusOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeBorderRadiusOption* OH_ArkUI_RenderNodeUtils_CreateNodeBorderRadiusOption()
```

**描述：**

创建节点边框半径。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeBorderRadiusOption](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md)\* | 指向节点边框半径的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderRadiusOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeNodeBorderRadiusOption(ArkUI_NodeBorderRadiusOption* option)
```

**描述：**

释放节点边框半径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderRadiusOption](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md)\* option | 指向节点边框半径的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderRadiusOptionCornerRadius()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetNodeBorderRadiusOptionCornerRadius(ArkUI_NodeBorderRadiusOption* option, uint32_t cornerRadius, ArkUI_CornerDirection direction)
```

**描述：**

设置节点边框半径的边缘值。请注意，入参cornerRadius为uint32\_t，仅支持传入正整数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeBorderRadiusOption](pi-arkui-nativemodule-arkui-nodeborderradiusoption.md)\* option | 指向节点边框半径的指针。 |
| uint32\_t cornerRadius | 节点边框半径的边缘半径值。 |
| [ArkUI\_CornerDirection](capi-native-type-h.md#arkui_cornerdirection) direction | 边缘的方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateCircleShapeOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CircleShapeOption* OH_ArkUI_RenderNodeUtils_CreateCircleShapeOption()
```

**描述：**

创建圆形形状。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* | 指向圆形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeCircleShapeOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeCircleShapeOption(ArkUI_CircleShapeOption* option)
```

**描述：**

释放圆形形状。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* option | 指向圆形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterX()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetCircleShapeOptionCenterX(ArkUI_CircleShapeOption* option, float centerX)
```

**描述：**

设置圆形形状的圆心x轴坐标值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* option | 指向圆形形状的指针。 |
| float centerX | 圆心x轴坐标值。 |

### OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterY()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetCircleShapeOptionCenterY(ArkUI_CircleShapeOption* option, float centerY)
```

**描述：**

设置圆形形状的圆心y轴坐标值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* option | 指向圆形形状的指针。 |
| float centerY | 圆心y轴坐标值。 |

### OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionRadius()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetCircleShapeOptionRadius(ArkUI_CircleShapeOption* option, float radius)
```

**描述：**

设置圆形形状的半径值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* option | 指向圆形形状的指针。 |
| float radius | 半径值（以像素为单位）。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRoundRectShapeOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RoundRectShapeOption* OH_ArkUI_RenderNodeUtils_CreateRoundRectShapeOption()
```

**描述：**

创建圆角矩形形状。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption](capi-arkui-nativemodule-arkui-roundrectshapeoption.md)\* | 指向圆角矩形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeRoundRectShapeOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeRoundRectShapeOption(ArkUI_RoundRectShapeOption* option)
```

**描述：**

释放圆角矩形形状。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption](capi-arkui-nativemodule-arkui-roundrectshapeoption.md)\* option | 指向圆角矩形形状的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionEdgeValue()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRoundRectShapeOptionEdgeValue(ArkUI_RoundRectShapeOption* option, float edgeValue, ArkUI_EdgeDirection direction)
```

**描述：**

设置圆角矩形形状的边缘值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption](capi-arkui-nativemodule-arkui-roundrectshapeoption.md)\* option | 指向圆角矩形形状的指针。 |
| float edgeValue | 圆角矩形形状的边缘值。 |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) direction | 要设置边缘值的矩形方向。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionCornerXY()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRoundRectShapeOptionCornerXY(ArkUI_RoundRectShapeOption* option, float x, float y, ArkUI_CornerDirection direction)
```

**描述：**

设置目标角的坐标值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption](capi-arkui-nativemodule-arkui-roundrectshapeoption.md)\* option | 指向圆角矩形形状的指针。 |
| float x | 目标角的X坐标（以像素为单位）。 |
| float y | 目标角的Y坐标（以像素为单位）。 |
| [ArkUI\_CornerDirection](capi-native-type-h.md#arkui_cornerdirection) direction | 角的方向。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateCommandPathOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CommandPathOption* OH_ArkUI_RenderNodeUtils_CreateCommandPathOption()
```

**描述：**

创建自定义绘制路径。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CommandPathOption](capi-arkui-nativemodule-arkui-commandpathoption.md)\* | 指向自定义绘制路径的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeCommandPathOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeCommandPathOption(ArkUI_CommandPathOption* option)
```

**描述：**

释放自定义绘制路径。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CommandPathOption](capi-arkui-nativemodule-arkui-commandpathoption.md)\* option | 指向自定义绘制路径的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetCommandPathOptionCommands()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetCommandPathOptionCommands(ArkUI_CommandPathOption* option, char* commands)
```

**描述：**

设置自定义绘制路径的命令值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CommandPathOption](capi-arkui-nativemodule-arkui-commandpathoption.md)\* option | 指向自定义绘制路径的指针。 |
| char\* commands | 命令值。入参格式为SVG的[<path>形状标签](ts-basic-svg.md#基础形状)。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRectShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeMaskOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeMaskOptionFromRectShape(ArkUI_RectShapeOption* shape)
```

**描述：**

从矩形形状创建遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption\*](capi-arkui-nativemodule-arkui-rectshapeoption.md) shape | 指向矩形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRoundRectShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeMaskOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeMaskOptionFromRoundRectShape(ArkUI_RoundRectShapeOption* shape)
```

**描述：**

从圆角矩形形状创建遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption\*](capi-arkui-nativemodule-arkui-roundrectshapeoption.md) shape | 指向圆角矩形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCircleShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeMaskOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeMaskOptionFromCircleShape(ArkUI_CircleShapeOption* shape)
```

**描述：**

从圆形形状创建遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption\*](capi-arkui-nativemodule-arkui-circleshapeoption.md) shape | 指向圆形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromOvalShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeMaskOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeMaskOptionFromOvalShape(ArkUI_RectShapeOption* shape)
```

**描述：**

从椭圆形形状创建遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption\*](capi-arkui-nativemodule-arkui-rectshapeoption.md) shape | 指向椭圆形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCommandPath()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeMaskOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeMaskOptionFromCommandPath(ArkUI_CommandPathOption* path)
```

**描述：**

从自定义绘制路径创建遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CommandPathOption\*](capi-arkui-nativemodule-arkui-commandpathoption.md) path | 指向自定义绘制路径的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeMaskOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeRenderNodeMaskOption(ArkUI_RenderNodeMaskOption* option)
```

**描述：**

释放渲染节点遮罩。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption\*](capi-arkui-nativemodule-arkui-rendernodemaskoption.md) option | 指向渲染节点遮罩的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionFillColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRenderNodeMaskOptionFillColor(ArkUI_RenderNodeMaskOption* mask, uint32_t fillColor)
```

**描述：**

设置渲染节点遮罩的填充颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md)\* mask | 指向渲染节点遮罩的指针。 |
| uint32\_t fillColor | 遮罩的填充颜色。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRenderNodeMaskOptionStrokeColor(ArkUI_RenderNodeMaskOption* mask, uint32_t strokeColor)
```

**描述：**

设置渲染节点遮罩的描边颜色。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md)\* mask | 指向渲染节点遮罩的指针。 |
| uint32\_t strokeColor | 遮罩的描边颜色。 |

### OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_SetRenderNodeMaskOptionStrokeWidth(ArkUI_RenderNodeMaskOption* mask, float strokeWidth)
```

**描述：**

设置渲染节点遮罩的描边宽度。以边框路径为中心进行相应宽度的绘制。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeMaskOption](capi-arkui-nativemodule-arkui-rendernodemaskoption.md)\* mask | 指向渲染节点遮罩的指针。 |
| float strokeWidth | 遮罩的描边宽度。  取值范围：(0, +∞)，当取值为负数或0时，绘制时会被设定成1像素。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRectShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeClipOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeClipOptionFromRectShape(ArkUI_RectShapeOption* shape)
```

**描述：**

从矩形形状创建裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption](capi-arkui-nativemodule-arkui-rectshapeoption.md)\* shape | 指向矩形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRoundRectShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeClipOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeClipOptionFromRoundRectShape(ArkUI_RoundRectShapeOption* shape)
```

**描述：**

从圆角矩形形状创建裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RoundRectShapeOption](capi-arkui-nativemodule-arkui-roundrectshapeoption.md)\* shape | 指向圆角矩形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCircleShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeClipOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeClipOptionFromCircleShape(ArkUI_CircleShapeOption* shape)
```

**描述：**

从圆形形状创建裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CircleShapeOption](capi-arkui-nativemodule-arkui-circleshapeoption.md)\* shape | 指向圆形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromOvalShape()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeClipOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeClipOptionFromOvalShape(ArkUI_RectShapeOption* shape)
```

**描述：**

从椭圆形形状创建裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RectShapeOption](capi-arkui-nativemodule-arkui-rectshapeoption.md)\* shape | 指向椭圆形形状的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCommandPath()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_RenderNodeClipOption* OH_ArkUI_RenderNodeUtils_CreateRenderNodeClipOptionFromCommandPath(ArkUI_CommandPathOption* path)
```

**描述：**

从自定义绘制路径创建裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CommandPathOption](capi-arkui-nativemodule-arkui-commandpathoption.md)\* path | 指向自定义绘制路径的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeClipOption()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_RenderNodeUtils_DisposeRenderNodeClipOption(ArkUI_RenderNodeClipOption* option)
```

**描述：**

释放渲染节点裁剪。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)\* option | 指向渲染节点裁剪的指针。 |

### OH\_ArkUI\_RenderNodeUtils\_GetRenderNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RenderNodeUtils_GetRenderNode(ArkUI_NodeHandle node, ArkUI_RenderNodeHandle* renderNode);
```

**描述：**

获取已被接纳为附属节点的目标节点的RenderNode。如果一个RenderNode是通过该接口获取的，调用[ArkUI\_NativeNodeAPI\_1](capi-arkui-nativemodule-arkui-nativenodeapi-1.md)的[disposeNode](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#disposenode)接口主动销毁FrameNode时，需要额外调用[OH\_ArkUI\_RenderNodeUtils\_DisposeNode](capi-native-render-h.md#oh_arkui_rendernodeutils_disposenode)释放该RenderNode。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针，指定目标节点。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md)\* renderNode | ArkUI\_RenderNodeHandle\*指针，目标节点的RenderNode。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化失败。  [ARKUI\_ERROR\_CODE\_RENDER\_NOT\_ADOPTED\_NODE](capi-native-type-h.md#arkui_errorcode) 该节点未被接纳为附属节点。 |
