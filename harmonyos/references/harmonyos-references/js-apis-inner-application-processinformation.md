---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation
title: ProcessInformation
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ProcessInformation
category: harmonyos-references
scraped_at: 2026-09-02T15:00:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:156f8b758dace974c9e83080a784ca01798c4e2695b151ef387549c9a76c8d3f
---

运行进程信息，可以通过appManager的[getRunningProcessInformation](js-apis-app-ability-appmanager.md#appmanagergetrunningprocessinformation)来获取运行进程信息。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { appManager } from '@kit.AbilityKit';
```

## 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 否 | 否 | 应用程序的UID。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| processName | string | 否 | 否 | 进程名称。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| bundleNames | Array<string> | 否 | 否 | 进程中所有运行的Bundle名称。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| state10+ | [appManager.ProcessState](js-apis-app-ability-appmanager.md#processstate10) | 否 | 否 | 当前进程运行状态。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| bundleType12+ | [bundleManager.BundleType](js-apis-bundlemanager.md#bundletype) | 否 | 否 | 当前进程运行的Bundle类型。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| appCloneIndex12+ | number | 否 | 是 | 应用分身索引，用于标识不同的分身应用实例。0表示主应用，正整数表示对应的分身实例索引。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| isPreload | boolean | 否 | 是 | 进程是否为预加载。当进程是预加载且还未被某个组件启动请求所使用时为true；反之为false。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 26.0.0开始，该接口支持在元服务中使用。  **起始版本**：26.0.0 |

**示例：**

```ts
import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((error, data) => {
  if (error) {
    console.error(`getRunningProcessInformation fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`getRunningProcessInformation success, data: ${JSON.stringify(data)}`);
  }
});
```
