---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-add-permissions
title: 管理用户授权
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 管理用户授权
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4ab00d227cfdc52bc7f85ac02cd1479bfd8882ec4cec68d924e170f158d2914
---

## 场景介绍

应用拉起华为账号登录和授权界面，由用户授权相应的数据访问权限。用户可以自主选择授权的数据类型，可以只授权部分数据权限。

应用所能操作的用户数据，是用户授权和运动健康服务审批通过的数据权限的交集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/pnCL1OX2Qz6zPlFWKCKlhQ/zh-cn_image_0000002589245219.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=D09173431F53A99B57512A710515792F0809E58072378DF561C3FF34E931810A)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [requestAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorerequestauthorizations)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1), request: [AuthorizationRequest](../harmonyos-references/health-api-healthstore.md#authorizationrequest)): Promise<[AuthorizationResponse](../harmonyos-references/health-api-healthstore.md#authorizationresponse)> | 用户授权，入参为UIAbility上下文和授权参数[AuthorizationRequest](../harmonyos-references/health-api-healthstore.md#authorizationrequest)，添加需要读写的数据类型，拉起账号授权页面，引导用户完成授权，返回结果中的数据类型列表，其对应权限在[应用申请权限](health-apply.md)和用户授权权限的交集中。 |
| [getAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstoregetauthorizations)(request: [AuthorizationRequest](../harmonyos-references/health-api-healthstore.md#authorizationrequest)): Promise<[AuthorizationResponse](../harmonyos-references/health-api-healthstore.md#authorizationresponse)> | 查询用户权限，入参为[AuthorizationRequest](../harmonyos-references/health-api-healthstore.md#authorizationrequest)，添加需要查询的数据类型，查询传入类型是否有权限，返回结果中的数据类型列表，其对应权限在[应用申请权限](health-apply.md)和用户授权权限的交集中。 |
| [cancelAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorecancelauthorizations)(): Promise<void> | 取消用户所有授权。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口需在页面或自定义组件生命周期内调用。接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

### 用户授权

1.导入运动健康功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.创建授权请求，确保授权参数中的权限已在申请运动健康服务时勾选，权限说明请参考[权限说明](health-permission-description.md)。

```
1. let authorizationParameter: healthStore.AuthorizationRequest = {
2. readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
3. writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
4. }
```

3.调用[requestAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorerequestauthorizations)方法执行登录授权请求，并处理返回结果。

```
1. try {
2. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
3. let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);
4. hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
5. authorizationResponse.writeDataTypes.forEach(dataType => {
6. hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
7. });
8. authorizationResponse.readDataTypes.forEach(dataType => {
9. hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
10. });
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to request authorization. Code: ${err.code}, message: ${err.message}`);
13. }
```

### 查询权限

1.导入运动健康服务功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.创建查询权限请求。

```
1. let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
2. readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
3. writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
4. }
```

3.调用[getAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstoregetauthorizations)方法执行查询权限请求，并处理返回结果。

```
1. try {
2. let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);
3. hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
4. queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
5. hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
6. });
7. queryAuthorizationResponse.readDataTypes.forEach(dataType => {
8. hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
9. });
10. } catch (err) {
11. hilog.error(0x0000, 'testTag', `Failed to get authorization. Code: ${err.code}, message: ${err.message}`);
12. }
```

### 取消授权

1.导入运动健康服务功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.调用[cancelAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorecancelauthorizations)方法执行取消授权，并处理返回结果。

```
1. try {
2. await healthStore.cancelAuthorizations();
3. hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
4. } catch (err) {
5. hilog.error(0x0000, 'testTag', `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`);
6. }
```
