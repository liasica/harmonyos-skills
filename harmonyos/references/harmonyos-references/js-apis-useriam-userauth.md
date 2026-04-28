---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth
title: @ohos.userIAM.userAuth (用户认证)
breadcrumb: API参考 > 系统 > 安全 > User Authentication Kit（用户认证服务） > ArkTS API > @ohos.userIAM.userAuth (用户认证)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:44d7fe04d54b0650f29334ad15ae8482d9dd37b4985bd78054795663d9016603
---

提供用户认证能力，应用于设备解锁、支付、应用登录等场景。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { userAuth } from '@kit.UserAuthenticationKit';
```

## 常量

PhonePC/2in1TabletWearable

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| MAX\_ALLOWABLE\_REUSE\_DURATION12+ | number | 300000 | 复用解锁认证结果最大有效时长，值为300000毫秒。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PERMANENT\_LOCKOUT\_DURATION22+ | number | 0x7fffffff | 永久冻结时间，值为0x7fffffff毫秒。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## AuthLockState22+

PhonePC/2in1TabletWearable

认证类型的身份认证冻结状态。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLocked | boolean | 否 | 否 | 表示认证是否已被冻结。true表示已冻结；false表示未冻结。 |
| remainingAuthAttempts | number | 否 | 否 | 认证未被冻结时的剩余尝试次数，最大为5次。 |
| lockoutDuration | number | 否 | 否 | 认证被冻结时的剩余冻结时间，单位为毫秒。  当永久冻结时，值为PERMANENT\_LOCKOUT\_DURATION，需要PIN认证解锁。 |

## UserAuthTipCode20+

PhonePC/2in1TabletWearable

表示身份认证中间状态的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPARE\_FAILURE | 1 | 认证失败。 |
| TIMEOUT | 2 | 认证超时。 |
| TEMPORARILY\_LOCKED | 3 | 临时冻结。 |
| PERMANENTLY\_LOCKED | 4 | 永久冻结。 |
| WIDGET\_LOADED | 5 | 身份认证界面加载完毕。 |
| WIDGET\_RELEASED | 6 | 当前的身份认证界面退出，切换其他认证界面或身份认证控件关闭。 |
| COMPARE\_FAILURE\_WITH\_FROZEN | 7 | 认证失败并触发了认证冻结。 |

## EnrolledState12+

PhonePC/2in1TabletWearable

用户注册凭据的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialDigest | number | 否 | 否 | 注册的凭据摘要，在凭据增加时随机生成。 |
| credentialCount | number | 否 | 否 | 注册的凭据数量。 |

## ReuseMode12+

PhonePC/2in1TabletWearable

复用解锁认证结果的模式。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH\_TYPE\_RELEVANT | 1 | 与认证类型相关，只有当设备解锁认证结果在有效时间内，并且设备解锁的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUTH\_TYPE\_IRRELEVANT | 2 | 与认证类型无关，设备解锁认证结果在有效时间内，可以重复使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT14+ | 3 | 与认证类型相关，任意身份认证（包括设备解锁）结果在有效时间内，并且身份认证的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_IRRELEVANT14+ | 4 | 与认证类型无关，任意身份认证（包括设备解锁）结果在有效时间内，可以重复使用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## ReuseUnlockResult12+

PhonePC/2in1TabletWearable

复用解锁认证结果。

说明

如果身份认证解锁（包括设备解锁）后，在有效时间内凭据发生了变化，身份认证的结果依然可以复用，认证结果中返回当前实际的EnrolledState。若复用认证结果时，之前认证时所使用的身份认证凭据已经被删除，如果删除的是人脸、指纹，则认证结果依然可以复用，只是返回的EnrolledState中credentialCount和credentialDigest均为0；如果删除的是锁屏口令，则此次复用会失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reuseMode | [ReuseMode](js-apis-useriam-userauth.md#reusemode12) | 否 | 否 | 复用解锁认证结果的模式。 |
| reuseDuration | number | 否 | 否 | 允许复用解锁认证结果的有效时长，单位为毫秒。有效时长的值应大于0，最大值为[MAX\_ALLOWABLE\_REUSE\_DURATION](js-apis-useriam-userauth.md#常量)。 |

## userAuth.getAuthLockState22+

PhonePC/2in1TabletWearable

getAuthLockState(authType: UserAuthType): Promise<AuthLockState>

查询指定认证类型的冻结状态，使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthLockState](js-apis-useriam-userauth.md#authlockstate22)> | Promise对象，当查询成功时，返回值为指定认证类型的身份认证冻结状态。失败时报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500008 | The parameter is out of range. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let queryType = userAuth.UserAuthType.PIN;
5. let authLockState : userAuth.AuthLockState = {
6. isLocked : false,
7. remainingAuthAttempts : 0,
8. lockoutDuration : 0
9. }

11. userAuth.getAuthLockState(queryType)
12. .then((result: userAuth.AuthLockState) => {
13. authLockState = result;
14. console.info('get auth lock state successfully.');
15. })
16. .catch((err: BusinessError) => {
17. console.info(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
18. })
```

## userAuth.getEnrolledState12+

PhonePC/2in1TabletWearable

getEnrolledState(authType: UserAuthType): EnrolledState

