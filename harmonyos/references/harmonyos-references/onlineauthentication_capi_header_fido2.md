---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2
title: fido2_api.h
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 头文件 > fido2_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c3786434dbec342d37f8be6bde48cc6286f807b25cb089b586a53e58039ba5a
---

## 概述

定义身份认证扩展的接口。

**库：** libfido2\_ndk.z.so

**引用文件：** <OnlineAuthenticationKit/fido2\_api.h>

**系统能力：** SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

**相关模块：** [Passkey](passkey.md)

## 汇总

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
