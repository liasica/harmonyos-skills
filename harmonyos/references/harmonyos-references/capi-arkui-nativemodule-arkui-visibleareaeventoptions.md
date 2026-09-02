---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-visibleareaeventoptions
title: ArkUI_VisibleAreaEventOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_VisibleAreaEventOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a94e3e11f77e5c090de2fea47ec97ac55dd55b454bbda4b6002efc269839e272
---

```c
typedef struct ArkUI_VisibleAreaEventOptions ArkUI_VisibleAreaEventOptions
```

## 概述

ArkUI\_VisibleAreaEventOptions用于配置可见区域变化监听的参数，包括阈值数组、预期更新间隔和可见区域计算模式，适用于需要监听组件可见区域变化并按指定阈值触发更新的场景。

开发者在使用该类型时，首先需要调用[OH\_ArkUI\_VisibleAreaEventOptions\_Create](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_create)创建一个ArkUI\_VisibleAreaEventOptions参数对象。然后可通过如下接口配置监听行为：

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_setratios)设置阈值数组，定义触发可见区域变化的阈值条件。

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_setexpectedupdateinterval)设置预期更新间隔，定义两次可见区域变化通知之间的最小时间间隔。

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_setmeasurefromviewport)设置可见区域计算模式，定义是否从视口区域计算可见比例。

如需获取已设置的参数值，可使用：

[OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_getratios)获取阈值数组。

[OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_getexpectedupdateinterval)获取预期更新间隔。

[OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_getmeasurefromviewport)获取可见区域计算模式。

使用完毕后，应调用[OH\_ArkUI\_VisibleAreaEventOptions\_Dispose](capi-common-attributes-h.md#oh_arkui_visibleareaeventoptions_dispose)释放资源。

**起始版本：** 17

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [common\_attributes.h](capi-common-attributes-h.md)
