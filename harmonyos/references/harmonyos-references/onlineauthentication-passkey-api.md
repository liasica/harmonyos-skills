---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-passkey-api
title: 通行密钥
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > 通行密钥
category: harmonyos-references
scraped_at: 2026-09-02T14:52:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4f42a17f6071d4a478585595d518d634a9406528c33580dc56a3e791bc89c310
---

本模块主要提供了以下能力：

* 通行密钥注册：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，在本设备上创建应用或网页的通行密钥。
* 本地免密认证：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，使用通行密钥在本设备上进行应用或网页的免密认证。
* 跨设备扫码认证：支持使用已注册通行密钥的移动设备作为漫游认证器，使用跨设备扫码的方式，在其他设备上进行应用或网页的免密认证。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { fido2 } from '@kit.OnlineAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

## AuthenticatorAttestationResponse

以Uint8Array格式表示的认证器证明响应。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attestationObject | Uint8Array | 是 | 否 | 注册凭证的响应报文中，用于向服务器证明新生成密钥对合法性的数据结构。 |
| clientDataJson | Uint8Array | 是 | 否 | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| publicKeyAlgorithm | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 密码算法。 |
| publicKey | Uint8Array | 否 | 是 | 注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。默认值为空。 |
| authenticatorData | Uint8Array | 否 | 否 | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。 |
| transports | string[] | 否 | 否 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举。 |

## AuthenticatorAttestationResponseJson

认证器证明响应，JSON字符串的结构。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientDataJson | string | 否 | 否 | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。长度限制0到4096。 |
| authenticatorData | string | 否 | 否 | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。长度限制0到4096。 |
| transports | Array<string> | 否 | 否 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举。 |
| publicKey | string | 否 | 是 | 注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。默认值为空。长度限制0到4096。 |
| publicKeyAlgorithm | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 密码算法。 |
| attestationObject | string | 否 | 否 | 注册凭证的响应报文中，用于向服务器证明新生成密钥对合法性的数据结构。长度限制0到10000。 |

## AuthenticationExtensionsClientOutputsJson

当依赖方调用 create() 或 get() 时，处理依赖方请求的客户端扩展的结果。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

## AuthenticatorAssertionResponseJson

认证器断言响应，JSON字符串的结构。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientDataJson | string | 否 | 否 | 客户端数据。长度限制0到4096。 |
| authenticatorData | string | 否 | 否 | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。长度限制0到4096。 |
| signature | string | 否 | 否 | FIDO2认证的签名信息。长度限制0到4096。 |
| userHandle | string | 否 | 是 | 用户句柄。默认值为空。长度限制0到4096。 |

## AuthenticatorAssertionResponse

认证器断言响应。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authenticatorData | Uint8Array | 是 | 否 | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。 |
| signature | Uint8Array | 是 | 否 | FIDO2认证的签名信息。 |
| userHandle | Uint8Array | 是 | 是 | 用户句柄。默认值为空。 |
| clientDataJson | Uint8Array | 是 | 否 | 客户端数据。 |

## AuthenticationExtensionsClientOutputs

身份认证扩展输出。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

## PublicKeyAttestationCredential

