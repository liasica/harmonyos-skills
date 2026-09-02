---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-add-permissions
title: 管理用户授权
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > LiteWearable应用开发 > 管理用户授权
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:26+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c93959b051eaa5466cc77fca7f374939bcfa79b874e5a1f08de326a0085b2b65
---

## 场景介绍

从6.1.1(24) 版本开始，支持管理用户授权。

应用拉起华为账号同步和授权界面，由用户授权相应的数据访问权限。用户可以自主选择授权的数据类型，可以只授权部分数据权限。应用所能操作的用户数据，是用户授权和运动健康服务审批通过的数据权限的交集。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [requestAuthorizations](../harmonyos-references/health-api-healthstore-lite.md#healthstorerequestauthorizations)(request: AuthorizationRequest): AuthorizationResponse | 用户授权，入参为授权参数[AuthorizationRequest](../harmonyos-references/health-api-healthstore-lite.md#authorizationrequest)，添加需要读写的数据类型，拉起账号授权页面，引导用户完成授权，返回结果中的数据类型列表，其对应权限在[应用申请权限](health-permission-description.md)和用户授权权限的交集中。 |
| [getAuthorizations](../harmonyos-references/health-api-healthstore-lite.md#healthstoregetauthorizations)(request: AuthorizationRequest): AuthorizationResponse | 查询用户权限，入参为[AuthorizationRequest](../harmonyos-references/health-api-healthstore-lite.md#authorizationrequest)，添加需要查询的数据类型，查询传入类型是否有权限，返回结果中的数据类型列表，其对应权限在[应用申请权限](health-permission-description.md)和用户授权权限的交集中。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)。
* 常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

1. 导入运动健康服务功能模块。

   ```javascript
   import healthStore from '@hms.health.store';
   ```
2. 查询权限。

   ```javascript
   function getAuthorizations() {
     let queryAuthorizationRequest = {
       readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
       writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
       scopes: ['https://www.huawei.com/healthkit/workout']
     }

     try {
       let queryAuthorizationResponse = healthStore.getAuthorizations(queryAuthorizationRequest);
     } catch (err) {
       // 异常场景处理
     }
   }
   ```
3. 发起用户授权请求。

   ```javascript
   function requestAuthorizations() {
     let authorizationParameter = {
       readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
       writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
       scopes: ['https://www.huawei.com/healthkit/workout']
     }
     try {
       let authorizationResponse = healthStore.requestAuthorizations(authorizationParameter);
     } catch (err) {
       // 异常场景处理
     }
   }
   ```
