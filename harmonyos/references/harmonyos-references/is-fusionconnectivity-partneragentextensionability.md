---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-fusionconnectivity-partneragentextensionability
title: @ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6984265c4dc8a73214fde7b4c8da5426940d49bbc0b25604e4cdd338140303c
---

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。应用模块级配置文件[module.json5](../harmonyos-guides/module-configuration-file.md) 中的[extensionabilities](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的type属性应该配置为partnerAgent。

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1Tablet

```
1. import { PartnerAgentExtensionAbility, partnerAgent } from '@kit.ConnectivityKit';
```

## PartnerDeviceAddress

PhonePC/2in1Tablet

type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress

描述设备地址信息。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 信息互通设备的地址信息。 |

## PartnerAgentExtensionAbilityDestroyReason

PhonePC/2in1Tablet

type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason

描述PartnerAgentExtensionAbility被销毁的原因。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerAgentExtensionAbilityDestroyReason](js-apis-fusionconnectivity-partneragent.md#partneragentpartneragentextensionabilitydestroyreason) | PartnerAgentExtensionAbility被销毁的原因。 |

## PartnerAgentExtensionAbility

PhonePC/2in1Tablet

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。本能力继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)。

### 属性

PhonePC/2in1Tablet

**系统能力**： SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [PartnerAgentExtensionContext](is-fusionconnectivity-partneragentextensioncontext.md) | 否 | 否 | PartnerAgentExtensionAbility的上下文。 |

### onDestroyWithReason

PhonePC/2in1Tablet

onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void

外设互通扩展能力被销毁时触发的方法回调。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [PartnerAgentExtensionAbilityDestroyReason](js-apis-fusionconnectivity-partneragent.md#partneragentpartneragentextensionabilitydestroyreason) | 是 | 通知销毁该应用的原因。 |

**示例：**

```
1. export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
2. onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
3. console.info(`onDestroyWithReason is: ${reason}`);
4. }
5. }
```

### onDeviceDiscovered

PhonePC/2in1Tablet

onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void

当已注册的设备被发现时，系统会调用此回调方法。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用需在PartnerDeviceAddress类型中设置bluetoothAddress选项。 |

**示例：**

```
1. export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
2. onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
3. console.info(`onDeviceDiscovered success: ${deviceAddress.bluetoothAddress}`);
4. }
5. }
```
