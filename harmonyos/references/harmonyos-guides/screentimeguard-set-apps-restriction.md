---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-set-apps-restriction
title: 设置应用访问限制
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用访问限制 > 设置应用访问限制
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:c245fa333cf07fd39c64b61306907ce6de9b78e365c690e8041b4e4a9d52d105
---

## 场景介绍

当管控应用希望限制访问某些特定应用时，可通过调用限制应用访问接口实现。Screen Time Guard Kit会根据传入的应用token以及限制类型，限制用户对指定应用的访问。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/VGy8AKZaS4OYJRAMsHFL8g/zh-cn_image_0000002736434351.png)

流程说明：

1. 应用调用设置应用访问限制的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的限制类型以及token，对应用做限制处理，返回处理结果。

## 接口说明

限制应用访问的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [setAppsRestriction](../harmonyos-references/screentimeguard-guardservice.md#setappsrestriction)(appInfo: [AppInfo](../harmonyos-references/screentimeguard-guardservice.md#appinfo), restrictionType: [RestrictionType](../harmonyos-references/screentimeguard-guardservice.md#restrictiontype)): Promise<void> | 可根据传入的应用token数组，以及限制类型（禁用/许可清单），来决定是对应用数组做限制，还是对应用数组之外的应用做限制 |

**说明** 

**定义释义：**

* 限制类型为禁用清单时，对应用数组中的应用做限制。
* 限制类型为许可清单时，对应用数组以外的应用做限制。

**边界场景：**

* 如果传入的应用数组为空，限制类型为禁用清单，则不对任何应用做限制。该场景相当于没有开启有效管控。
* 如果传入的应用数组为空，限制类型为许可清单，则对系统内置许可清单应用（电话、联系人、设置、未成年人模式）、管控发起应用本身、已授权的管控应用之外的所有应用做限制。
* 对同一个管控应用，如果反复调用该接口做限制（不管是许可清单还是禁用清单），均以最新的一次的限制来生效。
* 传入的应用数组中如果包含无效token，则为参数错误。

## 开发前提

设置应用访问限制需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用setAppsRestriction，设置应用访问限制。

   ```typescript
   private async restrictApps(appInfo: guardService.AppInfo): Promise<void> {
     try {
       await guardService.setAppsRestriction(appInfo, guardService.RestrictionType.BLOCKLIST_TYPE);
       // ...
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `setAppsRestriction fail, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
