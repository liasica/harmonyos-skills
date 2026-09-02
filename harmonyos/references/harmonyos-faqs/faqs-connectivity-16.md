---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-16
title: HarmonyOS是否支持通过蓝牙连接第三方设备的音频模块
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > HarmonyOS是否支持通过蓝牙连接第三方设备的音频模块
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7f621b673793137ab91ae71ce3fcbe15b5b4d467f36b346c42cf659723b9fd6b
---

## 问题现象

HarmonyOS是否支持通过蓝牙连接第三方设备音频模块，是否有相关的接口能力？

## 背景知识

* [@ohos.bluetooth.hfp (蓝牙hfp模块)](../harmonyos-references/js-apis-bluetooth-hfp.md)提供了访问蓝牙呼叫接口的方法。HFP协议定义了设备间语音交互的标准化流程，在HFP协议中存在两种角色：
  + AG：音源设备，负责音频传输，联系人信息发送，通话控制等。
  + HF：音频接收输出，用户操作等。
* 蓝牙开发流程可参考：[查找设备](../harmonyos-guides/br-discovery-development-guide.md)，[配对与连接设备](../harmonyos-guides/br-pair-device-development-guide.md)，[连接和传输数据](../harmonyos-guides/spp-development-guide.md)。

## 解决方案

需要确认对端设备是否支持HFP协议，可通过[hfp.createHfpAgProfile](../harmonyos-references/js-apis-bluetooth-hfp.md#hfpcreatehfpagprofile)创建[HandsFreeAudioGatewayProfile](../harmonyos-references/js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile)后，连接到对应的profile进行开发。

完整开发示例可参考：[配对与连接设备完整示例](../harmonyos-guides/br-pair-device-development-guide.md#完整示例)。

## 常见FAQ

Q：参考上述方案进行开发，可以配对成功，但为什么连接的时候提示2900099？

A：蓝牙子系统会在配对过程中查询和保存目标设备支持的所有profile能力。建议判断目标设备的profile能力是否存在A2DP/HFP/HID。