查询凭据注册的状态，以检测用户注册凭据的变更。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EnrolledState](js-apis-useriam-userauth.md#enrolledstate12) | 当查询成功时，返回值为用户注册凭据的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
6. console.info('get current enrolled state successfully.');
7. } catch (error) {
8. const err: BusinessError = error as BusinessError;
9. console.error(`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}`);
10. }
```

## AuthParam10+

PhonePC/2in1TabletWearable

用户认证相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| challenge | Uint8Array | 否 | 否 | 随机挑战值，可用于防重放攻击。最大长度为32字节，可传Uint8Array([])。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8)[] | 否 | 否 | 认证类型列表，用来指定用户认证界面提供的认证方法。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 否 | 否 | 期望达到的认证可信等级。典型操作需要的身份认证可信等级，以及身份认证可信等级的划分请参见[认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| reuseUnlockResult12+ | [ReuseUnlockResult](js-apis-useriam-userauth.md#reuseunlockresult12) | 否 | 是 | 表示可以复用解锁认证的结果。默认为不复用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| skipLockedBiometricAuth20+ | boolean | 否 | 是 | 是否跳过已禁用的认证方式自动切换至其它方式的认证。若无可切换的认证方式则关闭控件，返回认证冻结错误码。  true表示生物认证冻结时，跳过倒计时界面直接切换到其他方式的认证；  false表示不跳过；默认为false。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## WidgetParam10+

PhonePC/2in1TabletWearable

用户认证界面配置相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 用户认证界面的标题，建议传入认证目的，例如用于支付、登录应用等，不支持传空字串，最大长度为500字符。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navigationButtonText | string | 否 | 是 | 导航按键的说明文本，最大长度为60字符。在单指纹、单人脸场景下支持，从API 18开始，增加支持人脸+指纹场景。默认为不展示自定义导航按键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uiContext18+ | Context | 否 | 是 | 以模应用弹窗方式显示身份认证对话框，仅支持在2in1设备上使用，如果没有此参数或其他类型的设备，身份认证对话框将以模系统弹窗方式显示。 默认以模系统弹窗方式显示身份认证对话框。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## UserAuthResult10+

PhonePC/2in1TabletWearable

用户认证结果。认证成功时，返回认证类型和认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 用户认证结果。若成功返回SUCCESS，若失败返回相应错误码，参见[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)。 |
| token | Uint8Array | 否 | 是 | 认证成功时，返回认证成功的令牌信息。最大长度为1024字节。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 否 | 是 | 认证成功时，返回认证类型。 |
| enrolledState12+ | [EnrolledState](js-apis-useriam-userauth.md#enrolledstate12) | 否 | 是 | 认证成功时，返回注册凭据的状态。 |

## IAuthCallback10+

PhonePC/2in1TabletWearable

返回认证结果的回调对象。

### onResult10+

PhonePC/2in1TabletWearable

onResult(result: UserAuthResult): void

回调函数，返回认证结果。认证成功时，可以通过UserAuthResult获取到认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [UserAuthResult](js-apis-useriam-userauth.md#userauthresult10) | 是 | 认证结果。 |

**示例1：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令认证，获取认证结果。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };

29. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
30. console.info('get userAuth instance successfully.');
31. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
32. userAuthInstance.on('result', {
33. onResult (result) {
34. console.info(`userAuthInstance callback result = ${result.result}`);
35. }
36. });
37. console.info('auth on successfully.');
38. userAuthInstance.start();
39. console.info('auth start successfully.');
40. } catch (error) {
41. const err: BusinessError = error as BusinessError;
42. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
43. }
```

**示例2：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+认证类型相关+复用设备解锁最大有效时长认证，获取认证结果。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. let reuseUnlockResult: userAuth.ReuseUnlockResult = {
6. reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
7. reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
8. }
9. try {
10. const rand = cryptoFramework.createRandom();
11. const len: number = 16;
12. let randData: Uint8Array | null = null;
13. let retryCount = 0;
14. while(retryCount < 3){
15. randData = rand?.generateRandomSync(len)?.data;
16. if(randData){
17. break;
18. }
19. retryCount++;
20. }
21. if(!randData){
22. return;
23. }
24. const authParam: userAuth.AuthParam = {
25. challenge: randData,
26. authType: [userAuth.UserAuthType.PIN],
27. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
28. reuseUnlockResult: reuseUnlockResult,
29. };
30. const widgetParam: userAuth.WidgetParam = {
31. title: '请输入密码',
32. };
33. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
34. console.info('get userAuth instance successfully.');
35. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
36. userAuthInstance.on('result', {
37. onResult (result) {
38. console.info(`userAuthInstance callback result = ${result.result}`);
39. }
40. });
41. console.info('auth on successfully.');
42. userAuthInstance.start();
43. console.info('auth start successfully.');
44. } catch (error) {
45. const err: BusinessError = error as BusinessError;
46. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
47. }
```

**示例3：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+任意应用认证类型相关+复用任意应用最大有效时长认证，获取认证结果。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. let reuseUnlockResult: userAuth.ReuseUnlockResult = {
6. reuseMode: userAuth.ReuseMode.CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT,
7. reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
8. }
9. try {
10. const rand = cryptoFramework.createRandom();
11. const len: number = 16;
12. let randData: Uint8Array | null = null;
13. let retryCount = 0;
14. while(retryCount < 3){
15. randData = rand?.generateRandomSync(len)?.data;
16. if(randData){
17. break;
18. }
19. retryCount++;
20. }
21. if(!randData){
22. return;
23. }
24. const authParam: userAuth.AuthParam = {
25. challenge: randData,
26. authType: [userAuth.UserAuthType.PIN],
27. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
28. reuseUnlockResult: reuseUnlockResult,
29. };
30. const widgetParam: userAuth.WidgetParam = {
31. title: '请输入密码',
32. };
33. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
34. console.info('get userAuth instance successfully.');
35. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
36. userAuthInstance.on('result', {
37. onResult (result) {
38. console.info(`userAuthInstance callback result = ${result.result}`);
39. }
40. });
41. console.info('auth on successfully.');
42. userAuthInstance.start();
43. console.info('auth start successfully.');
44. } catch (error) {
45. const err: BusinessError = error as BusinessError;
46. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
47. }
```

