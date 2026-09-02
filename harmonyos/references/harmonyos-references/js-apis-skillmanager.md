---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-skillmanager
title: "@ohos.bundle.skillManager (skillManager模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.skillManager (skillManager模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fb5f89b013fb7e7423acea06a97897868bc36a7eca13a57c1bcdd36ba6e8f5f4
---

本模块提供技能（Skill）信息的查询能力，支持查询应用自身的技能信息、指定应用的技能信息以及所有应用的技能信息。AI代理框架在规划任务时，可通过本模块查询设备上所有应用可用的技能，选择合适的技能来完成用户请求。通过技能信息查询，可以实现智能任务调度、能力匹配优化，提升AI代理的任务执行效率，降低开发者的技能集成复杂度。

**起始版本：** 26.0.0

## 导入模块

```ts
import { skillManager } from '@kit.AbilityKit';
```

## SkillInfoFlag

技能信息标志，指示需要获取的技能信息的内容。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET\_SKILL\_INFO\_DEFAULT | 0x00000000 | 获取默认技能信息，不包含description、srcEntries、permissions和requestPermissions。 |
| GET\_SKILL\_INFO\_WITH\_DESCRIPTION | 0x00000001 | 用于获取包含description的技能信息。 |
| GET\_SKILL\_INFO\_WITH\_SRC\_ENTRIES | 0x00000002 | 用于获取包含srcEntries的技能信息。 |
| GET\_SKILL\_INFO\_WITH\_PERMISSIONS | 0x00000004 | 用于获取包含permissions的技能信息。 |
| GET\_SKILL\_INFO\_WITH\_REQUEST\_PERMISSIONS | 0x00000008 | 用于获取包含requestPermissions的技能信息。 |

## skillManager.getSkillInfoForSelf

getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>

