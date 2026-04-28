---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-passkey-api
title: 通行密钥
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > 通行密钥
category: harmonyos-references
scraped_at: 2026-04-28T08:07:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:183318c0805606850895cb5e887a7a77643bd6260b17d5370740562d68ff5974
---

本模块主要提供了以下能力：

* 通行密钥注册：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，在本设备上创建应用或网页的通行密钥。
* 本地免密认证：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，使用通行密钥在本设备上进行应用或网页的免密认证。
* 跨设备扫码认证：支持使用已注册通行密钥的移动设备作为漫游认证器，使用跨设备扫码的方式，在其他设备上进行应用或网页的免密认证。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { fido2 } from '@kit.OnlineAuthenticationKit';
2. import { BusinessError } from '@kit.BasicServicesKit'
```

## AuthenticatorAttestationResponse

PhonePC/2in1Tablet

以Uint8Array格式表示的认证器证明响应。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attestationObject | Uint8Array | 是 | 否 | 声明对象。 |
| clientDataJson | Uint8Array | 是 | 否 | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| publicKeyAlgorithm | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 密码算法。 |
| publicKey | Uint8Array | 否 | 是 | publicKey凭证请求的选项。默认值为空。 |
| authenticatorData | Uint8Array | 否 | 否 | 认证器数据。 |
| transports | string[] | 否 | 否 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举。 |

## AuthenticatorAttestationResponseJson

PhonePC/2in1Tablet

认证器证明响应，JSON字符串的结构。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientDataJson | string | 否 | 否 | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。长度限制0到4096。 |
| authenticatorData | string | 否 | 否 | 认证器数据。长度限制0到4096。 |
| transports | Array<string> | 否 | 否 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举。 |
| publicKey | string | 否 | 是 | publicKey凭证请求的选项。默认值为空。长度限制0到4096。 |
| publicKeyAlgorithm | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 密码算法。 |
| attestationObject | string | 否 | 否 | 声明对象。长度限制0到10000。 |

## AuthenticationExtensionsClientOutputsJson

PhonePC/2in1Tablet

当依赖方调用 create() 或 get() 时，处理依赖方请求的客户端扩展的结果。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

## AuthenticatorAssertionResponseJson

PhonePC/2in1Tablet

认证器断言响应，JSON字符串的结构。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientDataJson | string | 否 | 否 | 客户端数据。长度限制0到4096。 |
| authenticatorData | string | 否 | 否 | 认证器数据。长度限制0到4096。 |
| signature | string | 否 | 否 | 签名。长度限制0到4096。 |
| userHandle | string | 否 | 是 | 用户句柄。默认值为空。长度限制0到4096。 |

## AuthenticatorAssertionResponse

PhonePC/2in1Tablet

认证器断言响应。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authenticatorData | Uint8Array | 是 | 否 | 认证器数据。 |
| signature | Uint8Array | 是 | 否 | 签名。 |
| userHandle | Uint8Array | 是 | 是 | 用户句柄。默认值为空。 |
| clientDataJson | Uint8Array | 是 | 否 | 客户端数据。 |

## AuthenticationExtensionsClientOutputs

PhonePC/2in1Tablet

身份验证扩展。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

## PublicKeyAttestationCredential

PhonePC/2in1Tablet

注册返回参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

注册返回参数的JSON格式。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

定义通行密钥认证请求参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| challenge | Uint8Array | 否 | 否 | 获取挑战值。 |
| timeout | number | 否 | 是 | 认证操作最长时间，单位为毫秒。默认值为300000ms。 |
| rpId | string | 否 | 是 | 依赖方标识。默认值为空。长度限制0到512。 |
| allowCredentials | Array<[PublicKeyCredentialDescriptor](onlineauthentication-passkey-api.md#publickeycredentialdescriptor)> | 否 | 是 | 认证凭据的附加参数列表。默认值为空。 |
| userVerification | [UserVerificationRequirement](onlineauthentication-passkey-api.md#userverificationrequirement) | 否 | 是 | 用户认证需求枚举。默认值为preferred。 |
| hints | Array<[PublicKeyCredentialHint](onlineauthentication-passkey-api.md#publickeycredentialhint)> | 否 | 是 | 认证方式指示。默认值为[]。 |
| extensions | Map<string, Object> | 否 | 是 | 扩展名必须是表示Map<string，Object> object的JSON字符串。默认值为空。 |

## PublicKeyAssertionCredential

PhonePC/2in1Tablet

认证返回参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

认证返回参数的JSON格式。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

用户介入要求的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| SILENT | 'silent' | 禁止用户介入指定的操作。如果可以在不需要用户介入的情况下进行操作，则正常。 如果需要用户介入，则操作将返回null。 |
| OPTIONAL | 'optional' | 如果在没有用户介入的情况下，可以为给定的操作传递凭据，则正常传递。 如果需要用户介入，那么用户代理将让用户介入决策。 |
| CONDITIONAL | 'conditional' | 有条件的需要用户介入。对于认证场景，如果设备有凭据，则需要用户介入以选择凭据。对于注册场景，如果用户之前已同意创建凭据，可在无用户介入的情况下创建凭据。 |
| REQUIRED | 'required' | 在没有用户介入的情况下，用户代理将不会移交凭证。 |

## CredentialCreationOptions

PhonePC/2in1Tablet

注册信息字典对象，包含原始的注册报文。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mediation | [CredentialMediationRequirement](onlineauthentication-passkey-api.md#credentialmediationrequirement) | 否 | 是 | 该操作是否需要用户参与，默认值为"optional"。 |
| publicKey | [PublicKeyCredentialCreationOptions](onlineauthentication-passkey-api.md#publickeycredentialcreationoptions) | 否 | 否 | FIDO2注册报文，包含challenge、rp、用户信息、认证器选择结果等信息。 |

## CredentialRequestOptions

PhonePC/2in1Tablet

认证信息字典对象，包含原始的认证报文和是否需要用户参与选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mediation | [CredentialMediationRequirement](onlineauthentication-passkey-api.md#credentialmediationrequirement) | 否 | 是 | 该操作是否需要用户参与，默认值为"optional"。 |
| publicKey | [PublicKeyCredentialRequestOptions](onlineauthentication-passkey-api.md#publickeycredentialrequestoptions) | 否 | 否 | FIDO2认证报文，包含challenge、依赖方信息、用户信息、认证器选择结果等信息。 |

## TokenBindingStatus

PhonePC/2in1Tablet

TokenBinding协议的状态枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| PRESENT | 'present' | 正常通信时的状态。 |
| SUPPORTED | 'supported' | 支持令牌绑定，但通信尚不可用。 |

## TokenBinding

PhonePC/2in1Tablet

Token binding协议，用于客户端与依赖方通信。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [TokenBindingStatus](onlineauthentication-passkey-api.md#tokenbindingstatus) | 否 | 否 | TokenBinding协议中客户端的绑定状态。 |
| id | string | 否 | 否 | 标识符。长度限制0到512。 |

## AttestationConveyancePreference

PhonePC/2in1Tablet

供WebAuthn依赖方在生成凭据时参考的枚举值，用于指定凭据传递的首选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| NONE | 'none' | 依赖方对验证者证明不感兴趣，默认值为none。 |
| INDIRECT | 'indirect' | 间接依赖方倾向于提供可验证的证明声明文档，但允许客户决定如何获得这种证明声明。 |
| DIRECT | 'direct' | 直接依赖方希望接收验证者生成的证明声明。 |
| ENTERPRISE | 'enterprise' | 依赖方希望接收企业证明，企业证明是一个证明声明， 其中可能包括唯一标识认证者的信息。 |

## UserVerificationRequirement

PhonePC/2in1Tablet

依赖方可能需要对某些操作进行用户鉴权（验证当前用户是否为用户）， 但不需要对其他操作进行验证。定义枚举类型是为了区分不同的需求级别。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| REQUIRED | 'required' | 需要进行用户验证。 |
| PREFERRED | 'preferred' | 在可能的情况下，依赖方优先处理操作的用户验证， 但如果响应没有设置用户验证标志，则不会失败。 |
| DISCOURAGED | 'discouraged' | 依赖方在操作过程中不希望使用用户鉴权。 |

## ResidentKeyRequirement

PhonePC/2in1Tablet

标识是否需要可发现凭证的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| DISCOURAGED | 'discouraged' | 依赖方更倾向于创建服务器端凭证，但也可以接受客户端可发现的凭证。客户端和认证器应尽可能创建服务器端凭证。 |
| PREFERRED | 'preferred' | 依赖方强烈倾向于创建客户端可发现的凭证，但也可以接受服务器端凭证。 |
| REQUIRED | 'required' | 依赖方需要客户端可发现的凭证。如果无法创建客户端可发现的凭证，客户端必须返回错误。 |

## AuthenticatorAttachment

PhonePC/2in1Tablet

认证器信息（平台、漫游），默认值为platform。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| PLATFORM | 'platform' | 平台认证器，例如PIN码、指纹、人脸等。 |
| CROSS\_PLATFORM | 'cross-platform' | 跨平台认证器，即漫游认证器，包括蓝牙、NFC、USB等。 |

## AuthenticatorSelectionCriteria

PhonePC/2in1Tablet

由webAuthn依赖方指定，与认证器有关。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authenticatorAttachment | [AuthenticatorAttachment](onlineauthentication-passkey-api.md#authenticatorattachment) | 否 | 是 | 认证器信息。默认值为platform。 |
| residentKey | string | 否 | 是 | 常驻键。默认值为空。长度限制0到4096。 |
| requireResidentKey | boolean | 否 | 是 | 是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。 |
| userVerification | [UserVerificationRequirement](onlineauthentication-passkey-api.md#userverificationrequirement) | 否 | 是 | 用户认证需求枚举。默认值为preferred。 |

## AuthenticatorTransport

PhonePC/2in1Tablet

用于身份验证传输的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

注册或验证凭据的参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PublicKeyCredentialType](onlineauthentication-passkey-api.md#publickeycredentialtype) | 否 | 否 | 凭证类型。 |
| id | Uint8Array | 否 | 否 | 凭据的标识符。 |
| transports | Array<[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)> | 否 | 是 | 定义身份认证器访问类型，取值范围为[AuthenticatorTransport](onlineauthentication-passkey-api.md#authenticatortransport)枚举，默认值为空列表。 |

## Algorithm

PhonePC/2in1Tablet

算法枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

PhonePC/2in1Tablet

用于公共密钥凭据提示的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECURITY\_KEY | 'security-key' | 安全密钥。 |
| CLIENT\_DEVICE | 'client-device' | 客户端设备。 |
| HYBRID | 'hybrid' | 混合。 |

## PublicKeyCredentialType

PhonePC/2in1Tablet

用于公共密钥凭证类型的枚举。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PUBLIC\_KEY | 'public-key' | 公共密钥。 |

## PublicKeyCredentialParameters

PhonePC/2in1Tablet

认证凭据的附加参数。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PublicKeyCredentialType](onlineauthentication-passkey-api.md#publickeycredentialtype) | 否 | 否 | 凭证类型。 |
| alg | [Algorithm](onlineauthentication-passkey-api.md#algorithm) | 否 | 否 | 算法。 |

## PublicKeyCredentialUserEntity

PhonePC/2in1Tablet

创建新凭据时提供其他用户账户属性。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | Uint8Array | 否 | 否 | 凭据的标识符。长度限制0到64。 |
| displayName | string | 否 | 否 | 前台显示的用户名。长度限制0到512。 |
| name | string | 否 | 否 | 用户名。长度限制0到512。 |

## PublicKeyCredentialRpEntity

PhonePC/2in1Tablet

创建新凭据时依赖方的属性。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 是 | 凭据的标识符。默认值为空。长度限制0到512。 |
| name | string | 否 | 否 | 用户名。长度限制0到512。 |

## PublicKeyCredentialCreationOptions

PhonePC/2in1Tablet

创建新身份验证凭据的选项。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rp | [PublicKeyCredentialRpEntity](onlineauthentication-passkey-api.md#publickeycredentialrpentity) | 否 | 否 | 创建新凭证时依赖方属性。 |
| user | [PublicKeyCredentialUserEntity](onlineauthentication-passkey-api.md#publickeycredentialuserentity) | 否 | 否 | 用户信息。 |
| challenge | Uint8Array | 否 | 否 | 挑战值。长度限制16到512。 |
| pubKeyCredParams | Array<[PublicKeyCredentialParameters](onlineauthentication-passkey-api.md#publickeycredentialparameters)> | 否 | 否 | 身份验证凭据的附加参数列表。 |
| timeout | number | 否 | 是 | 超时时间。默认值为300000ms。限制300s到600s。 |
| excludeCredentials | Array<[PublicKeyCredentialDescriptor](onlineauthentication-passkey-api.md#publickeycredentialdescriptor)> | 否 | 是 | FIDO服务器已注册的凭据列表，默认值为空数组。 |
| authenticatorSelection | [AuthenticatorSelectionCriteria](onlineauthentication-passkey-api.md#authenticatorselectioncriteria) | 否 | 是 | 身份认证器相关配置项。默认值为空。 |
| hints | Array<[PublicKeyCredentialHint](onlineauthentication-passkey-api.md#publickeycredentialhint)> | 否 | 是 | 提示。默认值为空数组。 |
| attestation | [AttestationConveyancePreference](onlineauthentication-passkey-api.md#attestationconveyancepreference) | 否 | 是 | 凭证首选项，默认值为“none”。 |
| attestationFormats | Array<string> | 否 | 是 | 依赖方可以使用此可选成员来指定对认证器使用的验证声明格式的偏好，默认值为空数组。 |
| extensions | Map<string, Object> | 否 | 是 | 扩展参数。默认值为空。 |

## Uvm

PhonePC/2in1Tablet

平台认证器的枚举值。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| UVM\_FINGERPRINT | 2 | 指纹。 |
| UVM\_PIN | 4 | PIN码。 |
| UVM\_FACE | 16 | 人脸。 |

## ClientCapability

PhonePC/2in1Tablet

当前设备支持的认证能力的枚举值。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | **值** | 说明 |
| --- | --- | --- |
| CONDITIONAL\_CREATE | 'conditionalCreate' | 通行密钥注册。 |
| CONDITIONAL\_GET | 'conditionalGet' | 通行密钥认证。 |
| HYBRID\_TRANSPORT | 'hybridTransport' | 混合传输，表示支持多种传输方式。 |
| PASSKEY\_PLATFORM\_AUTHENTICATOR | 'passkeyPlatformAuthenticator' | Passkey平台认证器。 |
| USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR | 'userVerifyingPlatformAuthenticator' | 用户认证平台认证器。 |
| RELATED\_ORIGINS | 'relatedOrigins' | 支持相关源/域的凭据操作。 |
| SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS | 'signalAllAcceptedCredentials' | 发送所有接受的凭据。 |
| SIGNAL\_CURRENT\_USER\_DETAILS | 'signalCurrentUserDetails' | 发送当前用户详细信息。 |
| SIGNAL\_UNKNOWN\_CREDENTIAL | 'signalUnknownCredential' | 发送未知凭据。 |

## AuthenticatorMetadata

PhonePC/2in1Tablet

认证器元数据。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| aaguid | string | 是 | 否 | 认证器唯一标识。长度限制0到512。 |
| uvm | [Uvm](onlineauthentication-passkey-api.md#uvm) | 是 | 否 | 支持的平台认证器类型，人脸、指纹、PIN码。 |
| isAvailable | boolean | 是 | 否 | true表示该认证器可用，false表示该认证器不可用。 |

## getClientCapabilities

PhonePC/2in1Tablet

getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>

查询当前设备支持的客户端能力列表，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

以下错误码的详细介绍请参见[通行密钥服务错误码](onlineauthentication-error-code-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1021300007 | Unknown error. |
| 1021300011 | Failed to connect to the service. |

**示例：**

```
1. import { common } from '@kit.AbilityKit'

