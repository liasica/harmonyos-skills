---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-reporthandovermode-c
title: 迁移模式设置 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网切换) (C/C++) > 迁移模式设置 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05d7ae7b8f022e09f8525686f30e146ccc1ee6b7b56a15ebb7f7061fed648a80
---

## 场景介绍

应用可通过迁移模式设置接口变更连接迁移模式，包括委托模式（由系统发起连接迁移）和自主模式（由应用发起连接迁移）。应用未调用SetHandoverMode则默认为委托模式，应用可以通过该接口禁止系统发起连接迁移。在某些场景下，比如该应用切换到后台时，依旧有可能由系统触发切换。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_SetHandoverMode(NetworkBoost\_HandoverMode mode) | 应用设置迁移模式，默认为委托模式。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. #include "NetworkBoostKit/network_boost_handover.h"
   2. #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```
   1. libnetwork_boost.so
   ```
3. 调用SetHandoverMode接口，设置为自主模式，禁止系统发起连接迁移。

   ```
   1. int32_t SetHandoverMode()
   2. {
   3. NetworkBoost_HandoverMode mode = NB_MODE_DISCRETION;
   4. int32_t ret = HMS_NetworkBoost_SetHandoverMode(mode);
   5. printf("设置连接迁移模式结果: %d\n", ret);
   6. return ret;
   7. }
   ```
