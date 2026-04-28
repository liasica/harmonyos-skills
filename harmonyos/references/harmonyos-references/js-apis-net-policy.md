---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy
title: @ohos.net.policy (网络策略管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.policy (网络策略管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:91d9d7d134d73e8eef51af8de06396fa802bff3b16a4e6696cbcd6fb23c777f0
---

本模块提供网络策略管理能力，采用防火墙技术对用户使用数据流量进行控制管理。

说明

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { policy } from '@kit.NetworkKit';
```

## NetBearType

PhonePC/2in1TabletTVWearable

type NetBearType = connection.NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.NetBearType](js-apis-net-connection.md#netbeartype) | 网络类型。 |

## policy.showAppNetPolicySettings22+

PhonePC/2in1TabletTVWearable

showAppNetPolicySettings(context: Context): Promise<void>

当需要设置当前应用能否使用Wi-Fi/蜂窝联网时，调用该接口可以打开当前应用的联网设置界面，以设置应用的联网权限。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异**：该接口在Phone、2in1、Tablet设备中可正常调用，在其他设备调用不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | Stage模型的应用上下文（仅支持UIAbilityContext和ExtensionContext）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { policy } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. policy.showAppNetPolicySettings(context).then(() => {
6. console.info("showAppNetPolicySettings success");
7. }).catch(() => {
8. console.error("showAppNetPolicySettings failed");
9. }
10. )
```