3. uiContext1: UIContext = this.getUIContext();
4. uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可

6. try {
7. let clientCapabilities: Map<fido2.ClientCapability, boolean> =
8. await fido2.getClientCapabilities(this.uiContext); // 获取客户端能力列表
9. console.info("Succeeded in doing getClientCapabilities.");
10. } catch (error) {
11. const err: BusinessError = error as BusinessError;
12. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
13. }
```

## getPlatformAuthenticators

PhonePC/2in1Tablet

getPlatformAuthenticators(context: common.Context): Promise<Array<AuthenticatorMetadata>>

查询当前支持的平台认证器能力列表（人脸、指纹、PIN码），使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

以下错误码的详细介绍请参见[通行密钥服务错误码](onlineauthentication-error-code-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1021300007 | Unknown error. |
| 1021300011 | Failed to connect to the service. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. uiContext1: UIContext = this.getUIContext();
4. uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可

6. try{
7. let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
8. await fido2.getPlatformAuthenticators(this.uiContext); // 获取平台认证器信息
9. console.info("Succeeded in doing getPlatformAuthenticators.");
10. } catch (error) {
11. const err: BusinessError = error as BusinessError;
12. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
13. }
```

## register

PhonePC/2in1Tablet

register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAttestationCredential>

进行通行密钥的注册，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

