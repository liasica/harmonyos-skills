---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-minorsprotection
title: "@hms.core.account.minorsProtection (华为账号未成年人模式)"
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > @hms.core.account.minorsProtection (华为账号未成年人模式)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4469e5807b041f5174f17085d957bce375e4327275cb6489975b8e961eaaf1e7
---

## 模块概述

@hms.core.account.minorsProtection模块提供华为账号未成年人模式能力，用于帮助应用与系统的未成年人模式联动，提供未成年人网络保护。开发者可通过该能力，快速实现自动切换未成年人模式状态，从而简化家长用户的操作步骤，为未成年人提供安全、健康的网络环境。

该模块提供的未成年人模式能力如下：

* [查询是否支持系统未成年人模式](account-api-minorsprotection.md#查询是否支持系统未成年人模式)：查询当前华为账号、系统用户空间是否支持系统未成年人模式。
* [获取系统未成年人模式开启状态和年龄段信息](account-api-minorsprotection.md#获取系统未成年人模式开启状态和年龄段信息)：获取当前系统未成年人模式的开启状态和年龄段信息，用于开启/关闭应用的未成年人模式，并展示适龄内容。
* [开启/关闭系统未成年人模式](account-api-minorsprotection.md#开启关闭系统未成年人模式)：拉起开启/关闭系统未成年人模式的引导页，引导用户开启系统的未成年人模式。
* [验证系统未成年人模式密码能力](account-api-minorsprotection.md#验证系统未成年人模式密码能力)：在系统未成年人模式开启状态下，拉起未成年人模式密码验证页面，用于验证家长身份。在开启过程中，需要家长设置六位数字密码作为系统未成年人模式状态的指令依据。在系统未成年人模式开启时，开发者可按需调用系统家长身份验证接口，以验证家长身份。

### 基本概念

* 未成年人

  本章节中所指未成年人，即中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）未满十八周岁的公民。
* 适龄应用

  适龄应用指在华为应用市场中的应用分级小于或等于未成年使用者的年龄的应用。例如：

  1. 某应用在华为应用市场的年龄分级为年满12周岁（12+），未成年使用者为13周岁，则该应用为适龄应用。
  2. 某应用在华为应用市场的年龄分级为年满18周岁（18+），未成年使用者为7周岁，则该应用为非适龄应用。
* 开启系统未成年人模式后的限制项目

  1. 使用时长限制：针对16周岁及以上不满18周岁的未成年人使用者，默认每日可使用时长2小时，其他年龄的未成年人使用者，默认每日可使用时长为1小时。
  2. 应用安装限制：默认仅允许安装适龄应用。
  3. 应用打开限制：默认仅允许打开已[接入未成年人模式](../harmonyos-guides/account-overview-minorsprotection.md#接入规范)且配置minors\_mode值为"1"的应用（游戏类应用要求额外满足“适龄应用”条件），家长可对应用进行豁免，允许本次使用。
  4. 内容访问限制：接入未成年人模式的应用默认随系统切换至未成年人模式，在应用内展示适龄内容。
  5. 其他系统功能限制：部分系统功能将受限使用，包括部分应用的卸载更新，退出系统华为账号登录，USB调试功能等，更多限制请进入“设置 > 健康使用设备”查看。
* 远程守护

  可在“设置 > 华为账号 > 家人共享 > 远程守护”开启远程守护。开启远程守护后，未成年人的设备上的系统未成年人模式会自动关闭。

### 查询是否支持系统未成年人模式

@hms.core.account.minorsProtection模块提供查询是否支持系统未成年人模式能力。开发者可通过接口[supportMinorsMode](account-api-minorsprotection.md#supportminorsmode)查询。如果当前系统登录的华为账号注册地为中国境外、香港特别行政区、澳门特别行政区或中国台湾，或系统处于隐私空间，则不支持系统未成年人模式。

### 获取系统未成年人模式开启状态和年龄段信息

@hms.core.account.minorsProtection模块提供获取系统未成年人模式开启状态、年龄段信息能力。开发者可通过接口[getMinorsProtectionInfo](account-api-minorsprotection.md#getminorsprotectioninfo)或[getMinorsProtectionInfoSync](account-api-minorsprotection.md#getminorsprotectioninfosync)主动查询系统未成年人模式的开启状态，从而判断是否需要开启应用的未成年人模式。

在系统未成年人模式开启时，开发者可读取当前系统未成年人模式下的未成年人使用者的年龄段，并向未成年人使用者提供符合该年龄段的内容和服务。当前可获取的年龄段划分如下：

* 不满3周岁；
* 3周岁及以上不满8周岁；
* 8周岁及以上不满12周岁；
* 12周岁及以上不满16周岁；
* 16周岁及以上不满18周岁。

### 开启/关闭系统未成年人模式

@hms.core.account.minorsProtection模块提供开启/关闭系统未成年人模式能力。开发者可通过接口[leadToTurnOnMinorsMode](account-api-minorsprotection.md#leadtoturnonminorsmode)/[leadToTurnOffMinorsMode](account-api-minorsprotection.md#leadtoturnoffminorsmode)拉起开启/关闭系统未成年人模式的引导页，引导用户开启/关闭系统的未成年人模式。

### 验证系统未成年人模式密码能力

@hms.core.account.minorsProtection模块提供家长身份验证能力。在用户开启系统未成年人模式过程中，系统会引导家长用户设置六位数字密码作为系统未成年人模式状态的指令依据。在系统未成年人模式开启时，开发者可通过接口[verifyMinorsProtectionCredential](account-api-minorsprotection.md#verifyminorsprotectioncredential)拉起系统未成年人模式密码验证页面，当用户输入正确的六位数字密码后，会返回成功结果从而验证家长身份，用于调整应用使用时长限制、内容偏好等设置。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { minorsProtection } from '@kit.AccountKit';
```

## MinorsProtectionInfo

未成年人模式信息。[getMinorsProtectionInfo](account-api-minorsprotection.md#getminorsprotectioninfo)和[getMinorsProtectionInfoSync](account-api-minorsprotection.md#getminorsprotectioninfosync)方法返回值，包含系统未成年人模式的开启状态以及年龄段信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minorsProtectionMode | boolean | 否 | 否 | 系统未成年人模式开启状态。  true：表示系统未成年人模式为开启状态。  false：表示系统未成年人模式为关闭状态。 |
| ageGroup | [AgeGroup](account-api-minorsprotection.md#agegroup) | 否 | 是 | 年龄段信息。  **说明：**  1. 仅当未成年人模式开启时才返回此字段。  2. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）儿童账号（14周岁以下）开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)或[12,16)。  例如用户登录4周岁儿童账号，则返回年龄段信息为[3,8)；用户登录9周岁儿童账号，则返回年龄段信息为[8,12)。  3. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）非儿童账号开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)、[12,16)或[16,18)。  例如用户创建13周岁临时使用者，则返回年龄段信息为[12,16)；用户创建17周岁临时使用者，则返回年龄段信息为[16,18)。 |

## AgeGroup

年龄段，包含年龄段上、下限。开发者可根据当前年龄段信息，展示适龄内容。年龄段划分范围包括：[0,3)、[3,8)、[8,12)、[12,16)、[16,18)，单位：周岁。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lowerAge | number | 否 | 否 | 年龄段下限，包含下限值。单位：周岁。  **说明：** 该字段取值范围：0、3、8、12或16。 |
| upperAge | number | 否 | 否 | 年龄段上限，不包含上限值。单位：周岁。  **说明：** 该字段取值范围：3、8、12、16或18。 |

## MinorsModeErrorCode

华为账号未成年人模式接口错误码枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| MINORS\_MODE\_NOT\_ENABLED | [1009900002](errorcode-account-kit.md#section1009900002-未成年人模式未开启) | 未成年人模式未开启。 |
| USER\_CANCELED | [1009900003](errorcode-account-kit.md#section1009900003-用户取消操作) | 用户取消操作。 |
| MINORS\_MODE\_ALREADY\_ON | [1009900005](errorcode-account-kit.md#section1009900005-未成年人模式已经开启) | 未成年人模式已经开启。 |
| MINORS\_MODE\_ALREADY\_OFF | [1009900006](errorcode-account-kit.md#section1009900006-未成年人模式已经关闭) | 未成年人模式已经关闭。 |
| UNSUPPORTED\_ACCOUNT | [1009900007](errorcode-account-kit.md#section1009900007-不支持的账号) | 不支持的账号。 |
| SERVICE\_NOT\_AVAILABLE | [1009900011](errorcode-account-kit.md#section1009900011-服务不可用) | 服务不可用。 |

## supportMinorsMode

supportMinorsMode(): boolean

查询是否支持系统未成年人模式方法。开发者可通过该方法判断当前设备环境是否支持系统未成年人模式能力。该方法为同步方法。

不支持的场景：当前系统登录的华为账号注册地为中国境外、香港特别行政区、澳门特别行政区或中国台湾，或系统处于隐私空间。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持系统未成年人模式。  true：支持系统未成年人模式。  false：不支持系统未成年人模式。  **说明：** 当登录海外华为账号、系统处于隐私空间均会返回false，其他场景均为true。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const supportMinorsMode: boolean = minorsProtection.supportMinorsMode();
  hilog.info(0x0000, 'testTag', `Succeeded in getting supportMinorsMode is: ${supportMinorsMode}`);
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
}
```

## getMinorsProtectionInfoSync

getMinorsProtectionInfoSync(): MinorsProtectionInfo

获取系统未成年人模式信息方法，用于获取系统未成年人模式开启状态和年龄段信息。应用可跟随系统未成年人模式开启状态，开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。该方法为同步方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo) | 返回[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)对象。用于获取系统未成年人模式开启状态、年龄段信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 查询是否支持系统未成年人模式
  if (minorsProtection.supportMinorsMode()) {
    const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
      minorsProtection.getMinorsProtectionInfoSync();
    // 获取未成年人模式开启状态
    const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
    // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
    hilog.info(0x0000, 'testTag',
      `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode}`);
    // 未成年人模式已开启，获取年龄段信息
    if (minorsProtectionMode) {
      const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
      if (ageGroup) {
        hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
        hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
        // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
      }
    } else {
      // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
    }
  } else {
    hilog.info(0x0000, 'testTag',
      'The current device environment does not support the youth mode, please check the current device environment.');
  }
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
      errMessage: ${error.message}`);
}
```

## getMinorsProtectionInfo

getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>

获取系统未成年人模式信息方法，用于获取系统未成年人模式开启状态和年龄段信息。应用可跟随系统未成年人模式开启状态，开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)> | Promise对象，返回[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)对象。用于获取系统未成年人模式开启状态、年龄段信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 查询是否支持系统未成年人模式
  if (minorsProtection.supportMinorsMode()) {
    minorsProtection.getMinorsProtectionInfo()
      .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
        // 获取未成年人模式开启状态
        const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
        // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
        hilog.info(0x0000, 'testTag',
          `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode}`);
        // 未成年人模式已开启，获取年龄段信息
        if (minorsProtectionMode) {
          const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
          if (ageGroup) {
            hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
            hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
            // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
          }
        } else {
          // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
        }
      })
      .catch((error: BusinessError<Object>) => {
        dealGetMinorsInfoAllError(error);
      });
  } else {
    hilog.info(0x0000, 'testTag',
      'The current device environment does not support the youth mode, please check the current device environment.');
  }
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
}

function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}`);
}
```

## verifyMinorsProtectionCredential

verifyMinorsProtectionCredential(context: common.Context): Promise<boolean>

验证系统未成年人模式密码方法。当用户开启系统未成年人模式时，系统会引导家长用户设置六位数字密码作为系统未成年人模式状态的指令依据。当用户需要调整应用的未成年人模式相关设置时，开发者可通过该方法拉起系统未成年人模式密码验证页面，验证六位数字密码，密码输入正确验证成功后，会返回true，否则返回false。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示密码验证通过；返回false表示密码验证未通过。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |
| [1009900002](errorcode-account-kit.md#section1009900002-未成年人模式未开启) | The minors mode is not enabled. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 查询是否支持系统未成年人模式
  if (minorsProtection.supportMinorsMode()) {
    // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
    minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
      .then((result: boolean) => {
        hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result}`);
        // 使用结果判断验密是否通过，执行后续流程
      })
      .catch((error: BusinessError<Object>) => {
        dealVerifyAllError(error);
      });
  } else {
    hilog.info(0x0000, 'testTag',
      'The current device environment does not support the youth mode, please check the current device environment.');
  }
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
}

function dealVerifyAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

## leadToTurnOnMinorsMode

leadToTurnOnMinorsMode(context: common.Context): Promise<void>

引导开启系统未成年人模式方法。开发者可调用该方法拉起开启系统未成年人模式引导页面，页面支持用户选择开启或取消，当选择开启后返回无结果的Promise对象，否则返回错误码。系统未成年人模式相关限制可参考[基本概念](account-api-minorsprotection.md#基本概念)。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |
| [1009900003](errorcode-account-kit.md#section1009900003-用户取消操作) | The user canceled the operation. |
| [1009900005](errorcode-account-kit.md#section1009900005-未成年人模式已经开启) | The minors mode is already on. |
| [1009900007](errorcode-account-kit.md#section1009900007-不支持的账号) | Unsupported HUAWEI ID. |
| [1009900011](errorcode-account-kit.md#section1009900011-服务不可用) | Service not available. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 查询是否支持系统未成年人模式
  if (minorsProtection.supportMinorsMode()) {
    // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
    minorsProtection.leadToTurnOnMinorsMode(this.getUIContext().getHostContext())
      .then(() => {
        // 接口调用完成，如需显示弹窗，请在此处处理
      })
      .catch((error: BusinessError<Object>) => {
        dealTurnOnAllError(error);
      });
  } else {
    hilog.info(0x0000, 'testTag',
      'The current device environment does not support the youth mode, please check the current device environment.');
  }
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
}

function dealTurnOnAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOnMinorsMode. Code: ${error.code}, message: ${error.message}`);
}
```

## leadToTurnOffMinorsMode

leadToTurnOffMinorsMode(context: common.Context): Promise<void>

引导关闭系统未成年人模式方法。开发者可调用该方法拉起是否关闭系统未成年人模式引导页面，用户点击关闭后，会验证开启系统未成年人模式时设置的六位数字密码，验证成功后返回无结果的Promise对象，否则返回错误码。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |
| [1009900003](errorcode-account-kit.md#section1009900003-用户取消操作) | The user canceled the operation. |
| [1009900006](errorcode-account-kit.md#section1009900006-未成年人模式已经关闭) | The minors mode is already off. |
| [1009900011](errorcode-account-kit.md#section1009900011-服务不可用) | Service not available. |

**示例：**

```typescript
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 查询是否支持系统未成年人模式
  if (minorsProtection.supportMinorsMode()) {
    // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
    minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
      .then(() => {
        // 接口调用完成，如需显示弹窗，请在此处处理
      })
      .catch((error: BusinessError<Object>) => {
        dealTurnOffAllError(error);
      });
  } else {
    hilog.info(0x0000, 'testTag',
      'The current device environment does not support the youth mode, please check the current device environment.');
  }
} catch (error) {
  hilog.error(0x0000, 'testTag',
    `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
}

function dealTurnOffAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
}
```
