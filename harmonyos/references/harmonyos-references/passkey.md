---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey
title: 通行密钥
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 模块 > 通行密钥
category: harmonyos-references
scraped_at: 2026-04-28T08:07:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9783f9725e727e3d91a27be80fdfc573c6fb1a560acbc1c37b0924d43f7d757
---

## 概述

提供通行密钥能力。

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [fido2\_api.h](onlineauthentication_capi_header_fido2.md) | 本声明用于访问FIDO2的API。提供FIDO2（通行密钥）能力的相关接口。FIDO2的基础核心能力，包含：获取支持的FIDO2能力、获取平台认证器能力、注册通行密钥能力和使用通行密钥认证能力。 |

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [Uint8Buff](_uint8_buff.md) | 定义uint8\_t字节流。 |
| struct [AuthenticationExtensionsClientOutputs](_authentication_extensions_client_outputs.md) | 身份认证扩展。 |
| struct [FIDO2\_AuthenticatorResponse](_f_i_d_o2___authenticator_response.md) | 定义获取认证器断言响应的结构体。 |
| struct [FIDO2\_PublicKeyAssertionCredential](_f_i_d_o2___public_key_assertion_credential.md) | 定义获取认证结果结构体。 |
| struct [FIDO2\_AuthenticatorTransportArray](_f_i_d_o2___authenticator_transport_array.md) | 认证器传输方式数组。 |
| struct [FIDO2\_AuthenticatorAttestationResponse](_f_i_d_o2___authenticator_attestation_response.md) | 认证器声明响应。 |
| struct [FIDO2\_PublicKeyAttestationCredential](_f_i_d_o2___public_key_attestation_credential.md) | 定义获取注册结果结构体。 |
| struct [FIDO2\_AuthenticatorSelectionCriteria](_f_i_d_o2___authenticator_selection_criteria.md) | 由webAuthn依赖方（即接入协议的应用或网页）指定，与认证器有关。 |
| struct [FIDO2\_PublicKeyCredentialDescriptor](_f_i_d_o2___public_key_credential_descriptor.md) | 用于注册或认证凭据的参数。 |
| struct [FIDO2\_PublicKeyCredentialParameters](_f_i_d_o2___public_key_credential_parameters.md) | 认证凭据的附加参数。 |
| struct [FIDO2\_PublicKeyCredentialUserEntity](_f_i_d_o2___public_key_credential_user_entity.md) | 创建新凭据时用户的属性。 |
| struct [FIDO2\_PublicKeyCredentialRpEntity](_f_i_d_o2___public_key_credential_rp_entity.md) | 创建新凭据时依赖方的属性。 |
| struct [FIDO2\_PublicKeyCredentialDescriptorArray](_f_i_d_o2___public_key_credential_descriptor_array.md) | PublicKey凭证描述符数组。 |
| struct [FIDO2\_PublicKeyCredentialHintArray](_f_i_d_o2___public_key_credential_hint_array.md) | 认证方式指示数组。 |
| struct [FIDO2\_PublicKeyCredentialRequestOptions](_f_i_d_o2___public_key_credential_request_options.md) | 定义通行密钥认证请求参数。 |
| struct [FIDO2\_CredentialCreationOptionArray](_f_i_d_o2___credential_creation_option_array.md) | 认证凭据的附加参数数组。 |
| struct [FIDO2\_AttestationFormatsArray](_f_i_d_o2___attestation_formats_array.md) | 依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。 |
| struct [FIDO2\_PublicKeyCredentialCreationOptions](_f_i_d_o2___public_key_credential_creation_options.md) | 创建新的认证凭据的选项。 |
| struct [FIDO2\_CredentialCreationOptions](_f_i_d_o2___credential_creation_options.md) | 凭据请求的选项。 |
| struct [FIDO2\_AuthenticatorMetadata](_f_i_d_o2___authenticator_metadata.md) | 认证器元数据。 |
| struct [FIDO2\_CredentialRequestOptions](_f_i_d_o2___credential_request_options.md) | 认证信息字典对象。 |
| struct [FIDO2\_AuthenticatorMetadataArray](_f_i_d_o2___authenticator_metadata_array.md) | 描述支持的认证器数组。 |
| struct [FIDO2\_Capability](_f_i_d_o2___capability.md) | 通行密钥能力的结构体。 |
| struct [FIDO2\_CapabilityArray](_f_i_d_o2___capability_array.md) | 描述能力数组。 |
| struct [FIDO2\_TokenBinding](_f_i_d_o2___token_binding.md) | Token binding协议，用于客户端与依赖方通信。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [Uint8Buff](_uint8_buff.md) [Uint8Buff](passkey.md#uint8buff) | 定义uint8\_t字节流。 |
| typedef enum [FIDO2\_TokenBindingStatus](passkey.md#fido2_tokenbindingstatus-1) [FIDO2\_TokenBindingStatus](passkey.md#fido2_tokenbindingstatus) | TokenBinding协议的状态。 |
| typedef enum [FIDO2\_AttestationConveyancePreference](passkey.md#fido2_attestationconveyancepreference-1) [FIDO2\_AttestationConveyancePreference](passkey.md#fido2_attestationconveyancepreference) | 供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。 |
| typedef enum [FIDO2\_UserVerificationRequirement](passkey.md#fido2_userverificationrequirement-1) [FIDO2\_UserVerificationRequirement](passkey.md#fido2_userverificationrequirement) | 依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。 |
| typedef enum [FIDO2\_AuthenticatorAttachment](passkey.md#fido2_authenticatorattachment-1) [FIDO2\_AuthenticatorAttachment](passkey.md#fido2_authenticatorattachment) | 认证器信息（平台、漫游）。 |
| typedef enum [FIDO2\_AuthenticatorTransport](passkey.md#fido2_authenticatortransport-1) [FIDO2\_AuthenticatorTransport](passkey.md#fido2_authenticatortransport) | 认证器传输方式的枚举。 |
| typedef enum [FIDO2\_Algorithm](passkey.md#fido2_algorithm-1) [FIDO2\_Algorithm](passkey.md#fido2_algorithm) | 加密算法的枚举。 |
| typedef enum [FIDO2\_PublicKeyCredentialHint](passkey.md#fido2_publickeycredentialhint-1) [FIDO2\_PublicKeyCredentialHint](passkey.md#fido2_publickeycredentialhint) | 认证方式指示的枚举。 |
| typedef enum [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype-1) [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype) | 公钥凭据类型的枚举。 |
| typedef enum [FIDO2\_Uvm](passkey.md#fido2_uvm-1) [FIDO2\_Uvm](passkey.md#fido2_uvm) | UVM的枚举。 |
| typedef enum [FIDO2\_ClientCapability](passkey.md#fido2_clientcapability-1) [FIDO2\_ClientCapability](passkey.md#fido2_clientcapability) | 客户端能力的枚举。 |
| typedef enum [FIDO2\_CredentialMediationRequirement](passkey.md#fido2_credentialmediationrequirement-1) [FIDO2\_CredentialMediationRequirement](passkey.md#fido2_credentialmediationrequirement) | 用户介入要求的枚举。 |
| typedef enum [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) [FIDO2\_ErrorCode](passkey.md#fido2_errorcode) | 错误码定义。 |
| typedef struct [AuthenticationExtensionsClientOutputs](_authentication_extensions_client_outputs.md) [AuthenticationExtensionsClientOutputs](passkey.md#authenticationextensionsclientoutputs) | 身份认证扩展。 |
| typedef struct [FIDO2\_AuthenticatorResponse](_f_i_d_o2___authenticator_response.md) [FIDO2\_AuthenticatorResponse](passkey.md#fido2_authenticatorresponse) | 定义获取认证器断言响应的结构体。 |
| typedef struct [FIDO2\_PublicKeyAssertionCredential](_f_i_d_o2___public_key_assertion_credential.md) [FIDO2\_PublicKeyAssertionCredential](passkey.md#fido2_publickeyassertioncredential) | 定义获取认证结果结构体。 |
| typedef struct [FIDO2\_AuthenticatorTransportArray](_f_i_d_o2___authenticator_transport_array.md) [FIDO2\_AuthenticatorTransportArray](passkey.md#fido2_authenticatortransportarray) | 认证器传输方式数组。 |
| typedef struct [FIDO2\_AuthenticatorAttestationResponse](_f_i_d_o2___authenticator_attestation_response.md) [FIDO2\_AuthenticatorAttestationResponse](passkey.md#fido2_authenticatorattestationresponse) | 认证器声明响应。 |
| typedef struct [FIDO2\_PublicKeyAttestationCredential](_f_i_d_o2___public_key_attestation_credential.md) [FIDO2\_PublicKeyAttestationCredential](passkey.md#fido2_publickeyattestationcredential) | 定义获取注册结果结构体。 |
| typedef struct [FIDO2\_AuthenticatorSelectionCriteria](_f_i_d_o2___authenticator_selection_criteria.md) [FIDO2\_AuthenticatorSelectionCriteria](passkey.md#fido2_authenticatorselectioncriteria) | 由webAuthn依赖方指定，与认证器有关。 |
| typedef struct [FIDO2\_PublicKeyCredentialDescriptor](_f_i_d_o2___public_key_credential_descriptor.md) [FIDO2\_PublicKeyCredentialDescriptor](passkey.md#fido2_publickeycredentialdescriptor) | 用于注册或认证凭据的参数。 |
| typedef struct [FIDO2\_PublicKeyCredentialParameters](_f_i_d_o2___public_key_credential_parameters.md) [FIDO2\_PublicKeyCredentialParameters](passkey.md#fido2_publickeycredentialparameters) | 认证凭据的附加参数。 |
| typedef struct [FIDO2\_PublicKeyCredentialUserEntity](_f_i_d_o2___public_key_credential_user_entity.md) [FIDO2\_PublicKeyCredentialUserEntity](passkey.md#fido2_publickeycredentialuserentity) | 创建新凭据时用户的属性。 |
| typedef struct [FIDO2\_PublicKeyCredentialRpEntity](_f_i_d_o2___public_key_credential_rp_entity.md) [FIDO2\_PublicKeyCredentialRpEntity](passkey.md#fido2_publickeycredentialrpentity) | 创建新凭据时依赖方的属性。 |
| typedef struct [FIDO2\_PublicKeyCredentialDescriptorArray](_f_i_d_o2___public_key_credential_descriptor_array.md) [FIDO2\_PublicKeyCredentialDescriptorArray](passkey.md#fido2_publickeycredentialdescriptorarray) | PublicKey凭证描述符数组。 |
| typedef struct [FIDO2\_PublicKeyCredentialHintArray](_f_i_d_o2___public_key_credential_hint_array.md) [FIDO2\_PublicKeyCredentialHintArray](passkey.md#fido2_publickeycredentialhintarray) | 认证方式指示数组。 |
| typedef struct [FIDO2\_PublicKeyCredentialRequestOptions](_f_i_d_o2___public_key_credential_request_options.md) [FIDO2\_PublicKeyCredentialRequestOptions](passkey.md#fido2_publickeycredentialrequestoptions) | 定义通行密钥认证请求参数。 |
| typedef struct [FIDO2\_CredentialCreationOptionArray](_f_i_d_o2___credential_creation_option_array.md) [FIDO2\_CredentialCreationOptionArray](passkey.md#fido2_credentialcreationoptionarray) | 认证凭据的附加参数数组。 |
| typedef struct [FIDO2\_AttestationFormatsArray](_f_i_d_o2___attestation_formats_array.md) [FIDO2\_AttestationFormatsArray](passkey.md#fido2_attestationformatsarray) | 依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。 |
| typedef struct [FIDO2\_PublicKeyCredentialCreationOptions](_f_i_d_o2___public_key_credential_creation_options.md) [FIDO2\_PublicKeyCredentialCreationOptions](passkey.md#fido2_publickeycredentialcreationoptions) | 创建新的认证凭据的选项。 |
| typedef struct [FIDO2\_CredentialCreationOptions](_f_i_d_o2___credential_creation_options.md) [FIDO2\_CredentialCreationOptions](passkey.md#fido2_credentialcreationoptions) | 凭据请求的选项。 |
| typedef struct [FIDO2\_AuthenticatorMetadata](_f_i_d_o2___authenticator_metadata.md) [FIDO2\_AuthenticatorMetadata](passkey.md#fido2_authenticatormetadata) | 认证器元数据。 |
| typedef struct [FIDO2\_CredentialRequestOptions](_f_i_d_o2___credential_request_options.md) [FIDO2\_CredentialRequestOptions](passkey.md#fido2_credentialrequestoptions) | 认证信息字典对象。 |
| typedef struct [FIDO2\_AuthenticatorMetadataArray](_f_i_d_o2___authenticator_metadata_array.md) [FIDO2\_AuthenticatorMetadataArray](passkey.md#fido2_authenticatormetadataarray) | 描述支持的认证器数组。 |
| typedef struct [FIDO2\_Capability](_f_i_d_o2___capability.md) [FIDO2\_Capability](passkey.md#fido2_capability) | 通行密钥能力的结构体。 |
| typedef struct [FIDO2\_CapabilityArray](_f_i_d_o2___capability_array.md) [FIDO2\_CapabilityArray](passkey.md#fido2_capabilityarray) | 描述能力数组。 |
| typedef struct [FIDO2\_TokenBinding](_f_i_d_o2___token_binding.md) [FIDO2\_TokenBinding](passkey.md#fido2_tokenbinding) | Token binding（协议），用于客户端与依赖方通信。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_TokenBindingStatus](passkey.md#fido2_tokenbindingstatus-1) { FIDO2\_PRESENT = 0, FIDO2\_SUPPORTED = 1 } | TokenBinding协议的状态。 |
| [FIDO2\_AttestationConveyancePreference](passkey.md#fido2_attestationconveyancepreference-1) { FIDO2\_NONE = 0, FIDO2\_INDIRECT = 1, FIDO2\_DIRECT = 2, FIDO2\_ENTERPRISE = 3 } | 供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。 |
| [FIDO2\_UserVerificationRequirement](passkey.md#fido2_userverificationrequirement-1) { FIDO2\_REQUIRED = 0, FIDO2\_PREFERRED = 1, FIDO2\_DISCOURAGED = 2 } | 依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。 |
| [FIDO2\_AuthenticatorAttachment](passkey.md#fido2_authenticatorattachment-1) { FIDO2\_PLATFORM = 0, FIDO2\_CROSS\_PLATFORM = 1 } | 认证器信息（平台、漫游）。 |
| [FIDO2\_AuthenticatorTransport](passkey.md#fido2_authenticatortransport-1) {  FIDO2\_USB = 0, FIDO2\_NFC = 1, FIDO2\_BLE = 2, FIDO2\_SMART\_CARD = 3,  FIDO2\_HYBRID = 4, FIDO2\_INTERNAL = 5  } | 认证器传输方式的枚举。 |
| [FIDO2\_Algorithm](passkey.md#fido2_algorithm-1) {  FIDO2\_ES256 = -7, FIDO2\_ES384 = -35, FIDO2\_ES512 = -36, FIDO2\_RS256 = -257,  FIDO2\_RS384 = -258, FIDO2\_RS512 = -259, FIDO2\_PS256 = -37, FIDO2\_PS384 = -38,  FIDO2\_PS512 = -39  } | 算法的枚举。 |
| [FIDO2\_PublicKeyCredentialHint](passkey.md#fido2_publickeycredentialhint-1) { FIDO2\_SECURITY\_KEY = 0, FIDO2\_CLIENT\_DEVICE = 1, FIDO2\_HINT\_HYBRID = 2 } | 认证方式指示的枚举。 |
| [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype-1) { FIDO2\_PUBLIC\_KEY = 0 } | 公钥凭据类型的枚举。 |
| [FIDO2\_Uvm](passkey.md#fido2_uvm-1) { FIDO2\_UVM\_FINGERPRINT = 2, FIDO2\_UVM\_PIN = 4, FIDO2\_UVM\_FACEPRINT = 16 } | UVM的枚举。 |
| [FIDO2\_ClientCapability](passkey.md#fido2_clientcapability-1) {  FIDO2\_CONDITIONAL\_CREATE = 0, FIDO2\_CONDITIONAL\_GET = 1, FIDO2\_HYBRID\_TRANSPORT = 2, FIDO2\_PASSKEY\_PLATFORM\_AUTHENTICATOR = 3,  FIDO2\_USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR = 4, FIDO2\_RELATED\_ORIGINS = 5, FIDO2\_SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS = 6, FIDO2\_SIGNAL\_CURRENT\_USER\_DETAILS = 7,  FIDO2\_SIGNAL\_UNKNOWN\_CREDENTIAL = 8, FIDO2\_EXTENSION\_UVI = 9  } | 客户端能力的枚举。 |
| [FIDO2\_CredentialMediationRequirement](passkey.md#fido2_credentialmediationrequirement-1) { FIDO2\_SILENT = 0, FIDO2\_OPTIONAL = 1, FIDO2\_CONDITIONAL = 2, FIDO2\_MEDIATION\_REQUIRED = 3 } | 用户介入要求的枚举。 |
| [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) {  FIDO2\_SUCCESS = 0, FIDO2\_PERMISSION\_DENIED = 201, FIDO2\_DEVICE\_NOT\_SUPPORT = 801, FIDO2\_NOT\_SUPPORT = 1021300001, FIDO2\_INVALID\_STATE = 1021300002,  FIDO2\_INTEGRITY\_CHECK\_FAILED = 1021300003, FIDO2\_USER\_ABORT = 1021300004, FIDO2\_TIMEOUT = 1021300005, FIDO2\_ENCODING\_ERROR = 1021300006,  FIDO2\_UNKNOWN\_ERROR = 1021300007, FIDO2\_CONSTRAINT\_ERROR = 1021300008, FIDO2\_DATA\_ERROR = 1021300009, FIDO2\_USER\_REJECTS = 1021300010,  FIDO2\_CONNECT\_SERVICE\_FAILED = 1021300011, FIDO2\_MAX\_CRED\_NUM\_REACHED = 1021300012, FIDO2\_INVALID\_CTAP\_COMMAND = 1021310001, FIDO2\_INVALID\_PARAMETERS = 1021310002, FIDO2\_INVALID\_MESSAGE\_OR\_ATTRIBUTE\_LENGTH = 1021310003,  FIDO2\_INVALID\_CBOR\_OR\_UNPREDICTABLE = 1021310004, FIDO2\_PARSE\_CBOR\_FAILED = 1021310005, FIDO2\_INVALID\_CREDENTIALS = 1021310006, FIDO2\_NOT\_ALLOWED = 1021310007,  FIDO2\_USER\_VERIFICATION\_FAILED = 1021310008, FIDO2\_OTHER\_ERROR = 1021310009  } | 错误码定义。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FIDO2\_initCreationOptions](passkey.md#hms_fido2_initcreationoptions) ([FIDO2\_CredentialCreationOptions](_f_i_d_o2___credential_creation_options.md) \*options) | 初始化FIDO2\_CredentialCreationOptions结构。 |
| void [HMS\_FIDO2\_initTokenBinding](passkey.md#hms_fido2_inittokenbinding) ([FIDO2\_TokenBinding](_f_i_d_o2___token_binding.md) \*tokenBinding) | 初始化FIDO2\_TokenBinding结构体。 |
| void [HMS\_FIDO2\_initRequestOptions](passkey.md#hms_fido2_initrequestoptions) ([FIDO2\_CredentialRequestOptions](_f_i_d_o2___credential_request_options.md) \*options) | 初始化FIDO2\_CredentialRequestOptions结构。 |
| [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) [HMS\_FIDO2\_getClientCapability](passkey.md#hms_fido2_getclientcapability) ([FIDO2\_CapabilityArray](_f_i_d_o2___capability_array.md) \*\*capability) | 查询当前设备支持的客户端能力列表。当给定功能的值为true时，表示通行密钥客户端当前支持该能力。 |
| [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) [HMS\_FIDO2\_getPlatformAuthenticator](passkey.md#hms_fido2_getplatformauthenticator) ([FIDO2\_AuthenticatorMetadataArray](_f_i_d_o2___authenticator_metadata_array.md) \*\*authenticators) | 获取支持的平台身份认证器列表。 |
| [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) [HMS\_FIDO2\_register](passkey.md#hms_fido2_register) (const [FIDO2\_CredentialCreationOptions](_f_i_d_o2___credential_creation_options.md) options, const [FIDO2\_TokenBinding](_f_i_d_o2___token_binding.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAttestationCredential](_f_i_d_o2___public_key_attestation_credential.md) \*\*publicKeyAttestationCredential) | 通行密钥注册。 |
| [FIDO2\_ErrorCode](passkey.md#fido2_errorcode-1) [HMS\_FIDO2\_authenticate](passkey.md#hms_fido2_authenticate) (const [FIDO2\_CredentialRequestOptions](_f_i_d_o2___credential_request_options.md) options, const [FIDO2\_TokenBinding](_f_i_d_o2___token_binding.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAssertionCredential](_f_i_d_o2___public_key_assertion_credential.md) \*\*publicKeyAssertionCredential) | 基于fido2的认证。 |
| void [HMS\_FIDO2\_CapabilityArray\_Destroy](passkey.md#hms_fido2_capabilityarray_destroy) ([FIDO2\_CapabilityArray](_f_i_d_o2___capability_array.md) \*capability) | 释放能力的数组。 |
| void [HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy](passkey.md#hms_fido2_authenticatormetadataarray_destroy) ([FIDO2\_AuthenticatorMetadataArray](_f_i_d_o2___authenticator_metadata_array.md) \*authenticators) | 释放认证者元数据数组。 |
| void [HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy](passkey.md#hms_fido2_publickeyattestationcredential_destroy) ([FIDO2\_PublicKeyAttestationCredential](_f_i_d_o2___public_key_attestation_credential.md) \*publicKeyAttestationCredential) | 释放PublicKeyAttestationCredential的结构体。 |
| void [HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy](passkey.md#hms_fido2_publickeyassertioncredential_destroy) ([FIDO2\_PublicKeyAssertionCredential](_f_i_d_o2___public_key_assertion_credential.md) \*publicKeyAssertionCredential) | 释放PublicKeyAssertionCredential的结构体。 |

## 类型定义说明

### AuthenticationExtensionsClientOutputs

```
1. typedef struct AuthenticationExtensionsClientOutputs AuthenticationExtensionsClientOutputs
```

**描述**

身份认证扩展。

**起始版本：** 6.0.0(20)

### FIDO2\_Algorithm

```
1. typedef enum FIDO2_Algorithm FIDO2_Algorithm
```

**描述**

算法的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_AttestationConveyancePreference

```
1. typedef enum FIDO2_AttestationConveyancePreference FIDO2_AttestationConveyancePreference
```

**描述**

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

**起始版本：** 6.0.0(20)

### FIDO2\_AttestationFormatsArray

```
1. typedef struct FIDO2_AttestationFormatsArray FIDO2_AttestationFormatsArray
```

**描述**

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorAttachment

```
1. typedef enum FIDO2_AuthenticatorAttachment FIDO2_AuthenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorAttestationResponse

```
1. typedef struct FIDO2_AuthenticatorAttestationResponse FIDO2_AuthenticatorAttestationResponse
```

**描述**

认证器声明响应。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorMetadata

```
1. typedef struct FIDO2_AuthenticatorMetadata FIDO2_AuthenticatorMetadata
```

**描述**

认证器元数据。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorMetadataArray

```
1. typedef struct FIDO2_AuthenticatorMetadataArray FIDO2_AuthenticatorMetadataArray
```

**描述**

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorResponse

```
1. typedef struct FIDO2_AuthenticatorResponse FIDO2_AuthenticatorResponse
```

**描述**

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorSelectionCriteria

```
1. typedef struct FIDO2_AuthenticatorSelectionCriteria FIDO2_AuthenticatorSelectionCriteria
```

**描述**

由webAuthn依赖方指定，与认证器有关。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorTransport

```
1. typedef enum FIDO2_AuthenticatorTransport FIDO2_AuthenticatorTransport
```

**描述**

认证器传输方式的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_AuthenticatorTransportArray

```
1. typedef struct FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorTransportArray
```

**描述**

认证器传输方式数组。

**起始版本：** 6.0.0(20)

### FIDO2\_Capability

```
1. typedef struct FIDO2_Capability FIDO2_Capability
```

**描述**

通行密钥能力的结构体。

**起始版本：** 6.0.0(20)

### FIDO2\_CapabilityArray

```
1. typedef struct FIDO2_CapabilityArray FIDO2_CapabilityArray
```

**描述**

描述能力数组。

**起始版本：** 6.0.0(20)

### FIDO2\_ClientCapability

```
1. typedef enum FIDO2_ClientCapability FIDO2_ClientCapability
```

**描述**

客户端能力的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_CredentialCreationOptionArray

```
1. typedef struct FIDO2_CredentialCreationOptionArray FIDO2_CredentialCreationOptionArray
```

**描述**

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

### FIDO2\_CredentialCreationOptions

```
1. typedef struct FIDO2_CredentialCreationOptions FIDO2_CredentialCreationOptions
```

**描述**

凭据请求的选项。

**起始版本：** 6.0.0(20)

### FIDO2\_CredentialMediationRequirement

```
1. typedef enum FIDO2_CredentialMediationRequirement FIDO2_CredentialMediationRequirement
```

**描述**

用户介入要求的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_CredentialRequestOptions

```
1. typedef struct FIDO2_CredentialRequestOptions FIDO2_CredentialRequestOptions
```

**描述**

认证信息字典对象。

**起始版本：** 6.0.0(20)

### FIDO2\_ErrorCode

```
1. typedef enum FIDO2_ErrorCode FIDO2_ErrorCode
```

**描述**

错误码定义。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyAssertionCredential

```
1. typedef struct FIDO2_PublicKeyAssertionCredential FIDO2_PublicKeyAssertionCredential
```

**描述**

定义获取认证结果结构体。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyAttestationCredential

```
1. typedef struct FIDO2_PublicKeyAttestationCredential FIDO2_PublicKeyAttestationCredential
```

**描述**

定义获取注册结果结构体。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialCreationOptions

```
1. typedef struct FIDO2_PublicKeyCredentialCreationOptions FIDO2_PublicKeyCredentialCreationOptions
```

**描述**

创建新的认证凭据的选项。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialDescriptor

```
1. typedef struct FIDO2_PublicKeyCredentialDescriptor FIDO2_PublicKeyCredentialDescriptor
```

**描述**

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialDescriptorArray

```
1. typedef struct FIDO2_PublicKeyCredentialDescriptorArray FIDO2_PublicKeyCredentialDescriptorArray
```

**描述**

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialHint

```
1. typedef enum FIDO2_PublicKeyCredentialHint FIDO2_PublicKeyCredentialHint
```

**描述**

认证方式指示的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialHintArray

```
1. typedef struct FIDO2_PublicKeyCredentialHintArray FIDO2_PublicKeyCredentialHintArray
```

**描述**

认证方式指示数组。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialParameters

```
1. typedef struct FIDO2_PublicKeyCredentialParameters FIDO2_PublicKeyCredentialParameters
```

**描述**

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialRequestOptions

```
1. typedef struct FIDO2_PublicKeyCredentialRequestOptions FIDO2_PublicKeyCredentialRequestOptions
```

**描述**

定义通行密钥认证请求参数。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialRpEntity

```
1. typedef struct FIDO2_PublicKeyCredentialRpEntity FIDO2_PublicKeyCredentialRpEntity
```

**描述**

创建新凭据时依赖方的属性。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialType

```
1. typedef enum FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialType
```

**描述**

公钥凭据类型的枚举。

**起始版本：** 6.0.0(20)

### FIDO2\_PublicKeyCredentialUserEntity

```
1. typedef struct FIDO2_PublicKeyCredentialUserEntity FIDO2_PublicKeyCredentialUserEntity
```

**描述**

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

### FIDO2\_TokenBinding

```
1. typedef struct FIDO2_TokenBinding FIDO2_TokenBinding
```

**描述**

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

### FIDO2\_TokenBindingStatus

```
1. typedef enum FIDO2_TokenBindingStatus FIDO2_TokenBindingStatus
```

**描述**

TokenBinding协议的状态。

**起始版本：** 6.0.0(20)

### FIDO2\_UserVerificationRequirement

```
1. typedef enum FIDO2_UserVerificationRequirement FIDO2_UserVerificationRequirement
```

**描述**

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

**起始版本：** 6.0.0(20)

### FIDO2\_Uvm

```
1. typedef enum FIDO2_Uvm FIDO2_Uvm
```

**描述**

UVM的枚举。

**起始版本：** 6.0.0(20)

### Uint8Buff

```
1. typedef struct Uint8Buff Uint8Buff
```

**描述**

定义uint8\_t字节流。

**起始版本：** 6.0.0(20)

## 枚举类型说明

### FIDO2\_Algorithm

```
1. enum FIDO2_Algorithm
```

**描述**

加密算法的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_ES256 | ES256算法。 |
| FIDO2\_ES384 | ES384算法。 |
| FIDO2\_ES512 | ES512算法。 |
| FIDO2\_RS256 | RS256算法。 |
| FIDO2\_RS384 | RS384算法。 |
| FIDO2\_RS512 | RS512算法。 |
| FIDO2\_PS256 | PS256算法。 |
| FIDO2\_PS384 | PS384算法。 |
| FIDO2\_PS512 | PS512算法。 |

### FIDO2\_AttestationConveyancePreference

```
1. enum FIDO2_AttestationConveyancePreference
```

**描述**

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_NONE | 依赖方对认证者证明不感兴趣，默认值为none。 |
| FIDO2\_INDIRECT | 间接依赖方倾向于提供可认证的证明声明文档，但允许用户决定如何获得这种证明声明。 |
| FIDO2\_DIRECT | 直接依赖方希望接收认证者生成的证明声明。 |
| FIDO2\_ENTERPRISE | 依赖方希望接收企业证明。企业证明是一个证明声明， 其中可能包括唯一标识认证者的信息。 |

### FIDO2\_AuthenticatorAttachment

```
1. enum FIDO2_AuthenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_PLATFORM | 平台认证器，例如PIN码、指纹、人脸等。 |
| FIDO2\_CROSS\_PLATFORM | 跨平台认证器，即漫游认证器，包括蓝牙、NFC、USB等。 |

### FIDO2\_AuthenticatorTransport

```
1. enum FIDO2_AuthenticatorTransport
```

**描述**

认证器传输方式的枚举，表示认证器和客户端设备之间传递认证数据的方式。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_USB | USB方式。 |
| FIDO2\_NFC | NFC方式。 |
| FIDO2\_BLE | BLE方式。 |
| FIDO2\_SMART\_CARD | 智能卡方式。 |
| FIDO2\_HYBRID | 混合方式。即支持多种传输方式 |
| FIDO2\_INTERNAL | 内部方式。 |

### FIDO2\_ClientCapability

```
1. enum FIDO2_ClientCapability
```

**描述**

客户端能力的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_CONDITIONAL\_CREATE | 通行密钥注册。 |
| FIDO2\_CONDITIONAL\_GET | 通行密钥认证。 |
| FIDO2\_HYBRID\_TRANSPORT | 混合传输，表示支持多种传输方式。 |
| FIDO2\_PASSKEY\_PLATFORM\_AUTHENTICATOR | Passkey平台认证器。 |
| FIDO2\_USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR | 用户认证平台认证器。 |
| FIDO2\_RELATED\_ORIGINS | 支持相关源/域的凭据操作。 |
| FIDO2\_SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS | 发送所有接受的凭据。 |
| FIDO2\_SIGNAL\_CURRENT\_USER\_DETAILS | 发送当前用户详细信息。 |
| FIDO2\_SIGNAL\_UNKNOWN\_CREDENTIAL | 发送未知凭据。 |
| FIDO2\_EXTENSION\_UVI | uvi的扩展参数。 |

### FIDO2\_CredentialMediationRequirement

```
1. enum FIDO2_CredentialMediationRequirement
```

**描述**

用户介入要求的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_SILENT | 禁止用户介入指定的操作。如果可以在不需要用户介入的情况下进行操作，则正常。 如果需要用户介入，则操作将返回null。 |
| FIDO2\_OPTIONAL | 如果在没有用户介入的情况下，可以为给定的操作传递凭据，则正常传递。 如果需要用户介入，那么用户代理将让用户介入决策。 |
| FIDO2\_CONDITIONAL | 有条件的需要用户介入。对于认证场景，如果设备有凭据，则需要用户介入以选择凭据。对于注册场景，如果用户之前已同意创建凭据，可在无用户介入的情况下创建凭据。 |
| FIDO2\_MEDIATION\_REQUIRED | 在没有用户介入的情况下，用户代理将不会移交凭证。 |

### FIDO2\_ErrorCode

```
1. enum FIDO2_ErrorCode
```

**描述**

错误码定义。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_SUCCESS | 成功。 |
| FIDO2\_PERMISSION\_DENIED | 权限被拒绝。 |
| FIDO2\_DEVICE\_NOT\_SUPPORT | 设备类型错误。  **起始版本**：6.0.1(21) |
| FIDO2\_NOT\_SUPPORT | 系统不支持。 |
| FIDO2\_INVALID\_STATE | 无效的状态。 |
| FIDO2\_INTEGRITY\_CHECK\_FAILED | 系统完整性校验失败。 |
| FIDO2\_USER\_ABORT | 用户中止。 |
| FIDO2\_TIMEOUT | 超时。 |
| FIDO2\_ENCODING\_ERROR | 编码错误。 |
| FIDO2\_UNKNOWN\_ERROR | 未知错误。 |
| FIDO2\_CONSTRAINT\_ERROR | 约束条件错误。 |
| FIDO2\_DATA\_ERROR | 数据错误。 |
| FIDO2\_USER\_REJECTS | 用户拒绝。 |
| FIDO2\_CONNECT\_SERVICE\_FAILED | 连接服务失败。 |
| FIDO2\_MAX\_CRED\_NUM\_REACHED | 凭据达到上限。 |
| FIDO2\_INVALID\_CTAP\_COMMAND | 无效的CTAP命令。 |
| FIDO2\_INVALID\_PARAMETERS | 命令包含无效参数。 |
| FIDO2\_INVALID\_MESSAGE\_OR\_ATTRIBUTE\_LENGTH | 无效的消息或属性长度。 |
| FIDO2\_INVALID\_CBOR\_OR\_UNPREDICTABLE | 无效的CBOR或不可预知的错误。 |
| FIDO2\_PARSE\_CBOR\_FAILED | 解析CBOR失败。 |
| FIDO2\_INVALID\_CREDENTIALS | 未提供有效凭据。 |
| FIDO2\_NOT\_ALLOWED | 不允许。 |
| FIDO2\_USER\_VERIFICATION\_FAILED | 用户认证失败。 |
| FIDO2\_OTHER\_ERROR | 其他错误。 |

### FIDO2\_PublicKeyCredentialHint

```
1. enum FIDO2_PublicKeyCredentialHint
```

**描述**

认证方式指示的枚举，用于指示用户选用哪种认证方式。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_SECURITY\_KEY | 安全密钥。 |
| FIDO2\_CLIENT\_DEVICE | 客户端设备。 |
| FIDO2\_HINT\_HYBRID | 混合。 |

### FIDO2\_PublicKeyCredentialType

```
1. enum FIDO2_PublicKeyCredentialType
```

**描述**

公钥凭据类型的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_PUBLIC\_KEY | 公钥。 |

### FIDO2\_TokenBindingStatus

```
1. enum FIDO2_TokenBindingStatus
```

**描述**

TokenBinding协议的状态。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_PRESENT | 正常通信时的状态。 |
| FIDO2\_SUPPORTED | 支持令牌绑定，但是在与依赖方通信时未进行协商。 |

### FIDO2\_UserVerificationRequirement

```
1. enum FIDO2_UserVerificationRequirement
```

**描述**

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_REQUIRED | 需要进行用户认证。 |
| FIDO2\_PREFERRED | 在可能的情况下，依赖方优先处理操作的用户认证， 但如果响应没有设置用户认证标志，则不会失败。 |
| FIDO2\_DISCOURAGED | 依赖方在操作过程中不希望使用用户鉴权。 |

### FIDO2\_Uvm

```
1. enum FIDO2_Uvm
```

**描述**

UVM的枚举。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| FIDO2\_UVM\_FINGERPRINT | 指纹认证器。 |
| FIDO2\_UVM\_PIN | PIN认证器。 |
| FIDO2\_UVM\_FACEPRINT | 3D人脸认证器。 |

## 函数说明

### HMS\_FIDO2\_authenticate()

```
1. FIDO2_ErrorCode HMS_FIDO2_authenticate (const FIDO2_CredentialRequestOptions options, const FIDO2_TokenBinding tokenBinding, const char * origin, FIDO2_PublicKeyAssertionCredential ** publicKeyAssertionCredential)
```

**描述**

通行密钥认证。仅支持非UI线程调用。

**申请权限：** ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 认证请求选项。 |
| tokenBinding | 认证令牌绑定。 |
| origin | 调用该方法时的安全来源。长度限制0到256。 |
| publicKeyAssertionCredential | 认证响应。 |

**返回：**

如果函数执行成功，则返回FIDO2\_SUCCESS；如果函数执行失败，则返回特定的错误代码。详细信息请参见[FIDO2\_ErrorCode](passkey.md#fido2_errorcode)。

### HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy()

```
1. void HMS_FIDO2_AuthenticatorMetadataArray_Destroy (FIDO2_AuthenticatorMetadataArray * authenticators)
```

**描述**

释放认证者元数据数组。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| authenticators | 要释放的鉴权字元数据数组。 |

### HMS\_FIDO2\_CapabilityArray\_Destroy()

```
1. void HMS_FIDO2_CapabilityArray_Destroy (FIDO2_CapabilityArray * capability)
```

**描述**

释放能力的数组。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| capability | 要释放的能力的数组。 |

### HMS\_FIDO2\_getClientCapability()

```
1. FIDO2_ErrorCode HMS_FIDO2_getClientCapability (FIDO2_CapabilityArray ** capability)
```

**描述**

查询当前设备支持的客户端能力列表。当给定功能的值为true时，表示通行密钥客户端当前支持该能力。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| capability | 客户端是否支持此特性。 |

**返回：**

如果函数执行成功，则返回FIDO2\_SUCCESS； 如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2\_ErrorCode](passkey.md#fido2_errorcode)。

### HMS\_FIDO2\_getPlatformAuthenticator()

```
1. FIDO2_ErrorCode HMS_FIDO2_getPlatformAuthenticator (FIDO2_AuthenticatorMetadataArray ** authenticators)
```

**描述**

获取支持的平台身份认证器列表。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| authenticators | 支持的平台认证器列表。 |

**返回：**

如果函数执行成功，则返回FIDO2\_SUCCESS；如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2\_ErrorCode](passkey.md#fido2_errorcode)。

### HMS\_FIDO2\_initCreationOptions()

```
1. void HMS_FIDO2_initCreationOptions (FIDO2_CredentialCreationOptions * options)
```

**描述**

初始化FIDO2\_CredentialCreationOptions结构。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向要初始化的FIDO2\_CredentialCreationOptions结构体的指针。 |

### HMS\_FIDO2\_initRequestOptions()

```
1. void HMS_FIDO2_initRequestOptions (FIDO2_CredentialRequestOptions * options)
```

**描述**

初始化FIDO2\_CredentialRequestOptions结构。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向要初始化的FIDO2\_CredentialRequestOptions结构体的指针。 |

### HMS\_FIDO2\_initTokenBinding()

```
1. void HMS_FIDO2_initTokenBinding (FIDO2_TokenBinding * tokenBinding)
```

**描述**

初始化FIDO2\_TokenBinding结构体。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tokenBinding | 指向要初始化的FIDO2\_TokenBinding结构体的指针。 |

### HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy()

```
1. void HMS_FIDO2_PublicKeyAssertionCredential_Destroy (FIDO2_PublicKeyAssertionCredential * publicKeyAssertionCredential)
```

**描述**

释放PublicKeyAssertionCredential的结构体。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| publicKeyAssertionCredential | 要释放的PublicKeyAssertionCredential的结构体。 |

### HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy()

```
1. void HMS_FIDO2_PublicKeyAttestationCredential_Destroy (FIDO2_PublicKeyAttestationCredential * publicKeyAttestationCredential)
```

**描述**

释放PublicKeyAttestationCredential的结构体。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| publicKeyAttestationCredential | 要释放的PublicKeyAttestationCredential的结构体。 |

### HMS\_FIDO2\_register()

```
1. FIDO2_ErrorCode HMS_FIDO2_register (const FIDO2_CredentialCreationOptions options, const FIDO2_TokenBinding tokenBinding, const char * origin, FIDO2_PublicKeyAttestationCredential ** publicKeyAttestationCredential)
```

**描述**

通行密钥注册。仅支持非UI线程调用。

**申请权限：** ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 注册请求选项。 |
| tokenBinding | 注册令牌绑定。 |
| origin | 调用该方法时的来源。长度限制0到256。 |
| publicKeyAttestationCredential | 注册响应。 |

**返回：**

如果函数执行成功，则返回FIDO2\_SUCCESS；如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2\_ErrorCode](passkey.md#fido2_errorcode)。
