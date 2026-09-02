---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-list-h
title: list.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > list.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:04c8416154c74911b85e5783d692f15c798874c2d336f7b4fd96e230112291ac
---

## 概述

定义List组件相关的枚举和接口。

**引用文件：** <arkui/node\_attributes/list.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [ScrollableNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ScrollableNDK)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md) | ArkUI\_ListChildrenMainSize | 定义List组件子组件的主轴尺寸信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ListItemAlignment](capi-list-h.md#arkui_listitemalignment) | ArkUI\_ListItemAlignment | 交叉轴方向的布局方式。 |
| [ArkUI\_StickyStyle](capi-list-h.md#arkui_stickystyle) | ArkUI\_StickyStyle | 定义列表是否吸顶和吸底枚举值。 |
| [ArkUI\_ListItemGroupArea](capi-list-h.md#arkui_listitemgrouparea) | ArkUI\_ListItemGroupArea | 定义ListItemGroup组件区域。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize\* OH\_ArkUI\_ListChildrenMainSizeOption\_Create()](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_create) | 创建ListChildrenMainSize接口设置的配置项。使用结束后需调用OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose释放资源。 |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose(ArkUI\_ListChildrenMainSize\* option)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_dispose) | 销毁由OH\_ArkUI\_ListChildrenMainSizeOption\_Create创建的ListChildrenMainSize实例。销毁后不得继续访问该实例。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option, float defaultMainSize)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_setdefaultmainsize) | 设置List组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_getdefaultmainsize) | 获取List组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Resize(ArkUI\_ListChildrenMainSize\* option, int32\_t totalSize)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_resize) | 调整List组件子项主轴尺寸数组的长度。扩大数组时，新增元素的初始值为-1。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_Splice(ArkUI\_ListChildrenMainSize\* option, int32\_t index, int32\_t deleteCount, int32\_t addCount)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_splice) | 从指定索引位置开始删除deleteCount个List组件子项主轴尺寸数组元素，并在该位置插入addCount个初始值为-1的元素。deleteCount超出剩余元素个数时，删除至数组末尾。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index, float mainSize)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_updatesize) | 更新List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index)](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_getmainsize) | 获取List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |

## 枚举类型说明

### ArkUI\_ListItemAlignment

```c
enum ArkUI_ListItemAlignment
```

**描述：**

交叉轴方向的布局方式，默认值为ARKUI\_LIST\_ITEM\_ALIGNMENT\_START。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_START = 0 | [ListItem](ts-container-listitem.md#listitem10)在List中，交叉轴方向首部对齐。 |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_CENTER = 1 | ListItem在List中，交叉轴方向居中对齐。 |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_END = 2 | ListItem在List中，交叉轴方向尾部对齐。 |

### ArkUI\_StickyStyle

```c
enum ArkUI_StickyStyle
```

**描述：**

定义列表是否吸顶和吸底枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_STICKY\_STYLE\_NONE = 0 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸底。 |
| ARKUI\_STICKY\_STYLE\_HEADER = 1 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸底。 |
| ARKUI\_STICKY\_STYLE\_FOOTER = 2 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸底。 |
| ARKUI\_STICKY\_STYLE\_BOTH = 3 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸底。 |

### ArkUI\_ListItemGroupArea

```c
enum ArkUI_ListItemGroupArea
```

**描述：**

定义[ListItemGroup](ts-container-listitemgroup.md)组件区域，默认值为ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE = 0 | ListItemGroup区域外。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_NONE = 1 | ListItemGroup没有[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)、[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)和[ListItem](ts-container-listitem.md#listitem10)时的区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_ITEM = 2 | ListItemGroup的ListItem区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_HEADER = 3 | ListItemGroup的header区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_FOOTER = 4 | ListItemGroup的footer区域。 |

## 函数说明

### OH\_ArkUI\_ListChildrenMainSizeOption\_Create()

```c
ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create()
```

**描述：**

创建ListChildrenMainSize接口设置的配置项。使用结束后需调用[OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_dispose)释放资源。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* | ListChildrenMainSize配置项实例。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose()

```c
void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option)
```

**描述：**

销毁由[OH\_ArkUI\_ListChildrenMainSizeOption\_Create](capi-list-h.md#oh_arkui_listchildrenmainsizeoption_create)创建的ListChildrenMainSize实例。销毁后不得继续访问该实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | 要销毁的ListChildrenMainSize实例。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize()

```c
int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize)
```

**描述：**

设置[List](ts-container-list.md)组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。为空指针时返回ARKUI\_ERROR\_CODE\_PARAM\_INVALID。 |
| float defaultMainSize | 列表项在主轴方向的默认尺寸值，单位为vp，取值范围为大于等于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize()

```c
float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option)
```

**描述：**

获取[List](ts-container-list.md)组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 列表项在主轴方向的默认尺寸值，默认为0，单位为[vp](ts-types.md#vp10)，option为空指针时返回-1。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Resize()

```c
void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize)
```

**描述：**

调整[List](ts-container-list.md)组件子项主轴尺寸数组的长度。扩大数组时，新增元素的初始值为-1。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。为空指针时不执行操作。 |
| int32\_t totalSize | 目标数组长度，取值范围为大于0。传入小于等于0的值时不执行操作。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Splice()

```c
int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount)
```

**描述：**

从指定索引位置开始删除deleteCount个[List](ts-container-list.md)组件子项主轴尺寸数组元素，并在该位置插入addCount个初始值为-1的元素。deleteCount超出剩余元素个数时，删除至数组末尾。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。为空指针时返回ARKUI\_ERROR\_CODE\_PARAM\_INVALID。 |
| int32\_t index | 操作起始索引位置，取值范围为0至数组当前长度减1。 |
| int32\_t deleteCount | 从起始位置开始删除的元素数量，取值范围为大于等于0。数量超出剩余元素个数时删除至数组末尾。 |
| int32\_t addCount | 从起始位置开始新增的元素数量，取值范围为大于等于0。新增元素的初始值为-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize()

```c
int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize)
```

**描述：**

更新[List](ts-container-list.md)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。为空指针时返回ARKUI\_ERROR\_CODE\_PARAM\_INVALID。 |
| int32\_t index | 目标元素的数组索引位置，取值范围为0至数组当前长度减1。 |
| float mainSize | 要设置的主轴尺寸值，单位为vp，取值范围为大于等于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize()

```c
float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index)
```

**描述：**

获取[List](ts-container-list.md)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| int32\_t index | 目标元素的数组索引位置，取值范围为0至数组当前长度减1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数组指定位置的主轴尺寸值，单位为vp。option为空指针或index超出数组范围时返回-1。 |
