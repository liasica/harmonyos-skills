---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription
title: 取消订阅公共事件（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 取消订阅公共事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dffcbc00cf90c92216f5709263fb59f0a3a96596393f4a728fb74bce4957dba4
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

   ```
   1. #include "hilog/log.h"
   2. #include "BasicServicesKit/oh_commonevent.h"
   ```

   [common\_event\_unsubscribe.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_unsubscribe.h#L19-L22)
2. 在CMake脚本中添加动态链接库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libohcommonevent.so
   5. )
   ```
3. 取消订阅公共事件。

   订阅者订阅公共事件并完成业务需求后，可以通过[OH\_CommonEvent\_UnSubscribe](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_unsubscribe)主动取消订阅事件。

   ```
   1. void Unsubscribe(CommonEvent_Subscriber *subscriber)
   2. {
   3. // 通过传入订阅者来退订事件
   4. int32_t ret = OH_CommonEvent_UnSubscribe(subscriber);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_UnSubscribe ret <%{public}d>.", ret);
   6. }
   ```

   [common\_event\_unsubscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_unsubscribe.cpp#L17-L24)
