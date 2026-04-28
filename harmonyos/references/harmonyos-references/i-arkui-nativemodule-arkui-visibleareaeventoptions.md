---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-visibleareaeventoptions
title: ArkUI_VisibleAreaEventOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_VisibleAreaEventOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:04:33+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:c0758531827ac259b40dbb26e30b07df64cc3d9dde58df8fffc4ee72eec7c9d1
---

```
1. typedef struct ArkUI_VisibleAreaEventOptions ArkUI_VisibleAreaEventOptions
```

## 概述

PhonePC/2in1TabletTVWearable

可见区域变化监听的参数。

开发者在使用该类型时，首先需要调用[OH\_ArkUI\_VisibleAreaEventOptions\_Create](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_create)创建一个ArkUI\_VisibleAreaEventOptions参数对象。然后可通过如下接口配置监听行为：

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setratios)设置阈值数组，定义触发可见区域变化的阈值条件。

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setexpectedupdateinterval)设置预期更新间隔。

使用[OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setmeasurefromviewport)设置可见区域的计算模式。

如需获取已设置的参数值，可使用：

[OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getratios)获取阈值数组。

[OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getexpectedupdateinterval)获取预期更新间隔。

[OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getmeasurefromviewport)获取可见区域计算模式。

使用完毕后，应调用[OH\_ArkUI\_VisibleAreaEventOptions\_Dispose](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_dispose)释放资源。

**起始版本：** 17

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)
