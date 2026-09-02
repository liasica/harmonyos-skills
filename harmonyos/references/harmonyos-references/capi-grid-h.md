---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-grid-h
title: grid.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > grid.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f1698ba7c912a20c2844f4267051becf663af07c078d5f49817c3ad5efa221c6
---

## 概述

定义Grid组件相关的枚举和接口。

**引用文件：** <arkui/node\_attributes/grid.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NDKGridSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKGridSample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_GridItemSize](capi-arkui-nativemodule-arkui-griditemsize.md) | ArkUI\_GridItemSize | 定义Grid布局选项onGetIrregularSizeByIndex回调返回值结构体。 |
| [ArkUI\_GridItemRect](capi-arkui-nativemodule-arkui-griditemrect.md) | ArkUI\_GridItemRect | 定义Grid布局选项onGetRectByIndex回调返回值结构体。 |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md) | ArkUI\_GridLayoutOptions | 定义Grid（网格）布局选项，用于配置Grid组件中不规则GridItem的布局参数，包括不规则项索引和布局回调。不规则GridItem是指在网格布局中跨行跨列或尺寸不同的网格项。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_GridItemAlignment](capi-grid-h.md#arkui_griditemalignment) | ArkUI\_GridItemAlignment | [GridItem](ts-container-griditem.md)对齐方式枚举。 |
| [ArkUI\_GridItemStyle](capi-grid-h.md#arkui_griditemstyle) | ArkUI\_GridItemStyle | GridItem样式枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions\* OH\_ArkUI\_GridLayoutOptions\_Create()](capi-grid-h.md#oh_arkui_gridlayoutoptions_create) | 创建Grid布局选项。使用完毕后调用OH\_ArkUI\_GridLayoutOptions\_Dispose销毁。 |
| [void OH\_ArkUI\_GridLayoutOptions\_Dispose(ArkUI\_GridLayoutOptions\* option)](capi-grid-h.md#oh_arkui_gridlayoutoptions_dispose) | 销毁Grid布局选项并释放资源。 |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t size)](capi-grid-h.md#oh_arkui_gridlayoutoptions_setirregularindexes) | 设置Grid中不规则GridItem的索引数组。 |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t\* size)](capi-grid-h.md#oh_arkui_gridlayoutoptions_getirregularindexes) | 获取Grid中不规则GridItem的索引数组。当不设置OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。 |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemSize(\*callback)(int32\_t itemIndex, void\* userData))](capi-grid-h.md#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback) | Grid布局选项通过GridItem索引获取指定Item占用的行列数。 |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData))](capi-grid-h.md#oh_arkui_gridlayoutoptions_registergetrectbyindexcallback) | Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。 |

## 枚举类型说明

### ArkUI\_GridItemAlignment

```c
enum ArkUI_GridItemAlignment
```

**描述：**

[GridItem](ts-container-griditem.md)对齐方式枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| GRID\_ITEM\_ALIGNMENT\_DEFAULT = 0 | Grid的默认对齐方式。 |
| GRID\_ITEM\_ALIGNMENT\_STRETCH = 1 | 以一行中的最高的GridItem作为其他GridItem的高度。 |

### ArkUI\_GridItemStyle

```c
enum ArkUI_GridItemStyle
```

**描述：**

GridItem样式枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| GRID\_ITEM\_STYLE\_NONE = 0 | 无样式。 |
| GRID\_ITEM\_STYLE\_PLAIN = 1 | 显示Hover、Press态样式。 |

## 函数说明

### OH\_ArkUI\_GridLayoutOptions\_Create()

```c
ArkUI_GridLayoutOptions* OH_ArkUI_GridLayoutOptions_Create()
```

**描述：**

创建Grid布局选项。使用完毕后调用OH\_ArkUI\_GridLayoutOptions\_Dispose销毁。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* | 创建的Grid布局选项。 |

### OH\_ArkUI\_GridLayoutOptions\_Dispose()

```c
void OH_ArkUI_GridLayoutOptions_Dispose(ArkUI_GridLayoutOptions* option)
```

**描述：**

销毁Grid布局选项并释放资源。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | 待销毁的Grid布局选项。 |

### OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes()

```c
int32_t OH_ArkUI_GridLayoutOptions_SetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t size)
```

**描述：**

设置Grid中不规则GridItem的索引数组。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | 待设置的Grid布局选项。 |
| uint32\_t\* irregularIndexes | 用于设置Grid布局选项的不规则GridItem索引数组。 |
| int32\_t size | irregularIndexes数组元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes()

```c
int32_t OH_ArkUI_GridLayoutOptions_GetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t* size)
```

**描述：**

获取Grid中不规则GridItem的索引数组。当不设置OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | 待获取的Grid布局选项。 |
| uint32\_t\* irregularIndexes | 用于接收不规则GridItem索引数组的缓冲区。 |
| int32\_t\* size | irregularIndexes缓冲区可容纳的元素个数。调用前传入缓冲区容量，调用成功后更新为实际写入的索引数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数组大小不够。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback()

```c
void OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemSize (*callback)(int32_t itemIndex, void* userData))
```

**描述：**

Grid布局选项通过GridItem索引获取指定Item占用的行列数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_GridItemSize](capi-arkui-nativemodule-arkui-griditemsize.md) (\*callback)(int32\_t itemIndex, void\* userData) | 根据index获取指定Item占用的行列数。  itemIndex: GridItem索引值，取值范围来自[OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes](capi-grid-h.md#oh_arkui_gridlayoutoptions_setirregularindexes)。 |

### OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback()

```c
void OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemRect (*callback)(int32_t itemIndex, void* userData))
```

**描述：**

Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_GridItemRect](capi-arkui-nativemodule-arkui-griditemrect.md) (\*callback)(int32\_t itemIndex, void\* userData) | 根据index获取指定Item的起始行列和占用的行列数。  itemIndex: GridItem索引值。 |
