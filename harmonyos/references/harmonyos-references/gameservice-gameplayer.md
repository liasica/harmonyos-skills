---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-gameplayer
title: gamePlayer（基础游戏服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:92f473d3f247ee94a69c748ac6de16b4a9d8524ae86f4e06923047843782f4fe
---

本模块提供接入Game Service Kit（游戏服务）的基础游戏服务能力。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { gamePlayer } from '@kit.GameServiceKit';
```

## GSKLocalPlayer

PhonePC/2in1TabletTV

玩家信息类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| gamePlayerId | string | 否 | 否 | 游戏玩家ID。转移场景下gamePlayerId不为空。  最大长度256个字符。 |
| teamPlayerId | string | 否 | 否 | 团队玩家ID。绑定场景下teamPlayerId不为空。  最大长度256个字符。 |
| idCompatibleType | number | 否 | 否 | ID兼容类型。  0：gamePlayerId与openId、playerId不兼容，即调用[getLocalPlayer](gameservice-gameplayer.md#gameplayergetlocalplayer)接口时，玩家首次登录游戏生成的玩家标识；teamPlayerId与unionId不兼容，即调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口时，玩家首次登录游戏未选择转移APK游戏数据生成的玩家标识。  1：gamePlayerId兼容playerId，即玩家首次登录游戏时选择转移APK游戏数据，且APK游戏使用了playerId作为玩家标识，Game Service Kit将playerId作为新的gamePlayerId。  2：gamePlayerId兼容openId，即玩家首次登录游戏时选择转移APK游戏数据，且APK游戏使用了openId作为玩家标识，Game Service Kit将openId作为新的gamePlayerId。 |
| level | number | 否 | 否 | 玩家等级。**此参数为预留参数，当前固定返回0。** |
| playableTime | number | 否 | 否 | 玩家本次可玩时长，单位：分钟。**此参数为预留参数，当前固定返回-1。**  **说明**：-1表示成年玩家返回的当前可玩时长，大于等于0则表示未成年玩家当前的可玩时长。 |
| loginIdType | number | 否 | 否 | 登录游戏时，玩家使用的账号ID类型。  1：gamePlayerId  2：teamPlayerId  **起始版本：** 5.0.0(12)。 |

## GSKPlayerRole

PhonePC/2in1TabletTV

玩家角色信息类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

注意

gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| roleId | string | 否 | 否 | 玩家角色ID，请勿传""和null。  如果游戏没有角色系统，请传入“0”。  最大长度128个字符。 |
| roleName | string | 否 | 否 | 玩家角色名，请勿传""和null。  如果游戏没有角色系统，请传入“default”。  最大长度128个字符。 |
| serverId | string | 否 | 是 | 玩家区服ID。  最大长度128个字符。 |
| serverName | string | 否 | 是 | 玩家区服名。  最大长度128个字符。 |
| gamePlayerId | string | 否 | 是 | 游戏玩家ID。  最大长度256个字符。 |
| teamPlayerId | string | 否 | 是 | 团队玩家ID。游戏官方账号与华为teamPlayerId绑定场景下可传入此参数。  最大长度256个字符。 |
| thirdOpenId | string | 否 | 是 | 游戏官方账号ID。  最大长度128个字符。  **起始版本：** 5.0.0(12)。 |

## ThirdUserInfo

PhonePC/2in1TabletTV

账号合规信息类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

说明

华为账号合规校验时，无需传isRealName、isAdult、ageRange参数。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| thirdOpenId | string | 否 | 否 | 游戏官方账号ID。若无，则传空字符串""。  最大长度128个字符。 |
| isRealName | boolean | 否 | 是 | 玩家是否实名。  - true：已实名  - false：未实名 |
| isAdult | boolean | 否 | 是 | 玩家账号实名认证是否为成年人。  - true：已成年  - false：未成年 |
| ageRange | [ThirdUserAgeRange](gameservice-gameplayer.md#thirduseragerange) | 否 | 是 | 玩家当前年龄段信息。 |

## UnionLoginParam

PhonePC/2in1TabletTV

联合登录参数。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| thirdAccountInfos | Array<[ThirdAccountInfo](gameservice-gameplayer.md#thirdaccountinfo)> | 否 | 否 | 游戏官方账号信息，用于在联合登录面板中展示。不同账号的账号名称不能相同。  **说明**：若只需实现华为账号快速登录，此参数传空数组。 |
| showLoginDialog | boolean | 否 | 否 | 是否强制弹出联合登录面板，允许玩家选择重新登录。  - true：调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口时，强制弹出联合登录面板。当需要切换账号或进行其他操作时，请将此值设置为true。  - false：调用[unionLogin](gameservice-gameplayer.md#gameplayerunionlogin)接口时，优先使用玩家上一次的选择，不强制弹出联合登录面板。  默认为false。 |
| loginPanelType | [LoginPanelType](gameservice-gameplayer.md#loginpaneltype) | 否 | 是 | 联合登录面板类型：  - ICON  - BUTTON  默认为ICON。 |

## ThirdAccountInfo

PhonePC/2in1TabletTV

游戏官方账号信息。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| accountIcon | [Resource](ts-types.md#resource) | 否 | 否 | 游戏官方账号图标资源信息。总和最大支持35KB。  当前仅支持**media**目录下的图片。 |
| accountName | string | 否 | 否 | 游戏官方账号在联合登录面板上的显示名称。  建议传入具体的“xx游账号登录”、“xx通行证登录”等，例如“游友账号登录”，不建议使用“官方账号登录”等容易有歧义的账号名称。  若游戏存在多语言版本，开发者需要自行判断语种并传入当前语种对应的账号名称。  在LoginPanelType设置成“BUTTON”时，accountName作为对外展示的按钮文字。  最大长度19个字符。 |
| accountIdentifier | string | 否 | 是 | 当前账号的唯一标识符，用来标识账号，并在登录结果中判断玩家选择的账号。  建议传入和当前账号相关的标识符，例如“youyou\_account”。  默认值：undefined。  最大长度32个字符。  **起始版本：** 6.0.2(22) |
| isOnTop | boolean | 否 | 是 | 在LoginPanelType设置为“ICON”时生效。  当前账号是否在联合登录面板上置顶：  - true：置顶。  - false：不置顶。  默认为false。  **说明**：  - 仅会置顶第一个传入“true”的账号，且被置顶的账号展示为按钮样式（按钮文案为传入的accountName值），非置顶账号展示为图标样式。  - 在BUTTON或ICON类型的登录面板上，华为侧置顶华为账号的优先级更高。  **起始版本：** 6.0.2(22) |

## BoundPlayerInfo

PhonePC/2in1TabletTV

绑定信息类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| thirdOpenId | string | 否 | 否 | 游戏官方账号ID。 |
| bindType | [BindType](gameservice-gameplayer.md#bindtype) | 否 | 否 | 与游戏官方账号绑定的类型。 |

## BindType

PhonePC/2in1TabletTV

账号绑定枚举类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| CP\_ACCOUNT\_LEVEL | 0 | 开发者级别。 |
| APP\_LEVEL | 1 | 游戏级别。 |

## UnionLoginResult

PhonePC/2in1TabletTV

联合登录结果。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| accountName | string | 否 | 否 | 账号名。  - 若玩家选择华为账号，则返回“hw\_account”。  - 若玩家选择开发者提供的游戏官方账号，则返回传入的ThirdAccountInfo.accountName。  - 若登录过程中出现异常，则返回“official\_account”。  “official\_account”表示目前无法返回具体的账号名，建议从开发者提供的账号中选择其中一个登录。  最大长度19个字符。 |
| needBinding | boolean | 否 | 否 | 玩家标识是否需要绑定游戏官方账号。  - true：为绑定场景，需要绑定游戏官方账号。  - false：为转移场景，无需绑定游戏官方账号。  游戏服务器需要根据玩家选择的登录场景进行适配：  - 转移场景下，服务器需与HarmonyOS系统的渠道包策略保持一致。  - 绑定场景下/选择游戏官方账号登录场景下，服务器策略和游戏官方包保持一致。 |
| boundPlayerInfo | [BoundPlayerInfo](gameservice-gameplayer.md#boundplayerinfo) | 否 | 否 | 与华为PlayerId绑定的游戏官方账号信息。 |
| localPlayer | [GSKLocalPlayer](gameservice-gameplayer.md#gsklocalplayer) | 否 | 否 | 玩家信息。 |
| accountIdentifier | string | 否 | 是 | 当前账号的唯一标识符，用来判断玩家选择的账号：  - 若玩家选择华为账号登录，则返回“hw\_account”。  - 若玩家选择开发者提供的游戏官方账号，则返回传入的ThirdAccountInfo.accountIdentifier。  - 若登录过程中出现异常，则返回“official\_account”。  “official\_account”表示目前无法返回具体的账号名，建议从开发者提供的账号中选择其中一个登录。  最大长度为32个字符。  **起始版本：** 6.0.2(22) |

## PlayerChangedResult

PhonePC/2in1TabletTV

玩家变化结果。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| event | [PlayerChangedEvent](gameservice-gameplayer.md#playerchangedevent) | 否 | 否 | 玩家变化事件。 |
| resultInfo | string | 否 | 否 | JSON字符串，返回当前事件的相关信息。  最大长度1024个字符。 |

## PlayerChangedEvent

PhonePC/2in1TabletTV

玩家变化事件枚举类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| SWITCH\_GAME\_ACCOUNT | 0 | 玩家切换游戏账号。 |

## ThirdUserAgeRange

PhonePC/2in1TabletTV

游戏官方账号的年龄信息枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| AGE\_RANGE\_8 | 1 | 玩家实名认证年龄小于8周岁。 |
| AGE\_RANGE\_16 | 2 | 玩家实名认证年龄大于等于8周岁，且小于16周岁。 |
| AGE\_RANGE\_18 | 3 | 玩家实名认证年龄大于等于16周岁，且小于18周岁。 |
| AGE\_RANGE\_ADULT | 4 | 玩家实名认证年龄大于等于18周岁。 |

## LoginPanelType

PhonePC/2in1TabletTV

登录面板枚举类。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ICON | 0 | - 除了华为账号，联合登录面板上最多还可以展示三个游戏官方账号。  - 开发者可以设置isOnTop参数，置顶登录面板上的任一种游戏官方账号。 |
| BUTTON | 1 | - 登录面板上仅展示华为账号和游戏官方账号，且这两种登录账号均展示为按钮样式。  - 开发者无需设置置顶参数，登录面板上默认游戏官方账号在上、华为账号在下。 |

## GameErrorCode

PhonePC/2in1TabletTV

错误码枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.1.0(11)

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| **名称** | 值 | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | 1002000001 | 游戏内部通用错误。 |
| NETWORK\_ERROR | 1002000002 | 网络连接错误。 |
| GET\_HWID\_INFO\_FAILED | 1002000003 | 未查到华为账号相关信息。 |
| REALNAME\_CANCELED\_OR\_NOT\_REALNAME | 1002000004 | 实名认证返回强制实名但用户取消，或需要强制实名但没有实名。 |
| COUNTRY\_OR\_REGION\_NOT\_SUPPORTED | 1002000005 | 只支持服务地和注册地均为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号。 |
| ANTI\_ADDICTION\_ERROR | 1002000006 | 玩家未成年并且当前不在可游戏时间。  **起始版本：** 5.0.0(12)。 |
| PRODUCT\_BELONG\_REGION\_ERROR | 1002000007 | 商品所属的应用未在指定国家/地区上架。 |
| HWID\_IN\_BLOCKLIST | 1002000008 | 该华为账号在禁止名单中。 |
| GAME\_ACCOUNT\_UNAVAILABLE | 1002000009 | 当前游戏不支持第三方游戏账号。  **起始版本：** 5.0.0(12)。 |
| PLAYER\_ID\_INVALID | 1002000010 | 华为teamPlayerId与当前玩家不匹配。  **起始版本：** 5.0.0(12)。 |
| AGREEMENT\_NOT\_AGREED | 1002000011 | 玩家未同意隐私协议。  **起始版本：** 5.0.0(12)。 |
| OPEN\_ID\_OR\_PLAYER\_ID\_BOUND | 1002000012 | 游戏官方账号与华为teamPlayerId已绑定。  **起始版本：** 5.0.0(12)。 |
| OPEN\_ID\_AND\_PLAYER\_ID\_NOT\_BOUND | 1002000013 | 游戏官方账号与华为teamPlayerId未绑定。  **起始版本：** 5.0.0(12)。 |
| CURRENT\_API\_NOT\_AVAILABLE\_FOR\_GAME | 1002000014 | 此接口不适用于此游戏。  **起始版本：** 5.0.0(12)。 |
| CURRENT\_PLAYER\_INFO\_INVALID | 1002000015 | 当前玩家信息无效。  **起始版本：** 5.0.0(12)。 |
| UNION\_LOGIN\_CANCELED | 1002000016 | 玩家取消联合登录。  **起始版本：** 5.0.0(12)。 |
| ILLEGAL\_APPLICATION | 1002000017 | 非法应用。  **起始版本：** 5.0.0(12)。 |
| NOT\_MINI\_GAME\_ERROR | 1002000018 | 此API仅支持小游戏。  **起始版本：** 6.0.1(21)。 |
| PARAM\_ERROR | 1002000019 | 参数错误。  **起始版本：** 6.0.1(21)。 |
| USER\_CANCELED | 1002000020 | 当前操作被用户取消。  **起始版本：** 6.0.1(21)。 |
| CALLS\_FREQUENT | 1002000021 | API调用过于频繁。  **起始版本：** 6.0.1(21)。 |
| PAY\_PRODUCT\_INVALID | 1002000050 | 无效的商品信息。  **起始版本：** 6.0.1(21)。 |
| PAY\_PRODUCT\_OWNED | 1002000051 | 由于已经拥有该商品，购买失败。  **起始版本：** 6.0.1(21)。 |
| PAY\_PRODUCT\_NOT\_OWNED | 1002000052 | 由于未拥有该商品，发货失败。  **起始版本：** 6.0.1(21)。 |
| PAY\_PRODUCT\_CONSUMED | 1002000053 | 此次购买已经完成发货，无需重复发货。  **起始版本：** 6.0.1(21)。 |
| PAY\_ACCOUNT\_REGION\_UNSUPPORTED | 1002000054 | 用户账号所在服务地不在IAP Kit支持结算的国家/地区中。  **起始版本：** 6.0.1(21)。 |
| PAY\_DEAL\_REJECTED | 1002000056 | 用户交易被拒绝。  **起始版本：** 6.0.1(21)。 |

## gamePlayer.init

PhonePC/2in1TabletTV

init(context: common.UIAbilityContext): Promise<void>

游戏启动时，需要对Game Service Kit进行初始化。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。  **说明**：严格要求继承UIAbility，并且获取上下文的时机是onWindowStageCreate生命周期中页面加载成功后。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { gamePlayer } from '@kit.GameServiceKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. windowStage.loadContent("pages/index", (err, data) => {
10. try {
11. gamePlayer.init(this.context).then(() => {
12. hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
13. });
14. } catch (error) {
15. let err = error as BusinessError;
16. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
17. }
18. });
19. }
20. }
```

