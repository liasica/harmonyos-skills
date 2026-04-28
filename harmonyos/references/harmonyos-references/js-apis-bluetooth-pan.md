---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-pan
title: @ohos.bluetooth.pan (蓝牙pan模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.pan (蓝牙pan模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9fd71d3724c398d001db1119720abd6309a65dc94dc4e0395a879984d016e275
---

本模块提供基于蓝牙个人局域网协议（Personal Area Networking，[PAN](../harmonyos-guides/terminology.md#pan)）的蓝牙共享网络能力，支持获取连接状态等方法。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { pan } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## pan.createPanProfile

PhonePC/2in1TabletTVWearable

createPanProfile(): PanProfile

创建蓝牙[NAP](../harmonyos-guides/terminology.md#nap)实例。通过该实例可使用本端作为NAP设备的接口，如：获取和其他设备间的蓝牙个人局域网服务连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PanProfile | 返回NAP实例。  - 该类继承于[BaseProfile](js-apis-bluetooth-pan.md#baseprofile)，因此可以使用其父类中的方法。  - 和该实例角色相对应的是[PANU](../harmonyos-guides/terminology.md#panu)角色。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let panProfile : pan.PanProfile= pan.createPanProfile();
5. console.info('pan success');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```
