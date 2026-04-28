---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc-c
title: 业务场景设置(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网并发)（C/C++） > 业务场景设置(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b73a3f6862697234691684a55fc2a59ce587f7d09ad25fc6727ca623180bc288
---

从6.0.2(22)开始，支持业务场景设置。

## 场景介绍

应用在请求多网并发之前，通过设置业务场景，可以帮助系统进行多网并发管控和业务时长分析。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_SetSceneDesc(NetworkBoost\_SceneDesc sceneDesc) | 设置业务场景。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. #include "NetworkBoostKit/network_boost.h"
   2. #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```
   1. libnetwork_boost.so
   ```
3. 调用SetSceneDesc接口。

   ```
   1. int32_t SetSceneDesc()
   2. {
   3. NetworkBoost_SceneDesc sceneDesc;
   4. sceneDesc.duration = 0;
   5. sceneDesc.startTime = 0;
   6. sceneDesc.scene = NB_SERVICE_LOGIN;
   7. sceneDesc.sceneEvent = SCENE_EVENT_ENTER;
   8. int32_t ret = HMS_NetworkBoost_SetSceneDesc(sceneDesc);
   9. printf("业务场景设置结果: %d\n", ret);
   10. return ret;
   11. }
   ```