获取本应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定查询技能所属模块的名称。 |
| skillName | string | 是 | 指定查询技能的名称。 |
| flags | number | 是 | 指定返回的SkillInfo所包含的信息。详情请参考[SkillInfoFlag](js-apis-skillmanager.md#skillinfoflag)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkillInfo](js-apis-bundlemanager-skillinfo.md)> | Promise对象，返回指定技能的SkillInfo。 |

**错误码：**

以下错误码的详细介绍请参见[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17700002 | The specified module is not found. |
| 17700093 | The specified skillName is not found. |

**示例：**

```ts
import { skillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = "entry";
let skillName = "mySkill";
let flags = skillManager.SkillInfoFlag.GET_SKILL_INFO_DEFAULT;
try {
  skillManager.getSkillInfoForSelf(moduleName, skillName, flags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getSkillInfoForSelf succeed: Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getSkillInfoForSelf failed: %{public}d  %{public}s', err.code, err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSkillInfoForSelf failed: error %{public}d  %{public}s', code, message);
}
```

## skillManager.getSkillInfosForSelf

getSkillInfosForSelf(flags: number): Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>>

获取本应用的所有技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flags | number | 是 | 指定返回的SkillInfo所包含的信息。详情请参考[SkillInfoFlag](js-apis-skillmanager.md#skillinfoflag)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>> | Promise对象，返回调用方所在应用的所有技能信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17700101 | Bundle manager service is exception. Possible causes: 1. Failed to connect to the system service. 2. IPC data transmission failed. 3. Failed to obtain the object constructor. |

**示例：**

```ts
import { skillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flags = skillManager.SkillInfoFlag.GET_SKILL_INFO_DEFAULT;
try {
  skillManager.getSkillInfosForSelf(flags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getSkillInfosForSelf succeed: Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getSkillInfosForSelf failed: %{public}d  %{public}s', err.code, err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSkillInfosForSelf failed: error %{public}d  %{public}s', code, message);
}
```

## skillManager.getSkillInfo

getSkillInfo(bundleName: string, moduleName: string, skillName: string, flags: number, userId?: number): Promise<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>

获取指定应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE\_SKILL\_PRIVILEGE 或 ohos.permission.MANAGE\_SKILL

**说明** 

跨用户查询时还需要 ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 指定查询应用的包名。 |
| moduleName | string | 是 | 指定查询技能所属模块的名称。 |
| skillName | string | 是 | 指定查询技能的名称。 |
| flags | number | 是 | 指定返回的SkillInfo所包含的信息。详情请参考[SkillInfoFlag](js-apis-skillmanager.md#skillinfoflag)。 |
| userId | number | 否 | 指定查询的用户ID，可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)获取。  默认值：调用方所在用户。  取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkillInfo](js-apis-bundlemanager-skillinfo.md)> | Promise对象，返回指定技能的SkillInfo。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 17700001 | The specified bundleName is not found. |
| 17700002 | The specified module is not found. |
| 17700004 | The specified user ID is not found. |
| 17700093 | The specified skillName is not found. |

**示例：**

```ts
import { skillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let moduleName = "entry";
let skillName = "mySkill";
let flags = skillManager.SkillInfoFlag.GET_SKILL_INFO_DEFAULT;
try {
  skillManager.getSkillInfo(bundleName, moduleName, skillName, flags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getSkillInfo succeed: Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getSkillInfo failed: %{public}d  %{public}s', err.code, err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSkillInfo failed: error %{public}d  %{public}s', code, message);
}
```

## skillManager.getSkillInfos

getSkillInfos(bundleName: string, flags: number, userId?: number): Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>>

获取指定应用的所有技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE\_SKILL\_PRIVILEGE 或 ohos.permission.MANAGE\_SKILL

**说明** 

跨用户查询时还需要 ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 指定查询应用的包名。 |
| flags | number | 是 | 指定返回的SkillInfo所包含的信息。详情请参考[SkillInfoFlag](js-apis-skillmanager.md#skillinfoflag)。 |
| userId | number | 否 | 指定查询的用户ID，可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)获取。  默认值：调用方所在用户。  取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>> | Promise对象，返回指定应用的所有技能信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |

**示例：**

```ts
import { skillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let flags = skillManager.SkillInfoFlag.GET_SKILL_INFO_DEFAULT;
try {
  skillManager.getSkillInfos(bundleName, flags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getSkillInfos succeed: Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getSkillInfos failed: %{public}d  %{public}s', err.code, err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSkillInfos failed: error %{public}d  %{public}s', code, message);
}
```

## skillManager.getAllSkillInfos

getAllSkillInfos(flags: number, userId?: number): Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>>

获取设备上安装应用的所有技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE\_SKILL\_PRIVILEGE 或 ohos.permission.MANAGE\_SKILL

**说明** 

跨用户查询时还需要 ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flags | number | 是 | 指定返回的SkillInfo所包含的信息。详情请参考[SkillInfoFlag](js-apis-skillmanager.md#skillinfoflag)。 |
| userId | number | 否 | 指定查询的用户ID，可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)获取。  默认值：调用方所在用户。  取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[SkillInfo](js-apis-bundlemanager-skillinfo.md)>> | Promise对象，返回所有应用的技能信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 17700004 | The specified user ID is not found. |

**示例：**

```ts
import { skillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flags = skillManager.SkillInfoFlag.GET_SKILL_INFO_DEFAULT;
try {
  skillManager.getAllSkillInfos(flags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getAllSkillInfos succeed: Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAllSkillInfos failed: %{public}d  %{public}s', err.code, err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllSkillInfos failed: error %{public}d  %{public}s', code, message);
}
```

## SkillInfo

type SkillInfo = \_SkillInfo

技能配置信息，用于定义AI代理的技能能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_SkillInfo](js-apis-bundlemanager-skillinfo.md#skillinfo-1) | 应用技能信息。 |

## SkillType

type SkillType = \_SkillType

技能类型的枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 类型 | 说明 |
| --- | --- |
| [\_SkillType](js-apis-bundlemanager-skillinfo.md#skilltype) | 技能类型的枚举。 |
