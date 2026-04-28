---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice
title: GuardService（屏幕时间守护服务）
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > GuardService（屏幕时间守护服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ecfea73b33a6c73ec07e3660ba71fc2419c761a635280e76cf908dfea26e64ad
---

本模块提供管控Screen Time Guard Kit对外开放能力，包括应用授权能力、使用时长管控、应用访问限制等功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

## 导入模块

PhoneTablet

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';
```

## GuardServiceErrorCode

PhoneTablet

该枚举定义了Screen Time Guard Kit屏幕时间守护服务错误码。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | [1019000001](screentimeguard-error-code.md#section1019000001-内部错误) | 内部错误。 |
| USER\_NOT\_AUTHORIZED | [1019000002](screentimeguard-error-code.md#section1019000002-用户未授权) | 用户未授权。 |
| USER\_CANCELED | [1019000003](screentimeguard-error-code.md#section1019000003-用户取消) | 用户取消。 |
| STRATEGIES\_EXCEED\_LIMIT | [1019000004](screentimeguard-error-code.md#section1019000004-策略数量超限) | 策略数量超限。 |
| STRATEGY\_NAME\_ALREADY\_EXIST | [1019000005](screentimeguard-error-code.md#section1019000005-策略名称重复) | 策略名称重复。 |
| NONEXISTENT\_STRATEGY | [1019000006](screentimeguard-error-code.md#section1019000006-策略不存在) | 策略不存在。 |
| STRATEGY\_ALREADY\_EXECUTED | [1019000007](screentimeguard-error-code.md#section1019000007-策略重复执行) | 策略重复执行。 |
| STRATEGY\_NOT\_STARTED | [1019000008](screentimeguard-error-code.md#section1019000008-策略未执行) | 策略未执行。 |
| INVALID\_PARAM | [1019000009](screentimeguard-error-code.md#section1019000009-参数检查失败) | 无效参数。  **起始版本：** 6.0.2(22) |

## requestUserAuth

PhoneTablet

requestUserAuth(context: common.UIAbilityContext): Promise<void>

请求用户授权访问Screen Time Guard Kit的所有管控接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

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

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function requestUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { guardService } from '@kit.ScreenTimeGuardKit';

4. @Entry
5. @Component
6. struct TestPage {
7. build() {
8. Column() {
9. Button("TestRequestUserAuth")
10. .onClick(() => {
11. guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext)
12. .then(() => {
13. console.info('requestUserAuth invoke success');
14. })
15. })
16. }
17. }
18. }
```

## revokeUserAuth

PhoneTablet

revokeUserAuth(): Promise<void>

取消用户授权访问Screen Time Guard Kit的相关管控接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function revokeUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testRevokeUserAuth() {
4. guardService.revokeUserAuth()
5. .then(() => {
6. console.info('revokeUserAuth invoke success.');
7. })
8. }
```

## getUserAuthStatus

PhoneTablet

getUserAuthStatus(): Promise<AuthStatus>

获取用户授权状态，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthStatus](screentimeguard-guardservice.md#authstatus)> | Promise对象，返回用户授权状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function getUserAuthStatus can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testGetUserAuthStatus() {
4. guardService.getUserAuthStatus()
5. .then((status) => {
6. const statusToMsg = ['AUTH_INIT', 'AUTH_GRANTED', 'AUTH_DENIED'];
7. console.info('getUserAuthStatus invoke success. ' + statusToMsg[status + 1]);
8. })
9. }
```

## AuthStatus

PhoneTablet

用户授权状态类型的枚举。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH\_INIT | -1 | 初始状态 |
| AUTH\_GRANTED | 0 | 用户已授权 |
| AUTH\_DENIED | 1 | 用户已拒绝 |

## AppInfo

PhoneTablet

该接口为应用token信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| appTokens | string[] | 否 | 否 | 应用token数组。  数组数量上限：100。  **说明**：  1. appTokens数组中存在错误的token，若只是部分错误，则取其中正常的token做显示和应用。  2. 该数组可以为空数组，即用户不设置任何应用在禁止/允许清单中，是正常场景。 |

## addGuardStrategy

PhoneTablet

addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>

