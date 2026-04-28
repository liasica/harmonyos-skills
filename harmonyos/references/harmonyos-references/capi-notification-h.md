---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-notification-h
title: notification.h
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > C API > 头文件 > notification.h
category: harmonyos-references
scraped_at: 2026-04-28T08:17:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a40a8ce4a3d30ec92217c2f020d9d3983e371904f13db76ae1aba95cde2344dd
---

## 概述

PhonePC/2in1TabletTVWearable

定义通知服务API接口。

**引用文件：** <NotificationKit/notification.h>

**库：** libohnotification.so

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 13

**相关模块：** [NOTIFICATION](capi-notification.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [bool OH\_Notification\_IsNotificationEnabled(void)](capi-notification-h.md#oh_notification_isnotificationenabled) | 查询当前应用通知使能状态。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Notification\_IsNotificationEnabled()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Notification_IsNotificationEnabled(void)
```

**描述**

查询当前应用通知使能状态。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true - 表示当前应用已使能通知。  false - 表示当前应用未使能通知。 |
