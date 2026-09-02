---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice
title: "@hms.utilityApplication.screenTimeGuard.guardService（屏幕时间守护服务）"
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > @hms.utilityApplication.screenTimeGuard.guardService（屏幕时间守护服务）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d6f39cdc8120c6532c1f87dd3f3ac4df38b0e4e05c947a7466ac27cdc0a9990c
---

## 模块概述

守护服务模块是Screen Time Guard Kit的核心模块，提供了用户授权管理和应用访问管理的功能。开发者可以通过接入本Kit实现管控应用，以此管理其它应用（被管控应用）的使用时长。

通过该模块，开发者可以：

* 用户授权管理：请求授权、撤销授权和查询授权状态。
* 守护策略管理：创建、更新、查询、删除和启动/停止守护策略，通过策略在特定时间范围内对指定被管控应用实施管控，如一天中只能在某个时间段内使用、只能使用多少时长等。
* 直接应用限制：立即限制被管控应用的使用，直至管控应用主动取消限制，适用于需要立即生效的简单限制场景。

### 用户授权管理

用户授权管理能力指用户为管控应用授予权限的相关功能。应用授权是使用本Kit所有功能的前提条件，出于隐私保护考虑，管控应用必须先获得用户的明确授权，才能使用本Kit提供的管控能力。

