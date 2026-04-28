---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoextensionability
title: @ohos.security.CryptoExtensionAbility (密钥扩展能力)
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > ArkTS API > @ohos.security.CryptoExtensionAbility (密钥扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb91093dbc2feb776363b8e5571add18db12b4e0591b138a26da5def718913cd
---

模块提供外部密钥扩展能力，包括资源管理、PIN码认证管理、密码操作、通用操作等接口能力。

ExtensionAbility实现约束：

1. 设备管理，单个ExtensionAbility实现，最多支持10个Ukey接入。
2. 句柄管理，针对同一个Ukey资源（例如，容器下的密钥），支持应用维度资源句柄管理。
   * 支持多个HarmonyOS应用，打开同一个Ukey密钥资源。例如：HarmonyOS应用1打开容器A后，HarmonyOS应用2也可以再次打开容器A。
   * 支持多个HarmonyOS应用，操作同一个Ukey密钥资源。例如：HarmonyOS应用1操作容器A中的私钥签名后，HarmonyOS应用2也验证PIN码后，也可以操作容器A中的私钥进行签名，两者互不影响。
3. 密钥会话管理，支持三段式密钥管理操作，单次签名验签需通过[onInitSession](js-apis-cryptoextensionability.md#cryptoextensionabilityoninitsession)/[onUpdateSession](js-apis-cryptoextensionability.md#cryptoextensionabilityonupdatesession)/[onFinishSession](js-apis-cryptoextensionability.md#cryptoextensionabilityonfinishsession)三个函数三步配合完成，需支持会话管理，缓存密钥会话状态。
   * init操作，初始化密钥会话，并返回会话句柄信息。
   * update操作，传入分组数据，对分组数据进行密码操作，更新密钥会话信息后，将中间数据（如果有）返回。
   * finish操作，对传入最后一段分组数据，进行密钥返回操作，并结束密钥会话，将最终结果返回。
4. 认证状态管理，支持应用维度的认证状态管理。针对同一个Ukey中的应用A，HarmonyOS应用1验证Ukey应用A的PIN码后，HarmonyOS应用2如果要访问Ukey应用A，也需要进行PIN码认证操作。
5. 证书查询，支持根据证书类型，枚举所有证书或查询单个容器中的证书。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { huks, huksExternalCrypto, CryptoExtensionAbility } from '@kit.UniversalKeystoreKit';
```

## HuksCryptoExtensionResultCode

PC/2in1

[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)中的resultCode枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_EXTENSION\_FAIL | 34800000 | 密钥扩展错误。可能的原因：  1. 输入参数无效。  2. 密钥扩展出现无法解决的错误状态。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_UKEY\_NOT\_EXIST | 34800001 | UKey不存在。可能的原因：  1. UKey已被移除。  2. 密钥扩展陷入错误的UKey状态。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_UKEY\_DRIVER\_FAIL | 34800002 | UKey驱动出现未知错误。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_NO\_AUTH | 34800003 | UKey PIN码未认证，需要先认证Ukey PIN码。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_HANDLE\_NOT\_EXIST | 34800004 | 句柄不存在。可能的原因：  1. 句柄无效。  2. HUKS服务和密钥扩展的状态不一致。由于异常情况，HUKS服务持有的句柄未能释放。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_HANDLE\_UNAVAILABLE | 34800005 | 句柄不可用。可能的原因：  密钥扩展和Ukey的状态不一致。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_INCORRECT | 34800006 | UKey PIN码错误，需要检查输入的PIN码。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_LOCKED | 34800007 | UKey PIN码被锁。可能的原因：  PIN码输入错误次数过多。 |

## HuksCryptoExtensionCertInfo

PC/2in1

[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)中的certs数组中的元素。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| purpose | [certificateManager.CertificatePurpose](js-apis-certmanager.md#certificatepurpose22) | 否 | 否 | 表示证书链对应密钥的使用类型。 |
| resourceId | string | 否 | 否 | 资源ID。JSON格式，能够映射到Ukey中的某个资源。 |
| cert | Uint8Array | 否 | 否 | 证书。 |

## HuksCryptoExtensionResult

PC/2in1

接口返回值的通用类型。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 否 | 否 | 返回值的错误码。 |
| handle | string | 否 | 是 | 资源句柄。 |
| authState | number | 否 | 是 | 认证状态。 |
| retryCount | number | 否 | 是 | 重试次数。 |
| certs | Array<[HuksCryptoExtensionCertInfo](js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)> | 否 | 是 | 证书。 |
| property | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 是 | 属性。 |
| outData | Uint8Array | 否 | 是 | 返回的数据。 |

## CryptoExtensionAbility.onOpenResource

PC/2in1

onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

根据参数中的resourceId，打开Ukey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，handle携带资源句柄信息。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 Ukey不存在。  34800002 Ukey驱动错误。  34800004 句柄不存在。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. // 解析resourceId，打开底层句柄，并映射为新的句柄返回。
6. let result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. handle: "test handle"
9. };

11. // ...
12. return Promise.resolve(result);
13. }
14. }
```

## CryptoExtensionAbility.onCloseResource

PC/2in1

onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

根据参数中的handle，关闭Ukey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示关闭资源成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. // 执行句柄关闭操作。如果需要关闭底层句柄，则执行关闭操作。
6. const result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. };

10. // ...
11. return Promise.resolve(result);
12. }
13. }
```

## CryptoExtensionAbility.onGetProperty

PC/2in1

onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

根据参数中的handle和propertyId获取属性。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| propertyId | string | 是 | 查找操作的属性名称，是GMT 0016-2023中定义的SKF接口名，要业务针对接口名适配。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的property成员非空，包含获取到的属性，由[HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800003 Ukey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 Ukey PIN码被锁。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. // 按照propertyId执行相关函数，函数参数从params中获取。输出数据封装到返回值的property字段中，由HUKS_EXT_CRYPTO_TAG_EXTRA_DATA携带。
6. const emptyArray: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
7. const result: HuksCryptoExtensionResult = {
8. resultCode: 0,
9. property: emptyArray
10. };

12. // ...
13. return Promise.resolve(result);
14. }
15. }
```

