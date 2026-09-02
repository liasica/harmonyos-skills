---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription
title: 取消订阅公共事件（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 取消订阅公共事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b8fbdc4cd4a5b0ccb823eb55fa346829078881b4bffa45ecd7a9b1bb5884b0a
---

## 场景介绍

订阅者在完成业务需求之后，需要取消订阅公共事件。

## 接口说明

详细的API说明请参考[oh\_commonevent.h](../harmonyos-references/capi-oh-commonevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| [CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_unsubscribe) | 取消订阅公共事件。 |

## 开发步骤

1. 引用头文件。

   ```c
   #include "hilog/log.h"
   #include "BasicServicesKit/oh_commonevent.h"
   ```
2. 在CMake脚本中添加动态链接库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libhilog_ndk.z.so
       libohcommonevent.so
   )
   ```
3. 取消订阅公共事件。

   订阅者订阅公共事件并完成业务需求后，可以通过[OH\_CommonEvent\_UnSubscribe](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_unsubscribe)主动取消订阅事件。

   ```
   void Unsubscribe(CommonEvent_Subscriber *subscriber)
   {
       // 通过传入订阅者来退订事件
       int32_t ret = OH_CommonEvent_UnSubscribe(subscriber);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_UnSubscribe ret <%{public}d>.", ret);
   }
   ```