## gamePlayer.init

PhonePC/2in1TabletTV

init(context: common.UIAbilityContext, callback: AsyncCallback<void>): void

游戏启动时，需要对Game Service Kit进行初始化。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。  **说明**：严格要求继承UIAbility，并且获取上下文的时机是onWindowStageCreate生命周期中页面加载成功后。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当初始化成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { gamePlayer } from '@kit.GameServiceKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. windowStage.loadContent("pages/index", (err, data) => {
10. try {
11. gamePlayer.init(this.context,()=>{
12. hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
13. });
14. } catch (error) {
15. let err = error as BusinessError;
16. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
17. }
18. });
19. }
20. }
```

## gamePlayer.unionLogin

PhonePC/2in1TabletTV

unionLogin(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult>

华为账号和游戏官方账号联合登录。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| loginParam | [UnionLoginParam](gameservice-gameplayer.md#unionloginparam) | 是 | 联合登录参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[UnionLoginResult](gameservice-gameplayer.md#unionloginresult)> | Promise对象。返回联合登录结果对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000004 | User cancels real name authentication or not real name. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000008 | The HUAWEI ID is in the blocklist. |
| 1002000011 | Agreement not agreed. |
| 1002000014 | This interface is not available for this game. |
| 1002000016 | Union login canceled by user. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct UnionLogin {
9. build() {
10. Row() {
11. Button('unionLogin')
12. .onClick(() => {
13. this.callUnionLogin();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callUnionLogin() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let thirdAccountInfo1: gamePlayer.ThirdAccountInfo = {
25. 'accountName': 'testName1', // 游戏官方账号在联合登录面板上的显示名称。建议传入具体的“xx游账号登录”、“xx通行证登录”等，例如“游友账号登录”，不建议使用“官方账号登录”等容易有歧义的账号名称。若游戏存在多语言版本，需要开发者自行判断语种并传入当前语种对应的账号名称
26. 'accountIcon': $r('app.media.icon'), // 游戏官方账号图标资源信息，图标大小总和不能超过35KB
27. 'accountIdentifier': 'testIdentifier1', // 当前账号的唯一标识符，此标识符用来标识账号并在登录结果处理中用于判断识别玩家选择的账号
28. 'isOnTop': true // 当前账号是否置顶显示，且仅会置顶第一个传入true的账号
29. };
30. let request: gamePlayer.UnionLoginParam = {
31. showLoginDialog: true, // 是否弹出联合登录面板。true表示强制弹出面板，false表示优先使用玩家上一次的登录选择，不弹出联合登录面板，若玩家首次登录或卸载重装，则正常弹出
32. thirdAccountInfos: [
33. thirdAccountInfo1 // 若游戏无官包或无官方账号体系，请传空数组
34. ]
35. };
36. try {
37. gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
38. hilog.info(0x0000, 'testTag', `Succeeded in logging in: ${result?.accountName}`);
39. }).catch((error: BusinessError) => {
40. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
41. });
42. } catch (error) {
43. let err = error as BusinessError;
44. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
45. }
46. }
47. }
```

