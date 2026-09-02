---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy
title: "@ohos.net.policy (网络策略管理)"
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.policy (网络策略管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:13439f6e28506c5b9f357b860ab32db7c4e4136365cd7210bf52b5be91932542
---

本模块提供网络策略管理能力，采用防火墙技术对用户使用数据流量进行控制管理。

**说明** 

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { policy } from '@kit.NetworkKit';
```

## NetBearType

type NetBearType = connection.NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.NetBearType](js-apis-net-connection.md#netbeartype) | 网络类型。 |

## policy.showAppNetPolicySettings22+

showAppNetPolicySettings(context: Context): Promise<void>

当需要设置当前应用能否使用Wi-Fi/蜂窝联网时，调用该接口可以打开当前应用的联网设置界面，以设置应用的联网权限。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异**：该接口在Phone和Tablet设备中可正常调用，在其他设备调用不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | Stage模型的应用上下文（仅支持UIAbilityContext和ExtensionContext）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

**说明** 

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```ts
import { policy } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
policy.showAppNetPolicySettings(context).then(() => {
    console.info("showAppNetPolicySettings success");
}).catch(() => {
    console.error("showAppNetPolicySettings failed");
    }
)
```

## policy.getNetAccessPolicy

getNetAccessPolicy(): Promise<NetAccessPolicy>

查询自身应用的联网策略（是否允许使用蜂窝、Wi-Fi网络上网），可在设备中“设置 > 移动网络 > 流量管理 > 应用联网”中查看。使用Promise异步回调。

**起始版本：** 26.0.0

**系统能力**：SystemCapability.Communication.NetManager.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAccessPolicy](js-apis-net-policy.md#netaccesspolicy)> | Promise对象。返回应用自身联网策略。 |

**错误码：**

以下错误码的详细介绍参见[策略管理错误码](errorcode-net-policy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error, such as nullptr. |

**示例：**

```ts
import { policy } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

policy.getNetAccessPolicy().then((policyInfo: policy.NetAccessPolicy) => {
  console.info(`getNetAccessPolicy success. WiFi: ${policyInfo.allowWiFi}, Cellular: ${policyInfo.allowCellular}`);
}).catch((err: BusinessError) => {
  console.error(`getNetAccessPolicy fail. error info: ${err.code} - ${err.message}`);
});
```

## NetAccessPolicy

应用联网策略信息。

**起始版本：** 26.0.0

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| allowWiFi | boolean | 否 | 否 | 是否允许使用Wi-Fi网络上网。  true：允许使用Wi-Fi网络上网。  false： 不允许使用Wi-Fi网络上网。 |
| allowCellular | boolean | 否 | 否 | 是否允许使用蜂窝网络上网。  true：允许使用蜂窝网络上网。  false： 不允许使用蜂窝网络上网。 |
