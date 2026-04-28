---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hfp
title: @ohos.bluetooth.hfp (蓝牙hfp模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.hfp (蓝牙hfp模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2644c25ec782b5f7bc4ff93a6e8b8a35034e2c16a36ffb47331fd63a7be0b317
---

本模块提供基于免提协议（Hands-Free Profile， [HFP](../harmonyos-guides/terminology.md#hfp)）的蓝牙通话音频能力，支持获取连接状态等方法。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { hfp } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## hfp.createHfpAgProfile

PhonePC/2in1TabletTVWearable

createHfpAgProfile(): HandsFreeAudioGatewayProfile

创建蓝牙通话音频中的[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)实例。通过该实例可使用本端作为HFP AG设备的接口，如：获取和其他设备间的蓝牙通话音频连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HandsFreeAudioGatewayProfile](js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile) | 返回HFP AG实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let hfpAgProfile = hfp.createHfpAgProfile();
5. console.info('hfpAg success');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## HandsFreeAudioGatewayProfile

PhonePC/2in1TabletTVWearable

该实例表示蓝牙通话音频中的[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)角色‌。

* 该类继承于[BaseProfile](js-apis-bluetooth-hfp.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的接口前，需通过[createHfpAgProfile](js-apis-bluetooth-hfp.md#hfpcreatehfpagprofile)接口构造该类的实例。
* 和该实例角色相对应的是[HF](../harmonyos-guides/terminology.md#hf)角色。
