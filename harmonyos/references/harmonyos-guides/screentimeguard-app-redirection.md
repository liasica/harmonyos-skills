---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-app-redirection
title: 拦截页跳转至管控应用
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 拦截页跳转至管控应用
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:13+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:0222661c454a89570eda0d6f629b607960139054843dd336dfc6dec61ed485f2
---

## 场景介绍

Screen Time Guard Kit支持用户通过被管控应用拦截页跳转至当前管控应用，管理当前的管控策略。从26.0.0版本开始，Screen Time Guard Kit新增支持跳转时want参数携带当前管控策略相关信息。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/TnKh2DuySbShLh6Pi8MFSg/zh-cn_image_0000002820406601.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=05999025EF998BAB194150524054FC29038C5DEFBFCCF78C1EE6C99A84E8DA31)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KhDEKkceQ5ucewv3tr72Sw/zh-cn_image_0000002820526605.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2033AF2EEB05D7FEE7211FB76F65103AE024070880193F3D2DA28F145BB6575)

流程说明：

1. 应用的某一管控规则生效，导致被管控应用不可用时，用户点击被管控应用，健康使用设备会拉起该应用的拦截页面。
2. 用户点击拦截页面下方跳转按钮，健康使用设备查询被管控应用的token和对被管控应用生效的规则，将规则相关信息写入want自定义参数中。
3. 健康使用设备调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口拉起管控应用，传递的want参数携带当前管控规则相关信息。
4. 应用可以在入口Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中接收并解析want参数，获取被管控应用的token、正在生效的管控规则名称等信息。

## 参数说明

want自定义参数如下表所示：

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| token | string | 被管控应用的token。 |
| strategyNames | string[] | 当前对被管控应用生效的策略名称。  若有多个时间守护策略对该应用进行管控，则返回对应的策略名称数组。 |
| isSetAppsRestriction | boolean | 正在生效的规则是否包含[应用访问限制](screentimeguard-set-apps-restriction.md)。  true: 正在生效的规则包含应用访问限制，应用访问限制规则名称不会体现在strategyNames参数中。  false: 正在生效的规则不包含应用访问限制。 |

## 开发前提

拦截页跳转至管控应用并携带管控规则相关信息需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 拦截页跳转至管控应用并携带管控规则相关信息

1. 导入相关模块。

   ```typescript
   import { UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在onCreate和onNewWant回调中接收并解析want参数，获取当前管控规则相关信息。

   ```typescript
   export default class EntryAbility extends UIAbility {

     // 当UIAbility实例创建完成时，系统会触发该回调
     onCreate(want: Want): void {
       hilog.info(0x0000, 'GuardService', 'onCreate');
       let token: string = want.parameters?.['token'] as string;
       if (token !== undefined) {
         hilog.info(0x0000, 'GuardService', `Token: ${token}`);
       }
       let strategyNames: string[] = want.parameters?.['strategyNames'] as string[];
       if (strategyNames !== undefined) {
         hilog.info(0x0000, 'GuardService', `StrategyNames: ${strategyNames}`);
       }
       let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
       if (isSetAppsRestriction !== undefined) {
         hilog.info(0x0000, 'GuardService', `IsSetAppsRestriction: ${isSetAppsRestriction}`);
       }
     }

     // ...

     // 当已经启动的UIAbility实例再次被拉起时，系统会触发该回调
     onNewWant(want: Want): void {
       hilog.info(0x0000, 'GuardService', 'onNewWant');
       let token: string = want.parameters?.['token'] as string;
       if (token !== undefined) {
         hilog.info(0x0000, 'GuardService', `Token: ${token}`);
       }
       let strategyNames: string[] = want.parameters?.['strategyNames'] as string[];
       if (strategyNames !== undefined) {
         hilog.info(0x0000, 'GuardService', `StrategyNames: ${strategyNames}`);
       }
       let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
       if (isSetAppsRestriction !== undefined) {
         hilog.info(0x0000, 'GuardService', `IsSetAppsRestriction: ${isSetAppsRestriction}`);
       }
     }

     // ...
   }
   ```