## AuthTipInfo20+

PhonePC/2in1TabletWearable

用户认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tipType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 否 | 否 | 中间状态对应的认证类型。 |
| tipCode | [UserAuthTipCode](js-apis-useriam-userauth.md#userauthtipcode20) | 否 | 否 | 中间状态值。 |

## AuthTipCallback20+

PhonePC/2in1TabletWearable

type AuthTipCallback = (authTipInfo: AuthTipInfo) => void

回调函数，返回认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authTipInfo | [AuthTipInfo](js-apis-useriam-userauth.md#authtipinfo20) | 是 | 认证中间状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };

29. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
30. console.info('get userAuth instance successfully.');
31. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
32. userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
33. console.info('userAuthInstance callback');
34. });
35. console.info('auth on successfully.');
36. userAuthInstance.start();
37. console.info('auth start successfully.');
38. } catch (error) {
39. const err: BusinessError = error as BusinessError;
40. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
41. }
```

## UserAuthInstance10+

PhonePC/2in1TabletWearable

用于执行用户身份认证，并支持使用统一用户身份认证控件。

使用以下接口前，需先通过[getUserAuthInstance](js-apis-useriam-userauth.md#userauthgetuserauthinstance10)方法获取UserAuthInstance对象。

### on('result')10+

PhonePC/2in1TabletWearable

on(type: 'result', callback: IAuthCallback): void

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证失败尝试并不会通过该接口返回。如果需要感知整个认证过程中用户的每一次认证失败尝试，请通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅。

说明

在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](js-apis-useriam-userauth.md#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10) | 是 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |

**示例1：**

以模系统弹窗方式进行用户身份认证。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
31. userAuthInstance.on('result', {
32. onResult (result) {
33. console.info(`userAuthInstance callback result = ${result.result}`);
34. }
35. });
36. console.info('auth on successfully.');
37. userAuthInstance.start();
38. console.info('auth start successfully.');
39. } catch (error) {
40. const err: BusinessError = error as BusinessError;
41. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
42. }
```

**示例2：**

以模应用弹窗方式进行用户身份认证。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. @Entry
6. @Component
7. struct Index {
8. modelApplicationAuth(): void {
9. try {
10. const rand = cryptoFramework.createRandom();
11. const len: number = 16;
12. let randData: Uint8Array | null = null;
13. let retryCount = 0;
14. while(retryCount < 3){
15. randData = rand?.generateRandomSync(len)?.data;
16. if(randData){
17. break;
18. }
19. retryCount++;
20. }
21. if(!randData){
22. return;
23. }
24. const authParam: userAuth.AuthParam = {
25. challenge: randData,
26. authType: [userAuth.UserAuthType.PIN],
27. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
28. };
29. const uiContext: UIContext = this.getUIContext();
30. const context: Context | undefined = uiContext.getHostContext();
31. const widgetParam: userAuth.WidgetParam = {
32. title: '请输入密码',
33. uiContext: context,
34. };
35. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
36. console.info('get userAuth instance successfully.');
37. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
38. userAuthInstance.on('result', {
39. onResult (result) {
40. console.info(`userAuthInstance callback result =${result.result}`);
41. }
42. });
43. console.info('auth on successfully.');
44. userAuthInstance.start();
45. console.info('auth start successfully.');
46. } catch (error) {
47. const err: BusinessError = error as BusinessError;
48. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
49. }
50. }

52. build() {
53. Column() {
54. Button('start auth')
55. .onClick(() => {
56. this.modelApplicationAuth();
57. })
58. }
59. }
60. }
```

### off('result')10+

PhonePC/2in1TabletWearable

off(type: 'result', callback?: IAuthCallback): void

取消订阅用户身份认证的结果。

说明

需要使用已经成功订阅事件的[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10) | 否 | 认证接口的回调函数，用于返回认证结果。当不传该参数时默认值为调用[on('result')](js-apis-useriam-userauth.md#onresult10-1)接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. userAuthInstance.off('result', {
31. onResult (result) {
32. console.info(`auth off result = ${result.result}`);
33. }
34. });
35. console.info('auth off successfully.');
36. } catch (error) {
37. const err: BusinessError = error as BusinessError;
38. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
39. }
```

### start10+

PhonePC/2in1TabletWearable

start(): void

开始认证。

说明

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC 或 ohos.permission.USER\_AUTH\_FROM\_BACKGROUND（仅向系统应用开放）

