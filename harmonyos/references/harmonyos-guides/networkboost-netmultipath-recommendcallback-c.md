---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-recommendcallback-c
title: 多网建议监听(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网并发)（C/C++） > 多网建议监听(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:597e09c38c6a569927de55e66c24a3addeaef22d1202942721da93723fa4d65b
---

从6.0.2(22)开始，支持多网建议监听。

## 场景介绍

系统感知到应用可能需要使用多网络加速的场景时，如弱网、网络切换等特定场景，会给出建议。应用通过监听多网络加速的建议，决策发起多网络加速的请求。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback(HMS\_NetworkBoost\_OnMultiPathRecommendationcallback, uint32\_t \*callbackId) | 注册系统多网建议变化事件。 |
| int32\_t HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback(uint32\_t callbackId) | 取消注册系统多网建议变化事件。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```cpp
   #include "NetworkBoostKit/network_boost_handover.h"
   #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```cpp
   libnetwork_boost.so
   ```
3. 调用HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback接口，注册多网建议变化回调。

   ```cpp
   uint32_t callbackId = 0;
   void onMultiPathRecommendationCallback(NetworkBoost_MultiPathRecommendation* recommendation)
   {
       if (recommendation != nullptr) {
           printf("Recommendation type: %d\n", recommendation->action);
       }
       // 多网建议变化回调处理
   }

   int32_t RegisterMultiPathRecommendation()
   {
       // 注册回调，获取回调Id，该Id由系统返回并用于后续取消注册操作
       int32_t ret = HMS_NetworkBoost_RegisterMultiPathRecommendationCallback(onMultiPathRecommendationCallback, &callbackId);
       printf("注册多网建议监听回调结果: %d, Id：%d\n", ret, callbackId);
       return ret;
   }
   ```
4. 当应用业务流程结束，取消注册多网建议变化回调。

   ```cpp
   int32_t UnregisterMultiPathRecommendation() {
       // 使用注册时获取的回调Id取消注册
       int32_t ret = HMS_NetworkBoost_UnregisterMultiPathRecommendationCallback(callbackId);
       printf("取消多网建议监听回调结果: %d\n", ret);
       return ret;
   }
   ```
