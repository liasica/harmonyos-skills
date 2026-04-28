---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-getmultipathquota-c
title: 多网配额查询(C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移(多网并发)（C/C++） > 多网配额查询(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c49b5e85e24f27e07570a030399d94d5b6ebad841cf71733d8a55c75535d0a7
---

从6.0.2(22)开始，支持多网配额查询。

## 场景介绍

由于多网络加速受到配额的管控，应用可以获取当前剩余的多网并发配额信息，合理分配使用多网络加速的次数和时长。应用配额以24小时的周期进行刷新。配额（次数或时长）耗尽会限制使用，此时请求多网会抛出错误码，24小时后会重新分配。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_GetMultiPathQuotaStats(NetworkBoost\_MultiPathQuota \*quota) | 获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。 |

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
3. 调用GetMultiPathQuotaStats接口，获取多网配额信息。

   ```
   1. int32_t GetMultiPathQuotaStats()
   2. {
   3. NetworkBoost_MultiPathQuota quota = { 0 };
   4. int32_t ret = HMS_NetworkBoost_GetMultiPathQuotaStats(&quota);
   5. printf("获取多网配额信息结果: %d\n", ret);
   6. printf("获取多网配额信息已使用时长: %d\n", quota.used.duration);
   7. printf("获取多网配额信息已使用次数: %d\n", quota.used.count);
   8. printf("获取多网配额信息剩余总时长: %d\n", quota.remaining.duration);
   9. printf("获取多网配额信息剩余总次数: %d\n", quota.remaining.count);
   10. return ret;
   11. }
   ```
