---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-map
title: @ohos.bluetooth.map (蓝牙map模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.map (蓝牙map模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:668cf0cac0a00871b09c891ceaef66c4bc57499db6bc6cdf2dde420c9daea935
---

本模块提供基于消息访问协议（Message Access Profile，[MAP](../harmonyos-guides/terminology.md#map)）的蓝牙消息访问能力，支持获取连接状态等方法。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { map } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## map.createMapMseProfile

PhonePC/2in1TabletTVWearable

createMapMseProfile(): MapMseProfile

创建蓝牙消息访问协议中的[MSE](../harmonyos-guides/terminology.md#mse)实例。通过该实例可使用本端作为MSE设备的接口，如：获取和其他设备间的蓝牙消息服务连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MapMseProfile | 返回该profile的实例。 |

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
4. let mapMseProfile = map.createMapMseProfile();
5. console.info('MapMse success');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## MapMseProfile

PhonePC/2in1TabletTVWearable

该实例表示蓝牙消息访问协议中的[MSE](../harmonyos-guides/terminology.md#mse)角色。

* 该类继承于[BaseProfile](js-apis-bluetooth-map.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的接口前，需通过[createMapMseProfile](js-apis-bluetooth-map.md#mapcreatemapmseprofile)接口构造该类的实例。
* 和该实例角色相对应的是[MCE](../harmonyos-guides/terminology.md#mce)角色。
