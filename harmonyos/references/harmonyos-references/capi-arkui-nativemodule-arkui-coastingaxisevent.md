---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coastingaxisevent
title: ArkUI_CoastingAxisEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CoastingAxisEvent
category: harmonyos-references
scraped_at: 2026-04-28T08:04:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:122858f495cea2c4cc6ac907f1bc6d9152fdf5a68f291a4eda31b32991574414
---

```
1. typedef struct ArkUI_CoastingAxisEvent ArkUI_CoastingAxisEvent
```

## 概述

PhonePC/2in1TabletTVWearable

定义惯性滚动轴事件。

当用户在触控板上用双指滑动时，系统会根据手指抬起时的速度，按照一定的衰减曲线构造滑动事件。可以监听此类事件，以便在常规轴事件之后立即处理抛滑效果。

仅当用户在触控板上双指抛滑，且指针位置下存在通过[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](capi-native-node-h.md#arkui_nodeeventtype)事件的组件时，才能接收到此事件。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](capi-arkui-eventmodule.md)

**所在头文件：** [ui\_input\_event.h](capi-ui-input-event-h.md)
