---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hfp
title: "@ohos.bluetooth.hfp (蓝牙hfp模块)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.hfp (蓝牙hfp模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50fa903ca141c5545cc03012ac0fba12a4fc7eeaed89aaf15d17623b5f03ac9e
---

本模块提供基于免提协议（Hands-Free Profile， [HFP](../harmonyos-guides/terminology.md#hfp)）的蓝牙通话音频能力，支持创建[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)和[HF](../harmonyos-guides/terminology.md#hf)实例、获取连接状态等。适用于需要在应用中实现蓝牙通话音频连接管理、监听通话音频连接状态等场景。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { hfp } from '@kit.ConnectivityKit';
```

## BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## hfp.createHfpAgProfile

createHfpAgProfile(): HandsFreeAudioGatewayProfile

创建蓝牙通话音频中的[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)实例。通过该实例可使用本端作为HFP AG设备的接口，如：获取和其他设备间的蓝牙通话音频连接状态。典型应用场景包括车载信息娱乐系统的蓝牙通话功能等，本端设备作为音频网关（AG）角色管理通话音频路由。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [HandsFreeAudioGatewayProfile](js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile) | 返回HFP AG实例，可用于获取和其他设备间的蓝牙通话音频连接状态等操作。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```js
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let hfpAgProfile = hfp.createHfpAgProfile();
    console.info('hfpAg success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## hfp.createHfpHfProfile

createHfpHfProfile(): HandsFreeHfProfile

创建蓝牙通话音频中的[HF](../harmonyos-guides/terminology.md#hf)实例。通过该实例可使用本端作为HF设备的接口，如：获取和其他设备间的蓝牙通话音频连接状态。典型应用场景包括蓝牙耳机的免提通话功能、车载免提系统等，本端设备作为免提（HF）角色接收和处理通话音频。

**起始版本**： 26.0.0

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [HandsFreeHfProfile](js-apis-bluetooth-hfp.md#handsfreehfprofile) | 返回HF实例，可用于获取和其他设备间的蓝牙通话音频连接状态等操作。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例**：

```js
try {
    let hfProfile = hfp.createHfpHfProfile();
    console.info('hf success');
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

## HandsFreeAudioGatewayProfile

该实例表示蓝牙通话音频中的[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)角色‌。

* 该类继承于[BaseProfile](js-apis-bluetooth-hfp.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的接口前，需通过[createHfpAgProfile](js-apis-bluetooth-hfp.md#hfpcreatehfpagprofile)接口构造该类的实例。
* 和该实例角色相对应的是[HF](../harmonyos-guides/terminology.md#hf)角色。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

## HandsFreeHfProfile

该实例表示蓝牙通话音频中的[HF](../harmonyos-guides/terminology.md#hf)角色‌。

* 该类继承于[BaseProfile](js-apis-bluetooth-hfp.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的接口前，需通过[createHfpHfProfile](js-apis-bluetooth-hfp.md#hfpcreatehfphfprofile)接口构造该类的实例。
* 和该实例角色相对应的是[HFP AG](../harmonyos-guides/terminology.md#hfp-ag)角色。

**起始版本**： 26.0.0

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。