以下错误码的详细介绍请参见[通行密钥服务错误码](onlineauthentication-error-code-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
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

```
1. import { common } from '@kit.AbilityKit';

3. uiContext1: UIContext = this.getUIContext();
4. uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可

6. try {
7. let credentialCreationOp: fido2.CredentialCreationOptions = {
8. publicKey: pkOptions // pkOptions为从FIDO服务器获取的注册报文
9. } // credentialCreationOp为应用组装的注册信息
10. let publicKeyAttestationCredential: fido2.PublicKeyAttestationCredential =
11. await fido2.register(this.uiContext, credentialCreationOp); // 进行FIDO2注册
12. console.info("Succeeded in doing register.");
13. } catch (error) {
14. const err: BusinessError = error as BusinessError;
15. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
16. }
```

## authenticate

PhonePC/2in1Tablet

authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAssertionCredential>

进行通行密钥的认证，使用Promise异步回调。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

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

以下错误码的详细介绍请参见[通行密钥服务错误码](onlineauthentication-error-code-passkey.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1021300002 | Invalid state. |
| 1021300003 | System integrity check failed. |
| 1021300004 | User abort. |
| 1021300005 | Time out. |
| 1021300006 | Encoding error. |
| 1021300007 | Unknown error. |
| 1021300009 | Data error. |
| 1021300010 | User Rejects. |
| 1021300011 | Failed to connect to the service. |
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

```
1. import { common } from '@kit.AbilityKit';

3. uiContext1: UIContext = this.getUIContext();
4. uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // 使用uiContext需要获取页面UIAbility的Context，一个页面获取一次即可

6. try {
7. let authCredentialRequestOptions: fido2.CredentialRequestOptions = {
8. publicKey: authPub, // authPub为从FIDO服务器获取的认证报文
9. mediation: "optional" as fido2.CredentialMediationRequirement //
10. } // authCredentialRequestOptions为应用组装的认证信息
11. let pkAssertionCredential: fido2.PublicKeyAssertionCredential =
12. await fido2.authenticate(this.uiContext, authCredentialRequestOptions); // 进行FIDO2认证
13. console.info("Succeeded in doing authenticate.");
14. } catch (error) {
15. const err: BusinessError = error as BusinessError;
16. console.error(`Failed to call discover. Code is ${err.code}, message is ${err.message}`);
17. }
```
