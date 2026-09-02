---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-statechangecallback-c
title: 多网状态监听(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网并发)（C/C++） > 多网状态监听(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b6f9859e2b50b6d485e513733fe9daa1ae12f6701ecf8b029b61150bc59976ed
---

从6.0.2(22)开始，支持多网状态监听。

## 场景介绍

应用通过监听多网络状态的变化，感知可用网络的变化，从而选择在多网络上传输数据的策略。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback(HMS\_NetworkBoost\_OnMultiPathStateChangecallback, uint32\_t \*callbackId) | 注册多网状态变化事件。 |
| int32\_t HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback(uint32\_t callbackId) | 去注册多网状态变化事件。 |

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
3. 调用HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback接口，获取多网状态变化信息。

   ```cpp
   uint32_t callbackId = 0;
   void onMultiPathStateChangeCallback(NetworkBoost_MultiPathStateChange* result)
   {
       // 多网状态变化回调处理
       if (result != NULL) {
           printf("多网状态回调：多网状态=%d, 多网状态变化原因=%d\n", result->multiPathState, result->changeCause);
           printf("多网状态回调：多网链路的netHandle=%d, 多网链路状态=%d\n", result->netHandle, result->pathState);
           printf("多网状态回调：多网链路类型=%d\n", result->pathType);
       } else {
           printf("回调参数为空\n");
       }
   }

   int32_t RegisterMultiPathStateChange()
   {
       // 注册回调，获取回调Id，该Id由系统返回并用于后续取消注册操作
       int32_t ret = HMS_NetworkBoost_RegisterMultiPathStateChangeCallback(onMultiPathStateChangeCallback, &callbackId);
       printf("注册多网状态监听回调结果: %d, Id：%d\n", ret, callbackId);
       return ret;
   }
   ```
4. 当应用业务流程结束，通过取消注册的方式取消多网状态监听。

   ```cpp
   int32_t UnregisterMultiPathStateChange() {
       // 使用注册时获取的回调Id取消注册
       int32_t ret = HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback(callbackId);
       printf("取消多网状态监听回调结果: %d\n", ret);
       return ret;
   }
   ```