从API 20开始，仅系统应用可以通过申请ohos.permission.USER\_AUTH\_FROM\_BACKGROUND，在后台发起认证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Possible causes:  1.No permission to access biometric.  2.No permission to start authentication from background. |
| 401 | Parameter error. Possible causes:  1.Incorrect parameter types. |
| 12500002 | General operation error. |
| 12500003 | Authentication canceled. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500009 | Authentication is locked out. |
| 12500010 | The type of credential has not been enrolled. |
| 12500011 | Switched to the customized authentication process. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. userAuthInstance.start();
31. console.info('auth start successfully.');
32. } catch (error) {
33. const err: BusinessError = error as BusinessError;
34. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
35. }
```

### cancel10+

PhonePC/2in1TabletWearable

cancel(): void

取消认证。

说明

此时UserAuthInstance必须是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Incorrect parameter types. |
| 12500002 | General operation error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam : userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. // 需要调用UserAuthInstance的start()接口，启动认证后，才能调用cancel()接口。
31. userAuthInstance.start();
32. console.info('auth start successfully.');
33. userAuthInstance.cancel();
34. console.info('auth cancel successfully.');
35. } catch (error) {
36. const err: BusinessError = error as BusinessError;
37. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
38. }
```

### on('authTip')20+

PhonePC/2in1TabletWearable

on(type: 'authTip', callback: AuthTipCallback): void

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证失败尝试。使用callback异步回调。

说明

在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](js-apis-useriam-userauth.md#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件类型，支持的事件为'authTip'，当[start()](js-apis-useriam-userauth.md#start10)调用完成，发起身份认证，触发该事件。 |
| callback | [AuthTipCallback](js-apis-useriam-userauth.md#authtipcallback20) | 是 | 认证接口的回调函数，用于返回认证中间状态。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
31. userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
32. console.info('userAuthInstance callback.');
33. });
34. console.info('auth on successfully.');
35. userAuthInstance.start();
36. console.info('auth start successfully.');
37. } catch (error) {
38. const err: BusinessError = error as BusinessError;
39. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
40. }
```

### off('authtip')20+

PhonePC/2in1TabletWearable

off(type: 'authTip', callback?: AuthTipCallback): void

取消订阅用户身份认证中间状态。

说明

需要使用已经成功订阅事件的[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型，支持的事件为'authTip'，当[start()](js-apis-useriam-userauth.md#start10)调用完成，发起身份认证并调用[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)订阅该事件后，调用该方法可取消订阅，不会再触发该事件。 |
| callback | [AuthTipCallback](js-apis-useriam-userauth.md#authtipcallback20) | 否 | 认证接口的回调函数，用于返回认证中间状态。 当不传该参数时默认值为调用[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
31. console.info('userAuthInstance callback');
32. });
33. console.info('auth off successfully.');
34. } catch (error) {
35. const err: BusinessError = error as BusinessError;
36. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
37. }
```

## userAuth.getUserAuthInstance10+

PhonePC/2in1TabletWearable

getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance

