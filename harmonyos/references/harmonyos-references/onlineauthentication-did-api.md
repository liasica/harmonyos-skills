---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-did-api
title: DID
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > DID
category: harmonyos-references
scraped_at: 2026-09-02T14:52:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3933e4246ba52c782b21659daa7023531aa4f168630e08f6ecc0414ed54eef2
---

DID（Decentralized Identifier，去中心化身份）能力。

DID提供基于W3C DID标准的身份认证和可验证凭证管理能力，支持DID密钥生成、数字凭证导入/查询/删除、数据签名等功能，提供去中心化身份认证和可验证凭证管理能力。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
```

## KeyAlgo

密钥算法枚举，用于DID密钥生成。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SM2 | 1 | 国家商用密码方案，SM2非对称密码算法。 |
| SM4 | 2 | 国家商用密码方案，SM4对称密码算法。 |
| P256 | 3 | 椭圆曲线密码算法，P256类型。 |
| ED25519 | 4 | 椭圆曲线密码算法，ED25519类型。 |
| AES128 | 5 | AES128密码算法。 |
| AES256 | 6 | AES256密码算法。 |

## AuthType

认证器认证类型枚举，包括PIN码、指纹、3D人脸。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| UVM\_PIN | 1 | PIN认证器。 |
| UVM\_FACE | 2 | 3D人脸认证器。 |
| UVM\_FINGERPRINT | 4 | 指纹认证器。 |

## KeyPurpose

密钥用途枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| ENCRYPT | 1 | 加密。 |
| DECRYPT | 2 | 解密。 |
| SIGN | 3 | 签名。 |
| VERIFY | 4 | 验签。 |

## CredentialType

凭证类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| VC | 1 | W3C协议定义的可验证凭证。 |
| VP | 2 | W3C协议定义的可验证表达。 |
| SELECTIVE\_DISCLOSURE\_VC | 3 | 选择性披露凭证。 |
| SELECTIVE\_DISCLOSURE\_VP | 4 | 选择性披露表达。 |

## CryptoScheme

加密方案枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| IFAA\_FIXED\_ENVELOPE | 1 | IFAA固定信封。 |
| IFAA\_SEPARATE\_DECLARE\_ENVELOPE | 2 | IFAA分离声明信封。 |

## ApprovalScheme

批准方案枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| IFAA\_OPERATOR\_APPROVAL | 1 | IFAA操作员批准。 |

## AuthMode

认证模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SINGLE | 1 | 生物特征独立验证，即在创建DID和展示证书时各进行一次生物特征验证。 |

## KeyConfig

DID密钥生成配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algorithm | [KeyAlgo](onlineauthentication-did-api.md#keyalgo) | 否 | 否 | 密钥生成算法。 |
| purposeList | [KeyPurpose](onlineauthentication-did-api.md#keypurpose)[] | 否 | 否 | 密钥生成用途列表。表示密钥用途。一个密钥仅能用于单类用途，不能既用于加解密又用于签名验签。创建加解密密钥时，传入[1, 2]；创建签名验签密钥时，传入[3, 4] |

## AuthenticatorConfig

认证器配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authTypeList | [AuthType](onlineauthentication-did-api.md#authtype)[] | 否 | 否 | 使用的认证器类型列表。 |
| requireBioId | boolean | 否 | 是 | true表示返回生物特征/PIN认证凭证ID，false表示不返回，默认false不返回。 |
| authMode | [AuthMode](onlineauthentication-did-api.md#authmode) | 否 | 是 | 认证模式。默认值为1，生物特征独立验证。 |

## GenerateKeyRequest

DID密钥生成请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyAlias | string | 否 | 否 | 新DID密钥的别名。最大长度为128字节，建议不包含个人信息等敏感词汇。默认值为空。 |
| keyConfig | [KeyConfig](onlineauthentication-did-api.md#keyconfig) | 否 | 否 | 新DID密钥的配置。 |
| authenticatorConfig | [AuthenticatorConfig](onlineauthentication-did-api.md#authenticatorconfig) | 否 | 是 | 新DID密钥的认证器配置。如果为空，表示该密钥不需要生物认证访问控制。 |
| extension | string | 否 | 是 | 新DID密钥的扩展信息。最大长度为1024字节。默认值为空。目前支持以下扩展信息 - {"systemPrompt": "half\_modal"}，表示需要系统半模态提示。{"systemPrompt": "none"}，表示无需提示。 |

## GenerateKeyResponse

DID密钥生成响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| publicKey | Uint8Array | 否 | 否 | 新DID密钥的公钥。ASN1格式。 |
| bioId | string | 否 | 是 | 认证器凭证ID。最大长度为1024字节。默认值为空。 |
| certChain | Array<Uint8Array> | 否 | 否 | DID密钥的证书链。 |
| extension | string | 否 | 是 | 扩展信息。最大长度为10000字节。默认值为空。 |

## DidKey

DID密钥信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyAlias | string | 否 | 是 | DID密钥别名。最大长度为128字节。默认值为空。 |
| keyId | string | 否 | 是 | DID密钥ID。最大长度为256字节。默认值为空。 |

## ImportDidRequest

DID导入请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isUpdate | boolean | 否 | 是 | true表示更新DID信息，false表示导入DID信息，默认false为导入。 |
| did | string | 否 | 否 | DID标识符。最大长度为256字节。默认值为空。 |
| didKeyList | [DidKey](onlineauthentication-did-api.md#didkey)[] | 否 | 否 | DID的密钥列表。 |
| didDoc | string | 否 | 是 | W3C DID协议的DID文档。长度限制10000字节。默认值为空。 |
| additionalData | string | 否 | 是 | DID的附加数据。长度限制10000字节。默认值为空。 |

## SignRequest

数据签名请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inData | Uint8Array | 否 | 否 | 待签名的输入数据。 |
| keyId | string | 否 | 否 | DID密钥的keyId。最大长度为256字节。默认值为空。 |

## SignResponse

数据签名响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| outData | Uint8Array | 否 | 否 | 签名后的输出数据。ASN1格式。 |
| bioId | string | 否 | 是 | 认证器凭证ID。最大长度为1024字节。默认值为空。 |

## QueryDidConfig

DID查询配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requireDidKey | boolean | 否 | 是 | true表示返回DID密钥，false表示不返回，默认false不返回。 |
| requireDidDoc | boolean | 否 | 是 | true表示返回DID文档，false表示不返回，默认false不返回。 |
| requireAdditionalData | boolean | 否 | 是 | true表示返回附加数据，false表示不返回，默认false不返回。 |

## QueryDidRequest

DID查询请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| did | string | 否 | 否 | DID标识符。最大长度为256字节。默认值为空。 |
| queryDidConfig | [QueryDidConfig](onlineauthentication-did-api.md#querydidconfig) | 否 | 是 | DID查询配置。 |

## QueryDidResponse

DID查询响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| didKeyList | [DidKey](onlineauthentication-did-api.md#didkey)[] | 否 | 是 | DID的密钥列表。 |
| didDoc | string | 否 | 是 | W3C DID协议的DID文档。最大长度为10000字节。默认值为空。 |
| additionalData | string | 否 | 是 | DID的附加数据。最大长度为10000字节。默认值为空。 |

## EncryptConfig

加密方案配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cryptoScheme | [CryptoScheme](onlineauthentication-did-api.md#cryptoscheme) | 否 | 否 | 加密方案。 |
| encryptKey | Uint8Array | 否 | 否 | 加密密钥。 |
| keyId | string | 否 | 是 | DID密钥ID。最大长度为256字节。默认值为空。 |
| algorithm | [KeyAlgo](onlineauthentication-did-api.md#keyalgo) | 否 | 否 | 加密算法。 |

## ApprovalData

批准数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| approvalScheme | [ApprovalScheme](onlineauthentication-did-api.md#approvalscheme) | 否 | 否 | 批准方案。 |
| data | string | 否 | 是 | 批准数据。最大长度为10000字节。默认值为空。 |

## DecryptConfig

解密方案配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cryptoScheme | [CryptoScheme](onlineauthentication-did-api.md#cryptoscheme) | 否 | 否 | 解密方案。 |
| keyId | string | 否 | 否 | DID密钥ID。最大长度为256字节。默认值为空。 |
| data | string | 否 | 是 | 解密数据。最大长度为10000字节。默认值为空。 |

## ApprovalConfig

批准配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| approvalScheme | [ApprovalScheme](onlineauthentication-did-api.md#approvalscheme) | 否 | 否 | 批准方式。 |
| publicKey | Uint8Array | 否 | 否 | 公钥。 |
| algorithm | [KeyAlgo](onlineauthentication-did-api.md#keyalgo) | 否 | 否 | 算法。 |

## CredentialDisplayConfig

凭证显示配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialDisplayName | string | 否 | 否 | 凭证显示名称。最大长度为1024字节。默认值为空。 |
| issuerDisplayName | string | 否 | 否 | 发行方显示名称。最大长度为1024字节。默认值为空。 |
| propertyDisplayName | string | 否 | 否 | 属性显示名称。最大长度为10000字节。默认值为空。 |

## AuthConfig

认证配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requireAuth | boolean | 否 | 是 | true表示需要用户身份认证，false表示不需要，默认false不需要。 |

## CredentialSecurityConfig

凭证安全配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| approvalConfig | [ApprovalConfig](onlineauthentication-did-api.md#approvalconfig) | 否 | 是 | 批准配置。 |
| decryptConfig | [DecryptConfig](onlineauthentication-did-api.md#decryptconfig) | 否 | 是 | 解密配置。 |
| authConfig | [AuthConfig](onlineauthentication-did-api.md#authconfig) | 否 | 是 | 认证配置。 |

## ImportDigitalCredentialRequest

数字凭证导入请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| did | string | 否 | 否 | DID标识符。长度限制为256字节。默认值为空。 |
| credentialType | [CredentialType](onlineauthentication-did-api.md#credentialtype) | 否 | 是 | 数字凭证类型。 |
| isUpdate | boolean | 否 | 是 | true表示更新凭证信息，false表示导入凭证信息，默认false为导入。 |
| securityConfig | [CredentialSecurityConfig](onlineauthentication-did-api.md#credentialsecurityconfig) | 否 | 是 | 凭证的安全配置。 |
| credentialData | string | 否 | 否 | 凭证数据，当前仅支持导入W3C协议标准中的VC格式。长度限制为10000字节。默认值为空。 |
| displayConfig | [CredentialDisplayConfig](onlineauthentication-did-api.md#credentialdisplayconfig) | 否 | 否 | 显示配置。 |
| extension | string | 否 | 是 | 扩展信息。最大长度为10000字节。默认值为空。 |

## ImportDigitalCredentialResponse

数字凭证导入响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialSummary | string | 否 | 否 | 数字凭证的摘要信息。最大长度为10000字节。默认值为空。 |

## HolderConfig

持有者配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| holderDid | string | 否 | 否 | 持有者DID。最大长度为1024字节。默认值为空。 |
| holderDidKeyId | string | 否 | 否 | 持有者DID密钥ID。最大长度为1024字节。默认值为空。 |

## CredentialFilter

数字凭证过滤条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialId | string | 否 | 是 | 数字凭证ID。最大长度为256字节。默认值为空。 |
| issuerDid | string | 否 | 是 | 发行方DID。最大长度为1024字节。默认值为空。 |
| credentialProvider | string | 否 | 是 | 凭证提供方。最大长度为1024字节。默认值为空。 |
| credentialDisclosurePropertyList | string[] | 否 | 是 | 凭证披露属性列表。默认值为空。 |
| credentialDisplayConfig | [CredentialDisplayConfig](onlineauthentication-did-api.md#credentialdisplayconfig) | 否 | 是 | 凭证显示配置。 |
| credentialCategory | string | 否 | 是 | 凭证类型。最大长度为1024字节。默认值为空。 |
| extension | string | 否 | 是 | 扩展信息。最大长度为1024字节。默认值为空。 |

## PresentDisplayConfig

出示显示配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verifierDisplayName | string | 否 | 否 | 验证方显示名称。最大长度为1024字节。默认值为空。 |
| purpose | string | 否 | 否 | 用途。最大长度为1024字节。默认值为空。 |
| extension | string | 否 | 是 | 扩展信息。最大长度为10000字节。默认值为空。 |

## GetDigitalCredentialRequest

获取数字凭证请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialType | [CredentialType](onlineauthentication-did-api.md#credentialtype) | 否 | 是 | 凭证类型。 |
| displayConfig | [PresentDisplayConfig](onlineauthentication-did-api.md#presentdisplayconfig) | 否 | 否 | 显示配置。 |
| verifierDid | string | 否 | 是 | 验证方DID。最大长度为1024字节。默认值为空。 |
| encryptConfig | [EncryptConfig](onlineauthentication-did-api.md#encryptconfig) | 否 | 是 | 加密配置。 |
| approvalData | [ApprovalData](onlineauthentication-did-api.md#approvaldata) | 否 | 是 | 批准数据。 |
| holderConfigList | [HolderConfig](onlineauthentication-did-api.md#holderconfig)[] | 否 | 否 | 持有者配置列表。 |
| credentialFilterList | [CredentialFilter](onlineauthentication-did-api.md#credentialfilter)[] | 否 | 是 | 凭证过滤条件列表。 |
| extension | string | 否 | 是 | 扩展信息。最大长度为1024字节。默认值为空。 |

## QueryDigitalCredentialResponse

查询数字凭证响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialSummaryList | string[] | 否 | 否 | 数字凭证摘要列表。 |

## GetDigitalCredentialResponse

获取数字凭证响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialData | string | 否 | 否 | 凭证数据，当前仅支持W3C协议标准中的VC/VP格式。最大长度为1024字节。默认值为空。 |
| bioId | string | 否 | 是 | 认证器凭证ID。最大长度为1024字节。默认值为空。 |

## did.generateKey

generateKey(context: common.Context, generateKeyRequest: GenerateKeyRequest): Promise<GenerateKeyResponse>

生成DID密钥。使用Promise异步回调。DID密钥数量上限（500个）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| generateKeyRequest | [GenerateKeyRequest](onlineauthentication-did-api.md#generatekeyrequest) | 是 | DID密钥生成参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GenerateKeyResponse](onlineauthentication-did-api.md#generatekeyresponse)> | Promise对象，返回DID密钥生成结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600002 | The user does not record biometric features or the authentication module is abnormal. |
| 1024600003 | The user canceled the operation. |
| 1024600004 | The key alias has been used. |
| 1024600006 | The security level of the authenticator on the device is lower than ATL4. |
| 1024600007 | Unknown error. |
| 1024600012 | The number of did keys has reached the maximum limit. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let generateKeyRequest: did.GenerateKeyRequest = {
  keyAlias: 'myDidKey',
  keyConfig: {
    algorithm: did.KeyAlgo.SM2,
    purposeList: [did.KeyPurpose.SIGN, did.KeyPurpose.VERIFY]
  },
  authenticatorConfig: {
    authTypeList: [did.AuthType.UVM_FINGERPRINT],
    requireBioId: true
  }
};

try {
  let response: did.GenerateKeyResponse = await did.generateKey(context, generateKeyRequest);
  console.info('Succeeded in generating did key', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to generate did key. Code: ${err.code}, message: ${err.message}`);
}
```

## did.importDid

importDid(context: common.Context, importDidRequest: ImportDidRequest): Promise<void>

导入DID信息。使用Promise异步回调。DID数量上限（50个）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| importDidRequest | [ImportDidRequest](onlineauthentication-did-api.md#importdidrequest) | 是 | 导入DID的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600005 | The key is invalid. |
| 1024600007 | Unknown error. |
| 1024600008 | The DID does not exist. |
| 1024600011 | The application does not have permission to perform this operation. |
| 1024600013 | The number of DIDs has reached the maximum limit. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let importDidRequest: did.ImportDidRequest = {
  isUpdate: false,
  did: 'did:example:123456',
  didKeyList: [{
    keyAlias: 'myDidKey',
    keyId: 'keyId123'
  }],
  didDoc: JSON.stringify({
    '@context': 'https://www.w3.org/ns/did/v1',
    id: 'did:example:123456'
  })
};

try {
  await did.importDid(context, importDidRequest);
  console.info('Succeeded in importing did');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to import did. Code: ${err.code}, message: ${err.message}`);
}
```

## did.queryDid

queryDid(context: common.Context, queryDidRequest: QueryDidRequest): Promise<QueryDidResponse>

查询DID信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| queryDidRequest | [QueryDidRequest](onlineauthentication-did-api.md#querydidrequest) | 是 | 查询DID的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryDidResponse](onlineauthentication-did-api.md#querydidresponse)> | Promise对象，返回查询DID的响应。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600007 | Unknown error. |
| 1024600008 | The DID does not exist. |
| 1024600011 | The application does not have permission to perform this operation. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let queryDidRequest: did.QueryDidRequest = {
  did: 'did:example:123456',
  queryDidConfig: {
    requireDidKey: true,
    requireDidDoc: true,
    requireAdditionalData: true
  }
};

try {
  let response: did.QueryDidResponse = await did.queryDid(context, queryDidRequest);
  console.info('Succeeded in querying did', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to query did. Code: ${err.code}, message: ${err.message}`);
}
```

## did.deleteDid

deleteDid(context: common.Context, did: string): Promise<void>

删除DID。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| did | string | 是 | 要删除的DID标识符。最大长度为256字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600007 | Unknown error. |
| 1024600008 | The DID does not exist. |
| 1024600011 | The application does not have permission to perform this operation. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

try {
  await did.deleteDid(context, 'did:example:123456');
  console.info('Succeeded in deleting did');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to delete did. Code: ${err.code}, message: ${err.message}`);
}
```

## did.sign

sign(context: common.Context, signRequest: SignRequest): Promise<SignResponse>

数据签名。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| signRequest | [SignRequest](onlineauthentication-did-api.md#signrequest) | 是 | 数据签名参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SignResponse](onlineauthentication-did-api.md#signresponse)> | Promise对象，返回数据签名结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600002 | The user does not record biometric features or the authentication module is abnormal. |
| 1024600003 | The user canceled the operation. |
| 1024600005 | The key is invalid. |
| 1024600007 | Unknown error. |
| 1024600011 | The application does not have permission to perform this operation. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let signRequest: did.SignRequest = {
  inData: new Uint8Array([0x01, 0x02, 0x03]),
  keyId: 'keyId123'
};

try {
  let response: did.SignResponse = await did.sign(context, signRequest);
  console.info('Succeeded in signing data', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to sign data. Code: ${err.code}, message: ${err.message}`);
}
```

## did.importDigitalCredential

importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>

导入数字凭证。使用Promise异步回调。凭证数量上限（1000个）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**申请权限：** ohos.permission.ACCESS\_DIGITAL\_IDENTITY

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| importDigitalCredentialRequest | [ImportDigitalCredentialRequest](onlineauthentication-did-api.md#importdigitalcredentialrequest) | 是 | 导入数字凭证的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImportDigitalCredentialResponse](onlineauthentication-did-api.md#importdigitalcredentialresponse)> | Promise对象，返回导入数字凭证的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600005 | The key is invalid. |
| 1024600007 | Unknown error. |
| 1024600008 | The DID does not exist. |
| 1024600009 | Failed to decrypt the credential. |
| 1024600014 | The number of credentials has reached the maximum limit. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let importDigitalCredentialRequest: did.ImportDigitalCredentialRequest = {
  did: 'did:example:123456',
  credentialType: did.CredentialType.VC,
  isUpdate: false,
  credentialData: JSON.stringify({
    '@context': ['https://www.w3.org/2018/credentials/v1'],
    type: ['VerifiableCredential'],
    issuer: 'did:example:issuer123',
    issuanceDate: '2024-01-01T00:00:00Z',
    credentialSubject: {
      id: 'did:example:123456',
      name: 'Alice'
    }
  }),
  displayConfig: {
    credentialDisplayName: '身份证',
    issuerDisplayName: '公安部门',
    propertyDisplayName: '姓名'
  }
};

try {
  let response: did.ImportDigitalCredentialResponse =
    await did.importDigitalCredential(context, importDigitalCredentialRequest);
  console.info('Succeeded in importing digital credential', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to import digital credential. Code: ${err.code}, message: ${err.message}`);
}
```

## did.queryDigitalCredential

queryDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<QueryDigitalCredentialResponse>

查询数字凭证。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| did | string | 否 | DID标识符。最大长度为256字节。默认值为空。 |
| credentialId | string | 否 | 数字凭证ID。最大长度为256字节。默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryDigitalCredentialResponse](onlineauthentication-did-api.md#querydigitalcredentialresponse)> | Promise对象，返回查询数字凭证的响应。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600007 | Unknown error. |
| 1024600010 | The credential does not exist. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

try {
  let response: did.QueryDigitalCredentialResponse = await did.queryDigitalCredential(context, 'did:example:123456');
  console.info('Succeeded in querying digital credential', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to query digital credential. Code: ${err.code}, message: ${err.message}`);
}
```

## did.deleteDigitalCredential

deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>

删除数字凭证。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**申请权限：** ohos.permission.ACCESS\_DIGITAL\_IDENTITY

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| did | string | 否 | DID标识符。最大长度为256字节。默认值为空。 |
| credentialId | string | 否 | 数字凭证ID。最大长度为256字节。默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600007 | Unknown error. |
| 1024600010 | The credential does not exist. |
| 1024600011 | The application does not have permission to perform this operation. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

try {
  await did.deleteDigitalCredential(context, 'did:example:123456', 'credentialId123');
  console.info('Succeeded in deleting digital credential');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to delete digital credential. Code: ${err.code}, message: ${err.message}`);
}
```

## did.getDigitalCredential

getDigitalCredential(context: common.Context, getDigitalCredentialRequest: GetDigitalCredentialRequest): Promise<GetDigitalCredentialResponse>

获取数字凭证。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DID

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Ability的上下文。 |
| getDigitalCredentialRequest | [GetDigitalCredentialRequest](onlineauthentication-did-api.md#getdigitalcredentialrequest) | 是 | 获取数字凭证的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GetDigitalCredentialResponse](onlineauthentication-did-api.md#getdigitalcredentialresponse)> | Promise对象，返回获取数字凭证的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[DID错误码](errorcode-onlineauthentication-did.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Invalid device type. |
| 1024600001 | Invalid parameters. |
| 1024600002 | The user does not record biometric features or the authentication module is abnormal. |
| 1024600003 | The user canceled the operation. |
| 1024600006 | The security level of the authenticator on the device is lower than ATL4. |
| 1024600007 | Unknown error. |
| 1024600010 | The credential does not exist. |

**示例：**

```typescript
import { did } from '@kit.OnlineAuthenticationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 以下获取context的代码要放进UI组件类中调用
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let getDigitalCredentialRequest: did.GetDigitalCredentialRequest = {
  credentialType: did.CredentialType.VC,
  displayConfig: {
    verifierDisplayName: '验证方',
    purpose: '身份验证'
  },
  holderConfigList: [{
    holderDid: 'did:example:123456',
    holderDidKeyId: 'keyId123'
  }]
};

try {
  let response: did.GetDigitalCredentialResponse = await did.getDigitalCredential(context, getDigitalCredentialRequest);
  console.info('Succeeded in getting digital credential', response);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to get digital credential. Code: ${err.code}, message: ${err.message}`);
}
```
