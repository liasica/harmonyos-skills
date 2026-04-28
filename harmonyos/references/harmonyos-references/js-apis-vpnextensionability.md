---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vpnextensionability
title: @ohos.app.ability.VpnExtensionAbility (三方VPN能力)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.app.ability.VpnExtensionAbility (三方VPN能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cc164378d5c5e31e8f45528413466d9608417b3e380d80580935141daf0e7298
---

VpnExtensionAbility模块提供三方VPN相关能力，提供三方VPN创建、销毁等生命周期回调。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { VpnExtensionAbility } from '@kit.NetworkKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [VpnExtensionContext](js-apis-inner-application-vpnextensioncontext.md) | 否 | 否 | VpnExtension的上下文环境，继承自ExtensionContext。 |

## VpnExtensionAbility.onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

在启动三方VPN进行初始化时回调。

说明

建议配对调用[onDestroy](js-apis-vpnextensionability.md#vpnextensionabilityondestroy)监听三方VPN的销毁，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 指示要启动的信息。 |

**示例：**

```
1. import { VpnExtensionAbility } from '@kit.NetworkKit';
2. import { Want } from '@kit.AbilityKit';

4. class MyVpnExtAbility extends VpnExtensionAbility {
5. onCreate(want: Want) {
6. console.info('MyVpnExtAbility onCreate');
7. }
8. }
```

## VpnExtensionAbility.onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

VpnExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```
1. import { VpnExtensionAbility } from '@kit.NetworkKit';

3. class MyVpnExtAbility extends VpnExtensionAbility {
4. onDestroy() {
5. console.info('MyVpnExtAbility onDestroy');
6. }
7. }
```
