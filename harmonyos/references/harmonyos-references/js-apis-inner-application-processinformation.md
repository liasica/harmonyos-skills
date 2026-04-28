---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation
title: ProcessInformation
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ProcessInformation
category: harmonyos-references
scraped_at: 2026-04-28T07:58:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c70d24ac5fd3b2621c814088d68f1d41f35280ff1d0ce37b3d61897dc45199e8
---

运行进程信息，可以通过appManager的[getRunningProcessInformation](js-apis-app-ability-appmanager.md#appmanagergetrunningprocessinformation)来获取运行进程信息。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appManager } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 否 | 否 | 应用程序的UID。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| processName | string | 否 | 否 | 进程名称。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| bundleNames | Array<string> | 否 | 否 | 进程中所有运行的Bundle名称。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| state10+ | [appManager.ProcessState](js-apis-app-ability-appmanager.md#processstate10) | 否 | 否 | 当前进程运行状态。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| bundleType12+ | [bundleManager.BundleType](js-apis-bundlemanager.md#bundletype) | 否 | 否 | 当前进程运行的包类型。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| appCloneIndex12+ | number | 否 | 是 | 分身应用索引。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. appManager.getRunningProcessInformation((error, data) => {
4. if (error) {
5. console.error(`getRunningProcessInformation fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`getRunningProcessInformation success, data: ${JSON.stringify(data)}`);
8. }
9. });
```
