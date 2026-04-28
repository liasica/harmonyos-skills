---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-ability
title: VoIPExtensionAbility（应用内通话消息扩展Ability）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > VoIPExtensionAbility（应用内通话消息扩展Ability）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91029d8f78eb2582dbf1628809fc1fd32faf84d82aa8f06940f4443617b6c910
---

VoIPExtensionAbility为应用内通话消息扩展Ability，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，增加获取场景化消息数据的回调。有如下约束：

* VoIPExtensionAbility为独立子进程，轻量级。
* 不允许调用卡片API。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { VoIPExtensionAbility } from '@kit.PushKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该属性在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [VoIPExtensionContext](push-voip-context.md#voipextensioncontext) | 否 | 否 | VoIPExtensionAbility的上下文环境，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。 |

## onReceiveMessage

PhonePC/2in1TabletTVWearable

onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void

应用继承VoIPExtensionAbility后接收应用内通话消息的接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| voipInfo | pushCommon.[VoIPInfo](push-pushcommon.md#voipinfo) | 是 | 网络音视频通话消息数据。 |

**示例：**

```
1. import { VoIPExtensionAbility, pushCommon } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class VoipExtAbility extends VoIPExtensionAbility {
5. // voipInfo为场景化消息数据
6. onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void {
7. hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
8. }
9. }
```
