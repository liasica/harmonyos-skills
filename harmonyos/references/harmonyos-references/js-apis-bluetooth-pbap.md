---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-pbap
title: "@ohos.bluetooth.pbap (蓝牙pbap模块)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.pbap (蓝牙pbap模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2a69d8f39274a145160c55bb625d236e576d9d223363904ba6b382849d2f7b89
---

本模块提供基于电话簿访问协议（Phone Book Access Profile，[PBAP](../harmonyos-guides/terminology.md#pbap)）的蓝牙电话簿访问能力，支持创建[PSE](../harmonyos-guides/terminology.md#pse)服务端实例、获取设备间蓝牙电话簿服务连接状态等，适用于本端设备作为PSE对外提供电话簿访问服务的场景，可帮助开发者快速实现蓝牙电话簿的共享与连接管理功能。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { pbap } from '@kit.ConnectivityKit';
```

## BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## pbap.createPbapServerProfile

createPbapServerProfile(): PbapServerProfile

创建蓝牙电话簿访问协议中的[PSE](../harmonyos-guides/terminology.md#pse)实例。通过该实例可使用本端作为PSE设备的接口，如：获取本端和其他设备间的蓝牙电话簿服务连接状态。典型使用场景包括：车载蓝牙系统访问手机电话簿、跨设备联系人同步等需要本端作为电话簿服务端的场景。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PbapServerProfile | 返回PSE实例。  - 该类继承于[BaseProfile](js-apis-bluetooth-pbap.md#baseprofile)，因此可以使用其父类中的方法。  - 和该实例角色相对应的是[PCE](../harmonyos-guides/terminology.md#pce)角色。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let pbapServerProfile = pbap.createPbapServerProfile();
    console.info('pbapServer success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