## gamePlayer.getLocalPlayer

PhonePC/2in1TabletTV

getLocalPlayer(context: common.UIAbilityContext): Promise<GSKLocalPlayer>

获取玩家信息。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[GSKLocalPlayer](gameservice-gameplayer.md#gsklocalplayer)> | Promise对象。返回玩家信息。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000004 | User cancels real name authentication or not real name. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000006 | User is underage and has no playable time. |
| 1002000011 | Agreement not agreed. |
| 1002000014 | This interface is not available for this game. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct GetLocalPlayer {
9. build() {
10. Row() {
11. Button('getLocalPlayer')
12. .onClick(() => {
13. this.callGetLocalPlayer();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callGetLocalPlayer() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. try {
25. gamePlayer.getLocalPlayer(context).then((result) => {
26. hilog.info(0x0000, 'testTag', `Succeeded in getting: ${result?.gamePlayerId}`);
27. }).catch((error: BusinessError) => {
28. hilog.error(0x0000, 'testTag', `Failed to get. Code: ${error.code}, message: ${error.message}`);
29. });
30. } catch (error) {
31. let err = error as BusinessError;
32. hilog.error(0x0000, 'testTag', `Failed to get. Code: ${err.code}, message: ${err.message}`);
33. }
34. }
35. }
```

## gamePlayer.getLocalPlayer

PhonePC/2in1TabletTV

getLocalPlayer(context: common.UIAbilityContext, callback: AsyncCallback<GSKLocalPlayer>): void

获取玩家信息。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| callback | AsyncCallback<[GSKLocalPlayer](gameservice-gameplayer.md#gsklocalplayer)> | 是 | 回调函数。当获取玩家信息成功，err为undefined，否则为错误对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000004 | User cancels real name authentication or not real name. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000006 | User is underage and has no playable time. |
| 1002000011 | Agreement not agreed. |
| 1002000014 | This interface is not available for this game. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct GetLocalPlayer {
9. build() {
10. Row() {
11. Button('getLocalPlayer')
12. .onClick(() => {
13. this.callGetLocalPlayer();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callGetLocalPlayer() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. try {
25. gamePlayer.getLocalPlayer(context, (error, result) => {
26. if (error) {
27. hilog.error(0x0000, 'testTag', `Failed to get. Code: ${error.code}, message: ${error.message}`);
28. return;
29. }
30. hilog.info(0x0000, 'testTag', `Succeeded in getting: ${result?.gamePlayerId}`);
31. });
32. } catch (error) {
33. let err = error as BusinessError;
34. hilog.error(0x0000, 'testTag', `Failed to get. Code: ${err.code}, message: ${err.message}`);
35. }
36. }
37. }
```

## gamePlayer.bindPlayer

PhonePC/2in1TabletTV

bindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>

将玩家华为账号对应的teamPlayerId与游戏官方账号绑定。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| thirdOpenId | string | 是 | 游戏官方账号ID。  最大长度128个字符。 |
| teamPlayerId | string | 是 | 玩家华为账号对应的teamPlayerId。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000010 | The playerId is not current player. |
| 1002000011 | Agreement not agreed. |
| 1002000012 | The thirdOpenId or teamPlayerId has been bound. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct BindPlayer {
9. build() {
10. Row() {
11. Button('bindPlayer')
12. .onClick(() => {
13. this.callBindPlayer();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callBindPlayer() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let thirdOpenId = '123xxxx';
25. let teamPlayerId = '456xxx';
26. try {
27. gamePlayer.bindPlayer(context, thirdOpenId, teamPlayerId).then(() => {
28. hilog.info(0x0000, 'testTag', `Succeeded in binding.`);
29. }).catch((error: BusinessError) => {
30. hilog.error(0x0000, 'testTag', `Failed to bind. Code: ${error.code}, message: ${error.message}`);
31. });
32. } catch (error) {
33. let err = error as BusinessError;
34. hilog.error(0x0000, 'testTag', `Failed to bind. Code: ${err.code}, message: ${err.message}`);
35. }
36. }
37. }
```

## gamePlayer.unbindPlayer

PhonePC/2in1TabletTV

unbindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>

将玩家华为账号对应的teamPlayerId与游戏官方账号解绑。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| thirdOpenId | string | 是 | 游戏官方账号ID。 |
| teamPlayerId | string | 是 | 玩家华为账号对应的teamPlayerId。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000010 | The playerId is not current player. |
| 1002000011 | Agreement not agreed. |
| 1002000013 | The thirdOpenId and teamPlayerId are not bound. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct UnbindPlayer {
9. build() {
10. Row() {
11. Button('unbindPlayer')
12. .onClick(() => {
13. this.callUnbindPlayer();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callUnbindPlayer() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let thirdOpenId = '123xxxx';
25. let teamPlayerId = '456xxx';
26. try {
27. gamePlayer.unbindPlayer(context, thirdOpenId, teamPlayerId).then(() => {
28. hilog.info(0x0000, 'testTag', `Succeeded in unbinding.`);
29. }).catch((error: BusinessError) => {
30. hilog.error(0x0000, 'testTag', `Failed to unbind. Code: ${error.code}, message: ${error.message}`);
31. });
32. } catch (error) {
33. let err = error as BusinessError;
34. hilog.error(0x0000, 'testTag', `Failed to unbind. Code: ${err.code}, message: ${err.message}`);
35. }
36. }
37. }
```

## gamePlayer.verifyLocalPlayer

PhonePC/2in1TabletTV

verifyLocalPlayer(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void>

合规校验接口，校验当前设备登录的账号的实名认证、游戏防沉迷信息。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| thirdUserInfo | [ThirdUserInfo](gameservice-gameplayer.md#thirduserinfo) | 是 | 游戏自己维护的玩家合规信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000004 | User cancels real name authentication or not real name. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000006 | User is underage and has no playable time. |
| 1002000008 | The HUAWEI ID is in the blocklist. |
| 1002000011 | Agreement not agreed. |
| 1002000015 | The current player information is invalid. Execute the login process again to obtain the player information. |
| 1002000017 | Illegal application identity. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct VerifyLocalPlayer {
9. build() {
10. Row() {
11. Button('verifyLocalPlayer')
12. .onClick(() => {
13. this.callVerifyLocalPlayer();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callVerifyLocalPlayer() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. // thirdUserInfo是使用游戏官方账号登录游戏的玩家合规信息，接入华为账号登录时无需传入该信息，但在接入游戏官方账号登录时要求传入相关信息
25. let request: gamePlayer.ThirdUserInfo = {
26. thirdOpenId: '123xxxx', // 游戏官方账号ID，接入华为账号登录时传空
27. isRealName: true // 玩家是否实名,该值为true时表示已实名,为false时表示未实名，接入华为账号登录时不传该字段
28. };
29. try {
30. gamePlayer.verifyLocalPlayer(context, request).then(() => {
31. hilog.info(0x0000, 'testTag', `Succeeded in verifying.`);
32. }).catch((error: BusinessError) => {
33. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
34. });
35. } catch (error) {
36. let err = error as BusinessError;
37. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${err.code}, message: ${err.message}`);
38. }
39. }
40. }
```

## gamePlayer.savePlayerRole

PhonePC/2in1TabletTV

savePlayerRole(context: common.UIAbilityContext, request: GSKPlayerRole): Promise<void>

保存角色信息到游戏服务器。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| request | [GSKPlayerRole](gameservice-gameplayer.md#gskplayerrole) | 是 | 上报角色信息，玩家选择角色及区服后上报。如果游戏没有角色系统，roleId请传入“0”，roleName请传入“default”。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct SavePlayerRole {
9. build() {
10. Row() {
11. Button('savePlayerRole')
12. .onClick(() => {
13. this.callSavePlayerRole();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callSavePlayerRole() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let request: gamePlayer.GSKPlayerRole = {
25. roleId: '123', // 玩家角色ID，如游戏没有角色系统，请传入“0”，务必不要传""和null
26. roleName: 'Jason', // 玩家角色名，如游戏没有角色系统，请传入“default”，务必不要传""和null
27. serverId: '456',
28. serverName: 'Zhangshan',
29. gamePlayerId: '789' // 请根据实际获取到的gamePlayerId传值
30. };
31. try {
32. gamePlayer.savePlayerRole(context, request).then(() => {
33. hilog.info(0x0000, 'testTag', `Succeeded in saving.`);
34. });
35. } catch (error) {
36. let err = error as BusinessError;
37. hilog.error(0x0000, 'testTag', `Failed to save. Code: ${err.code}, message: ${err.message}`);
38. }
39. }
40. }
```

## gamePlayer.savePlayerRole

PhonePC/2in1TabletTV

savePlayerRole(context: common.UIAbilityContext, request: GSKPlayerRole, callback: AsyncCallback<void>): void

保存角色信息到游戏服务器。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 上下文信息。 |
| request | [GSKPlayerRole](gameservice-gameplayer.md#gskplayerrole) | 是 | 上报角色信息，玩家选择角色及区服后上报。如果游戏没有角色系统，roleId请传入“0”，roleName请传入“default”。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当保存角色信息成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct SavePlayerRole {
9. build() {
10. Row() {
11. Button('savePlayerRole')
12. .onClick(() => {
13. this.callSavePlayerRole();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callSavePlayerRole() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let request: gamePlayer.GSKPlayerRole = {
25. roleId: '123', // 玩家角色ID，如游戏没有角色系统，请传入“0”，务必不要传""和null
26. roleName: 'Jason', // 玩家角色名，如游戏没有角色系统，请传入“default”，务必不要传""和null
27. serverId: '456',
28. serverName: 'Zhangshan',
29. gamePlayerId: '789' // 请根据实际获取到的gamePlayerId传值
30. };
31. try {
32. gamePlayer.savePlayerRole(context, request, () => {
33. hilog.info(0x0000, 'testTag', `Succeeded in saving.`);
34. });
35. } catch (error) {
36. let err = error as BusinessError;
37. hilog.error(0x0000, 'testTag', `Failed to save. Code: ${err.code}, message: ${err.message}`);
38. }
39. }
40. }
```

## gamePlayer.on('playerChanged')

PhonePC/2in1TabletTV

on(type: 'playerChanged', callback: Callback<PlayerChangedResult>): void

玩家变化事件监听。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'playerChanged'事件。 |
| callback | Callback<[PlayerChangedResult](gameservice-gameplayer.md#playerchangedresult)> | 是 | 回调函数，返回玩家变化结果。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let playerChangedEventCallback = (result: gamePlayer.PlayerChangedResult): void => {
6. if (result.event === gamePlayer.PlayerChangedEvent.SWITCH_GAME_ACCOUNT) {
7. // ...
8. // 游戏号已切换，完成本地缓存清理工作后，再次调用unionLogin接口等
9. }
10. }

12. // 调用on接口注册playerChanged事件监听
13. try {
14. gamePlayer.on('playerChanged', playerChangedEventCallback);
15. } catch (error) {
16. let err = error as BusinessError;
17. hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
18. }
```

## gamePlayer.off('playerChanged')

PhonePC/2in1TabletTV

off(type: 'playerChanged', callback?: Callback<PlayerChangedResult>): void

取消玩家变化事件监听。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定为'playerChanged'事件。 |
| callback | Callback<[PlayerChangedResult](gameservice-gameplayer.md#playerchangedresult)> | 否 | 回调函数，返回玩家变化结果。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消playerChanged事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例1**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. gamePlayer.off('playerChanged');
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
10. }
```

**示例2**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let playerChangedEventCallback = (result: gamePlayer.PlayerChangedResult): void => {
6. if (result.event === gamePlayer.PlayerChangedEvent.SWITCH_GAME_ACCOUNT) {
7. // ...
8. // 游戏号已切换，完成本地缓存清理工作后，再次调用unionLogin接口等
9. }
10. }

12. try {
13. // 参数playerChangedEventCallback为gamePlayer.on('playerChanged', playerChangedEventCallback)中第二个参数
14. gamePlayer.off('playerChanged', playerChangedEventCallback);
15. } catch (error) {
16. let err = error as BusinessError;
17. hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
18. }
```

## MiniGameLoginParam

PhonePC/2in1TabletTV

小游戏登录信息。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| gameAppId | string | 否 | 否 | 小游戏APP ID。 |
| extraData | string | 否 | 是 | 附加信息，要求JSON String格式，可以将额外需要传入的字段以key:value的形式设置在JSON String中，并通过该参数传入。例如：  let extraData = "{"key1":"value1","key2":"value2"}"; |

## MiniGamePlayer

PhonePC/2in1TabletTV

小游戏玩家信息。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| playerId | string | 否 | 否 | 玩家账号ID。 |
| isAdult | boolean | 否 | 否 | 玩家账号实名认证是否为成年人。  - true：已成年。  - false：未成年。 |
| playerLevel | number | 否 | 否 | 当前玩家账号等级。 |
| playerSign | string | 否 | 否 | 玩家登录签名。 |
| signTs | string | 否 | 否 | 玩家登录签名的时间戳。 |
| extraData | string | 否 | 是 | 附加信息，要求JSON String格式，可以将额外需要传入的字段以key:value的形式设置在JSON String中，并通过该参数传入。例如：  let extraData = "{"key1":"value1","key2":"value2"}"; |

## gamePlayer.on('miniGameAddictionPrevented')

PhonePC/2in1TabletTV

on(type: 'miniGameAddictionPrevented', callback: Callback<string>): void

注册小游戏防沉迷事件监听。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'miniGameAddictionPrevented'事件。 |
| callback | Callback<string> | 是 | 回调函数，返回注册小游戏防沉迷事件结果。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002000018 | This API is only provided for HarmonyOS mini games. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let miniGameAddictionPreventedCallback = (result: string): void => {
6. // 退出小游戏
7. }

9. // 调用on接口注册小游戏防沉迷事件监听
10. try {
11. gamePlayer.on('miniGameAddictionPrevented', miniGameAddictionPreventedCallback);
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
15. }
```

## gamePlayer.off('miniGameAddictionPrevented')

PhonePC/2in1TabletTV

off(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void

取消注册小游戏防沉迷事件监听。使用callback回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定为'miniGameAddictionPrevented'事件。 |
| callback | Callback<string> | 否 | 回调函数，返回取消注册小游戏防沉迷事件结果。  如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消miniGameAddictionPrevented事件的所有callback订阅。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002000018 | This API is only provided for HarmonyOS mini games. |

**示例1**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. gamePlayer.off('miniGameAddictionPrevented');
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
10. }
```

**示例**2：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let miniGameAddictionPreventedCallback = (result: string): void => {
6. // 退出小游戏
7. }

9. try {
10. // 参数miniGameAddictionPreventedCallback为gamePlayer.on('miniGameAddictionPrevented', miniGameAddictionPreventedCallback)中第二个参数
11. gamePlayer.off('miniGameAddictionPrevented', miniGameAddictionPreventedCallback);
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
15. }
```

## gamePlayer.miniGameLogin

PhonePC/2in1TabletTV

miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>

登录小游戏。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.Context | 是 | 上下文信息。 |
| loginParam | [MiniGameLoginParam](gameservice-gameplayer.md#minigameloginparam) | 是 | 小游戏登录信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[MiniGamePlayer](gameservice-gameplayer.md#minigameplayer)> | Promise对象。返回玩家信息。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000004 | User cancels real name authentication or not real name. |
| 1002000005 | The country or region of the signed-in Huawei ID does not support. |
| 1002000006 | User is underage and has no playable time. |
| 1002000008 | The HUAWEI ID is in the blocklist. |
| 1002000011 | Agreement not agreed. |
| 1002000018 | This API is only provided for HarmonyOS mini games. |
| 1002000019 | Parameter error. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct MiniGameLogin {
9. build() {
10. Row() {
11. Button('miniGameLogin')
12. .onClick(() => {
13. this.callMiniGameLogin();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callMiniGameLogin() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let request: gamePlayer.MiniGameLoginParam = {
25. 'gameAppId': '123xxx', // 小游戏appId
26. 'extraData': 'xxx' // 附加信息，要求JSON String格式
27. };
28. try {
29. gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
30. hilog.info(0x0000, 'testTag', `Succeeded in logging in`);
31. }).catch((error: BusinessError) => {
32. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
33. });
34. } catch (error) {
35. let err = error as BusinessError;
36. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
37. }
38. }
39. }
```

## gamePlayer.miniGamePay

PhonePC/2in1TabletTV

miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

提供小游戏付费功能。使用Promise异步回调。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 6.0.1(21)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.Context | 是 | 上下文信息。 |
| parameter | [PurchaseParameter](gameservice-gameplayer.md#purchaseparameter) | 是 | 购买商品参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CreatePurchaseResult](gameservice-gameplayer.md#createpurchaseresult)> | Promise对象。返回创建商品结果信息。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](gameservice-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002000001 | System internal error. |
| 1002000002 | Network connection error. |
| 1002000003 | The HUAWEI ID is not signed in or not authorized. |
| 1002000007 | The application to which the product belongs is not listed in the specified country. |
| 1002000018 | This API is only provided for HarmonyOS mini games. |
| 1002000019 | Parameter error. |
| 1002000020 | The operation was canceled by the user. |
| 1002000021 | Too frequent API calls. |
| 1002000050 | Invalid product information. |
| 1002000051 | Failed to purchase a product because the user already owns the product. |
| 1002000052 | The purchase cannot be finished because the user has not paid for it. |
| 1002000053 | The purchase has been finished and cannot be finished again. |
| 1002000054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1002000056 | The user is not allowed to make purchase. |

**示例**：

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct MiniGamePay {
9. build() {
10. Row() {
11. Button('miniGamePay')
12. .onClick(() => {
13. this.callMiniGamePay();
14. })
15. .width('100%')
16. }
17. .margin(16)
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. private callMiniGamePay() {
23. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
24. let request: gamePlayer.PurchaseParameter = {
25. productId: 'xxx', // 待支付的商品ID
26. productType: 0, // 待查询的商品类型
27. developerPayload: 'xxx', // 商户侧保留信息，该参数长度限制为[0, 256]。若该字段有值，在支付成功后的回调结果中会原样返回给应用
28. reservedInfo: 'xxx' // 要求JSON String格式，商户可以将额外需要传入的字段以key-value的形式设置在JSON String中，并通过该参数传入
29. };
30. try {
31. gamePlayer.miniGamePay(context, request).then((result: gamePlayer.CreatePurchaseResult) => {
32. hilog.info(0x0000, 'testTag', `Succeeded in paying`);
33. }).catch((error: BusinessError) => {
34. hilog.error(0x0000, 'testTag', `Failed to pay. Code: ${error.code}, message: ${error.message}`);
35. });
36. } catch (error) {
37. let err = error as BusinessError;
38. hilog.error(0x0000, 'testTag', `Failed to pay. Code: ${err.code}, message: ${err.message}`);
39. }
40. }
41. }
```

## PurchaseParameter

PhonePC/2in1TabletTV

购买商品参数，仅供IAP Kit和小游戏使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productId | string | 否 | 否 | 待支付的商品ID。 |
| productType | [ProductType](gameservice-gameplayer.md#producttype) | 否 | 否 | 待查询的商品类型。 |
| developerPayload | string | 否 | 是 | 商户侧保留信息，该参数长度限制为[0, 256]。若该字段有值，在支付成功后的回调结果中会原样返回给应用。 |
| reservedInfo | string | 否 | 是 | 要求JSON String格式，商户可以将额外需要传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。例如：  let reservedInfo = "{"key1":"value1","key2":"value2"}";  **说明：** 该字段为预留字段，可选传入，开发者暂时无需关注。 |

## ProductType

PhonePC/2in1TabletTV

商品类型，仅供IAP Kit和小游戏使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONSUMABLE | 0 | 消耗型商品。 |
| NONCONSUMABLE | 1 | 非消耗型商品。 |
| AUTORENEWABLE | 2 | 自动续期订阅商品。  **起始版本：** 5.0.0(12) |

## PurchaseResult

PhonePC/2in1TabletTV

订购商品结果信息，仅供IAP Kit使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| inAppPurchaseData | string | 否 | 否 | 订单数据的JSON字符串。 |
| signature | string | 否 | 否 | 返回使用IAP私钥签署paymentData字符串生成的签名字符串。 |
| signatureAlgorithm | string | 否 | 否 | 签名算法，固定为SHA256WithRSA/PSS。 |

## CreatePurchaseResult

PhonePC/2in1TabletTV

创建商品结果信息，仅供IAP Kit和小游戏使用。

**系统能力：** SystemCapability.Game.GameService.GamePlayer

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| purchaseData | string | 否 | 否 | 包含支付结果的JSON字符串。 |
