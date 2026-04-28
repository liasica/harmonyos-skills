---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-qoscallback-c
title: 网络质量评估 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 (C/C++) > 网络质量评估 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:812a07b826520c8c5fdf176624b75efb3c41f87f3801ec33cdfcdeac22d06b30
---

## 场景介绍

应用在订阅网络质量Qos评估后，系统按照一定的周期或Qos变化后回调给应用。回调的Qos信息包括数据传输的链路类型、上下行空口实时带宽、上下行空口实时速率、RTT时延等。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/network-boost-c-overview.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_NetworkBoost\_RegisterNetQosCallback(HMS\_NetworkBoost\_NetQosChange callback, uint32\_t\* callbackId) | 注册Qos信息状态变化回调。 |
| int32\_t HMS\_NetworkBoost\_UnregisterNetQosCallback(uint32\_t callbackId) | 取消注册Qos信息状态变化回调。 |

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
3. 通过注册回调的方式监听网络质量评估信息。

   ```
   1. uint32_t callbackId = 0;
   2. void onNetworkQoSChanged(NetworkBoost_NetworkQosArray *msg)
   3. {
   4. for (int32_t i = 0; i < msg->pathNum; i++) {
   5. // 回调信息处理
   6. printf("数据链路类型: %d\n", msg->networkQos[i].pathType);
   7. printf("该数据链路类型的上行带宽: %ld\n", msg->networkQos[i].linkUpBandwidth);
   8. printf("该数据链路类型的下行带宽: %ld\n", msg->networkQos[i].linkDownBandwidth);
   9. // 单位为bps，若需转化为B/s，数值需要除以8
   10. printf("该数据链路类型的上行速率: %ld\n", msg->networkQos[i].linkUpRate);
   11. // 单位为bps，若需转化为B/s，数值需要除以8
   12. printf("该数据链路类型的下行速率: %ld\n", msg->networkQos[i].linkDownRate);
   13. // 实时速率为上行速率和下行速率之和
   14. printf("该数据链路类型的实时速率(B/s): %ld\n", (msg->networkQos[i].linkUpRate + msg->networkQos[i].linkDownRate) / 8);
   15. printf("该数据链路类型的RTT时延: %d\n", msg->networkQos[i].rttMs);
   16. printf("该数据链路类型的上行发送空口缓冲时延: %d\n", msg->networkQos[i].linkUpBufferDelayMs);
   17. }
   18. }

   20. int32_t RegisterNetQualityCallback()
   21. {
   22. HMS_NetworkBoost_NetQosChange callback;
   23. callback = onNetworkQoSChanged;
   24. // 注册回调，获取回调Id
   25. int32_t ret = HMS_NetworkBoost_RegisterNetQosCallback(callback, &callbackId);
   26. printf("注册网络质量结果: %d, Id：%d\n", ret, callbackId);
   27. return ret;
   28. }
   ```
4. 当应用业务流程结束，通过取消注册的方式取消监听网络质量评估信息。

   ```
   1. int32_t UnregisterNetQualityCallback()
   2. {
   3. // 使用注册时获取的回调Id取消注册
   4. int32_t ret = HMS_NetworkBoost_UnregisterNetQosCallback(callbackId);
   5. printf("取消注册网络质量结果: %d\n", ret);
   6. return ret;
   7. }
   ```