添加屏幕时间管控策略，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| guardStrategy | [GuardStrategy](screentimeguard-guardservice.md#guardstrategy) | 是 | 管控策略。  **说明**：  添加管控策略时策略数量的上限为50条。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

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

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testAddGuardStrategy() {
4. const time: guardService.TimeStrategy = {
5. type: guardService.TimeStrategyType.START_END_TIME_TYPE,
6. startTime: "08:00",
7. endTime: "19:00",
8. repeat: [1,2,3]
9. }
10. const info: guardService.AppInfo = {
11. appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token
12. }
13. const strategy: guardService.GuardStrategy = {
14. name: "TestStrategy",
15. timeStrategy: time,
16. appInfo: info,
17. appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
18. }
19. guardService.addGuardStrategy(strategy)
20. .then(() => {
21. console.info('addGuardStrategy invoke success.');
22. })
23. }
```

## GuardStrategy

PhoneTablet

该接口为守护策略对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 策略名称。长度不超过64字符，仅支持字母、数字和下划线，超出范围时返回401错误码。 |
| timeStrategy | [TimeStrategy](screentimeguard-guardservice.md#timestrategy) | 否 | 否 | 时间策略。 |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 否 | 否 | 应用信息。 |
| appRestrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 否 | 否 | 限制类型。 |

## TimeStrategy

PhoneTablet

该接口为时间策略对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | [TimeStrategyType](screentimeguard-guardservice.md#timestrategytype) | 否 | 否 | 时间管控策略类型。 |
| startTime | string | 否 | 是 | 起始时间，需采用"HH:mm"格式，有效范围为"00:00"至"23:59"。格式错误或超出范围将返回401错误码。  **说明**：  若TimeStrategyType为START\_END\_TIME\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。 |
| endTime | string | 否 | 是 | 结束时间，需采用"HH:mm"格式，有效范围为"00:00"至"23:59"。格式错误或超出范围将返回401错误码。  **说明**：  1. 若TimeStrategyType为START\_END\_TIME\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。  2. 若结束时间小于起始时间，则代表的是次日。  3. 起始时间和结束时间不能相同。 |
| totalDuration | number | 否 | 是 | 总时长，单位为min。参数范围：0-1440。  **说明**：  若TimeStrategyType为TOTAL\_DURATION\_TYPE或INCLUSIVE\_DURATION\_TYPE，此参数必填，置空将返回401错误码；若TimeStrategyType为其它，此参数不生效。 |
| repeat | number[] | 否 | 是 | 重复执行时间，支持填写1~7，代表周一到周日。如果传入的是空数组则表示只执行一次。  默认值：[]。  **说明**：  TimeStrategyType为START\_END\_TIME\_TYPE和INCLUSIVE\_DURATION\_TYPE时此参数才生效。 |

## TimeStrategyType

PhoneTablet

时长策略类型的枚举。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START\_END\_TIME\_TYPE | 1 | 起始时间策略类型，表示策略在配置的起始时间和结束时间内生效。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime必填，totalDuration非必填。 |
| TOTAL\_DURATION\_TYPE | 2 | 总时长策略类型，表示策略生效的总时长，从调用[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)接口成功后开始计时。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime非必填，totalDuration必填。 |
| INCLUSIVE\_DURATION\_TYPE | 3 | 共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额，超额后所有应用均受时长限制，从调用[startGuardStrategy](screentimeguard-guardservice.md#startguardstrategy)接口成功后开始计时。如果为此类型，则[TimeStrategy](screentimeguard-guardservice.md#timestrategy)接口中的startTime、endTime非必填，totalDuration必填，RestrictionType只支持TRUSTLIST\_TYPE。  **起始版本：** 6.0.2(22) |

## RestrictionType

PhoneTablet

限制类型的枚举。

**模型约束：** 此枚举仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRUSTLIST\_TYPE | 1 | 按允许清单做限制。 |
| BLOCKLIST\_TYPE | 2 | 按禁止清单做限制。 |

## updateGuardStrategy

PhoneTablet

updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>

更新已存在的守护策略。更新策略立即生效，如果策略已被启动，管控效果会立即刷新。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 待更新的时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线，超出范围时返回401错误码。 |
| guardStrategy | [GuardStrategy](screentimeguard-guardservice.md#guardstrategy) | 是 | 新的时间管控策略。  **说明**：  如想修改策略名称，可以在guardStrategy的name属性中传入新名称。但不能是已存在的名称，如果名称已存在则返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function updateGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testUpdateGuardService() {
4. const time: guardService.TimeStrategy = {
5. type: guardService.TimeStrategyType.START_END_TIME_TYPE,
6. startTime: "08:00",
7. endTime: "19:00",
8. repeat: [1,2,3,4,5]
9. }
10. const info: guardService.AppInfo = {
11. appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token
12. }
13. const strategy: guardService.GuardStrategy = {
14. name: "TestStrategyChanged",
15. timeStrategy: time,
16. appInfo: info,
17. appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
18. }
19. // "TestStrategy"策略需提前通过addGuardStrategy接口添加
20. guardService.updateGuardStrategy("TestStrategy", strategy)
21. .then(() => {
22. console.info('updateGuardStrategy invoke success.');
23. })
24. }
```

## queryGuardStrategies

PhoneTablet

queryGuardStrategies(): Promise<GuardStrategy[]>

查询该应用下的所有管控策略，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GuardStrategy[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice#guardstrategy)> | Promise对象，返回该应用下所有管控策略的数组。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function queryGuardStrategies can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testQueryGuardService() {
4. guardService.queryGuardStrategies()
5. .then((guardStrategy: guardService.GuardStrategy[]) => {
6. console.info('queryGuardStrategies invoke success, GuardStrategies: ' + guardStrategy);
7. })
8. }
```

## removeGuardStrategy

PhoneTablet

removeGuardStrategy(strategyName: string): Promise<void>

移除指定的守护策略。策略移除后，该策略将无法再被启动，如果策略正在执行中，会先自动停止策略再移除。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线，超出范围时返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function removeGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testRemoveGuardService() {
4. guardService.removeGuardStrategy("TestStrategy")
5. .then(() => {
6. console.info('removeGuardStrategy invoke success');
7. })
8. }
```

## startGuardStrategy

PhoneTablet

startGuardStrategy(strategyName: string): Promise<void>

根据策略名称，立即启动指定的管控策略，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线，超出范围时返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

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

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testGuardService() {
4. guardService.startGuardStrategy("TestStrategy")
5. .then(() => {
6. console.info('startGuardStrategy invoke success');
7. })
8. }
```

## stopGuardStrategy

PhoneTablet

stopGuardStrategy(strategyName: string): Promise<void>

根据策略名称，立即停止指定的管控策略，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线，超出范围时返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

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

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testStopGuardService() {
4. guardService.stopGuardStrategy("TestStrategy")
5. .then(() => {
6. console.info('stopGuardStrategy invoke success');
7. })
8. }
```

## setAppsRestriction

PhoneTablet

setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

可根据传入的应用token数组，以及限制类型（允许/禁用清单），实现对相应的应用添加访问限制，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 被选择的应用token集合，是一个字符串数组。 |
| restrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 是 | 限制类型  TRUSTLIST\_TYPE表示对appInfo外的应用进行限制，BLOCKLIST\_TYPE表示对appInfo内的应用进行限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function setAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testSetAppsRestriction() {
4. let selectedTokens: string[] = []; // 可以通过调用startAppPicker接口获取相应的应用token
5. let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
6. let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE;
7. guardService.setAppsRestriction(appInfo, restrictionType)
8. .then(() => {
9. console.info('setAppsRestriction invoke success');
10. });
11. }
```

## releaseAppsRestriction

PhoneTablet

releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

可根据传入的应用token数组，以及限制类型（允许/禁用清单），实现对相应的应用解除访问限制，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | [AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 被选择的应用token集合，是一个字符串数组。 |
| restrictionType | [RestrictionType](screentimeguard-guardservice.md#restrictiontype) | 是 | 限制类型  TRUSTLIST\_TYPE表示对appInfo外的应用进行限制，BLOCKLIST\_TYPE表示对appInfo内的应用进行限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function releaseAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

**示例：**

```
1. import { guardService } from '@kit.ScreenTimeGuardKit';

3. function testReleaseAppsRestriction() {
4. let selectedTokens: string[] = []; // 可以通过调用startAppPicker获取相应应用的token
5. let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
6. let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE;
7. guardService.releaseAppsRestriction(appInfo, restrictionType)
8. .then(() => {
9. console.info('releaseAppsRestriction invoke success');
10. });
11. }
```