开发者可以使用[requestUserAuth](screentimeguard-guardservice.md#requestuserauth)请求用户授予权限，并使用[getUserAuthStatus](screentimeguard-guardservice.md#getuserauthstatus)查询当前的授权状态。若不再需要权限，管控应用可主动调用[revokeUserAuth](screentimeguard-guardservice.md#revokeuserauth)以取消授权。

```typescript
// 以下为调用逻辑的伪代码
guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext); // 请求用户授权
guardService.getUserAuthStatus(); // 查询授权状态
... // 若授权成功，可以调用Screen Time Guard Kit相关接口
guardService.revokeUserAuth(); // 取消授权
... // 取消授权后，无法调用Screen Time Guard Kit相关接口
```

### 应用访问管理

应用访问管理能力指限制用户访问指定应用的相关功能，用户将无法打开被限制访问的应用。当前支持通过策略和直接两种方式来实现访问限制:

* 策略方式

  策略方式通过策略来限制对应用的访问，使用策略来表示在何时对哪些应用的访问进行限制。守护策略[GuardStrategy](screentimeguard-guardservice.md#guardstrategy)是相关接口的核心参数，代表了一个具体策略对象，由策略名称、时间策略、应用信息和限制类型组成：

  + [TimeStrategy](screentimeguard-guardservice.md#timestrategy)：时间策略，代表了应用可用时长的不同形式，由时间策略类型和不同类型对应的时间参数组成，目前支持三种时间策略类型，以支持不同的管控场景：
    - 起止时间策略：通过设定开始时间和结束时间，可设定多个应用在该时间段内被限制访问，适用于固定时间段控制的场景。
    - 总时长策略：通过设定一个时间长度，可限定多个应用在该时间长度内被限制访问，适用于使用时长限制的场景。
    - 共享时长策略：通过设定一个时间额度，可限定多个应用共同消耗该时间额度，若时间额度消耗完毕，则以上应用被限制访问，适用于多个应用共享时间额度的场景。
  + [AppInfo](screentimeguard-guardservice.md#appinfo)：应用信息，由一组应用对应的标识符（token）组成。token用于在接口调用中作为被管控应用的唯一标识符，以区分不同的被管控应用。token中不包含应用自身信息如包名、应用名等，保障用户数据隐私安全。具体token值可以使用应用选择模块中的[startAppPicker](screentimeguard-app-picker.md#startapppicker)接口获取。
  + [RestrictionType](screentimeguard-guardservice.md#restrictiontype): 限制类型，用于选择被管控应用的范围，开发者可以指定策略生效对象是AppInfo对应的应用还是除AppInfo以外的应用。

  要实现策略管控，开发者需要实例化一个守护策略对象，以下代码片段说明如何配置守护策略以实现时长管控功能。

  ```typescript
  // 以下为调用逻辑的伪代码
  guardService.addGuardStrategy(guardStrategy); // 添加守护策略，该策略可以被启动
  guardService.startGuardStrategy(guardStrategy.name); // 启动守护策略
  guardService.stopGuardStrategy(guardStrategy.name);  // 停止守护策略
  guardService.removeGuardStrategy(guardStrategy.name); // 删除守护策略，该策略已无法再被启动
  ```
* 直接方式

  直接方式则直接对指定应用进行访问限制。管控应用调用[setAppsRestriction](screentimeguard-guardservice.md#setappsrestriction)接口后立即开始限制指定应用的访问，直至调用[releaseAppsRestriction](screentimeguard-guardservice.md#releaseappsrestriction)接口后取消访问限制。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';
```

## GuardServiceErrorCode

该枚举值定义了Screen Time Guard Kit的所有特殊错误码。相较于通用错误码，该特殊错误码只有在调用本Kit的接口时才会返回。开发者可根据该枚举值来处理遇到的不同错误。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | [1019000001](errorcode-screentimeguard.md#section1019000001-内部错误) | 内部错误。 |
| USER\_NOT\_AUTHORIZED | [1019000002](errorcode-screentimeguard.md#section1019000002-用户未授权) | 用户未授权。 |
| USER\_CANCELED | [1019000003](errorcode-screentimeguard.md#section1019000003-用户取消) | 用户取消。 |
| STRATEGIES\_EXCEED\_LIMIT | [1019000004](errorcode-screentimeguard.md#section1019000004-策略数量超限) | 策略数量超限。 |
| STRATEGY\_NAME\_ALREADY\_EXIST | [1019000005](errorcode-screentimeguard.md#section1019000005-策略名称重复) | 策略名称重复。 |
| NONEXISTENT\_STRATEGY | [1019000006](errorcode-screentimeguard.md#section1019000006-策略不存在) | 策略不存在。 |
| STRATEGY\_ALREADY\_EXECUTED | [1019000007](errorcode-screentimeguard.md#section1019000007-策略重复执行) | 策略重复执行。 |
| STRATEGY\_NOT\_STARTED | [1019000008](errorcode-screentimeguard.md#section1019000008-策略未执行) | 策略未执行。 |
| INVALID\_PARAM | [1019000009](errorcode-screentimeguard.md#section1019000009-参数检查失败) | 无效参数。  **起始版本：** 6.0.2(22) |
| SYSCAP\_UNSUPPORTED\_DEVICE | [1019000010](errorcode-screentimeguard.md#section1019000010-该设备不支持此api) | 该设备不支持此API。  **起始版本：** 6.1.1(24) |
| SYSCAP\_UNSUPPORTED\_STRATEGY\_TYPE | [1019000011](errorcode-screentimeguard.md#section1019000011-策略类型不支持) | 策略类型不支持。  **起始版本：** 26.0.0 |

## requestUserAuth

requestUserAuth(context: common.UIAbilityContext): Promise<void>

请求用户授权，用户授权后管控应用能够获取访问Screen Time Guard Kit所有接口的权限。调用此接口后，系统会拉起授权半模态页面，用户可以在页面中选择是否授予管控应用权限。通过此接口获取用户授权后，管控应用在管控生效过程中不允许被卸载，若需要卸载，可以调用带有[appConfig](screentimeguard-guardservice.md#appconfig)参数的[requestUserAuth](screentimeguard-guardservice.md#requestuserauth-1)接口。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)的上下文环境。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function requestUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { guardService } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('TestRequestUserAuth')
        .onClick(() => {
            // 获取UIAbilityContext上下文
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            guardService.requestUserAuth(context)
               .then(() => {
                  console.info('requestUserAuth invoke success');
               });
        })
    }
  }
}
```

## requestUserAuth

requestUserAuth(context: common.UIAbilityContext, appConfig: AppConfig): Promise<void>

请求用户授权，同时配置管控应用在管控生效过程中是否可以被卸载，用户授权后管控应用能够获取访问Screen Time Guard Kit的所有接口的权限。调用此接口后，系统会拉起授权半模态页面，用户可以在页面中选择是否授予管控应用权限。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)的上下文环境。 |
| appConfig | [AppConfig](screentimeguard-guardservice.md#appconfig) | 是 | 应用配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000009 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1019000010 | Capability is not supported on current device. function requestUserAuth can not work correctly due to limited device capabilities. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { guardService } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('TestRequestUserAuthWithAppConfig')
         .onClick(() => {
            // 配置应用是否支持卸载的参数
            const appConfig:guardService.AppConfig = {
               isSupportAppUninstall: true // 设置是否允许在管控生效期间卸载应用
            };
            // 获取UIAbilityContext上下文
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            guardService.requestUserAuth(context, appConfig)
               .then(() => {
                  console.info('requestUserAuth invoke success');
               });
         })
    }
  }
}
```

## AppConfig

应用配置信息，用于在调用[requestUserAuth](screentimeguard-guardservice.md#requestuserauth-1)时配置管控应用是否可以在管控生效过程中被卸载。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.1.1(24)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| isSupportAppUninstall | boolean | 否 | 否 | 是否支持应用可卸载。  true: 在管控生效期间支持卸载管控应用。  false: 在管控生效期间禁止卸载管控应用。  说明：  1. 卸载管控应用后，该应用设置的管控规则立即失效。  2. 卸载后重新安装应用需要重新申请授权，否则无法调用管控相关接口。 |

## revokeUserAuth

revokeUserAuth(): Promise<void>

撤销用户授权，取消管控应用访问Screen Time Guard Kit所有接口的权限。调用此接口后，管控应用将无法使用本Kit提供的能力，直到再次获得用户授权。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function revokeUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testRevokeUserAuth() {
   guardService.revokeUserAuth()
      .then(() => {
         console.info('revokeUserAuth invoke success.');
      });
}
```

## getUserAuthStatus

getUserAuthStatus(): Promise<AuthStatus>

获取当前用户对管控应用的授权状态。通过此接口，管控应用可以了解是否已获得用户授权，从而决定是否可以调用其他接口。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthStatus](screentimeguard-guardservice.md#authstatus)> | Promise对象，返回用户授权状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function getUserAuthStatus can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testGetUserAuthStatus() {
   guardService.getUserAuthStatus()
      .then((status) => {
         const statusToMsg = ['AUTH_INIT', 'AUTH_GRANTED', 'AUTH_DENIED'];
         console.info('getUserAuthStatus invoke success. ' + statusToMsg[status + 1]);
      });
}
```

## AuthStatus

用户授权状态类型的枚举值，调用[getUserAuthStatus](screentimeguard-guardservice.md#getuserauthstatus)接口后返回，可以用于区分管控应用是否已请求用户授权、请求用户授权后被拒绝、请求用户授权后同意三种状态。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH\_INIT | -1 | 初始状态 |
| AUTH\_GRANTED | 0 | 用户已授权 |
| AUTH\_DENIED | 1 | 用户已拒绝 |

## AppInfo

应用信息，用于表示具体的应用，需与[RestrictionType](screentimeguard-guardservice.md#restrictiontype)组合使用以指定被管控应用。该参数由appTokens组成，appTokens是由不同应用对应token组成的数组。token由随机字符串构成，用于在接口调用中作为被管控应用的唯一标识符，不包含包名、应用名等隐私信息，保障用户数据隐私安全。appTokens可通过[startAppPicker](screentimeguard-app-picker.md#startapppicker)接口获取。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| appTokens | string[] | 否 | 否 | 应用token数组。  数组数量上限：100。  **说明**：  1. appTokens数组中存在错误的token，若只是部分错误，则取其中正常的token做显示和应用。  2. 该数组可以为空数组，即用户不设置任何应用在禁止/许可清单中，是正常场景。 |

## addGuardStrategy

addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>

添加守护策略。通过此接口，系统可以接收策略配置信息，但策略创建后默认处于未启动状态，需调用[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)接口启动，若需要在指定时间启动策略，可以调用带有startDate参数的[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy-1)接口。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| guardStrategy | [GuardStrategy](screentimeguard-guardservice.md#guardstrategy) | 是 | 守护策略。  **说明**：  添加守护策略时策略数量的上限为50条。若超过50条，接口将抛出1019000004错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function addGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000004 | The number of strategies exceeds the upper limit. |
| 1019000005 | The strategy name is already existed. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testAddGuardStrategy() {
   // 定义起止时间策略，应用于周一至周三的08:00至19:00时间段
   const time: guardService.TimeStrategy = {
      type: guardService.TimeStrategyType.START_END_TIME_TYPE,
      startTime: '08:00',
      endTime: '19:00',
      repeat: [1, 2, 3]
   };
   const info: guardService.AppInfo = {
      appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token并填充，本次初始化为空数组，表示未指定任何应用
   };
   const strategy: guardService.GuardStrategy = {
      name: 'TestStrategy',
      timeStrategy: time,
      appInfo: info,
      appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE // 使用禁止清单类型，表示限制appInfo内的应用访问
   };
   guardService.addGuardStrategy(strategy)
      .then(() => {
         console.info('addGuardStrategy invoke success.');
      });
}
```

## GuardStrategy

守护策略，表示在何时对哪些应用的访问进行限制。在指定的时间内，指定的被管控应用将被限制访问，即无法被用户打开。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |
| timeStrategy | [TimeStrategy](screentimeguard-guardservice.md#timestrategy) | 否 | 否 | 时间策略。 |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 否 | 否 | 应用信息。 |
| appRestrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 否 | 否 | 限制类型。 |

## TimeStrategy

时间策略，表示守护策略应该在何时生效，精度为min。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | [TimeStrategyType](screentimeguard-guardservice.md#timestrategytype) | 否 | 否 | 时间策略类型。 |
| startTime | string | 否 | 是 | 起始时间，需采用"HH:mm"格式，有效范围为"00:00"至"23:59"。格式错误或超出范围将返回401错误码。  **说明**：  若TimeStrategyType为START\_END\_TIME\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。 |
| endTime | string | 否 | 是 | 结束时间，需采用"HH:mm"格式，有效范围为"00:00"至"23:59"。格式错误或超出范围将返回401错误码。  **说明**：  1. 若TimeStrategyType为START\_END\_TIME\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。  2. 若结束时间小于起始时间，则代表的是次日。  3. 起始时间和结束时间不能相同。 |
| totalDuration | number | 否 | 是 | 总时长，单位为min。参数范围：0-1440。  **说明**：  若TimeStrategyType为TOTAL\_DURATION\_TYPE或INCLUSIVE\_DURATION\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。 |
| repeat | number[] | 否 | 是 | 重复执行时间，支持填写1~7，代表周一到周日。如果传入的是空数组则表示只执行一次。  默认值：[]。  **说明**：  TimeStrategyType为START\_END\_TIME\_TYPE和INCLUSIVE\_DURATION\_TYPE时此参数才生效。 |

## TimeStrategyType

时间策略类型的枚举，表示时间策略生效时间的形式，当前分别支持以起止时间、时间长度和时间额度的形式生效。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START\_END\_TIME\_TYPE | 1 | 起始时间策略类型，表示策略在配置的起始时间和结束时间内生效。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime必填，totalDuration非必填。 |
| TOTAL\_DURATION\_TYPE | 2 | 总时长策略类型，表示策略生效的总时长，从调用[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)接口成功后开始计时。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime非必填，totalDuration必填。 |
| INCLUSIVE\_DURATION\_TYPE | 3 | 共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额，超额后所有应用均受时长限制，从调用[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)接口成功后开始计时。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime非必填，totalDuration必填，RestrictionType只支持TRUSTLIST\_TYPE。  **起始版本：** 6.0.2(22) |

## RestrictionType

限制类型的枚举值，包含许可清单和禁止清单，与[AppInfo](screentimeguard-guardservice.md#appinfo)组合以指定被管控应用：若为许可清单类型，表示AppInfo以外的应用为被管控应用；若为禁止清单类型，表示AppInfo对应的应用为被管控应用。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRUSTLIST\_TYPE | 1 | 许可清单类型。 |
| BLOCKLIST\_TYPE | 2 | 禁止清单类型。 |

## updateGuardStrategy

updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>

更新已存在的守护策略。更新策略立即生效，如果策略已被启动，管控效果会立即刷新。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 待更新的时间守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |
| guardStrategy | [GuardStrategy](screentimeguard-guardservice.md#guardstrategy) | 是 | 新的时间守护策略。  **说明**：  如想修改策略名称，可以在guardStrategy的name属性中传入新名称。但不能是已存在的名称，如果名称已存在则返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function updateGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testUpdateGuardService() {
   // 定义起止时间策略，应用于周一至周三的08:00至19:00时间段
   const time: guardService.TimeStrategy = {
      type: guardService.TimeStrategyType.START_END_TIME_TYPE,
      startTime: '08:00',
      endTime: '19:00',
      repeat: [1, 2, 3, 4, 5]
   };
   const info: guardService.AppInfo = {
      appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token并填充，本次初始化为空数组，表示未指定任何应用
   };
   const strategy: guardService.GuardStrategy = {
      name: 'TestStrategyChanged',
      timeStrategy: time,
      appInfo: info,
      appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE // 使用禁止清单类型，表示限制appInfo内的应用访问
   };
   // TestStrategy策略需提前通过addGuardStrategy接口添加
   guardService.updateGuardStrategy('TestStrategy', strategy)
      .then(() => {
         console.info('updateGuardStrategy invoke success.');
      });
}
```

## queryGuardStrategies

queryGuardStrategies(): Promise<GuardStrategy[]>

查询当前管控应用添加的所有守护策略。返回策略数组，包含每个策略的完整信息，如策略名称、时间策略、应用信息和限制类型。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GuardStrategy[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice#guardstrategy)> | Promise对象，返回该应用下所有守护策略的数组。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function queryGuardStrategies can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testQueryGuardService() {
   guardService.queryGuardStrategies()
      .then((guardStrategy: guardService.GuardStrategy[]) => {
         console.info('queryGuardStrategies invoke success, GuardStrategies: ' + guardStrategy);
      });
}
```

## removeGuardStrategy

removeGuardStrategy(strategyName: string): Promise<void>

移除指定的守护策略。策略移除后，该策略将无法再被启动，如果策略正在执行中，会先自动停止策略再移除。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function removeGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testRemoveGuardService() {
   guardService.removeGuardStrategy('TestStrategy')
      .then(() => {
         console.info('removeGuardStrategy invoke success');
      });
}
```

## startGuardStrategy

startGuardStrategy(strategyName: string): Promise<void>

启动指定的守护策略，需先调用[addGuardStrategy](screentimeguard-guardservice.md#addguardstrategy)接口添加策略后才可启动。策略启动后，系统会根据策略定义的规则设置指定应用的访问限制。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function startGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000007 | The strategy is already being executed. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testStartGuardStrategy() {
   guardService.startGuardStrategy('TestStrategy')
      .then(() => {
         console.info('startGuardStrategy invoke success');
      });
}
```

## startGuardStrategy

startGuardStrategy(strategyName: string, startDate: Date): Promise<void>

在指定时间启动指定的守护策略。指定的时间如果早于或等于调用接口的时间，策略立即启动；如果晚于调用接口的时间，策略直到指定的时间才会启动。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |
| startDate | Date | 是 | 策略启动时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000007 | The strategy is already being executed. |
| 1019000009 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1019000010 | Capability is not supported on current device. function startGuardStrategy can not work correctly due to limited device capabilities. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testStartStrategyAtSpecificTime() {
   const now = new Date();
   const startDate = new Date(now.getTime() + 5 * 60 * 1000);
   // 五分钟后启动策略TestStrategy
   guardService.startGuardStrategy('TestStrategy', startDate)
      .then(() => {
         console.info('startGuardStrategy invoke success');
      });
}
```

## stopGuardStrategy

stopGuardStrategy(strategyName: string): Promise<void>

停止指定的守护策略。策略停止后，访问限制效果立即解除，但策略仍然保留在系统中，可以再次启动。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function stopGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000008 | This strategy has not been started yet. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testStopGuardService() {
   guardService.stopGuardStrategy('TestStrategy')
      .then(() => {
         console.info('stopGuardStrategy invoke success');
      });
}
```

## setAppsRestriction

setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

设置指定应用的访问限制。与策略管控不同，此接口直接对被管控应用进行访问限制，无需创建策略，设置后立即生效，直至调用[releaseAppsRestriction](screentimeguard-guardservice.md#releaseappsrestriction)接口主动解除限制。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 被选择的应用token。 |
| restrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 是 | 限制类型。  TRUSTLIST\_TYPE表示对appInfo外的应用进行限制，BLOCKLIST\_TYPE表示对appInfo内的应用进行限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function setAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testSetAppsRestriction() {
   let selectedTokens: string[] = []; // 可以通过调用startAppPicker接口获取相应的应用token并填充，本次初始化为空数组，表示未指定任何应用
   let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
   let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE; // 使用禁止清单类型，表示限制appInfo内的应用访问
   guardService.setAppsRestriction(appInfo, restrictionType)
      .then(() => {
         console.info('setAppsRestriction invoke success');
      });
}
```

## releaseAppsRestriction

releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

解除指定应用被[setAppsRestriction](screentimeguard-guardservice.md#setappsrestriction)接口所设置的访问限制。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 被选择的应用token集合，是一个字符串数组。 |
| restrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 是 | 限制类型。  TRUSTLIST\_TYPE表示对appInfo外的应用解除限制，BLOCKLIST\_TYPE表示对appInfo内的应用解除限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function releaseAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testReleaseAppsRestriction() {
   let selectedTokens: string[] = []; // 可以通过调用startAppPicker接口获取相应的应用token并填充，本次初始化为空数组，表示未指定任何应用
   let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
   let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE; // 使用禁止清单类型，表示解除appInfo内的应用访问限制
   guardService.releaseAppsRestriction(appInfo, restrictionType)
      .then(() => {
         console.info('releaseAppsRestriction invoke success');
      });
}
```

## GuardStrategyData

守护策略运行数据，用于表示某个守护策略的已使用时长。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 26.0.0

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| usageDuration | number | 否 | 否 | 策略已使用时长，单位为s。 |

## queryGuardStrategyData

queryGuardStrategyData(strategyName: string): Promise<GuardStrategyData>

查询守护策略的使用时长，即从启动该策略开始，到调用该接口时的所经过的时间。该接口只支持查询[INCLUSIVE\_DURATION\_TYPE](screentimeguard-guardservice.md#timestrategytype)类型的策略使用时长。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 守护策略名称。长度不超过64个字符，仅支持字母、数字和下划线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GuardStrategyData](screentimeguard-guardservice.md#guardstrategydata)> | Promise对象，返回该管控策略的运行数据，包括策略已使用时长。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000008 | This strategy has not been started yet. |
| 1019000009 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1019000010 | Capability is not supported on current device. function queryGuardStrategyData can not work correctly due to limited device capabilities. |
| 1019000011 | The strategy type is not supported. |

**示例：**

```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

function testQueryGuardStrategyData() {
   guardService.queryGuardStrategyData('testStrategyName')
      .then((guardStrategyData: guardService.GuardStrategyData) => {
         console.info('queryGuardStrategyData invoke success, usageData: ' + guardStrategyData.usageDuration);
      });
}
```
