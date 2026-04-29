---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/want-overview
title: Want概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 信息传递载体Want > Want概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:df294b15b3362afc3f07f1842575ec3d754e0f9bebf29e0f19379732e30980af
---

## Want的定义与用途

[Want](../harmonyos-references/js-apis-app-ability-want.md)是一种对象，用于在应用组件之间传递信息。

其中，一种常见的使用场景是作为[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法的参数。例如，当UIAbilityA需要启动UIAbilityB并向UIAbilityB传递一些数据时，可以使用Want作为一个载体，将数据传递给UIAbilityB。

**图1** Want用法示意

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/gkhr4f5LRlKfWt_s7jPtog/zh-cn_image_0000002589243791.png?HW-CC-KV=V1&HW-CC-Date=20260429T052545Z&HW-CC-Expire=86400&HW-CC-Sign=8F54868AC07838C856310519B917A7AE0AC407C75737D0055F6BC322158D4CFB)

## Want的类型

* **显式Want**：在启动目标应用组件时，调用方传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中指定了abilityName和bundleName，称为显式Want。

  显式Want通常用于应用内组件启动，通过在Want对象内指定本应用Bundle名称信息（bundleName）和abilityName来启动应用内目标组件。当有明确处理请求的对象时，显式Want是一种简单有效的启动目标应用组件的方式。

  说明

  从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定[应用链接](app-startup-overview.md#应用链接)的方式来实现。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. // ···

  4. let wantInfo: Want = {
  5. deviceId: '', // deviceId为空表示本设备
  6. bundleName: 'com.samples.wantoverview',
  7. abilityName: 'ExplicitAbility',
  8. };
  ```

  [ExplicitPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/WantOverview/entry/src/main/ets/pages/ExplicitPage.ets#L15-L30)
* **隐式Want**：在启动目标应用组件时，调用方传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中未指定abilityName，称为隐式Want。

  当需要处理的对象不明确时，可以使用隐式Want，在当前应用中使用其他应用提供的某个能力，而不关心提供该能力的具体应用。隐式Want使用[skills标签](module-configuration-file.md#skills标签)来定义需要使用的能力，并由系统匹配声明支持该请求的所有应用来处理请求。例如，需要打开一个链接的请求，系统将匹配所有声明支持该请求的应用，然后让用户选择使用哪个应用打开链接。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. // ···

  4. let wantInfo: Want = {
  5. // uncomment line below if wish to implicitly query only in the specific bundle.
  6. // bundleName: 'com.example.myapplication',
  7. action: 'ohos.want.action.search',
  8. // entities can be omitted
  9. entities: ['entity.system.browsable'],
  10. uri: 'https://www.test.com:8080/query/student',
  11. type: 'text/plain',
  12. };
  ```

  [ImplicitPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/WantOverview/entry/src/main/ets/pages/ImplicitPage.ets#L15-L34)

  说明

  + 根据系统中待匹配应用组件的匹配情况不同，使用隐式Want启动应用组件时会出现以下三种情况。
    - 未匹配到满足条件的应用组件：启动失败。
    - 匹配到一个满足条件的应用组件：直接启动该应用组件。
    - 匹配到多个满足条件的应用组件（[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)）：弹出选择框让用户选择。
