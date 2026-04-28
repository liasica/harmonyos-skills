---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules
title: 组件启动规则（Stage模型）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 组件启动规则（Stage模型）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a53d91bcbaedc1573d4c1da37d9b1b947b2fa291e94aff24d26a97640afc13e1
---

启动组件是指一切启动或连接应用组件的行为：

* 启动[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)、DataShareExtensionAbility，如使用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)、[startAbilityByCall()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)、[openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)等相关接口。
* 连接ServiceExtensionAbility、DataShareExtensionAbility，如使用[connectServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)、createDataShareHelper()等相关接口。

## 组件启动总体规则

为了保证用户具有更好的使用体验，对以下几种易影响用户体验与系统安全的行为做了限制：

* 后台应用任意弹框，如各种广告弹窗，影响用户使用。
* 后台应用相互唤醒，不合理的占用系统资源，导致系统功耗增加或系统卡顿。
* 前台应用任意跳转至其他应用，如随意跳转到其他应用的支付页面，存在安全风险。

鉴于此，制定了一套组件启动规则，主要包括：

* **跨应用启动组件，需校验目标组件是否可以被其他应用调用。**

  若目标组件exported字段配置为true，表示可以被其他应用调用；若目标组件exported字段配置为false，表示不可以被其他应用调用，还需进一步校验ohos.permission.START\_INVISIBLE\_ABILITY权限（该权限仅系统应用可申请）。组件exported字段说明可参考[abilities标签](module-configuration-file.md#abilities标签)。
* **位于后台的UIAbility应用，启动组件需校验BACKGROUND权限ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND（该权限仅系统应用可申请）。**

  说明

  + 前后台应用的判断依据：若应用进程获焦或所属的UIAbility组件位于前台则判定为前台应用，否则为后台应用。
  + 对于2in1和Tablet设备：
    - 从API version 18开始，如果应用已创建在前台显示的悬浮窗，当该应用退至后台时，无需校验BACKGROUND权限也可以拉起其他Ability。
    - 从API version 21开始，如果应用自身已经添加到状态栏，则当应用退至后台时，无需校验BACKGROUND权限也可以拉起自身的UIAbility。
* **跨设备使用startAbilityByCall接口，需校验分布式权限ohos.permission.DISTRIBUTED\_DATASYNC。**

上述组件启动规则自API 9版本开始生效，新增规则生效版本在规则中单独说明。开发者需熟知组件启动规则，避免业务功能异常。启动组件的具体校验流程见下文。

## 同设备组件启动规则

设备内启动组件，不同场景下的规则不同，可分为如下三种场景：

* 启动UIAbility。
* 启动ServiceExtensionAbility、DataShareExtensionAbility。
* 通过[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动UIAbility。

说明

下图中的BACKGROUND权限是指ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND，CALL权限是指ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/9qVoWuTdSDuZGipT9ZnPcg/zh-cn_image_0000002552957498.png?HW-CC-KV=V1&HW-CC-Date=20260427T233744Z&HW-CC-Expire=86400&HW-CC-Sign=06245F9EFC9C6C408A7337A0CEB109B3F66D025DC0A38310A8DC5AE18BDB11CC)

## 分布式跨设备组件启动规则

跨设备启动组件，不同场景下的规则不同，可分为如下三种场景：

* 启动UIAbility。
* 启动ServiceExtensionAbility、DataShareExtensionAbility。
* 通过[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动UIAbility。

说明

下图中的BACKGROUND权限是指ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND，DATASYNC权限是指ohos.permission.DISTRIBUTED\_DATASYNC。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/svKX7YvBToq9ZyNYye7quA/zh-cn_image_0000002583477499.png?HW-CC-KV=V1&HW-CC-Date=20260427T233744Z&HW-CC-Expire=86400&HW-CC-Sign=F647292F52DE0E6D4A8E1F2860F1A3EA19A762CADAFD549161127B80E185BE96)
