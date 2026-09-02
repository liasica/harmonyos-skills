---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc-c
title: 业务场景设置(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网并发)（C/C++） > 业务场景设置(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4c84ea3886cc313561f1fabe472eb1b9b09e0ee022eabe7b5cf6935d552d9537
---

从6.0.2(22)开始，支持业务场景设置。

## 场景介绍

本节介绍如何在请求多网并发之前，通过设置业务场景来帮助系统进行多网并发管控和业务时长分析。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_SetSceneDesc(NetworkBoost\_SceneDesc sceneDesc) | 设置业务场景。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```cpp
   #include "NetworkBoostKit/network_boost.h"
   #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```cpp
   libnetwork_boost.so
   ```
3. 调用SetSceneDesc接口。

   ```cpp
   int32_t SetSceneDesc()
   {
       NetworkBoost_SceneDesc sceneDesc;
       sceneDesc.duration = 0;
       sceneDesc.startTime = 0;
       sceneDesc.scene = NB_SERVICE_LOGIN;
       sceneDesc.sceneEvent = SCENE_EVENT_ENTER;
       int32_t ret = HMS_NetworkBoost_SetSceneDesc(sceneDesc);
       if (ret == 0) {
           printf("业务场景设置成功: duration=%ld, startTime=%ld, scene=%d, sceneEvent=%d\n",
               sceneDesc.duration, sceneDesc.startTime, sceneDesc.scene, sceneDesc.sceneEvent);
       } else {
           printf("业务场景设置失败，错误码: %d\n", ret);
       }
       return ret;
   }
   ```