## CryptoExtensionAbility.onAuthUkeyPin

PC/2in1

onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

请求Ukey认证PIN码。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，authState非0，表示认证请求成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  34800006 Ukey PIN码错误。  34800007 Ukey PIN码被锁。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. // 执行PIN码认证操作，并且维护应用的PIN码认证状态。
6. const result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. authState: 1
9. };

11. // ...
12. return Promise.resolve(result);
13. }
14. }
```

## CryptoExtensionAbility.onGetUkeyPinAuthState

PC/2in1

onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

获取Ukey的PIN码认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的authState成员非空，为获取的PIN码认证状态。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. // 查询PIN码认证状态。
6. const result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. authState: 1
9. };

11. // ...
12. return Promise.resolve(result);
13. }
14. }
```

## CryptoExtensionAbility.onClearUkeyPinAuthState

PC/2in1

onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

清除应用维度PIN码的认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示清除PIN码认证状态成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
5. const result: HuksCryptoExtensionResult = {
6. resultCode: 0
7. };

9. // ...
10. return Promise.resolve(result);
11. }
12. }
```

## CryptoExtensionAbility.onInitSession

PC/2in1

onInitSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult>

三段式初始化密钥会话操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，handle成员非空。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800003 Ukey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 Ukey PIN码被锁。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onInitSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
5. const result: HuksCryptoExtensionResult = {
6. resultCode: 0,
7. handle: "test handle"
8. };

10. // ...
11. return Promise.resolve(result);
12. }
13. }
```

## CryptoExtensionAbility.onUpdateSession

PC/2in1

onUpdateSession(initHandle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult>

三段式密钥会话更新数据操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800003 Ukey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 Ukey PIN码被锁。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onUpdateSession(initHandle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
5. let outBuffer: Uint8Array = new Uint8Array(1024);
6. const result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. outData: outBuffer
9. };

11. // ...
12. return Promise.resolve(result);
13. }
14. }
```

## CryptoExtensionAbility.onFinishSession

PC/2in1

onFinishSession(initHandle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult>

三段式密钥会话结束操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | 是 | 传入的参数，应用身份可通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带，还包括算法参数（算法类型、填充模式等）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 Ukey驱动错误。  34800003 Ukey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 Ukey PIN码被锁。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

3. export default class CryptoExtension extends CryptoExtensionAbility {
4. onFinishSession(initHandle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
5. let outBuffer: Uint8Array = new Uint8Array(1024);
6. const result: HuksCryptoExtensionResult = {
7. resultCode: 0,
8. outData: outBuffer
9. };

11. // ...
12. return Promise.resolve(result);
13. }
14. }
```

## CryptoExtensionAbility.onExportCertificate

PC/2in1

onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

查询指定resourceId下的证书。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。会附带在[HuksCryptoExtensionCertInfo](js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)中。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 操作属性。默认获取签名类型的证书，也可以通过参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](js-apis-huksexternalcrypto.md#huksexternalcryptotag)指定获取证书类型，支持的类型包括签名验签、加解密等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，certs成员非空，包含获取的单本证书。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 Ukey不存在。  34800002 Ukey驱动错误。  34800004 句柄不存在。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult,
2. HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

4. export default class CryptoExtension extends CryptoExtensionAbility {
5. onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
6. const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
7. const result: HuksCryptoExtensionResult = {
8. resultCode: 0,
9. certs: certInfoSetArray
10. };

12. // ...
13. return Promise.resolve(result);
14. }
15. }
```

## CryptoExtensionAbility.onEnumCertificates

PC/2in1

onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult>

枚举Extension下所有Ukey设备的证书信息。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 操作属性。默认获取签名类型的[证书](../harmonyos-guides/certmanager-overview.md)，也可以通过参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](js-apis-huksexternalcrypto.md#huksexternalcryptotag)指定获取证书类型，支持的类型包括签名验签、加解密等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，certs成员非空，包含获取的所有证书。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 Ukey不存在。  34800002 Ukey驱动错误。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```
1. import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult,
2. HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

4. export default class CryptoExtension extends CryptoExtensionAbility {
5. onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
6. const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
7. const result: HuksCryptoExtensionResult = {
8. resultCode: 0,
9. certs: certInfoSetArray
10. };

12. // ...
13. return Promise.resolve(result);
14. }
15. }
```