注册返回参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rawId | Uint8Array | 是 | 否 | 凭据唯一索引。 |
| response | [AuthenticatorAttestationResponse](onlineauthentication-passkey-api.md#authenticatorattestationresponse) | 是 | 否 | 返回报文。 |
| authenticatorAttachment | [AuthenticatorAttachment](onlineauthentication-passkey-api.md#authenticatorattachment) | 是 | 是 | 认证器信息（平台、漫游），默认值为platform。 |
| id | string | 是 | 否 | 凭据ID（base64格式）。长度限制0到512。 |
| type | string | 是 | 否 | 凭据类型。长度限制0到512。 |
| clientExtensionResults | [AuthenticationExtensionsClientOutputs](onlineauthentication-passkey-api.md#authenticationextensionsclientoutputs) | 是 | 否 | 客户端扩展结果。 |
| registrationResponseJson | [RegistrationResponseJson](onlineauthentication-passkey-api.md#registrationresponsejson) | 否 | 否 | 认证结果，JSON格式。 |

## RegistrationResponseJson

注册返回参数的JSON格式。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。长度限制0到512。 |
| rawId | string | 否 | 否 | 原始凭据ID。长度限制0到512。 |
| response | [AuthenticatorAttestationResponseJson](onlineauthentication-passkey-api.md#authenticatorattestationresponsejson) | 否 | 否 | 认证器证明响应。 |
| authenticatorAttachment | string | 否 | 是 | 认证器信息（平台、漫游），默认值为platform。长度限制0到512。 |
| clientExtensionResults | [AuthenticationExtensionsClientOutputsJson](onlineauthentication-passkey-api.md#authenticationextensionsclientoutputsjson) | 否 | 否 | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |
| type | string | 否 | 否 | 该属性返回对象的接口对象的插槽的值，它指定此对象所表示的凭据类型。长度限制0到512。 |

## PublicKeyCredentialRequestOptions

定义通行密钥认证请求参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| challenge | Uint8Array | 否 | 否 | 获取挑战值。 |
| timeout | number | 否 | 是 | 超时时间。单位为ms。默认为300000（5分钟），限制为0到600000（10分钟）。 |
| rpId | string | 否 | 是 | 依赖方标识。默认值为空。长度限制0到512。 |
| allowCredentials | Array<[PublicKeyCredentialDescriptor](onlineauthentication-passkey-api.md#publickeycredentialdescriptor)> | 否 | 是 | 认证凭据的附加参数列表。默认值为空。 |
| userVerification | [UserVerificationRequirement](onlineauthentication-passkey-api.md#userverificationrequirement) | 否 | 是 | 用户认证需求枚举。默认值为FIDO2\_PREFERRED。 |
| hints | Array<[PublicKeyCredentialHint](onlineauthentication-passkey-api.md#publickeycredentialhint)> | 否 | 是 | 认证方式指示。默认值为[]。 |
| extensions | Map<string, Object> | 否 | 是 | 扩展名必须是表示Map<string，Object> object的JSON字符串。默认值为空。 |

## PublicKeyAssertionCredential

认证返回参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rawId | Uint8Array | 是 | 否 | 凭据唯一索引。 |
| response | [AuthenticatorAssertionResponse](onlineauthentication-passkey-api.md#authenticatorassertionresponse) | 是 | 否 | 返回报文。 |
| authenticatorAttachment | [AuthenticatorAttachment](onlineauthentication-passkey-api.md#authenticatorattachment) | 是 | 是 | 认证器信息（平台、漫游），默认值为platform。 |
| id | string | 是 | 否 | 凭据ID（base64格式）。长度限制0到512。 |
| type | string | 是 | 否 | 凭据类型。长度限制0到512。 |
| clientExtensionResults | [AuthenticationExtensionsClientOutputs](onlineauthentication-passkey-api.md#authenticationextensionsclientoutputs) | 否 | 否 | 客户端扩展结果。 |
| authenticationResponseJson | [AuthenticationResponseJson](onlineauthentication-passkey-api.md#authenticationresponsejson) | 否 | 否 | 认证响应数据，格式为JSON字符串。 |

## AuthenticationResponseJson

认证返回参数的JSON格式。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 凭据的标识符，作为JSON字符串。对于每种类型的凭据，标识符的要求都是不同的。长度限制0到512。 |
| rawId | string | 否 | 否 | 原始凭据Id，格式为JSON字符串。长度限制0到512。 |
| response | [AuthenticatorAssertionResponseJson](onlineauthentication-passkey-api.md#authenticatorassertionresponsejson) | 否 | 否 | 认证器断言响应，JSON字符串的结构。 |
| authenticatorAttachment | string | 否 | 是 | 认证器信息（平台、漫游），默认值为platform。长度限制0到512。 |
| clientExtensionResults | [AuthenticationExtensionsClientOutputsJson](onlineauthentication-passkey-api.md#authenticationextensionsclientoutputsjson) | 否 | 否 | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |
| type | string | 否 | 否 | 该属性以JSON字符串形式返回对象的接口对象的插槽的值，该插槽指定此对象所表示的凭据类型。长度限制0到512。 |

## CredentialMediationRequirement

用户介入要求的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| SILENT | 'silent' | 禁止用户介入指定的操作。如果可以在不需要用户介入的情况下进行操作，则正常。 如果需要用户介入，则操作将返回null。 |
| OPTIONAL | 'optional' | 如果在没有用户介入的情况下，可以为给定的操作传递凭据，则正常传递。 如果需要用户介入，那么用户代理将让用户介入决策。 |
| CONDITIONAL | 'conditional' | 有条件的需要用户介入。对于认证场景，如果设备有凭据，则需要用户介入以选择凭据。对于注册场景，如果用户之前已同意创建凭据，可在无用户介入的情况下创建凭据。 |
| REQUIRED | 'required' | 在没有用户介入的情况下，用户代理将不会移交凭证。 |

## CredentialCreationOptions

注册信息字典对象，包含原始的注册报文。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mediation | [CredentialMediationRequirement](onlineauthentication-passkey-api.md#credentialmediationrequirement) | 否 | 是 | 该操作是否需要用户参与，默认值为"optional"。 |
| publicKey | [PublicKeyCredentialCreationOptions](onlineauthentication-passkey-api.md#publickeycredentialcreationoptions) | 否 | 否 | FIDO2注册报文，包含challenge、rp、用户信息、认证器选择结果等信息。 |

## CredentialRequestOptions

认证信息字典对象，包含原始的认证报文和是否需要用户参与选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mediation | [CredentialMediationRequirement](onlineauthentication-passkey-api.md#credentialmediationrequirement) | 否 | 是 | 该操作是否需要用户参与，默认值为"optional"。 |
| publicKey | [PublicKeyCredentialRequestOptions](onlineauthentication-passkey-api.md#publickeycredentialrequestoptions) | 否 | 否 | FIDO2认证报文，包含challenge、依赖方信息、用户信息、认证器选择结果等信息。 |

## TokenBindingStatus

TokenBinding协议的状态枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| PRESENT | 'present' | 正常通信时的状态。 |
| SUPPORTED | 'supported' | 支持令牌绑定，但通信尚不可用。 |

## TokenBinding

Token binding协议，用于客户端与依赖方通信。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [TokenBindingStatus](onlineauthentication-passkey-api.md#tokenbindingstatus) | 否 | 否 | TokenBinding协议中客户端的绑定状态。 |
| id | string | 否 | 否 | 标识符。长度限制0到512。 |

## AttestationConveyancePreference

供WebAuthn依赖方在生成凭据时参考的枚举值，用于指定凭据传递的首选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| NONE | 'none' | 依赖方对验证者证明不感兴趣，默认值为none。 |
| INDIRECT | 'indirect' | 间接依赖方倾向于提供可验证的证明声明文档，但允许客户决定如何获得这种证明声明。 |
| DIRECT | 'direct' | 直接依赖方希望接收验证者生成的证明声明。 |
| ENTERPRISE | 'enterprise' | 依赖方希望接收企业证明，企业证明是一个证明声明， 其中可能包括唯一标识认证者的信息。 |

## UserVerificationRequirement

依赖方可能需要对某些操作进行用户鉴权（验证当前用户是否为用户）， 但不需要对其他操作进行验证。定义枚举类型是为了区分不同的需求级别。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| REQUIRED | 'required' | 需要进行用户验证。 |
| PREFERRED | 'preferred' | 在可能的情况下，依赖方优先处理操作的用户验证， 但如果响应没有设置用户验证标志，则不会失败。 |
| DISCOURAGED | 'discouraged' | 依赖方在操作过程中不希望使用用户鉴权。 |

## ResidentKeyRequirement

标识是否需要可发现凭证的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| DISCOURAGED | 'discouraged' | 依赖方更倾向于创建服务器端凭证，但也可以接受客户端可发现的凭证。客户端和认证器应尽可能创建服务器端凭证。 |
| PREFERRED | 'preferred' | 依赖方强烈倾向于创建客户端可发现的凭证，但也可以接受服务器端凭证。 |
| REQUIRED | 'required' | 依赖方需要客户端可发现的凭证。如果无法创建客户端可发现的凭证，客户端必须返回错误。 |

## AuthenticatorAttachment

认证器信息（平台、漫游），默认值为platform。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| PLATFORM | 'platform' | 平台认证器，例如PIN码、指纹、人脸等。 |
| CROSS\_PLATFORM | 'cross-platform' | 跨平台认证器，即漫游认证器，包括蓝牙、NFC、USB等。 |

## AuthenticatorSelectionCriteria

由WebAuthn依赖方指定，与认证器有关。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authenticatorAttachment | [AuthenticatorAttachment](onlineauthentication-passkey-api.md#authenticatorattachment) | 否 | 是 | 认证器信息。默认值为platform。 |
| residentKey | string | 否 | 是 | 常驻键。默认值为空。长度限制0到4096。 |
| requireResidentKey | boolean | 否 | 是 | 是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。 |
| userVerification | [UserVerificationRequirement](onlineauthentication-passkey-api.md#userverificationrequirement) | 否 | 是 | 用户认证需求枚举。默认值为preferred。 |

## AuthenticatorTransport

用于身份验证传输的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB | 'usb' | 通用串行总线。 |
| NFC | 'nfc' | 近场通信。 |
| BLE | 'ble' | 蓝牙。 |
| SMART\_CARD | 'smart-card' | 智能卡。 |
| HYBRID | 'hybrid' | 混合。 |
| INTERNAL | 'internal' | 设备内置。 |

## PublicKeyCredentialDescriptor

注册或验证凭据的参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PublicKeyCredentialType](onlineauthentication-passkey-api.md#publickeycredentialtype) | 否 | 否 | 凭证类型。 |
| id | Uint8Array | 否 | 否 | 凭据的标识符。 |
| transports | Array<[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)> | 否 | 是 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举，默认值为空列表。 |

## Algorithm

算法枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ES256 | -7 | ES256算法。 |
| ES384 | -35 | ES384算法。 |
| ES512 | -36 | ES512算法。 |
| RS256 | -257 | RS256算法。 |
| RS384 | -258 | RS384算法。 |
| RS512 | -259 | RS512算法。 |
| PS256 | -37 | PS256算法。 |
| PS384 | -38 | PS384算法。 |
| PS512 | -39 | PS512算法。 |

## PublicKeyCredentialHint

用于公共密钥凭据提示的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECURITY\_KEY | 'security-key' | 安全密钥。 |
| CLIENT\_DEVICE | 'client-device' | 客户端设备。 |
| HYBRID | 'hybrid' | 混合。 |

## PublicKeyCredentialType

用于公共密钥凭证类型的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PUBLIC\_KEY | 'public-key' | 公共密钥。 |

## PublicKeyCredentialParameters

认证凭据的附加参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PublicKeyCredentialType](onlineauthentication-passkey-api.md#publickeycredentialtype) | 否 | 否 | 凭证类型。 |
| alg | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 凭证所使用的密码算法。 |

## PublicKeyCredentialUserEntity

创建新凭据时提供其他用户账户属性。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | Uint8Array | 否 | 否 | 凭据的标识符。长度限制0到512。 |
| displayName | string | 否 | 否 | 前台显示的用户名。长度限制0到512。 |
| name | string | 否 | 否 | 用户名。长度限制0到512。 |

## PublicKeyCredentialRpEntity

创建新凭据时依赖方的属性。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 是 | 凭据的标识符。默认值为空。长度限制0到512。 |
| name | string | 否 | 否 | 用户名。长度限制0到512。 |

## PublicKeyCredentialCreationOptions

创建新身份验证凭据的选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rp | [PublicKeyCredentialRpEntity](onlineauthentication-passkey-api.md#publickeycredentialrpentity) | 否 | 否 | 创建新凭证时依赖方属性。 |
| user | [PublicKeyCredentialUserEntity](onlineauthentication-passkey-api.md#publickeycredentialuserentity) | 否 | 否 | 用户信息。 |
| challenge | Uint8Array | 否 | 否 | 挑战值。长度限制16到512。 |
| pubKeyCredParams | Array<[PublicKeyCredentialParameters](onlineauthentication-passkey-api.md#publickeycredentialparameters)> | 否 | 否 | 身份验证凭据的附加参数列表。 |
| timeout | number | 否 | 是 | 超时时间。单位为ms。默认为300000（5分钟），限制为0到600000（10分钟）。 |
| excludeCredentials | Array<[PublicKeyCredentialDescriptor](onlineauthentication-passkey-api.md#publickeycredentialdescriptor)> | 否 | 是 | FIDO服务器已注册的凭据列表，默认值为空数组。 |
| authenticatorSelection | [AuthenticatorSelectionCriteria](onlineauthentication-passkey-api.md#authenticatorselectioncriteria) | 否 | 是 | 身份认证器相关配置项。默认值为空。 |
| hints | Array<[PublicKeyCredentialHint](onlineauthentication-passkey-api.md#publickeycredentialhint)> | 否 | 是 | 提示。默认值为空数组。 |
| attestation | [AttestationConveyancePreference](onlineauthentication-passkey-api.md#attestationconveyancepreference) | 否 | 是 | 凭证首选项，默认值为“FIDO2\_NONE”。 |
| attestationFormats | Array<string> | 否 | 是 | 依赖方可以使用此可选成员来指定对认证器使用的验证声明格式的偏好，默认值为空数组。 |
| extensions | Map<string, Object> | 否 | 是 | 扩展参数。默认值为空。 |

## Uvm

平台认证器的枚举值。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| UVM\_FINGERPRINT | 2 | 指纹。 |
| UVM\_PIN | 4 | PIN码。 |
| UVM\_FACE | 16 | 人脸。 |

## ClientCapability

当前设备支持的认证能力的枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| CONDITIONAL\_CREATE | 'conditionalCreate' | 通行密钥注册。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| CONDITIONAL\_GET | 'conditionalGet' | 通行密钥认证。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| HYBRID\_TRANSPORT | 'hybridTransport' | 混合传输，表示支持多种传输方式。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| PASSKEY\_PLATFORM\_AUTHENTICATOR | 'passkeyPlatformAuthenticator' | Passkey平台认证器。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR | 'userVerifyingPlatformAuthenticator' | 用户认证平台认证器。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| RELATED\_ORIGINS | 'relatedOrigins' | 支持相关源/域的凭据操作。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS | 'signalAllAcceptedCredentials' | 发送所有接受的凭据。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| SIGNAL\_CURRENT\_USER\_DETAILS | 'signalCurrentUserDetails' | 发送当前用户详细信息。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| SIGNAL\_UNKNOWN\_CREDENTIAL | 'signalUnknownCredential' | 发送未知凭据。  **元服务API**：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| EXTENSION\_LARGEBLOB | 'extension:largeblob' | largeBlob的扩展参数。  **起始版本**：26.0.0  **元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。 |
| EXTENSION\_AUTH\_TYPE\_LIST | 'extension:authTypeList' | authTypeList的扩展参数。  **起始版本**：26.0.0  **元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。 |

## AuthenticatorMetadata

认证器元数据。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| aaguid | string | 是 | 否 | 认证器的唯一标识符。长度限制0到512。 |
| uvm | [Uvm](onlineauthentication-passkey-api.md#uvm) | 是 | 否 | 支持的平台认证器类型，人脸、指纹、PIN码。 |
| isAvailable | boolean | 是 | 否 | true表示该认证器可用，false表示该认证器不可用。 |

## fido2.getClientCapabilities

getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>

查询当前设备支持的客户端能力列表，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 当前Ability的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Map<[ClientCapability](onlineauthentication-passkey-api.md#clientcapability), boolean>> | Promise对象，返回能力枚举的列表，用true和false代表支持或不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通行密钥服务错误码](errorcode-onlineauthentication-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error.  适用版本：6.0.1(21)+ |
| 1021300007 | Unknown error. |
| 1021300009 | Data error.  适用版本：26.0.0+ |
| 1021300011 | Failed to connect to the service. |

**示例：**

```typescript
import { UIContext } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  uiContext = new UIContext();
  context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
  build() {
    RelativeContainer() {
      Text()
        .id('HelloWorld')
        .onClick(async () => {
          try {
            let clientCapabilities: Map<fido2.ClientCapability, boolean> =
              await fido2.getClientCapabilities(this.context);
            console.info('Succeeded in doing getClientCapabilities. clientCapabilities:', JSON.stringify(clientCapabilities));
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call getClientCapabilities. Code is ${err.code}, message is ${err.message}`);
          }
        })
    }
  }
}
```

## fido2.getPlatformAuthenticators

getPlatformAuthenticators(context: common.Context): Promise<Array<AuthenticatorMetadata>>

查询当前支持的平台认证器能力列表（人脸、指纹、PIN码），使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 当前Ability的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AuthenticatorMetadata](onlineauthentication-passkey-api.md#authenticatormetadata)>> | Promise对象，返回认证器元数据列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通行密钥服务错误码](errorcode-onlineauthentication-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error.  适用版本：6.0.1(21)+ |
| 1021300007 | Unknown error. |
| 1021300009 | Data error.  适用版本：26.0.0+ |
| 1021300011 | Failed to connect to the service. |

**示例：**

```typescript
import { UIContext } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  uiContext = new UIContext();
  context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
  build() {
    RelativeContainer() {
      Text()
        .id('HelloWorld')
        .onClick(async () => {
          try {
            let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
              await fido2.getPlatformAuthenticators(this.context);
            console.info('Succeeded in doing getPlatformAuthenticators. platformAuthenticators:',
              JSON.stringify(platformAuthenticators));
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call getPlatformAuthenticators. Code is ${err.code}, message is ${err.message}`);
          }
        })
    }
  }
}
```

## fido2.register

register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAttestationCredential>

进行通行密钥的注册，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 当前Ability的上下文。 |
| options | [CredentialCreationOptions](onlineauthentication-passkey-api.md#credentialcreationoptions) | 是 | 注册报文选项。 |
| tokenBinding | [TokenBinding](onlineauthentication-passkey-api.md#tokenbinding) | 否 | 通道参数，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PublicKeyAttestationCredential](onlineauthentication-passkey-api.md#publickeyattestationcredential)> | Promise对象，返回注册结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通行密钥服务错误码](errorcode-onlineauthentication-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error.  适用版本：6.0.1(21)+ |
| 1021300001 | The system does not support. |
| 1021300002 | Invalid state. |
| 1021300003 | System integrity check failed. |
| 1021300004 | User abort. |
| 1021300005 | Time out. |
| 1021300006 | Encoding error. |
| 1021300007 | Unknown error. |
| 1021300008 | The constraint condition is incorrect. |
| 1021300009 | Data error. |
| 1021300010 | User Rejects. |
| 1021300011 | Failed to connect to the service. |
| 1021300012 | The number of credentials has reached the maximum limit. |

**示例：**

```typescript
import { UIContext } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  uiContext = new UIContext();
  context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
  build() {
    RelativeContainer() {
      Text()
        .id('HelloWorld')
        .onClick(async () => {
          let pkOptions: fido2.PublicKeyCredentialCreationOptions = {
            rp: { id: 'example.com', name: 'Example Corp' },
            user: { id: new Uint8Array([1, 2, 3, 4]), name: 'user', displayName: 'User Name' },
            pubKeyCredParams: [
            ],
            challenge: new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8])
          };
          let credentialCreationOp: fido2.CredentialCreationOptions = {
            publicKey: pkOptions
          };
          try {
            let publicKeyAttestationCredential: fido2.PublicKeyAttestationCredential =
              await fido2.register(this.context, credentialCreationOp);
            console.info('Succeeded in doing register. publicKeyAttestationCredential:',
              JSON.stringify(publicKeyAttestationCredential));
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call register. Code is ${err.code}, message is ${err.message}`);
          }
        })
    }
  }
}
```

## fido2.authenticate

authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAssertionCredential>

进行通行密钥的认证，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 当前Ability的上下文。 |
| options | [CredentialRequestOptions](onlineauthentication-passkey-api.md#credentialrequestoptions) | 是 | 认证报文选项。 |
| tokenBinding | [TokenBinding](onlineauthentication-passkey-api.md#tokenbinding) | 否 | 通道参数，默认值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PublicKeyAssertionCredential](onlineauthentication-passkey-api.md#publickeyassertioncredential)> | Promise对象，返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通行密钥服务错误码](errorcode-onlineauthentication-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error.  适用版本：6.0.1(21)+ |
| 1021300002 | Invalid state. |
| 1021300003 | System integrity check failed. |
| 1021300004 | User abort. |
| 1021300005 | Time out. |
| 1021300006 | Encoding error. |
| 1021300007 | Unknown error. |
| 1021300009 | Data error. |
| 1021300010 | User Rejects. |
| 1021300011 | Failed to connect to the service. |
| 1021300013 | Switched to the custom authentication process.  适用版本：26.0.0+ |
| 1021310001 | Invalid CTAP command. |
| 1021310002 | The command contains invalid parameters. |
| 1021310003 | Invalid message or attribute length. |
| 1021310004 | Invalid CBOR or unpredictable error. |
| 1021310005 | Failed to parse the CBOR. |
| 1021310006 | Not found valid credentials. |
| 1021310007 | Not allowed. |
| 1021310008 | User verification failed. |
| 1021310009 | Other error. |

**示例：**

```typescript
import { UIContext } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  uiContext = new UIContext();
  context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
  build() {
    RelativeContainer() {
      Text()
        .id('HelloWorld')
        .onClick(async () => {
          let authPub: fido2.PublicKeyCredentialRequestOptions = {
            challenge: new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]),
            rpId: 'example.com'
          };
          let authCredentialRequestOptions: fido2.CredentialRequestOptions = {
            publicKey: authPub,
            mediation: 'optional' as fido2.CredentialMediationRequirement
          };
          try {
            let pkAssertionCredential: fido2.PublicKeyAssertionCredential =
              await fido2.authenticate(this.context, authCredentialRequestOptions);
            console.info('Succeeded in doing authenticate. pkAssertionCredential:', JSON.stringify(pkAssertionCredential));
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            console.error(`Failed to call authenticate. Code is ${err.code}, message is ${err.message}`);
          }
        })
    }
  }
}
```
