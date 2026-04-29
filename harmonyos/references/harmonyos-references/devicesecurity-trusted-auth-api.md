---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-trusted-auth-api
title: TrustedAuthentication（数字盾服务）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > TrustedAuthentication（数字盾服务）
category: harmonyos-references
scraped_at: 2026-04-29T13:57:42+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3bd97da591fa1fe3c60d0ce54c080ab606edcee487f95ec62e56bafef08851b9
---

本模块提供数字盾密码创建、修改、删除、交易认证，开通生物特征（3D人脸/指纹）交易认证能力、生物特征交易认证，密钥信息导入导出相关接口，金融应用可以使用对应接口，支撑数字盾业务开发。

**起始版本：** 6.0.0(20)

## 导入模块

Phone

```
1. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
```

## enableTrustedAuthentication

Phone

enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>

拉起TUI（Trusted User Interface）界面并指引用户创建数字盾密码。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 在发起请求之前通过[Universal Keystore Kit初始化会话](js-apis-huks.md#huksinitsession9)获取的challenge值，参数规格为32字节随机数。 |
| pwdInfo | [PasswordInfo](devicesecurity-trusted-auth-api.md#passwordinfo) | 是 | 密码对应的定制信息，详细信息参考PasswordInfo。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息，详见TUILable。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthInfo](devicesecurity-trusted-auth-api.md#authinfo)> | Promise对象，返回开通数字盾密码对应的authID和authToken信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100007 | Unsupported custom image. |
| 1019100008 | The user canceled the operation. |
| 1019100011 | The title text cannot be displayed. |
| 1019100013 | Failed to set the password. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. const TAG = "TrustedAuthenticationJsTest";
9. try {
10. const rand = cryptoFramework.createRandom();
11. const len: number = 32;
12. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
13. const passwordInfo: trustedAuthentication.PasswordInfo = {
14. pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_MIXED,
15. pwdMaxLength: 10,
16. pwdMinLength: 6,
17. maxAuthFailCount: 6
18. };
19. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
20. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
21. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
22. const buffer = fileData.buffer;
23. const label:trustedAuthentication.TUILable = {
24. image: buffer as ArrayBuffer,
25. title: "开通数字盾",
26. }
27. const authToken = await trustedAuthentication.enableTrustedAuthentication(challenge, passwordInfo, label);
28. } catch (err) {
29. let e: BusinessError = err as BusinessError;
30. hilog.error(0x0000, TAG, 'enableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
31. }
```

## modifyTrustedAuthenticationPwd

Phone

modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>

拉起TUI界面并指引用户修改数字盾密码，修改密码前会根据authID进行对应密码认证。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 在发起请求之前通过[Universal Keystore Kit初始化会话](js-apis-huks.md#huksinitsession9)获取的challenge值，参数规格为32字节随机数。 |
| pwdInfo | [PasswordInfo](devicesecurity-trusted-auth-api.md#passwordinfo) | 是 | 密码对应的定制信息。 |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthToken](devicesecurity-trusted-auth-api.md#authtoken)> | Promise对象，返回修改数字盾密码对应的authToken信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100003 | The maximum number of password authentication attempts has been reached. |
| 1019100005 | Face/Fingerprint/Password authentication failed. |
| 1019100007 | Unsupported custom image. |
| 1019100008 | The user canceled the operation. |
| 1019100011 | The title text cannot be displayed. |
| 1019100012 | Invalid authentication ID. |
| 1019100014 | Failed to change the password. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. const TAG = "TrustedAuthenticationJsTest";

10. try {
11. const rand = cryptoFramework.createRandom();
12. const len: number = 32;
13. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
14. const passwordInfo: trustedAuthentication.PasswordInfo = {
15. pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
16. pwdMaxLength: 10,
17. pwdMinLength: 6,
18. maxAuthFailCount: 6,
19. };
20. const authID: bigint = 1687413472599354502n;
21. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
22. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
23. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
24. const buffer = fileData.buffer;
25. const label:trustedAuthentication.TUILable = {
26. image: buffer as ArrayBuffer,
27. title: "修改密码",
28. }
29. const authToken = await trustedAuthentication.modifyTrustedAuthenticationPwd(challenge, passwordInfo, authID, label);
30. } catch (err) {
31. let e: BusinessError = err as BusinessError;
32. hilog.error(0x0000, TAG, 'modifyTrustedAuthenticationPwd failed: %{public}d %{public}s', e.code, e.message);
33. }
```

## disableTrustedAuthentication

Phone

disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>

关闭数字盾服务，开发者可通过参数needAuth控制密码关闭前是否需要密码认证。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 当needAuth为true时，在发起请求之前通过[Universal Keystore Kit初始化会话](js-apis-huks.md#huksinitsession9)获取的challenge值，参数规格为32字节随机数。  当needAuth为false时，该值可不从Universal Keystore Kit获取，challenge值为任意32字节数即可。 |
| needAuth | boolean | 是 | 是否需要进行密码认证标识。  当值为false时，表示不进行密码认证发起的数字盾服务关闭场景。  当值为true时，表示需要进行密码认证，密码认证通过后才可关闭数字盾服务。 |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthToken](devicesecurity-trusted-auth-api.md#authtoken)> | Promise对象，返回删除数字盾密码对应的authToken信息，当needAuth为false时，返回的authToken信息为全0无效的authToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100003 | The maximum number of password authentication attempts has been reached. |
| 1019100004 | Failed to delete the password. |
| 1019100005 | Face/Fingerprint/Password authentication failed. |
| 1019100007 | Unsupported custom image. |
| 1019100008 | The user canceled the operation. |
| 1019100011 | The title text cannot be displayed. |
| 1019100012 | Invalid authentication ID. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. const TAG = "TrustedAuthenticationJsTest";

10. try {
11. const rand = cryptoFramework.createRandom();
12. const len: number = 32;
13. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
14. const authID: bigint = 1687413472599354502n;
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
17. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
18. const buffer = fileData.buffer;
19. const label:trustedAuthentication.TUILable = {
20. image: buffer as ArrayBuffer,
21. title: "关闭数字盾",
22. }
23. const authToken = await trustedAuthentication.disableTrustedAuthentication(challenge, true, authID, label);
24. } catch (err) {
25. let e: BusinessError = err as BusinessError;
26. hilog.error(0x0000, TAG, 'disableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
27. }
```

## trustedAuthentication

Phone

trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>

提供数字盾密码认证能力，开发者可使用该接口完成绑定生物特征支付前的密码认证。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 在发起请求之前通过[Universal Keystore Kit初始化会话](js-apis-huks.md#huksinitsession9)获取的challenge值，参数规格为32字节随机数。 |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthToken](devicesecurity-trusted-auth-api.md#authtoken)> | Promise对象，返回数字盾密码认证对应的authToken信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100003 | The maximum number of password authentication attempts has been reached. |
| 1019100005 | Face/Fingerprint/Password authentication failed. |
| 1019100007 | Unsupported custom image. |
| 1019100008 | The user canceled the operation. |
| 1019100012 | Invalid authentication ID. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. const TAG = "TrustedAuthenticationJsTest";

10. try {
11. const rand = cryptoFramework.createRandom();
12. const len: number = 32;
13. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
14. const authID: bigint = 1687413472599354502n;
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
17. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
18. const buffer = fileData.buffer;
19. const label:trustedAuthentication.TUILable = {
20. image: buffer as ArrayBuffer,
21. title: "密码认证",
22. }
23. const authToken = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
24. } catch (err) {
25. let e: BusinessError = err as BusinessError;
26. hilog.error(0x0000, TAG, 'trustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
27. }
```

## procContentAuthentication

Phone

procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>

数字盾交易认证接口。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 在发起请求之前通过[Universal Keystore Kit初始化会话](js-apis-huks.md#huksinitsession9)获取的challenge值，参数规格为32字节随机数。 |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| authMsg | [AuthReqParams](devicesecurity-trusted-auth-api.md#authreqparams) | 是 | 交易认证请求相关参数。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthToken](devicesecurity-trusted-auth-api.md#authtoken)> | Promise对象。  当使用密码认证时，返回结果包括交易数据信息的authToken。  当使用生物特征进行认证时，返回结果为临时authToken，在经过生物认证通过后，需使用[getBiometricAuthToken](devicesecurity-trusted-auth-api.md#getbiometricauthtoken)获取正式签发的包含交易信息的authToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100005 | Face/Fingerprint/Password authentication failed. |
| 1019100008 | The user canceled the operation. |
| 1019100011 | The text content cannot be displayed. |
| 1019100012 | Invalid authentication ID. |
| 1019100021 | The corresponding biometric data has not been bound. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
5. import { resourceManager } from '@kit.LocalizationKit';
6. import { common } from '@kit.AbilityKit';

8. const TAG = "TrustedAuthenticationJsTest";

10. try {
11. const rand = cryptoFramework.createRandom();
12. const len: number = 32;
13. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
14. const authID: bigint = 1687413472599354502n;
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
17. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
18. const reqParams:trustedAuthentication.AuthReqParams = {
19. reqType: trustedAuthentication.AuthType.AUTH_TYPE_TUI_PIN,
20. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"],
21. }
22. const buffer = fileData.buffer;
23. const label:trustedAuthentication.TUILable = {
24. image: buffer as ArrayBuffer,
25. title: "密码交易认证",
26. }
27. const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
28. } catch (err) {
29. let e: BusinessError = err as BusinessError;
30. hilog.error(0x0000, TAG, 'procContentAuthentication failed: %{public}d %{public}s', e.code, e.message);
31. }
```

## getBiometricAuthToken

Phone

getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>

获取生物特征绑定/生物特征交易认证对应的authToken信息。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| operType | [OperateType](devicesecurity-trusted-auth-api.md#operatetype) | 是 | 获取生物特征authToken操作类型，详见[OperateType](devicesecurity-trusted-auth-api.md#operatetype)。 |
| tuiAuthToken | Uint8Array | 是 | 当操作类型为OPERATE\_TYPE\_BIOMETRIC\_AUTH时，tuiAuthToken表示通过密码认证（即[trustedAuthentication](devicesecurity-trusted-auth-api.md#trustedauthentication)）获取的authToken信息。  当操作类型为OPERATE\_TYPE\_CONTENT\_AUTH时，tuiAuthToken表示通过交易信息临时确认（即[procContentAuthentication](devicesecurity-trusted-auth-api.md#proccontentauthentication)）获取的authToken信息。 |
| bioAuthToken | Uint8Array | 是 | 生物特征认证获取的authToken，要求tuiAuthToken和bioAuthToken获取时使用同一个challenge，即保障两个authToken通过同一次会话获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthToken](devicesecurity-trusted-auth-api.md#authtoken)> | Promise对象。  在生物特征认证绑定流程中，获取的authToken为经数字盾服务认证签发的包括生物特征ID的authToken。  在生物特征交易认证流程中，获取的authToken为经数字盾服务认证前的包括交易信息和生物特征ID的authToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100005 | Face/Fingerprint/Password authentication failed. |
| 1019100015 | Failed to get the biometric authToken. |
| 1019100019 | The biometric data for authentication does not match the bound biometric feature. |
| 1019100020 | The biometric data has already been bound. |

**示例：**

```
1. import { userAuth } from '@kit.UserAuthenticationKit';
2. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
3. import { BusinessError} from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
6. import { resourceManager } from '@kit.LocalizationKit';
7. import { common } from '@kit.AbilityKit';

9. const TAG = "TrustedAuthenticationJsTest";
10. async function PwdVerify(challenge: Uint8Array, resourceMgr:resourceManager.ResourceManager):Promise<trustedAuthentication.AuthToken> {
11. try {
12. const authID: bigint = 11842183505170721246n; // 实际填充为从服务器获取到的账号对应的authID值
13. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); // 实际使用时请替换为应用要在TUI界面展示的logo图片名称
14. const buffer = fileData.buffer;
15. const label:trustedAuthentication.TUILable = {
16. image: buffer as ArrayBuffer,
17. title: "数字盾密码认证",
18. }
19. const result = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
20. return result;
21. } catch (err) {
22. hilog.error(0x0000, 'testTag', `Failed to trustedAuthentication, code:${err.code}, message:${err.message}`);
23. throw new Error('Password verify failed:' + (err as BusinessError).message);
24. }
25. }
26. const rand = cryptoFramework.createRandom();
27. const len: number = 32;
28. let challengeID: Uint8Array = rand?.generateRandomSync(len)?.data;
29. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
30. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
31. const TuiAuthToken: trustedAuthentication.AuthToken = await PwdVerify(challengeID, resourceMgr);
32. let authTypeList :number[] = new Array();
33. authTypeList[0] = userAuth.UserAuthType.FINGERPRINT;
34. authTypeList[1] = userAuth.UserAuthType.FACE;

36. const authParam : userAuth.AuthParam = {
37. challenge:  challengeID,
38. authType: authTypeList,
39. authTrustLevel: userAuth.AuthTrustLevel.ATL4
40. };
41. const widgetParam: userAuth.WidgetParam = {
42. title: '请输入盾密码',
43. navigationButtonText: '请输入盾密码',
44. };

46. try {
47. const userAuthInstance = await userAuth.getUserAuthInstance(authParam, widgetParam);
48. userAuthInstance.on('result', {
49. onResult (result) {
50. let authTokenData = result.token;
51. let operType = trustedAuthentication.OperateType.OPERATE_TYPE_BIOMETRIC_AUTH;
52. trustedAuthentication.getBiometricAuthToken(operType, TuiAuthToken.authToken, authTokenData).then((newAuthToken) => {
53. let authToken = newAuthToken.authToken as Uint8Array;
54. hilog.info(0x0000, TAG, `authToken content: ${authToken}`);
55. });
56. }
57. })
58. userAuthInstance.start();
59. } catch (err) {
60. let e: BusinessError = err as BusinessError;
61. hilog.error(0x0000, TAG, 'getUserAuthInstance failed: %{public}d %{public}s', e.code, e.message);
62. }
```

## importData

Phone

importData(data: ArrayBuffer, authID: bigint): Promise<void>

导入备份的数据信息（即与HUKS签名验签时使用的加密密钥信息）。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 通常指定为从Universal Keystore Kit获取的wrapkey数据信息，导入数据大小限制在2048字节内，对应数据不支持反复导入。 |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100010 | Failed to import data. |
| 1019100012 | Invalid authentication ID. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "TrustedAuthenticationJsTest";

7. try {
8. const authID: bigint = 1687413472599354502n;
9. const buffer = new ArrayBuffer(8);
10. const bufferArray = new Uint8Array(buffer);
11. bufferArray.set([1, 2, 3, 4, 5, 6, 7, 8]);
12. const result = await trustedAuthentication.importData(buffer, authID);
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. hilog.error(0x0000, TAG, 'importData failed: %{public}d %{public}s', e.code, e.message);
16. }
```

## exportData

Phone

exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>

导出备份的数据信息（即与HUKS签名验签时使用的加密密钥信息），在导出时，需要经过密码认证，认证通过后才可导出对应的备份数据信息。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| label | [TUILable](devicesecurity-trusted-auth-api.md#tuilable) | 是 | 用于TUI界面展示时的定制信息，详见[TUILable](devicesecurity-trusted-auth-api.md#tuilable)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回备份的数据信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100009 | Failed to export data. |
| 1019100012 | Invalid authentication ID. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import { common } from '@kit.AbilityKit';

7. const TAG = "TrustedAuthenticationJsTest";

9. try {
10. const credentialID: bigint = 1687413472599354502n;
11. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
13. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
14. const buffer = fileData.buffer;
15. const label:trustedAuthentication.TUILable = {
16. image: buffer as ArrayBuffer,
17. title: "备份数据导出",
18. }
19. const result = await trustedAuthentication.exportData(credentialID, label);
20. } catch (err) {
21. let e: BusinessError = err as BusinessError;
22. hilog.error(0x0000, TAG, 'exportData failed: %{public}d %{public}s', e.code, e.message);
23. }
```

## checkConfirmUITextFormat

Phone

checkConfirmUITextFormat(text: string): Promise<TextCheckResult>

检查将在TUI呈现的内容是否可以在屏幕上单行完整展示。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 将在TUI界面展示的认证信息内容。在交易认证前，可通过该接口确认交易信息是否可以在屏幕上单行完整展示，长度规格为1~200字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TextCheckResult](devicesecurity-trusted-auth-api.md#textcheckresult)> | Promise对象，TUI界面显示指定text对应检查结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100006 | Check input confirm text failed. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "TrustedAuthenticationJsTest";

7. try {
8. const text: string = "检查将在TUI呈现的text是否可以正常展示";
9. const result = await trustedAuthentication.checkConfirmUITextFormat(text);
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. hilog.error(0x0000, TAG, 'checkConfirmUITextFormat failed: %{public}d %{public}s', e.code, e.message);
13. }
```

## getRemainAuthTimes

Phone

getRemainAuthTimes(authID: bigint): Promise<number>

获取数字盾剩余认证次数。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，数字盾剩余认证次数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100012 | Invalid authentication ID. |
| 1019100017 | Failed to get the remaining number of authentication attempts. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "TrustedAuthenticationJsTest";

7. try {
8. const authID: bigint = 1687413472599354502n;
9. const remainTimes = await trustedAuthentication.getRemainAuthTimes(authID);
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. hilog.error(0x0000, TAG, 'getRemainAuthTimesfailed: %{public}d %{public}s', e.code, e.message);
13. }
```

## disableTrustedBioAuthentication

Phone

disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>

解绑指定生物类型认证能力。使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authID | bigint | 是 | 密码创建时获取的authID信息。 |
| authType | AuthType | 是 | 仅支持AUTH\_TYPE\_FACE、AUTH\_TYPE\_FINGERPRINT |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-trusted-auth.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 1019100001 | The interface invoker does not have the corresponding permission. |
| 1019100002 | Parameter error.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1019100012 | Invalid authentication ID. |
| 1019100018 | Failed to unbind the corresponding biometric data. |
| 1019100021 | The corresponding biometric data has not been bound. |

**示例：**

```
1. import { trustedAuthentication} from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "TrustedAuthenticationJsTest";

7. try {
8. const authID: bigint = 1687413472599354502n;
9. const remainTimes = await trustedAuthentication.disableTrustedBioAuthentication(authID, trustedAuthentication.AuthType.AUTH_TYPE_FACE);
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. hilog.error(0x0000, TAG, 'disableTrustedBioAuthentication: %{public}d %{public}s', e.code, e.message);
13. }
```

## PasswordInfo

Phone

设置密码时业务对密码规格参数要求。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| pwdType | [PasswordType](devicesecurity-trusted-auth-api.md#passwordtype) | 否 | 否 | 密码类型，取值范围详见[PasswordType](devicesecurity-trusted-auth-api.md#passwordtype)。 |
| pwdMaxLength | number | 否 | 否 | 密码最大长度，取值范围6~18。 |
| pwdMinLength | number | 否 | 否 | 密码最小长度，取值范围6~18，且小于等于pwdMaxLength。 |
| maxAuthFailCount | number | 否 | 否 | 密码最大连续认证失败次数，取值范围1~10。 |

## TUILable

Phone

TUI页面下的定制信息，包括定制图像logo和页面标题。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| image | ArrayBuffer | 否 | 否 | 定制logo信息，要求图片格式为PNG RGBA格式、最大宽度、长度要求均为216px。 |
| title | string | 否 | 否 | 定制TUI页面标题信息，最大长度要求为31字节。 |

## AuthInfo

Phone

开通数字盾服务对应的参数信息。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authToken | Uint8Array | 否 | 否 | 包括密码authID的authToken信息。 |
| authID | bigint | 否 | 否 | 表示数字盾密码authID索引，用于密码认证、删除、修改。 |

## AuthToken

Phone

经数字盾服务指定操作获取的authToken，不同操作流程中authToken包括的加密信息不同，详细可参考各个接口参数说明。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authToken | Uint8Array | 否 | 否 | 对应操作流程中authToken信息。 |

## AuthType

Phone

交易认证类型定义。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| AUTH\_TYPE\_FACE | 2 | 人脸认证 |
| AUTH\_TYPE\_FINGERPRINT | 4 | 指纹认证 |
| AUTH\_TYPE\_TUI\_PIN | 32 | TUI密码认证 |

## PasswordType

Phone

密码类型定义，根据密码类型TUI界面弹出不同类型的安全键盘。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| PASSWORD\_TYPE\_DIGITAL | 0 | 纯数字密码类型 |
| PASSWORD\_TYPE\_MIXED | 1 | 数字、字符混合密码类型 |

## OperateType

Phone

操作类型定义。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| OPERATE\_TYPE\_BIOMETRIC\_AUTH | 1 | 生物特征与密码认证绑定操作 |
| OPERATE\_TYPE\_CONTENT\_AUTH | 2 | 使用生物特征进行交易认证操作 |

## AuthReqParams

Phone

交易认证请求相关参数。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| reqType | [AuthType](devicesecurity-trusted-auth-api.md#authtype) | 否 | 否 | 认证类型，取值范围详见[AuthType](devicesecurity-trusted-auth-api.md#authtype)。 |
| authContent | Array<string> | 否 | 否 | 认证数据，即交易场景下交易数据，单条数据大小在1024字节以内。 |

## TextCheckResult

Phone

TUI界面文本信息是否可以单行显示的检查结果。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 指定输入文本检查结果，如果可以正常显示，返回为0，否则返回[1019100011 不合法的TUI认证信息](devicesecurity-arktsapi-errcode-trusted-auth.md#section1019100011-不合法的tui认证信息)。 |
| lastIndex | number | 否 | 否 | 输入字符串可正常显示的最后一个字符对应的索引。 |

## TrustedAuthErrorCode

Phone

数字盾服务开放接口执行失败错误码。

**系统能力：** SystemCapability.Security.TrustedAuthentication

**起始版本：** 6.0.0(20)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION | 1019100001 | 权限校验失败 |
| TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT | 1019100002 | 参数检查失败 |
| TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED | 1019100003 | 密码认证连续失败次数达到应用定义的最大次数 |
| TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED | 1019100004 | 删除密码失败 |
| TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED | 1019100005 | 密码认证失败 |
| TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED | 1019100006 | 输入文本信息检查失败 |
| TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE | 1019100007 | 不支持的图片格式 |
| TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL | 1019100008 | 用户取消操作 |
| TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED | 1019100009 | 备份数据导出失败 |
| TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED | 1019100010 | 备份数据导入失败 |
| TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT | 1019100011 | 不合法的TUI认证信息 |
| TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID | 1019100012 | 无效的authID |
| TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED | 1019100013 | 创建密码失败 |
| TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED | 1019100014 | 修改密码失败 |
| TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED | 1019100015 | 生物认证authToken签发失败 |
| TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED | 1019100016 | 数字盾服务未使能 |
| TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME | 1019100017 | 获取数字盾剩余认证次数失败 |
| TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH | 1019100018 | 解绑指定生物特征认证能力失败 |
| TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH | 1019100019 | 认证的生物特征与绑定的生物特征不匹配 |
| TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND | 1019100020 | 已绑定对应的生物特征 |
| TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO | 1019100021 | 对应生物特征未绑定 |
