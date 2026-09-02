---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragentextensionability
title: "@ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fae7f170d2d07a40d9e4c2a8c42c384c430d64c651af5d9b7dab0bfe42253ec7
---

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。应用模块级配置文件[module.json5](../harmonyos-guides/module-configuration-file.md) 中的[extensionabilities](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的type属性应该配置为partnerAgent。

**说明** 

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 约束限制

为保障系统安全性和稳定性，防止PartnerAgentExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-fusionconnectivity-partneragentextensionability.md#附录)。

## 导入模块

```ts
import { PartnerAgentExtensionAbility, partnerAgent } from '@kit.ConnectivityKit';
```

## PartnerDeviceAddress

type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress

描述设备地址信息。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partnerdeviceaddress) | 信息互通设备的地址信息。 |

## PartnerAgentExtensionAbilityDestroyReason

type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason

描述PartnerAgentExtensionAbility被销毁的原因。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerAgentExtensionAbilityDestroyReason](js-apis-fusionconnectivity-partneragent.md#partneragentextensionabilitydestroyreason) | PartnerAgentExtensionAbility被销毁的原因。 |

## PartnerAgentExtensionAbility

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，本能力继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)，需要应用继承实现。

### 属性

**系统能力**： SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [PartnerAgentExtensionContext](js-apis-fusionconnectivity-partneragentextensioncontext.md) | 否 | 否 | PartnerAgentExtensionAbility的上下文。 |

### onDestroyWithReason

onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void

外设互通扩展能力被销毁时触发的方法回调。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [PartnerAgentExtensionAbilityDestroyReason](js-apis-fusionconnectivity-partneragent.md#partneragentextensionabilitydestroyreason) | 是 | 通知销毁该外设互通扩展能力的原因。不同枚举值代表不同的销毁场景，应用可根据不同的销毁原因执行相应的资源释放或状态保存逻辑。 |

**示例：**

```ts
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
    console.info(`onDestroyWithReason is: ${reason}`);
  }
}
```

### onDeviceDiscovered

onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void

当已注册的设备被发现时，系统会调用此回调方法。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用需在PartnerDeviceAddress类型中设置bluetoothAddress选项。 |

**示例：**

```ts
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
    console.info(`onDeviceDiscovered success: ${deviceAddress.bluetoothAddress}`);
  }
}
```

## 附录

PartnerAgentExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Background Tasks Kit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Background Tasks Kit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Camera Kit | [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| Connectivity Kit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md) |
| Connectivity Kit | [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md) |
| Connectivity Kit | [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md) |
| Connectivity Kit | [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md) |
| Connectivity Kit | [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| Connectivity Kit | [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md) |
| Connectivity Kit | [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md) |
| Connectivity Kit | [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md) |
| Location Kit | [@ohos.geolocation (位置服务)](js-apis-geolocation.md) |
| Location Kit | [@ohos.geoLocationManager (位置服务)](js-apis-geolocationmanager.md) |
| Media Library Kit | [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md) |
| Telephony Kit | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| Telephony Kit | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
