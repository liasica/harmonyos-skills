---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-scenecallback-c
title: 网络场景识别 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 (C/C++) > 网络场景识别 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:253144b8943406e3d151608dafdad34af062be20798fcdb101294a5af546a4cf
---

## 场景介绍

应用在订阅网络场景识别后，系统在网络场景实时信息或预测信息发生变化后回调给应用，回调的网络场景信息包括数据传输的链路类型、网络场景类型、数传策略建议、弱信号信息等。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_RegisterNetSceneCallback(HMS\_NetworkBoost\_NetSceneChange callback, uint32\_t\* callbackId) | 注册网络场景信息状态变化回调。 |
| int32\_t HMS\_NetworkBoost\_UnregisterNetSceneCallback(uint32\_t callbackId) | 取消注册网络场景信息状态变化回调。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```cpp
   #include "NetworkBoostKit/network_boost_quality.h"
   #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```cpp
   libnetwork_boost.so
   ```
3. 通过注册回调的方式监听网络场景识别信息。

   ```cpp
   uint32_t callbackId = 0;
   void onNetworkSceneChanged(NetworkBoost_NetworkScene *ns)
   {
       // 网络场景识别回调信息处理
       printf("数据路径类型: %d\n", ns->pathType);
       printf("网络场景: %d\n", ns->scene);
       switch (ns->scene) {
           case NB_SCENE_NORMAL:
               // 普通场景处理
               break;
           case NB_SCENE_CONGESTION:
               // 拥塞场景处理
               break;
           case NB_SCENE_FREQUENT_HANDOVER:
               // 信号快切场景处理
               break;
           case NB_SCENE_WEAK_SIGNAL:
               // 弱信号场景处理
               break;
       }
       printf("应用数传策略建议: %d\n", ns->recommendedAction);
       if (ns->weakSignalPrediction.duration > 0) {
           // 弱信号预测处理
       }
   }

   int32_t RegisterNetSceneCallback()
   {
       HMS_NetworkBoost_NetSceneChange callback;
       callback = onNetworkSceneChanged;
       // 注册回调，获取回调Id，该Id由系统返回并用于后续取消注册操作
       int32_t ret = HMS_NetworkBoost_RegisterNetSceneCallback(callback, &callbackId);
       printf("注册网络场景结果: %d, Id：%d\n", ret, callbackId);
       return ret;
   }
   ```
4. 当应用业务流程结束，通过取消注册的方式取消监听网络场景识别信息。

   ```cpp
   int32_t UnregisterNetSceneCallback()
   {
       // 使用注册时获取的回调Id取消注册
       int32_t ret = HMS_NetworkBoost_UnregisterNetSceneCallback(callbackId);
       printf("取消注册网络场景结果: %d\n", ret);
       return ret;
   }
   ```
