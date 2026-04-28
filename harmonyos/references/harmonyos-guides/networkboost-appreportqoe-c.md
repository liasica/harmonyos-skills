---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-appreportqoe-c
title: 应用传输体验反馈 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 (C/C++) > 应用传输体验反馈 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1283d9fe64a6ccc1a91cc4d479f09c60633f2dee363ac31ff988cd9876bbdae
---

## 场景介绍

当应用传输体验发生变化时，应用将传输体验和传输的业务类型信息通过实时反馈接口传输给系统网络业务模块，系统网络业务模块进行精细化调度，实现网络加速。

例如：视频类App播放过程中卡顿，将卡顿信息上报后，Network Boost Kit将信息反馈给系统网络加速模块，该模块会记录播放卡顿信息，并根据当前网络情况，启用网络加速能力。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_ReportQoe(NetworkBoost\_ServiceType serviceType, NetworkBoost\_QoeType qoeType) | 应用反馈传输体验信息。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. #include "NetworkBoostKit/network_boost_quality.h"
   2. #include <cstdio>
   ```
2. CMakeLists.txt中添加以下lib，具体请见[C API开发准备](networkboost-preparations.md#c-api开发准备)。

   ```
   1. libnetwork_boost.so
   ```
3. 调用ReportQoe接口将应用传输体验信息通知给系统。

   ```
   1. int32_t ReportQoe()
   2. {
   3. NetworkBoost_ServiceType serviceType = NB_SERVICE_SHORT_VIDEO;
   4. NetworkBoost_QoeType qoeType = NB_QOE_BAD_SERVER_ERROR;
   5. int32_t ret = HMS_NetworkBoost_ReportQoe(serviceType, qoeType);
   6. printf("传输体验反馈结果: %d\n", ret);
   7. return ret;
   8. }
   ```
