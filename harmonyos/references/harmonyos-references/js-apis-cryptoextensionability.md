---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoextensionability
title: "@ohos.security.CryptoExtensionAbility (密钥扩展能力)"
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > ArkTS API > @ohos.security.CryptoExtensionAbility (密钥扩展能力)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce66e044d64b8b7fe6bf34f9f9feb1ae9028a65b1d7ca3364914a7e47dac95ed
---

模块提供外部密钥扩展能力，包括资源管理、PIN码认证管理、密码操作、通用操作等接口能力。

ExtensionAbility功能与约束：

1. 设备管理，单个ExtensionAbility实现，最多支持10个UKey接入。
2. 句柄管理，针对同一个UKey资源（例如，容器下的密钥），支持应用维度资源句柄管理。
   * 支持多个HarmonyOS应用，打开同一个UKey密钥资源。例如：HarmonyOS应用1打开容器A后，HarmonyOS应用2也可以再次打开容器A。
   * 支持多个HarmonyOS应用，操作同一个UKey密钥资源。例如：HarmonyOS应用1操作容器A中的私钥签名后，HarmonyOS应用2也验证PIN码后，也可以操作容器A中的私钥进行签名，两者互不影响。
3. 密钥会话管理，支持三段式密钥管理操作，单次签名验签需通过[onInitSession](js-apis-cryptoextensionability.md#oninitsession)/[onUpdateSession](js-apis-cryptoextensionability.md#onupdatesession)/[onFinishSession](js-apis-cryptoextensionability.md#onfinishsession)三个函数三步配合完成，需支持会话管理，缓存密钥会话状态。
   * init操作，初始化密钥会话，并返回会话句柄信息。
   * update操作，传入分组数据，对分组数据进行密码操作，更新密钥会话信息后，将中间数据（如果有）返回。
   * finish操作，对传入最后一段分组数据，进行密钥返回操作，并结束密钥会话，将最终结果返回。
4. 认证状态管理，支持应用维度的认证状态管理。针对同一个UKey中的应用A，HarmonyOS应用1验证UKey应用A的PIN码后，HarmonyOS应用2如果要访问UKey应用A，也需要进行PIN码认证操作。
5. 证书查询，支持根据证书类型，枚举所有证书或查询单个容器中的证书。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 约束限制

CryptoExtensionAbility作为密钥管理扩展能力，为减少安全攻击面，保障CryptoExtensionAbility合理实现，系统对网络、蓝牙、位置等能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-cryptoextensionability.md#附录)。

## 导入模块

```ts
import { huks, huksExternalCrypto, CryptoExtensionAbility } from '@kit.UniversalKeystoreKit';
```

## HuksCryptoExtensionResultCode

[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)中的resultCode枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_EXTENSION\_FAIL | 34800000 | 密钥扩展错误。可能的原因：  1. 输入参数无效。  2. 密钥扩展出现无法解决的错误状态。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_UKEY\_NOT\_EXIST | 34800001 | UKey不存在。可能的原因：  1. UKey已被移除。  2. 密钥扩展陷入错误的UKey状态。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_UKEY\_DRIVER\_FAIL | 34800002 | UKey驱动出现未知错误。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_NO\_AUTH | 34800003 | UKey PIN码未认证，需要先通过[onAuthUkeyPin](js-apis-cryptoextensionability.md#onauthukeypin)认证UKey PIN码。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_HANDLE\_NOT\_EXIST | 34800004 | 句柄不存在。可能的原因：  1. 句柄无效。  2. HUKS服务和密钥扩展的状态不一致。由于异常情况，HUKS服务持有的句柄未能释放。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_HANDLE\_UNAVAILABLE | 34800005 | 句柄不可用。可能的原因：  密钥扩展和UKey的状态不一致。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_INCORRECT | 34800006 | UKey PIN码错误，需要检查输入的PIN码。 |
| HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_LOCKED | 34800007 | UKey PIN码被锁定。可能的原因：  PIN码输入错误次数过多。 |

## HuksCryptoExtensionCertInfo

[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)中的certs数组中的元素。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| purpose | [certificateManager.CertificatePurpose](js-apis-certmanager.md#certificatepurpose22) | 否 | 否 | 表示证书链对应密钥的使用类型。 |
| resourceId | string | 否 | 否 | 资源ID。JSON格式，能够映射到UKey中的某个资源。 |
| cert | Uint8Array | 否 | 否 | 证书。 |

## HuksCryptoExtensionResult

接口返回值的通用类型。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 否 | 否 | 返回值的错误码。 |
| handle | string | 否 | 是 | 资源句柄。 |
| authState | number | 否 | 是 | 认证状态。 |
| retryCount | number | 否 | 是 | 重试次数，表示PIN码认证剩余可用次数，为0时表示无剩余重试机会。 |
| certs | Array<[HuksCryptoExtensionCertInfo](js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)> | 否 | 是 | 证书。 |
| property | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 是 | 属性。 |
| outData | Uint8Array | 否 | 是 | 返回的数据。 |
| resourceId | string | 否 | 是 | 返回的资源ID。默认值为空。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
| errInfo | [huksExternalCrypto.HuksExternalErrorInfo](js-apis-huksexternalcrypto.md#huksexternalerrorinfo) | 否 | 是 | 返回的详细错误信息。默认值为{0,""}。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

## HuksCryptoExtensionParam

密钥扩展操作参数，用于指定操作的属性标签和对应值。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tag | [huksExternalCrypto.HuksExternalCryptoTag](js-apis-huksexternalcrypto.md#huksexternalcryptotag) | [huks.HuksTag](js-apis-huks.md#hukstag) | number | 否 | 否 | 标签。 |
| value | boolean | number | bigint | Uint8Array | 否 | 否 | 标签对应值。 |

## HuksCryptoExtensionParams

密钥扩展操作参数集合，用于传递操作所需的属性和输入数据。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 否 | 否 | 属性，用于存储HuksCryptoExtensionParam的数组。默认为undefined。 |
| inData | Uint8Array | 否 | 是 | 输入数据。默认为undefined。 |

## CryptoExtensionAbility

密钥扩展能力类，提供外部密钥管理扩展所需接口定义，包括打开/关闭资源、PIN码认证管理、密钥会话操作、证书管理、密钥生成与导入、通用操作等接口能力。驱动厂商需继承CryptoExtensionAbility并实现相关接口，通过[registerProvider](js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)完成能力注册后，由HUKS和证书管理将对应的密钥管理扩展能力开放给应用使用。

CryptoExtensionAbility可以隔离不同的UKey驱动厂商实现的差异。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

### onOpenResource

onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

根据参数中的resourceId，打开UKey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，handle携带资源句柄信息。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 UKey不存在。  34800002 UKey驱动错误。  34800004 句柄不存在。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析resourceId，打开底层句柄，并映射为新的句柄返回。
    let result: HuksCryptoExtensionResult = {
      resultCode: 0,
      handle: "test handle"
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onCloseResource

onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

根据参数中的handle，关闭UKey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示关闭资源成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 执行句柄关闭操作。如果需要关闭底层句柄，则执行关闭操作。
    const result: HuksCryptoExtensionResult = {
        resultCode: 0,
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onGetProperty

onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

根据参数中的handle和propertyId获取属性。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| propertyId | string | 是 | 查找操作的属性名称，是GMT 0016-2023中定义的SKF接口名，要业务针对接口名适配。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的property成员非空，包含获取到的属性，由[HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800003 UKey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 UKey PIN码被锁定。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 按照propertyId执行相关函数，函数参数从params中获取。输出数据封装到返回值的property字段中，由HUKS_EXT_CRYPTO_TAG_EXTRA_DATA携带。
    const emptyArray: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      property: emptyArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onSetProperty

onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

根据参数中的handle和propertyId设置属性。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| propertyId | string | 是 | 设置操作的属性名称，推荐使用GMT 0016-2023中定义的SKF接口名作为属性ID。 |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，包含与propertyId相关的操作参数。应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示设置属性成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。可能的原因：  1. 输入参数无效。  2. 密钥扩展出现无法解决的错误状态。  34800002 UKey驱动错误。  34800003 UKey PIN码未认证，需要先认证UKey PIN码。  34800004 句柄不存在。可能的原因：  1. 句柄无效。  2. HUKS服务和密钥扩展的状态不一致。由于异常情况，HUKS服务持有的句柄未能释放。  34800005 句柄不可用。可能的原因：  密钥扩展和UKey的状态不一致。  34800007 UKey PIN码被锁定。可能的原因：  PIN码输入错误次数过多。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 按照propertyId执行相关设置操作，操作参数从params中获取。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onAuthUkeyPin

onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

请求UKey认证PIN码。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，authState非0，表示认证请求成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  34800006 UKey PIN码错误。  34800007 UKey PIN码被锁定。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 执行PIN码认证操作，并且维护应用的PIN码认证状态。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      authState: 1
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onGetUkeyPinAuthState

onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

获取UKey的PIN码认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的authState成员非空，为获取的PIN码认证状态。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 查询PIN码认证状态。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      authState: 1
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onClearUkeyPinAuthState

onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

清除应用维度PIN码的认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示清除PIN码认证状态成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onInitSession

onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult>

三段式初始化密钥会话操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | [HuksCryptoExtensionParams](js-apis-cryptoextensionability.md#hukscryptoextensionparams) | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，handle成员非空。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800003 UKey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 UKey PIN码被锁定。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      handle: "test handle"
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onUpdateSession

onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult>

三段式密钥会话更新数据操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | [HuksCryptoExtensionParams](js-apis-cryptoextensionability.md#hukscryptoextensionparams) | 是 | 传入的参数，应用身份通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800003 UKey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 UKey PIN码被锁定。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    let outBuffer: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: outBuffer
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onFinishSession

onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult>

三段式密钥会话结束操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | [huks.HuksOptions](js-apis-huks.md#huksoptions) | [HuksCryptoExtensionParams](js-apis-cryptoextensionability.md#hukscryptoextensionparams) | 是 | 传入的参数，应用身份可通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带，还包括算法参数（算法类型、填充模式等）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800003 UKey PIN码未认证。  34800004 句柄不存在。  34800005 句柄不可用。  34800007 UKey PIN码被锁定。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    let outBuffer: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: outBuffer
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onExportCertificate

onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

查询指定resourceId下的证书。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。会附带在[HuksCryptoExtensionCertInfo](js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)中。 |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 否 | 操作属性。默认获取签名类型的证书，也可以通过参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](js-apis-huksexternalcrypto.md#huksexternalcryptotag)指定获取证书类型，支持的类型包括签名验签、加解密等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，certs成员非空，包含获取的单本证书。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 UKey不存在。  34800002 UKey驱动错误。  34800004 句柄不存在。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult,
  HuksCryptoExtensionCertInfo, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      certs: certInfoSetArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onEnumCertificates

onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

枚举Extension下所有UKey设备的证书信息。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<[huksExternalCrypto.HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 否 | 操作属性。默认获取签名类型的[证书](../harmonyos-guides/certmanager-overview.md)，也可以通过参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](js-apis-huksexternalcrypto.md#huksexternalcryptotag)指定获取证书类型，支持的类型包括签名验签、加解密等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，certs成员非空，包含获取的所有证书。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 UKey不存在。  34800002 UKey驱动错误。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      certs: certInfoSetArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onGetResourceId

onGetResourceId(params: HuksCryptoExtensionParam[]):Promise<HuksCryptoExtensionResult>

获取外部扩展设备内的资源ID。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 获取资源ID所需的属性参数。必选TAG包括：[HUKS\_EXT\_CRYPTO\_TAG\_RESOURCE\_INFO](js-apis-huksexternalcrypto.md#huksexternalcryptotag)（厂商自定义的资源信息）、[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)（调用方身份）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，resourceId携带资源ID信息。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetResourceId(params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      resourceId: "test resourceId"
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onImportCertificate

onImportCertificate(handle: string, params: HuksCryptoExtensionParam[], certInfo: HuksCryptoExtensionCertInfo): Promise<HuksCryptoExtensionResult>

导入指定资源句柄的证书。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 导入证书的资源句柄。 |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 导入证书所需的属性参数。 |
| certInfo | [HuksCryptoExtensionCertInfo](js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo) | 是 | 待导入的证书信息。需指定证书类型（purpose）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示导入证书成功。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800001 UKey不存在。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { CryptoExtensionAbility, HuksCryptoExtensionParam, HuksCryptoExtensionResult,
  HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onImportCertificate(handle: string, params: HuksCryptoExtensionParam[],
      certInfo: HuksCryptoExtensionCertInfo): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onGenerateKeyItem

onGenerateKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

用于在扩展设备内生成密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待生成密钥的资源句柄。 |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 密钥生成操作的属性参数。必选TAG：[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)（调用方身份）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示生成密钥成功。调用失败时，resultCode携带错误码信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGenerateKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数
    let algorithm: huks.HuksKeyAlg | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
    let keySize: huks.HuksKeySize | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入参数，设置默认值
    if (algorithm === undefined) {
      algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA; // 默认RSA算法
    }
    if (keySize === undefined) {
      keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048; // 默认2048位
    }
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN; // 默认签名用途
    }

    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onExportKeyItem

onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>

用于导出指定密钥的公钥。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待导出公钥的资源句柄。 |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 导出公钥操作的属性参数。必选TAG：[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)（调用方身份）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，outData携带导出的公钥数据。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数，推荐传入密钥用途
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入用途参数，设置默认值（推荐默认签名用途）
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;
    }

    let pubKey: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: pubKey
    };

    // ...
    return Promise.resolve(result);
  }
}
```

### onImportWrappedKeyItem

onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[], wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult>

用于导入加密封装的密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待导入密钥的资源句柄。 |
| wrappingHandle | string | 是 | 用于解封导入密钥的密钥资源句柄。 |
| params | [HuksCryptoExtensionParam](js-apis-cryptoextensionability.md#hukscryptoextensionparam)[] | 是 | 导入封装密钥操作的属性参数。必选TAG：[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)（调用方身份）。 |
| wrappedKey | Uint8Array | 是 | 封装密钥数据，格式由密钥扩展定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksCryptoExtensionResult](js-apis-cryptoextensionability.md#hukscryptoextensionresult)> | Promise对象。当调用成功时，resultCode为0，表示导入密钥成功。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。  可能返回的错误码值：  34800000 密钥扩展错误。  34800002 UKey驱动错误。  34800004 句柄不存在。  34800005 句柄不可用。  具体含义可查询[HuksCryptoExtensionResultCode](js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)。 |

**示例：**

```ts
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';
export default class CryptoExtension extends CryptoExtensionAbility {
  onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[], wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数
    let algorithm: huks.HuksKeyAlg | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
    let keySize: huks.HuksKeySize | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入参数，设置默认值
    if (algorithm === undefined) {
      algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA;
    }
    if (keySize === undefined) {
      keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
    }
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT;
    }

    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```

## 附录

CryptoExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | [@ohos.wantAgent (WantAgent模块)](js-apis-wantagent.md) |
| Ads Kit | [@ohos.advertising.AdComponent (广告展示组件)](js-apis-adcomponent.md) |
| Ads Kit | [@ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)](js-apis-adsserviceextensionability.md) |
| Ads Kit | [@ohos.advertising.AutoAdComponent (轮播广告展示组件)](js-apis-autoadcomponent.md) |
| Ads Kit | [@ohos.advertising (广告服务框架)](js-apis-advertising.md) |
| AppGallery Kit | [appInfoManager（应用元数据管理服务）](appgallery-appinfomanager.md) |
| AppGallery Kit | [attributionManager（应用归因服务）](store-attributionmanager.md) |
| AppGallery Kit | [attributionTestManager（应用归因接入调试功能）](store-attributiontestmanager.md) |
| AppGallery Kit | [commentManager（应用评论服务）](appgallery-commentmanager.md) |
| AppGallery Kit | [moduleInstallManager (产品特性按需分发)](store-moduleinstallmanager.md) |
| AppGallery Kit | [privacyManager（隐私管理服务）](store-privacymanager.md) |
| AppGallery Kit | [productViewManager（应用市场推荐）](store-productviewmanager.md) |
| AppGallery Kit | [updateManager（更新功能）](store-updatemanager.md) |
| AR Engine Kit | [arEngine（AR增强现实能力）](arengine-api-arengine.md) |
| AR Engine Kit | [ARView（AR场景可视化）](arengine-api-component-arview.md) |
| ArkUI | [@ohos.atomicservice.AtomicServiceNavigation (AtomicServiceNavigation)](ohos-atomicservice-atomicservicenavigation.md) |
| ArkUI | [@ohos.atomicservice.AtomicServiceSearch (AtomicServiceSearch)](ohos-atomicservice-atomicservicesearch.md) |
| ArkUI | [@ohos.atomicservice.AtomicServiceTabs (AtomicServiceTabs)](ohos-atomicservice-atomicservicetabs.md) |
| ArkUI | [@ohos.atomicservice.AtomicServiceWeb (AtomicServiceWeb)](ohos-atomicservice-atomicserviceweb.md) |
| ArkUI | [@ohos.atomicservice.HalfScreenLaunchComponent (HalfScreenLaunchComponent)](ohos-atomicservice-halfscreenlaunchcomponent.md) |
| ArkUI | [@ohos.atomicservice.InterstitialDialogAction (InterstitialDialogAction)](ohos-atomicservice-interstitialdialogaction.md) |
| ArkUI | [@ohos.atomicservice.NavPushPathHelper (NavPushPathHelper)](ohos-atomicservice-navpushpathhelper.md) |
| ArkUI | [@ohos.PiPWindow (画中画窗口)](js-apis-pipwindow.md) |
| ArkUI | [@ohos.mediaquery (媒体查询)](js-apis-mediaquery.md) |
| ArkUI | [@ohos.screenshot (屏幕截图)](js-apis-screenshot.md) |
| ArkWeb | [@ohos.web.netErrorList (ArkWeb网络协议栈错误列表)](arkts-apis-neterrorlist.md) |
| ArkWeb | [@ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)](arkts-apis-web-webnativemessagingextensionability.md) |
| ArkWeb | [@ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)](arkts-apis-web-webnativemessagingextensioncontext.md) |
| ArkWeb | [@ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)](arkts-apis-web-webnativemessagingextensionmanager.md) |
| ArkWeb | [@ohos.web.webview](arkts-apis-webview.md) |
| ArkWeb | [@ohos.web.webview (WebView)](arkts-apis-webview.md) |
| Audio Kit | [@ohos.multimedia.audioHaptic (音振协同)](js-apis-audiohaptic.md) |
| Audio Kit | [@ohos.multimedia.systemSoundManager (系统声音管理)](js-apis-systemsoundmanager.md) |
| Audio Kit | [@ohos.multimedia.avVolumePanel (音量面板)](ohos-multimedia-avvolumepanel.md) |
| AVSession Kit | [@ohos.multimedia.avCastPicker (投播组件)](ohos-multimedia-avcastpicker.md) |
| AVSession Kit | [@ohos.multimedia.avCastPickerParam (投播组件参数)](js-apis-avcastpickerparam.md) |
| AVSession Kit | [@ohos.multimedia.avInputCastPicker (录音设备选择组件)](ohos-multimedia-avinputcastpicker.md) |
| Basic Service Kit | [@ohos.pasteboard (剪贴板)](js-apis-pasteboard.md) |
| Basic Service Kit | [@ohos.scan (扫描)](js-apis-scan.md) |
| Basic Service Kit | [@ohos.screenLock (锁屏管理)](js-apis-screen-lock.md) |
| Basic Service Kit | [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| Basic Service Kit | [@ohos.settings (设置数据项名称)](js-apis-settings.md) |
| Calendar Kit | [@ohos.calendarManager (日程管理能力)](js-apis-calendarmanager.md) |
| Call Service Kit | [CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)](callservicekit-callerinfoquery-extension-ability.md) |
| Call Service Kit | [CallerInfoQueryExtensionContext（来去电信息查询扩展Context）](callservicekit-callerinfoquery-extension-context.md) |
| Call Service Kit | [voipCall（应用内通话管理）](call-voipcall.md) |
| Camera Kit | [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| Cloud Foundation Kit | [cloudCommon (公共模块)](cloudfoundation-cloudcommon.md) |
| Cloud Foundation Kit | [cloudDatabase (云数据库模块)](cloudfoundation-clouddatabase.md) |
| Cloud Foundation Kit | [cloudFunction (云函数模块)](cloudfoundation-cloudfunction.md) |
| Cloud Foundation Kit | [cloudResPrefetch（预加载模块）](cloudfoundation-cloudresprefetch.md) |
| Cloud Foundation Kit | [cloudStorage (云存储模块)](cloudfoundation-cloudstorage.md) |
| Connectivity Kit | [@ohos.bluetooth.a2dp (蓝牙a2dp模块)](js-apis-bluetooth-a2dp.md) |
| Connectivity Kit | [@ohos.bluetooth.access (蓝牙access模块)](js-apis-bluetooth-access.md) |
| Connectivity Kit | [@ohos.bluetooth.baseProfile (蓝牙baseProfile模块)](js-apis-bluetooth-baseprofile.md) |
| Connectivity Kit | [@ohos.bluetooth.ble (蓝牙ble模块)](js-apis-bluetooth-ble.md) |
| Connectivity Kit | [@ohos.bluetooth.common (蓝牙common模块)](js-apis-bluetooth-common.md) |
| Connectivity Kit | [@ohos.bluetooth.connection (蓝牙connection模块)](js-apis-bluetooth-connection.md) |
| Connectivity Kit | [@ohos.bluetooth.constant (蓝牙constant模块)](js-apis-bluetooth-constant.md) |
| Connectivity Kit | [@ohos.bluetooth (蓝牙)](js-apis-bluetooth.md) |
| Connectivity Kit | [@ohos.bluetooth.hfp (蓝牙hfp模块)](js-apis-bluetooth-hfp.md) |
| Connectivity Kit | [@ohos.bluetooth.hid (蓝牙hid模块)](js-apis-bluetooth-hid.md) |
| Connectivity Kit | [@ohos.bluetoothManager (蓝牙)](js-apis-bluetoothmanager.md) |
| Connectivity Kit | [@ohos.bluetooth.map (蓝牙map模块)](js-apis-bluetooth-map.md) |
| Connectivity Kit | [@ohos.bluetooth.pan (蓝牙pan模块)](js-apis-bluetooth-pan.md) |
| Connectivity Kit | [@ohos.bluetooth.pbap (蓝牙pbap模块)](js-apis-bluetooth-pbap.md) |
| Connectivity Kit | [@ohos.bluetooth.socket (蓝牙socket模块)](js-apis-bluetooth-socket.md) |
| Connectivity Kit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md) |
| Connectivity Kit | [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md) |
| Connectivity Kit | [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md) |
| Connectivity Kit | [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md) |
| Connectivity Kit | [@ohos.wifi (WLAN)](js-apis-wifi.md) |
| Connectivity Kit | [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md) |
| Connectivity Kit | [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md) |
| Connectivity Kit | [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md) |
| Contacts Kit | [@ohos.contact (联系人)](js-apis-contact.md) |
| Core Speech Kit | [speechRecognizer（语音识别）](hms-ai-speechrecognizer.md) |
| Core Speech Kit | [textToSpeech（文本转语音）](hms-ai-texttospeech.md) |
| Core Vision Kit | [faceComparator（人脸比对）](core-vision-facecomparator-api.md) |
| Core Vision Kit | [faceDetector（人脸检测）](core-vision-face-detector-api.md) |
| Core Vision Kit | [textRecognition（文字识别）](core-vision-text-recognition-api.md) |
| Core Vision Kit | [objectDetection（多目标识别）](core-vision-object-detection-api.md) |
| Core Vision Kit | [skeletonDetection（骨骼点检测）](core-vision-skeleton-detection-api.md) |
| Core Vision Kit | [subjectSegmentation（主体分割）](core-vision-subjectsegmentation-api.md) |
| Core Vision Kit | [visionBase（Core Vision Kit基类）](core-vision-vision-base-api.md) |
| Data Protection Kit | [@ohos.dlpPermission (数据防泄漏)](js-apis-dlppermission.md) |
| Distributed Service Kit | [@ohos.distributedDeviceManager (设备管理)](js-apis-distributeddevicemanager.md) |
| Distributed Service Kit | [@ohos.distributedsched.abilityConnectionManager (应用多端协同管理)](js-apis-distributed-abilityconnectionmanager.md) |
| Distributed Service Kit | [@ohos.distributedsched.linkEnhance (增强连接)](js-apis-link-enhance.md) |
| Distributed Service Kit | [@ohos.distributedsched.proxyChannelManager (代理通道管理)](js-apis-proxychannelmanager.md) |
| DRM Kit | [@ohos.multimedia.drm](arkts-apis-drm.md) |
| Form Kit | [@ohos.app.form.formBindingData (卡片数据绑定类)](js-apis-app-form-formbindingdata.md) |
| Form Kit | [@ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)](js-apis-app-form-formeditextensionability.md) |
| Form Kit | [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](js-apis-app-form-formextensionability.md) |
| Form Kit | [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md) |
| Form Kit | [@ohos.app.form.formProvider (formProvider)](js-apis-app-form-formprovider.md) |
| Game Service Kit | [gameNearbyTransfer（游戏近场快传）](gameservice-nearbytransfer.md) |
| Game Service Kit | [gamePerformance（游戏场景感知）](gameservice-gameperformance.md) |
| Game Service Kit | [gamePlayer（基础游戏服务）](gameservice-gameplayer.md) |
| Graphics Accelerate Kit | [AssetAccelerationExtensionAbility（资源加速ExtensionAbility）](graphics-accelerate-extensionability.md) |
| Graphics Accelerate Kit | [AssetAccelerationExtensionContext（资源加速ExtensionContext）](graphics-accelerate-extensioncontext.md) |
| Graphics Accelerate Kit | [assetDownloadManager（资源包下载管理）](graphics-accelerate-assetdownloadmanager.md) |
| Graphics Accelerate Kit | [launchAcceleration（游戏启动加速）](graphics-accelerate-launchacceleration.md) |
| Image Kit | [@ohos.multimedia.sendableImage (基于Sendable对象的图片处理)](js-apis-sendableimage.md) |
| Image Kit | [@ohos.multimedia.videoProcessingEngine (视频处理引擎)](js-apis-videoprocessingengine.md) |
| Intents Kit | [InsightIntentUIExtensionAbility (意图调用UI扩展能力)](intents-arkts-api-insightintent-uiextension.md) |
| Location Kit | [@ohos.geolocation (位置服务)](js-apis-geolocation.md) |
| Location Kit | [@ohos.geoLocationManager (位置服务)](js-apis-geolocationmanager.md) |
| Live View Kit | [LiveViewLockScreenExtensionAbility](liveview-lock-screen-ability.md) |
| Live View Kit | [LiveViewLockScreenExtensionContext](liveview-lock-screen-context.md) |
| Live View Kit | [liveViewManager](liveview-liveviewmanager.md) |
| MDM Kit | [@ohos.enterprise.accountManager（账号管理）](js-apis-enterprise-accountmanager.md) |
| MDM Kit | [@ohos.enterprise.adminManager（admin权限管理）](js-apis-enterprise-adminmanager.md) |
| MDM Kit | [@ohos.enterprise.applicationManager（应用管理）](js-apis-enterprise-applicationmanager.md) |
| MDM Kit | [@ohos.enterprise.bluetoothManager（蓝牙管理）](js-apis-enterprise-bluetoothmanager.md) |
| MDM Kit | [@ohos.enterprise.browser（浏览器管理）](js-apis-enterprise-browser.md) |
| MDM Kit | [@ohos.enterprise.bundleManager（包管理）](js-apis-enterprise-bundlemanager.md) |
| MDM Kit | [@ohos.enterprise.common（Enterprise公共模块）](js-apis-enterprise-common.md) |
| MDM Kit | [@ohos.enterprise.deviceControl（设备控制管理）](js-apis-enterprise-devicecontrol.md) |
| MDM Kit | [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
| MDM Kit | [@ohos.enterprise.deviceSettings （设备设置管理）](js-apis-enterprise-devicesettings.md) |
| MDM Kit | [@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）](js-apis-enterpriseadminextensionability.md) |
| MDM Kit | [@ohos.enterprise.locationManager（位置服务管理）](js-apis-enterprise-locationmanager.md) |
| MDM Kit | [@ohos.enterprise.networkManager（网络管理）](js-apis-enterprise-networkmanager.md) |
| MDM Kit | [@ohos.enterprise.restrictions （限制类策略）](js-apis-enterprise-restrictions.md) |
| MDM Kit | [@ohos.enterprise.securityManager（安全管理）](js-apis-enterprise-securitymanager.md) |
| MDM Kit | [@ohos.enterprise.systemManager （系统管理）](js-apis-enterprise-systemmanager.md) |
| MDM Kit | [@ohos.enterprise.telephonyManager（通话管理）](js-apis-enterprise-telephonymanager.md) |
| MDM Kit | [@ohos.enterprise.usbManager（USB管理）](js-apis-enterprise-usbmanager.md) |
| MDM Kit | [@ohos.enterprise.wifiManager（Wi-Fi管理）](js-apis-enterprise-wifimanager.md) |
| Media Library Kit | [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md) |
| Mechanic Kit | [@ohos.distributedHardware.mechanicManager (机械体控制模块)](js-apis-mechanicmanager.md) |
| MindSpore Lite Kit | [@ohos.ai.mindSporeLite (端侧AI框架)](js-apis-mindsporelite.md) |
| Natural Language Kit | [textProcessing（文本处理）](natural-language-text-processing-api.md) |
| NearLink Kit | [advertising（星闪广播能力）](nearlink-advertising.md) |
| NearLink Kit | [dataTransfer（星闪数传能力）](nearlink-data-transfer-api.md) |
| NearLink Kit | [remoteDevice（对端设备的连接能力）](nearlink-remote-device.md) |
| NearLink Kit | [scan（星闪扫描能力）](nearlink-scan.md) |
| NearLink Kit | [ssap（星闪SSAP连接能力）](nearlink-ssap.md) |
| Network Boost Kit | [netHandover（连接迁移）](networkboost-nethandover.md) |
| Network Boost Kit | [netBoost（网络加速）](networkboost-netboost.md) |
| Network Boost Kit | [netQuality（网络质量）](networkboost-netquality.md) |
| Network Kit | [@ohos.net.connection (网络连接管理)](js-apis-net-connection.md) |
| Network Kit | [@ohos.net.eap (扩展认证)](js-apis-net-eap.md) |
| Network Kit | [@ohos.net.ethernet (以太网连接管理)](js-apis-net-ethernet.md) |
| Network Kit | [@ohos.net.http (数据请求)](js-apis-http.md) |
| Network Kit | [@ohos.net.mdns (MDNS管理)](js-apis-net-mdns.md) |
| Network Kit | [@ohos.net.netFirewall (网络防火墙)](js-apis-net-netfirewall.md) |
| Network Kit | [@ohos.net.networkSecurity (网络安全校验)](js-apis-networksecurity.md) |
| Network Kit | [@ohos.net.policy (网络策略管理)](js-apis-net-policy.md) |
| Network Kit | [@ohos.net.sharing (网络共享管理)](js-apis-net-sharing.md) |
| Network Kit | [@ohos.net.socket (Socket连接)](js-apis-socket.md) |
| Network Kit | [@ohos.net.statistics (流量管理)](js-apis-net-statistics.md) |
| Network Kit | [@ohos.net.vpn (VPN管理)](js-apis-net-vpn.md) |
| Network Kit | [@ohos.net.vpnExtension (VPN增强管理)](js-apis-net-vpnextension.md) |
| Network Kit | [@ohos.net.webSocket (WebSocket连接)](js-apis-websocket.md) |
| Payment Kit | [ecnyPaymentService (数字人民币服务)](payment-ecnypaymentservice.md) |
| Payment Kit | [paymentService (鸿蒙支付服务)](payment-paymentservice.md) |
| Payment Kit | [realNameService(身份验证服务)](payment-realnameservice.md) |
| Payment Kit | [thirdPaymentService(三方支付服务)](payment-third-payment-service.md) |
| Push Kit | [pushCommon（推送服务公共信息）](push-pushcommon.md) |
| Push Kit | [PushExtensionAbility（推送扩展Ability）](push-extension-ability.md) |
| Push Kit | [PushExtensionContext（推送扩展Context）](push-extension-context.md) |
| Push Kit | [pushService（推送服务基础能力）](push-pushservice.md) |
| Push Kit | [RemoteLocationExtensionAbility（定位扩展Ability）](remote-location-ability.md) |
| Push Kit | [RemoteLocationExtensionContext（定位扩展Context）](remote-location-context.md) |
| Push Kit | [RemoteNotificationExtensionAbility（通知扩展Ability）](push-remote-notification-extension-ability.md) |
| Push Kit | [RemoteNotificationExtensionContext（通知扩展Context）](push-remote-notification-extension-context.md) |
| Push Kit | [serviceNotification（服务通知）](push-servicenotification.md) |
| Push Kit | [VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃）](push-voip-ability.md) |
| Push Kit | [VoIPExtensionContext（应用内通话消息扩展Context）（废弃）](push-voip-context.md) |
| Remote Communication Kit | [urpc（高性能rpc通信库）](remote-communication-urpcapi.md) |
| Remote Communication Kit | [rcp（数据请求）](remote-communication-rcp.md) |
| Service Collaboration Kit | [CollaborationService (跨设备互通组件)](servicecollaboration-collaborationservice.md) |
| Service Collaboration Kit | [CollaborationCamera (跨设备互通组件)](servicecollaboration-collaborationcamera.md) |
| Service Collaboration Kit | [CollaborationDevicePicker（流转控件）](servicecollaboration-collaborationdevicepicker.md) |
| Service Collaboration Kit | [devicePicker（设备选择控制器）](servicecollaboration-devicepicker.md) |
| Share Kit | [harmonyShare（华为分享）](share-harmony-share.md) |
| Share Kit | [systemShare（分享）](share-system-share.md) |
| Speech Kit | [TextReader（朗读控件）](speech-textreader-api.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md) |
| Telephony Kit | [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md) |
| Telephony Kit | [@ohos.telephony.esim (eSIM卡管理)](js-apis-esim.md) |
| Telephony Kit | [@ohos.telephony.observer (observer)](js-apis-observer.md) |
| Telephony Kit | [@ohos.telephony.radio (网络搜索)](js-apis-radio.md) |
| Telephony Kit | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| Telephony Kit | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| Telephony Kit | [@ohos.telephony.vcard (VCard模块)](js-apis-vcard.md) |
| Vision Kit | [CardRecognition（卡证识别控件）](vision-card-recognition.md) |
| Vision Kit | [DocumentScanner（文档扫描控件）](vision-document-scanner.md) |
| Vision Kit | [interactiveLiveness（人脸活体检测）](vision-interactive-liveness.md) |
| Vision Kit | [visionImageAnalyzer（AI识图控件）](vision-image-analyzer.md) |
| Wallet Kit | [walletPass（Pass卡片能力）](wallet-walletpass.md) |
| Wallet Kit | [walletTransitCard（交通卡能力）](wallet-wallettransitcard.md) |
