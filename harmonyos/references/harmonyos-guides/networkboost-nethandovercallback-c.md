---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-nethandovercallback-c
title: 连接迁移通知 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网切换) (C/C++) > 连接迁移通知 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:348ed7003b768ea9a54f48b638973798015fc217261f153e768f7c901f3c659c
---

## 场景介绍

在弱网环境下，系统发起多网迁移（Wi-Fi与蜂窝网络切换，主卡与副卡切换等）的过程中，给应用提供连接迁移开始和完成通知，应用根据连接迁移通知的建议进行网络连接重建，快速恢复业务，给用户带来平滑、高速、低时延的上网体验。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_RegisterHandoverChangeCallback(HMS\_NetworkBoost\_HandoverCallback\* callback, uint32\_t\* callbackId) | 注册连接迁移回调。 |
| int32\_t HMS\_NetworkBoost\_UnregisterHandoverChangeCallback(uint32\_t callbackId) | 取消注册连接迁移回调。 |

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
3. 通过注册回调的方式获取连接迁移信息。

   ```cpp
   uint32_t callbackId = 0;
   void onNetworkHandoverStart(NetworkBoost_HandoverStart* handoverStart)
   {
       // 连接迁移开始回调，应用按照HandoverStart的建议调整数传策略
   }

   void onNetworkHandoverComplete(NetworkBoost_HandoverComplete* handoverComplete)
   {
       // 连接迁移完成回调，应用按照HandoverComplete的建议进行调速和重建恢复
   }

   int32_t RegisterNetworkHandoverCallback()
   {
       HMS_NetworkBoost_HandoverCallback callback;
       callback.onNetworkHandoverStart = onNetworkHandoverStart;
       callback.onNetworkHandoverComplete = onNetworkHandoverComplete;
       // 注册回调，获取回调Id，该Id由系统返回并用于后续取消注册操作
       int32_t ret = HMS_NetworkBoost_RegisterHandoverChangeCallback(&callback, &callbackId);
       printf("注册连接迁移结果: %d, Id：%d\n", ret, callbackId);
       return ret;
   }
   ```
4. 当应用业务流程结束，通过取消注册的方式取消监听连接迁移信息。

   ```cpp
   int32_t UnregisterNetworkHandoverCallback() {
       // 使用注册时获取的回调Id取消注册
       int32_t ret = HMS_NetworkBoost_UnregisterHandoverChangeCallback(callbackId);
       printf("取消注册连接迁移结果: %d\n", ret);
       return ret;
   }
   ```