获取[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象，执行用户身份认证，并支持使用统一用户身份认证控件。

说明

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authParam | [AuthParam](js-apis-useriam-userauth.md#authparam10) | 是 | 用户认证相关参数。 |
| widgetParam | [WidgetParam](js-apis-useriam-userauth.md#widgetparam10) | 是 | 用户认证界面配置相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10) | 支持用户界面的认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { userAuth } from '@kit.UserAuthenticationKit';

5. try {
6. const rand = cryptoFramework.createRandom();
7. const len: number = 16;
8. let randData: Uint8Array | null = null;
9. let retryCount = 0;
10. while(retryCount < 3){
11. randData = rand?.generateRandomSync(len)?.data;
12. if(randData){
13. break;
14. }
15. retryCount++;
16. }
17. if(!randData){
18. return;
19. }
20. const authParam: userAuth.AuthParam = {
21. challenge: randData,
22. authType: [userAuth.UserAuthType.PIN],
23. authTrustLevel: userAuth.AuthTrustLevel.ATL3,
24. };
25. const widgetParam: userAuth.WidgetParam = {
26. title: '请输入密码',
27. };
28. let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
29. console.info('get userAuth instance successfully.');
30. } catch (error) {
31. const err: BusinessError = error as BusinessError;
32. console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
33. }
```

## AuthResultInfo(deprecated)

PhonePC/2in1TabletWearable

表示认证结果信息，用于描述认证结果。

说明

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](js-apis-useriam-userauth.md#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 认证结果。 |
| token | Uint8Array | 否 | 是 | 用户身份认证通过的凭证。 |
| remainAttempts | number | 否 | 是 | 剩余的认证尝试次数。 |
| lockoutDuration | number | 否 | 是 | 认证操作的锁定时长，时间单位为毫秒ms。 |

## TipInfo(deprecated)

PhonePC/2in1TabletWearable

表示认证过程中的提示信息，用于提供认证过程的反馈。

说明

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[AuthTipInfo](js-apis-useriam-userauth.md#authtipinfo20)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| module | number | 否 | 否 | 发送提示信息的模块标识。 |
| tip | number | 否 | 否 | 认证过程提示信息。 |

## EventInfo(deprecated)

PhonePC/2in1TabletWearable

type EventInfo = AuthResultInfo | TipInfo

表示认证过程中事件信息的类型。

该类型为下表类型取值中的联合类型。

说明

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](js-apis-useriam-userauth.md#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| [AuthResultInfo](js-apis-useriam-userauth.md#authresultinfodeprecated) | 获取到的认证结果信息。 |
| [TipInfo](js-apis-useriam-userauth.md#tipinfodeprecated) | 认证过程中的提示信息。 |

## AuthEventKey(deprecated)

PhonePC/2in1TabletWearable

type AuthEventKey = 'result' | 'tip'

表示认证事件类型的关键字，作为[on](js-apis-useriam-userauth.md#ondeprecated)接口的参数。

该类型为下表类型取值中的联合类型。

说明

从 API version 9 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| 'result' | [on](js-apis-useriam-userauth.md#ondeprecated)接口第一个参数为"result"时，[callback](js-apis-useriam-userauth.md#callbackdeprecated)回调返回认证的结果信息。 |
| 'tip' | [on](js-apis-useriam-userauth.md#ondeprecated)接口第一个参数为"tip"时，[callback](js-apis-useriam-userauth.md#callbackdeprecated)回调返回认证操作中的提示信息。 |

## AuthEvent(deprecated)

PhonePC/2in1TabletWearable

认证接口的异步回调对象。

说明

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10)替代。

### callback(deprecated)

PhonePC/2in1TabletWearable

callback(result : EventInfo) : void

通过该回调获取认证结果信息或认证过程中的提示信息。

说明

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[onResult](js-apis-useriam-userauth.md#onresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [EventInfo](js-apis-useriam-userauth.md#eventinfodeprecated) | 是 | 返回的认证结果信息或提示信息。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
6. // 通过callback获取认证结果。
7. try {
8. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
9. auth.on('result', {
10. callback: (result: userAuth.AuthResultInfo) => {
11. console.info(`result: ${result.result}`);
12. }
13. } as userAuth.AuthEvent);
14. auth.start();
15. console.info('auth start successfully.');
16. } catch (error) {
17. console.error(`auth failed, error = ${error}`);
18. // do error.
19. }
20. // 通过callback获取认证过程中的提示信息。
21. try {
22. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
23. auth.on('tip', {
24. callback : (result : userAuth.TipInfo) => {
25. switch (result.tip) {
26. case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
27. // do something;
28. break;
29. case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
30. // do something;
31. break;
32. default:
33. // do others.
34. }
35. }
36. } as userAuth.AuthEvent);
37. auth.start();
38. console.info('auth start successfully.');
39. } catch (error) {
40. console.error(`auth failed, error = ${error}`);
41. // do error.
42. }
```

## AuthInstance(deprecated)

PhonePC/2in1TabletWearable

执行用户认证的对象。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)替代。

### on(deprecated)

PhonePC/2in1TabletWearable

on : (name : AuthEventKey, callback : AuthEvent) => void

订阅指定类型的用户认证事件。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[on('result')](js-apis-useriam-userauth.md#onresult10-1)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [AuthEventKey](js-apis-useriam-userauth.md#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，回调函数返回认证结果；取值为"tip"时，回调函数返回认证过程中的提示信息。 |
| callback | [AuthEvent](js-apis-useriam-userauth.md#autheventdeprecated) | 是 | 认证接口的回调函数，用于返回认证结果或认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
6. try {
7. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
8. // 订阅认证结果。
9. auth.on('result', {
10. callback: (result: userAuth.AuthResultInfo) => {
11. console.info(`result: ${result.result}`);
12. }
13. });
14. // 订阅认证过程中的提示信息。
15. auth.on('tip', {
16. callback : (result : userAuth.TipInfo) => {
17. switch (result.tip) {
18. case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
19. // do something;
20. break;
21. case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
22. // do something;
23. break;
24. default:
25. // do others.
26. }
27. }
28. } as userAuth.AuthEvent);
29. auth.start();
30. console.info('auth start successfully.');
31. } catch (error) {
32. console.error(`auth failed, error = ${error}`);
33. // do error.
34. }
```

### off(deprecated)

PhonePC/2in1TabletWearable

off : (name : AuthEventKey) => void

取消订阅特定类型的认证事件。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[off('result')](js-apis-useriam-userauth.md#offresult10)替代。

需要使用已经成功订阅事件的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行取消订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [AuthEventKey](js-apis-useriam-userauth.md#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，取消订阅认证结果；取值为"tip"时，取消订阅认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
6. try {
7. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
8. // 订阅认证结果。
9. auth.on('result', {
10. callback: (result: userAuth.AuthResultInfo) => {
11. console.info(`result: ${result.result}`);
12. }
13. });
14. // 取消订阅结果。
15. auth.off('result');
16. console.info('cancel subscribe authentication event successfully.');
17. } catch (error) {
18. console.error(`cancel subscribe authentication event failed, error = ${error}`);
19. // do error.
20. }
```

### start(deprecated)

PhonePC/2in1TabletWearable

start : () => void

开始认证。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[start](js-apis-useriam-userauth.md#start10)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行认证。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500001 | Authentication failed. |
| 12500002 | General operation error. |
| 12500003 | The operation is canceled. |
| 12500004 | The operation is time-out. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | The authentication task is busy. |
| 12500009 | The authenticator is locked. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

7. try {
8. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
9. auth.start();
10. console.info('auth start successfully.');
11. } catch (error) {
12. console.error(`auth failed, error = ${error}`);
13. }
```

### cancel(deprecated)

PhonePC/2in1TabletWearable

cancel : () => void

取消认证。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[cancel](js-apis-useriam-userauth.md#cancel10)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行取消认证，此[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)需要是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

7. try {
8. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
9. auth.cancel();
10. console.info('cancel auth successfully.');
11. } catch (error) {
12. console.error(`auth failed, error = ${error}`);
13. }
```

## userAuth.getAuthInstance(deprecated)

PhonePC/2in1TabletWearable

getAuthInstance(challenge : Uint8Array, authType : UserAuthType, authTrustLevel : AuthTrustLevel): AuthInstance

获取AuthInstance对象，用于执行用户身份认证。

说明

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[getUserAuthInstance](js-apis-useriam-userauth.md#userauthgetuserauthinstance10)替代。

每个AuthInstance只能进行一次认证，若需要再次进行认证则需重新获取AuthInstance。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，最大长度为32字节，可以传Uint8Array([])。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated) | 认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
4. let authType = userAuth.UserAuthType.FACE;
5. let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

7. try {
8. let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
9. console.info('get auth instance successfully.');
10. } catch (error) {
11. console.error(`get auth instance failed, error = ${error}`);
12. }
```

## userAuth.getAvailableStatus9+

PhonePC/2in1TabletWearable

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void

查询指定类型和等级的认证能力是否支持。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。从 API version 11 开始支持PIN查询。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |

说明

如果未注册对应执行器，系统不支持该认证能力，需返回12500005。

如果已注册对应执行器，功能未禁用，但认证安全等级低于业务指定时，需返回12500006。

如果已注册对应执行器，功能未禁用，但用户未注册凭据时，需返回12500010。

如果已注册对应执行器，功能未禁用，但密码过期时，需返回12500013。

注意

若用户注册的锁屏口令是4位PIN时，其认证可信等级为ATL3，调用该接口查询是否支持ATL4级别的密码认证时，需返回12500010。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500010 | The type of credential has not been enrolled. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. try {
4. userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
5. console.info('current auth trust level is supported');
6. } catch (error) {
7. console.error(`current auth trust level is not supported, error = ${error}`);
8. }
```

## UserAuthResultCode9+

PhonePC/2in1TabletWearable

表示返回码的枚举。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 12500000 | 执行成功。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FAIL | 12500001 | 认证失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| GENERAL\_ERROR | 12500002 | 操作通用错误。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED | 12500003 | 认证取消。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TIMEOUT | 12500004 | 认证超时。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_NOT\_SUPPORT | 12500005 | 认证类型不支持。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 12500006 | 认证等级不支持。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BUSY | 12500007 | 系统繁忙。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INVALID\_PARAMETERS20+ | 12500008 | 参数校验失败。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| LOCKED | 12500009 | 认证器已锁定。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NOT\_ENROLLED | 12500010 | 用户未录入指定的系统身份认证凭据。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED\_FROM\_WIDGET10+ | 12500011 | 用户取消了系统认证方式，选择应用自定义认证。需调用者拉起自定义认证界面。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PIN\_EXPIRED12+ | 12500013 | 当前的认证操作执行失败。返回这个错误码，表示系统锁屏口令过期。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## UserAuth(deprecated)

PhonePC/2in1TabletWearable

认证器对象。

### constructor(deprecated)

PhonePC/2in1TabletWearable

constructor()

创建认证器对象。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAuthInstance](js-apis-useriam-userauth.md#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
```

### getVersion(deprecated)

PhonePC/2in1TabletWearable

getVersion() : number

获取认证器的版本信息。

说明

从 API version 8 开始支持，从 API version 9 开始废弃。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 认证器版本信息。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
4. let version = auth.getVersion();
5. console.info(`auth version = ${version}`);
```

### getAvailableStatus(deprecated)

PhonePC/2in1TabletWearable

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel) : number

查询指定类型和等级的认证能力是否支持。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAvailableStatus](js-apis-useriam-userauth.md#userauthgetavailablestatus9)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 查询结果，结果为SUCCESS时表示支持，其他返回值参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
4. let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
5. if (checkCode == userAuth.ResultCode.SUCCESS) {
6. console.info('check auth support successfully.');
7. } else {
8. console.error(`check auth support failed, code = ${checkCode}`);
9. }
```

### auth(deprecated)

PhonePC/2in1TabletWearable

auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array

执行用户认证，使用回调函数返回结果。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，可以传Uint8Array([])。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |
| callback | [IUserAuthCallback](js-apis-useriam-userauth.md#iuserauthcallbackdeprecated) | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | ContextId，作为取消认证[cancelAuth](js-apis-useriam-userauth.md#cancelauthdeprecated)接口的入参。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
4. let challenge = new Uint8Array([]);
5. auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
6. onResult: (result, extraInfo) => {
7. try {
8. console.info(`auth onResult result = ${result}`);
9. if (result == userAuth.ResultCode.SUCCESS) {
10. // 此处添加认证成功逻辑。
11. } else {
12. // 此处添加认证失败逻辑。
13. }
14. } catch (error) {
15. console.error(`auth onResult failed, error = ${error}`);
16. }
17. }
18. });
```

### cancelAuth(deprecated)

PhonePC/2in1TabletWearable

cancelAuth(contextID : Uint8Array) : number

表示通过contextID取消本次认证。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[cancel](js-apis-useriam-userauth.md#canceldeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contextID | Uint8Array | 是 | 上下文的标识，通过[auth](js-apis-useriam-userauth.md#authdeprecated)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 取消认证的结果，结果为SUCCESS时表示取消成功，其他返回值参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. // contextId可通过auth接口获取，此处直接定义。
4. let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
5. let auth = new userAuth.UserAuth();
6. let cancelCode = auth.cancelAuth(contextId);
7. if (cancelCode == userAuth.ResultCode.SUCCESS) {
8. console.info('cancel auth successfully.');
9. } else {
10. console.error('cancel auth failed.');
11. }
```

## IUserAuthCallback(deprecated)

PhonePC/2in1TabletWearable

返回认证结果的回调对象。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthEvent](js-apis-useriam-userauth.md#autheventdeprecated)代替。

### onResult(deprecated)

PhonePC/2in1TabletWearable

onResult: (result : number, extraInfo : AuthResult) => void

回调函数，返回认证结果。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](js-apis-useriam-userauth.md#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | number | 是 | 认证结果，参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |
| extraInfo | [AuthResult](js-apis-useriam-userauth.md#authresultdeprecated) | 是 | 扩展信息，不同情况下的具体信息，  如果身份验证通过，则在extraInfo中返回用户认证令牌，  如果身份验证失败，则在extraInfo中返回剩余的用户认证次数，  如果身份验证执行器被锁定，则在extraInfo中返回冻结时间。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
4. let challenge = new Uint8Array([]);
5. auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
6. onResult: (result, extraInfo) => {
7. try {
8. console.info(`auth onResult result = ${result}`);
9. if (result == userAuth.ResultCode.SUCCESS) {
10. // 此处添加认证成功逻辑。
11. }  else {
12. // 此处添加认证失败逻辑。
13. }
14. } catch (error) {
15. console.error(`auth onResult failed, error = ${error}`);
16. }
17. }
18. });
```

### onAcquireInfo(deprecated)

PhonePC/2in1TabletWearable

onAcquireInfo ?: (module : number, acquire : number, extraInfo : any) => void

回调函数，返回认证过程中的提示信息，非必须实现。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](js-apis-useriam-userauth.md#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| module | number | 是 | 发送提示信息的模块标识。 |
| acquire | number | 是 | 认证执过程中的提示信息。 |
| extraInfo | any | 是 | 预留字段。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let auth = new userAuth.UserAuth();
4. let challenge = new Uint8Array([]);
5. auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
6. onResult: (result, extraInfo) => {
7. try {
8. console.info(`auth onResult result = ${result}`);
9. if (result == userAuth.ResultCode.SUCCESS) {
10. // 此处添加认证成功逻辑。
11. }  else {
12. // 此处添加认证失败逻辑。
13. }
14. } catch (error) {
15. console.error(`auth onResult failed, error = ${error}`);
16. }
17. },
18. onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
19. try {
20. console.info('auth onAcquireInfo successfully.');
21. } catch (error) {
22. console.error(`auth onAcquireInfo failed, error = ${error}`);
23. }
24. }
25. });
```

## AuthResult(deprecated)

PhonePC/2in1TabletWearable

表示认证结果的对象。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthResultInfo](js-apis-useriam-userauth.md#authresultinfodeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| token | Uint8Array | 否 | 是 | 认证成功的令牌信息。 |
| remainTimes | number | 否 | 是 | 剩余的认证操作次数。 |
| freezingTime | number | 否 | 是 | 认证操作的冻结时间。单位为毫秒。 |

## ResultCode(deprecated)

PhonePC/2in1TabletWearable

表示返回码的枚举。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAIL | 1 | 认证失败。 |
| GENERAL\_ERROR | 2 | 操作通用错误。 |
| CANCELED | 3 | 操作取消。 |
| TIMEOUT | 4 | 操作超时。 |
| TYPE\_NOT\_SUPPORT | 5 | 不支持的认证类型。 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 6 | 不支持的认证等级。 |
| BUSY | 7 | 忙碌状态。 |
| INVALID\_PARAMETERS | 8 | 无效参数。 |
| LOCKED | 9 | 认证器已锁定。 |
| NOT\_ENROLLED | 10 | 用户未录入认证信息。 |

## FaceTips(deprecated)

PhonePC/2in1TabletWearable

表示人脸认证过程中提示码的枚举。

说明

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FACE\_AUTH\_TIP\_TOO\_BRIGHT | 1 | 光线太强，获取的图像太亮。 |
| FACE\_AUTH\_TIP\_TOO\_DARK | 2 | 光线太暗，获取的图像太暗。 |
| FACE\_AUTH\_TIP\_TOO\_CLOSE | 3 | 人脸距离设备过近。 |
| FACE\_AUTH\_TIP\_TOO\_FAR | 4 | 人脸距离设备过远。 |
| FACE\_AUTH\_TIP\_TOO\_HIGH | 5 | 设备太高，仅获取到人脸上部。 |
| FACE\_AUTH\_TIP\_TOO\_LOW | 6 | 设备太低，仅获取到人脸下部。 |
| FACE\_AUTH\_TIP\_TOO\_RIGHT | 7 | 设备太靠右，仅获取到人脸右部。 |
| FACE\_AUTH\_TIP\_TOO\_LEFT | 8 | 设备太靠左，仅获取到人脸左部。 |
| FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION | 9 | 在图像采集过程中，用户人脸移动太快。 |
| FACE\_AUTH\_TIP\_POOR\_GAZE | 10 | 没有正视摄像头。 |
| FACE\_AUTH\_TIP\_NOT\_DETECTED | 11 | 没有检测到人脸信息。 |

## FingerprintTips(deprecated)

PhonePC/2in1TabletWearable

表示指纹认证过程中提示码的枚举。

说明

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINGERPRINT\_AUTH\_TIP\_GOOD | 0 | 获取的指纹图像良好。 |
| FINGERPRINT\_AUTH\_TIP\_DIRTY | 1 | 由于传感器上可疑或检测到的污垢，指纹图像噪音过大。 |
| FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT | 2 | 由于检测到的情况，指纹图像噪声太大，无法处理。 |
| FINGERPRINT\_AUTH\_TIP\_PARTIAL | 3 | 仅检测到部分指纹图像。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_FAST | 4 | 快速移动，指纹图像不完整。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW | 5 | 缺少运动，指纹图像无法读取。 |

## UserAuthType8+

PhonePC/2in1TabletWearable

表示身份认证的凭据类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PIN10+ | 1 | 口令认证。 |
| FACE | 2 | 人脸认证。 |
| FINGERPRINT | 4 | 指纹认证。 |

## AuthTrustLevel8+

PhonePC/2in1TabletWearable

表示认证结果的信任等级枚举。

典型场景及举例可参考[认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATL1 | 10000 | 认证结果的信任等级级别1，表示该认证方案能够识别用户个体，具备一定的活体检测能力。适用于业务风控、一般个人数据查询等场景。 |
| ATL2 | 20000 | 认证结果的信任等级级别2，表示该认证方案能够精确识别用户个体，具备一定的活体检测能力。适用于维持设备解锁状态、应用登录等场景。 |
| ATL3 | 30000 | 认证结果的信任等级级别3，表示该认证方案能够精确识别用户个体，具备较强的活体检测能力。适用于设备解锁等场景。 |
| ATL4 | 40000 | 认证结果的信任等级级别4，表示该认证方案能够高精度的识别用户个体，具备很强的活体检测能力。适用于小额支付等场景。 |

## SecureLevel(deprecated)

PhonePC/2in1TabletWearable

type SecureLevel = string

表示认证的安全级别。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示类型为字符，认证的安全级别包括：'S1' | 'S2'|'S3'|'S4'。  - 'S1'：认证结果的信任等级级别1，代表该认证方案能够识别用户个体，有一定的活体检测能力。常用的业务场景有业务风控、一般个人数据查询等。  - 'S2'：认证结果的信任等级级别2，代表该认证方案能够精确识别用户个体，有一定的活体检测能力。常用的业务场景有维持设备解锁状态，应用登录等。  - 'S3'：认证结果的信任等级级别3，代表该认证方案能够精确识别用户个体，有较强的活体检测能力。常用的业务场景有设备解锁等。  - 'S4'：认证结果的信任等级级别4，代表该认证方案能够高精度的识别用户个体，有很强的活体检测能力。常用的业务场景有小额支付等。 |

## AuthType(deprecated)

PhonePC/2in1TabletWearable

type AuthType = string

表示认证类型。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthType](js-apis-useriam-userauth.md#userauthtype8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示认证类型为字符，认证类型包括：'ALL'|'FACE\_ONLY'。  - 'ALL'：预留参数，当前版本暂不支持ALL类型的认证。  - 'FACE\_ONLY'：人脸认证。 |

## userAuth.getAuthenticator(deprecated)

PhonePC/2in1TabletWearable

getAuthenticator(): Authenticator

获取Authenticator对象，用于执行用户身份认证。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[getAuthInstance](js-apis-useriam-userauth.md#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Authenticator](js-apis-useriam-userauth.md#authenticatordeprecated) | 认证器对象。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let authenticator = userAuth.getAuthenticator();
```

## Authenticator(deprecated)

PhonePC/2in1TabletWearable

认证器对象。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)替代。

### execute(deprecated)

PhonePC/2in1TabletWearable

execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void

执行用户认证，使用callback方式作为异步方法。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE\_ONLY"。  ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。  具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。  具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |
| callback | AsyncCallback<number> | 是 | 回调函数。number表示认证结果，参见[AuthenticationResult](js-apis-useriam-userauth.md#authenticationresultdeprecated)。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. let authenticator = userAuth.getAuthenticator();
4. authenticator.execute('FACE_ONLY', 'S2', (error, code)=>{
5. if (code === userAuth.ResultCode.SUCCESS) {
6. console.info('auth successfully.');
7. return;
8. }
9. console.error(`auth failed, code = ${code}`);
10. });
```

### execute(deprecated)

PhonePC/2in1TabletWearable

execute(type : AuthType, level : SecureLevel): Promise<number>

执行用户认证，使用promise方式作为异步方法。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE\_ONLY"。  ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。  具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。  具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回携带一个number的Promise。number 为认证结果，参见[AuthenticationResult](js-apis-useriam-userauth.md#authenticationresultdeprecated)。 |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';

3. try {
4. let authenticator = userAuth.getAuthenticator();
5. authenticator.execute('FACE_ONLY', 'S2').then((code)=>{
6. console.info('auth successfully.');
7. })
8. } catch (error) {
9. console.error(`auth failed, code = ${error}`);
10. }
```

## AuthenticationResult(deprecated)

PhonePC/2in1TabletWearable

表示认证结果的枚举。

说明

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_SUPPORT | -1 | 设备不支持当前的认证方式。 |
| SUCCESS | 0 | 认证成功。 |
| COMPARE\_FAILURE | 1 | 比对失败。 |
| CANCELED | 2 | 用户取消认证。 |
| TIMEOUT | 3 | 认证超时。 |
| CAMERA\_FAIL | 4 | 开启相机失败。 |
| BUSY | 5 | 认证服务忙，请稍后重试。 |
| INVALID\_PARAMETERS | 6 | 认证参数无效。 |
| LOCKED | 7 | 认证失败次数过多，已锁定。 |
| NOT\_ENROLLED | 8 | 未录入认证凭据。 |
| GENERAL\_ERROR | 100 | 其他错误。 |
