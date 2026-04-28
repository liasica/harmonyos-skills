---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert
title: @ohos.security.cert (证书模块)
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > ArkTS API > @ohos.security.cert (证书模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f0dff72363f612a36218b4281c9002c3de27682155fd22d9efbdbb7fa5c2952d
---

证书算法库框架提供证书相关接口。其中，依赖加解密算法库框架的基础算法能力的部分，详细接口说明可参考[cryptoFramework API参考](js-apis-cryptoframework.md)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## CertResult

PhonePC/2in1TabletTVWearable

表示执行结果的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID\_PARAMS | 401 | 非法入参。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NOT\_SUPPORT | 801 | 操作不支持。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_OUT\_OF\_MEMORY | 19020001 | 内存错误。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_RUNTIME\_ERROR | 19020002 | 运行时外部错误。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_PARAMETER\_CHECK\_FAILED20+ | 19020003 | 参数检查失败。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| ERR\_CRYPTO\_OPERATION | 19030001 | 调用三方算法库API出错。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_CERT\_SIGNATURE\_FAILURE | 19030002 | 证书签名验证错误。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_CERT\_NOT\_YET\_VALID | 19030003 | 证书尚未生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_CERT\_HAS\_EXPIRED | 19030004 | 证书过期。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY | 19030005 | 无法获取证书的颁发者。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_KEYUSAGE\_NO\_CERTSIGN | 19030006 | 证书的密钥用途不含证书签名。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_KEYUSAGE\_NO\_DIGITAL\_SIGNATURE | 19030007 | 证书的密钥用途不含数字签名。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERR\_MAYBE\_WRONG\_PASSWORD18+ | 19030008 | 私钥密码错误。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## DataBlob

PhonePC/2in1TabletTVWearable

二进制数据的封装接口，核心字段data为Uint8Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 数据。 |

## DataArray

PhonePC/2in1TabletTVWearable

buffer数组的列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Array<Uint8Array> | 否 | 否 | 数据列表。 |

## EncodingFormat

PhonePC/2in1TabletTVWearable

表示证书编码格式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORMAT\_DER | 0 | DER格式。 |
| FORMAT\_PEM | 1 | PEM格式。 |
| FORMAT\_PKCS711+ | 2 | PKCS7格式。 |

## EncodingBaseFormat18+

PhonePC/2in1TabletTVWearable

表示生成CSR的编码格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | PEM格式。 |
| DER | 1 | DER格式。 |

## CsrAttribute18+

PhonePC/2in1TabletTVWearable

表示生成CSR的编码格式配置参数中的扩展。

openssl中规定了扩展类型，例如challengePassword、keyUsage等。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | openssl指定的扩展类型。 |
| value | string | 否 | 否 | 扩展值。 |

## CsrGenerationConfig18+

PhonePC/2in1TabletTVWearable

RSA私钥生成CSR时的配置参数，包含主体、扩展、摘要算法、输出格式等。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subject | [X500DistinguishedName](js-apis-cert.md#x500distinguishedname12) | 否 | 否 | X509定义的Name类型的对象。 |
| mdName | string | 否 | 否 | 摘要算法名。 |
| attributes | Array<[CsrAttribute](js-apis-cert.md#csrattribute18)> | 否 | 是 | 扩展。 |
| outFormat | [EncodingBaseFormat](js-apis-cert.md#encodingbaseformat18) | 否 | 是 | 输出类型。 |

说明

* subject是X509定义的Name类型的对象。
* mdName是摘要算法名，当前支持SHA1、SHA256、SHA384、SHA512。
* attributes是可选参数，指定openssl中规定的扩展类型跟扩展值生成CSR。例如challengePassword、keyUsage等。
* outFormat指定输出CSR的格式，若不指定默认为PEM格式。

## CertItemType10+

PhonePC/2in1TabletTVWearable

表示获取证书字段的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CERT\_ITEM\_TYPE\_TBS | 0 | 表示获取证书的待签名信息。 |
| CERT\_ITEM\_TYPE\_PUBLIC\_KEY | 1 | 表示获取证书的公钥信息。 |
| CERT\_ITEM\_TYPE\_ISSUER\_UNIQUE\_ID | 2 | 表示获取证书的颁发者唯一编号。 |
| CERT\_ITEM\_TYPE\_SUBJECT\_UNIQUE\_ID | 3 | 表示获取证书的主体唯一编号。 |
| CERT\_ITEM\_TYPE\_EXTENSIONS | 4 | 表示获取证书的扩展域信息。 |

## ExtensionOidType10+

PhonePC/2in1TabletTVWearable

表示获取扩展域中对象标识符类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTENSION\_OID\_TYPE\_ALL | 0 | 表示获取扩展域中所有的对象标识符。 |
| EXTENSION\_OID\_TYPE\_CRITICAL | 1 | 表示获取扩展域中critical为true的对象标识符。 |
| EXTENSION\_OID\_TYPE\_UNCRITICAL | 2 | 表示获取扩展域中critical为false的对象标识符。 |

## ExtensionEntryType10+

PhonePC/2in1TabletTVWearable

表示获取扩展域中对象类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTENSION\_ENTRY\_TYPE\_ENTRY | 0 | 表示获取整个对象。 |
| EXTENSION\_ENTRY\_TYPE\_ENTRY\_CRITICAL | 1 | 表示获取对象的critical属性。 |
| EXTENSION\_ENTRY\_TYPE\_ENTRY\_VALUE | 2 | 表示获取对象的数据。 |

## EncodingType12+

PhonePC/2in1TabletTVWearable

表示获取编码格式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENCODING\_UTF8 | 0 | UTF8编码格式。 |

## EncodingBlob

PhonePC/2in1TabletTVWearable

带编码格式的证书二进制数组。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 传入的证书数据。 |
| encodingFormat | [EncodingFormat](js-apis-cert.md#encodingformat) | 否 | 否 | 指明证书编码格式。 |

## CertChainData

PhonePC/2in1TabletTVWearable

证书链数据，在证书链校验时，作为入参传入。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 证书数据，按照长度（2字节）-数据的形式传入。如：08ABCDEFGH07ABCDEFG，第一本证书，前2个字节表示证书的长度为8字节，后面附加8字节的证书数据；第二本证书，前2个字节表示证书的长度为7字节，后面附加7字节的证书数据。 |
| count | number | 否 | 否 | 传入的数据中，包含的证书数量。 |
| encodingFormat | [EncodingFormat](js-apis-cert.md#encodingformat) | 否 | 否 | 指明证书编码格式。 |

## GeneralNameType12+

PhonePC/2in1TabletTVWearable

表示证书主体用途的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GENERAL\_NAME\_TYPE\_OTHER\_NAME | 0 | 表示其他名称。 |
| GENERAL\_NAME\_TYPE\_RFC822\_NAME | 1 | 表示电子邮件地址。 |
| GENERAL\_NAME\_TYPE\_DNS\_NAME | 2 | 表示一个DNS名称。 |
| GENERAL\_NAME\_TYPE\_X400\_ADDRESS | 3 | 表示X.400地址。 |
| GENERAL\_NAME\_TYPE\_DIRECTORY\_NAME | 4 | 表示一个目录名称。 |
| GENERAL\_NAME\_TYPE\_EDI\_PARTY\_NAME | 5 | 表示特定的EDI实体。 |
| GENERAL\_NAME\_TYPE\_UNIFORM\_RESOURCE\_ID | 6 | 表示一个统一资源标识符。 |
| GENERAL\_NAME\_TYPE\_IP\_ADDRESS | 7 | 表示一个IP地址。 |
| GENERAL\_NAME\_TYPE\_REGISTERED\_ID | 8 | 表示一个已注册的对象标识符。 |

## GeneralName12+

PhonePC/2in1TabletTVWearable

用于表示证书主体信息对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [GeneralNameType](js-apis-cert.md#generalname12) | 否 | 否 | 指定具体的证书主体类型。 |
| name | Uint8Array | 否 | 是 | 指定具体的证书主体DER格式内容。 |

## X509CertMatchParameters11+

PhonePC/2in1TabletTVWearable

用于匹配证书的过滤参数。如果参数中任一项都未指定，则匹配所有证书。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x509Cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 指定具体的证书对象。 |
| validDate | string | 否 | 是 | 指定证书有效期。 |
| issuer | Uint8Array | 否 | 是 | 指定证书颁发者，为DER编码格式。 |
| keyUsage | Array<boolean> | 否 | 是 | 指定是否需要匹配密钥用途。true为需要，false为不需要。 |
| serialNumber | bigint | 否 | 是 | 指定证书的序列号。 |
| subject | Uint8Array | 否 | 是 | 指定证书主题，DER编码格式。 |
| publicKey | [DataBlob](js-apis-cert.md#datablob) | 否 | 是 | 指定证书公钥，DER编码格式。 |
| publicKeyAlgID | string | 否 | 是 | 指定证书公钥的算法。 |
| subjectAlternativeNames12+ | Array<[GeneralName](js-apis-cert.md#generalname12)> | 否 | 是 | 指定证书主体名称。 |
| matchAllSubjectAltNames12+ | boolean | 否 | 是 | 指定是否需要匹配证书主体名称。true为需要，false为不需要。 |
| authorityKeyIdentifier12+ | Uint8Array | 否 | 是 | 指定证书颁发机构密钥。 |
| minPathLenConstraint12+ | number | 否 | 是 | 指定证书CA路径长度。 |
| extendedKeyUsage12+ | Array<string> | 否 | 是 | 指定证书扩展用途。 |
| nameConstraints12+ | Uint8Array | 否 | 是 | 指定证书的使用者名称。 |
| certPolicy12+ | Array<string> | 否 | 是 | 指定证书策略。 |
| privateKeyValid12+ | string | 否 | 是 | 指定证书私钥有效期。 |
| subjectKeyIdentifier12+ | Uint8Array | 否 | 是 | 指定证书公钥。 |

## X509CRLMatchParameters11+

PhonePC/2in1TabletTVWearable

用于匹配证书吊销列表的过滤参数。如果参数中任一项都未指定，则匹配所有证书吊销列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| issuer | Array<Uint8Array> | 否 | 是 | 指定颁发者作为过滤条件, 至少要匹配到其中一个issuer。 |
| x509Cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 指定具体的证书对象作为过滤条件, 判断该证书是否在CRL列表中。 |
| updateDateTime12+ | string | 否 | 是 | 指定证书更新时间。 |
| maxCRL12+ | bigint | 否 | 是 | 指定CRL个数最大值。 |
| minCRL12+ | bigint | 否 | 是 | 指定CRL个数最小值。 |

## CertChainBuildParameters12+

PhonePC/2in1TabletTVWearable

用于指定证书链创建参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certMatchParameters | [X509CertMatchParameters](js-apis-cert.md#x509certmatchparameters11) | 否 | 否 | 指定过滤条件。 |
| maxLength | number | 否 | 是 | 指定最终证书链中CA证书的最大长度。 |
| validationParameters | [CertChainValidationParameters](js-apis-cert.md#certchainvalidationparameters11) | 否 | 否 | 指定验证条件。 |

## CertChainBuildResult12+

PhonePC/2in1TabletTVWearable

用于指定证书链创建结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certChain | [X509CertChain](js-apis-cert.md#x509certchain11) | 是 | 否 | 生成的证书链对象。 |
| validationResult | [CertChainValidationResult](js-apis-cert.md#certchainvalidationresult11) | 是 | 否 | 指定最终证书链的最大长度。 |

## X509TrustAnchor11+

PhonePC/2in1TabletTVWearable

表示X509信任锚，用于校验证书链。使用信任锚中的证书或者公钥作为可信根，对证书链进行校验。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| CACert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 信任的CA证书。如果配置了CACert，则校验证书链时只使用CACert，不再使用CAPubKey和CASubject。 |
| CAPubKey | Uint8Array | 否 | 是 | 信任的CA证书公钥，DER格式。仅在未配置CACert时生效。 |
| CASubject | Uint8Array | 否 | 是 | 信任的CA证书主题，DER格式。仅在配置了CAPubKey时生效。校验对象根据CAPubKey类型（自签或上级）决定是校验根证书的主题还是颁发者。 |
| nameConstraints12+ | Uint8Array | 否 | 是 | 名称约束，DER格式。只校验当前证书链的叶子证书。 |

## RevocationCheckOptions12+

PhonePC/2in1TabletTVWearable

表示证书链在线校验证书吊销状态选项的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REVOCATION\_CHECK\_OPTION\_PREFER\_OCSP | 0 | 优先采用OCSP进行校验，默认采用CRL校验。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_ACCESS\_NETWORK | 1 | 支持通过访问网络获取CRL或OCSP响应进行吊销状态的校验，默认为关闭。仅支持通过证书中的CDP扩展中获取首个CRL分发点地址以检查证书吊销状态，或通过AIA扩展获取首个OCSP服务器地址以进行吊销状态验证，且仅支持http协议。必须声明ohos.permission.INTERNET权限。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_FALLBACK\_NO\_PREFER | 2 | 当ACCESS\_NETWORK选项打开时有效，如果优选的校验方法由于网络原因导致无法校验证书状态，则采用备选的方案进行校验。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_FALLBACK\_LOCAL | 3 | 当ACCESS\_NETWORK选项打开时有效，如果在线获取CRL和OCSP响应都由于网络的原因导致无法校验证书状态，则采用本地设置的CRL和OCSP响应进行校验。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_CHECK\_INTERMEDIATE\_CA\_ONLINE22+ | 4 | 当ACCESS\_NETWORK选项打开时有效。如果开启了该能力，对终端实体证书OCSP或CRL校验失败，则会继续校验中间证书的吊销情况。默认关闭。  **注意**：当前能力与REVOCATION\_CHECK\_OPTION\_LOCAL\_CRL\_ONLY\_CHECK\_END\_ENTITY\_CERT不能同时开启。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_LOCAL\_CRL\_ONLY\_CHECK\_END\_ENTITY\_CERT22+ | 5 | 如果开启了该能力，则会拿本地吊销列表校验终端实体证书的吊销情况。默认关闭。  **注意**：当前能力与REVOCATION\_CHECK\_OPTION\_CHECK\_INTERMEDIATE\_CA\_ONLINE不能同时开启。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| REVOCATION\_CHECK\_OPTION\_IGNORE\_NETWORK\_ERROR23+ | 6 | 如果开启了该能力，通过访问网络获取CRL或OCSP响应进行吊销状态的校验时，忽略网络不可达错误。默认关闭，默认情况下，网络不可达可能导致证书链校验失败。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ValidationPolicyType12+

PhonePC/2in1TabletTVWearable

表示证书链在线校验策略的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VALIDATION\_POLICY\_TYPE\_X509 | 0 | 默认值，不需要校验证书中的sslHostname或dNSName。 |
| VALIDATION\_POLICY\_TYPE\_SSL | 1 | 需要校验证书中的sslHostname或dNSName。 |

## KeyUsageType12+

PhonePC/2in1TabletTVWearable

表示证书中密钥用途的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEYUSAGE\_DIGITAL\_SIGNATURE | 0 | 证书持有者可以用证书中包含的私钥进行数字签名操作。 |
| KEYUSAGE\_NON\_REPUDIATION | 1 | 证书持有者不可否认使用证书中包含的私钥进行的数字签名操作。 |
| KEYUSAGE\_KEY\_ENCIPHERMENT | 2 | 证书持有者可以使用证书中包含的公钥进行密钥加密操作。 |
| KEYUSAGE\_DATA\_ENCIPHERMENT | 3 | 证书持有者可以使用证书中包含的公钥进行数据加密操作。 |
| KEYUSAGE\_KEY\_AGREEMENT | 4 | 证书持有者可以使用证书中包含的私钥进行密钥协商操作。 |
| KEYUSAGE\_KEY\_CERT\_SIGN | 5 | 证书持有者可以使用证书中包含的私钥对其他证书进行签名。 |
| KEYUSAGE\_CRL\_SIGN | 6 | 证书持有者可以使用证书中包含的私钥对证书吊销列表（CRL）进行签名。 |
| KEYUSAGE\_ENCIPHER\_ONLY | 7 | 证书持有者只能进行加密操作，不能进行解密操作。 |
| KEYUSAGE\_DECIPHER\_ONLY | 8 | 证书持有者只能进行解密操作，不能进行加密操作。 |

## RevocationCheckParameter12+

PhonePC/2in1TabletTVWearable

表示证书链校验证书吊销状态的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ocspRequestExtension | Array<Uint8Array> | 否 | 是 | 表示发送OCSP请求的扩展字段。 |
| ocspResponderURI | string | 否 | 是 | 表示用于OCSP请求的备选服务器URI地址，支持HTTP/HTTPS，具体配置由与服务器协商决定。  **说明**：当前URI只针对实体证书生效。 |
| ocspResponderCert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 表示用于OCSP响应的签名校验的签名证书。 |
| ocspResponses | Uint8Array | 否 | 是 | 表示用于OCSP服务器响应的备选数据。 |
| crlDownloadURI | string | 否 | 是 | 表示用于CRL请求的备选下载地址。  **说明**：当前URI只针对实体证书生效。 |
| options | Array<[RevocationCheckOptions](js-apis-cert.md#revocationcheckoptions12)> | 否 | 是 | 表示证书吊销状态查询的策略组合。 |
| ocspDigest | string | 否 | 是 | 表示OCSP通信时创建证书ID使用的哈希算法。默认为SHA256，支持可配置MD5、SHA1、SHA224、SHA256、SHA384、SHA512算法。 |

## CertChainValidationParameters11+

PhonePC/2in1TabletTVWearable

表示证书链校验的参数。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 是 | 表示需要校验证书的有效期。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| trustAnchors | Array<[X509TrustAnchor](js-apis-cert.md#x509trustanchor11)> | 否 | 否 | 表示信任锚列表。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| trustSystemCa20+ | boolean | 否 | 是 | 表示是否使用系统预置CA证书校验证书链。true表示使用；false表示不使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| allowDownloadIntermediateCa23+ | boolean | 否 | 是 | 表示是否允许尝试从网络下载缺失的中间CA证书。  true表示允许；false表示不允许。默认值为false。  下载地址将从证书AIA扩展中获取，仅支持http，如需使用网络下载，需申请ohos.permission.INTERNET权限。配置方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| certCRLs | Array<[CertCRLCollection](js-apis-cert.md#certcrlcollection11)> | 否 | 是 | 表示需要校验证书是否在证书吊销列表中。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| revocationCheckParam12+ | [RevocationCheckParameter](js-apis-cert.md#revocationcheckparameter12) | 否 | 是 | 表示需要在线校验证证书吊销状态的参数对象。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| policy12+ | [ValidationPolicyType](js-apis-cert.md#validationpolicytype12) | 否 | 是 | 表示需要校验证书的策略类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sslHostname12+ | string | 否 | 是 | 表示需要校验证书中主机名，与policy配合使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| keyUsage12+ | Array<[KeyUsageType](js-apis-cert.md#keyusagetype12)> | 否 | 是 | 表示需要校验证书中的密钥用途。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## CertChainValidationResult11+

PhonePC/2in1TabletTVWearable

表示证书链校验的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trustAnchor | [X509TrustAnchor](js-apis-cert.md#x509trustanchor11) | 是 | 否 | 表示信任锚。 |
| entityCert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 否 | 表示实体证书。 |

## EncodingBaseFormat18+

PhonePC/2in1TabletTVWearable

编码基础格式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | 表示PEM格式。 |
| DER | 1 | 表示DER格式。 |

## Pkcs12Data18+

PhonePC/2in1TabletTVWearable

表示返回P12文件的解析后的证书、私钥及其他证书合集。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| privateKey | string | Uint8Array | 否 | 是 | 表示P12文件解析后的私钥。 |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 表示P12文件解析后的证书。 |
| otherCerts | Array<[X509Cert](js-apis-cert.md#x509cert)> | 否 | 是 | 表示P12文件解析后的其他证书合集。 |

## Pkcs12ParsingConfig18+

PhonePC/2in1TabletTVWearable

表示解析P12文件的配置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | 否 | 否 | 表示P12文件的密码。 |
| needsPrivateKey | boolean | 否 | 是 | 表示是否获取私钥。默认为true。  true为获取，返回PKCS8编码的私钥数据；false为不获取。 |
| privateKeyFormat | [EncodingBaseFormat](js-apis-cert.md#encodingbaseformat18) | 否 | 是 | 表示获取私钥的格式，当前支持PEM和DER格式。参数缺省时，默认为PEM格式。  **注意**：当needsPrivateKey值为true时，该参数生效。 |
| needsCert | boolean | 否 | 是 | 表示是否获取证书。默认为true。true为获取，false为不获取。 |
| needsOtherCerts | boolean | 否 | 是 | 表示是否获取其他证书合集。默认为false。true为获取，false为不获取。 |

## PbesEncryptionAlgorithm21+

PhonePC/2in1TabletTVWearable

表示基于密码的加密算法枚举。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AES\_128\_CBC | 0 | AES-128-CBC加密算法。 |
| AES\_192\_CBC | 1 | AES-192-CBC加密算法。 |
| AES\_256\_CBC | 2 | AES-256-CBC加密算法。 |

## PbesParams21+

PhonePC/2in1TabletTVWearable

表示基于密码的加密算法参数，当前仅支持PBES2。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| saltLen | number | 否 | 是 | 表示盐值长度。默认为16，最小值为8。 |
| iterations | number | 否 | 是 | 表示迭代次数。默认为2048。 |
| encryptionAlgorithm | [PbesEncryptionAlgorithm](js-apis-cert.md#pbesencryptionalgorithm21) | 否 | 是 | 表示PBES加密算法类型。默认为AES\_256\_CBC。 |

## Pkcs12MacDigestAlgorithm21+

PhonePC/2in1TabletTVWearable

表示PKCS12 MAC摘要算法枚举。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHA256 | 0 | SHA256摘要算法。 |
| SHA384 | 1 | SHA384摘要算法。 |
| SHA512 | 2 | SHA512摘要算法。 |

## Pkcs12CreationConfig21+

PhonePC/2in1TabletTVWearable

表示创建P12文件的配置。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | 否 | 否 | 表示P12文件的密码。最小长度为4。 |
| keyEncParams | [PbesParams](js-apis-cert.md#pbesparams21) | 否 | 是 | 表示私钥加密的算法参数。 |
| encryptCert | boolean | 否 | 是 | 表示是否加密证书。默认为true。true为加密，false为不加密。 |
| certEncParams | [PbesParams](js-apis-cert.md#pbesparams21) | 否 | 是 | 表示证书加密的算法参数。 |
| macSaltLen | number | 否 | 是 | 表示P12 MAC的盐值长度。最小值为8，默认为16。 |
| macIterations | number | 否 | 是 | 表示P12 MAC的迭代次数。默认为2048。 |
| macDigestAlgorithm | [Pkcs12MacDigestAlgorithm](js-apis-cert.md#pkcs12macdigestalgorithm21) | 否 | 是 | 表示P12 MAC的摘要算法。默认为SHA256。 |

## CmsContentType18+

PhonePC/2in1TabletTVWearable

表示Cms内容类型的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIGNED\_DATA | 0 | 签名数据。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| ENVELOPED\_DATA22+ | 1 | 封装数据。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## CmsContentDataFormat18+

PhonePC/2in1TabletTVWearable

表示Cms内容数据格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BINARY | 0 | 表示二进制数据格式。 |
| TEXT | 1 | 表示文本数据格式。 |

## CmsFormat18+

PhonePC/2in1TabletTVWearable

表示Cms签名格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | 表示PEM格式。 |
| DER | 1 | 表示DER格式。 |

## CmsRsaSignaturePadding22+

PhonePC/2in1TabletTVWearable

表示RSA类型CMS签名填充方式的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PKCS1\_PADDING | 0 | PKCS1填充方式。 |
| PKCS1\_PSS\_PADDING | 1 | PKCS1 PSS填充方式。 |

## CmsKeyAgreeRecipientDigestAlgorithm22+

PhonePC/2in1TabletTVWearable

CMS KeyAgree类型接收者摘要算法的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHA256 | 0 | SHA256 算法 |
| SHA384 | 1 | SHA384 算法 |
| SHA512 | 2 | SHA512 算法 |

## CmsRecipientEncryptionAlgorithm22+

PhonePC/2in1TabletTVWearable

CMS接收者对称算法的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AES\_128\_CBC | 0 | AES\_128\_CBC 算法 |
| AES\_192\_CBC | 1 | AES\_192\_CBC 算法 |
| AES\_256\_CBC | 2 | AES\_256\_CBC 算法 |
| AES\_128\_GCM | 3 | AES\_128\_GCM 算法 |
| AES\_192\_GCM | 4 | AES\_192\_GCM 算法 |
| AES\_256\_GCM | 5 | AES\_256\_GCM 算法 |

## CmsCertType22+

PhonePC/2in1TabletTVWearable

从CMS中获取证书不同类型的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIGNER\_CERTS | 0 | 签名者证书 |
| ALL\_CERTS | 1 | 全部证书 |

## PrivateKeyInfo18+

PhonePC/2in1TabletTVWearable

表示私钥信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | Uint8Array | 否 | 否 | 未加密或加密的私钥，支持PEM或DER格式。 |
| password | string | 否 | 是 | 私钥的密码，如果私钥是加密的。 |

## CmsSignerConfig18+

PhonePC/2in1TabletTVWearable

表示Cms签名者的配置选项。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mdName | string | 否 | 否 | 消息摘要算法的名称，例如 "SHA384", 当前支持"SHA1"、"SHA256"、"SHA384"、"SHA512"。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| rsaSignaturePadding22+ | [CmsRsaSignaturePadding](js-apis-cert.md#cmsrsasignaturepadding22) | 否 | 是 | RSA 签名填充方式。默认值为：PKCS1\_PADDING。  当设置为 PKCS1\_PSS\_PADDING 时，mdName 必须为 "SHA256"、"SHA384" 或 "SHA512"。  **说明**：仅当签名者私钥类型为RSA时有效。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| addCert | boolean | 否 | 是 | 是否添加证书。默认为true。true为需要，false为不需要。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| addAttr | boolean | 否 | 是 | 是否添加签名属性。默认为true。true为需要，false为不需要。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| addSmimeCapAttr | boolean | 否 | 是 | 是否将SMIME能力添加到Cms对象。默认为true。true为需要，false为不需要。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## CmsKeyTransRecipientInfo22+

PhonePC/2in1TabletTVWearable

CMS封装数据的KeyTrans接收方信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 否 | RSA证书。 |

## CmsKeyAgreeRecipientInfo22+

PhonePC/2in1TabletTVWearable

CMS封装数据的KeyAgree接收方信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 否 | EC证书。 |
| digestAlgorithm | [CmsKeyAgreeRecipientDigestAlgorithm](js-apis-cert.md#cmskeyagreerecipientdigestalgorithm22) | 否 | 是 | KDF摘要算法，默认为SHA256。 |

## CmsRecipientInfo22+

PhonePC/2in1TabletTVWearable

CMS封装数据的接收者信息。

说明

至少需要设置一个接收者。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyTransInfo | [CmsKeyTransRecipientInfo](js-apis-cert.md#cmskeytransrecipientinfo22) | 否 | 是 | keyTrans接收者信息。 |
| keyAgreeInfo | [CmsKeyAgreeRecipientInfo](js-apis-cert.md#cmskeyagreerecipientinfo22) | 否 | 是 | keyAgree接收者信息。 |

## CmsGeneratorOptions18+

PhonePC/2in1TabletTVWearable

表示生成Cms签名结果的配置选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contentDataFormat | [CmsContentDataFormat](js-apis-cert.md#cmscontentdataformat18) | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |
| outFormat | [CmsFormat](js-apis-cert.md#cmsformat18) | 否 | 是 | Cms最终数据的输出格式。默认为DER。 |
| isDetached | boolean | 否 | 是 | Cms最终数据是否不包含原始数据。默认为false。true为包含，false为不包含。 |

## CmsVerificationConfig22+

PhonePC/2in1TabletTVWearable

CMS验证的配置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trustCerts | Array<[X509Cert](js-apis-cert.md#x509cert)> | 否 | 否 | 信任证书。  **说明**：需要配置所有签名者的信任证书。 |
| signerCerts | Array<[X509Cert](js-apis-cert.md#x509cert)> | 否 | 是 | 签名证书。默认为空。 |
| contentData | Uint8Array | 否 | 是 | 内容数据，如果是detached模式，则需要指定明文数据。attached模式可以不传。 |
| contentDataFormat | [CmsContentDataFormat](js-apis-cert.md#cmscontentdataformat18) | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |

## CmsEnvelopedDecryptionConfig22+

PhonePC/2in1TabletTVWearable

CMS解封装的配置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyInfo | [PrivateKeyInfo](js-apis-cert.md#privatekeyinfo18) | 否 | 是 | 私钥参数。默认为空。 |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 否 | 是 | 公钥证书。默认为空。 |
| encryptedContentData | Uint8Array | 否 | 是 | 加密的内容数据，如果CMS不包含指定数据。默认为空。 |
| contentDataFormat | [CmsContentDataFormat](js-apis-cert.md#cmscontentdataformat18) | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |

## cert.createX509Cert

PhonePC/2in1TabletTVWearable

createX509Cert(inStream : EncodingBlob, callback : AsyncCallback<X509Cert>) : void

表示创建X509证书对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | X509证书序列化数据。 |
| callback | AsyncCallback<[X509Cert](js-apis-cert.md#x509cert)> | 是 | 回调函数，表示X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. // 证书二进制数据，需业务自行赋值。
13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
15. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
16. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
17. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
18. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
19. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
20. 'Qw==\n' +
21. '-----END CERTIFICATE-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(certData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
30. if (error) {
31. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Cert result: success.');
34. }
35. });
```

## cert.createX509Cert

PhonePC/2in1TabletTVWearable

createX509Cert(inStream : EncodingBlob) : Promise<X509Cert>

表示创建X509证书对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | X509证书序列化数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509Cert](js-apis-cert.md#x509cert)> | 表示X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob).then(x509Cert => {
31. console.info('createX509Cert result: success.');
32. }).catch((error: BusinessError) => {
33. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
34. });
```

## X509Cert

PhonePC/2in1TabletTVWearable

X509证书类。

### verify

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对证书验签。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');

36. // 业务需通过上级X509Cert证书对象（或当前证书对象为自签名的证书）的getPublicKey获取PubKey。
37. try {
38. let pubKey = x509Cert.getPublicKey();

40. // 验证证书签名。
41. x509Cert.verify(pubKey, (err, data) => {
42. if (err) {
43. console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
44. } else {
45. console.info('verify result: success.');
46. }
47. });
48. } catch (error) {
49. let e: BusinessError = error as BusinessError;
50. console.error(`getPublicKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
51. }
52. }
53. });
```

### verify

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对证书验签。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 用于验签的公钥对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob).then(x509Cert => {
31. console.info('createX509Cert result: success.');

33. try {
34. // 业务需通过上级X509Cert证书对象（或当前证书对象为自签名的证书）的getPublicKey获取PubKey。
35. let pubKey = x509Cert.getPublicKey();
36. x509Cert.verify(pubKey).then(result => {
37. console.info('verify result: success.');
38. }).catch((error: BusinessError) => {
39. console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
40. });
41. } catch (error) {
42. console.error(`getPublicKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
43. }
44. }).catch((error: BusinessError) => {
45. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
46. });
```

### getEncoded

PhonePC/2in1TabletTVWearable

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EncodingBlob](js-apis-cert.md#encodingblob)> | 是 | 回调函数，表示X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. // 证书二进制数据，需业务自行赋值。
13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
15. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
16. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
17. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
18. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
19. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
20. 'Qw==\n' +
21. '-----END CERTIFICATE-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(certData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
30. if (error) {
31. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Cert result: success.');
34. x509Cert.getEncoded((error, data) => {
35. if (error) {
36. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
37. } else {
38. console.info('getEncoded result: success.');
39. }
40. });
41. }
42. });
```

### getEncoded

PhonePC/2in1TabletTVWearable

getEncoded() : Promise<EncodingBlob>

表示获取X509证书序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EncodingBlob](js-apis-cert.md#encodingblob)> | 表示X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
16. 'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
17. 'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
18. 'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
19. 'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
20. '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
21. 'BetUokslUfjT6+s/X4ByaxycAA==\n' +
22. '-----END CERTIFICATE-----\n';

24. // 证书二进制数据，需业务自行赋值。
25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(certData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };
30. cert.createX509Cert(encodingBlob).then(x509Cert => {
31. console.info('createX509Cert result: success.');
32. x509Cert.getEncoded().then(result => {
33. console.info('getEncoded result: success.');
34. }).catch((error: BusinessError) => {
35. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
36. });
37. }).catch((error: BusinessError) => {
38. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
39. });
```

### getPublicKey

PhonePC/2in1TabletTVWearable

getPublicKey() : cryptoFramework.PubKey

表示获取X509证书公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | X509证书公钥对象：仅用于X509Cert的verify接口。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let pubKey = x509Cert.getPublicKey();
37. } catch (error) {
38. let e: BusinessError = error as BusinessError;
39. console.error(`getPublicKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### checkValidityWithDate

PhonePC/2in1TabletTVWearable

checkValidityWithDate(date: string) : void

表示检查X509证书有效期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | string | 是 | 日期，为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');

36. let date = '231001000001Z';
37. // Verify the certificate validity period.
38. try {
39. x509Cert.checkValidityWithDate(date);
40. } catch (error) {
41. let e: BusinessError = error as BusinessError;
42. console.error(`checkValidityWithDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
43. }
44. }
45. });
```

### getVersion

PhonePC/2in1TabletTVWearable

getVersion() : number

表示获取X509证书版本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书版本。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. // 证书二进制数据，需业务自行赋值。
13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
15. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
16. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
17. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
18. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
19. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
20. 'Qw==\n' +
21. '-----END CERTIFICATE-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(certData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };
28. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
29. if (error) {
30. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Cert result: success.');
33. let version = x509Cert.getVersion();
34. }
35. });
```

### getSerialNumber(deprecated)

PhonePC/2in1TabletTVWearable

getSerialNumber() : number

表示获取X509证书序列号。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[getCertSerialNumber](js-apis-cert.md#getcertserialnumber10)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书序列号。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. // 证书二进制数据，需业务自行赋值。
13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
15. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
16. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
17. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
18. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
19. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
20. 'Qw==\n' +
21. '-----END CERTIFICATE-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(certData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
30. if (error) {
31. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Cert result: success.');
34. let serialNumber = x509Cert.getSerialNumber();
35. }
36. });
```

### getCertSerialNumber10+

PhonePC/2in1TabletTVWearable

getCertSerialNumber() : bigint

表示获取X509证书序列号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| bigint | 表示X509证书序列号。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let serialNumber = x509Cert.getCertSerialNumber();
37. } catch (err) {
38. let e: BusinessError = err as BusinessError;
39. console.error(`getCertSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getIssuerName

PhonePC/2in1TabletTVWearable

getIssuerName() : DataBlob

表示获取X509证书颁发者名称。

说明

获取到的X509证书颁发者名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let issuerName = x509Cert.getIssuerName();
37. } catch (err) {
38. let e: BusinessError = err as BusinessError;
39. console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getIssuerName20+

PhonePC/2in1TabletTVWearable

getIssuerName(encodingType: EncodingType): string

根据编码类型获取X509证书颁发者名称。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书颁发者名称，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDgTCCAmmgAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
16. 'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
17. '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMzA1MDk1MTIzWhcN\n' +
18. 'MzUwMzAzMDk1MTIzWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
19. 'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
20. '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkonJ4UIuxRzX\n' +
21. 'gr8fLU1PjadDWJp/GrxkYGe30TXqQHDh7O14Rc0xxacj3aLMNffzj+rhxUzl3C9p\n' +
22. 'wLzIVO2e3iC3Fx2csRzOSIdbimR8879/3uaW8CPkgqlKQw8FDwrGk0S26sdDV8of\n' +
23. '8AAHlrnUO2yyL53rAunn4ZKo4EyxHrvHmZKuv006onj0SByu8RNHx97v+4KaaY7p\n' +
24. 'HngTC55F0KVALiNGygJHeKP7GGxS7kpYV/CvBuABpA00WMqc7nmo2vCa4yC/mIk2\n' +
25. '5CF7l860rQ50HLjrmlDYJHpc8p88NJ2BEyHQWiN4YkSKDAKNr+SssD3Tf2wHSYxA\n' +
26. 'UwdgsatGlwIDAQABo1MwUTAdBgNVHQ4EFgQUMFEfTXLVm7D6fsC7LYtTMhIgVQUw\n' +
27. 'HwYDVR0jBBgwFoAUMFEfTXLVm7D6fsC7LYtTMhIgVQUwDwYDVR0TAQH/BAUwAwEB\n' +
28. '/zANBgkqhkiG9w0BAQsFAAOCAQEABCr9+iK30OSp67ksK1qhkKCzwKYDH2E5KEF4\n' +
29. '1E1/o4haXIR14V+5DGcX/1OH3Znd863TecQdNnCFMGArWygq8j7O0uStbWMb3Rhu\n' +
30. '+7RJ9GOCbBSeR3v2fC6+T3LI0Sm1G77xIYADmHGt33IW0DRKr44iOalwi6IbcqzD\n' +
31. 's9XlNO8e6ht2apeL656fjv1gCo/PA7e+A0QHn6zapggzEccEwKdFixCsw5ZMZaHm\n' +
32. 'adGz3lBCK+0QKYXYL1CtX/6wcDgQ9PuZSgdQgrudLKRN+843m3LJSUJ7AIyL1kQW\n' +
33. 'kY1ah7eSx4wwaKrLOM06ZkzORMnY5GAy8Aup+UCh6mWU3dPv3w==\n' +
34. '-----END CERTIFICATE-----\n';

36. let encodingBlob: cert.EncodingBlob = {
37. data: stringToUint8Array(certData),
38. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
39. encodingFormat: cert.EncodingFormat.FORMAT_PEM
40. };

42. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
43. if (error) {
44. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
45. } else {
46. console.info('createX509Cert result: success.');
47. try {
48. let issuerName = x509Cert.getIssuerName(cert.EncodingType.ENCODING_UTF8);
49. console.info('issuerName output is ' + issuerName);
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
55. });
```

### getSubjectName

PhonePC/2in1TabletTVWearable

getSubjectName(encodingType?: EncodingType) : DataBlob

表示获取X509证书主体名称。

说明

获取到的X509证书主体名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 否 | 编码类型。设置参数表示获取UTF8格式编码；不设置默认获取ASCII格式编码。  API 12后支持设置此参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书主体名称，转化成字符串后使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Incorrect parameter types;  2. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let subjectName = x509Cert.getSubjectName();
37. } catch (err) {
38. let e: BusinessError = err as BusinessError;
39. console.error(`getSubjectName failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. try {
42. let subjectNameutf8 = x509Cert.getSubjectName(cert.EncodingType.ENCODING_UTF8);
43. } catch (err) {
44. let e: BusinessError = err as BusinessError;
45. console.error(`getSubjectNameUtf8 failed, errCode: ${e.code}, errMsg: ${e.message}`);
46. }
47. }
48. });
```

### getNotBeforeTime

PhonePC/2in1TabletTVWearable

getNotBeforeTime() : string

表示获取X509证书有效期起始时间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书有效期起始时间，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let notBefore = x509Cert.getNotBeforeTime();
37. } catch (err) {
38. let e: BusinessError = err as BusinessError;
39. console.error(`getNotBeforeTime failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getNotAfterTime

PhonePC/2in1TabletTVWearable

getNotAfterTime() : string

表示获取X509证书有效期截止时间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书有效期截止时间，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. // 证书二进制数据，需业务自行赋值。
15. let certData = '-----BEGIN CERTIFICATE-----\n' +
16. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
17. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
18. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
19. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
20. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
21. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
22. 'Qw==\n' +
23. '-----END CERTIFICATE-----\n';

25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(certData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };

31. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
32. if (error) {
33. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
34. } else {
35. console.info('createX509Cert result: success.');
36. try {
37. let notAfter = x509Cert.getNotAfterTime();
38. } catch (err) {
39. let e: BusinessError = err as BusinessError;
40. console.error(`getNotAfterTime failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. });
```

### getSignature

PhonePC/2in1TabletTVWearable

getSignature() : DataBlob

表示获取X509证书签名数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. // 证书二进制数据，需业务自行赋值。
15. let certData = '-----BEGIN CERTIFICATE-----\n' +
16. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
17. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
18. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
19. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
20. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
21. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
22. 'Qw==\n' +
23. '-----END CERTIFICATE-----\n';

25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(certData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };

31. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
32. if (error) {
33. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
34. } else {
35. console.info('createX509Cert result: success.');
36. try {
37. let signature = x509Cert.getSignature();
38. } catch (err) {
39. let e: BusinessError = err as BusinessError;
40. console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. });
```

### getSignatureAlgName

PhonePC/2in1TabletTVWearable

getSignatureAlgName() : string

表示获取X509证书签名算法名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书签名算法名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. // 证书二进制数据，需业务自行赋值。
15. let certData = '-----BEGIN CERTIFICATE-----\n' +
16. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
17. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
18. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
19. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
20. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
21. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
22. 'Qw==\n' +
23. '-----END CERTIFICATE-----\n';

25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(certData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };

31. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
32. if (error) {
33. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
34. } else {
35. console.info('createX509Cert result: success.');
36. try {
37. let sigAlgName = x509Cert.getSignatureAlgName();
38. } catch (err) {
39. let e: BusinessError = err as BusinessError;
40. console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. });
```

### getSignatureAlgOid

PhonePC/2in1TabletTVWearable

getSignatureAlgOid() : string

表示获取X509证书签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书签名算法对象标志符OID。若OID长度超过128字节，则会被截断。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let sigAlgOid = x509Cert.getSignatureAlgOid();
37. } catch (err) {
38. let e: BusinessError = err as BusinessError;
39. console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getSignatureAlgParams

PhonePC/2in1TabletTVWearable

getSignatureAlgParams() : DataBlob

表示获取X509证书签名算法参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书签名算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIEETCCAs6gAwIBAgIUKRqK4hH6D1p3NSuChKOwHnIVx74wOAYJKoZIhvcNAQEK\n' +
16. 'MCugDTALBglghkgBZQMEAgGhGjAYBgkqhkiG9w0BAQgwCwYJYIZIAWUDBAIBMG0x\n' +
17. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDAR0ZXN0MQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
18. 'VQQKDAR0ZXN0MQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MRMwEQYJKoZI\n' +
19. 'hvcNAQkBFgR0ZXN0MB4XDTI1MTAzMDAxNDAzMVoXDTI2MTAzMDAxNDAzMVowbTEL\n' +
20. 'MAkGA1UEBhMCRU4xDTALBgNVBAgMBHRlc3QxDTALBgNVBAcMBHhpYW4xDTALBgNV\n' +
21. 'BAoMBHRlc3QxDTALBgNVBAsMBHRlc3QxDTALBgNVBAMMBHRlc3QxEzARBgkqhkiG\n' +
22. '9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaHZMj\n' +
23. 'UCQm53hgVYQq+kbmgKOH4e+vrsoAeOaX8KEgCbJfwLVpF7lj3Ld2c52X31JxziJx\n' +
24. 'D6rmGIk0Tp13/rNA/AZrmhbO/+PKKQiWQJpUbNI4A4scxELn9emLk8B3x76k8KGh\n' +
25. 'E7Re0XgKxfbZXU4AOZ0+9sXAZrSOPc8hYEfpwkGl09EojRuqQ4uSzjN3ikasfkZx\n' +
26. 'xM4twRPXiumC34+ep8Z1uxZy6MUClT2plNM8fAdfUwRY0lnKh2RjAJcK1lQBlPlW\n' +
27. 'Qc7S0/ifFXxgh+sBt+4dq+pphm5R/i6MIMWZ0JUg6tUlh1iY3nLVMVz0Z+LT7JUS\n' +
28. '5ILjwwybwhtatFh5AgMBAAGjUzBRMB0GA1UdDgQWBBQM3AOhyH6sHP7CJAB/Z5Xy\n' +
29. '4VQxJzAfBgNVHSMEGDAWgBQM3AOhyH6sHP7CJAB/Z5Xy4VQxJzAPBgNVHRMBAf8E\n' +
30. 'BTADAQH/MDgGCSqGSIb3DQEBCjAroA0wCwYJYIZIAWUDBAIBoRowGAYJKoZIhvcN\n' +
31. 'AQEIMAsGCWCGSAFlAwQCAQOCAQEAXhXExMyEnkBs9c6syxL4H98b9VtatezhKsMY\n' +
32. 'c4vTxw5D5IoN+SM+YS6wNKN1fh0fO8nZm7kHmB/KyxtdKja5cwGfhqwsY2NHOkK7\n' +
33. 'X5jWkbS0hbGPjj0UZkYRfC63d76lEPqz/bvf5Lgsv+W/J3ZFFBCV4tiBVr1ubpEy\n' +
34. '/n+C1r2NMxOKfGOEdE8tPa5LiR85/MYFaaAvzHVX4irXsQmzXPJMaMWt2DJAAze3\n' +
35. 'ro0L1Hcd3VKyh5fYowA6nCDpNkKtQnVG/102SOM8HBH7wMSMHpsDzZbTuWRNJ35J\n' +
36. 'ach83y13Yx4Td+DVsZgNjl/7yeA+XdusunygAnqHqx2brCTaNw==\n' +
37. '-----END CERTIFICATE-----\n';

39. let encodingBlob: cert.EncodingBlob = {
40. data: stringToUint8Array(certData),
41. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
42. encodingFormat: cert.EncodingFormat.FORMAT_PEM
43. };

45. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
46. if (error) {
47. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
48. } else {
49. console.info('createX509Cert result: success.');
50. try {
51. let sigAlgParams = x509Cert.getSignatureAlgParams();
52. } catch (err) {
53. let e: BusinessError = err as BusinessError;
54. console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
55. }
56. }
57. });
```

### getKeyUsage

PhonePC/2in1TabletTVWearable

getKeyUsage() : DataBlob

表示获取X509证书密钥用途。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书密钥用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDIjCCAgqgAwIBAgIUUb7sok900ODOxkyE1FzstJbKCSQwDQYJKoZIhvcNAQEL\n' +
16. 'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAxNTQ0NFoX\n' +
17. 'DTI2MTAzMDAxNTQ0NFowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
18. 'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv3+V/0Nl4rytCHNcb7PMpRbsxvOX\n' +
19. '8zxwfb+5McmJ8ZZj59My3oqF7YgFM1VgZjjwaz8HljXvoaxrUJWQEu6AYjIa5ywN\n' +
20. 'duySyyNNgfbqiwUOVdUICh3WsEjvvxK+8f55L3xU0LybZxyEf0+31pc15SzCvTvv\n' +
21. 'E0OC8n3bYr2Nn0mvwtMHIl0Dr6AZbP10B/KKk68oX9UYOlsp4y0GTEXVDt/9bScx\n' +
22. 'PV2WvaKPWcrQoJVz1ys2RtyUgcwPiWugQdx54xHG6zIAMYptKxDaHgsOEtUR4J1p\n' +
23. 'xP1Ih7fY2wFZkeyRZG05ivYVqSHzHQV9Z42i+KjzfJUsMQt9TosuSsDi1wIDAQAB\n' +
24. 'o2AwXjAdBgNVHQ4EFgQUKF6T271JCNpwjwyCSzTSN66T95EwHwYDVR0jBBgwFoAU\n' +
25. 'KF6T271JCNpwjwyCSzTSN66T95EwDwYDVR0TAQH/BAUwAwEB/zALBgNVHQ8EBAMC\n' +
26. 'BaAwDQYJKoZIhvcNAQELBQADggEBACa9A6d/cdFb7h8EMmjs0l+3aIAI10EskgRT\n' +
27. '+WHZ8zi+Q94/WEsOJW8CXIquJ2SxjXvl/A4UgrnfQyN+4kgEg7hLyuugg1QTk0so\n' +
28. 'Kj6tlG82Oxr/gjzxf3MMFhkzLpi2nUYu66HnskzAfI1XLuLz995qY0hCj9r2gUiX\n' +
29. '6GR0H4p9pO5h9Fx7pbyosr2sn/JZbo9j6fWSuuvqoedjEuIb8aRmB6kbUkjhh/Iz\n' +
30. '5htY+aYZz0pRSm2F93WLy6HBhPNdAmWOCpNXrynsRXDgCPKqeIasba8MBjXTsqvI\n' +
31. 'mgbc4MCLhLciWi34u9NpkAGbkwYVLE6URw/o373mD9fqe214Jdw=\n' +
32. '-----END CERTIFICATE-----\n';

34. let encodingBlob: cert.EncodingBlob = {
35. data: stringToUint8Array(certData),
36. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
37. encodingFormat: cert.EncodingFormat.FORMAT_PEM
38. };

40. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
41. if (error) {
42. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
43. } else {
44. console.info('createX509Cert result: success.');
45. try {
46. let keyUsage = x509Cert.getKeyUsage();
47. } catch (err) {
48. let e: BusinessError = err as BusinessError;
49. console.error(`getKeyUsage failed, errCode: ${e.code}, errMsg: ${e.message}`);
50. }
51. }
52. });
```

### getExtKeyUsage

PhonePC/2in1TabletTVWearable

getExtKeyUsage() : DataArray

表示获取X509证书扩展密钥用途。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataArray](js-apis-cert.md#dataarray) | 表示X509证书扩展密钥用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDNDCCAhygAwIBAgIUJBLt/gmdgnDAq21wWU4R7rzgE5cwDQYJKoZIhvcNAQEL\n' +
16. 'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyMzMxOVoX\n' +
17. 'DTI2MTAzMDAyMzMxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
18. 'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0p3wb2jK23w+mihsah0w4wRaJ1TC\n' +
19. 'YC20ODjSHyyCL75XfR6n87DdXvb15a71hkD/1cdgDRxIO91hNu04Ru4MFL0CqgTM\n' +
20. 'ERSwZZGVo9DzJSG5q22FgbIFPi+XpTPtKk7mOCggPsfIrV1G0OH9zTREWoZ2/fJD\n' +
21. 'Pj0MiaPlYtS4Jolu0qDnRZjgP8yVdaV4Upvni1PNX60rZfhf5YC4yvkMmpnyoUOZ\n' +
22. 'IS3I/QucXZaiwXAO4ziHjYXtlp2aeUnrWSoRs3sFrsIVGB9x0ZYjwCwiih9TqaBK\n' +
23. 'SY1CKSQE5xjVP1uY5JwJ6A5N648J3JjGosYEsXT+WieJ4SGHafGa2DGd2wIDAQAB\n' +
24. 'o3IwcDAdBgNVHQ4EFgQUDyuOK1aix/tBR3QViD7TYdrDUQEwHwYDVR0jBBgwFoAU\n' +
25. 'DyuOK1aix/tBR3QViD7TYdrDUQEwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHSUEFjAU\n' +
26. 'BggrBgEFBQcDAQYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAC0A7HqO/OL0\n' +
27. 'Ve8HTUqM31hFxXYiqDum/gPiegXDA+9ixEP2Fjz8vmhe75FX5XOvCk0+FWRayoVw\n' +
28. 'lc7TD7SfV/oHRZVY58H8+Qxe5Rf4xQfOBNpG81uz73gfq3zIbzfJXxWlUpnBs6Tf\n' +
29. 'P44NZboLpgaA0eMI7NwZJyomZ98qOK3PmxBL9qATmDep2GM6VlOuapYh2fo8wFhY\n' +
30. 'DSp2EmcbIN9F+RPNrP+BvM/x2ZBtBoSFLh8jQ+GnP6g26DL57JBuBemt00BuYLOg\n' +
31. 'fF00YBUgwK9tIFfI5IAfrwEF8Y49XIzpXrHuMZZXbuESzQMBsAZAYqIgi2p5dAon\n' +
32. 'gdg3C4I6QRY=\n' +
33. '-----END CERTIFICATE-----\n';

35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(certData),
37. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
38. encodingFormat: cert.EncodingFormat.FORMAT_PEM
39. };

41. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
42. if (error) {
43. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
44. } else {
45. console.info('createX509Cert result: success.');
46. try {
47. let extKeyUsage = x509Cert.getExtKeyUsage();
48. } catch (err) {
49. let e: BusinessError = err as BusinessError;
50. console.error(`getExtKeyUsage failed, errCode: ${e.code}, errMsg: ${e.message}`);
51. }
52. }
53. });
```

### getBasicConstraints

PhonePC/2in1TabletTVWearable

getBasicConstraints() : number

表示获取X509证书基本约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书基本约束。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. // 证书二进制数据，需业务自行赋值。
13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
15. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
16. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
17. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
18. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
19. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
20. 'Qw==\n' +
21. '-----END CERTIFICATE-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(certData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
30. if (error) {
31. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Cert result: success.');
34. let basicConstraints = x509Cert.getBasicConstraints();
35. }
36. });
```

### getSubjectAltNames

PhonePC/2in1TabletTVWearable

getSubjectAltNames() : DataArray

表示获取X509证书主体可选名称。

说明

获取到的X509证书主体可选名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataArray](js-apis-cert.md#dataarray) | 表示X509证书主体可选名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDRjCCAi6gAwIBAgIUU3RfsnV6Ur2a514YvAygbMvcjaowDQYJKoZIhvcNAQEL\n' +
16. 'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyNDIyM1oX\n' +
17. 'DTI2MTAzMDAyNDIyM1owGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
18. 'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5yQDXUKnsNTPkqwVzCjtaE+Q8Tla\n' +
19. 'Qod6tb0fo044DLrYFvly6W10sqfvqZpuEfUuyzh/cs7279SoP8FYjnrykcE3yxqu\n' +
20. '3N6vNn6iXm3CQnjlqBVB7ChTcoXv8GEwHNXcjNTaX3FZQW62WAYLLER4I9/ZwE/N\n' +
21. 'iqf+rJu5O2eRzZ4AFappCLquFSp6Yw5yyhenhNFd026dBf58ggpUs0H9DThxS3N3\n' +
22. 'GFUs6JDiOJpxjbv+p7ns9MsryqewB8i5TCJjMJkcCg+2YyKFKYDv3mC4eoV71MU0\n' +
23. 'DVoy7sBhs1naTV7joM+wGSOLcW3ee6K9qCp8zXmqN1tRJOYxm/JkVvi5oQIDAQAB\n' +
24. 'o4GDMIGAMB0GA1UdDgQWBBTXIqHf66clGd8UhAr2SJSaukwphDAfBgNVHSMEGDAW\n' +
25. 'gBTXIqHf66clGd8UhAr2SJSaukwphDAPBgNVHRMBAf8EBTADAQH/MC0GA1UdEQQm\n' +
26. 'MCSCC2V4YW1wbGUuY29tgg93d3cuZXhhbXBsZS5jb22HBH8AAAEwDQYJKoZIhvcN\n' +
27. 'AQELBQADggEBABI/bnHX9xqw/3RfvEqXp/ocmI0Dm7XwQZ6MS9XlTgYVp9rPYFbz\n' +
28. 'eS79q47nV1SMKc6LDeLoDcHT04aYGsKrA0O/9VVFhb50S1JBoa3HrEe0Q5WD4k48\n' +
29. 'GUJE2CaaO+MG3P9ZF4P3qxvPZ1PLoHr2B2YkaIMapjlNDUyTGLyWwPEuJSraBiXj\n' +
30. 'hnl1C9D5Y7ss8zuh4zzJl8MtU36kk19BbBglZVE0H7KDGGhqqvEbIFBNZmqy2vb3\n' +
31. '7xSbXJL0/SQV+nr2Qvv8DU4XZJliJKVJHr3GkrqXRSFVVZ0ADNpEdLxFT0IF1X/T\n' +
32. 'JiAZrIdZPozWsjUVtQ4KVMJj+D7canRVuCg=\n' +
33. '-----END CERTIFICATE-----\n';

35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(certData),
37. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
38. encodingFormat: cert.EncodingFormat.FORMAT_PEM
39. };

41. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
42. if (error) {
43. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
44. } else {
45. console.info('createX509Cert result: success.');
46. try {
47. let subjectAltNames = x509Cert.getSubjectAltNames();
48. } catch (err) {
49. let e: BusinessError = err as BusinessError;
50. console.error(`getSubjectAltNames failed, errCode: ${e.code}, errMsg: ${e.message}`);
51. }
52. }
53. });
```

### getIssuerAltNames

PhonePC/2in1TabletTVWearable

getIssuerAltNames() : DataArray

表示获取X509证书颁发者可选名称。

说明

获取到的X509证书颁发者可选名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataArray](js-apis-cert.md#dataarray) | 表示X509证书颁发者可选名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIC9zCCAd+gAwIBAgIUS3GIfzu10vWzw2RSLbxTxxMfz/wwDQYJKoZIhvcNAQEL\n' +
16. 'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyNDkzNFoX\n' +
17. 'DTI2MTAzMDAyNDkzNFowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
18. 'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvKGnKn9NZoFOzdffrCIE01dTCiIo\n' +
19. 'XPweKanLs49ZaxpEJ48OCP4vs8qmedsW1pUMpe7kQQyRINZ5tvXyFbiBS1u4clN/\n' +
20. 'nU+E8rhNMa+2LA2YOUH/fC1ikussXq+acqjEqRbM900QdkmPzJX3NcloGYwdVfAe\n' +
21. '3ENEXHaXvj1qrf6pF5mbdelnlp1TrjpnXT4sSQaKbFjZrNl+zTT4xbIxTHR0cB8S\n' +
22. 'oOVc3jI57rtP6x0FcLWzE/LX1E8eUkCIHEapPjqsGzLNtJTJI8z9QLinFIRmjdSI\n' +
23. '0xS8Qj/QitrOswzjHie2fgaz1LZx76CZGExC5f6f3Em5hJx6rjYysmEZBQIDAQAB\n' +
24. 'ozUwMzAxBgNVHRIEKjAogRJpc3N1ZXJAZXhhbXBsZS5jb22CEmlzc3Vlci5leGFt\n' +
25. 'cGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAI5UjPssP3VzV2m47ke2nytAsTt9Y\n' +
26. 'DNYKhqM4qZVVaIj5BRmca1jJXnWAgV4uUbad92E7R8askfSuJkBVtLJD5kSMTQrK\n' +
27. '5vYPbZ/WSRKthSbMotcynz/vWjBh4XY7bmiZC71ZNBCq9ybWRNzv61D9N1CJOlr6\n' +
28. 'W+1zCYq9dFDYf1nJ60qvkYHmzX3o0a1LHdiTHHvUZIIFXkJ50+NDIbruh8j8Lijk\n' +
29. 'Eed63QMcrSfLuIIAgoPoWo8WK2+AmA3k3EoTRvci5Ck+HDlLULBhyCrp+QUvn6OR\n' +
30. 'B7ZBoW+U/OIpNTI4rvsn3rcdkZAVcwRI0vV04IDB52jRzUArSi+08ggCiQ==\n' +
31. '-----END CERTIFICATE-----\n';

33. let encodingBlob: cert.EncodingBlob = {
34. data: stringToUint8Array(certData),
35. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
36. encodingFormat: cert.EncodingFormat.FORMAT_PEM
37. };

39. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
40. if (error) {
41. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
42. } else {
43. console.info('createX509Cert result: success.');
44. try {
45. let issuerAltNames = x509Cert.getIssuerAltNames();
46. } catch (err) {
47. let e: BusinessError = err as BusinessError;
48. console.error(`getIssuerAltNames failed, errCode: ${e.code}, errMsg: ${e.message}`);
49. }
50. }
51. });
```

### getItem10+

PhonePC/2in1TabletTVWearable

getItem(itemType: CertItemType) : DataBlob

表示获取X509证书对应的字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | [CertItemType](js-apis-cert.md#certitemtype10) | 是 | 表示需要获取的证书字段。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书对应的字段，返回值为DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书二进制数据，需业务自行赋值。
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. cert.createX509Cert(encodingBlob, (error, x509Cert) => {
31. if (error) {
32. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. } else {
34. console.info('createX509Cert result: success.');
35. try {
36. let tbs = x509Cert.getItem(cert.CertItemType.CERT_ITEM_TYPE_TBS);
37. let pubKey = x509Cert.getItem(cert.CertItemType.CERT_ITEM_TYPE_PUBLIC_KEY);
38. } catch (err) {
39. let e: BusinessError = err as BusinessError;
40. console.error(`getItem failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. });
```

### match11+

PhonePC/2in1TabletTVWearable

match(param: X509CertMatchParameters): boolean

判断证书是否与输入参数匹配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CertMatchParameters](js-apis-cert.md#x509certmatchparameters11) | 是 | 表示需要匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当参数匹配时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509Cert(): Promise<cert.X509Cert> {
14. let certData =  '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDTTCCAjWgAwIBAgIBAzANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
16. 'IENBMB4XDTI0MDMxOTAyMDM1NFoXDTM0MDMxNzAyMDM1NFowETEPMA0GA1UEAwwG\n' +
17. 'ZGV2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuoGk2J0aKWTP\n' +
18. 'J3D7lS3oFdME3MMA1z0Y0ftthrtUKybE2xh8P90ztMV73bewmgAPqiApqhaWEZM/\n' +
19. '6DSLc/MxbOeYjg6njveJIu721gchiuB2PFikDFSWlcLOJNw+CgBx77Ct3KllivHs\n' +
20. 'oi/gjuxrWiF/3VhbBErPNj/fw9se3pVrFRXIFdkcybtom2mUmkcxDfSg587SO14i\n' +
21. 'ZzXGM6nhMzYWXxLho6SJrsnzfs4pD6ifksWmY4089zitqsN+9jQXafY1+/sh1mgu\n' +
22. 'FvAwg9IbigGOBIiF8t5qdNGpqCHXbEHblNCWfT4fVNDV0Vc9pByjZaMYEGMhpz+6\n' +
23. 'lxlc2CqbNQIDAQABo4GuMIGrMAkGA1UdEwQCMAAwHQYDVR0OBBYEFAEVpuP+pPpg\n' +
24. 'kr3dA3aV2XdFZ9rGMB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMB0G\n' +
25. 'A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjALBgNVHQ8EBAMCB4AwMgYIKwYB\n' +
26. 'BQUHAQEEJjAkMCIGCCsGAQUFBzABhhZodHRwczovLzEyNy4wLjAuMTo5OTk5MA0G\n' +
27. 'CSqGSIb3DQEBCwUAA4IBAQBjM1agcDcgVHsD0dS39gxtlyRbZRvDcW3YsdwgpN6S\n' +
28. 'e4wGzdZbhsiZv7y3+PSuozKwp5Yjn+UqnnEz7QuTGJRt/pzHDVY3QceNvlx2HPRe\n' +
29. 'fECS4bpGLcM5B17oZZjE4HenIrGmigXnnwYL5TjhC4ybtddXPYv/M6z2eFCnfQNa\n' +
30. 'zFwz8LJ7ukWvf5koBqcHq2zsuVByOIPXLIrAJPtMmBb/pHCFt8hxOxwqujdrxz16\n' +
31. 'pe5LQUYzvG1YCxw3Ye9OrM1yXJQr/4KYncQC1yQQo+UK7NsDRK30PsMEYxhierLA\n' +
32. 'JKyPn1xSlOJiGa2rRn/uevmEOhfagj5TtprU9Gu1+nZo\n' +
33. '-----END CERTIFICATE-----\n';

35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(certData),
37. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
38. encodingFormat: cert.EncodingFormat.FORMAT_PEM
39. };

41. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
42. try {
43. x509Cert = await cert.createX509Cert(encodingBlob);
44. } catch (err) {
45. let e: BusinessError = err as BusinessError;
46. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
47. }
48. return x509Cert;
49. }

51. async function matchX509Cert() {
52. const x509Cert = await createX509Cert();
53. try {
54. // 需业务自行赋值。
55. const param: cert.X509CertMatchParameters = {
56. x509Cert,
57. validDate: '20241121074700Z',
58. keyUsage: [true, false, false, false, false, false, false, false, false],
59. publicKeyAlgID: '1.2.840.113549.1.1.1'
60. };
61. const result = x509Cert.match(param);
62. console.info('call x509Cert match result: success.');
63. } catch (err) {
64. let e: BusinessError = err as BusinessError;
65. console.error(`call x509Cert match failed, errCode: ${e.code}, errMsg: ${e.message}`);
66. }
67. }
```

### getCRLDistributionPoint12+

PhonePC/2in1TabletTVWearable

getCRLDistributionPoint(): DataArray

获取X509证书CRL的分发点统一资源标识符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataArray](js-apis-cert.md#dataarray) | 表示X509证书CRL的分发点统一资源标识符。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIB/jCCAaSgAwIBAgICA+gwCgYIKoZIzj0EAwIwLDELMAkGA1UEBhMCQ04xDTAL\n' +
15. 'BgNVBAoMBHRlc3QxDjAMBgNVBAMMBXN1YmNhMB4XDTIzMTAwNzA0MDEwOFoXDTMz\n' +
16. 'MTAwNDA0MDEwOFowLDELMAkGA1UEBhMCQ04xDTALBgNVBAoMBHRlc3QxDjAMBgNV\n' +
17. 'BAMMBWxvY2FsMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEZDPvdlJI6Yv4fiaR\n' +
18. 'nQHcusXVbukk90mQ0rBGOYRikFvgvm5cjTdaUGcQKEtwYIKDQl5n6Pf7ElCJ7GRz\n' +
19. 'raWZ+qOBtTCBsjAJBgNVHRMEAjAAMCwGCWCGSAGG+EIBDQQfFh1PcGVuU1NMIEdl\n' +
20. 'bmVyYXRlZCBDZXJ0aWZpY2F0ZTAdBgNVHQ4EFgQU63Gbl8gIsUn0VyZ4rya3PCjm\n' +
21. 'sfEwHwYDVR0jBBgwFoAU77mynM0rz1SD43DQjleWM7bF+MEwNwYDVR0fBDAwLjAs\n' +
22. 'oCqgKIYmaHR0cDovL3Rlc3QudGVzdENSTGRwLmNvbS9DUkxfRFBfMS5jcmwwCgYI\n' +
23. 'KoZIzj0EAwIDSAAwRQIhAISKHH9u221mBgdDWfll3loLvEHJ3or9NUO5Zn6SrX6L\n' +
24. 'AiAtRlOa6/mTD68faQTdhsAaQP955QfW34B4yFqU2Bq72A==\n' +
25. '-----END CERTIFICATE-----\n';

27. // 证书二进制数据，需业务自行赋值。
28. let encodingBlob: cert.EncodingBlob = {
29. data: stringToUint8Array(certData),
30. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
31. encodingFormat: cert.EncodingFormat.FORMAT_PEM
32. };

34. async function certGetCRLDistributionPoint() {
35. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
36. try {
37. x509Cert = await cert.createX509Cert(encodingBlob);
38. console.info('createX509Cert result: success.');
39. let point = x509Cert.getCRLDistributionPoint();
40. } catch (err) {
41. let e: BusinessError = err as BusinessError;
42. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
43. }
44. }
```

### getIssuerX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

getIssuerX500DistinguishedName(): X500DistinguishedName

获取颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [X500DistinguishedName](js-apis-cert.md#x500distinguishedname12) | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
15. 'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
16. 'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
17. 'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
18. 'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
19. 'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
20. 'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
21. 'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
22. 'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
23. 'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
24. '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
25. 'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
26. '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
27. 'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
28. 'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
29. 'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
30. 'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
31. '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
32. 'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
33. 'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
34. 'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
35. '-----END CERTIFICATE-----\n'

37. // 证书二进制数据，需业务自行赋值。
38. let encodingBlob: cert.EncodingBlob = {
39. data: stringToUint8Array(certData),
40. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
41. encodingFormat: cert.EncodingFormat.FORMAT_PEM
42. };

44. async function certGetIssuerX500DistinguishedName() {
45. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
46. try {
47. x509Cert = await cert.createX509Cert(encodingBlob);
48. console.info('createX509Cert result: success.');
49. let name = x509Cert.getIssuerX500DistinguishedName();
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
```

### getSubjectX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

getSubjectX500DistinguishedName(): X500DistinguishedName

获取证书主题的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [X500DistinguishedName](js-apis-cert.md#x500distinguishedname12) | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
15. 'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
16. 'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
17. 'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
18. 'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
19. 'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
20. 'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
21. 'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
22. 'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
23. 'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
24. '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
25. 'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
26. '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
27. 'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
28. 'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
29. 'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
30. 'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
31. '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
32. 'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
33. 'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
34. 'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
35. '-----END CERTIFICATE-----\n'

37. // 证书二进制数据，需业务自行赋值。
38. let encodingBlob: cert.EncodingBlob = {
39. data: stringToUint8Array(certData),
40. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
41. encodingFormat: cert.EncodingFormat.FORMAT_PEM
42. };

44. async function certGetSubjectX500DistinguishedName() {
45. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
46. try {
47. x509Cert = await cert.createX509Cert(encodingBlob);
48. console.info('createX509Cert result: success.');
49. let name = x509Cert.getSubjectX500DistinguishedName();
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
```

### toString12+

PhonePC/2in1TabletTVWearable

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
15. 'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
16. 'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
17. 'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
18. 'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
19. 'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
20. 'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
21. 'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
22. 'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
23. 'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
24. '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
25. 'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
26. '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
27. 'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
28. 'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
29. 'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
30. 'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
31. '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
32. 'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
33. 'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
34. 'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
35. '-----END CERTIFICATE-----\n'

37. // 证书二进制数据，需业务自行赋值。
38. let encodingBlob: cert.EncodingBlob = {
39. data: stringToUint8Array(certData),
40. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
41. encodingFormat: cert.EncodingFormat.FORMAT_PEM
42. };

44. async function certToString() {
45. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
46. try {
47. x509Cert = await cert.createX509Cert(encodingBlob);
48. console.info('createX509Cert result: success.');
49. console.info('certToString success: ' + x509Cert.toString());
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
```

### toString20+

PhonePC/2in1TabletTVWearable

toString(encodingType: EncodingType): string

根据编码类型获取对象的字符串类型数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIDgTCCAmmgAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
15. 'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
16. '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMzA1MDk1MTIzWhcN\n' +
17. 'MzUwMzAzMDk1MTIzWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
18. 'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
19. '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkonJ4UIuxRzX\n' +
20. 'gr8fLU1PjadDWJp/GrxkYGe30TXqQHDh7O14Rc0xxacj3aLMNffzj+rhxUzl3C9p\n' +
21. 'wLzIVO2e3iC3Fx2csRzOSIdbimR8879/3uaW8CPkgqlKQw8FDwrGk0S26sdDV8of\n' +
22. '8AAHlrnUO2yyL53rAunn4ZKo4EyxHrvHmZKuv006onj0SByu8RNHx97v+4KaaY7p\n' +
23. 'HngTC55F0KVALiNGygJHeKP7GGxS7kpYV/CvBuABpA00WMqc7nmo2vCa4yC/mIk2\n' +
24. '5CF7l860rQ50HLjrmlDYJHpc8p88NJ2BEyHQWiN4YkSKDAKNr+SssD3Tf2wHSYxA\n' +
25. 'UwdgsatGlwIDAQABo1MwUTAdBgNVHQ4EFgQUMFEfTXLVm7D6fsC7LYtTMhIgVQUw\n' +
26. 'HwYDVR0jBBgwFoAUMFEfTXLVm7D6fsC7LYtTMhIgVQUwDwYDVR0TAQH/BAUwAwEB\n' +
27. '/zANBgkqhkiG9w0BAQsFAAOCAQEABCr9+iK30OSp67ksK1qhkKCzwKYDH2E5KEF4\n' +
28. '1E1/o4haXIR14V+5DGcX/1OH3Znd863TecQdNnCFMGArWygq8j7O0uStbWMb3Rhu\n' +
29. '+7RJ9GOCbBSeR3v2fC6+T3LI0Sm1G77xIYADmHGt33IW0DRKr44iOalwi6IbcqzD\n' +
30. 's9XlNO8e6ht2apeL656fjv1gCo/PA7e+A0QHn6zapggzEccEwKdFixCsw5ZMZaHm\n' +
31. 'adGz3lBCK+0QKYXYL1CtX/6wcDgQ9PuZSgdQgrudLKRN+843m3LJSUJ7AIyL1kQW\n' +
32. 'kY1ah7eSx4wwaKrLOM06ZkzORMnY5GAy8Aup+UCh6mWU3dPv3w==\n' +
33. '-----END CERTIFICATE-----\n';

35. // 证书二进制数据，需业务自行赋值。
36. let encodingBlob: cert.EncodingBlob = {
37. data: stringToUint8Array(certData),
38. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
39. encodingFormat: cert.EncodingFormat.FORMAT_PEM
40. };

42. async function certToString() {
43. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
44. try {
45. x509Cert = await cert.createX509Cert(encodingBlob);
46. console.info('createX509Cert result: success.');
47. console.info('certToString success: ' + x509Cert.toString(cert.EncodingType.ENCODING_UTF8));
48. } catch (err) {
49. let e: BusinessError = err as BusinessError;
50. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
51. }
52. }
```

### hashCode12+

PhonePC/2in1TabletTVWearable

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
15. 'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
16. 'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
17. 'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
18. 'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
19. 'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
20. 'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
21. 'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
22. 'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
23. 'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
24. '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
25. 'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
26. '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
27. 'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
28. 'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
29. 'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
30. 'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
31. '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
32. 'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
33. 'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
34. 'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
35. '-----END CERTIFICATE-----\n'

37. // 证书二进制数据，需业务自行赋值。
38. let encodingBlob: cert.EncodingBlob = {
39. data: stringToUint8Array(certData),
40. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
41. encodingFormat: cert.EncodingFormat.FORMAT_PEM
42. };

44. async function certHashCode() {
45. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
46. try {
47. x509Cert = await cert.createX509Cert(encodingBlob);
48. console.info('createX509Cert result: success.');
49. console.info('certHashCode success: ' + x509Cert.hashCode());
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
```

### getExtensionsObject12+

PhonePC/2in1TabletTVWearable

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CertExtension](js-apis-cert.md#certextension10) | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
15. 'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
16. 'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
17. 'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
18. 'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
19. 'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
20. 'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
21. 'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
22. 'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
23. 'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
24. '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
25. 'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
26. '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
27. 'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
28. 'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
29. 'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
30. 'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
31. '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
32. 'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
33. 'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
34. 'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
35. '-----END CERTIFICATE-----\n'

37. // 证书二进制数据，需业务自行赋值。
38. let encodingBlob: cert.EncodingBlob = {
39. data: stringToUint8Array(certData),
40. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
41. encodingFormat: cert.EncodingFormat.FORMAT_PEM
42. };

44. async function certGetExtensionsObject() {
45. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
46. try {
47. x509Cert = await cert.createX509Cert(encodingBlob);
48. console.info('createX509Cert result: success.');
49. let object = x509Cert.getExtensionsObject();
50. } catch (err) {
51. let e: BusinessError = err as BusinessError;
52. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
53. }
54. }
```

## cert.createCertExtension10+

PhonePC/2in1TabletTVWearable

createCertExtension(inStream : EncodingBlob, callback : AsyncCallback<CertExtension>) : void

表示创建证书扩展域段的对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书扩展域段序列化数据。 |
| callback | AsyncCallback<[CertExtension](js-apis-cert.md#certextension10)> | 是 | 回调函数，表示扩展域段对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // 证书扩展域段二进制数据，需业务自行赋值。
4. let extData = new Uint8Array([
5. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
6. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
7. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
8. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
9. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
10. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
11. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
12. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
13. 0xD9, 0xE4
14. ]);

16. let encodingBlob: cert.EncodingBlob = {
17. data: extData,
18. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
19. encodingFormat: cert.EncodingFormat.FORMAT_DER
20. };

22. cert.createCertExtension(encodingBlob, (error, certExt) => {
23. if (error) {
24. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
25. } else {
26. console.info('createCertExtension result: success.');
27. }
28. });
```

## cert.createCertExtension10+

PhonePC/2in1TabletTVWearable

createCertExtension(inStream : EncodingBlob) : Promise<CertExtension>

表示创建证书扩展域段的对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书扩展域段序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CertExtension](js-apis-cert.md#certextension10)> | 表示证书扩展域段对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 证书扩展域段二进制数据，需业务自行赋值。
5. let extData = new Uint8Array([
6. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
7. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
8. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
9. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
10. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
11. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
12. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
13. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
14. 0xD9, 0xE4
15. ]);

17. let encodingBlob: cert.EncodingBlob = {
18. data: extData,
19. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
20. encodingFormat: cert.EncodingFormat.FORMAT_DER
21. };

23. cert.createCertExtension(encodingBlob).then(certExt => {
24. console.info('createCertExtension result: success.');
25. }).catch((error: BusinessError) => {
26. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
27. });
```

## CertExtension10+

PhonePC/2in1TabletTVWearable

证书扩展域段类。

### getEncoded10+

PhonePC/2in1TabletTVWearable

getEncoded() : EncodingBlob

表示获取证书扩展域段序列化数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EncodingBlob](js-apis-cert.md#encodingblob) | 表示证书扩展域段序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 证书扩展域段二进制数据，需业务自行赋值。
5. let extData = new Uint8Array([
6. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
7. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
8. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
9. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
10. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
11. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
12. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
13. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
14. 0xD9, 0xE4
15. ]);

17. let encodingBlob: cert.EncodingBlob = {
18. data: extData,
19. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
20. encodingFormat: cert.EncodingFormat.FORMAT_DER
21. };

23. cert.createCertExtension(encodingBlob, (error, certExt) => {
24. if (error) {
25. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
26. } else {
27. console.info('createCertExtension result: success.');
28. try {
29. let extEncodedBlob = certExt.getEncoded();
30. } catch (err) {
31. let e: BusinessError = err as BusinessError;
32. console.error(`ext getEncoded failed, errCode: ${e.code}, errMsg: ${e.message}`);
33. }
34. }
35. });
```

### getOidList10+

PhonePC/2in1TabletTVWearable

getOidList(valueType : ExtensionOidType) : DataArray

表示获取证书扩展域段对象标识符列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valueType | [ExtensionOidType](js-apis-cert.md#extensionoidtype10) | 是 | 表示证书扩展域段对象标识符类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataArray](js-apis-cert.md#dataarray) | 表示证书扩展域段对象标识符列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 证书扩展域段二进制数据，需业务自行赋值。
5. let extData = new Uint8Array([
6. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
7. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
8. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
9. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
10. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
11. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
12. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
13. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
14. 0xD9, 0xE4
15. ]);

17. let encodingBlob: cert.EncodingBlob = {
18. data: extData,
19. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
20. encodingFormat: cert.EncodingFormat.FORMAT_DER
21. };

23. cert.createCertExtension(encodingBlob, (error, certExt) => {
24. if (error) {
25. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
26. } else {
27. console.info('createCertExtension result: success.');
28. try {
29. let oidList = certExt.getOidList(cert.ExtensionOidType.EXTENSION_OID_TYPE_ALL);
30. } catch (err) {
31. let e: BusinessError = err as BusinessError;
32. console.error(`ext getOidList failed, errCode: ${e.code}, errMsg: ${e.message}`);
33. }
34. }
35. });
```

### getEntry10+

PhonePC/2in1TabletTVWearable

getEntry(valueType: ExtensionEntryType, oid : DataBlob) : DataBlob

表示获取证书扩展域段对象信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valueType | [ExtensionEntryType](js-apis-cert.md#extensionentrytype10) | 是 | 表示证书扩展域段获取的类型。 |
| oid | [DataBlob](js-apis-cert.md#datablob) | 是 | 表示证书扩展域段获取的对象标识符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示证书扩展域段对象的数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 证书扩展域段二进制数据，需业务自行赋值。
5. let extData = new Uint8Array([
6. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
7. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
8. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
9. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
10. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
11. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
12. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
13. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
14. 0xD9, 0xE4
15. ]);

17. let encodingBlob: cert.EncodingBlob = {
18. data: extData,
19. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
20. encodingFormat: cert.EncodingFormat.FORMAT_DER
21. };

23. cert.createCertExtension(encodingBlob, (error, certExt) => {
24. if (error) {
25. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
26. } else {
27. console.info('createCertExtension result: success.');
28. let oid = new Uint8Array([0x32, 0x2e, 0x35, 0x2e, 0x32, 0x39, 0x2e, 0x31, 0x35]);
29. let oidBlob: cert.DataBlob = {
30. data: oid
31. }
32. try {
33. let entry = certExt.getEntry(cert.ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, oidBlob);
34. } catch (err) {
35. let e: BusinessError = err as BusinessError;
36. console.error(`ext getEntry failed, errCode: ${e.code}, errMsg: ${e.message}`);
37. }
38. }
39. });
```

### checkCA10+

PhonePC/2in1TabletTVWearable

checkCA() : number

表示校验证书是否为CA证书。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 当证书扩展域段中密钥用途包含签名用途，并且基本约束中cA字段为true时，表示证书为CA证书。如果不是CA，则返回-1；否则返回基本约束中的路径长度。如果证书是CA证书，但是基本约束中未给定路径长度，则返回-2，表示无路径长度限制。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 证书扩展域段二进制数据，需业务自行赋值。
5. let extData = new Uint8Array([
6. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
7. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
8. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
9. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
10. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
11. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
12. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
13. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
14. 0xD9, 0xE4
15. ]);

17. let encodingBlob: cert.EncodingBlob = {
18. data: extData,
19. // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
20. encodingFormat: cert.EncodingFormat.FORMAT_DER
21. };
22. cert.createCertExtension(encodingBlob, (error, certExt) => {
23. if (error) {
24. console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
25. } else {
26. console.info('createCertExtension result: success.');
27. try {
28. let res = certExt.checkCA();
29. } catch (err) {
30. let e: BusinessError = err as BusinessError;
31. console.error(`ext checkCA failed, errCode: ${e.code}, errMsg: ${e.message}`);
32. }
33. }
34. });
```

### hasUnsupportedCriticalExtension11+

PhonePC/2in1TabletTVWearable

hasUnsupportedCriticalExtension(): boolean

判断是否存在不支持的关键扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当存在不支持的关键扩展时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let encodingData = new Uint8Array([
5. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
6. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
7. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
8. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
9. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
10. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
11. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
12. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
13. 0xD9, 0xE4
14. ]);
15. let encodingBlob: cert.EncodingBlob = {
16. data: new Uint8Array(encodingData),
17. encodingFormat: cert.EncodingFormat.FORMAT_DER
18. };

20. cert.createCertExtension(encodingBlob).then((extensionObj) => {
21. console.info('createCertExtension result: success.');
22. const result = extensionObj.hasUnsupportedCriticalExtension()
23. console.info('has unsupported critical extension result =' + result);
24. }).catch((err: BusinessError) => {
25. console.error(`createCertExtension failed, errCode: ${err.code}, errMsg: ${err.message}`);
26. });
```

## cert.createX509Crl(deprecated)

PhonePC/2in1TabletTVWearable

createX509Crl(inStream : EncodingBlob, callback : AsyncCallback<X509Crl>) : void

表示创建X509证书吊销列表的对象。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[cert.createX509CRL](js-apis-cert.md#certcreatex509crl11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书吊销列表序列化数据。 |
| callback | AsyncCallback<[X509Crl](js-apis-cert.md#x509crldeprecated)> | 是 | 回调函数，表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
29. if (error) {
30. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Crl result: success.');
33. }
34. });
```

## cert.createX509Crl(deprecated)

PhonePC/2in1TabletTVWearable

createX509Crl(inStream : EncodingBlob) : Promise<X509Crl>

表示创建X509证书吊销列表的对象。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[cert.createX509CRL](js-apis-cert.md#certcreatex509crl11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书吊销列表序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[X509Crl](js-apis-cert.md#x509crldeprecated)> | 表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob).then(x509Crl => {
30. console.info('createX509Crl result: success.');
31. }).catch((error: BusinessError) => {
32. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. });
```

## cert.createX509CRL11+

PhonePC/2in1TabletTVWearable

createX509CRL(inStream : EncodingBlob, callback : AsyncCallback<X509CRL>) : void

表示创建X509证书吊销列表的对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书吊销列表序列化数据。当前支持的数据长度不超过8192字节。 |
| callback | AsyncCallback<[X509CRL](js-apis-cert.md#x509crl11)> | 是 | 回调函数，表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (error, X509CRL) => {
29. if (error) {
30. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509CRL result: success.');
33. }
34. });
```

## cert.createX509CRL11+

PhonePC/2in1TabletTVWearable

createX509CRL(inStream : EncodingBlob) : Promise<X509CRL>

表示创建X509证书吊销列表的对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | 表示证书吊销列表序列化数据。当前支持的数据长度不超过8192字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CRL](js-apis-cert.md#x509crl11)> | 表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob).then(X509CRL => {
30. console.info('createX509CRL result: success.');
31. }).catch((error: BusinessError) => {
32. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
33. });
```

## X509Crl(deprecated)

PhonePC/2in1TabletTVWearable

X509证书吊销列表对象。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL](js-apis-cert.md#x509crl11)替代。

### isRevoked(deprecated)

PhonePC/2in1TabletTVWearable

isRevoked(cert : X509Cert) : boolean

表示检查证书是否吊销。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.isRevoked](js-apis-cert.md#isrevoked11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 表示被检查的证书对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示证书吊销状态，true表示已吊销，false表示未吊销。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. let certData = '-----BEGIN CERTIFICATE-----\n' +
23. 'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
24. 'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
25. 'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
26. 'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
27. 'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
28. '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
29. 'BetUokslUfjT6+s/X4ByaxycAA==\n' +
30. '-----END CERTIFICATE-----\n';

32. // 证书吊销列表二进制数据，需业务自行赋值。
33. let encodingBlob: cert.EncodingBlob = {
34. data: stringToUint8Array(crlData),
35. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
36. encodingFormat: cert.EncodingFormat.FORMAT_PEM
37. };

39. let certEncodingBlob: cert.EncodingBlob = {
40. data: stringToUint8Array(certData),
41. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
42. encodingFormat: cert.EncodingFormat.FORMAT_PEM
43. };

45. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
46. if (error) {
47. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
48. } else {
49. console.info('createX509Crl result: success.');
50. // Create an X509Cert instance.
51. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
52. if (error) {
53. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
54. } else {
55. try {
56. let revokedFlag = x509Crl.isRevoked(x509Cert);
57. } catch (error) {
58. let e: BusinessError = error as BusinessError;
59. console.error(`isRevoked failed, errCode: ${e.code}, errMsg: ${e.message}`);
60. }
61. }
62. });
63. }
64. });
```

### getType(deprecated)

PhonePC/2in1TabletTVWearable

getType() : string

表示获取证书吊销列表类型。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getType](js-apis-cert.md#gettype11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书吊销列表类型。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
29. if (error) {
30. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Crl result: success.');
33. let type = x509Crl.getType();
34. }
35. });
```

### getEncoded(deprecated)

PhonePC/2in1TabletTVWearable

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书吊销列表的序列化数据。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getEncoded](js-apis-cert.md#getencoded11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EncodingBlob](js-apis-cert.md#encodingblob)> | 是 | 回调函数，表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
29. if (error) {
30. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Crl result: success.');
33. x509Crl.getEncoded((error, data) => {
34. if (error) {
35. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
36. } else {
37. console.info('getEncoded result: success.');
38. }
39. });
40. }
41. });
```

### getEncoded(deprecated)

PhonePC/2in1TabletTVWearable

getEncoded() : Promise<EncodingBlob>

表示获取X509证书吊销列表的序列化数据。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getEncoded](js-apis-cert.md#getencoded11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EncodingBlob](js-apis-cert.md#encodingblob)> | 表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob).then(x509Crl => {
30. console.info('createX509Crl result: success.');
31. x509Crl.getEncoded().then(result => {
32. console.info('getEncoded result: success.');
33. }).catch((error: BusinessError) => {
34. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. });
36. }).catch((error: BusinessError) => {
37. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. });
```

### verify(deprecated)

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对X509证书吊销列表进行验签。使用callback异步回调。验签支持RSA算法。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.verify](js-apis-cert.md#verify11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 表示用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数,使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. let pubKeyData = new Uint8Array([
24. 0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
25. 0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
26. 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
27. 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
28. 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
29. 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
30. 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
31. 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
32. 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
33. 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
34. 0x00, 0x01
35. ]);

37. let priKeyData = new Uint8Array([
38. 0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
39. 0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
40. 0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
41. 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
42. 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
43. 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
44. 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
45. 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
46. 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
47. 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
48. 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
49. 0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
50. 0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
51. 0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
52. 0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
53. 0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
54. 0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
55. 0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
56. 0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
57. 0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
58. 0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
59. 0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
60. 0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
61. 0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
62. 0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
63. 0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
64. 0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
65. 0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
66. 0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
67. 0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
68. 0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
69. 0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
70. 0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
71. 0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
72. 0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
73. 0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
74. 0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
75. 0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
76. 0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
77. 0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
78. ]);

80. // 证书吊销列表二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(crlData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
88. if (error) {
89. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
90. } else {
91. console.info('createX509Crl result: success.');
92. try {
93. let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
94. console.info('createAsyKeyGenerator result: success.');
95. let priEncodingBlob: cryptoFramework.DataBlob = {
96. data: priKeyData,
97. };
98. let pubEncodingBlob: cryptoFramework.DataBlob = {
99. data: pubKeyData,
100. };
101. keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob, (e, keyPair) => {
102. if (e) {
103. console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
104. } else {
105. console.info('convert key result: success.');
106. x509Crl.verify(keyPair.pubKey, (err, data) => {
107. if (err) {
108. console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
109. } else  {
110. console.info('verify result: success.');
111. }
112. });
113. }
114. })
115. } catch (error) {
116. let e: BusinessError = error as BusinessError;
117. console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
118. }
119. }
120. });
```

### verify(deprecated)

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对X509证书吊销列表进行验签。使用Promise异步回调。验签支持RSA算法。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.verify](js-apis-cert.md#verify11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 表示用于验签的公钥对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit'
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. let pubKeyData = new Uint8Array([
24. 0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
25. 0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
26. 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
27. 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
28. 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
29. 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
30. 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
31. 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
32. 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
33. 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
34. 0x00, 0x01
35. ]);

37. let priKeyData = new Uint8Array([
38. 0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
39. 0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
40. 0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
41. 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
42. 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
43. 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
44. 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
45. 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
46. 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
47. 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
48. 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
49. 0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
50. 0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
51. 0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
52. 0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
53. 0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
54. 0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
55. 0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
56. 0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
57. 0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
58. 0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
59. 0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
60. 0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
61. 0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
62. 0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
63. 0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
64. 0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
65. 0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
66. 0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
67. 0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
68. 0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
69. 0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
70. 0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
71. 0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
72. 0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
73. 0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
74. 0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
75. 0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
76. 0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
77. 0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
78. ]);

80. // 证书吊销列表二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(crlData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. cert.createX509Crl(encodingBlob).then(x509Crl => {
88. console.info('createX509Crl result: success.');

90. try {
91. // 生成公钥对象。
92. let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
93. console.info('createAsyKeyGenerator result: success.');
94. let priEncodingBlob: cryptoFramework.DataBlob = {
95. data: priKeyData,
96. };
97. let pubEncodingBlob: cryptoFramework.DataBlob = {
98. data: pubKeyData,
99. };
100. keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob).then((keyPair) => {
101. console.info('convert key result: success.');
102. x509Crl.verify(keyPair.pubKey).then(result => {
103. console.info('verify result: success.');
104. }).catch((error: BusinessError) => {
105. console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
106. });
107. }).catch((error: BusinessError) => {
108. console.error(`convert key failed, errCode: ${error.code}, errMsg: ${error.message}`);
109. });
110. } catch (error) {
111. let e: BusinessError = error as BusinessError;
112. console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
113. }
114. }).catch((error: BusinessError) => {
115. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
116. });
```

### getVersion(deprecated)

PhonePC/2in1TabletTVWearable

getVersion() : number

表示获取X509证书吊销列表的版本号。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getVersion](js-apis-cert.md#getversion11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示获取X509证书吊销列表的版本号。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
29. if (error) {
30. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Crl result: success.');
33. let version = x509Crl.getVersion();
34. }
35. });
```

### getIssuerName(deprecated)

PhonePC/2in1TabletTVWearable

getIssuerName() : DataBlob

表示获取X509证书吊销列表颁发者名称。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getIssuerName](js-apis-cert.md#getissuername11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let issuerName = x509Crl.getIssuerName();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getLastUpdate(deprecated)

PhonePC/2in1TabletTVWearable

getLastUpdate() : string

表示获取X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getLastUpdate](js-apis-cert.md#getlastupdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let lastUpdate = x509Crl.getLastUpdate();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getLastUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getNextUpdate(deprecated)

PhonePC/2in1TabletTVWearable

getNextUpdate() : string

表示获取证书吊销列表下一次更新的日期，日期为ASN.1时间格式。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getNextUpdate](js-apis-cert.md#getnextupdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表下一次更新的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let nextUpdate = x509Crl.getNextUpdate();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getNextUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getRevokedCert(deprecated)

PhonePC/2in1TabletTVWearable

getRevokedCert(serialNumber : number) : X509CrlEntry

表示通过指定证书序列号获取被吊销X509证书对象。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCert](js-apis-cert.md#getrevokedcert11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 表示证书序列号。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [X509CrlEntry](js-apis-cert.md#x509crlentrydeprecated) | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. let serialNumber = 1000;
35. try {
36. let entry = x509Crl.getRevokedCert(serialNumber);
37. } catch (error) {
38. let e: BusinessError = error as BusinessError;
39. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getRevokedCertWithCert(deprecated)

PhonePC/2in1TabletTVWearable

getRevokedCertWithCert(cert : X509Cert) : X509CrlEntry

表示通过指定证书对象获取被吊销X509证书对象。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCertWithCert](js-apis-cert.md#getrevokedcertwithcert11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 表示证书对象。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [X509CrlEntry](js-apis-cert.md#x509crlentrydeprecated) | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
15. 'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
16. 'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
17. 'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
18. 'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
19. 'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
20. 'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
21. 'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
22. '+i2osvdPWRia0dJCL1PCA14k\n' +
23. '-----END X509 CRL-----\n';

25. // 证书二进制数据，需业务自行赋值。
26. let certData = '-----BEGIN CERTIFICATE-----\n' +
27. 'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
28. 'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
29. 'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
30. 'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
31. 'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
32. 'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
33. 'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
34. '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
35. '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
36. 'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
37. 'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
38. 'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
39. 'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
40. '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
41. 'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
42. 'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
43. 'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
44. 'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
45. '-----END CERTIFICATE-----\n';

47. let certEncodingBlob: cert.EncodingBlob = {
48. data: stringToUint8Array(certData),
49. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
50. encodingFormat: cert.EncodingFormat.FORMAT_PEM
51. };

53. // 证书吊销列表二进制数据，需业务自行赋值。
54. let encodingBlob: cert.EncodingBlob = {
55. data: stringToUint8Array(crlData),
56. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
57. encodingFormat: cert.EncodingFormat.FORMAT_PEM
58. };

60. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
61. if (error) {
62. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
63. } else {
64. console.info('createX509Crl result: success.');
65. // 创建X509证书对象。
66. cert.createX509Cert(certEncodingBlob).then((x509Cert) => {
67. try {
68. let entry = x509Crl.getRevokedCertWithCert(x509Cert);
69. console.info('getRevokedCertWithCert result: success.');
70. } catch (error) {
71. let e: BusinessError = error as BusinessError;
72. console.error(`getRevokedCertWithCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
73. }
74. }).catch((error: BusinessError) => {
75. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
76. })
77. }
78. });
```

### getRevokedCerts(deprecated)

PhonePC/2in1TabletTVWearable

getRevokedCerts(callback : AsyncCallback<Array<X509CrlEntry>>) : void

表示获取被吊销X509证书列表。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCerts](js-apis-cert.md#getrevokedcerts11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[X509CrlEntry](js-apis-cert.md#x509crlentrydeprecated)>> | 是 | 回调函数，表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
29. if (error) {
30. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509Crl result: success.');
33. x509Crl.getRevokedCerts((error, array) => {
34. if (error) {
35. console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
36. } else {
37. console.info('getRevokedCerts result: success.');
38. }
39. });
40. }
41. });
```

### getRevokedCerts(deprecated)

PhonePC/2in1TabletTVWearable

getRevokedCerts() : Promise<Array<X509CrlEntry>>

表示获取被吊销X509证书列表。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCerts](js-apis-cert.md#getrevokedcerts11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509CrlEntry](js-apis-cert.md#x509crlentrydeprecated)>> | 表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob).then(x509Crl => {
30. console.info('createX509Crl result: success.');
31. x509Crl.getRevokedCerts().then(array => {
32. console.info('getRevokedCerts result: success.');
33. }).catch((error: BusinessError) => {
34. console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. });
36. }).catch((error: BusinessError) => {
37. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. });
```

### getTbsInfo(deprecated)

PhonePC/2in1TabletTVWearable

getTbsInfo() : DataBlob

表示获取证书吊销列表的tbsCertList信息。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getTBSInfo](js-apis-cert.md#gettbsinfo11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示证书吊销列表的tbsCertList信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let tbsInfo = x509Crl.getTbsInfo();
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`getTbsInfo failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignature(deprecated)

PhonePC/2in1TabletTVWearable

getSignature() : DataBlob

表示获取X509证书吊销列表的签名数据。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignature](js-apis-cert.md#getsignature11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表的签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let signature = x509Crl.getSignature();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgName(deprecated)

PhonePC/2in1TabletTVWearable

getSignatureAlgName() : string

表示获取X509证书吊销列表签名的算法名称。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgName](js-apis-cert.md#getsignaturealgname11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名的算法名。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let sigAlgName = x509Crl.getSignatureAlgName();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgOid(deprecated)

PhonePC/2in1TabletTVWearable

getSignatureAlgOid() : string

表示获取X509证书吊销列表签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgOid](js-apis-cert.md#getsignaturealgoid11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名算法的对象标志符OID。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let sigAlgOid = x509Crl.getSignatureAlgOid();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgParams(deprecated)

PhonePC/2in1TabletTVWearable

getSignatureAlgParams() : DataBlob

表示获取X509证书吊销列表签名的算法参数。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgParams](js-apis-cert.md#getsignaturealgparams11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表签名的算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509Crl(encodingBlob, (error, x509Crl) => {
30. if (error) {
31. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509Crl result: success.');
34. try {
35. let sigAlgParams = x509Crl.getSignatureAlgParams();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

## X509CRL11+

PhonePC/2in1TabletTVWearable

被吊销证书列表对象。

### isRevoked11+

PhonePC/2in1TabletTVWearable

isRevoked(cert : X509Cert) : boolean

表示检查证书是否吊销。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 表示被检查的证书对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示证书吊销状态，true表示已吊销，false表示未吊销。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. let certData = '-----BEGIN CERTIFICATE-----\n' +
23. 'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
24. 'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
25. 'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
26. 'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
27. 'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
28. '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
29. 'BetUokslUfjT6+s/X4ByaxycAA==\n' +
30. '-----END CERTIFICATE-----\n';

32. // 证书吊销列表二进制数据，需业务自行赋值。
33. let encodingBlob: cert.EncodingBlob = {
34. data: stringToUint8Array(crlData),
35. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
36. encodingFormat: cert.EncodingFormat.FORMAT_PEM
37. };

39. let certEncodingBlob: cert.EncodingBlob = {
40. data: stringToUint8Array(certData),
41. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
42. encodingFormat: cert.EncodingFormat.FORMAT_PEM
43. };

45. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
46. if (error) {
47. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
48. } else {
49. console.info('createX509CRL result: success.');
50. // Create an X509Cert instance.
51. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
52. if (error) {
53. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
54. } else {
55. try {
56. let revokedFlag = x509CRL.isRevoked(x509Cert);
57. } catch (error) {
58. let e: BusinessError = error as BusinessError;
59. console.error(`isRevoked failed, errCode: ${e.code}, errMsg: ${e.message}`);
60. }
61. }
62. });
63. }
64. });
```

### getType11+

PhonePC/2in1TabletTVWearable

getType() : string

表示获取证书吊销列表类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书吊销列表类型。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
29. if (error) {
30. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509CRL result: success.');
33. let type = x509CRL.getType();
34. }
35. });
```

### getEncoded11+

PhonePC/2in1TabletTVWearable

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书吊销列表的序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EncodingBlob](js-apis-cert.md#encodingblob)> | 是 | 回调函数，表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
29. if (error) {
30. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509CRL result: success.');
33. x509CRL.getEncoded((error, data) => {
34. if (error) {
35. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
36. } else {
37. console.info('getEncoded result: success.');
38. }
39. });
40. }
41. });
```

### getEncoded11+

PhonePC/2in1TabletTVWearable

getEncoded() : Promise<EncodingBlob>

表示获取X509证书吊销列表的序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EncodingBlob](js-apis-cert.md#encodingblob)> | 表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob).then(x509CRL => {
30. console.info('createX509CRL result: success.');
31. x509CRL.getEncoded().then(result => {
32. console.info('getEncoded result: success.');
33. }).catch((error: BusinessError) => {
34. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. });
36. }).catch((error: BusinessError) => {
37. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. });
```

### verify11+

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对X509证书吊销列表进行验签。使用callback异步回调。验签支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 表示用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数,使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. let pubKeyData = new Uint8Array([
24. 0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
25. 0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
26. 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
27. 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
28. 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
29. 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
30. 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
31. 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
32. 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
33. 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
34. 0x00, 0x01
35. ]);

37. let priKeyData = new Uint8Array([
38. 0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
39. 0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
40. 0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
41. 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
42. 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
43. 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
44. 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
45. 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
46. 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
47. 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
48. 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
49. 0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
50. 0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
51. 0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
52. 0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
53. 0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
54. 0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
55. 0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
56. 0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
57. 0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
58. 0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
59. 0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
60. 0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
61. 0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
62. 0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
63. 0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
64. 0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
65. 0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
66. 0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
67. 0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
68. 0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
69. 0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
70. 0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
71. 0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
72. 0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
73. 0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
74. 0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
75. 0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
76. 0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
77. 0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
78. ]);

80. // 证书吊销列表二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(crlData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
88. if (error) {
89. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
90. } else {
91. console.info('createX509Crl result: success.');
92. try {
93. let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
94. console.info('createAsyKeyGenerator result: success.');
95. let priEncodingBlob: cryptoFramework.DataBlob = {
96. data: priKeyData,
97. };
98. let pubEncodingBlob: cryptoFramework.DataBlob = {
99. data: pubKeyData,
100. };
101. keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob, (e, keyPair) => {
102. if (e) {
103. console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
104. } else {
105. console.info('convert key result: success.');
106. x509CRL.verify(keyPair.pubKey, (err, data) => {
107. if (err) {
108. console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
109. } else {
110. console.info('verify result: success.');
111. }
112. });
113. }
114. })
115. } catch (error) {
116. let e: BusinessError = error as BusinessError;
117. console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
118. }
119. }
120. });
```

### verify11+

PhonePC/2in1TabletTVWearable

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对X509证书吊销列表进行验签。使用Promise异步回调。验签支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [cryptoFramework.PubKey](js-apis-cryptoframework.md#pubkey) | 是 | 表示用于验签的公钥对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit'
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. let arr: Array<number> = [];
8. for (let i = 0, j = str.length; i < j; i++) {
9. arr.push(str.charCodeAt(i));
10. }
11. return new Uint8Array(arr);
12. }

14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. let pubKeyData = new Uint8Array([
24. 0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
25. 0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
26. 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
27. 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
28. 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
29. 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
30. 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
31. 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
32. 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
33. 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
34. 0x00, 0x01
35. ]);

37. let priKeyData = new Uint8Array([
38. 0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
39. 0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
40. 0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
41. 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
42. 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
43. 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
44. 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
45. 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
46. 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
47. 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
48. 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
49. 0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
50. 0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
51. 0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
52. 0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
53. 0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
54. 0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
55. 0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
56. 0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
57. 0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
58. 0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
59. 0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
60. 0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
61. 0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
62. 0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
63. 0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
64. 0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
65. 0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
66. 0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
67. 0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
68. 0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
69. 0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
70. 0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
71. 0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
72. 0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
73. 0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
74. 0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
75. 0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
76. 0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
77. 0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
78. ]);

80. // 证书吊销列表二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(crlData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. cert.createX509CRL(encodingBlob).then(x509CRL => {
88. console.info('createX509Crl result: success.');

90. try {
91. // 生成公钥对象。
92. let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
93. console.info('createAsyKeyGenerator result: success.');
94. let priEncodingBlob: cryptoFramework.DataBlob = {
95. data: priKeyData,
96. };
97. let pubEncodingBlob: cryptoFramework.DataBlob = {
98. data: pubKeyData,
99. };
100. keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob).then((keyPair) => {
101. console.info('convert key result: success.');
102. x509CRL.verify(keyPair.pubKey).then(result => {
103. console.info('verify result: success.');
104. }).catch((error: BusinessError) => {
105. console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
106. });
107. }).catch((error: BusinessError) => {
108. console.error(`convert key failed, errCode: ${error.code}, errMsg: ${error.message}`);
109. });
110. } catch (error) {
111. let e: BusinessError = error as BusinessError;
112. console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
113. }
114. }).catch((error: BusinessError) => {
115. console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
116. });
```

### getVersion11+

PhonePC/2in1TabletTVWearable

getVersion() : number

表示获取X509证书吊销列表的版本号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示获取X509证书吊销列表的版本号。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
29. if (error) {
30. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509CRL result: success.');
33. let version = x509CRL.getVersion();
34. }
35. });
```

### getIssuerName11+

PhonePC/2in1TabletTVWearable

getIssuerName() : DataBlob

表示获取X509证书吊销列表颁发者名称。

说明

获取到的X509证书吊销列表颁发者名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let issuerName = x509CRL.getIssuerName();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getIssuerName20+

PhonePC/2in1TabletTVWearable

getIssuerName(encodingType: EncodingType): string

根据编码类型获取X509证书吊销列表颁发者名称。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表颁发者名称，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIByzCBtAIBATANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
15. 'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMG\n' +
16. 'A1UEAwwM5Lit5paH5rWL6K+VFw0yNDEwMTYwODUwMDlaFw0yNDExMTUwODUwMDla\n' +
17. 'MBkwFwIGAXKnJjrAFw0yNDEwMTYwODQ5NDBaoA4wDDAKBgNVHRQEAwIBADANBgkq\n' +
18. 'hkiG9w0BAQsFAAOCAQEAU0JPK/DnGmjCi5lKyun506JE+FVDuQsEWuF5CZPqE2um\n' +
19. 'hA04Qffi+8AfwLpG2KPBaAYTteU4fx30y8Wm0kLutalk32FgrbQX0VQ7EaCOmkMU\n' +
20. '2dnQMmFmaFiVcOTaRzgqDOYKuzSAptCo6hqtk9kgjbda5HnsNiVC7dNMRp1Jlzwr\n' +
21. 'k/42mqZ3fFIy3wYLaxRlq368BX3u94J9Cx754V2V/XEApiRI/FsiSRzRX+jfUBa4\n' +
22. '+wwu3WhWxisQj6z3bBkQD4RTg3S+ic8hhP44wt/1MmSLG946Dc9uVYJKUVZqTco9\n' +
23. 'QDoDwYfBJBzcXjManSkPsGCb7RfTAr5HqcEtIHsK+w==\n' +
24. '-----END X509 CRL-----\n';
25. // 证书吊销列表二进制数据，需业务自行赋值。
26. let encodingBlob: cert.EncodingBlob = {
27. data: stringToUint8Array(crlData),
28. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
29. encodingFormat: cert.EncodingFormat.FORMAT_PEM
30. };

32. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
33. if (error) {
34. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. } else {
36. console.info('createX509CRL result: success.');
37. try {
38. let issuerName = x509CRL.getIssuerName(cert.EncodingType.ENCODING_UTF8);
39. console.info('issuerName output = ' + issuerName);
40. } catch (err) {
41. let e: BusinessError = err as BusinessError;
42. console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
43. }
44. }
45. });
```

### getLastUpdate11+

PhonePC/2in1TabletTVWearable

getLastUpdate() : string

表示获取X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let lastUpdate  = x509CRL.getLastUpdate();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getLastUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getNextUpdate11+

PhonePC/2in1TabletTVWearable

getNextUpdate() : string

表示获取证书吊销列表下一次更新的日期，日期为ASN.1时间格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表下一次更新的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let nextUpdate = x509CRL.getNextUpdate();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getNextUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getRevokedCert11+

PhonePC/2in1TabletTVWearable

getRevokedCert(serialNumber : bigint) : X509CRLEntry

表示通过指定证书序列号获取被吊销X509证书对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | bigint | 是 | 表示证书序列号。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [X509CRLEntry](js-apis-cert.md#x509crlentry11) | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. let serialNumber = BigInt(1000);
35. try {
36. let entry = x509CRL.getRevokedCert(serialNumber);
37. } catch (error) {
38. let e: BusinessError = error as BusinessError;
39. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
40. }
41. }
42. });
```

### getRevokedCertWithCert11+

PhonePC/2in1TabletTVWearable

getRevokedCertWithCert(cert : X509Cert) : X509CRLEntry

表示通过指定证书对象获取被吊销X509证书对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 表示证书对象。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [X509CRLEntry](js-apis-cert.md#x509crlentry11) | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
15. 'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
16. 'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
17. 'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
18. 'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
19. 'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
20. 'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
21. 'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
22. '+i2osvdPWRia0dJCL1PCA14k\n' +
23. '-----END X509 CRL-----\n';

25. // 证书二进制数据，需业务自行赋值。
26. let certData = '-----BEGIN CERTIFICATE-----\n' +
27. 'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
28. 'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
29. 'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
30. 'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
31. 'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
32. 'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
33. 'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
34. '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
35. '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
36. 'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
37. 'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
38. 'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
39. 'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
40. '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
41. 'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
42. 'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
43. 'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
44. 'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
45. '-----END CERTIFICATE-----\n';

47. let certEncodingBlob: cert.EncodingBlob = {
48. data: stringToUint8Array(certData),
49. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
50. encodingFormat: cert.EncodingFormat.FORMAT_PEM
51. };

53. // 证书吊销列表二进制数据，需业务自行赋值。
54. let encodingBlob: cert.EncodingBlob = {
55. data: stringToUint8Array(crlData),
56. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
57. encodingFormat: cert.EncodingFormat.FORMAT_PEM
58. };

60. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
61. if (error) {
62. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
63. } else {
64. console.info('createX509CRL result: success.');
65. // 创建X509证书对象。
66. cert.createX509Cert(certEncodingBlob).then((x509Cert) => {
67. try {
68. let entry = x509CRL.getRevokedCertWithCert(x509Cert);
69. console.info('getRevokedCertWithCert result: success.');
70. } catch (error) {
71. let e: BusinessError = error as BusinessError;
72. console.error(`getRevokedCertWithCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
73. }
74. }).catch((error: BusinessError) => {
75. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
76. })
77. }
78. });
```

### getRevokedCerts11+

PhonePC/2in1TabletTVWearable

getRevokedCerts(callback : AsyncCallback<Array<X509CRLEntry>>) : void

表示获取被吊销X509证书列表。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[X509CRLEntry](js-apis-cert.md#x509crlentry11)>> | 是 | 回调函数，表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let crlData = '-----BEGIN X509 CRL-----\n' +
13. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
14. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
15. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
16. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
17. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
18. 'eavsH0Q3\n' +
19. '-----END X509 CRL-----\n';

21. // 证书吊销列表二进制数据，需业务自行赋值。
22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
29. if (error) {
30. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
31. } else {
32. console.info('createX509CRL result: success.');
33. x509CRL.getRevokedCerts((error, array) => {
34. if (error) {
35. console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
36. } else {
37. console.info('getRevokedCerts result: success.');
38. }
39. });
40. }
41. });
```

### getRevokedCerts11+

PhonePC/2in1TabletTVWearable

getRevokedCerts() : Promise<Array<X509CRLEntry>>

表示获取被吊销X509证书列表。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509CRLEntry](js-apis-cert.md#x509crlentry11)>> | 表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob).then(x509CRL => {
30. console.info('createX509CRL result: success.');
31. x509CRL.getRevokedCerts().then(array => {
32. console.info('getRevokedCerts result: success.');
33. }).catch((error: BusinessError) => {
34. console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. });
36. }).catch((error: BusinessError) => {
37. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. });
```

### getSignature11+

PhonePC/2in1TabletTVWearable

getSignature() : DataBlob

表示获取X509证书吊销列表的签名数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表的签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let signature = x509CRL.getSignature();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgName11+

PhonePC/2in1TabletTVWearable

getSignatureAlgName() : string

表示获取X509证书吊销列表签名的算法名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名的算法名。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let sigAlgName = x509CRL.getSignatureAlgName();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgOid11+

PhonePC/2in1TabletTVWearable

getSignatureAlgOid() : string

表示获取X509证书吊销列表签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名算法的对象标志符OID。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let sigAlgOid = x509CRL.getSignatureAlgOid();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getSignatureAlgParams11+

PhonePC/2in1TabletTVWearable

getSignatureAlgParams() : DataBlob

表示获取X509证书吊销列表签名的算法参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509证书吊销列表签名的算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let sigAlgParams = x509CRL.getSignatureAlgParams();
36. } catch (err) {
37. let e: BusinessError = err as BusinessError;
38. console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getTBSInfo11+

PhonePC/2in1TabletTVWearable

getTBSInfo() : DataBlob

表示获取证书吊销列表的tbsCertList信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示证书吊销列表的tbsCertList信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
30. if (error) {
31. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
32. } else {
33. console.info('createX509CRL result: success.');
34. try {
35. let tbsInfo = x509CRL.getTBSInfo();
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`getTBSInfo failed, errCode: ${e.code}, errMsg: ${e.message}`);
39. }
40. }
41. });
```

### getExtensions11+

PhonePC/2in1TabletTVWearable

getExtensions(): DataBlob

表示获取CRL的扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509CRL扩展用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
15. 'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
16. 'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
17. 'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
18. 'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
19. 'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
20. 'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
21. 'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
22. '+i2osvdPWRia0dJCL1PCA14k\n' +
23. '-----END X509 CRL-----\n';

25. // 证书吊销列表二进制数据，需业务自行赋值。
26. let encodingBlob: cert.EncodingBlob = {
27. data: stringToUint8Array(crlData),
28. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
29. encodingFormat: cert.EncodingFormat.FORMAT_PEM
30. };

32. cert.createX509CRL(encodingBlob, (error, x509CRL) => {
33. if (error) {
34. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
35. } else {
36. console.info('createX509CRL result: success.');
37. try {
38. let extensions = x509CRL.getExtensions();
39. } catch (error) {
40. let e: BusinessError = error as BusinessError;
41. console.error(`getExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
42. }
43. }
44. });
```

### match11+

PhonePC/2in1TabletTVWearable

match(param: X509CRLMatchParameters): boolean

判断证书吊销列表是否与输入参数匹配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CRLMatchParameters](js-apis-cert.md#x509crlmatchparameters11) | 是 | 表示需要匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当参数匹配时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let crlEncodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. const certData = '-----BEGIN CERTIFICATE-----\r\n' +
30. 'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
31. 'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
32. 'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
33. 'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
34. 'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
35. 'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
36. 'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
37. 'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
38. 'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
39. 'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
40. 'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
41. 'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
42. 'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
43. 'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
44. 'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
45. 'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
46. '-----END CERTIFICATE-----\r\n';
47. const certEncodingBlob: cert.EncodingBlob = {
48. data: stringToUint8Array(certData),
49. encodingFormat: cert.EncodingFormat.FORMAT_PEM,
50. };

52. async function crlMatch() {
53. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
54. try {
55. x509Cert = await cert.createX509Cert(certEncodingBlob);
56. console.info('createX509Cert result: success.');
57. } catch (error) {
58. let e: BusinessError = error as BusinessError;
59. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
60. }

62. cert.createX509CRL(crlEncodingBlob, (error, x509CRL) => {
63. if (error) {
64. console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
65. } else {
66. console.info('createX509CRL result: success.');
67. try {
68. const param: cert.X509CRLMatchParameters = {
69. issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43,
70. 0x4E, 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73,
71. 0x75, 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E,
72. 0x67, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09,
73. 0x06, 0x03, 0x55, 0x04, 0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03,
74. 0x13, 0x02, 0x74, 0x73])],
75. x509Cert: x509Cert
76. }
77. const result = x509CRL.match(param);
78. } catch (error) {
79. let e: BusinessError = error as BusinessError;
80. console.error(`x509CRL match failed, errCode: ${e.code}, errMsg: ${e.message}`);
81. }
82. }
83. });
84. }
```

### getIssuerX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

getIssuerX500DistinguishedName(): X500DistinguishedName

获取颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [X500DistinguishedName](js-apis-cert.md#x500distinguishedname12) | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let crlEncodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. async function crlGetIssuerX500DistinguishedName() {
30. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
31. try {
32. x509Crl = await cert.createX509CRL(crlEncodingBlob);
33. console.info('createX509CRL result: success.');
34. let name = x509Crl.getIssuerX500DistinguishedName();
35. } catch (err) {
36. let e: BusinessError = err as BusinessError;
37. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
38. }
39. }
```

### toString12+

PhonePC/2in1TabletTVWearable

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let crlEncodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. async function crlToString() {
30. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
31. try {
32. x509Crl = await cert.createX509CRL(crlEncodingBlob);
33. console.info('createX509CRL result: success.');
34. console.info('crlToString success: ' + x509Crl.toString());
35. } catch (err) {
36. let e: BusinessError = err as BusinessError;
37. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
38. }
39. }
```

### toString20+

PhonePC/2in1TabletTVWearable

toString(encodingType: EncodingType): string

根据编码类型获取对象的字符串类型数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIByzCBtAIBATANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
15. 'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMG\n' +
16. 'A1UEAwwM5Lit5paH5rWL6K+VFw0yNDEwMTYwODUwMDlaFw0yNDExMTUwODUwMDla\n' +
17. 'MBkwFwIGAXKnJjrAFw0yNDEwMTYwODQ5NDBaoA4wDDAKBgNVHRQEAwIBADANBgkq\n' +
18. 'hkiG9w0BAQsFAAOCAQEAU0JPK/DnGmjCi5lKyun506JE+FVDuQsEWuF5CZPqE2um\n' +
19. 'hA04Qffi+8AfwLpG2KPBaAYTteU4fx30y8Wm0kLutalk32FgrbQX0VQ7EaCOmkMU\n' +
20. '2dnQMmFmaFiVcOTaRzgqDOYKuzSAptCo6hqtk9kgjbda5HnsNiVC7dNMRp1Jlzwr\n' +
21. 'k/42mqZ3fFIy3wYLaxRlq368BX3u94J9Cx754V2V/XEApiRI/FsiSRzRX+jfUBa4\n' +
22. '+wwu3WhWxisQj6z3bBkQD4RTg3S+ic8hhP44wt/1MmSLG946Dc9uVYJKUVZqTco9\n' +
23. 'QDoDwYfBJBzcXjManSkPsGCb7RfTAr5HqcEtIHsK+w==\n' +
24. '-----END X509 CRL-----\n';
25. // 证书吊销列表二进制数据，需业务自行赋值。
26. let crlEncodingBlob: cert.EncodingBlob = {
27. data: stringToUint8Array(crlData),
28. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
29. encodingFormat: cert.EncodingFormat.FORMAT_PEM
30. };

32. async function crlToString() {
33. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
34. try {
35. x509Crl = await cert.createX509CRL(crlEncodingBlob);
36. console.info('createX509CRL result: success.');
37. console.info('crlToString success: ' + x509Crl.toString(cert.EncodingType.ENCODING_UTF8));
38. } catch (err) {
39. let e: BusinessError = err as BusinessError;
40. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
```

### hashCode12+

PhonePC/2in1TabletTVWearable

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n';

22. // 证书吊销列表二进制数据，需业务自行赋值。
23. let crlEncodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. async function crlHashCode() {
30. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
31. try {
32. x509Crl = await cert.createX509CRL(crlEncodingBlob);
33. console.info('createX509CRL result: success.');
34. console.info('crlHashCode success: ' + x509Crl.hashCode());
35. } catch (err) {
36. let e: BusinessError = err as BusinessError;
37. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
38. }
39. }
```

### getExtensionsObject12+

PhonePC/2in1TabletTVWearable

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CertExtension](js-apis-cert.md#certextension10) | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIB6DCB0QIBATANBgkqhkiG9w0BAQsFADCBjjELMAkGA1UEBhMCUlUxFTATBgNV\n' +
15. 'BAgMDNCc0L7RgdC60LLQsDELMAkGA1UECgwC0K8xCzAJBgNVBAsMAtCvMSowKAYD\n' +
16. 'VQQDDCHQlNC80LjRgtGA0LjQuSDQkdC10LvRj9Cy0YHQutC40LkxIjAgBgkqhkiG\n' +
17. '9w0BCQEWE2JlbGRtaXRAZXhhbXBsZS5jb20XDTE3MDQyNDEzMjUzMVoXDTE3MDUy\n' +
18. 'NDEzMjUzMVqgDjAMMAoGA1UdFAQDAgEBMA0GCSqGSIb3DQEBCwUAA4IBAQCF5eX+\n' +
19. '1BM/BxoHU2/3pQHJgPSKevN0/K/daiFHiJl7Kb9GCwKY14B1RvbN2rUP/58Mt+aq\n' +
20. 'jvauf1yBzlaJQeJKZcsCmG9p6Tr1y0BJXhrq5kC0SLyNDsfGUTfuxnwmo+clHXRU\n' +
21. '+gKuk+h0WkJL022ZYbJ38w588k4NT3CWVHeE23EDC264p942mlDE7en6MyL152Pe\n' +
22. 'Ld9YrWiq5iOIOrIbQLErq0EjwxvHG9sMiYFUa6VrwmRf26nyZ7u9RKJDP+o2dltw\n' +
23. 'diBaSXC3Qt3pZ8BIfv/l81lwp8Dr63SwCII2pIRplyICdQqmX/a+1q8kThXIP2Kx\n' +
24. '+X48g7VE2o2X4cfy\n' +
25. '-----END X509 CRL-----\n';

27. // 证书吊销列表二进制数据，需业务自行赋值。
28. let crlEncodingBlob: cert.EncodingBlob = {
29. data: stringToUint8Array(crlData),
30. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
31. encodingFormat: cert.EncodingFormat.FORMAT_PEM
32. };

34. async function crlHashCode() {
35. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
36. try {
37. x509Crl = await cert.createX509CRL(crlEncodingBlob);
38. console.info('createX509CRL result: success.');
39. let object = x509Crl.getExtensionsObject();
40. } catch (err) {
41. let e: BusinessError = err as BusinessError;
42. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
43. }
44. }
```

## cert.createCertChainValidator

PhonePC/2in1TabletTVWearable

createCertChainValidator(algorithm :string) : CertChainValidator

表示创建证书链校验器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | string | 是 | 表示证书链校验器算法。当前仅支持输入"PKIX"。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CertChainValidator](js-apis-cert.md#certchainvalidator) | 表示证书链校验器对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let validator = cert.createCertChainValidator('PKIX');
6. } catch (error) {
7. let e: BusinessError = error as BusinessError;
8. console.error(`createCertChainValidator failed, errCode: ${e.code}, errMsg: ${e.message}`);
9. }
```

## CertChainValidator

PhonePC/2in1TabletTVWearable

证书链校验器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algorithm | string | 是 | 否 | X509证书链校验器算法名称。 |

### validate

PhonePC/2in1TabletTVWearable

validate(certChain : CertChainData, callback : AsyncCallback<void>) : void

表示校验X509证书链。使用callback异步回调。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X509证书的[checkValidityWithDate](js-apis-cert.md#checkvaliditywithdate)方法进行检查。详见[证书规格](../harmonyos-guides/certificate-framework-overview.md#证书规格)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certChain | [CertChainData](js-apis-cert.md#certchaindata) | 是 | 表示X509证书链序列化数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数，使用AsyncCallback的第一个error参数判断是否校验成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书链二进制数据。
14. let certPem = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
16. 'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
17. 'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
18. 'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
19. 'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
20. 'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
21. 'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
22. '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
23. '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
24. 'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
25. 'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
26. 'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
27. 'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
28. '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
29. 'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
30. 'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
31. 'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
32. 'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
33. '-----END CERTIFICATE-----';

35. let caPem = '-----BEGIN CERTIFICATE-----\n' +
36. 'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
37. 'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
38. 'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
39. '6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
40. 'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
41. 'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
42. 'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
43. 'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
44. 'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
45. 'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
46. 'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
47. 'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
48. 'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
49. 'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
50. 'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
51. 'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
52. 'sSus\n' +
53. '-----END CERTIFICATE-----';

55. let certPemData = stringToUint8Array(certPem);
56. let caPemData = stringToUint8Array(caPem);

58. let certPemDataLenData = new Uint8Array(new Uint16Array([certPemData.length]).buffer)
59. let caPemDataLenData = new Uint8Array(new Uint16Array([caPemData.length]).buffer)

61. let certChainBuff =
62. new Uint8Array(certPemDataLenData.length + certPemData.length + caPemDataLenData.length + caPemData.length)
63. certChainBuff.set(certPemDataLenData)
64. certChainBuff.set(certPemData, certPemDataLenData.length)
65. certChainBuff.set(caPemDataLenData, certPemDataLenData.length + certPemData.length)
66. certChainBuff.set(caPemData, certPemDataLenData.length + certPemData.length + caPemDataLenData.length)

68. let certChainData: cert.CertChainData = {
69. data: certChainBuff,
70. // 证书链包含的证书个数，需业务自行赋值。
71. count: 2,
72. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };

76. try {
77. let validator = cert.createCertChainValidator('PKIX');
78. validator.validate(certChainData, (error, data) => {
79. if (error) {
80. console.error(`validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
81. } else {
82. console.info('validate result: success.');
83. }
84. });
85. } catch (error) {
86. let e: BusinessError = error as BusinessError;
87. console.error(`validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
88. }
```

### validate

PhonePC/2in1TabletTVWearable

validate(certChain : CertChainData) : Promise<void>

表示校验X509证书链。使用Promise异步回调。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X509证书的[checkValidityWithDate](js-apis-cert.md#checkvaliditywithdate)方法进行检查。详见[证书规格](../harmonyos-guides/certificate-framework-overview.md#证书规格)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certChain | [CertChainData](js-apis-cert.md#certchaindata) | 是 | 表示X509证书链序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书链数据。
14. let certPem = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
16. 'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
17. 'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
18. 'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
19. 'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
20. 'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
21. 'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
22. '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
23. '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
24. 'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
25. 'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
26. 'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
27. 'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
28. '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
29. 'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
30. 'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
31. 'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
32. 'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
33. '-----END CERTIFICATE-----';

35. let caPem = '-----BEGIN CERTIFICATE-----\n' +
36. 'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
37. 'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
38. 'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
39. '6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
40. 'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
41. 'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
42. 'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
43. 'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
44. 'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
45. 'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
46. 'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
47. 'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
48. 'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
49. 'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
50. 'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
51. 'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
52. 'sSus\n' +
53. '-----END CERTIFICATE-----';

55. let certPemData = stringToUint8Array(certPem);
56. let caPemData = stringToUint8Array(caPem);

58. let certPemDataLenData = new Uint8Array(new Uint16Array([certPemData.length]).buffer)
59. let caPemDataLenData = new Uint8Array(new Uint16Array([caPemData.length]).buffer)

61. let certChainBuff =
62. new Uint8Array(certPemDataLenData.length + certPemData.length + caPemDataLenData.length + caPemData.length)
63. certChainBuff.set(certPemDataLenData)
64. certChainBuff.set(certPemData, certPemDataLenData.length)
65. certChainBuff.set(caPemDataLenData, certPemDataLenData.length + certPemData.length)
66. certChainBuff.set(caPemData, certPemDataLenData.length + certPemData.length + caPemDataLenData.length)

68. let certChainData: cert.CertChainData = {
69. data: certChainBuff,
70. // 证书链包含的证书个数，需业务自行赋值。
71. count: 2,
72. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };

76. try {
77. let validator = cert.createCertChainValidator('PKIX');
78. validator.validate(certChainData).then(result => {
79. console.info('validate result: success.');
80. }).catch((error: BusinessError) => {
81. console.error(`validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
82. });
83. } catch (error) {
84. let e: BusinessError = error as BusinessError;
85. console.error(`validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
86. }
```

## X509CrlEntry(deprecated)

PhonePC/2in1TabletTVWearable

被吊销证书对象。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry](js-apis-cert.md#x509crlentry11)替代。

### getEncoded(deprecated)

PhonePC/2in1TabletTVWearable

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取被吊销证书的序列化数据。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getEncoded](js-apis-cert.md#getencoded11-2)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EncodingBlob](js-apis-cert.md#encodingblob)> | 是 | 回调函数，表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (err, x509Crl) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 crl result: success.');

34. try {
35. let serialNumber = 1000;
36. let crlEntry = x509Crl.getRevokedCert(serialNumber);
37. crlEntry.getEncoded((error, data) => {
38. if (error) {
39. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
40. } else {
41. console.info('getEncoded result: success.');
42. }
43. });
44. } catch (error) {
45. let e: BusinessError = error as BusinessError;
46. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
47. }
48. }
49. })
```

### getEncoded(deprecated)

PhonePC/2in1TabletTVWearable

getEncoded() : Promise<EncodingBlob>

表示获取被吊销证书的序列化数据。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getEncoded](js-apis-cert.md#getencoded11-3)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EncodingBlob](js-apis-cert.md#encodingblob)> | 表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (err, x509Crl) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 crl result: success.');

34. try {
35. let serialNumber = 1000;
36. let crlEntry = x509Crl.getRevokedCert(serialNumber);
37. crlEntry.getEncoded().then(result => {
38. console.info('getEncoded result: success.');
39. }).catch((error: BusinessError) => {
40. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
41. });
42. } catch (error) {
43. let e: BusinessError = error as BusinessError;
44. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
45. }
46. }
47. })
```

### getSerialNumber(deprecated)

PhonePC/2in1TabletTVWearable

getSerialNumber() : number

表示获取被吊销证书的序列号。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getSerialNumber](js-apis-cert.md#getserialnumber11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示被吊销证书的序列号。 |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (err, x509Crl) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 crl result: success.');

34. try {
35. let serialNumber = 1000;
36. let crlEntry = x509Crl.getRevokedCert(serialNumber);
37. serialNumber = crlEntry.getSerialNumber();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getCertIssuer(deprecated)

PhonePC/2in1TabletTVWearable

getCertIssuer() : DataBlob

表示获取被吊销证书的颁发者信息。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getCertIssuer](js-apis-cert.md#getcertissuer11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示被吊销证书的颁发者信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (err, x509Crl) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 crl result: success.');

34. try {
35. let serialNumber = 1000;
36. let crlEntry = x509Crl.getRevokedCert(serialNumber);
37. let issuer = crlEntry.getCertIssuer();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getRevocationDate(deprecated)

PhonePC/2in1TabletTVWearable

getRevocationDate() : string

表示获取证书被吊销的日期，日期为ASN.1时间格式。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getRevocationDate](js-apis-cert.md#getrevocationdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书被吊销的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509Crl(encodingBlob, (err, x509Crl) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 crl result: success.');

34. try {
35. let serialNumber = 1000;
36. let crlEntry = x509Crl.getRevokedCert(serialNumber);
37. let date = crlEntry.getRevocationDate();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getRevocationDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

## X509CRLEntry11+

PhonePC/2in1TabletTVWearable

被吊销证书对象。

### getEncoded11+

PhonePC/2in1TabletTVWearable

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取被吊销证书的序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EncodingBlob](js-apis-cert.md#encodingblob)> | 是 | 回调函数，表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. crlEntry.getEncoded((error, data) => {
38. if (error) {
39. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
40. } else {
41. console.info('getEncoded result: success.');
42. }
43. });
44. } catch (error) {
45. let e: BusinessError = error as BusinessError;
46. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
47. }
48. }
49. })
```

### getEncoded11+

PhonePC/2in1TabletTVWearable

getEncoded() : Promise<EncodingBlob>

表示获取被吊销证书的序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EncodingBlob](js-apis-cert.md#encodingblob)> | 表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('create x509 CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. crlEntry.getEncoded().then(result => {
38. console.info('getEncoded result: success.');
39. }).catch((error: BusinessError) => {
40. console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
41. });
42. } catch (error) {
43. let e: BusinessError = error as BusinessError;
44. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
45. }
46. }
47. })
```

### getSerialNumber11+

PhonePC/2in1TabletTVWearable

getSerialNumber() : bigint

表示获取被吊销证书的序列号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| bigint | 表示被吊销证书的序列号。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('createX509CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. serialNumber = crlEntry.getSerialNumber();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getCertIssuer11+

PhonePC/2in1TabletTVWearable

getCertIssuer() : DataBlob

表示获取被吊销证书的颁发者信息。

说明

获取到的被吊销证书的颁发者信息数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示被吊销证书的颁发者信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('createX509CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. let issuer = crlEntry.getCertIssuer();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getCertIssuer20+

PhonePC/2in1TabletTVWearable

getCertIssuer(encodingType: EncodingType): string

根据编码类型获取被吊销证书的颁发者信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示被吊销证书的颁发者信息，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIBTDCBtgIBATANBgkqhkiG9w0BAQsFADBZMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
15. 'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEXMBUG\n' +
16. 'A1UEAwwO5Lit5paH5rWL6K+VIyMXDTI1MDMyNDA5MTExNVoXDTI1MDQyMzA5MTEx\n' +
17. 'NVowGTAXAgYBcqcmOsAXDTI1MDIyMDA2MTMwM1qgDjAMMAoGA1UdFAQDAgECMA0G\n' +
18. 'CSqGSIb3DQEBCwUAA4GBACedFnn4unfYLiRCl1ZAFXx6LFdX6U+IZ/buW44xKAWi\n' +
19. 'fyvcSxKIeGtMVjmQSs4HeNfNujIjaDN1+/J2nLSmHPiQ/c0LAc47zefVt2VnFuR4\n' +
20. 'TMUJEDUlnekYfDMxQqtihAO/Bpw33twK6otDvaAPm9vJoCu8JmGXxt6g+8vbYuNT\n' +
21. '-----END X509 CRL-----\n';

23. let encodingBlob: cert.EncodingBlob = {
24. data: stringToUint8Array(crlData),
25. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
26. encodingFormat: cert.EncodingFormat.FORMAT_PEM
27. };

29. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
30. if (err) {
31. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
32. } else {
33. console.info('createX509CRL result: success.');

35. try {
36. let serialNumber = BigInt(1591942200000);
37. let crlEntry = x509CRL.getRevokedCert(serialNumber);
38. let issuer = crlEntry.getCertIssuer(cert.EncodingType.ENCODING_UTF8);
39. console.info('issuer output = ' + issuer);
40. } catch (error) {
41. let e: BusinessError = error as BusinessError;
42. console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
43. }
44. }
45. })
```

### getRevocationDate11+

PhonePC/2in1TabletTVWearable

getRevocationDate() : string

表示获取证书被吊销的日期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书被吊销的日期。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('createX509CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. let date = crlEntry.getRevocationDate();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or getRevocationDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getExtensions11+

PhonePC/2in1TabletTVWearable

getExtensions(): DataBlob

表示获取CRL的扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DataBlob](js-apis-cert.md#datablob) | 表示X509CRLEntry扩展用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
15. 'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
16. 'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
17. 'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
18. 'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
19. 'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
20. 'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
21. 'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
22. '+i2osvdPWRia0dJCL1PCA14k\n' +
23. '-----END X509 CRL-----\n';

25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(crlData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };

31. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
32. if (err) {
33. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
34. } else {
35. console.info('createX509CRL result: success.');

37. try {
38. let serialNumber = BigInt(4);
39. let crlEntry = x509CRL.getRevokedCert(serialNumber);
40. let extensions = crlEntry.getExtensions();
41. } catch (error) {
42. let e: BusinessError = error as BusinessError;
43. console.error(`getRevokedCert or getExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
44. }
45. }
46. })
```

### hasExtensions11+

PhonePC/2in1TabletTVWearable

hasExtensions(): boolean

表示判断CRL Entry是否有扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true则表示CRL Entry有扩展，返回false则表示无扩展。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. cert.createX509CRL(encodingBlob, (err, x509CRL) => {
29. if (err) {
30. console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
31. } else {
32. console.info('createX509CRL result: success.');

34. try {
35. let serialNumber = BigInt(1000);
36. let crlEntry = x509CRL.getRevokedCert(serialNumber);
37. let hasExtensions = crlEntry.hasExtensions();
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`getRevokedCert or hasExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
41. }
42. }
43. })
```

### getCertIssuerX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

getCertIssuerX500DistinguishedName(): X500DistinguishedName

获取证书颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [X500DistinguishedName](js-apis-cert.md#x500distinguishedname12) | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. async function certGetCertIssuerX500DistinguishedName() {
29. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509Crl = await cert.createX509CRL(encodingBlob);
32. console.info('createX509CRL result: success.');
33. let name = x509Crl.getRevokedCert(BigInt(1000)).getCertIssuerX500DistinguishedName();
34. } catch (error) {
35. let e: BusinessError = error as BusinessError;
36. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
37. }
38. }
```

### toString12+

PhonePC/2in1TabletTVWearable

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. async function certToString() {
29. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509Crl = await cert.createX509CRL(encodingBlob);
32. console.info('createX509CRL result: success.');
33. console.info('toString success: ' + x509Crl.getRevokedCert(BigInt(1000)).toString());
34. } catch (error) {
35. let e: BusinessError = error as BusinessError;
36. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
37. }
38. }
```

### hashCode12+

PhonePC/2in1TabletTVWearable

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
15. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
16. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
17. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
18. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
19. 'eavsH0Q3\n' +
20. '-----END X509 CRL-----\n'

22. let encodingBlob: cert.EncodingBlob = {
23. data: stringToUint8Array(crlData),
24. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
25. encodingFormat: cert.EncodingFormat.FORMAT_PEM
26. };

28. async function certHashCode() {
29. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509Crl = await cert.createX509CRL(encodingBlob);
32. console.info('createX509CRL result: success.');
33. console.info('hashCode success: ' + x509Crl.getRevokedCert(BigInt(1000)).hashCode());
34. } catch (error) {
35. let e: BusinessError = error as BusinessError;
36. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
37. }
38. }
```

### getExtensionsObject12+

PhonePC/2in1TabletTVWearable

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CertExtension](js-apis-cert.md#certextension10) | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let crlData = '-----BEGIN X509 CRL-----\n' +
14. 'MIINlTCCDH0CAQEwDQYJKoZIhvcNAQELBQAwTDELMAkGA1UEBhMCVVMxFTATBgNV\n' +
15. 'BAoTDERpZ2lDZXJ0IEluYzEmMCQGA1UEAxMdRGlnaUNlcnQgU2VjdXJlIFNpdGUg\n' +
16. 'Q04gQ0EgRzMXDTI0MDMxMjE4NDQ0NVoXDTI0MDMxOTE4NDQ0NVowggvJMCECEAbk\n' +
17. 'wC/+N2YXfpw7vgDJ2xAXDTIzMDIwNzA1NTg1OFowIQIQDonqcHww7uhlmWH+OfIe\n' +
18. 'PhcNMjMwMzA5MDcwMzI1WjAvAhAM4CTrULrJUEinWgT9AFPvFw0yMzAzMjAxOTE4\n' +
19. 'NTRaMAwwCgYDVR0VBAMKAQQwIQIQBQP4xflKkcRehoJ2NaA/jhcNMjMwMzIyMDk0\n' +
20. 'NTI5WjAvAhAOmgzoiIqznAaFec53PVPUFw0yMzAzMjcyMDI4MDNaMAwwCgYDVR0V\n' +
21. 'BAMKAQQwLwIQBaC2Z3D4dcQ/O7HnzFU9KBcNMjMwMzI5MTc1OTQ1WjAMMAoGA1Ud\n' +
22. 'FQQDCgEFMCECEAlz9Rg1b+9La4oFqsHUc4AXDTIzMDMzMTAyMzk0MVowIQIQD9yW\n' +
23. '92pX6BinUKVBVSSTmBcNMjMwNDExMDExNjI5WjAvAhAIIarHUWWee4V9W/Yzm86k\n' +
24. 'Fw0yMzA0MTQyMDE5MTJaMAwwCgYDVR0VBAMKAQQwIQIQC2OiM3VIJX2dEe8/pf8f\n' +
25. 'hRcNMjMwNDIxMDMzMDIyWjAhAhAP0ueyg5n/7b2Hotml7f42Fw0yMzA0MjYwMjU3\n' +
26. 'NDJaMCECEAqMu61nkOEmTOdMbUZTMrkXDTIzMDUxNzAxMzI0NVowLwIQDYv1rt0K\n' +
27. 'olvP+nQoi5LeLRcNMjMwNTIzMTc0MDE4WjAMMAoGA1UdFQQDCgEEMC8CEA8WMKlw\n' +
28. 'iCK36PruJvup5bUXDTIzMDUyMzE3NDA1M1owDDAKBgNVHRUEAwoBBDAvAhAJ5uwT\n' +
29. 'aqwgLzNVpxh4u9EPFw0yMzA1MjUxNzEwNTBaMAwwCgYDVR0VBAMKAQQwIQIQCg0k\n' +
30. '5UadwDH5xm14yxcgLRcNMjMwNjA3MDcyNDAwWjAhAhAEByUhbBR6/pZRFUH2PTxE\n' +
31. 'Fw0yMzA2MDgwMjIwMzBaMCECEATquAQcy3W1kUOkb4VoOvEXDTIzMDYyNjA5MDIw\n' +
32. 'NlowIQIQBrF5sueIjk1snKdO0ISOXhcNMjMwNjMwMDI0MDA0WjAhAhAJEG72WQtV\n' +
33. 'lTOYiA0xjVk5Fw0yMzA3MDUwMjEyMzdaMCECEAmXIuCMJv9gllYuKfCHm5EXDTIz\n' +
34. 'MDcwNTAyMTIzN1owIQIQAotQots0ngzRwACzrS9mCBcNMjMwNzA2MDU0NDU3WjAh\n' +
35. 'AhAG2hyGc9SfXrLc0Uk2J1BeFw0yMzA3MjQwMTUwNDBaMCECEAJhm5FSlVyTG9UK\n' +
36. 'zS+ecUgXDTIzMDcyNjA2NDQzM1owIQIQC4mlxBQuFxWC4pF7/P8BDxcNMjMwNzMx\n' +
37. 'MTAzMjU0WjAhAhADCEp333/avF3m6HZtBImOFw0yMzA3MzExMDMzNTBaMCECEAKd\n' +
38. 'P7fydlXUcS4v/YnZMMwXDTIzMDczMTEwMzQzOFowIQIQC+m5EUcRd1E0lEIPj17Z\n' +
39. 'rRcNMjMwODAxMDYwNDE4WjAvAhAF4QcgQQlWpAi4FVflzbKxFw0yMzA4MDMxNjIz\n' +
40. 'MTdaMAwwCgYDVR0VBAMKAQQwIQIQAn01GEZ50Y5ugIcEuGfF9BcNMjMwODA4MDE1\n' +
41. 'NzM1WjAhAhAFHj3FDKeP9q9CM924d8RIFw0yMzA4MDgwMTU5NDhaMC8CEAnkNPSD\n' +
42. 'U5yiMsV3fU06a6oXDTIzMDgwODE5MjIwMlowDDAKBgNVHRUEAwoBBDAvAhAETU4z\n' +
43. '13iMKiwQujsxJDRhFw0yMzA4MTAyMDU4NDdaMAwwCgYDVR0VBAMKAQQwIQIQB1oD\n' +
44. 'M2mOYuse7e/nTqx+8xcNMjMwOTA0MDUwOTU3WjAhAhALf3Bp63so6O+R5QbWPWu6\n' +
45. 'Fw0yMzEwMDkwNjE5NTVaMCECEAKFHdXcy/zBXRtMj3BVhO0XDTIzMTAwOTA2MTk1\n' +
46. 'N1owIQIQDNNmVHN4tMu1xth6IAe4ZhcNMjMxMDEyMDc0MjQ1WjAhAhACNNJA2oMM\n' +
47. 'pr+giIgczvHOFw0yMzEwMTYwNTEyMzdaMCECEAoQun7uSHhvy6GBoxG7XOkXDTIz\n' +
48. 'MTExNjA3MDAzN1owLwIQA1NsI22PLvohCvKwdtAJwBcNMjMxMjA2MTgyNzUzWjAM\n' +
49. 'MAoGA1UdFQQDCgEEMCECEAWagozDt4jfBzi+aDGFr88XDTIzMTIxMTA3MjM1OFow\n' +
50. 'IQIQD1g7NdEk7t05zg6yweYc5hcNMjMxMjExMDcyNTM3WjAhAhAMJnRjUQAzFQFH\n' +
51. 'kwIguRz2Fw0yMzEyMTEwNzI2NDJaMCECEAT0bVxyPKkeTV8JQuPxfcwXDTIzMTIx\n' +
52. 'MTA3MjcyNlowIQIQA/5BlE0Ushtw24Ol9L2sexcNMjMxMjExMDcyODA2WjAhAhAL\n' +
53. 'Ij6FAKVJDnKAwwt19+/RFw0yMzEyMTEwNzI5MDJaMCECEAmPyfX3FuOHgryS2i8c\n' +
54. 'SrUXDTIzMTIxMTA3Mjk0M1owIQIQC+uGa6tmPRPCB0jW+6WWUhcNMjMxMjExMDcz\n' +
55. 'MDIzWjAhAhAJCq59mFZj6SWLH/m18Fq2Fw0yMzEyMTEwNzMwNTJaMCECEAp0Po24\n' +
56. 'WHmdEMTVyp9AMssXDTIzMTIxMTA3MzEyNlowIQIQAcf+793qPEHipkAhjf7MghcN\n' +
57. 'MjMxMjExMDczMTQ5WjAhAhAElLuCARMBoDIH0Y2D1DpSFw0yMzEyMTEwNzMyMTla\n' +
58. 'MCECEAWlgWhTXqKOB61zA7Ao8vQXDTIzMTIxMTA3MzI0OFowIQIQAeZqfkFYc/6t\n' +
59. 'zO7j/FVYwBcNMjMxMjExMDczMzM1WjAhAhAHzftyRhskxV6opTfHb59OFw0yMzEy\n' +
60. 'MTEwNzM0MDNaMCECEASXrBHdRYUm9VIZ1wN4qAsXDTIzMTIxMTA3MzQyN1owIQIQ\n' +
61. 'BDFb/OY65CZ1sTdMPAc+IhcNMjMxMjExMDczNTEzWjAhAhAFg7mRyWvWXc+KT014\n' +
62. 'Ro5AFw0yMzEyMTEwNzM1NDhaMCECEA+wAstqfBUEkSvinYlWeOwXDTIzMTIxMTA3\n' +
63. 'MzYyNVowIQIQB3Z75ksHGnvGmuHbvwbheRcNMjMxMjExMDczNjU5WjAhAhALfrIn\n' +
64. 'OGRVeePivKkJ+d1xFw0yMzEyMTEwNzM4MDFaMCECEAnm5NfU36m+FXNlJiUsXpMX\n' +
65. 'DTIzMTIxMTA3MzgzNVowIQIQCrBoHo4X2md3Amteqh7h3RcNMjMxMjExMDczOTA3\n' +
66. 'WjAhAhAGxHlqrHu66ifOwTTMhHHFFw0yMzEyMTEwNzM5NDNaMCECEA2BDG1SI7Se\n' +
67. '2GAt+b9UnF8XDTIzMTIxMTA3NDAyNFowLwIQDZvl5jkmAwjTweDCtrXbLRcNMjMx\n' +
68. 'MjExMjA0NDQ3WjAMMAoGA1UdFQQDCgEEMCECEAzgcwGVpyXXZSmLLF4MExQXDTIz\n' +
69. 'MTIxOTE3MjczMlowIQIQARB9nVoMuE5GSFeb3U553hcNMjMxMjE5MTcyODA1WjAh\n' +
70. 'AhAD+JIH7lFcX9UNqTogrMcPFw0yMzEyMTkxNzI5MDZaMCECEAux1kd8ugXs4mI+\n' +
71. 'xMfXgpsXDTIzMTIxOTE3MjkyOFowIQIQCUO5VqAmbxA8Jdly97msLhcNMjMxMjE5\n' +
72. 'MTcyOTU0WjAhAhAFyzrU1JtsiPNPeWrfdvGvFw0yMzEyMTkxNzMwNDlaMCECEAwT\n' +
73. 'tMq5EsBTUhQwm6nWhnAXDTIzMTIyMDE3NDc1NlowIQIQBx3qL8rMclE9gxamaa14\n' +
74. 'xBcNMjMxMjIwMTc0ODM2WjAhAhAOnKUlrCaxs+lRqLrBmk2PFw0yNDAxMzAxOTMw\n' +
75. 'MTVaMCECEAtYs/5ZRsrMAxQVDA44eWYXDTI0MDIwNjA2MjYwMFowIQIQDjrMV1d3\n' +
76. '0NhxngX5rqqxjBcNMjQwMjIxMDc0ODEwWjAhAhAPGohz3+JyS6H4JzHCjLrXFw0y\n' +
77. 'NDAyMjgyMDQxMjZaMC8CEAqZ2QktAMprzZmtolbOXlgXDTI0MDIyOTE4MDYzMVow\n' +
78. 'DDAKBgNVHRUEAwoBBDAhAhAMAHgNfiburtKDp8OJuzRCFw0yNDAzMDQwNjA3MzJa\n' +
79. 'MCECEA/HgrXcSBqkb2JdfrFDAfgXDTI0MDMwNDA2MDczMlqgMDAuMB8GA1UdIwQY\n' +
80. 'MBaAFETZyEozjtNSjaeSlGEfmsilt+zLMAsGA1UdFAQEAgIFrDANBgkqhkiG9w0B\n' +
81. 'AQsFAAOCAQEAJ5rSr0Av5sH59J2LXW5hZ8SJTzDbR8ADdi/CCLolbUUnE0oaAZ+2\n' +
82. '9z0niAD5m8HQikNz8K+FKAsQatN/CAj4bzRMeF37hQCiZpqNtxP69JDGeWpGPiH2\n' +
83. 'K/YfpzL9iSbBOxFmosxUX8J/iX36mCUl+3OUHh+qSYeElboxeAmTCnY5Pl5Bq9is\n' +
84. 'gp0MmzNYCo7GEFrtS03p2msK25uRqQl6Qn0NZS0yGjdUG7RTZe4xua5drjEkB1o/\n' +
85. '15f+mtYj6DtWM1twi1q3VYVxhRSsk6XmmS0BViTEl+MT0BRAPwBSdlyt++1Pnnrd\n' +
86. 'BsQoO8O2EVpJ54fxKMCSDOkJf1hNCxi3eQ==\n' +
87. '-----END X509 CRL-----\n';

89. let encodingBlob: cert.EncodingBlob = {
90. data: stringToUint8Array(crlData),
91. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
92. encodingFormat: cert.EncodingFormat.FORMAT_PEM
93. };

95. async function certGetExtensionsObject() {
96. let x509Crl: cert.X509CRL = {} as cert.X509CRL;
97. try {
98. x509Crl = await cert.createX509CRL(encodingBlob);
99. console.info('createX509CRL result: success.');
100. let object = x509Crl.getRevokedCert(BigInt('14091103387070223745671018446433705560')).getExtensionsObject();
101. } catch (error) {
102. let e: BusinessError = error as BusinessError;
103. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
104. }
105. }
```

## cert.createCertCRLCollection11+

PhonePC/2in1TabletTVWearable

createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection

表示创建证书和证书吊销列表集合对象，并返回相应的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certs | Array<[X509Cert](js-apis-cert.md#x509cert)> | 是 | X509Cert数组。 |
| crls | Array<[X509CRL](js-apis-cert.md#x509crl11)> | 否 | X509CRL数组。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CertCRLCollection](js-apis-cert.md#certcrlcollection11) | 表示证书和证书吊销列表集合对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509CRL(): Promise<cert.X509CRL> {
14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. // 证书吊销列表二进制数据，需业务自行赋值。
24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(crlData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };
29. let x509CRL: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509CRL = await cert.createX509CRL(encodingBlob);
32. } catch (err) {
33. let e: BusinessError = err as BusinessError;
34. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
35. }
36. return x509CRL;
37. }

39. async function createX509Cert(): Promise<cert.X509Cert> {
40. let certData = '-----BEGIN CERTIFICATE-----\n' +
41. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
42. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
43. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
44. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
45. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
46. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
47. 'Qw==\n' +
48. '-----END CERTIFICATE-----\n';

50. let encodingBlob: cert.EncodingBlob = {
51. data: stringToUint8Array(certData),
52. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
53. encodingFormat: cert.EncodingFormat.FORMAT_PEM
54. };

56. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
57. try {
58. x509Cert = await cert.createX509Cert(encodingBlob);
59. } catch (err) {
60. let e: BusinessError = err as BusinessError;
61. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
62. }
63. return x509Cert;
64. }

66. async function createCollection() {
67. const x509Cert = await createX509Cert();
68. const x509CRL = await createX509CRL();
69. try {
70. const collection: cert.CertCRLCollection = cert.createCertCRLCollection([x509Cert], [x509CRL]);
71. console.info('createCertCRLCollection result: success.');
72. } catch (err) {
73. let e: BusinessError = err as BusinessError;
74. console.error(`createCertCRLCollection failed, errCode: ${e.code}, errMsg: ${e.message}`);
75. }
76. }
```

## CertCRLCollection11+

PhonePC/2in1TabletTVWearable

证书和证书吊销列表集合对象。

### selectCerts11+

PhonePC/2in1TabletTVWearable

selectCerts(param: X509CertMatchParameters): Promise<Array<X509Cert>>

查找证书和证书吊销列表集合中所有与参数匹配的证书对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CertMatchParameters](js-apis-cert.md#x509certmatchparameters11) | 是 | 表示证书需匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509Cert](js-apis-cert.md#x509cert)>> | Promise对象。表示匹配到的证书对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509Cert(): Promise<cert.X509Cert> {
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
31. try {
32. x509Cert = await cert.createX509Cert(encodingBlob);
33. } catch (err) {
34. let e: BusinessError = err as BusinessError;
35. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
36. }
37. return x509Cert;
38. }

40. async function selectCerts() {
41. const x509Cert = await createX509Cert();
42. const collection = cert.createCertCRLCollection([x509Cert]);

44. try {
45. const param: cert.X509CertMatchParameters = {
46. x509Cert,
47. validDate: '20231121074700Z',
48. issuer: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
49. subject: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
50. publicKeyAlgID: '1.2.840.10045.2.1'
51. };
52. const certs = await collection.selectCerts(param);
53. console.info('call selectCerts result: success.');
54. } catch (err) {
55. let e: BusinessError = err as BusinessError;
56. console.error(`call selectCerts failed, errCode: ${e.code}, errMsg: ${e.message}`);
57. }
58. }
```

### selectCerts11+

PhonePC/2in1TabletTVWearable

selectCerts(param: X509CertMatchParameters, callback: AsyncCallback<Array<X509Cert>>): void

查找证书和证书吊销列表集合中所有与参数匹配的证书对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CertMatchParameters](js-apis-cert.md#x509certmatchparameters11) | 是 | 表示证书需匹配的参数。 |
| callback | AsyncCallback<Array<[X509Cert](js-apis-cert.md#x509cert)>> | 是 | 回调函数，表示匹配到的证书对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509Cert(): Promise<cert.X509Cert> {
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(certData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };

30. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
31. try {
32. x509Cert = await cert.createX509Cert(encodingBlob);
33. } catch (err) {
34. let e: BusinessError = err as BusinessError;
35. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
36. }
37. return x509Cert;
38. }

40. async function selectCerts() {
41. const x509Cert = await createX509Cert();
42. const collection = cert.createCertCRLCollection([x509Cert]);
43. // 需业务自行赋值。
44. const param: cert.X509CertMatchParameters = {
45. x509Cert,
46. validDate: '20231121074700Z',
47. issuer: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
48. subject: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
49. publicKeyAlgID: '1.2.840.10045.2.1'
50. };
51. collection.selectCerts(param, (err, certs) => {
52. if (err) {
53. console.error(`selectCerts failed, errCode: ${err.code}, errMsg: ${err.message}`);
54. } else {
55. console.info('selectCerts result: success.');
56. }
57. });
58. }
```

### selectCRLs11+

PhonePC/2in1TabletTVWearable

selectCRLs(param: X509CRLMatchParameters): Promise<Array<X509CRL>>

查找证书和证书吊销列表集合中所有与参数匹配的证书吊销列表对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CRLMatchParameters](js-apis-cert.md#x509crlmatchparameters11) | 是 | 表示证书吊销列表需匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509CRL](js-apis-cert.md#x509crl11)>> | Promise对象，表示匹配到的证书吊销列表对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509CRL(): Promise<cert.X509CRL> {
14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. // 证书吊销列表二进制数据，需业务自行赋值。
24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(crlData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };
29. let x509CRL: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509CRL = await cert.createX509CRL(encodingBlob);
32. } catch (err) {
33. let e: BusinessError = err as BusinessError;
34. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
35. }
36. return x509CRL;
37. }

39. async function createX509Cert(): Promise<cert.X509Cert> {
40. const certData = '-----BEGIN CERTIFICATE-----\r\n' +
41. 'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
42. 'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
43. 'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
44. 'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
45. 'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
46. 'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
47. 'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
48. 'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
49. 'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
50. 'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
51. 'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
52. 'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
53. 'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
54. 'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
55. 'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
56. 'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
57. '-----END CERTIFICATE-----\r\n';
58. const certEncodingBlob: cert.EncodingBlob = {
59. data: stringToUint8Array(certData),
60. encodingFormat: cert.EncodingFormat.FORMAT_PEM,
61. };

63. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
64. try {
65. x509Cert = await cert.createX509Cert(certEncodingBlob);
66. console.info('createX509Cert result: success.');
67. } catch (err) {
68. let e: BusinessError = err as BusinessError;
69. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
70. }
71. return x509Cert;
72. }

74. async function selectCRLs() {
75. const x509CRL = await createX509CRL();
76. const x509Cert = await createX509Cert();
77. const collection = cert.createCertCRLCollection([], [x509CRL]);

79. const param: cert.X509CRLMatchParameters = {
80. issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43, 0x4E,
81. 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73, 0x75, 0x31,
82. 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E, 0x67, 0x31, 0x0B,
83. 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04,
84. 0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x02, 0x74, 0x73])],
85. x509Cert: x509Cert
86. }
87. try {
88. const crls = await collection.selectCRLs(param);
89. console.info('selectCRLs result: success.');
90. } catch (err) {
91. let e: BusinessError = err as BusinessError;
92. console.error(`selectCRLs failed, errCode: ${e.code}, errMsg: ${e.message}`);
93. }
94. }
```

### selectCRLs11+

PhonePC/2in1TabletTVWearable

selectCRLs(param: X509CRLMatchParameters, callback: AsyncCallback<Array<X509CRL>>): void

查找证书和证书吊销列表集合中所有与参数匹配的证书吊销列表对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [X509CRLMatchParameters](js-apis-cert.md#x509crlmatchparameters11) | 是 | 表示证书吊销列表需匹配的参数对象。 |
| callback | AsyncCallback<Array<[X509CRL](js-apis-cert.md#x509crl11)>> | 是 | 回调函数，表示匹配到的证书吊销列表对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509CRL(): Promise<cert.X509CRL> {
14. let crlData = '-----BEGIN X509 CRL-----\n' +
15. 'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
16. 'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
17. 'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
18. 'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
19. '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
20. 'eavsH0Q3\n' +
21. '-----END X509 CRL-----\n';

23. // 证书吊销列表二进制数据，需业务自行赋值。
24. let encodingBlob: cert.EncodingBlob = {
25. data: stringToUint8Array(crlData),
26. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
27. encodingFormat: cert.EncodingFormat.FORMAT_PEM
28. };
29. let x509CRL: cert.X509CRL = {} as cert.X509CRL;
30. try {
31. x509CRL = await cert.createX509CRL(encodingBlob);
32. } catch (err) {
33. let e: BusinessError = err as BusinessError;
34. console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
35. }
36. return x509CRL;
37. }

39. async function createX509Cert(): Promise<cert.X509Cert> {
40. const certData = '-----BEGIN CERTIFICATE-----\r\n' +
41. 'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
42. 'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
43. 'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
44. 'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
45. 'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
46. 'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
47. 'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
48. 'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
49. 'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
50. 'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
51. 'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
52. 'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
53. 'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
54. 'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
55. 'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
56. 'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
57. '-----END CERTIFICATE-----\r\n';
58. const certEncodingBlob: cert.EncodingBlob = {
59. data: stringToUint8Array(certData),
60. encodingFormat: cert.EncodingFormat.FORMAT_PEM,
61. };

63. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
64. try {
65. x509Cert = await cert.createX509Cert(certEncodingBlob);
66. console.info('createX509Cert result: success.');
67. } catch (err) {
68. let e: BusinessError = err as BusinessError;
69. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
70. }
71. return x509Cert;
72. }

74. async function selectCRLs() {
75. const x509CRL = await createX509CRL();
76. const x509Cert = await createX509Cert();
77. const collection = cert.createCertCRLCollection([], [x509CRL]);

79. const param: cert.X509CRLMatchParameters = {
80. issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43, 0x4E,
81. 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73, 0x75, 0x31,
82. 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E, 0x67, 0x31, 0x0B,
83. 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04,
84. 0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x02, 0x74, 0x73])],
85. x509Cert: x509Cert
86. }
87. collection.selectCRLs(param, (err, crls) => {
88. if (err) {
89. console.error(`selectCRLs failed, errCode: ${err.code}, errMsg: ${err.message}`);
90. } else {
91. console.info('selectCRLs result: success.');
92. }
93. });
94. }
```

## cert.createX509CertChain11+

PhonePC/2in1TabletTVWearable

createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>

表示创建X509证书链对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | X509证书序列化数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CertChain](js-apis-cert.md#x509certchain11)> | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509CertChain(): Promise<cert.X509CertChain> {
14. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
16. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
17. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
18. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
19. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
20. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
21. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
22. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
23. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
24. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
25. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
26. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
27. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
28. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
29. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
30. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
31. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
32. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
33. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
34. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
35. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
36. '-----END CERTIFICATE-----\n' +
37. '-----BEGIN CERTIFICATE-----\n' +
38. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
39. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
40. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
41. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
42. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
43. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
44. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
45. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
46. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
47. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
48. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
49. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
50. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
51. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
52. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
53. 'uKPWR9dKBA==\n' +
54. '-----END CERTIFICATE-----\n' +
55. '-----BEGIN CERTIFICATE-----\n' +
56. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
57. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
58. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
59. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
60. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
61. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
62. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
63. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
64. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
65. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
66. 'xjoE\n' +
67. '-----END CERTIFICATE-----\n';

69. // 证书链二进制数据，需业务自行赋值。
70. let encodingBlob: cert.EncodingBlob = {
71. data: stringToUint8Array(certChainData),
72. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
76. try {
77. x509CertChain = await cert.createX509CertChain(encodingBlob);
78. } catch (error) {
79. let e: BusinessError = error as BusinessError;
80. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
81. }
82. return x509CertChain;
83. }

85. createX509CertChain();
```

## cert.createX509CertChain11+

PhonePC/2in1TabletTVWearable

createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void

表示创建X509证书链对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | [EncodingBlob](js-apis-cert.md#encodingblob) | 是 | X509证书序列化数据。 |
| callback | AsyncCallback<[X509CertChain](js-apis-cert.md#x509certchain11)> | 是 | 回调函数，表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
13. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
14. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
15. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
16. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
17. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
18. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
19. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
20. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
21. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
22. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
23. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
24. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
25. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
26. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
27. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
28. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
29. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
30. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
31. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
32. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
33. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
34. '-----END CERTIFICATE-----\n' +
35. '-----BEGIN CERTIFICATE-----\n' +
36. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
37. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
38. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
39. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
40. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
41. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
42. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
43. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
44. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
45. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
46. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
47. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
48. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
49. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
50. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
51. 'uKPWR9dKBA==\n' +
52. '-----END CERTIFICATE-----\n' +
53. '-----BEGIN CERTIFICATE-----\n' +
54. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
55. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
56. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
57. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
58. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
59. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
60. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
61. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
62. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
63. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
64. 'xjoE\n' +
65. '-----END CERTIFICATE-----\n';

67. // 证书链二进制数据，需业务自行赋值。
68. let encodingBlob: cert.EncodingBlob = {
69. data: stringToUint8Array(certChainData),
70. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
71. encodingFormat: cert.EncodingFormat.FORMAT_PEM
72. };

74. cert.createX509CertChain(encodingBlob, (err, certChain) => {
75. if (err) {
76. console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
77. } else {
78. console.info('createX509CertChain result: success.');
79. }
80. });
```

## cert.createX509CertChain11+

PhonePC/2in1TabletTVWearable

createX509CertChain(certs: Array<X509Cert>): X509CertChain

表示使用X509Cert数组方式创建X509证书链对象，并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certs | Array<[X509Cert](js-apis-cert.md#x509cert)> | 是 | X509证书对象数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [X509CertChain](js-apis-cert.md#x509certchain11) | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509Cert(): Promise<cert.X509Cert> {
14. let certData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
16. 'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
17. 'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
18. 'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
19. 'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
20. 'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
21. 'Qw==\n' +
22. '-----END CERTIFICATE-----\n';

24. // 证书二进制数据，需业务自行赋值。
25. let encodingBlob: cert.EncodingBlob = {
26. data: stringToUint8Array(certData),
27. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
28. encodingFormat: cert.EncodingFormat.FORMAT_PEM
29. };

31. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
32. try {
33. x509Cert = await cert.createX509Cert(encodingBlob);
34. } catch (error) {
35. let e: BusinessError = error as BusinessError;
36. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
37. }
38. return x509Cert;
39. }

41. async function createX509CertChain(): Promise<cert.X509CertChain> {
42. const x509Cert = await createX509Cert();
43. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
44. try {
45. x509CertChain = cert.createX509CertChain([x509Cert]);
46. } catch (error) {
47. let e: BusinessError = error as BusinessError;
48. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
49. }
50. return x509CertChain;
51. }

53. createX509CertChain();
```

## cert.buildX509CertChain12+

PhonePC/2in1TabletTVWearable

buildX509CertChain(param: [CertChainBuildParameters](js-apis-cert.md#certchainbuildparameters12)): Promise<CertChainBuildResult>

表示使用CertChainBuildParameters对象方式创建X509证书链对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [CertChainBuildParameters](js-apis-cert.md#certchainbuildparameters12) | 是 | 构建证书链的参数对象。  [CertChainBuildParameters](js-apis-cert.md#certchainbuildparameters12)中的maxLength要小于证书集合中证书数量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CertChainBuildResult](js-apis-cert.md#certchainbuildresult12)> | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. // 证书链数据。
14. let certPem = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
16. 'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
17. 'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
18. 'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
19. 'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
20. 'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
21. 'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
22. '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
23. '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
24. 'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
25. 'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
26. 'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
27. 'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
28. '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
29. 'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
30. 'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
31. 'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
32. 'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
33. '-----END CERTIFICATE-----';

35. let caPem = '-----BEGIN CERTIFICATE-----\n' +
36. 'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
37. 'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
38. 'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
39. '6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
40. 'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
41. 'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
42. 'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
43. 'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
44. 'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
45. 'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
46. 'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
47. 'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
48. 'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
49. 'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
50. 'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
51. 'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
52. 'sSus\n' +
53. '-----END CERTIFICATE-----';

55. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
56. // 证书二进制数据，需业务自行赋值。
57. let encodingBlob: cert.EncodingBlob = {
58. data: stringToUint8Array(certData),
59. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
60. encodingFormat: cert.EncodingFormat.FORMAT_PEM
61. };

63. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
64. try {
65. x509Cert = await cert.createX509Cert(encodingBlob);
66. } catch (error) {
67. let e: BusinessError = error as BusinessError;
68. console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
69. }
70. return x509Cert;
71. }

73. async function buildX509CertChain() {
74. try {
75. const caCert = await createX509Cert(caPem);
76. const x509Cert = await createX509Cert(certPem);
77. let certCrlCollection = cert.createCertCRLCollection([x509Cert]);
78. let param: cert.CertChainBuildParameters = {
79. certMatchParameters: { validDate: '20240812080000Z' },
80. maxLength: 3,
81. validationParameters: {
82. date: '20240812080000Z',
83. certCRLs: [certCrlCollection],
84. trustAnchors: [{ CACert: caCert }, { CACert: caCert }],
85. }
86. }
87. let certChainBuildResult = await cert.buildX509CertChain(param);
88. console.info("cert issuer name: " + certChainBuildResult.validationResult.entityCert.getIssuerName().data)
89. console.info("ca subject name: " + certChainBuildResult.validationResult.trustAnchor.CACert?.getSubjectName().data)
90. } catch (error) {
91. let e: BusinessError = error as BusinessError;
92. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
93. }
94. }

96. buildX509CertChain();
```

## cert.parsePkcs1218+

PhonePC/2in1TabletTVWearable

parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data

表示从P12文件中解析证书、私钥及其他证书合集，并返回结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | P12文件，DER格式。 |
| config | [Pkcs12ParsingConfig](js-apis-cert.md#pkcs12parsingconfig18) | 是 | P12文件的解析配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Pkcs12Data](js-apis-cert.md#pkcs12data18) | 表示P12文件解析后的证书、私钥及其他证书合集。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. function doTestParsePkcs12() {
4. try {
5. let p12_cert =
6. new Uint8Array([0x30, 0x82, 0x09, 0x51, 0x02, 0x01, 0x03, 0x30, 0x82, 0x09, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48,
7. 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x09, 0x08, 0x04, 0x82, 0x09, 0x04, 0x30, 0x82,
8. 0x09, 0x00, 0x30, 0x82, 0x03, 0xb7, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07,
9. 0x06, 0xa0, 0x82, 0x03, 0xa8, 0x30, 0x82, 0x03, 0xa4, 0x02, 0x01, 0x00, 0x30, 0x82, 0x03, 0x9d,
10. 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0x30, 0x1c, 0x06, 0x0a, 0x2a,
11. 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x06, 0x30, 0x0e, 0x04, 0x08, 0x7c, 0xd8, 0x60,
12. 0x3a, 0x07, 0xfb, 0x87, 0x8b, 0x02, 0x02, 0x08, 0x00, 0x80, 0x82, 0x03, 0x70, 0x4d, 0x64, 0xbe,
13. 0x82, 0xc2, 0x59, 0x58, 0x65, 0xf0, 0x37, 0x46, 0x4f, 0x6b, 0xfa, 0x43, 0x2e, 0x9d, 0xd9, 0x4f,
14. 0xd3, 0x54, 0x71, 0x69, 0x6e, 0x03, 0xf8, 0xb8, 0xf9, 0x05, 0xa2, 0x70, 0xa8, 0x70, 0xfb, 0xe6,
15. 0xda, 0x73, 0xdb, 0x4e, 0xdf, 0x72, 0xcd, 0xb6, 0x88, 0x81, 0xec, 0x3f, 0x8d, 0x7b, 0xdc, 0xa6,
16. 0x62, 0xd3, 0xd1, 0xdc, 0xef, 0xb9, 0x76, 0xb5, 0xd3, 0xb3, 0xfb, 0x61, 0x50, 0xeb, 0x22, 0x9b,
17. 0x72, 0x20, 0xb4, 0xe9, 0x7c, 0x5e, 0xaf, 0xa9, 0xb6, 0x40, 0x69, 0x70, 0xea, 0x79, 0x02, 0x1d,
18. 0x66, 0x71, 0x62, 0x39, 0x31, 0xd3, 0x31, 0xb1, 0x6f, 0x2a, 0x2d, 0x13, 0x59, 0xe9, 0xb7, 0x98,
19. 0xbe, 0x67, 0xfa, 0x5d, 0x6f, 0x8f, 0x7a, 0x43, 0x10, 0x5a, 0x3f, 0x13, 0xda, 0xb0, 0x94, 0x08,
20. 0x82, 0xf4, 0x39, 0x1d, 0x42, 0x26, 0x4a, 0xbe, 0x13, 0xe9, 0x89, 0x55, 0x52, 0xa4, 0x16, 0x3d,
21. 0x50, 0x83, 0x5c, 0xb9, 0x00, 0x5e, 0x03, 0x35, 0x65, 0x13, 0x1f, 0xd8, 0xf8, 0xeb, 0x28, 0xe5,
22. 0x00, 0x09, 0x9a, 0x62, 0x65, 0xab, 0x28, 0x21, 0x2e, 0x55, 0x11, 0x77, 0x7e, 0x64, 0xae, 0x12,
23. 0xc1, 0x5e, 0x85, 0xf2, 0xe7, 0xf7, 0x2b, 0x51, 0x46, 0xa6, 0xf8, 0x55, 0x2c, 0xc4, 0x0a, 0x80,
24. 0x6a, 0xc2, 0xa8, 0xba, 0x94, 0xf8, 0xee, 0x18, 0xf7, 0x32, 0x50, 0x53, 0xcc, 0x1e, 0x53, 0x85,
25. 0xeb, 0x0d, 0x1e, 0xec, 0xe2, 0xbb, 0xc2, 0xf3, 0xf7, 0x80, 0xfd, 0x81, 0x63, 0x8f, 0x87, 0x98,
26. 0x09, 0x47, 0x72, 0xee, 0x2d, 0x5a, 0x18, 0x89, 0x6b, 0x95, 0xef, 0x52, 0xde, 0x4d, 0xf5, 0x48,
27. 0x2a, 0x38, 0x6f, 0x4b, 0x98, 0x3c, 0x6d, 0x41, 0xdd, 0x1b, 0xfd, 0x65, 0x1b, 0x87, 0x8a, 0xcf,
28. 0xec, 0x47, 0xe3, 0x7a, 0xa0, 0x56, 0xd9, 0x36, 0x36, 0xcb, 0x17, 0xaa, 0x1b, 0x24, 0x79, 0x96,
29. 0xc6, 0x60, 0xd4, 0xe4, 0xa8, 0x59, 0x35, 0x5e, 0x4e, 0x00, 0xbf, 0x9a, 0xf5, 0x5c, 0x2a, 0xd7,
30. 0xd7, 0x92, 0x98, 0x79, 0xad, 0x13, 0xda, 0xea, 0xde, 0xcd, 0x65, 0x81, 0x26, 0xbd, 0x55, 0x0f,
31. 0xa4, 0x73, 0x54, 0x7b, 0x2f, 0x55, 0x2a, 0x2f, 0xb9, 0x2d, 0x6e, 0x04, 0xc8, 0x37, 0x5e, 0x93,
32. 0x09, 0xa7, 0x7f, 0xb1, 0x6b, 0x4a, 0x9f, 0xea, 0x59, 0x19, 0x57, 0xd0, 0xc1, 0xa1, 0x6b, 0xaf,
33. 0x27, 0x2b, 0xac, 0x81, 0xec, 0xcd, 0x2e, 0xa2, 0xa6, 0x08, 0x01, 0xfc, 0xa1, 0xbc, 0xc9, 0xdc,
34. 0x97, 0xb9, 0x48, 0xa8, 0x65, 0x5d, 0x63, 0xdb, 0x5c, 0x7e, 0x55, 0xe7, 0x47, 0xf2, 0x74, 0x17,
35. 0x67, 0xfe, 0x56, 0x20, 0x54, 0x65, 0x11, 0xdf, 0xec, 0x75, 0x70, 0x49, 0x59, 0xd1, 0xea, 0x6b,
36. 0x8f, 0x39, 0xec, 0x5d, 0x81, 0x82, 0x9a, 0xec, 0xce, 0x6c, 0x0c, 0x32, 0x14, 0xbd, 0xef, 0xac,
37. 0xae, 0x04, 0xd0, 0x75, 0x62, 0xf5, 0x82, 0x16, 0xd1, 0xa8, 0xfb, 0x22, 0x2a, 0xc2, 0xe7, 0x7a,
38. 0x75, 0x08, 0x59, 0x99, 0x34, 0x3d, 0xd9, 0xd7, 0x66, 0xb8, 0xcd, 0xaa, 0xf4, 0x48, 0xcc, 0x21,
39. 0x25, 0x83, 0xae, 0xad, 0x55, 0x0e, 0xff, 0x44, 0xf3, 0xcc, 0xd1, 0x89, 0x72, 0x0f, 0x9f, 0xe3,
40. 0xe5, 0xc7, 0xd4, 0x53, 0x94, 0xd6, 0xfb, 0x35, 0xd5, 0xd8, 0x2f, 0xa7, 0x4b, 0xf9, 0x50, 0x15,
41. 0x1e, 0x35, 0xfc, 0x3d, 0xca, 0xad, 0xb6, 0x49, 0x16, 0xee, 0xff, 0xd7, 0x8a, 0xcc, 0xf0, 0x96,
42. 0x11, 0x97, 0x22, 0xf3, 0xf7, 0x7c, 0x7a, 0x50, 0x49, 0x12, 0x68, 0x6e, 0x0e, 0x62, 0x32, 0xc7,
43. 0xe9, 0xc3, 0xa0, 0x1b, 0xfe, 0x29, 0x8c, 0x46, 0xc2, 0x7e, 0xe1, 0xea, 0xc3, 0xcb, 0x30, 0xaf,
44. 0xe4, 0x60, 0xe5, 0xa5, 0xa5, 0xb8, 0xf4, 0x16, 0xfa, 0x19, 0xd0, 0x1c, 0x14, 0xce, 0xf9, 0xa8,
45. 0x0b, 0x3f, 0x87, 0x89, 0xd3, 0xed, 0x9e, 0x16, 0x14, 0xbb, 0xd3, 0x64, 0xeb, 0x00, 0xe7, 0x48,
46. 0x1f, 0xd4, 0x47, 0xbc, 0xa9, 0x6f, 0x03, 0xe0, 0x0e, 0xaf, 0xb9, 0xad, 0x05, 0xa0, 0x1d, 0xee,
47. 0x0a, 0xcd, 0x0f, 0xd0, 0xb8, 0xf1, 0x35, 0x80, 0xa7, 0x72, 0xcd, 0x36, 0x8e, 0xce, 0x72, 0xf9,
48. 0x9f, 0xd5, 0x29, 0xae, 0x02, 0xb7, 0xbe, 0x65, 0xff, 0x38, 0x45, 0xf8, 0x8d, 0x87, 0x2f, 0xf8,
49. 0xdd, 0xc1, 0x72, 0x17, 0x2b, 0xdd, 0x3e, 0xfe, 0x01, 0xa0, 0x59, 0xb3, 0x19, 0x92, 0xf0, 0x59,
50. 0xf5, 0x06, 0x77, 0x8b, 0x1a, 0x41, 0x1d, 0x8b, 0x80, 0x74, 0x95, 0x8b, 0x30, 0x03, 0x18, 0xdd,
51. 0x1e, 0x1b, 0x21, 0x36, 0xdf, 0xde, 0xc3, 0xa2, 0x68, 0xe0, 0x3d, 0x94, 0x37, 0x6b, 0x48, 0xb2,
52. 0xb9, 0x41, 0x53, 0xd6, 0x65, 0xef, 0x7a, 0x3d, 0xdc, 0x09, 0x17, 0x66, 0xb4, 0x05, 0x58, 0x8a,
53. 0x5d, 0x2f, 0x40, 0x4a, 0x91, 0x8a, 0xa5, 0xb7, 0x29, 0xfb, 0x37, 0x81, 0x71, 0x77, 0x50, 0x8d,
54. 0x34, 0x80, 0x7e, 0xab, 0xb9, 0xc8, 0xdc, 0xb7, 0x2c, 0x7e, 0xbc, 0xad, 0x7c, 0x14, 0x5c, 0xf6,
55. 0x90, 0x88, 0x0e, 0x0d, 0x50, 0x7a, 0x4e, 0xa6, 0x85, 0xe4, 0x2a, 0xe7, 0x67, 0x21, 0x53, 0xbb,
56. 0x73, 0xd5, 0x30, 0x78, 0xbd, 0x08, 0x2b, 0x42, 0x44, 0x3e, 0x5d, 0x2b, 0x2f, 0x09, 0x8e, 0x82,
57. 0xc3, 0x5b, 0x9e, 0xd8, 0x20, 0xc6, 0xb7, 0x42, 0xe5, 0xb3, 0x60, 0x0b, 0x9b, 0x01, 0x76, 0x26,
58. 0xf7, 0xc1, 0xf7, 0xe1, 0xd1, 0x46, 0xf7, 0x9c, 0x21, 0xfd, 0x66, 0xb7, 0x14, 0x1d, 0x89, 0xb5,
59. 0xd3, 0xa1, 0x4e, 0x57, 0x97, 0xe7, 0xe4, 0x63, 0x96, 0xe2, 0x6f, 0x10, 0x6a, 0xb7, 0x8e, 0x83,
60. 0x64, 0x22, 0x10, 0x02, 0x27, 0x87, 0x6d, 0xb6, 0x11, 0x51, 0xe9, 0xe6, 0x68, 0x1a, 0xc8, 0xd3,
61. 0x6b, 0x23, 0x33, 0x68, 0x66, 0xab, 0x4d, 0xf9, 0x92, 0x11, 0x67, 0x9d, 0x24, 0xee, 0x18, 0xa8,
62. 0x3c, 0x5a, 0xfe, 0x79, 0x76, 0x99, 0xeb, 0x9f, 0x19, 0x9d, 0x74, 0xee, 0x13, 0xd9, 0xb1, 0x7b,
63. 0x4e, 0xcf, 0x30, 0x05, 0xdb, 0x5a, 0x3e, 0x00, 0x7e, 0x0a, 0xed, 0x6f, 0xaf, 0x0d, 0x1b, 0xf3,
64. 0x61, 0x24, 0x06, 0xe7, 0xf2, 0x57, 0x72, 0xf8, 0x61, 0x4d, 0x5f, 0x00, 0x78, 0x1f, 0x4d, 0xc7,
65. 0x28, 0x5e, 0xc4, 0x9b, 0xed, 0xac, 0x4f, 0x16, 0xaf, 0x81, 0x85, 0x33, 0x16, 0xbd, 0x6a, 0xb9,
66. 0xb2, 0x8e, 0x25, 0xbc, 0xaf, 0xfd, 0xea, 0xb7, 0x20, 0x32, 0x15, 0x62, 0x77, 0x52, 0xa1, 0xf2,
67. 0xd0, 0x9d, 0x12, 0x4c, 0x85, 0x71, 0x08, 0x03, 0xa7, 0x94, 0x34, 0xb4, 0x96, 0x30, 0x82, 0x05,
68. 0x41, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x05, 0x32,
69. 0x04, 0x82, 0x05, 0x2e, 0x30, 0x82, 0x05, 0x2a, 0x30, 0x82, 0x05, 0x26, 0x06, 0x0b, 0x2a, 0x86,
70. 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x0a, 0x01, 0x02, 0xa0, 0x82, 0x04, 0xee, 0x30, 0x82, 0x04,
71. 0xea, 0x30, 0x1c, 0x06, 0x0a, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x03, 0x30,
72. 0x0e, 0x04, 0x08, 0x30, 0xee, 0xbd, 0x7c, 0xcb, 0xb5, 0xa5, 0x1b, 0x02, 0x02, 0x08, 0x00, 0x04,
73. 0x82, 0x04, 0xc8, 0x1e, 0xd0, 0x7f, 0x7e, 0x86, 0x1c, 0x6f, 0x0e, 0xac, 0x6c, 0xe3, 0x35, 0xcb,
74. 0xff, 0xe4, 0x84, 0x88, 0x97, 0x45, 0xf3, 0x48, 0xa9, 0x98, 0xeb, 0x74, 0x91, 0x53, 0x07, 0x7a,
75. 0xe4, 0x78, 0x89, 0x13, 0xe7, 0xce, 0xa3, 0xc5, 0xab, 0x2c, 0x16, 0xe5, 0x02, 0x64, 0xc6, 0xb5,
76. 0x11, 0x36, 0x69, 0x0b, 0x5f, 0x7e, 0x95, 0x27, 0x59, 0x9a, 0xac, 0x98, 0x12, 0x76, 0x39, 0x31,
77. 0xaa, 0x4f, 0x22, 0x55, 0x21, 0x71, 0x20, 0xeb, 0x4e, 0x5e, 0x2d, 0xd8, 0xab, 0xd9, 0x64, 0x38,
78. 0x13, 0x9a, 0x14, 0x48, 0x7f, 0x48, 0x05, 0xec, 0x49, 0x55, 0x80, 0x49, 0xaf, 0x4e, 0x29, 0xdf,
79. 0x4a, 0xfb, 0xa1, 0x20, 0x2f, 0x98, 0x35, 0xf7, 0x8f, 0xb9, 0x41, 0x8b, 0x00, 0x14, 0x23, 0x9a,
80. 0x43, 0xfe, 0x55, 0xfc, 0xe5, 0x57, 0x19, 0xa9, 0x74, 0x44, 0x1f, 0xdd, 0xc3, 0xc8, 0x9f, 0xfa,
81. 0x9f, 0x67, 0x93, 0xed, 0x79, 0x11, 0xe1, 0x4e, 0xed, 0xd6, 0x20, 0x82, 0xc8, 0x85, 0xdf, 0x4e,
82. 0xa0, 0xcd, 0xd8, 0x36, 0x37, 0x4f, 0x67, 0x9d, 0x84, 0x44, 0x14, 0xce, 0xc0, 0xc9, 0xa6, 0xbd,
83. 0x73, 0x06, 0x27, 0xb7, 0x16, 0x97, 0x8c, 0x61, 0xd9, 0x63, 0xb2, 0x56, 0x8d, 0x28, 0x9e, 0x2e,
84. 0xcf, 0xa3, 0xfe, 0x8d, 0xaa, 0xef, 0x69, 0x32, 0x7b, 0x32, 0xbe, 0xd5, 0x62, 0x2c, 0x2e, 0x7f,
85. 0x72, 0xdb, 0x3c, 0x4b, 0xe4, 0x76, 0xa3, 0xa9, 0xa1, 0x67, 0x84, 0x86, 0xea, 0x14, 0x15, 0x6c,
86. 0x74, 0xd2, 0xac, 0x0e, 0xe2, 0x54, 0x54, 0xd4, 0x31, 0xa3, 0x88, 0x66, 0x89, 0x31, 0x7b, 0xf7,
87. 0x3c, 0x92, 0xce, 0x3e, 0x86, 0xfb, 0x57, 0xc8, 0x65, 0xae, 0x85, 0x6d, 0x48, 0xf6, 0xe6, 0x37,
88. 0xeb, 0x77, 0xcf, 0x06, 0xd6, 0x9e, 0x54, 0xb4, 0xd8, 0x9a, 0x5f, 0xdd, 0xc5, 0xa5, 0x05, 0xa0,
89. 0x4b, 0xd1, 0x54, 0xab, 0x4f, 0xd0, 0x3e, 0x6b, 0x8f, 0x03, 0x66, 0xd4, 0xe2, 0x90, 0xea, 0x2d,
90. 0x9b, 0x6a, 0x2b, 0xc4, 0x7b, 0x9d, 0xf1, 0xb5, 0x22, 0xdf, 0x86, 0xc2, 0xfd, 0x13, 0x0a, 0x69,
91. 0x29, 0x59, 0xe9, 0x45, 0xcd, 0xdf, 0xcd, 0xa5, 0x71, 0x7e, 0x70, 0xc3, 0x60, 0x9e, 0x47, 0x5d,
92. 0xd4, 0x6c, 0xcc, 0x15, 0x51, 0x23, 0x5b, 0x4e, 0xee, 0x72, 0x80, 0x49, 0xd6, 0xac, 0x89, 0x16,
93. 0x65, 0xf4, 0x95, 0x57, 0x19, 0x13, 0xab, 0x9c, 0x08, 0xe8, 0xdf, 0x0a, 0xe2, 0x39, 0xfc, 0xff,
94. 0x42, 0x02, 0xac, 0xaf, 0xf1, 0xb6, 0x56, 0xef, 0x75, 0x60, 0x2f, 0xc2, 0x5d, 0xef, 0xf5, 0x79,
95. 0xb5, 0x46, 0xa0, 0xb5, 0x03, 0x67, 0xef, 0x78, 0x3d, 0x49, 0xd0, 0xc5, 0x0e, 0xff, 0x42, 0x72,
96. 0x02, 0x86, 0x99, 0x93, 0xaa, 0xa3, 0x9e, 0x2c, 0xc7, 0xec, 0xa2, 0xdf, 0x25, 0x4e, 0x28, 0x81,
97. 0x82, 0x3e, 0x29, 0xd3, 0x37, 0xfd, 0x32, 0xf4, 0x85, 0x46, 0x42, 0xb9, 0x94, 0x44, 0x8a, 0xbf,
98. 0xd9, 0x14, 0xcb, 0xb6, 0xd3, 0xc5, 0xe7, 0x6b, 0x28, 0x70, 0xc3, 0x9c, 0xc2, 0x93, 0x9d, 0x2f,
99. 0xab, 0xd6, 0xb2, 0x19, 0x28, 0x9a, 0xda, 0x0d, 0x90, 0x5b, 0xba, 0x64, 0x6f, 0xcc, 0x11, 0xef,
100. 0x6c, 0x88, 0x18, 0x4f, 0x86, 0x6e, 0xed, 0xcf, 0xde, 0x0d, 0xec, 0xe2, 0x12, 0xc3, 0x89, 0x0a,
101. 0x3f, 0xbb, 0x3d, 0x8c, 0x8f, 0xa9, 0x40, 0xe6, 0xf8, 0xd1, 0x1a, 0x9a, 0x7e, 0x8a, 0xd7, 0x7b,
102. 0x56, 0xf4, 0x5d, 0x80, 0x64, 0xd5, 0x88, 0x86, 0x85, 0x18, 0x30, 0x5d, 0x64, 0x04, 0xb3, 0xc2,
103. 0xc7, 0x80, 0xda, 0x3e, 0xc4, 0xd6, 0xf6, 0xc4, 0x95, 0x56, 0xd5, 0xad, 0x82, 0x86, 0xcc, 0x1a,
104. 0x05, 0x69, 0x06, 0x08, 0x5b, 0x19, 0xea, 0x10, 0xc5, 0xcd, 0x67, 0x93, 0xab, 0x0f, 0xe3, 0xba,
105. 0xb0, 0x0d, 0xac, 0x99, 0x0d, 0x35, 0x6f, 0xe5, 0x41, 0xb2, 0x7c, 0x87, 0x91, 0x6c, 0xe2, 0x75,
106. 0x9b, 0x64, 0x62, 0x06, 0x2a, 0x8b, 0xd9, 0x4d, 0x23, 0xcd, 0x2b, 0xef, 0xf5, 0x61, 0x82, 0x8e,
107. 0x3f, 0xf6, 0x2b, 0xe1, 0x6f, 0xcf, 0xbd, 0xaa, 0x07, 0x97, 0x49, 0x4e, 0x02, 0x9d, 0xa5, 0x9e,
108. 0xc5, 0xd7, 0x8b, 0xd3, 0xe1, 0xd9, 0x35, 0x96, 0x9d, 0x1f, 0xa2, 0xf6, 0x91, 0xee, 0xd1, 0x3b,
109. 0xa8, 0xfe, 0x4d, 0xeb, 0xf9, 0xfc, 0xe4, 0xab, 0x60, 0xb7, 0x86, 0x9d, 0x2a, 0x35, 0xb0, 0x00,
110. 0xd4, 0x3c, 0x2a, 0x7e, 0x6d, 0x65, 0x5f, 0xf3, 0x7c, 0x23, 0x57, 0x52, 0x2a, 0x8c, 0x5b, 0x36,
111. 0x74, 0xb7, 0x61, 0x49, 0xf0, 0xdf, 0xcf, 0x8a, 0x28, 0xc5, 0x8d, 0xbc, 0x20, 0xcc, 0xac, 0x86,
112. 0x20, 0xd8, 0x2d, 0x86, 0x99, 0xf5, 0xf0, 0xdb, 0xed, 0x8d, 0xf9, 0xd7, 0x4e, 0xa8, 0xde, 0x84,
113. 0x35, 0x50, 0xc1, 0x7c, 0xbd, 0xdf, 0xc2, 0x24, 0x1a, 0x49, 0x24, 0x9a, 0x37, 0x93, 0xca, 0x2d,
114. 0x73, 0x47, 0x8f, 0x83, 0xed, 0x4d, 0xca, 0xf8, 0xf0, 0xd3, 0x9b, 0xe0, 0x4b, 0x3b, 0xf1, 0x86,
115. 0xeb, 0x78, 0x7b, 0x42, 0xa1, 0xb9, 0x36, 0x15, 0xde, 0x63, 0xab, 0x8b, 0x8b, 0x5d, 0xa2, 0x92,
116. 0x10, 0x95, 0xdf, 0xda, 0xd7, 0xba, 0xa0, 0x26, 0xb9, 0xdc, 0x83, 0xeb, 0xdc, 0xd2, 0x1f, 0xf1,
117. 0xb1, 0x8d, 0x21, 0x51, 0x71, 0x59, 0x0e, 0xe8, 0x7e, 0xf1, 0x53, 0x08, 0x98, 0x79, 0x05, 0x3b,
118. 0x22, 0xf1, 0xda, 0x07, 0x0d, 0xf7, 0x89, 0x5e, 0xc4, 0x62, 0x8c, 0xf9, 0x19, 0xc8, 0xbc, 0xa4,
119. 0x0c, 0x6f, 0x41, 0x34, 0x56, 0x22, 0x6b, 0xe6, 0xee, 0x7c, 0x4a, 0xd9, 0x26, 0x8c, 0x56, 0x12,
120. 0xf3, 0x03, 0x12, 0x1c, 0x5b, 0x8d, 0x64, 0x5c, 0x1c, 0xb6, 0x0f, 0x93, 0xaf, 0xb1, 0x67, 0x6f,
121. 0x13, 0xdd, 0xe3, 0xcf, 0x0e, 0xe6, 0x06, 0xf3, 0xb2, 0xbc, 0x99, 0xf5, 0xb0, 0xd7, 0xe9, 0x7e,
122. 0xb0, 0x6a, 0xb9, 0xb5, 0xda, 0xcf, 0x88, 0xf1, 0xc5, 0x58, 0x54, 0x05, 0x5c, 0x9d, 0x79, 0xc2,
123. 0xcd, 0xbb, 0xc6, 0xf2, 0x69, 0xa9, 0xe3, 0x4e, 0x05, 0x0d, 0x02, 0xb6, 0x4d, 0x8e, 0x7d, 0x60,
124. 0x8e, 0xda, 0x4d, 0x28, 0xd2, 0xec, 0x8a, 0x11, 0xe3, 0xe7, 0x17, 0x20, 0x07, 0x7b, 0xfc, 0x9b,
125. 0x4e, 0xf7, 0x79, 0xf5, 0x0a, 0x6e, 0xd1, 0x1e, 0x7b, 0x83, 0x66, 0x5e, 0x1b, 0x9d, 0x36, 0x32,
126. 0x89, 0xf6, 0x72, 0xa5, 0x58, 0x54, 0x42, 0xba, 0x90, 0xf3, 0xbb, 0x05, 0x46, 0xa4, 0x91, 0x1c,
127. 0xdb, 0xab, 0xf3, 0x68, 0x56, 0x7a, 0xd3, 0xff, 0x3f, 0x9f, 0xc5, 0x4a, 0x47, 0xbd, 0x89, 0x46,
128. 0xf6, 0x94, 0x3a, 0x94, 0xd4, 0x30, 0xd3, 0xae, 0x0d, 0x99, 0x95, 0xf7, 0x75, 0xfe, 0x14, 0x10,
129. 0x9e, 0xed, 0x21, 0x0f, 0x0d, 0x54, 0x7d, 0x54, 0xc5, 0x80, 0x21, 0x4d, 0xf2, 0xaf, 0x67, 0xaf,
130. 0x8a, 0x76, 0x9e, 0x34, 0x32, 0x74, 0x89, 0x2a, 0x32, 0xf9, 0x48, 0x20, 0x90, 0xe6, 0x4a, 0xa3,
131. 0x7f, 0xf2, 0x2a, 0x51, 0x22, 0x93, 0xe5, 0xdd, 0x59, 0xb3, 0x83, 0xa8, 0x47, 0xf5, 0x6b, 0x38,
132. 0x24, 0xc2, 0xac, 0x2d, 0x03, 0xda, 0xb1, 0x17, 0x19, 0xe0, 0x38, 0x2c, 0xb3, 0xa6, 0x4c, 0x8e,
133. 0xae, 0x63, 0xa7, 0xae, 0x96, 0xb1, 0x07, 0x8c, 0x8f, 0x6a, 0x08, 0x32, 0x15, 0x1f, 0x33, 0x97,
134. 0x21, 0x3b, 0x51, 0x70, 0xc5, 0x1f, 0xa6, 0xa3, 0x8a, 0xd0, 0x8f, 0x0b, 0xda, 0x64, 0xab, 0xbe,
135. 0xee, 0x4b, 0x14, 0xfd, 0x32, 0x87, 0x9e, 0xa7, 0x19, 0x75, 0xc9, 0xaa, 0xd3, 0xed, 0xa7, 0xa0,
136. 0x01, 0xe7, 0xa0, 0xe5, 0x28, 0xdd, 0x3b, 0x7c, 0x49, 0xe4, 0x24, 0x7d, 0x92, 0x86, 0x25, 0x03,
137. 0xb3, 0x66, 0x04, 0xf3, 0xa1, 0x40, 0x11, 0x35, 0x3a, 0x1d, 0xbf, 0x1c, 0x02, 0x83, 0x3d, 0x37,
138. 0x51, 0x88, 0xa3, 0x2b, 0x10, 0x8c, 0x8e, 0x10, 0xdd, 0xdc, 0xef, 0xa4, 0xe9, 0x14, 0x77, 0xb6,
139. 0x8e, 0x75, 0xb6, 0x8e, 0xea, 0xaa, 0x57, 0x16, 0x1f, 0xb0, 0x0c, 0xbc, 0x44, 0xed, 0x92, 0x94,
140. 0x9a, 0xb4, 0xf3, 0x31, 0x64, 0x02, 0x5c, 0xa1, 0x51, 0x63, 0x39, 0x42, 0x74, 0x7a, 0x1d, 0xf2,
141. 0xf5, 0x92, 0x50, 0xf1, 0x5a, 0x8a, 0xde, 0xb3, 0x4e, 0xf1, 0x6e, 0x67, 0xd9, 0x5b, 0x00, 0xa7,
142. 0xd1, 0x90, 0x58, 0x36, 0xc4, 0x15, 0x80, 0xbb, 0xa5, 0xbb, 0x98, 0xc0, 0x8a, 0x9b, 0x17, 0x35,
143. 0x36, 0x3b, 0x62, 0x0f, 0x29, 0xcd, 0xe9, 0x04, 0x0e, 0x9d, 0xca, 0x43, 0x04, 0xdf, 0x17, 0x49,
144. 0xbf, 0xb6, 0x7a, 0x7a, 0x3c, 0xdb, 0x0d, 0x6d, 0xd5, 0x89, 0xb9, 0x69, 0x94, 0xd8, 0xb2, 0xd6,
145. 0x38, 0x8a, 0xcc, 0x78, 0x44, 0x40, 0x63, 0x9f, 0x1e, 0x0e, 0x40, 0x33, 0x51, 0xd3, 0x65, 0xf8,
146. 0xf1, 0x42, 0x06, 0x75, 0x84, 0xe7, 0xb1, 0xe9, 0xd6, 0xa4, 0x5e, 0x7f, 0xb0, 0x48, 0x6f, 0x80,
147. 0x92, 0xf8, 0xfc, 0x2a, 0xdb, 0x18, 0x97, 0xe5, 0xe7, 0xc7, 0x46, 0xb6, 0x59, 0x8c, 0x3a, 0x09,
148. 0x91, 0xc1, 0x49, 0x55, 0xf9, 0xf3, 0x87, 0x19, 0xdc, 0x72, 0x56, 0xd3, 0x20, 0x5e, 0xc5, 0x3d,
149. 0xfb, 0x19, 0xea, 0x6a, 0xdf, 0x09, 0xb2, 0x8f, 0xb6, 0xdd, 0x26, 0x31, 0x25, 0x30, 0x23, 0x06,
150. 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x3b, 0xd2,
151. 0xb3, 0x51, 0x4c, 0x57, 0xd0, 0xca, 0x34, 0xa4, 0xf0, 0x06, 0xdd, 0xe9, 0x76, 0x08, 0xdb, 0x7b,
152. 0x3a, 0xb0, 0x30, 0x31, 0x30, 0x21, 0x30, 0x09, 0x06, 0x05, 0x2b, 0x0e, 0x03, 0x02, 0x1a, 0x05,
153. 0x00, 0x04, 0x14, 0x8e, 0x7f, 0x87, 0x67, 0x78, 0x64, 0x93, 0x36, 0x35, 0xe5, 0x93, 0x9d, 0xac,
154. 0x61, 0x09, 0x4f, 0xdc, 0x95, 0xd7, 0x4f, 0x04, 0x08, 0x23, 0xc2, 0xc0, 0xc6, 0x8d, 0x5f, 0x70,
155. 0x7e, 0x02, 0x02, 0x08, 0x00]);

157. let conf: cert.Pkcs12ParsingConfig = {
158. password: '123456',
159. needsCert: false,
160. needsPrivateKey: true,
161. privateKeyFormat: cert.EncodingBaseFormat.DER,
162. needsOtherCerts: false,
163. };
164. let p12: cert.Pkcs12Data = cert.parsePkcs12(p12_cert, conf);
165. console.info('parsePKCS12 result: success.');
166. if (p12.privateKey) {
167. console.info('privateKey:' + p12.privateKey.toString())
168. }
169. } catch (error) {
170. console.error(`parsePKCS12 failed: errCode: ${error.code}, errMsg: ${error.message}`);
171. }
172. }
```

## cert.parsePkcs1221+

PhonePC/2in1TabletTVWearable

parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>

表示从Pkcs12文件中解析证书、私钥及其他证书合集。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Pkcs12文件，DER格式。 |
| password | string | 是 | Pkcs12的密码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Pkcs12Data](js-apis-cert.md#pkcs12data18)> | Promise对象，返回Pkcs12文件解析后的证书、私钥及其他证书合集。返回的Pkcs12Data中的私钥采用PEM格式编码。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The length of the data is zero or too large;  2. The length of the password is zero or too large. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. async function doTestParsePkcs12() {
4. try {
5. let p12_cert =
6. new Uint8Array([0x30, 0x82, 0x09, 0x51, 0x02, 0x01, 0x03, 0x30, 0x82, 0x09, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48,
7. 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x09, 0x08, 0x04, 0x82, 0x09, 0x04, 0x30, 0x82,
8. 0x09, 0x00, 0x30, 0x82, 0x03, 0xb7, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07,
9. 0x06, 0xa0, 0x82, 0x03, 0xa8, 0x30, 0x82, 0x03, 0xa4, 0x02, 0x01, 0x00, 0x30, 0x82, 0x03, 0x9d,
10. 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0x30, 0x1c, 0x06, 0x0a, 0x2a,
11. 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x06, 0x30, 0x0e, 0x04, 0x08, 0x7c, 0xd8, 0x60,
12. 0x3a, 0x07, 0xfb, 0x87, 0x8b, 0x02, 0x02, 0x08, 0x00, 0x80, 0x82, 0x03, 0x70, 0x4d, 0x64, 0xbe,
13. 0x82, 0xc2, 0x59, 0x58, 0x65, 0xf0, 0x37, 0x46, 0x4f, 0x6b, 0xfa, 0x43, 0x2e, 0x9d, 0xd9, 0x4f,
14. 0xd3, 0x54, 0x71, 0x69, 0x6e, 0x03, 0xf8, 0xb8, 0xf9, 0x05, 0xa2, 0x70, 0xa8, 0x70, 0xfb, 0xe6,
15. 0xda, 0x73, 0xdb, 0x4e, 0xdf, 0x72, 0xcd, 0xb6, 0x88, 0x81, 0xec, 0x3f, 0x8d, 0x7b, 0xdc, 0xa6,
16. 0x62, 0xd3, 0xd1, 0xdc, 0xef, 0xb9, 0x76, 0xb5, 0xd3, 0xb3, 0xfb, 0x61, 0x50, 0xeb, 0x22, 0x9b,
17. 0x72, 0x20, 0xb4, 0xe9, 0x7c, 0x5e, 0xaf, 0xa9, 0xb6, 0x40, 0x69, 0x70, 0xea, 0x79, 0x02, 0x1d,
18. 0x66, 0x71, 0x62, 0x39, 0x31, 0xd3, 0x31, 0xb1, 0x6f, 0x2a, 0x2d, 0x13, 0x59, 0xe9, 0xb7, 0x98,
19. 0xbe, 0x67, 0xfa, 0x5d, 0x6f, 0x8f, 0x7a, 0x43, 0x10, 0x5a, 0x3f, 0x13, 0xda, 0xb0, 0x94, 0x08,
20. 0x82, 0xf4, 0x39, 0x1d, 0x42, 0x26, 0x4a, 0xbe, 0x13, 0xe9, 0x89, 0x55, 0x52, 0xa4, 0x16, 0x3d,
21. 0x50, 0x83, 0x5c, 0xb9, 0x00, 0x5e, 0x03, 0x35, 0x65, 0x13, 0x1f, 0xd8, 0xf8, 0xeb, 0x28, 0xe5,
22. 0x00, 0x09, 0x9a, 0x62, 0x65, 0xab, 0x28, 0x21, 0x2e, 0x55, 0x11, 0x77, 0x7e, 0x64, 0xae, 0x12,
23. 0xc1, 0x5e, 0x85, 0xf2, 0xe7, 0xf7, 0x2b, 0x51, 0x46, 0xa6, 0xf8, 0x55, 0x2c, 0xc4, 0x0a, 0x80,
24. 0x6a, 0xc2, 0xa8, 0xba, 0x94, 0xf8, 0xee, 0x18, 0xf7, 0x32, 0x50, 0x53, 0xcc, 0x1e, 0x53, 0x85,
25. 0xeb, 0x0d, 0x1e, 0xec, 0xe2, 0xbb, 0xc2, 0xf3, 0xf7, 0x80, 0xfd, 0x81, 0x63, 0x8f, 0x87, 0x98,
26. 0x09, 0x47, 0x72, 0xee, 0x2d, 0x5a, 0x18, 0x89, 0x6b, 0x95, 0xef, 0x52, 0xde, 0x4d, 0xf5, 0x48,
27. 0x2a, 0x38, 0x6f, 0x4b, 0x98, 0x3c, 0x6d, 0x41, 0xdd, 0x1b, 0xfd, 0x65, 0x1b, 0x87, 0x8a, 0xcf,
28. 0xec, 0x47, 0xe3, 0x7a, 0xa0, 0x56, 0xd9, 0x36, 0x36, 0xcb, 0x17, 0xaa, 0x1b, 0x24, 0x79, 0x96,
29. 0xc6, 0x60, 0xd4, 0xe4, 0xa8, 0x59, 0x35, 0x5e, 0x4e, 0x00, 0xbf, 0x9a, 0xf5, 0x5c, 0x2a, 0xd7,
30. 0xd7, 0x92, 0x98, 0x79, 0xad, 0x13, 0xda, 0xea, 0xde, 0xcd, 0x65, 0x81, 0x26, 0xbd, 0x55, 0x0f,
31. 0xa4, 0x73, 0x54, 0x7b, 0x2f, 0x55, 0x2a, 0x2f, 0xb9, 0x2d, 0x6e, 0x04, 0xc8, 0x37, 0x5e, 0x93,
32. 0x09, 0xa7, 0x7f, 0xb1, 0x6b, 0x4a, 0x9f, 0xea, 0x59, 0x19, 0x57, 0xd0, 0xc1, 0xa1, 0x6b, 0xaf,
33. 0x27, 0x2b, 0xac, 0x81, 0xec, 0xcd, 0x2e, 0xa2, 0xa6, 0x08, 0x01, 0xfc, 0xa1, 0xbc, 0xc9, 0xdc,
34. 0x97, 0xb9, 0x48, 0xa8, 0x65, 0x5d, 0x63, 0xdb, 0x5c, 0x7e, 0x55, 0xe7, 0x47, 0xf2, 0x74, 0x17,
35. 0x67, 0xfe, 0x56, 0x20, 0x54, 0x65, 0x11, 0xdf, 0xec, 0x75, 0x70, 0x49, 0x59, 0xd1, 0xea, 0x6b,
36. 0x8f, 0x39, 0xec, 0x5d, 0x81, 0x82, 0x9a, 0xec, 0xce, 0x6c, 0x0c, 0x32, 0x14, 0xbd, 0xef, 0xac,
37. 0xae, 0x04, 0xd0, 0x75, 0x62, 0xf5, 0x82, 0x16, 0xd1, 0xa8, 0xfb, 0x22, 0x2a, 0xc2, 0xe7, 0x7a,
38. 0x75, 0x08, 0x59, 0x99, 0x34, 0x3d, 0xd9, 0xd7, 0x66, 0xb8, 0xcd, 0xaa, 0xf4, 0x48, 0xcc, 0x21,
39. 0x25, 0x83, 0xae, 0xad, 0x55, 0x0e, 0xff, 0x44, 0xf3, 0xcc, 0xd1, 0x89, 0x72, 0x0f, 0x9f, 0xe3,
40. 0xe5, 0xc7, 0xd4, 0x53, 0x94, 0xd6, 0xfb, 0x35, 0xd5, 0xd8, 0x2f, 0xa7, 0x4b, 0xf9, 0x50, 0x15,
41. 0x1e, 0x35, 0xfc, 0x3d, 0xca, 0xad, 0xb6, 0x49, 0x16, 0xee, 0xff, 0xd7, 0x8a, 0xcc, 0xf0, 0x96,
42. 0x11, 0x97, 0x22, 0xf3, 0xf7, 0x7c, 0x7a, 0x50, 0x49, 0x12, 0x68, 0x6e, 0x0e, 0x62, 0x32, 0xc7,
43. 0xe9, 0xc3, 0xa0, 0x1b, 0xfe, 0x29, 0x8c, 0x46, 0xc2, 0x7e, 0xe1, 0xea, 0xc3, 0xcb, 0x30, 0xaf,
44. 0xe4, 0x60, 0xe5, 0xa5, 0xa5, 0xb8, 0xf4, 0x16, 0xfa, 0x19, 0xd0, 0x1c, 0x14, 0xce, 0xf9, 0xa8,
45. 0x0b, 0x3f, 0x87, 0x89, 0xd3, 0xed, 0x9e, 0x16, 0x14, 0xbb, 0xd3, 0x64, 0xeb, 0x00, 0xe7, 0x48,
46. 0x1f, 0xd4, 0x47, 0xbc, 0xa9, 0x6f, 0x03, 0xe0, 0x0e, 0xaf, 0xb9, 0xad, 0x05, 0xa0, 0x1d, 0xee,
47. 0x0a, 0xcd, 0x0f, 0xd0, 0xb8, 0xf1, 0x35, 0x80, 0xa7, 0x72, 0xcd, 0x36, 0x8e, 0xce, 0x72, 0xf9,
48. 0x9f, 0xd5, 0x29, 0xae, 0x02, 0xb7, 0xbe, 0x65, 0xff, 0x38, 0x45, 0xf8, 0x8d, 0x87, 0x2f, 0xf8,
49. 0xdd, 0xc1, 0x72, 0x17, 0x2b, 0xdd, 0x3e, 0xfe, 0x01, 0xa0, 0x59, 0xb3, 0x19, 0x92, 0xf0, 0x59,
50. 0xf5, 0x06, 0x77, 0x8b, 0x1a, 0x41, 0x1d, 0x8b, 0x80, 0x74, 0x95, 0x8b, 0x30, 0x03, 0x18, 0xdd,
51. 0x1e, 0x1b, 0x21, 0x36, 0xdf, 0xde, 0xc3, 0xa2, 0x68, 0xe0, 0x3d, 0x94, 0x37, 0x6b, 0x48, 0xb2,
52. 0xb9, 0x41, 0x53, 0xd6, 0x65, 0xef, 0x7a, 0x3d, 0xdc, 0x09, 0x17, 0x66, 0xb4, 0x05, 0x58, 0x8a,
53. 0x5d, 0x2f, 0x40, 0x4a, 0x91, 0x8a, 0xa5, 0xb7, 0x29, 0xfb, 0x37, 0x81, 0x71, 0x77, 0x50, 0x8d,
54. 0x34, 0x80, 0x7e, 0xab, 0xb9, 0xc8, 0xdc, 0xb7, 0x2c, 0x7e, 0xbc, 0xad, 0x7c, 0x14, 0x5c, 0xf6,
55. 0x90, 0x88, 0x0e, 0x0d, 0x50, 0x7a, 0x4e, 0xa6, 0x85, 0xe4, 0x2a, 0xe7, 0x67, 0x21, 0x53, 0xbb,
56. 0x73, 0xd5, 0x30, 0x78, 0xbd, 0x08, 0x2b, 0x42, 0x44, 0x3e, 0x5d, 0x2b, 0x2f, 0x09, 0x8e, 0x82,
57. 0xc3, 0x5b, 0x9e, 0xd8, 0x20, 0xc6, 0xb7, 0x42, 0xe5, 0xb3, 0x60, 0x0b, 0x9b, 0x01, 0x76, 0x26,
58. 0xf7, 0xc1, 0xf7, 0xe1, 0xd1, 0x46, 0xf7, 0x9c, 0x21, 0xfd, 0x66, 0xb7, 0x14, 0x1d, 0x89, 0xb5,
59. 0xd3, 0xa1, 0x4e, 0x57, 0x97, 0xe7, 0xe4, 0x63, 0x96, 0xe2, 0x6f, 0x10, 0x6a, 0xb7, 0x8e, 0x83,
60. 0x64, 0x22, 0x10, 0x02, 0x27, 0x87, 0x6d, 0xb6, 0x11, 0x51, 0xe9, 0xe6, 0x68, 0x1a, 0xc8, 0xd3,
61. 0x6b, 0x23, 0x33, 0x68, 0x66, 0xab, 0x4d, 0xf9, 0x92, 0x11, 0x67, 0x9d, 0x24, 0xee, 0x18, 0xa8,
62. 0x3c, 0x5a, 0xfe, 0x79, 0x76, 0x99, 0xeb, 0x9f, 0x19, 0x9d, 0x74, 0xee, 0x13, 0xd9, 0xb1, 0x7b,
63. 0x4e, 0xcf, 0x30, 0x05, 0xdb, 0x5a, 0x3e, 0x00, 0x7e, 0x0a, 0xed, 0x6f, 0xaf, 0x0d, 0x1b, 0xf3,
64. 0x61, 0x24, 0x06, 0xe7, 0xf2, 0x57, 0x72, 0xf8, 0x61, 0x4d, 0x5f, 0x00, 0x78, 0x1f, 0x4d, 0xc7,
65. 0x28, 0x5e, 0xc4, 0x9b, 0xed, 0xac, 0x4f, 0x16, 0xaf, 0x81, 0x85, 0x33, 0x16, 0xbd, 0x6a, 0xb9,
66. 0xb2, 0x8e, 0x25, 0xbc, 0xaf, 0xfd, 0xea, 0xb7, 0x20, 0x32, 0x15, 0x62, 0x77, 0x52, 0xa1, 0xf2,
67. 0xd0, 0x9d, 0x12, 0x4c, 0x85, 0x71, 0x08, 0x03, 0xa7, 0x94, 0x34, 0xb4, 0x96, 0x30, 0x82, 0x05,
68. 0x41, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x05, 0x32,
69. 0x04, 0x82, 0x05, 0x2e, 0x30, 0x82, 0x05, 0x2a, 0x30, 0x82, 0x05, 0x26, 0x06, 0x0b, 0x2a, 0x86,
70. 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x0a, 0x01, 0x02, 0xa0, 0x82, 0x04, 0xee, 0x30, 0x82, 0x04,
71. 0xea, 0x30, 0x1c, 0x06, 0x0a, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x03, 0x30,
72. 0x0e, 0x04, 0x08, 0x30, 0xee, 0xbd, 0x7c, 0xcb, 0xb5, 0xa5, 0x1b, 0x02, 0x02, 0x08, 0x00, 0x04,
73. 0x82, 0x04, 0xc8, 0x1e, 0xd0, 0x7f, 0x7e, 0x86, 0x1c, 0x6f, 0x0e, 0xac, 0x6c, 0xe3, 0x35, 0xcb,
74. 0xff, 0xe4, 0x84, 0x88, 0x97, 0x45, 0xf3, 0x48, 0xa9, 0x98, 0xeb, 0x74, 0x91, 0x53, 0x07, 0x7a,
75. 0xe4, 0x78, 0x89, 0x13, 0xe7, 0xce, 0xa3, 0xc5, 0xab, 0x2c, 0x16, 0xe5, 0x02, 0x64, 0xc6, 0xb5,
76. 0x11, 0x36, 0x69, 0x0b, 0x5f, 0x7e, 0x95, 0x27, 0x59, 0x9a, 0xac, 0x98, 0x12, 0x76, 0x39, 0x31,
77. 0xaa, 0x4f, 0x22, 0x55, 0x21, 0x71, 0x20, 0xeb, 0x4e, 0x5e, 0x2d, 0xd8, 0xab, 0xd9, 0x64, 0x38,
78. 0x13, 0x9a, 0x14, 0x48, 0x7f, 0x48, 0x05, 0xec, 0x49, 0x55, 0x80, 0x49, 0xaf, 0x4e, 0x29, 0xdf,
79. 0x4a, 0xfb, 0xa1, 0x20, 0x2f, 0x98, 0x35, 0xf7, 0x8f, 0xb9, 0x41, 0x8b, 0x00, 0x14, 0x23, 0x9a,
80. 0x43, 0xfe, 0x55, 0xfc, 0xe5, 0x57, 0x19, 0xa9, 0x74, 0x44, 0x1f, 0xdd, 0xc3, 0xc8, 0x9f, 0xfa,
81. 0x9f, 0x67, 0x93, 0xed, 0x79, 0x11, 0xe1, 0x4e, 0xed, 0xd6, 0x20, 0x82, 0xc8, 0x85, 0xdf, 0x4e,
82. 0xa0, 0xcd, 0xd8, 0x36, 0x37, 0x4f, 0x67, 0x9d, 0x84, 0x44, 0x14, 0xce, 0xc0, 0xc9, 0xa6, 0xbd,
83. 0x73, 0x06, 0x27, 0xb7, 0x16, 0x97, 0x8c, 0x61, 0xd9, 0x63, 0xb2, 0x56, 0x8d, 0x28, 0x9e, 0x2e,
84. 0xcf, 0xa3, 0xfe, 0x8d, 0xaa, 0xef, 0x69, 0x32, 0x7b, 0x32, 0xbe, 0xd5, 0x62, 0x2c, 0x2e, 0x7f,
85. 0x72, 0xdb, 0x3c, 0x4b, 0xe4, 0x76, 0xa3, 0xa9, 0xa1, 0x67, 0x84, 0x86, 0xea, 0x14, 0x15, 0x6c,
86. 0x74, 0xd2, 0xac, 0x0e, 0xe2, 0x54, 0x54, 0xd4, 0x31, 0xa3, 0x88, 0x66, 0x89, 0x31, 0x7b, 0xf7,
87. 0x3c, 0x92, 0xce, 0x3e, 0x86, 0xfb, 0x57, 0xc8, 0x65, 0xae, 0x85, 0x6d, 0x48, 0xf6, 0xe6, 0x37,
88. 0xeb, 0x77, 0xcf, 0x06, 0xd6, 0x9e, 0x54, 0xb4, 0xd8, 0x9a, 0x5f, 0xdd, 0xc5, 0xa5, 0x05, 0xa0,
89. 0x4b, 0xd1, 0x54, 0xab, 0x4f, 0xd0, 0x3e, 0x6b, 0x8f, 0x03, 0x66, 0xd4, 0xe2, 0x90, 0xea, 0x2d,
90. 0x9b, 0x6a, 0x2b, 0xc4, 0x7b, 0x9d, 0xf1, 0xb5, 0x22, 0xdf, 0x86, 0xc2, 0xfd, 0x13, 0x0a, 0x69,
91. 0x29, 0x59, 0xe9, 0x45, 0xcd, 0xdf, 0xcd, 0xa5, 0x71, 0x7e, 0x70, 0xc3, 0x60, 0x9e, 0x47, 0x5d,
92. 0xd4, 0x6c, 0xcc, 0x15, 0x51, 0x23, 0x5b, 0x4e, 0xee, 0x72, 0x80, 0x49, 0xd6, 0xac, 0x89, 0x16,
93. 0x65, 0xf4, 0x95, 0x57, 0x19, 0x13, 0xab, 0x9c, 0x08, 0xe8, 0xdf, 0x0a, 0xe2, 0x39, 0xfc, 0xff,
94. 0x42, 0x02, 0xac, 0xaf, 0xf1, 0xb6, 0x56, 0xef, 0x75, 0x60, 0x2f, 0xc2, 0x5d, 0xef, 0xf5, 0x79,
95. 0xb5, 0x46, 0xa0, 0xb5, 0x03, 0x67, 0xef, 0x78, 0x3d, 0x49, 0xd0, 0xc5, 0x0e, 0xff, 0x42, 0x72,
96. 0x02, 0x86, 0x99, 0x93, 0xaa, 0xa3, 0x9e, 0x2c, 0xc7, 0xec, 0xa2, 0xdf, 0x25, 0x4e, 0x28, 0x81,
97. 0x82, 0x3e, 0x29, 0xd3, 0x37, 0xfd, 0x32, 0xf4, 0x85, 0x46, 0x42, 0xb9, 0x94, 0x44, 0x8a, 0xbf,
98. 0xd9, 0x14, 0xcb, 0xb6, 0xd3, 0xc5, 0xe7, 0x6b, 0x28, 0x70, 0xc3, 0x9c, 0xc2, 0x93, 0x9d, 0x2f,
99. 0xab, 0xd6, 0xb2, 0x19, 0x28, 0x9a, 0xda, 0x0d, 0x90, 0x5b, 0xba, 0x64, 0x6f, 0xcc, 0x11, 0xef,
100. 0x6c, 0x88, 0x18, 0x4f, 0x86, 0x6e, 0xed, 0xcf, 0xde, 0x0d, 0xec, 0xe2, 0x12, 0xc3, 0x89, 0x0a,
101. 0x3f, 0xbb, 0x3d, 0x8c, 0x8f, 0xa9, 0x40, 0xe6, 0xf8, 0xd1, 0x1a, 0x9a, 0x7e, 0x8a, 0xd7, 0x7b,
102. 0x56, 0xf4, 0x5d, 0x80, 0x64, 0xd5, 0x88, 0x86, 0x85, 0x18, 0x30, 0x5d, 0x64, 0x04, 0xb3, 0xc2,
103. 0xc7, 0x80, 0xda, 0x3e, 0xc4, 0xd6, 0xf6, 0xc4, 0x95, 0x56, 0xd5, 0xad, 0x82, 0x86, 0xcc, 0x1a,
104. 0x05, 0x69, 0x06, 0x08, 0x5b, 0x19, 0xea, 0x10, 0xc5, 0xcd, 0x67, 0x93, 0xab, 0x0f, 0xe3, 0xba,
105. 0xb0, 0x0d, 0xac, 0x99, 0x0d, 0x35, 0x6f, 0xe5, 0x41, 0xb2, 0x7c, 0x87, 0x91, 0x6c, 0xe2, 0x75,
106. 0x9b, 0x64, 0x62, 0x06, 0x2a, 0x8b, 0xd9, 0x4d, 0x23, 0xcd, 0x2b, 0xef, 0xf5, 0x61, 0x82, 0x8e,
107. 0x3f, 0xf6, 0x2b, 0xe1, 0x6f, 0xcf, 0xbd, 0xaa, 0x07, 0x97, 0x49, 0x4e, 0x02, 0x9d, 0xa5, 0x9e,
108. 0xc5, 0xd7, 0x8b, 0xd3, 0xe1, 0xd9, 0x35, 0x96, 0x9d, 0x1f, 0xa2, 0xf6, 0x91, 0xee, 0xd1, 0x3b,
109. 0xa8, 0xfe, 0x4d, 0xeb, 0xf9, 0xfc, 0xe4, 0xab, 0x60, 0xb7, 0x86, 0x9d, 0x2a, 0x35, 0xb0, 0x00,
110. 0xd4, 0x3c, 0x2a, 0x7e, 0x6d, 0x65, 0x5f, 0xf3, 0x7c, 0x23, 0x57, 0x52, 0x2a, 0x8c, 0x5b, 0x36,
111. 0x74, 0xb7, 0x61, 0x49, 0xf0, 0xdf, 0xcf, 0x8a, 0x28, 0xc5, 0x8d, 0xbc, 0x20, 0xcc, 0xac, 0x86,
112. 0x20, 0xd8, 0x2d, 0x86, 0x99, 0xf5, 0xf0, 0xdb, 0xed, 0x8d, 0xf9, 0xd7, 0x4e, 0xa8, 0xde, 0x84,
113. 0x35, 0x50, 0xc1, 0x7c, 0xbd, 0xdf, 0xc2, 0x24, 0x1a, 0x49, 0x24, 0x9a, 0x37, 0x93, 0xca, 0x2d,
114. 0x73, 0x47, 0x8f, 0x83, 0xed, 0x4d, 0xca, 0xf8, 0xf0, 0xd3, 0x9b, 0xe0, 0x4b, 0x3b, 0xf1, 0x86,
115. 0xeb, 0x78, 0x7b, 0x42, 0xa1, 0xb9, 0x36, 0x15, 0xde, 0x63, 0xab, 0x8b, 0x8b, 0x5d, 0xa2, 0x92,
116. 0x10, 0x95, 0xdf, 0xda, 0xd7, 0xba, 0xa0, 0x26, 0xb9, 0xdc, 0x83, 0xeb, 0xdc, 0xd2, 0x1f, 0xf1,
117. 0xb1, 0x8d, 0x21, 0x51, 0x71, 0x59, 0x0e, 0xe8, 0x7e, 0xf1, 0x53, 0x08, 0x98, 0x79, 0x05, 0x3b,
118. 0x22, 0xf1, 0xda, 0x07, 0x0d, 0xf7, 0x89, 0x5e, 0xc4, 0x62, 0x8c, 0xf9, 0x19, 0xc8, 0xbc, 0xa4,
119. 0x0c, 0x6f, 0x41, 0x34, 0x56, 0x22, 0x6b, 0xe6, 0xee, 0x7c, 0x4a, 0xd9, 0x26, 0x8c, 0x56, 0x12,
120. 0xf3, 0x03, 0x12, 0x1c, 0x5b, 0x8d, 0x64, 0x5c, 0x1c, 0xb6, 0x0f, 0x93, 0xaf, 0xb1, 0x67, 0x6f,
121. 0x13, 0xdd, 0xe3, 0xcf, 0x0e, 0xe6, 0x06, 0xf3, 0xb2, 0xbc, 0x99, 0xf5, 0xb0, 0xd7, 0xe9, 0x7e,
122. 0xb0, 0x6a, 0xb9, 0xb5, 0xda, 0xcf, 0x88, 0xf1, 0xc5, 0x58, 0x54, 0x05, 0x5c, 0x9d, 0x79, 0xc2,
123. 0xcd, 0xbb, 0xc6, 0xf2, 0x69, 0xa9, 0xe3, 0x4e, 0x05, 0x0d, 0x02, 0xb6, 0x4d, 0x8e, 0x7d, 0x60,
124. 0x8e, 0xda, 0x4d, 0x28, 0xd2, 0xec, 0x8a, 0x11, 0xe3, 0xe7, 0x17, 0x20, 0x07, 0x7b, 0xfc, 0x9b,
125. 0x4e, 0xf7, 0x79, 0xf5, 0x0a, 0x6e, 0xd1, 0x1e, 0x7b, 0x83, 0x66, 0x5e, 0x1b, 0x9d, 0x36, 0x32,
126. 0x89, 0xf6, 0x72, 0xa5, 0x58, 0x54, 0x42, 0xba, 0x90, 0xf3, 0xbb, 0x05, 0x46, 0xa4, 0x91, 0x1c,
127. 0xdb, 0xab, 0xf3, 0x68, 0x56, 0x7a, 0xd3, 0xff, 0x3f, 0x9f, 0xc5, 0x4a, 0x47, 0xbd, 0x89, 0x46,
128. 0xf6, 0x94, 0x3a, 0x94, 0xd4, 0x30, 0xd3, 0xae, 0x0d, 0x99, 0x95, 0xf7, 0x75, 0xfe, 0x14, 0x10,
129. 0x9e, 0xed, 0x21, 0x0f, 0x0d, 0x54, 0x7d, 0x54, 0xc5, 0x80, 0x21, 0x4d, 0xf2, 0xaf, 0x67, 0xaf,
130. 0x8a, 0x76, 0x9e, 0x34, 0x32, 0x74, 0x89, 0x2a, 0x32, 0xf9, 0x48, 0x20, 0x90, 0xe6, 0x4a, 0xa3,
131. 0x7f, 0xf2, 0x2a, 0x51, 0x22, 0x93, 0xe5, 0xdd, 0x59, 0xb3, 0x83, 0xa8, 0x47, 0xf5, 0x6b, 0x38,
132. 0x24, 0xc2, 0xac, 0x2d, 0x03, 0xda, 0xb1, 0x17, 0x19, 0xe0, 0x38, 0x2c, 0xb3, 0xa6, 0x4c, 0x8e,
133. 0xae, 0x63, 0xa7, 0xae, 0x96, 0xb1, 0x07, 0x8c, 0x8f, 0x6a, 0x08, 0x32, 0x15, 0x1f, 0x33, 0x97,
134. 0x21, 0x3b, 0x51, 0x70, 0xc5, 0x1f, 0xa6, 0xa3, 0x8a, 0xd0, 0x8f, 0x0b, 0xda, 0x64, 0xab, 0xbe,
135. 0xee, 0x4b, 0x14, 0xfd, 0x32, 0x87, 0x9e, 0xa7, 0x19, 0x75, 0xc9, 0xaa, 0xd3, 0xed, 0xa7, 0xa0,
136. 0x01, 0xe7, 0xa0, 0xe5, 0x28, 0xdd, 0x3b, 0x7c, 0x49, 0xe4, 0x24, 0x7d, 0x92, 0x86, 0x25, 0x03,
137. 0xb3, 0x66, 0x04, 0xf3, 0xa1, 0x40, 0x11, 0x35, 0x3a, 0x1d, 0xbf, 0x1c, 0x02, 0x83, 0x3d, 0x37,
138. 0x51, 0x88, 0xa3, 0x2b, 0x10, 0x8c, 0x8e, 0x10, 0xdd, 0xdc, 0xef, 0xa4, 0xe9, 0x14, 0x77, 0xb6,
139. 0x8e, 0x75, 0xb6, 0x8e, 0xea, 0xaa, 0x57, 0x16, 0x1f, 0xb0, 0x0c, 0xbc, 0x44, 0xed, 0x92, 0x94,
140. 0x9a, 0xb4, 0xf3, 0x31, 0x64, 0x02, 0x5c, 0xa1, 0x51, 0x63, 0x39, 0x42, 0x74, 0x7a, 0x1d, 0xf2,
141. 0xf5, 0x92, 0x50, 0xf1, 0x5a, 0x8a, 0xde, 0xb3, 0x4e, 0xf1, 0x6e, 0x67, 0xd9, 0x5b, 0x00, 0xa7,
142. 0xd1, 0x90, 0x58, 0x36, 0xc4, 0x15, 0x80, 0xbb, 0xa5, 0xbb, 0x98, 0xc0, 0x8a, 0x9b, 0x17, 0x35,
143. 0x36, 0x3b, 0x62, 0x0f, 0x29, 0xcd, 0xe9, 0x04, 0x0e, 0x9d, 0xca, 0x43, 0x04, 0xdf, 0x17, 0x49,
144. 0xbf, 0xb6, 0x7a, 0x7a, 0x3c, 0xdb, 0x0d, 0x6d, 0xd5, 0x89, 0xb9, 0x69, 0x94, 0xd8, 0xb2, 0xd6,
145. 0x38, 0x8a, 0xcc, 0x78, 0x44, 0x40, 0x63, 0x9f, 0x1e, 0x0e, 0x40, 0x33, 0x51, 0xd3, 0x65, 0xf8,
146. 0xf1, 0x42, 0x06, 0x75, 0x84, 0xe7, 0xb1, 0xe9, 0xd6, 0xa4, 0x5e, 0x7f, 0xb0, 0x48, 0x6f, 0x80,
147. 0x92, 0xf8, 0xfc, 0x2a, 0xdb, 0x18, 0x97, 0xe5, 0xe7, 0xc7, 0x46, 0xb6, 0x59, 0x8c, 0x3a, 0x09,
148. 0x91, 0xc1, 0x49, 0x55, 0xf9, 0xf3, 0x87, 0x19, 0xdc, 0x72, 0x56, 0xd3, 0x20, 0x5e, 0xc5, 0x3d,
149. 0xfb, 0x19, 0xea, 0x6a, 0xdf, 0x09, 0xb2, 0x8f, 0xb6, 0xdd, 0x26, 0x31, 0x25, 0x30, 0x23, 0x06,
150. 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x3b, 0xd2,
151. 0xb3, 0x51, 0x4c, 0x57, 0xd0, 0xca, 0x34, 0xa4, 0xf0, 0x06, 0xdd, 0xe9, 0x76, 0x08, 0xdb, 0x7b,
152. 0x3a, 0xb0, 0x30, 0x31, 0x30, 0x21, 0x30, 0x09, 0x06, 0x05, 0x2b, 0x0e, 0x03, 0x02, 0x1a, 0x05,
153. 0x00, 0x04, 0x14, 0x8e, 0x7f, 0x87, 0x67, 0x78, 0x64, 0x93, 0x36, 0x35, 0xe5, 0x93, 0x9d, 0xac,
154. 0x61, 0x09, 0x4f, 0xdc, 0x95, 0xd7, 0x4f, 0x04, 0x08, 0x23, 0xc2, 0xc0, 0xc6, 0x8d, 0x5f, 0x70,
155. 0x7e, 0x02, 0x02, 0x08, 0x00]);

157. let p12: cert.Pkcs12Data = await cert.parsePkcs12(p12_cert, '123456');
158. console.info('parsePKCS12 result: success.');
159. if (p12.privateKey) {
160. console.info('privateKey:' + p12.privateKey.toString());
161. }
162. if (p12.cert) {
163. console.info('cert:' + p12.cert.toString());
164. }
165. if (p12.otherCerts && Array.isArray(p12.otherCerts)) {
166. console.info('otherCerts counts:', p12.otherCerts.length);
167. p12.otherCerts.forEach((cert, idx) => {
168. console.info(`otherCerts[${idx}]:\n${cert.toString()}`);
169. });
170. } else {
171. console.info('otherCerts is empty or not an array.');
172. }
173. } catch (err) {
174. console.error(`parsePKCS12 failed: errCode: ${err.code}, errMsg: ${err.message}`);
175. }
176. }
```

## cert.createPkcs1221+

PhonePC/2in1TabletTVWearable

createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>

表示创建Pkcs12数据。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [Pkcs12Data](js-apis-cert.md#pkcs12data18) | 是 | 要打包的Pkcs12数据对象。 |
| config | [Pkcs12CreationConfig](js-apis-cert.md#pkcs12creationconfig21) | 是 | Pkcs12文件的创建配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象。表示创建的Pkcs12文件，DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The password is too short or too long;  2. The private key does not match the certificate;  3. Invalid encryption algorithm parameters. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let priKey = '-----BEGIN PRIVATE KEY-----\n' +
4. 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
5. 'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
6. 'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
7. '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
8. 'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
9. 'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
10. 'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
11. '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
12. 'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
13. 'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
14. 'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
15. 'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
16. 'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
17. 'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
18. 'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
19. 'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
20. 'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
21. 'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
22. 'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
23. 'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
24. '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
25. 'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
26. 'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
27. 'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
28. 'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
29. 'a20rj9HG4sb8tUIHPBv0dgY=\n' +
30. '-----END PRIVATE KEY-----\n';

32. let othercert = '-----BEGIN CERTIFICATE-----\n' +
33. 'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
34. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
35. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
36. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
37. 'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
38. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
39. 'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
40. 'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
41. 'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
42. 'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
43. 'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
44. 'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
45. '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
46. 'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
47. 'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
48. 'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
49. 'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
50. '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
51. 'ZcLXS+9LpW3a\n' +
52. '-----END CERTIFICATE-----\n';

54. let certData = '-----BEGIN CERTIFICATE-----\n' +
55. 'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
56. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
57. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
58. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
59. 'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
60. 'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
61. 'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
62. 'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
63. 'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
64. '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
65. 'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
66. 'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
67. 'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
68. 'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
69. 'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
70. '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
71. 'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
72. 'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
73. 'nZSOvPxc0c2O34k=\n' +
74. '-----END CERTIFICATE-----\n';

76. // string转Uint8Array。
77. function stringToUint8Array(str: string): Uint8Array {
78. let arr: number[] = [];
79. for (let i = 0, j = str.length; i < j; i++) {
80. arr.push(str.charCodeAt(i));
81. }
82. return new Uint8Array(arr);
83. }

85. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
86. // 证书二进制数据，需业务自行赋值。
87. let encodingBlob: cert.EncodingBlob = {
88. data: stringToUint8Array(certData),
89. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
90. encodingFormat: cert.EncodingFormat.FORMAT_PEM
91. };

93. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
94. try {
95. x509Cert = await cert.createX509Cert(encodingBlob);
96. } catch (err) {
97. console.error(`createX509Cert failed: errCode: ${err.code}, errMsg: ${err.message}`);
98. }
99. return x509Cert;
100. }

102. async function doTestCreatePkcs12() {
103. const caCert = await createX509Cert(othercert);
104. const x509Cert = await createX509Cert(certData);

106. let data: cert.Pkcs12Data = {
107. privateKey: priKey,
108. cert: x509Cert,
109. otherCerts: [caCert]
110. }

112. let keyParam: cert.PbesParams = {
113. saltLen: 16,
114. iterations: 2048,
115. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_192_CBC
116. }

118. let certParam: cert.PbesParams = {
119. saltLen: 16,
120. iterations: 2048,
121. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_256_CBC
122. }

124. let config: cert.Pkcs12CreationConfig = {
125. password: '123456',
126. keyEncParams: keyParam,
127. encryptCert: true,
128. certEncParams: certParam,
129. macSaltLen: 16,
130. macIterations: 2048,
131. macDigestAlgorithm: cert.Pkcs12MacDigestAlgorithm.SHA384
132. }
133. try {
134. let p12 = await cert.createPkcs12(data, config);
135. console.info('createPkcs12 result: success, p12 = ' + p12);
136. } catch (err) {
137. console.error(`createPkcs12 failed: errCode: ${err.code}, errMsg: ${err.message}`);
138. }
139. }
```

## cert.createPkcs1221+

PhonePC/2in1TabletTVWearable

createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array

表示创建Pkcs12数据，同步返回结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [Pkcs12Data](js-apis-cert.md#pkcs12data18) | 是 | 要打包的P12数据对象。 |
| config | [Pkcs12CreationConfig](js-apis-cert.md#pkcs12creationconfig21) | 是 | P12文件的创建配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 表示创建的P12文件，DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The password is too short or too long;  2. The private key does not match the certificate;  3. Invalid encryption algorithm parameters. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let priKey = '-----BEGIN PRIVATE KEY-----\n' +
4. 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
5. 'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
6. 'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
7. '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
8. 'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
9. 'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
10. 'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
11. '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
12. 'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
13. 'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
14. 'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
15. 'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
16. 'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
17. 'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
18. 'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
19. 'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
20. 'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
21. 'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
22. 'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
23. 'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
24. '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
25. 'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
26. 'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
27. 'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
28. 'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
29. 'a20rj9HG4sb8tUIHPBv0dgY=\n' +
30. '-----END PRIVATE KEY-----\n';

32. let othercert = '-----BEGIN CERTIFICATE-----\n' +
33. 'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
34. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
35. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
36. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
37. 'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
38. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
39. 'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
40. 'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
41. 'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
42. 'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
43. 'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
44. 'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
45. '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
46. 'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
47. 'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
48. 'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
49. 'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
50. '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
51. 'ZcLXS+9LpW3a\n' +
52. '-----END CERTIFICATE-----\n';

54. let certData = '-----BEGIN CERTIFICATE-----\n' +
55. 'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
56. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
57. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
58. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
59. 'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
60. 'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
61. 'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
62. 'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
63. 'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
64. '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
65. 'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
66. 'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
67. 'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
68. 'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
69. 'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
70. '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
71. 'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
72. 'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
73. 'nZSOvPxc0c2O34k=\n' +
74. '-----END CERTIFICATE-----\n';

76. // string转Uint8Array。
77. function stringToUint8Array(str: string): Uint8Array {
78. let arr: number[] = [];
79. for (let i = 0, j = str.length; i < j; i++) {
80. arr.push(str.charCodeAt(i));
81. }
82. return new Uint8Array(arr);
83. }

85. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
86. // 证书二进制数据，需业务自行赋值。
87. let encodingBlob: cert.EncodingBlob = {
88. data: stringToUint8Array(certData),
89. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
90. encodingFormat: cert.EncodingFormat.FORMAT_PEM
91. };

93. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
94. try {
95. x509Cert = await cert.createX509Cert(encodingBlob);
96. } catch (err) {
97. console.error(`createX509Cert failed: errCode: ${err.code}, errMsg: ${err.message}`);
98. }
99. return x509Cert;
100. }

102. async function doTestCreatePkcs12Sync() {
103. const caCert = await createX509Cert(othercert);
104. const x509Cert = await createX509Cert(certData);

106. let data: cert.Pkcs12Data = {
107. privateKey: priKey,
108. cert: x509Cert,
109. otherCerts: [caCert]
110. }

112. let keyParam: cert.PbesParams = {
113. saltLen: 16,
114. iterations: 2048,
115. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_192_CBC
116. }

118. let certParam: cert.PbesParams = {
119. saltLen: 16,
120. iterations: 2048,
121. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_256_CBC
122. }

124. let config: cert.Pkcs12CreationConfig = {
125. password: '123456',
126. keyEncParams: keyParam,
127. encryptCert: true,
128. certEncParams: certParam,
129. macSaltLen: 16,
130. macIterations: 2048,
131. macDigestAlgorithm: cert.Pkcs12MacDigestAlgorithm.SHA384
132. }
133. try {
134. let p12 = cert.createPkcs12Sync(data, config);
135. console.info('createPkcs12Sync result: success, p12 = ' + p12);
136. } catch (err) {
137. console.error(`createPkcs12Sync failed: errCode: ${err.code}, errMsg: ${err.message}`);
138. }
139. }
```

## cert.createTrustAnchorsWithKeyStore12+

PhonePC/2in1TabletTVWearable

createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<[X509TrustAnchor](js-apis-cert.md#x509trustanchor11)>>

表示从P12文件中读取ca证书来构造[TrustAnchor](js-apis-cert.md#x509trustanchor11)对象数组。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | P12文件，DER格式。 |
| pwd | string | 是 | P12文件的密码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509TrustAnchor](js-apis-cert.md#x509trustanchor11)>> | 表示X509TrustAnchor对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. cert.createTrustAnchorsWithKeyStore(
6. new Uint8Array([0x30, 0x82, 0x07, 0x5C, 0x02, 0x01, 0x03, 0x30, 0x82, 0x07, 0x12, 0x06, 0x09, 0x2A, 0x86, 0x48,
7. 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x01, 0xA0, 0x82, 0x07, 0x03, 0x04, 0x82, 0x06, 0xFF, 0x30, 0x82, 0x06, 0xFB, 0x30,
8. 0x82, 0x05, 0xB2, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x06, 0xA0, 0x82, 0x05, 0xA3, 0x30,
9. 0x82, 0x05, 0x9F, 0x02, 0x01, 0x00, 0x30, 0x82, 0x05, 0x98, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01,
10. 0x07, 0x01, 0x30, 0x57, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0D, 0x30, 0x4A, 0x30, 0x29,
11. 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0C, 0x30, 0x1C, 0x04, 0x08, 0xA9, 0x1C, 0x1B, 0x19,
12. 0x36, 0xDE, 0xD4, 0x20, 0x02, 0x02, 0x08, 0x00, 0x30, 0x0C, 0x06, 0x08, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x02,
13. 0x09, 0x05, 0x00, 0x30, 0x1D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x01, 0x2A, 0x04, 0x10, 0x7D,
14. 0xE5, 0x23, 0x96, 0x18, 0x8B, 0xF4, 0xBC, 0x9F, 0x4E, 0xE8, 0xE9, 0xAA, 0x52, 0x18, 0x39, 0x80, 0x82, 0x05, 0x30,
15. 0x02, 0x2D, 0x59, 0xA9, 0x96, 0x5A, 0xFE, 0x20, 0x18, 0xB2, 0x25, 0xEA, 0xFC, 0x86, 0x0F, 0xA8, 0x3C, 0x2B, 0x26,
16. 0x2F, 0x44, 0x6E, 0xF3, 0x15, 0xB7, 0x94, 0xE4, 0x43, 0xEE, 0xE6, 0xC3, 0xBB, 0x3C, 0x9E, 0x60, 0x08, 0xF8, 0x15,
17. 0x61, 0x44, 0xD0, 0xEA, 0xD5, 0x6D, 0x1A, 0x3B, 0x9F, 0x4E, 0x2A, 0x1E, 0xBB, 0xB9, 0x4E, 0x15, 0x43, 0xB8, 0x68,
18. 0xDB, 0x1A, 0x4E, 0x41, 0xBA, 0x29, 0x8E, 0x75, 0xEB, 0x12, 0xC1, 0xF0, 0x4B, 0x0D, 0x13, 0xB2, 0xC2, 0x48, 0x6F,
19. 0xC4, 0xC4, 0x82, 0xF2, 0x26, 0xD4, 0x3D, 0x1F, 0x42, 0x7D, 0x67, 0xB0, 0x37, 0x55, 0x9E, 0xD9, 0x46, 0x99, 0x98,
20. 0xB4, 0xE7, 0x4B, 0x07, 0x08, 0x3F, 0xD3, 0x96, 0x9A, 0xC5, 0xDA, 0x37, 0x74, 0x08, 0x5D, 0x3B, 0x06, 0x8A, 0x16,
21. 0x6D, 0x81, 0x63, 0x01, 0x83, 0x94, 0xDA, 0x1B, 0x0E, 0x04, 0xCE, 0x18, 0xF0, 0x51, 0x22, 0xD8, 0x2D, 0xF1, 0x69,
22. 0x0C, 0xCB, 0xC9, 0x51, 0x17, 0x07, 0x1F, 0x2B, 0xCF, 0x74, 0x26, 0xD7, 0x73, 0xB3, 0x2D, 0xF2, 0x82, 0xF0, 0x38,
23. 0x5B, 0x8A, 0x8F, 0xCD, 0x84, 0x69, 0x40, 0x59, 0xCE, 0xB3, 0x39, 0xFE, 0xF6, 0xB7, 0x24, 0x89, 0x34, 0xFF, 0xF4,
24. 0x40, 0x50, 0x06, 0x4D, 0xC6, 0x13, 0x82, 0xAF, 0x7F, 0x84, 0xB1, 0x67, 0x3C, 0x89, 0xBB, 0x5D, 0x32, 0xC3, 0xA6,
25. 0xF1, 0x7D, 0xF5, 0x72, 0x68, 0x75, 0xCE, 0x69, 0xAB, 0x6C, 0x32, 0xDA, 0x16, 0x3B, 0xC4, 0xCA, 0x47, 0x45, 0xE9,
26. 0x59, 0x1E, 0xB1, 0x70, 0xDA, 0x8A, 0x00, 0x69, 0x80, 0x40, 0xCA, 0x60, 0xE6, 0x07, 0x16, 0xF0, 0xA2, 0xF9, 0x12,
27. 0x7D, 0x09, 0x43, 0x66, 0x46, 0x78, 0x35, 0xA6, 0x94, 0x35, 0x60, 0x82, 0xFC, 0xB8, 0x5E, 0x39, 0xE7, 0xA1, 0x22,
28. 0xAD, 0xCC, 0x6F, 0x5E, 0xCE, 0x01, 0x6B, 0xA1, 0xDD, 0xE5, 0xDD, 0x79, 0x9B, 0xA1, 0x28, 0xC4, 0x03, 0x84, 0x8D,
29. 0x6C, 0x07, 0xD4, 0xFE, 0x57, 0xFB, 0x89, 0x3F, 0x43, 0x44, 0x69, 0xF1, 0x9E, 0x53, 0x6C, 0x11, 0x11, 0x96, 0x79,
30. 0xE4, 0xB8, 0x3B, 0x49, 0x2E, 0xF6, 0x3B, 0xC5, 0x6C, 0x76, 0x21, 0x22, 0x15, 0x85, 0x77, 0x8A, 0xDD, 0xD2, 0x43,
31. 0x85, 0x73, 0x39, 0x77, 0x9F, 0xFA, 0x8F, 0xCF, 0xCB, 0xEA, 0x62, 0xBD, 0x5C, 0x66, 0x45, 0xCD, 0xB0, 0xCA, 0x42,
32. 0xCC, 0xB9, 0xCF, 0xE3, 0x84, 0x63, 0x9F, 0x63, 0xCE, 0x49, 0xE9, 0x74, 0x26, 0xCC, 0x26, 0x78, 0xCE, 0x9F, 0x4E,
33. 0x38, 0xA2, 0x9C, 0xEB, 0x75, 0xC5, 0x33, 0x6B, 0x00, 0x83, 0x85, 0xA3, 0x0F, 0xE7, 0xE1, 0x11, 0xA6, 0x48, 0xDC,
34. 0xEF, 0x0C, 0x05, 0xB3, 0xDE, 0x94, 0xB9, 0x69, 0xCB, 0x27, 0x09, 0xAB, 0x27, 0xD8, 0x06, 0xED, 0x25, 0xBC, 0xA6,
35. 0x2E, 0xB7, 0xF9, 0x2E, 0xAD, 0x84, 0x1D, 0xDD, 0x73, 0xD8, 0xC0, 0x46, 0x8A, 0xFE, 0x9A, 0xDF, 0x07, 0xE1, 0x33,
36. 0xE2, 0x1C, 0x37, 0x6A, 0x8E, 0xA2, 0x91, 0x0B, 0xD7, 0x76, 0xEF, 0x3C, 0x87, 0x4A, 0x53, 0x84, 0xFA, 0xFA, 0xC5,
37. 0x71, 0x76, 0xC0, 0x75, 0x70, 0x67, 0x67, 0x71, 0x9D, 0x8B, 0x81, 0x6F, 0x68, 0xC5, 0xB1, 0xFC, 0xA3, 0x59, 0xB5,
38. 0xD0, 0x03, 0x56, 0xE7, 0x89, 0x03, 0xD7, 0x99, 0xDE, 0x66, 0x33, 0xFA, 0x53, 0x50, 0x5F, 0xB4, 0x9D, 0xB3, 0x90,
39. 0x8F, 0x57, 0x20, 0xF0, 0x8B, 0xDB, 0x73, 0xCA, 0xA4, 0x71, 0x61, 0x67, 0x6A, 0x6D, 0xA5, 0xCA, 0x88, 0xD4, 0xCC,
40. 0x82, 0x34, 0xC9, 0x3E, 0x10, 0x10, 0x57, 0xD1, 0x08, 0x96, 0x80, 0x09, 0xA8, 0xBB, 0x6F, 0x53, 0x8F, 0xFD, 0x87,
41. 0xCF, 0x73, 0xFC, 0xE1, 0x3A, 0x92, 0x2E, 0x78, 0x66, 0xFB, 0x86, 0x5D, 0x62, 0xE0, 0xC4, 0x58, 0x55, 0x3F, 0xA4,
42. 0xEA, 0xA1, 0xBE, 0x5B, 0x5E, 0x8E, 0x46, 0x50, 0x5E, 0x7C, 0x01, 0xD6, 0x63, 0xAA, 0x6F, 0xD5, 0xFD, 0xAF, 0xC5,
43. 0x1D, 0xB3, 0x90, 0x9C, 0xD8, 0x5F, 0x8D, 0xF2, 0x81, 0xEB, 0xBF, 0xA1, 0xDE, 0xB7, 0x9D, 0xCD, 0x24, 0x82, 0x06,
44. 0x0B, 0x63, 0xE6, 0xBF, 0x57, 0x51, 0xF0, 0xB6, 0xE9, 0x7F, 0xAA, 0x7B, 0x10, 0xBD, 0xCD, 0x85, 0x41, 0xE0, 0xD7,
45. 0xF1, 0x53, 0xB7, 0xF8, 0x46, 0x91, 0x9E, 0x8D, 0x4B, 0xCB, 0x28, 0x35, 0x40, 0x37, 0x1E, 0x83, 0x64, 0x6A, 0x70,
46. 0x01, 0x9D, 0xBF, 0xF1, 0x0E, 0xB6, 0x2E, 0x7A, 0xB7, 0x8F, 0x0F, 0x8C, 0x69, 0xD6, 0xF2, 0xD1, 0xF6, 0x1E, 0xCD,
47. 0x08, 0xA8, 0xD4, 0x1B, 0xCB, 0x38, 0xEA, 0x26, 0x37, 0x5C, 0x60, 0x3A, 0x38, 0x5B, 0x12, 0x1D, 0x00, 0x7B, 0xEC,
48. 0xCE, 0xFB, 0x89, 0x23, 0x8A, 0x11, 0xE1, 0x1B, 0xDE, 0x54, 0x91, 0x6A, 0x26, 0x22, 0xD0, 0x1C, 0x2E, 0xBA, 0xD0,
49. 0x92, 0x87, 0xDA, 0xF0, 0x93, 0xBB, 0x3A, 0x2C, 0x52, 0xFB, 0xB2, 0xA9, 0xA8, 0x92, 0x19, 0xE3, 0x19, 0xDC, 0xB0,
50. 0x0E, 0xC5, 0xE7, 0x9D, 0xFB, 0xF9, 0xA3, 0x23, 0x32, 0xD0, 0x4E, 0x2C, 0x05, 0x2D, 0x76, 0xDB, 0x93, 0x53, 0x5B,
51. 0x0E, 0x2A, 0xA3, 0xDD, 0x5F, 0xD3, 0x1A, 0x3B, 0x1E, 0x1F, 0x26, 0x88, 0x43, 0xAD, 0x10, 0x1F, 0xA9, 0xC4, 0xF9,
52. 0x1F, 0xCD, 0xA5, 0xD2, 0xDC, 0x24, 0x95, 0x1D, 0xE7, 0x57, 0xE1, 0x02, 0x0A, 0x20, 0xEA, 0x6A, 0x78, 0x4E, 0x96,
53. 0xE2, 0xE5, 0x6D, 0x6F, 0xFD, 0x81, 0x7B, 0x61, 0x85, 0xA3, 0x3D, 0xC5, 0x7B, 0xEF, 0xAE, 0x58, 0xA2, 0xDB, 0x91,
54. 0x73, 0xDB, 0x47, 0x8E, 0xD1, 0x7D, 0xD7, 0x8F, 0x56, 0x06, 0x28, 0x8C, 0x78, 0x73, 0x02, 0x65, 0xB0, 0x16, 0x4B,
55. 0xE6, 0xA3, 0xD7, 0x06, 0x7C, 0xEA, 0x7D, 0xE2, 0xAE, 0xBB, 0xE5, 0xD2, 0xEB, 0xF0, 0x91, 0x71, 0x7C, 0xBC, 0xA6,
56. 0x1A, 0xE8, 0x9F, 0xD3, 0xA9, 0x3C, 0x5D, 0x60, 0xCF, 0x59, 0x26, 0x46, 0x45, 0xF2, 0x7F, 0x85, 0x6B, 0xE7, 0xC2,
57. 0x58, 0x52, 0x90, 0x12, 0x07, 0xBA, 0xE6, 0xB8, 0xE5, 0xD7, 0x24, 0x93, 0xD5, 0x6E, 0xB1, 0x74, 0x6C, 0xAA, 0xA0,
58. 0x60, 0xBF, 0xF3, 0x32, 0x41, 0x0B, 0xA2, 0x01, 0x84, 0x0D, 0x83, 0xE4, 0x43, 0xD1, 0xBA, 0xC1, 0x92, 0x84, 0x26,
59. 0xF8, 0xF2, 0x77, 0x20, 0x1B, 0xF2, 0x8F, 0x00, 0x69, 0x18, 0x2F, 0x6C, 0xA8, 0x58, 0xB5, 0x5D, 0xFA, 0x27, 0xD2,
60. 0x38, 0xD2, 0x49, 0x6E, 0xDF, 0x55, 0x79, 0xAF, 0x1C, 0x44, 0xDA, 0x5A, 0xD7, 0x44, 0x53, 0x50, 0x8B, 0x77, 0x70,
61. 0x4D, 0x91, 0xEC, 0x07, 0xA5, 0x64, 0x21, 0x3C, 0x31, 0x09, 0x68, 0x65, 0xB4, 0xFA, 0xBE, 0x23, 0xF9, 0xDF, 0x77,
62. 0x46, 0xA2, 0x9A, 0x5D, 0xE3, 0xBE, 0x1E, 0xE3, 0x84, 0xEF, 0xAE, 0x7D, 0xF8, 0x1C, 0x54, 0xE8, 0x4E, 0xAE, 0xB5,
63. 0xBB, 0xD6, 0xC3, 0x8D, 0x56, 0x79, 0xE8, 0x7C, 0x43, 0xDC, 0xF3, 0xB3, 0x7A, 0x30, 0x22, 0x09, 0xBC, 0x10, 0xD6,
64. 0x84, 0xC4, 0x0F, 0x4C, 0x0B, 0xA2, 0xD1, 0xCB, 0xCD, 0x1F, 0x50, 0x3D, 0xF7, 0x23, 0x45, 0x55, 0x18, 0x21, 0x3D,
65. 0x64, 0x05, 0x2E, 0x52, 0x3A, 0x73, 0xFD, 0xF2, 0xA9, 0xCA, 0x3F, 0xF6, 0x7F, 0x87, 0xE8, 0x56, 0x9B, 0x68, 0x6B,
66. 0x20, 0xB0, 0x1D, 0x83, 0x04, 0x2F, 0x59, 0xFD, 0x84, 0x57, 0x7D, 0x82, 0x97, 0x96, 0xE8, 0xFB, 0xDF, 0x71, 0x8C,
67. 0x26, 0x47, 0x85, 0xA5, 0xBE, 0xFB, 0xF5, 0x05, 0x4C, 0xD3, 0x3D, 0x73, 0xF4, 0xA5, 0xF1, 0xA3, 0x99, 0x98, 0x1B,
68. 0x84, 0x8B, 0xB3, 0x53, 0xCE, 0x4D, 0xEA, 0x5A, 0x48, 0xD2, 0xB9, 0x7E, 0xB6, 0xEB, 0x9B, 0x94, 0x6F, 0xDD, 0x44,
69. 0x80, 0x89, 0xD2, 0x78, 0x6D, 0xB9, 0xDA, 0x8B, 0x83, 0x49, 0xE0, 0x4D, 0x49, 0xDF, 0x6B, 0xFF, 0xF7, 0x04, 0x00,
70. 0x32, 0xAA, 0x1D, 0x4F, 0x8D, 0x4B, 0xDE, 0xB8, 0x0D, 0xC6, 0x54, 0x1C, 0xB2, 0xCD, 0x60, 0x29, 0x72, 0x0A, 0x7E,
71. 0xE7, 0xEB, 0x7A, 0xF6, 0x5B, 0x04, 0x3F, 0x5B, 0x93, 0x12, 0x0D, 0xD5, 0xFF, 0x7A, 0x41, 0x44, 0x0B, 0x37, 0x12,
72. 0x82, 0x3D, 0xDD, 0x1E, 0x59, 0xB9, 0xBE, 0x0F, 0x9E, 0xD6, 0xD0, 0x68, 0x69, 0x74, 0xF9, 0xB1, 0x21, 0xA3, 0x70,
73. 0x4F, 0xDA, 0xF8, 0x9F, 0xB9, 0x49, 0x3F, 0xC6, 0xB2, 0x69, 0xC8, 0xD8, 0x60, 0xF1, 0x6A, 0x52, 0x07, 0xFA, 0x42,
74. 0xFD, 0xA9, 0x06, 0xCF, 0x97, 0x4A, 0x0E, 0xC5, 0xFC, 0x63, 0x27, 0x54, 0xC8, 0xBE, 0x8B, 0x4F, 0xB6, 0x42, 0xBC,
75. 0xA2, 0xCC, 0x70, 0x4A, 0x6B, 0x24, 0x5B, 0x68, 0x28, 0x47, 0xFA, 0x6B, 0x89, 0x28, 0x07, 0x5D, 0xE0, 0x2C, 0x4A,
76. 0xD9, 0x22, 0xE3, 0xB3, 0x2F, 0xAA, 0xC2, 0xA0, 0x7C, 0x0F, 0x92, 0xC5, 0xDD, 0xB6, 0x23, 0x8F, 0x73, 0x73, 0x0F,
77. 0xD7, 0x73, 0x71, 0x2F, 0x0A, 0x78, 0xE8, 0x5B, 0xDB, 0xC2, 0xE0, 0xDB, 0xC9, 0x3E, 0xC3, 0x72, 0x9C, 0x14, 0xD7,
78. 0xD1, 0x28, 0xFD, 0xF4, 0xEE, 0xBC, 0x0E, 0x13, 0x37, 0xCA, 0x85, 0x9F, 0xB9, 0xA2, 0x0E, 0xF6, 0xE7, 0x49, 0xD1,
79. 0xD0, 0x11, 0x76, 0x53, 0xA3, 0x73, 0x95, 0x2A, 0x23, 0xC8, 0x0E, 0x97, 0x83, 0x07, 0x64, 0xB2, 0x51, 0xB7, 0xC8,
80. 0x51, 0x9F, 0xA4, 0x3E, 0x7B, 0xA4, 0x18, 0x6D, 0x99, 0xF0, 0x6E, 0xC3, 0x97, 0xAE, 0xF4, 0xB7, 0x66, 0x37, 0xFA,
81. 0x65, 0xFC, 0x5E, 0xE2, 0x57, 0xFA, 0x8B, 0x4C, 0x86, 0x10, 0xB4, 0x5C, 0xA4, 0xD2, 0x60, 0x83, 0x69, 0x1E, 0xFF,
82. 0x36, 0x9B, 0xF9, 0x84, 0xFB, 0xB8, 0x83, 0x64, 0xF1, 0x41, 0xA5, 0x25, 0x56, 0x21, 0xBA, 0x13, 0x98, 0x0C, 0x3B,
83. 0x04, 0xAA, 0x6C, 0x9A, 0xD4, 0xE3, 0x13, 0x15, 0x54, 0x05, 0x4C, 0x5C, 0xE1, 0x7A, 0x31, 0x5E, 0x90, 0xCF, 0x48,
84. 0x4E, 0x83, 0xD7, 0x7F, 0xED, 0x93, 0x22, 0xAB, 0x67, 0xE7, 0x76, 0x32, 0x64, 0xBA, 0x5A, 0x21, 0x3E, 0x30, 0x82,
85. 0x01, 0x41, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x01, 0xA0, 0x82, 0x01, 0x32, 0x04, 0x82,
86. 0x01, 0x2E, 0x30, 0x82, 0x01, 0x2A, 0x30, 0x82, 0x01, 0x26, 0x06, 0x0B, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01,
87. 0x0C, 0x0A, 0x01, 0x02, 0xA0, 0x81, 0xEF, 0x30, 0x81, 0xEC, 0x30, 0x57, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
88. 0x0D, 0x01, 0x05, 0x0D, 0x30, 0x4A, 0x30, 0x29, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0C,
89. 0x30, 0x1C, 0x04, 0x08, 0xED, 0x3E, 0xED, 0x07, 0x5C, 0x1F, 0x71, 0xAD, 0x02, 0x02, 0x08, 0x00, 0x30, 0x0C, 0x06,
90. 0x08, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x02, 0x09, 0x05, 0x00, 0x30, 0x1D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01,
91. 0x65, 0x03, 0x04, 0x01, 0x2A, 0x04, 0x10, 0xA7, 0x49, 0xA4, 0x6E, 0x00, 0x19, 0x75, 0x59, 0x75, 0x59, 0xBA, 0x4B,
92. 0xC7, 0x24, 0x88, 0x34, 0x04, 0x81, 0x90, 0xCA, 0x23, 0x82, 0xAA, 0x16, 0x57, 0x99, 0xFA, 0x94, 0x9F, 0xAE, 0x32,
93. 0x5C, 0x5B, 0xE7, 0x01, 0xD0, 0xED, 0xA7, 0x58, 0x57, 0x52, 0xBF, 0x57, 0x13, 0xD4, 0x15, 0xB0, 0x06, 0xF5, 0x38,
94. 0xCC, 0x64, 0x23, 0x09, 0xD5, 0x8C, 0x0D, 0x64, 0x31, 0xFA, 0x74, 0xAA, 0x96, 0x7E, 0x9B, 0x16, 0xCA, 0x21, 0xFD,
95. 0xC0, 0x54, 0x91, 0x40, 0x7F, 0xB3, 0xF2, 0xA3, 0xEC, 0xA1, 0x4A, 0x07, 0xF0, 0x87, 0x22, 0xDB, 0x8A, 0x49, 0x89,
96. 0xF7, 0xF2, 0x6A, 0xFC, 0x8D, 0x03, 0x6E, 0x32, 0x4F, 0xD0, 0xD8, 0x93, 0x92, 0xA5, 0xF1, 0x41, 0xBD, 0xEA, 0xE1,
97. 0x38, 0xA9, 0xD8, 0x9D, 0xAB, 0xB4, 0x8E, 0x4A, 0x40, 0x0E, 0xC7, 0xE3, 0xE9, 0xBF, 0x0E, 0xBA, 0x8D, 0xAA, 0x3E,
98. 0x93, 0x53, 0x88, 0xEE, 0x0A, 0x2C, 0x71, 0xF1, 0x61, 0x44, 0xA5, 0xAD, 0xED, 0x3E, 0xAB, 0x32, 0x9A, 0x32, 0x85,
99. 0x08, 0xF5, 0x8B, 0xCC, 0x15, 0x35, 0xEE, 0xFA, 0x17, 0x27, 0x97, 0x8D, 0xD9, 0x1C, 0x5E, 0x74, 0x9D, 0x7B, 0x31,
100. 0x25, 0x30, 0x23, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x5F,
101. 0x8E, 0xAB, 0x9C, 0x5F, 0xE2, 0x3B, 0xB1, 0x5C, 0x1A, 0x36, 0x1D, 0x7D, 0xCB, 0x90, 0x45, 0x20, 0x3C, 0x3B, 0xAC,
102. 0x30, 0x41, 0x30, 0x31, 0x30, 0x0D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x05, 0x00,
103. 0x04, 0x20, 0x93, 0x25, 0xC4, 0x3E, 0x2A, 0x6D, 0x4C, 0x30, 0x87, 0x0F, 0xE3, 0x5A, 0x95, 0xB0, 0xF2, 0x6C, 0xBA,
104. 0x07, 0x89, 0x7D, 0xFB, 0xCF, 0xCF, 0x1D, 0x54, 0xA3, 0x36, 0x24, 0x7B, 0x30, 0x97, 0xB5, 0x04, 0x08, 0xE7, 0x96,
105. 0x59, 0xCC, 0x42, 0x9F, 0xEF, 0xFC, 0x02, 0x02, 0x08, 0x00]),
106. '123456').then((data) => {
107. console.info('createTrustAnchorsWithKeyStore result: success, number of the result = ' + data.length);
108. }).catch((err: BusinessError) => {
109. console.error(`createTrustAnchorsWithKeyStore failed: errCode: ${err.code}, errMsg: ${err.message}`);
110. })
111. } catch (error) {
112. console.error(`createTrustAnchorsWithKeyStore failed: errCode: ${error.code}, errMsg: ${error.message}`);
113. }
```

## X509CertChain11+

PhonePC/2in1TabletTVWearable

X509证书链对象。

### getCertList11+

PhonePC/2in1TabletTVWearable

getCertList(): Array<X509Cert>

获取X509证书列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[X509Cert](js-apis-cert.md#x509cert)> | X509证书数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
15. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
16. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
17. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
18. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
19. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
20. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
21. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
22. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
23. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
24. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
25. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
26. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
27. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
28. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
29. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
30. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
31. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
32. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
33. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
34. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
35. '-----END CERTIFICATE-----\n' +
36. '-----BEGIN CERTIFICATE-----\n' +
37. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
38. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
39. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
40. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
41. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
42. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
43. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
44. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
45. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
46. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
47. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
48. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
49. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
50. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
51. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
52. 'uKPWR9dKBA==\n' +
53. '-----END CERTIFICATE-----\n' +
54. '-----BEGIN CERTIFICATE-----\n' +
55. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
56. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
57. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
58. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
59. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
60. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
61. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
62. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
63. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
64. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
65. 'xjoE\n' +
66. '-----END CERTIFICATE-----\n';

68. // 证书链二进制数据，需业务自行赋值。
69. let encodingBlob: cert.EncodingBlob = {
70. data: stringToUint8Array(certChainData),
71. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
72. encodingFormat: cert.EncodingFormat.FORMAT_PEM
73. };

75. cert.createX509CertChain(encodingBlob, (err, certChain) => {
76. if (err) {
77. console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
78. } else {
79. console.info('createX509CertChain result: success.');
80. try {
81. let certList = certChain.getCertList();
82. } catch (err) {
83. let e: BusinessError = err as BusinessError;
84. console.error(`X509CertChain getCertList failed, errCode: ${e.code}, errMsg: ${e.message}`);
85. }
86. }
87. });
```

### validate11+

PhonePC/2in1TabletTVWearable

validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>

校验证书链。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [CertChainValidationParameters](js-apis-cert.md#certchainvalidationparameters11) | 是 | 表示校验X509证书链的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CertChainValidationResult](js-apis-cert.md#certchainvalidationresult11)> | Promise对象，返回证书链校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. async function createX509CertChain(): Promise<cert.X509CertChain> {
14. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
15. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
16. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
17. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
18. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
19. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
20. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
21. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
22. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
23. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
24. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
25. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
26. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
27. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
28. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
29. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
30. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
31. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
32. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
33. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
34. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
35. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
36. '-----END CERTIFICATE-----\n' +
37. '-----BEGIN CERTIFICATE-----\n' +
38. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
39. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
40. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
41. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
42. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
43. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
44. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
45. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
46. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
47. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
48. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
49. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
50. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
51. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
52. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
53. 'uKPWR9dKBA==\n' +
54. '-----END CERTIFICATE-----\n' +
55. '-----BEGIN CERTIFICATE-----\n' +
56. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
57. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
58. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
59. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
60. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
61. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
62. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
63. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
64. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
65. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
66. 'xjoE\n' +
67. '-----END CERTIFICATE-----\n';

69. // 证书链二进制数据，需业务自行赋值。
70. let encodingBlob: cert.EncodingBlob = {
71. data: stringToUint8Array(certChainData),
72. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
76. try {
77. x509CertChain = await cert.createX509CertChain(encodingBlob);
78. } catch (error) {
79. let e: BusinessError = error as BusinessError;
80. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
81. }
82. return x509CertChain;
83. }

85. async function validate() {
86. const certChain = await createX509CertChain();
87. // 证书链校验数据，需业务自行赋值。
88. const param: cert.CertChainValidationParameters = {
89. date: '20231212080000Z',
90. trustAnchors: [{
91. CAPubKey: new Uint8Array([0x30, 0x2a, 0x30, 0x05, 0x06, 0x03, 0x2b, 0x65, 0x70, 0x03, 0x21, 0x00, 0xbb, 0x16,
92. 0x9d, 0x8f, 0x5c, 0x30, 0xd0, 0xba, 0x8f, 0x37, 0x6e, 0x33, 0xaf, 0x6f, 0x23, 0x71, 0x23, 0xa5, 0x49, 0x60,
93. 0x1e, 0xd1, 0x07, 0x4b, 0xc9, 0x11, 0x7e, 0x66, 0x01, 0xba, 0x92, 0x52]),
94. CASubject: new Uint8Array([0x30, 0x5a, 0x31, 0x0b, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x45,
95. 0x4e, 0x31, 0x10, 0x30, 0x0e, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x45, 0x6e, 0x67, 0x6c, 0x61, 0x6e,
96. 0x64, 0x31, 0x0f, 0x30, 0x0d, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x06, 0x4c, 0x6f, 0x6e, 0x64, 0x6f, 0x6e,
97. 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0a, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a,
98. 0x06, 0x03, 0x55, 0x04, 0x0b, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04,
99. 0x03, 0x13, 0x03, 0x74, 0x73, 0x31]),
100. }]
101. }
102. try {
103. const validationRes = await certChain.validate(param);
104. console.info('X509CertChain validate result: success.');
105. } catch (error) {
106. let e: BusinessError = error as BusinessError;
107. console.error(`X509CertChain validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
108. }
109. }

111. validate();
```

### validate11+

PhonePC/2in1TabletTVWearable

validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void

使用校验参数校验证书链。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [CertChainValidationParameters](js-apis-cert.md#certchainvalidationparameters11) | 是 | 表示校验X509证书链的参数。 |
| callback | AsyncCallback<[CertChainValidationResult](js-apis-cert.md#certchainvalidationresult11)> | 是 | 回调函数，返回证书链校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: Array<number> = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
13. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
14. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
15. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
16. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
17. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
18. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
19. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
20. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
21. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
22. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
23. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
24. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
25. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
26. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
27. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
28. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
29. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
30. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
31. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
32. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
33. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
34. '-----END CERTIFICATE-----\n' +
35. '-----BEGIN CERTIFICATE-----\n' +
36. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
37. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
38. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
39. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
40. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
41. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
42. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
43. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
44. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
45. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
46. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
47. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
48. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
49. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
50. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
51. 'uKPWR9dKBA==\n' +
52. '-----END CERTIFICATE-----\n' +
53. '-----BEGIN CERTIFICATE-----\n' +
54. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
55. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
56. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
57. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
58. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
59. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
60. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
61. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
62. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
63. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
64. 'xjoE\n' +
65. '-----END CERTIFICATE-----\n';

67. // 证书链二进制数据，需业务自行赋值。
68. let encodingBlob: cert.EncodingBlob = {
69. data: stringToUint8Array(certChainData),
70. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
71. encodingFormat: cert.EncodingFormat.FORMAT_PEM
72. };

74. // 证书链校验数据，需业务自行赋值。
75. let param: cert.CertChainValidationParameters = {
76. date: '20231212080000Z',
77. trustAnchors: [{
78. CAPubKey: new Uint8Array([0x30, 0x2a, 0x30, 0x05, 0x06, 0x03, 0x2b, 0x65, 0x70, 0x03, 0x21, 0x00, 0xbb, 0x16, 0x9d,
79. 0x8f, 0x5c, 0x30, 0xd0, 0xba, 0x8f, 0x37, 0x6e, 0x33, 0xaf, 0x6f, 0x23, 0x71, 0x23, 0xa5, 0x49, 0x60, 0x1e, 0xd1,
80. 0x07, 0x4b, 0xc9, 0x11, 0x7e, 0x66, 0x01, 0xba, 0x92, 0x52]),
81. CASubject: new Uint8Array([0x30, 0x5a, 0x31, 0x0b, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x45, 0x4e,
82. 0x31, 0x10, 0x30, 0x0e, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x45, 0x6e, 0x67, 0x6c, 0x61, 0x6e, 0x64, 0x31,
83. 0x0f, 0x30, 0x0d, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x06, 0x4c, 0x6f, 0x6e, 0x64, 0x6f, 0x6e, 0x31, 0x0c, 0x30,
84. 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0a, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04,
85. 0x0b, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x03, 0x74, 0x73,
86. 0x31]),
87. }]
88. };

90. cert.createX509CertChain(encodingBlob, (err, certChain) => {
91. if (err) {
92. console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
93. } else {
94. console.info('createX509CertChain result: success.');
95. certChain.validate(param, (error, validationRes) => {
96. if (error) {
97. console.error(`X509CertChain validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
98. } else {
99. console.info('X509CertChain validate result: success.');
100. }
101. });
102. }
103. });
```

### toString12+

PhonePC/2in1TabletTVWearable

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIGVjCCBT6gAwIBAgIQBMO0W3CU9LWVw1bE/jqYojANBgkqhkiG9w0BAQsFADBE\n' +
15. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMR4wHAYDVQQDExVH\n' +
16. 'ZW9UcnVzdCBSU0EgQ04gQ0EgRzIwHhcNMjMwMzIzMDAwMDAwWhcNMjQwNDIyMjM1\n' +
17. 'OTU5WjB1MQswCQYDVQQGEwJDTjERMA8GA1UECBMIemhlamlhbmcxETAPBgNVBAcT\n' +
18. 'CGhhbmd6aG91MSwwKgYDVQQKEyNOZXRFYXNlIChIYW5nemhvdSkgTmV0d29yayBD\n' +
19. 'by4sIEx0ZDESMBAGA1UEAwwJKi4xNjMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\n' +
20. 'AQ8AMIIBCgKCAQEAwELks0Q1Z81u1OpbGdEFE2Snm/WpLfmiC5YFj5nFrinSX+UZ\n' +
21. 'MIk42euBdjYSsWFxbljmWDdUCjstMhG8vRAjz3Nt1QniMCunHHFGujR5rSNLWYHE\n' +
22. 'vCPhfptIhqOaE/rvkWGZZr2KjTQQN0dRf8dm9Oewy8DHu95c9jW6c9AVgKWUVOni\n' +
23. 'tTOcJCnrndWjgCIPfKmKgrwaNaMnuQyy5nPIUHl/5EGzuGHrwjwlF+w+cT+Fwdix\n' +
24. 'C3msEOCwX6wzo6baDs4og2EzuPNyTp4n4UqH5aHhLePgBFboOAyJwWp3+XJNpNGw\n' +
25. 'GkU56cUUy7+AAn268EVvUNr7uQ65t2t+Ys32bQIDAQABo4IDETCCAw0wHwYDVR0j\n' +
26. 'BBgwFoAUJG+RP4mHhw4ywkAY38VM60/ISTIwHQYDVR0OBBYEFD1HyRYJ5jqkvYL7\n' +
27. 'C6TSt8/y3e7hMB0GA1UdEQQWMBSCCSouMTYzLmNvbYIHMTYzLmNvbTAOBgNVHQ8B\n' +
28. 'Af8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMD0GA1UdHwQ2\n' +
29. 'MDQwMqAwoC6GLGh0dHA6Ly9jcmwuZGlnaWNlcnQuY24vR2VvVHJ1c3RSU0FDTkNB\n' +
30. 'RzIuY3JsMD4GA1UdIAQ3MDUwMwYGZ4EMAQICMCkwJwYIKwYBBQUHAgEWG2h0dHA6\n' +
31. 'Ly93d3cuZGlnaWNlcnQuY29tL0NQUzBxBggrBgEFBQcBAQRlMGMwIwYIKwYBBQUH\n' +
32. 'MAGGF2h0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNuMDwGCCsGAQUFBzAChjBodHRwOi8v\n' +
33. 'Y2FjZXJ0cy5kaWdpY2VydC5jbi9HZW9UcnVzdFJTQUNOQ0FHMi5jcnQwCQYDVR0T\n' +
34. 'BAIwADCCAX4GCisGAQQB1nkCBAIEggFuBIIBagFoAHUA7s3QZNXbGs7FXLedtM0T\n' +
35. 'ojKHRny87N7DUUhZRnEftZsAAAGHDSE15QAABAMARjBEAiBRpmsJ3F9AI8wFxqOQ\n' +
36. 'bHp+RL6F8cvNydajQ0Bqxjvd3AIgefAU/po3jBm+96dFVdbX+AG1uss67DL3VL5I\n' +
37. 'nUmVva8AdgBz2Z6JG0yWeKAgfUed5rLGHNBRXnEZKoxrgBB6wXdytQAAAYcNITZS\n' +
38. 'AAAEAwBHMEUCID/sUP12odF7uTTEyE0PjCpKo3nF7A3ba3b5wJJsZrDrAiEAxrat\n' +
39. 'W2eeZTD458LPSPrMMBb1/o6zibWXqJCQye+bVFwAdwBIsONr2qZHNA/lagL6nTDr\n' +
40. 'HFIBy1bdLIHZu7+rOdiEcwAAAYcNITYeAAAEAwBIMEYCIQCCJ2ktM1F+d1I5mQju\n' +
41. 'Tn7oDYxy3GCGyG3u/yhu8k7EaAIhANSP8cAaMQFV6y8B2tubKY5eSQtgkF3a6NNq\n' +
42. 'QJjtPnoHMA0GCSqGSIb3DQEBCwUAA4IBAQC8dK/G4nvs/SyQe/mnK+rUYIdSFs+4\n' +
43. 'lgzatmq8V/I1tBly+Sv/FPhnn4F3iCrqy9j8y202FP51ev95DGbjlJRTIFPqVAO8\n' +
44. 'ywYrLhvl1SJhV0b/8NF0Pr3dZVnK5Vfn11+LSBUg0cBB2hcVV30nv3IuVhz3d12n\n' +
45. 'P+VseYQgMpQf7ad+ttpZtA7yqHzrUm4fzr03G7q88GztACRSHoYiPbOlz99SeTgW\n' +
46. '7bzZl1I4taxy2Q3b0ZBGfUt/kPY05tpKzKwDTbbqSErYszCt5X1RfVvf3coxF8Mo\n' +
47. '9bHbs2wYIzQBdujDQ/hU0u6ItERer3SUItZoxaSIxdrZ9eXFwVvXsT/g\n' +
48. '-----END CERTIFICATE-----\n' +
49. '-----BEGIN CERTIFICATE-----\n' +
50. 'MIIFDzCCA/egAwIBAgIQCxNitu5qnT6WiTDxbiB9OTANBgkqhkiG9w0BAQsFADBh\n' +
51. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
52. 'd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\n' +
53. 'QTAeFw0yMDAzMDQxMjA0NDBaFw0zMDAzMDQxMjA0NDBaMEQxCzAJBgNVBAYTAlVT\n' +
54. 'MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxHjAcBgNVBAMTFUdlb1RydXN0IFJTQSBD\n' +
55. 'TiBDQSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANA1OZJJtZUI\n' +
56. '7zj4qFHT79g+Otks4TEfmUEDhrNKBEEjb/i29GBfnpvFdT36azCg2VODJRSjIzFn\n' +
57. '4qADcc84EmfKiDEM97HFsQPp9RRkqxH5cB51EU2eBE9Ua95x+wQp/KSdCqITCQ/v\n' +
58. 'yvm3J4Upjl0wlW8wRCPCWcYw3pKClGRkNzVtI1KXnfpn7fG3N84n7wlBb9IGKJFa\n' +
59. 'c/6+hxvZx2qnfLsxdIKR0Q/biGoU6Z8Iy/R/p7GoPO8vamV090+QHEL5AdSzKtEh\n' +
60. 'U9vdvcuWjjLxVnaJLfj/6WoGZj8UWn3zFbEoTVaAfp2xqdzW7yRvi2r148m9ev7l\n' +
61. 'jDqHo8UX69sCAwEAAaOCAd4wggHaMB0GA1UdDgQWBBQkb5E/iYeHDjLCQBjfxUzr\n' +
62. 'T8hJMjAfBgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8E\n' +
63. 'BAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQI\n' +
64. 'MAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzABhhdodHRwOi8vb2Nz\n' +
65. 'cC5kaWdpY2VydC5jbjBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3JsLmRpZ2lj\n' +
66. 'ZXJ0LmNuL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDCB3QYDVR0gBIHVMIHSMIHF\n' +
67. 'BglghkgBhv1sAQEwgbcwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0\n' +
68. 'LmNvbS9DUFMwgYoGCCsGAQUFBwICMH4MfEFueSB1c2Ugb2YgdGhpcyBDZXJ0aWZp\n' +
69. 'Y2F0ZSBjb25zdGl0dXRlcyBhY2NlcHRhbmNlIG9mIHRoZSBSZWx5aW5nIFBhcnR5\n' +
70. 'IEFncmVlbWVudCBsb2NhdGVkIGF0IGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9y\n' +
71. 'cGEtdWEwCAYGZ4EMAQICMA0GCSqGSIb3DQEBCwUAA4IBAQCzkcXq0TN0oSn4UeXp\n' +
72. 'FBW7U8zrHBIhH9MXHNBp+Yy/yN19133UY05uuHXHaU2Uv0hxefckjPdkaX7ARso+\n' +
73. 'O3Ar6nf7YfBwCqSpqsNckKT7KKtf3Ot95wYFpKDa64jcRUfxzRWnmq12IVzczqHI\n' +
74. 'sIvUZQINw/UHSQcWekdUnMg58bQSHyTjwkj9jcX2RURxaVZkr15wxo/Z3Ydo2PVK\n' +
75. '3afEr0/vcuFvE7QeGXiI2DJdVt3JefatZ3rj4VTW2aUZwHGUiWWIUudBfQKR0JEp\n' +
76. 'lJ8MFaKDh4/A2VEJnXILu1iwvc1m3jCaPuzZKdoHM/1234bznJI2aAfhfIhoHw90\n' +
77. 'tPO+\n' +
78. '-----END CERTIFICATE-----\n';

80. // 证书链二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(certChainData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. async function certChainToString() {
88. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
89. try {
90. x509CertChain = await cert.createX509CertChain(encodingBlob);
91. console.info('createX509CertChain result: success.');
92. console.info('toString success: ' + x509CertChain.toString());
93. } catch (error) {
94. let e: BusinessError = error as BusinessError;
95. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
96. }
97. }
```

### hashCode12+

PhonePC/2in1TabletTVWearable

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
14. 'MIIGVjCCBT6gAwIBAgIQBMO0W3CU9LWVw1bE/jqYojANBgkqhkiG9w0BAQsFADBE\n' +
15. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMR4wHAYDVQQDExVH\n' +
16. 'ZW9UcnVzdCBSU0EgQ04gQ0EgRzIwHhcNMjMwMzIzMDAwMDAwWhcNMjQwNDIyMjM1\n' +
17. 'OTU5WjB1MQswCQYDVQQGEwJDTjERMA8GA1UECBMIemhlamlhbmcxETAPBgNVBAcT\n' +
18. 'CGhhbmd6aG91MSwwKgYDVQQKEyNOZXRFYXNlIChIYW5nemhvdSkgTmV0d29yayBD\n' +
19. 'by4sIEx0ZDESMBAGA1UEAwwJKi4xNjMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\n' +
20. 'AQ8AMIIBCgKCAQEAwELks0Q1Z81u1OpbGdEFE2Snm/WpLfmiC5YFj5nFrinSX+UZ\n' +
21. 'MIk42euBdjYSsWFxbljmWDdUCjstMhG8vRAjz3Nt1QniMCunHHFGujR5rSNLWYHE\n' +
22. 'vCPhfptIhqOaE/rvkWGZZr2KjTQQN0dRf8dm9Oewy8DHu95c9jW6c9AVgKWUVOni\n' +
23. 'tTOcJCnrndWjgCIPfKmKgrwaNaMnuQyy5nPIUHl/5EGzuGHrwjwlF+w+cT+Fwdix\n' +
24. 'C3msEOCwX6wzo6baDs4og2EzuPNyTp4n4UqH5aHhLePgBFboOAyJwWp3+XJNpNGw\n' +
25. 'GkU56cUUy7+AAn268EVvUNr7uQ65t2t+Ys32bQIDAQABo4IDETCCAw0wHwYDVR0j\n' +
26. 'BBgwFoAUJG+RP4mHhw4ywkAY38VM60/ISTIwHQYDVR0OBBYEFD1HyRYJ5jqkvYL7\n' +
27. 'C6TSt8/y3e7hMB0GA1UdEQQWMBSCCSouMTYzLmNvbYIHMTYzLmNvbTAOBgNVHQ8B\n' +
28. 'Af8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMD0GA1UdHwQ2\n' +
29. 'MDQwMqAwoC6GLGh0dHA6Ly9jcmwuZGlnaWNlcnQuY24vR2VvVHJ1c3RSU0FDTkNB\n' +
30. 'RzIuY3JsMD4GA1UdIAQ3MDUwMwYGZ4EMAQICMCkwJwYIKwYBBQUHAgEWG2h0dHA6\n' +
31. 'Ly93d3cuZGlnaWNlcnQuY29tL0NQUzBxBggrBgEFBQcBAQRlMGMwIwYIKwYBBQUH\n' +
32. 'MAGGF2h0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNuMDwGCCsGAQUFBzAChjBodHRwOi8v\n' +
33. 'Y2FjZXJ0cy5kaWdpY2VydC5jbi9HZW9UcnVzdFJTQUNOQ0FHMi5jcnQwCQYDVR0T\n' +
34. 'BAIwADCCAX4GCisGAQQB1nkCBAIEggFuBIIBagFoAHUA7s3QZNXbGs7FXLedtM0T\n' +
35. 'ojKHRny87N7DUUhZRnEftZsAAAGHDSE15QAABAMARjBEAiBRpmsJ3F9AI8wFxqOQ\n' +
36. 'bHp+RL6F8cvNydajQ0Bqxjvd3AIgefAU/po3jBm+96dFVdbX+AG1uss67DL3VL5I\n' +
37. 'nUmVva8AdgBz2Z6JG0yWeKAgfUed5rLGHNBRXnEZKoxrgBB6wXdytQAAAYcNITZS\n' +
38. 'AAAEAwBHMEUCID/sUP12odF7uTTEyE0PjCpKo3nF7A3ba3b5wJJsZrDrAiEAxrat\n' +
39. 'W2eeZTD458LPSPrMMBb1/o6zibWXqJCQye+bVFwAdwBIsONr2qZHNA/lagL6nTDr\n' +
40. 'HFIBy1bdLIHZu7+rOdiEcwAAAYcNITYeAAAEAwBIMEYCIQCCJ2ktM1F+d1I5mQju\n' +
41. 'Tn7oDYxy3GCGyG3u/yhu8k7EaAIhANSP8cAaMQFV6y8B2tubKY5eSQtgkF3a6NNq\n' +
42. 'QJjtPnoHMA0GCSqGSIb3DQEBCwUAA4IBAQC8dK/G4nvs/SyQe/mnK+rUYIdSFs+4\n' +
43. 'lgzatmq8V/I1tBly+Sv/FPhnn4F3iCrqy9j8y202FP51ev95DGbjlJRTIFPqVAO8\n' +
44. 'ywYrLhvl1SJhV0b/8NF0Pr3dZVnK5Vfn11+LSBUg0cBB2hcVV30nv3IuVhz3d12n\n' +
45. 'P+VseYQgMpQf7ad+ttpZtA7yqHzrUm4fzr03G7q88GztACRSHoYiPbOlz99SeTgW\n' +
46. '7bzZl1I4taxy2Q3b0ZBGfUt/kPY05tpKzKwDTbbqSErYszCt5X1RfVvf3coxF8Mo\n' +
47. '9bHbs2wYIzQBdujDQ/hU0u6ItERer3SUItZoxaSIxdrZ9eXFwVvXsT/g\n' +
48. '-----END CERTIFICATE-----\n' +
49. '-----BEGIN CERTIFICATE-----\n' +
50. 'MIIFDzCCA/egAwIBAgIQCxNitu5qnT6WiTDxbiB9OTANBgkqhkiG9w0BAQsFADBh\n' +
51. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
52. 'd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\n' +
53. 'QTAeFw0yMDAzMDQxMjA0NDBaFw0zMDAzMDQxMjA0NDBaMEQxCzAJBgNVBAYTAlVT\n' +
54. 'MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxHjAcBgNVBAMTFUdlb1RydXN0IFJTQSBD\n' +
55. 'TiBDQSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANA1OZJJtZUI\n' +
56. '7zj4qFHT79g+Otks4TEfmUEDhrNKBEEjb/i29GBfnpvFdT36azCg2VODJRSjIzFn\n' +
57. '4qADcc84EmfKiDEM97HFsQPp9RRkqxH5cB51EU2eBE9Ua95x+wQp/KSdCqITCQ/v\n' +
58. 'yvm3J4Upjl0wlW8wRCPCWcYw3pKClGRkNzVtI1KXnfpn7fG3N84n7wlBb9IGKJFa\n' +
59. 'c/6+hxvZx2qnfLsxdIKR0Q/biGoU6Z8Iy/R/p7GoPO8vamV090+QHEL5AdSzKtEh\n' +
60. 'U9vdvcuWjjLxVnaJLfj/6WoGZj8UWn3zFbEoTVaAfp2xqdzW7yRvi2r148m9ev7l\n' +
61. 'jDqHo8UX69sCAwEAAaOCAd4wggHaMB0GA1UdDgQWBBQkb5E/iYeHDjLCQBjfxUzr\n' +
62. 'T8hJMjAfBgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8E\n' +
63. 'BAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQI\n' +
64. 'MAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzABhhdodHRwOi8vb2Nz\n' +
65. 'cC5kaWdpY2VydC5jbjBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3JsLmRpZ2lj\n' +
66. 'ZXJ0LmNuL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDCB3QYDVR0gBIHVMIHSMIHF\n' +
67. 'BglghkgBhv1sAQEwgbcwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0\n' +
68. 'LmNvbS9DUFMwgYoGCCsGAQUFBwICMH4MfEFueSB1c2Ugb2YgdGhpcyBDZXJ0aWZp\n' +
69. 'Y2F0ZSBjb25zdGl0dXRlcyBhY2NlcHRhbmNlIG9mIHRoZSBSZWx5aW5nIFBhcnR5\n' +
70. 'IEFncmVlbWVudCBsb2NhdGVkIGF0IGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9y\n' +
71. 'cGEtdWEwCAYGZ4EMAQICMA0GCSqGSIb3DQEBCwUAA4IBAQCzkcXq0TN0oSn4UeXp\n' +
72. 'FBW7U8zrHBIhH9MXHNBp+Yy/yN19133UY05uuHXHaU2Uv0hxefckjPdkaX7ARso+\n' +
73. 'O3Ar6nf7YfBwCqSpqsNckKT7KKtf3Ot95wYFpKDa64jcRUfxzRWnmq12IVzczqHI\n' +
74. 'sIvUZQINw/UHSQcWekdUnMg58bQSHyTjwkj9jcX2RURxaVZkr15wxo/Z3Ydo2PVK\n' +
75. '3afEr0/vcuFvE7QeGXiI2DJdVt3JefatZ3rj4VTW2aUZwHGUiWWIUudBfQKR0JEp\n' +
76. 'lJ8MFaKDh4/A2VEJnXILu1iwvc1m3jCaPuzZKdoHM/1234bznJI2aAfhfIhoHw90\n' +
77. 'tPO+\n' +
78. '-----END CERTIFICATE-----\n';

80. // 证书链二进制数据，需业务自行赋值。
81. let encodingBlob: cert.EncodingBlob = {
82. data: stringToUint8Array(certChainData),
83. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
84. encodingFormat: cert.EncodingFormat.FORMAT_PEM
85. };

87. async function certChainHashCode() {
88. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
89. try {
90. x509CertChain = await cert.createX509CertChain(encodingBlob);
91. console.info('createX509CertChain result: success.');
92. console.info('hashCode success: ' + x509CertChain.hashCode());
93. } catch (error) {
94. let e: BusinessError = error as BusinessError;
95. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
96. }
97. }
```

## cert.generateCsr18+

PhonePC/2in1TabletTVWearable

generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array

表示使用指定的RSA私钥，传入主体、扩展、摘要算法、输出格式等配置参数去生成CSR。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyInfo | [PrivateKeyInfo](js-apis-cert.md#privatekeyinfo18) | 是 | 包含私钥跟口令的配置参数。 |
| config | [CsrGenerationConfig](js-apis-cert.md#csrgenerationconfig18) | 是 | 包含生成CSR的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Uint8Array | 表示生成的CSR数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function createCsrTest() {
5. let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
6. let prikeyEnstr: string =
7. '-----BEGIN RSA PRIVATE KEY-----\n' +
8. 'Proc-Type: 4,ENCRYPTED\n' +
9. 'DEK-Info: AES-128-CBC,B5FFA3AEEE7176106FDDB0988B532F07\n\n' +
10. 't3zNRGKp5X4BNkcsYATad/Le+94yMIX9CoNAGsBIDzQw+773UMGIoeGEYVlXWc8x\n' +
11. 'N1XWDinn4ytWw9x9OfUYgmNnrdkWRSaIuw+SpQfBgJip+MsNERYOHZ5TYWTR8n3k\n' +
12. '7/jHY8eCgTsP3hbNtyaePIrtbTLZGZAHG1YWY5UmLaYoI1O6/Vvobx72lx3b43Tx\n' +
13. '4j5lkknpLl85fcs1s4TYMOd8vEwhdpouR4VY8kfRSm44WQLtGXrce0An3MG3pXyZ\n' +
14. 'GhpmJyTcg0epTEYVzglENlBJrBVDL+bJ8uvHGH4tmeQb77e6ILXoxZntM7zQMMFo\n' +
15. 'A7dilqO6FBxu20n2TidVGCa0Yn+DZLpry2OdwVUC2nXyCHCehr3jAZz6k20FWg5B\n' +
16. 'EsU16yOIB+bp9BUKdTpJVtc/pmZJtnlA9pSCUVmWdltOsjjxkE94wfAUOYhO3Mvz\n' +
17. 'gF9KR1/bdAbLw4t7bGeuyV4N2iYr83FodLLXpupM6Qfb51+HVgHvm2aaHv2Q4sf3\n' +
18. 'poCVTNlegoVV9x3+7HqXY6MjlG8aU6LcWqH34ySqRBQrKL1PuDzQSY5/RmP7PUhG\n' +
19. 'ym4l6KbEaRC2H/XS2qKa4VCMgBCgA0hoiw4s48Xd4h2GUTuxLM9wGyW89OEaHky7\n' +
20. 'VE7t3O9a2zhkRTYDDYQ8QCycKhNrsKySyItRUWn/w2lXvuKM7PpAzYH7Ey3W1eZG\n' +
21. 'PyyeGG9exjpdIvD3tx5Hl/OWwBkW1DAzO40gT6sdD5FXzRv4fCHuCrIow5QMLF4T\n' +
22. 'd5Y4a6q13V4O5b73T5INmKl8rEbPGIw7WLR7BNj05QuzNcn5kA1aBFIJqsxQv46l\n' +
23. '-----END RSA PRIVATE KEY-----\n';
24. let priKeyInfo: cert.PrivateKeyInfo = {
25. key: prikeyEnstr,
26. password: '123abc'
27. }
28. let keyUsage: cert.CsrAttribute = {
29. type: 'keyUsage',
30. value: 'digitalSignature, keyEncipherment'
31. };

33. let challengePassword: cert.CsrAttribute = {
34. type: 'challengePassword',
35. value: '123456'
36. };
37. let attribute: cert.CsrAttribute[] = [
38. keyUsage, challengePassword
39. ];
40. try {
41. let data = await cert.createX500DistinguishedName(nameStr);
42. console.info('createX500DistinguishedName result: success. ' + data.getName('CN').toString());
43. let conf: cert.CsrGenerationConfig = {
44. subject: data,
45. mdName: 'SHA256',
46. outFormat: cert.EncodingBaseFormat.PEM,
47. attributes: attribute
48. }
49. try {
50. let csrStr = cert.generateCsr(priKeyInfo, conf)
51. console.info('generateCsr result: success, return str is ' + csrStr.toString())
52. } catch (error) {
53. let e: BusinessError = error as BusinessError;
54. console.error(`generateCsr failed, errCode: ${e.code}, errMsg: ${e.message}`);
55. }
56. } catch (error) {
57. let e: BusinessError = error as BusinessError;
58. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
59. }
60. }
```

## cert.createX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>

表示使用字符串格式的名称创建X500DistinguishedName对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nameStr | string | 是 | X509定义的Name字符串格式，使用斜杠'/'进行分割可分辨名称，每个可分辨名称为“属性=值”形式，常用属性包括CN（通用名）、O（组织名）、OU（组织单位）、C（国家/地区）、ST（省/州）、L（市/区）。例如：/CN=example.com/O=Example/C=CN。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X500DistinguishedName](js-apis-cert.md#x500distinguishedname12)> | 表示X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // string转Uint8Array。
5. function stringToUint8Array(str: string): Uint8Array {
6. let arr: Array<number> = [];
7. for (let i = 0, j = str.length; i < j; i++) {
8. arr.push(str.charCodeAt(i));
9. }
10. return new Uint8Array(arr);
11. }

13. let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
14. async function createX500DistinguishedName() {
15. try {
16. cert.createX500DistinguishedName(nameStr)
17. .then((data) => {
18. console.info('createX500DistinguishedName result: success.');
19. })
20. .catch((err: BusinessError) => {
21. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
22. })
23. } catch (error) {
24. let e: BusinessError = error as BusinessError;
25. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
26. }
27. }
```

## cert.createX500DistinguishedName12+

PhonePC/2in1TabletTVWearable

createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>

表示使用DER格式的名称创建X500DistinguishedName对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nameDer | Uint8Array | 是 | X509定义的Uint8Array类型的DER格式数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X500DistinguishedName](js-apis-cert.md#x500distinguishedname12)> | 表示X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let nameDer =
5. new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
6. 101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

8. async function createX500DistinguishedName() {
9. try {
10. cert.createX500DistinguishedName(nameDer)
11. .then((data) => {
12. console.info('createX500DistinguishedName result: success.');
13. })
14. .catch((err: BusinessError) => {
15. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
16. })
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
20. }
21. }
```

## X500DistinguishedName12+

PhonePC/2in1TabletTVWearable

X509定义的Name类型的对象。

### getName12+

PhonePC/2in1TabletTVWearable

getName(): string

获取可分辨名的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 可分辨名的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let nameDer =
5. new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
6. 101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

8. async function getName() {
9. try {
10. cert.createX500DistinguishedName(nameDer)
11. .then((data) => {
12. console.info('createX500DistinguishedName result: success.');
13. console.info('createX500DistinguishedName getName: ' + data.getName());
14. })
15. .catch((err: BusinessError) => {
16. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
17. })
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
21. }
22. }
```

### getName12+

PhonePC/2in1TabletTVWearable

getName(type: string): Array<string>

按指定类型获取相对可分辨名称的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 指定类型的名称。如"CN"、"OU"等。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<string> | 相对可分辨名称的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
5. async function getName() {
6. try {
7. cert.createX500DistinguishedName(nameStr)
8. .then((data) => {
9. console.info('createX500DistinguishedName result: success.');
10. console.info('createX500DistinguishedName getName: ' + data.getName("CN"));
11. })
12. .catch((err: BusinessError) => {
13. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
14. })
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
18. }
19. }
```

### getName20+

PhonePC/2in1TabletTVWearable

getName(encodingType: EncodingType): string

根据指定编码格式获取可分辨名称的字符串。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](js-apis-cert.md#encodingtype12) | 是 | 表示编码格式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示可分辨名称的字符串，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The value of encodingType is not in the EncodingType enumeration range. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let nameStr = '/CN=陕西@西安/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
5. async function getName() {
6. try {
7. cert.createX500DistinguishedName(nameStr)
8. .then((data) => {
9. console.info('createX500DistinguishedName result: success.');
10. console.info('createX500DistinguishedName getName: ' + data.getName(cert.EncodingType.ENCODING_UTF8));
11. })
12. .catch((err: BusinessError) => {
13. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
14. })
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
18. }
19. }
```

### getEncoded12+

PhonePC/2in1TabletTVWearable

getEncoded(): EncodingBlob

获取X509证书扩展域的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [EncodingBlob](js-apis-cert.md#encodingblob) | X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
5. async function getEncoded() {
6. try {
7. cert.createX500DistinguishedName(nameStr)
8. .then((data) => {
9. console.info('createX500DistinguishedName result: success.');
10. let encodingBlobData = data.getEncoded();
11. })
12. .catch((err: BusinessError) => {
13. console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
14. })
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
18. }
19. }
```

## cert.createCmsGenerator18+

PhonePC/2in1TabletTVWearable

createCmsGenerator(contentType: CmsContentType): CmsGenerator

表示创建CmsGenerator对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentType | [CmsContentType](js-apis-cert.md#cmscontenttype18) | 是 | 指定CMS内容类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CmsGenerator](js-apis-cert.md#cmsgenerator18) | CmsGenerator对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. // string转Uint8Array
21. function stringToUint8Array(str: string): Uint8Array {
22. let arr: Array<number> = [];
23. for (let i = 0, j = str.length; i < j; i++) {
24. arr.push(str.charCodeAt(i));
25. }
26. return new Uint8Array(arr);
27. }

29. function testcreateCmsGenerator() {
30. let certEncodingBlob: cert.EncodingBlob = {
31. data: stringToUint8Array(certData),
32. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
33. encodingFormat: cert.EncodingFormat.FORMAT_PEM
34. };
35. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
36. if (error) {
37. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. } else {
39. try {
40. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
41. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
42. console.info('testcreateCmsGenerator createCmsGenerator result: success.');
43. } catch (err) {
44. let e: BusinessError = err as BusinessError;
45. console.error(`createCmsGenerator failed, errCode: ${e.code}, errMsg: ${e.message}`);
46. }
47. }
48. });
49. }
```

## CmsGenerator18+

PhonePC/2in1TabletTVWearable

CmsGenerator对象用于生成CMS（Cryptographic Message Syntax）格式的消息。

说明

PKCS#7是用于存储签名或加密数据的标准语法。注意CMS是PKCS#7的扩展，PKCS#7支持的数据类型包括数据、签名数据、信封数据、

签名和信封数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

### addSigner18+

PhonePC/2in1TabletTVWearable

addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void;

用于为内容类型为SIGNED\_DATA的CMS添加签名者信息。

说明

由于openssl不支持自签名证书的验签操作，因此自签名证书不能作为签名者。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 指定X509证书。 |
| keyInfo | [PrivateKeyInfo](js-apis-cert.md#privatekeyinfo18) | 是 | 指定私钥信息。 |
| config | [CmsSignerConfig](js-apis-cert.md#cmssignerconfig18) | 是 | 指定签名者选项。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. let rsaStr1024: string  =
21. '-----BEGIN RSA PRIVATE KEY-----\n' +
22. 'Proc-Type: 4,ENCRYPTED\n' +
23. 'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
24. '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
25. 'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
26. 'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
27. 'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
28. 'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
29. 'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
30. 'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
31. '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
32. 'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
33. 'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
34. 'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
35. 'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
36. '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
37. '-----END RSA PRIVATE KEY-----\n';

39. // string转Uint8Array。
40. function stringToUint8Array(str: string): Uint8Array {
41. let arr: Array<number> = [];
42. for (let i = 0, j = str.length; i < j; i++) {
43. arr.push(str.charCodeAt(i));
44. }
45. return new Uint8Array(arr);
46. }

48. function testAddSigner() {
49. let certEncodingBlob: cert.EncodingBlob = {
50. data: stringToUint8Array(certData),
51. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
52. encodingFormat: cert.EncodingFormat.FORMAT_PEM
53. };
54. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
55. if (error) {
56. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
57. } else {
58. try {
59. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
60. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
61. console.info('testAddSigner createCmsGenerator result: success.');
62. let privateKeyInfo: cert.PrivateKeyInfo = {
63. key: rsaStr1024,
64. password: '123456'
65. };
66. // addCert设置为true时，第二次addSigner增加相同的证书，会报错。
67. let config: cert.CmsSignerConfig = {
68. mdName:'SHA256',
69. addCert:false,
70. addAttr:false,
71. addSmimeCapAttr:false
72. }
73. cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
74. console.info('testAddSigner addSigner result: success.');
75. } catch (err) {
76. let e: BusinessError = err as BusinessError;
77. console.error(`testAddSigner failed, errCode: ${e.code}, errMsg: ${e.message}`);
78. }
79. }
80. });
81. }
```

### addCert18+

PhonePC/2in1TabletTVWearable

addCert(cert: X509Cert): void

用于添加内容类型为SIGNED\_DATA的CMS的证书，例如签名证书的颁发者证书。

如果未调用addSigner接口，并且仅添加证书后，生成的CMS签名数据将只包含证书。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [X509Cert](js-apis-cert.md#x509cert) | 是 | 要添加的X509证书。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. // string转Uint8Array。
21. function stringToUint8Array(str: string): Uint8Array {
22. let arr: Array<number> = [];
23. for (let i = 0, j = str.length; i < j; i++) {
24. arr.push(str.charCodeAt(i));
25. }
26. return new Uint8Array(arr);
27. }

29. function testAddCert() {
30. let certEncodingBlob: cert.EncodingBlob = {
31. data: stringToUint8Array(certData),
32. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
33. encodingFormat: cert.EncodingFormat.FORMAT_PEM
34. };
35. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
36. if (error) {
37. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
38. } else {
39. try {
40. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
41. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
42. console.info('testAddCert createCmsGenerator result: success.');
43. // 第二次addCert增加相同的证书，会报错。
44. cmsGenerator.addCert(x509Cert);
45. console.info('testAddCert addCert result: success.');
46. } catch (err) {
47. let e: BusinessError = err as BusinessError;
48. console.error(`testAddCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
49. }
50. }
51. });
52. }
```

### setRecipientEncryptionAlgorithm22+

PhonePC/2in1TabletTVWearable

setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void

为内容类型为ENVELOPED\_DATA的CMS设置加密算法。

该方法应在创建ENVELOPED\_DATA类型的CmsGenerator后立即调用。如果未调用此方法，则默认使用AES\_256\_GCM作为加密算法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | [CmsRecipientEncryptionAlgorithm](js-apis-cert.md#cmsrecipientencryptionalgorithm22) | 是 | 用于CMS封装数据的加密算法。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The type of algorithm is invalid or not supported. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. function testSetRecipientEncryptionAlgorithm() {
4. try {
5. let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
6. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
7. console.info(`createCmsGenerator result: success.`);
8. let algorithm = cert.CmsRecipientEncryptionAlgorithm.AES_128_CBC;
9. cmsGenerator.setRecipientEncryptionAlgorithm(algorithm);
10. console.info(`setRecipientEncryptionAlgorithm result: success.`);
11. } catch (err) {
12. console.error(`testSetRecipientEncryptionAlgorithm failed: errCode: ${err.code}, errMsg: ${err.message}`);
13. }
14. }
```

### addRecipientInfo22+

PhonePC/2in1TabletTVWearable

addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>

为内容类型为ENVELOPED\_DATA的CMS添加接收者信息。使用Promise异步回调。

该方法至少需要设置一个接收者。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipientInfo | [CmsRecipientInfo](js-apis-cert.md#cmsrecipientinfo22) | 是 | 接收者信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The type of recipient certificate is invalid or not supported;  2. The digestAlgorithm of CmsKeyAgreeRecipientInfo is invalid or not supported;  3. The recipientInfo does not have any recipient info. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let eccCertData = '-----BEGIN CERTIFICATE-----\n' +
4. 'MIICOjCCAd+gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMHkxCzAJBgNVBAYTAmNo\n' +
5. 'MQ8wDQYDVQQIDAZodWF3ZWkxDTALBgNVBAcMBHhpYW4xDzANBgNVBAoMBmh1YXdl\n' +
6. 'aTENMAsGA1UECwwEdGVzdDENMAsGA1UEAwwEYW5uZTEbMBkGCSqGSIb3DQEJARYM\n' +
7. 'dGVzdEAxMjMuY29tMB4XDTI0MTEyNzAzMjQ1MFoXDTM0MTEyNTAzMjQ1MFoweTEL\n' +
8. 'MAkGA1UEBhMCY2gxDzANBgNVBAgMBmh1YXdlaTENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
9. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDARhbm5lMRswGQYJ\n' +
10. 'KoZIhvcNAQkBFgx0ZXN0QDEyMy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\n' +
11. 'AARzg16D6tsNHZa7w0tLHFprXg5kUQgXv/vv3KIM21hY+WDYMz1OST4tmTeQWQF8\n' +
12. 'kARtjjbHBxtOPufWxMfxf51Wo1MwUTAdBgNVHQ4EFgQUU/P31GCBwyrj3yXkoNaX\n' +
13. 'xvPp8uIwHwYDVR0jBBgwFoAUU/P31GCBwyrj3yXkoNaXxvPp8uIwDwYDVR0TAQH/\n' +
14. 'BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA/wCfbTorAWEEZcgd0CgfXI+EzXu2\n' +
15. 'Y88BmDD5LFlj3N0CIQDB34h77Li0CSpYpS4+7Mug237zbkFjHR3Q4/VWOT1G1A==\n' +
16. '-----END CERTIFICATE-----\n';

18. let rsaCertData = '-----BEGIN CERTIFICATE-----\n' +
19. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
20. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
21. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
22. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
23. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
24. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
25. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
26. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
27. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
28. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
29. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
30. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
31. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
32. '-----END CERTIFICATE-----\n';

34. // string转Uint8Array。
35. function stringToUint8Array(str: string): Uint8Array {
36. let arr: number[] = [];
37. for (let i = 0, j = str.length; i < j; i++) {
38. arr.push(str.charCodeAt(i));
39. }
40. return new Uint8Array(arr);
41. }

43. async function testAddRecipientInfo() {
44. let ecccertEncodingBlob: cert.EncodingBlob = {
45. data: stringToUint8Array(eccCertData),
46. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
47. encodingFormat: cert.EncodingFormat.FORMAT_PEM
48. };

50. let rsacertEncodingBlob: cert.EncodingBlob = {
51. data: stringToUint8Array(rsaCertData),
52. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
53. encodingFormat: cert.EncodingFormat.FORMAT_PEM
54. };
55. try {
56. let eccx509Certcert = await cert.createX509Cert(ecccertEncodingBlob);
57. let rsax509Certcert = await cert.createX509Cert(rsacertEncodingBlob);
58. let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
59. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
60. console.info(`createCmsGenerator result: success.`);

62. let eccCert : cert.CmsKeyAgreeRecipientInfo = {
63. cert : eccx509Certcert,
64. digestAlgorithm : cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256,
65. };
66. let rsaCert : cert.CmsKeyTransRecipientInfo = {
67. cert : rsax509Certcert,
68. };
69. let recipientInfo: cert.CmsRecipientInfo = {
70. keyTransInfo : rsaCert,
71. keyAgreeInfo : eccCert,
72. };
73. await cmsGenerator.addRecipientInfo(recipientInfo);
74. console.info(`addRecipientInfo result: success.`);
75. } catch (err) {
76. console.error(`testAddRecipientInfo failed: errCode: ${err.code}, errMsg: ${err.message}`);
77. }
78. }
```

### doFinal18+

PhonePC/2in1TabletTVWearable

doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>

用于获取CMS最终数据，例如CMS签名数据或CMS封装数据。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Cms操作的内容。 |
| options | [CmsGeneratorOptions](js-apis-cert.md#cmsgeneratoroptions18) | 否 | Cms操作的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array | string> | 返回Cms最终数据的Promise。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. let rsaStr1024: string  =
21. '-----BEGIN RSA PRIVATE KEY-----\n' +
22. 'Proc-Type: 4,ENCRYPTED\n' +
23. 'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
24. '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
25. 'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
26. 'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
27. 'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
28. 'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
29. 'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
30. 'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
31. '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
32. 'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
33. 'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
34. 'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
35. 'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
36. '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
37. '-----END RSA PRIVATE KEY-----\n';

39. // string转Uint8Array。
40. function stringToUint8Array(str: string): Uint8Array {
41. let arr: Array<number> = [];
42. for (let i = 0, j = str.length; i < j; i++) {
43. arr.push(str.charCodeAt(i));
44. }
45. return new Uint8Array(arr);
46. }

48. async function testDoFinalByPromise() {
49. let certEncodingBlob: cert.EncodingBlob = {
50. data: stringToUint8Array(certData),
51. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
52. encodingFormat: cert.EncodingFormat.FORMAT_PEM
53. };
54. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
55. if (error) {
56. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
57. } else {
58. try {
59. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
60. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
61. console.info('testDoFinalByPromise createCmsGenerator result: success.');
62. let privateKeyInfo: cert.PrivateKeyInfo = {
63. key: rsaStr1024,
64. password: '123456'
65. };
66. // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
67. let config: cert.CmsSignerConfig = {
68. mdName:'SHA256',
69. addCert:false,
70. addAttr:true,
71. addSmimeCapAttr:true
72. }
73. cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
74. console.info('testDoFinalByPromise addSigner result: success.');
75. cmsGenerator.addCert(x509Cert);
76. console.info('testDoFinalByPromise addCert result: success.');
77. let content = new Uint8Array([1,2,3,4]);
78. let optionsFinal: cert.CmsGeneratorOptions = {
79. contentDataFormat : cert.CmsContentDataFormat.BINARY,
80. outFormat : cert.CmsFormat.PEM,
81. isDetached : true
82. };
83. cmsGenerator.doFinal(content, optionsFinal).then(result => {
84. console.info('testDoFinalByPromise doFinal result: success, result = %s', result);
85. }).catch((error: BusinessError) => {
86. console.error(`testDoFinalByPromise failed, errCode: ${error.code}, errMsg: ${error.message}`);
87. });
88. } catch (err) {
89. let e: BusinessError = err as BusinessError;
90. console.error(`testDoFinalByPromise failed, errCode: ${e.code}, errMsg: ${e.message}`);
91. }
92. }
93. });
94. }
```

### doFinalSync18+

PhonePC/2in1TabletTVWearable

doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string

用于获取CMS最终数据，例如CMS签名数据或CMS封装数据。（同步方法）。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Cms操作的内容。 |
| options | [CmsGeneratorOptions](js-apis-cert.md#cmsgeneratoroptions18) | 否 | Cms操作的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | string | 返回Cms最终数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. let rsaStr1024: string  =
21. '-----BEGIN RSA PRIVATE KEY-----\n' +
22. 'Proc-Type: 4,ENCRYPTED\n' +
23. 'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
24. '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
25. 'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
26. 'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
27. 'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
28. 'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
29. 'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
30. 'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
31. '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
32. 'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
33. 'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
34. 'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
35. 'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
36. '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
37. '-----END RSA PRIVATE KEY-----\n';

39. // string转Uint8Array。
40. function stringToUint8Array(str: string): Uint8Array {
41. let arr: Array<number> = [];
42. for (let i = 0, j = str.length; i < j; i++) {
43. arr.push(str.charCodeAt(i));
44. }
45. return new Uint8Array(arr);
46. }

48. function testDoFinalSync() {
49. let certEncodingBlob: cert.EncodingBlob = {
50. data: stringToUint8Array(certData),
51. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
52. encodingFormat: cert.EncodingFormat.FORMAT_PEM
53. };
54. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
55. if (error) {
56. console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
57. } else {
58. try {
59. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
60. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
61. console.info('testDoFinalSync createCmsGenerator result: success.');
62. let privateKeyInfo: cert.PrivateKeyInfo = {
63. key: rsaStr1024,
64. password: '123456'
65. };
66. // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
67. let config: cert.CmsSignerConfig = {
68. mdName:'SHA256',
69. addCert:false,
70. addAttr:false,
71. addSmimeCapAttr:false
72. }
73. cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
74. console.info('testDoFinalSync addSigner result: success.');
75. cmsGenerator.addCert(x509Cert);
76. console.info('testDoFinalSync addCert result: success.');
77. let content = new Uint8Array([1,2,3,4]);
78. let optionsFinal: cert.CmsGeneratorOptions = {
79. contentDataFormat : cert.CmsContentDataFormat.BINARY,
80. outFormat : cert.CmsFormat.DER,
81. isDetached : false
82. };
83. let output = cmsGenerator.doFinalSync(content, optionsFinal);
84. console.info('testDoFinalSync doFinalSync result: success, output = %s.',output);
85. } catch (err) {
86. let e: BusinessError = err as BusinessError;
87. console.error(`testDoFinalSync failed, errCode: ${e.code}, errMsg: ${e.message}`);
88. }
89. }
90. });
91. }
```

### getEncryptedContentData22+

PhonePC/2in1TabletTVWearable

getEncryptedContentData(): Promise<Uint8Array>

用于获取内容类型为ENVELOPED\_DATA的CMS的加密内容数据。使用Promise异步回调。

如果创建了类型为ENVELOPED\_DATA的CmsGenerator并使用了数据分离来生成CMS封装数据，使用此方法来获取加密的内容数据。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象, 返回加密的数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let eccCertData = '-----BEGIN CERTIFICATE-----\n' +
4. 'MIICOjCCAd+gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMHkxCzAJBgNVBAYTAmNo\n' +
5. 'MQ8wDQYDVQQIDAZodWF3ZWkxDTALBgNVBAcMBHhpYW4xDzANBgNVBAoMBmh1YXdl\n' +
6. 'aTENMAsGA1UECwwEdGVzdDENMAsGA1UEAwwEYW5uZTEbMBkGCSqGSIb3DQEJARYM\n' +
7. 'dGVzdEAxMjMuY29tMB4XDTI0MTEyNzAzMjQ1MFoXDTM0MTEyNTAzMjQ1MFoweTEL\n' +
8. 'MAkGA1UEBhMCY2gxDzANBgNVBAgMBmh1YXdlaTENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
9. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDARhbm5lMRswGQYJ\n' +
10. 'KoZIhvcNAQkBFgx0ZXN0QDEyMy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\n' +
11. 'AARzg16D6tsNHZa7w0tLHFprXg5kUQgXv/vv3KIM21hY+WDYMz1OST4tmTeQWQF8\n' +
12. 'kARtjjbHBxtOPufWxMfxf51Wo1MwUTAdBgNVHQ4EFgQUU/P31GCBwyrj3yXkoNaX\n' +
13. 'xvPp8uIwHwYDVR0jBBgwFoAUU/P31GCBwyrj3yXkoNaXxvPp8uIwDwYDVR0TAQH/\n' +
14. 'BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA/wCfbTorAWEEZcgd0CgfXI+EzXu2\n' +
15. 'Y88BmDD5LFlj3N0CIQDB34h77Li0CSpYpS4+7Mug237zbkFjHR3Q4/VWOT1G1A==\n' +
16. '-----END CERTIFICATE-----\n';

18. let rsaCertData = '-----BEGIN CERTIFICATE-----\n' +
19. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
20. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
21. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
22. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
23. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
24. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
25. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
26. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
27. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
28. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
29. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
30. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
31. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
32. '-----END CERTIFICATE-----\n';

34. // string转Uint8Array。
35. function stringToUint8Array(str: string): Uint8Array {
36. let arr: number[] = [];
37. for (let i = 0, j = str.length; i < j; i++) {
38. arr.push(str.charCodeAt(i));
39. }
40. return new Uint8Array(arr);
41. }

43. async function testGetEncryptedContentData() {
44. try {
45. let ecccertEncodingBlob: cert.EncodingBlob = {
46. data: stringToUint8Array(eccCertData),
47. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
48. encodingFormat: cert.EncodingFormat.FORMAT_PEM
49. };

51. let rsacertEncodingBlob: cert.EncodingBlob = {
52. data: stringToUint8Array(rsaCertData),
53. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
54. encodingFormat: cert.EncodingFormat.FORMAT_PEM
55. };

57. let eccx509Certcert = await cert.createX509Cert(ecccertEncodingBlob);
58. let rsax509Certcert = await cert.createX509Cert(rsacertEncodingBlob);

60. let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
61. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
62. console.info(`createCmsGenerator result: success.`);
63. let algorithm = cert.CmsRecipientEncryptionAlgorithm.AES_256_GCM;
64. cmsGenerator.setRecipientEncryptionAlgorithm(algorithm);
65. console.info(`setRecipientEncryptionAlgorithm result: success.`);
66. let eccCert : cert.CmsKeyAgreeRecipientInfo = {
67. cert : eccx509Certcert,
68. digestAlgorithm : cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256,
69. };
70. let rsaCert : cert.CmsKeyTransRecipientInfo = {
71. cert : rsax509Certcert,
72. };
73. let recipientInfo: cert.CmsRecipientInfo = {
74. keyTransInfo : rsaCert,
75. keyAgreeInfo : eccCert,
76. };
77. await cmsGenerator.addRecipientInfo(recipientInfo);
78. console.info(`addRecipientInfo result: success.`);
79. let content = new Uint8Array([1,2,3,4]);
80. let optionsFinal: cert.CmsGeneratorOptions = {
81. contentDataFormat : cert.CmsContentDataFormat.BINARY,
82. outFormat : cert.CmsFormat.PEM,
83. isDetached : true
84. };
85. let cms = await cmsGenerator.doFinal(content, optionsFinal);
86. console.info(`doFinal result: success, cms = %s`, cms);
87. let data = await cmsGenerator.getEncryptedContentData();
88. console.info(`getEncryptedContentData result: success, data = %s`, data);
89. } catch (err) {
90. console.error(`testGetEncryptedContentData failed: errCode: ${err.code}, errMsg: ${err.message}`);
91. }
92. }
```

## cert.createCmsParser22+

PhonePC/2in1TabletTVWearable

createCmsParser(): CmsParser

表示创建CmsParser对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CmsParser](js-apis-cert.md#cmsparser22) | CmsParser对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. };
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);
76. return x509Cert;
77. }

79. async function testCmsVerifyTest() {
80. try {
81. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
82. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
83. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
84. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
85. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
86. let signerConfig: cert.CmsSignerConfig = {
87. mdName: 'SHA256',
88. };
89. let keyInfo: cert.PrivateKeyInfo = {
90. key: ECC_256_PRI_ENTRY_KEY
91. };
92. let option: cert.CmsGeneratorOptions = {
93. outFormat: cert.CmsFormat.PEM
94. };
95. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
96. let signData = cms.doFinalSync(plainText, option);
97. let config: cert.CmsVerificationConfig = {
98. trustCerts: [x509CertRoot, x509CertInter],
99. };
100. let verify: cert.CmsParser = cert.createCmsParser();
101. await verify.setRawData(signData, cert.CmsFormat.PEM);
102. await verify.verifySignedData(config);
103. console.info('verifySignedData result: success.');
104. } catch (error) {
105. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
106. }
107. }
```

## CmsParser22+

PhonePC/2in1TabletTVWearable

CmsParser对象用于对已签名跟封装的CMS（Cryptographic Message Syntax）格式的消息进行验签和解封装。

说明

PKCS#7是用于存储签名或加密数据的标准语法。注意CMS是PKCS#7的扩展，PKCS#7支持的数据类型包括数据、签名数据、信封数据、

签名和信封数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

### setRawData22+

PhonePC/2in1TabletTVWearable

setRawData(data: Uint8Array | string, cmsFormat: CmsFormat): Promise<void>

用于把CMS格式的数据转成CMS对象。使用Promise异步回调。

说明

支持PEM跟DER格式的CMS数据。string对应PEM格式；Uint8Array对应DER格式数据。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | string | 是 | CMS数据内容。 |
| cmsFormat | [CmsFormat](js-apis-cert.md#cmsformat18) | 是 | 指定输入的CMS格式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The length of the data is zero or too large;  2. The type of the cmsFormat is invalid or not supported. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. }
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM

75. };
76. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

78. return x509Cert;
79. }

81. async function testCmsVerifyTest() {
82. try {
83. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
84. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
85. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
86. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
87. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
88. let signerConfig: cert.CmsSignerConfig = {
89. mdName: 'SHA256',
90. };
91. let keyInfo: cert.PrivateKeyInfo = {
92. key: ECC_256_PRI_ENTRY_KEY
93. };
94. let option: cert.CmsGeneratorOptions = {
95. outFormat: cert.CmsFormat.PEM
96. };
97. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
98. let signData = cms.doFinalSync(plainText, option);
99. let config: cert.CmsVerificationConfig = {
100. trustCerts: [x509CertRoot, x509CertInter],
101. };
102. let verify: cert.CmsParser = cert.createCmsParser();
103. await verify.setRawData(signData, cert.CmsFormat.PEM);
104. await verify.verifySignedData(config);
105. console.info('verifySignedData result: success.');
106. } catch (error) {
107. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
108. }
109. }
```

### getContentType22+

PhonePC/2in1TabletTVWearable

getContentType(): CmsContentType

用于获取CMS的数据类型。当前支持获取签名数据、解封装数据两种类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CmsContentType](js-apis-cert.md#cmscontenttype18) | 返回CMS数据类型。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. };
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM

75. };
76. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

78. return x509Cert;
79. }

81. async function testCmsVerifyTest() {
82. try {
83. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
84. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
85. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
86. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
87. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
88. let signerConfig: cert.CmsSignerConfig = {
89. mdName: 'SHA256',
90. };
91. let keyInfo: cert.PrivateKeyInfo = {
92. key: ECC_256_PRI_ENTRY_KEY
93. };
94. let option: cert.CmsGeneratorOptions = {
95. outFormat: cert.CmsFormat.PEM
96. };
97. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
98. let signData = cms.doFinalSync(plainText, option);
99. let config: cert.CmsVerificationConfig = {
100. trustCerts: [x509CertRoot, x509CertInter],
101. };
102. let verify: cert.CmsParser = cert.createCmsParser();
103. await verify.setRawData(signData, cert.CmsFormat.PEM);
104. let contentType: cert.CmsContentType = verify.getContentType();
105. console.info('contentType = ' + contentType);
106. await verify.verifySignedData(config);
107. console.info('verifySignedData result: success.');
108. } catch (error) {
109. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
110. }
111. }
```

### verifySignedData22+

PhonePC/2in1TabletTVWearable

verifySignedData(config: CmsVerificationConfig): Promise<void>

用于验证Signed\_DATA内容类型的CMS。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CmsVerificationConfig](js-apis-cert.md#cmsverificationconfig22) | 是 | CMS验签配置内容。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The trustCerts of config is empty;  2. The length of the contentData of config is zero or too large;  3. The contentDataFormat of config is invalid or not supported. |
| 19030001 | crypto operation error. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. };
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

77. return x509Cert;
78. }

80. async function testCmsVerifyTest() {
81. try {
82. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
83. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
84. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
85. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
86. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
87. let signerConfig: cert.CmsSignerConfig = {
88. mdName: 'SHA256',
89. };
90. let keyInfo: cert.PrivateKeyInfo = {
91. key: ECC_256_PRI_ENTRY_KEY
92. };
93. let option: cert.CmsGeneratorOptions = {
94. outFormat: cert.CmsFormat.PEM
95. };
96. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
97. let signData = cms.doFinalSync(plainText, option);
98. let config: cert.CmsVerificationConfig = {
99. trustCerts: [x509CertRoot, x509CertInter],
100. };
101. let verify: cert.CmsParser = cert.createCmsParser();
102. await verify.setRawData(signData, cert.CmsFormat.PEM);
103. await verify.verifySignedData(config);
104. console.info('verifySignedData result: success.');
105. } catch (error) {
106. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
107. }
108. }
```

### getContentData22+

PhonePC/2in1TabletTVWearable

getContentData(): Promise<Uint8Array>

用于从签名类型的CMS数据中获取明文数据。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回CMS原始数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. }
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

77. return x509Cert;
78. }

80. async function testCmsVerifyTest() {
81. try {
82. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
83. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
84. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
85. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
86. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
87. let signerConfig: cert.CmsSignerConfig = {
88. mdName: 'SHA256',
89. };
90. let keyInfo: cert.PrivateKeyInfo = {
91. key: ECC_256_PRI_ENTRY_KEY
92. };
93. let option: cert.CmsGeneratorOptions = {
94. outFormat: cert.CmsFormat.PEM
95. };
96. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
97. let signData = cms.doFinalSync(plainText, option);
98. let config: cert.CmsVerificationConfig = {
99. trustCerts: [x509CertRoot, x509CertInter],
100. };
101. let verify: cert.CmsParser = cert.createCmsParser();
102. await verify.setRawData(signData, cert.CmsFormat.PEM);
103. await verify.verifySignedData(config);
104. console.info('verifySignedData result: success.');
105. let contentData = await verify.getContentData();
106. console.info('getContentData result: success, contentData = ' + contentData);
107. } catch (error) {
108. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
109. }
110. }
```

### getCerts22+

PhonePC/2in1TabletTVWearable

getCerts(type: CmsCertType): Promise<Array<[X509Cert](js-apis-cert.md#x509cert)>>

传入枚举值，用于从签名类型的CMS数据中获取证书。当前支持获取签名者证书或全部证书。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [CmsCertType](js-apis-cert.md#cmscerttype22) | 是 | 从cms中获取证书的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[X509Cert](js-apis-cert.md#x509cert)>> | Promise对象，返回证书集合。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The type of the cmsFormat is invalid or not supported. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: Array<number> = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. }
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM

75. };
76. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

78. return x509Cert;
79. }

81. async function testCmsVerifyTest() {
82. try {
83. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
84. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
85. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
86. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
87. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
88. let signerConfig: cert.CmsSignerConfig = {
89. mdName: 'SHA256',
90. };
91. let keyInfo: cert.PrivateKeyInfo = {
92. key: ECC_256_PRI_ENTRY_KEY
93. };
94. let option: cert.CmsGeneratorOptions = {
95. outFormat: cert.CmsFormat.PEM
96. };
97. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
98. let signData = cms.doFinalSync(plainText, option);
99. let config: cert.CmsVerificationConfig = {
100. trustCerts: [x509CertRoot, x509CertInter],
101. };
102. let verify: cert.CmsParser = cert.createCmsParser();
103. await verify.setRawData(signData, cert.CmsFormat.PEM);
104. await verify.verifySignedData(config);
105. console.info('verifySignedData result: success.');
106. let signerCerts: cert.X509Cert[] = await verify.getCerts(cert.CmsCertType.SIGNER_CERTS);
107. console.info('getCerts result: success, signerCerts.length = ' + signerCerts.length);
108. await verify.getContentData();
109. } catch (error) {
110. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
111. }
112. }
```

### decryptEnvelopedData22+

PhonePC/2in1TabletTVWearable

decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>

用于验证Enveloped\_DATA内容类型的CMS。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [CmsEnvelopedDecryptionConfig](js-apis-cert.md#cmsenvelopeddecryptionconfig22) | 是 | CMS解封装配置内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回解封装结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](errorcode-cert.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes:  1. Memory copy failed;  2. A null pointer occurs inside the system;  3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes:  1. The private key is invalid or not supported;  2. The recipient certificate is invalid or not supported. |
| 19030001 | crypto operation error. |

**示例：**

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUBKEY: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICGDCCAb6gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMFcxCzAJBgNVBAYTAkNO\n' +
6. 'MQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG5rWL\n' +
7. '6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwOTE2MDY0MTMwWhcNMzUw\n' +
8. 'OTE0MDY0MTMwWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8wDQYD\n' +
9. 'VQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH5rWL\n' +
10. '6K+VMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB06h4SzOryi3d7PW9yN2wACC\n' +
11. 'VxlduBQjVLWZlDKhFKkdZjve8mUyytSSbBj/rrzR2XmzUzofuNkUbAtje3DDJqN2\n' +
12. 'MHQwHQYDVR0OBBYEFNtUldgBESf31bwTnYtApIctaSdtMB8GA1UdIwQYMBaAFNtU\n' +
13. 'ldgBESf31bwTnYtApIctaSdtMAsGA1UdDwQEAwIBBjAJBgNVHREEAjAAMAkGA1Ud\n' +
14. 'EgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAzxzaG2vR\n' +
15. 'zUnFFL3X3lRQ0IOJrb6cvkSZuaFd4bW2lgUCIHW6QGGnECDFMbDNz7Og9kjkt+3k\n' +
16. 'FmEJWqEMYudBH3Ul\n' +
17. '-----END CERTIFICATE-----';
18. let ECC_256_PRIVATE: string =
19. '-----BEGIN PRIVATE KEY-----\n' +
20. 'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOYwEyIw3ZNIAL4xO\n' +
21. 'pP6eVcQYcrL2sfnt6vB0z9tKmMmhRANCAAQHTqHhLM6vKLd3s9b3I3bAAIJXGV24\n' +
22. 'FCNUtZmUMqEUqR1mO97yZTLK1JJsGP+uvNHZebNTOh+42RRsC2N7cMMm\n' +
23. '-----END PRIVATE KEY-----';

25. // string转Uint8Array。
26. function stringToUint8Array(str: string): Uint8Array {
27. let arr: Array<number> = [];
28. for (let i = 0, j = str.length; i < j; i++) {
29. arr.push(str.charCodeAt(i));
30. }
31. return new Uint8Array(arr);
32. }

34. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(inStream),
37. encodingFormat: cert.EncodingFormat.FORMAT_PEM
38. };
39. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

41. return x509Cert;
42. }

44. async function testCmsDecryptTest() {
45. try {
46. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
47. let x509CertEc: cert.X509Cert = await createX509Cert(ECC_256_PUBKEY);
48. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.ENVELOPED_DATA);
49. let option: cert.CmsGeneratorOptions = {
50. outFormat: cert.CmsFormat.PEM
51. };
52. cms.setRecipientEncryptionAlgorithm(cert.CmsRecipientEncryptionAlgorithm.AES_128_GCM);
53. let recipientInfo: cert.CmsRecipientInfo = {
54. keyAgreeInfo: {
55. cert: x509CertEc,
56. digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256
57. }
58. };
59. await cms.addRecipientInfo(recipientInfo);
60. console.info('addRecipientInfo result: success, recipientInfo.keyAgreeInfo.digestAlgorithm = ' +
61. recipientInfo.keyAgreeInfo?.digestAlgorithm);
62. let envelopeData = await cms.doFinal(plainText, option);
63. console.info('doFinal result: success, envelopeData = ' + envelopeData);
64. let cipherText = await cms.getEncryptedContentData();
65. console.info('getEncryptedContentData result: success, cipherText = ' + cipherText);
66. let config: cert.CmsEnvelopedDecryptionConfig = {
67. keyInfo: {
68. key: ECC_256_PRIVATE
69. },
70. };
71. let cmsDecrypt: cert.CmsParser = cert.createCmsParser();
72. await cmsDecrypt.setRawData(envelopeData, cert.CmsFormat.PEM);
73. let decPlainText: Uint8Array = await cmsDecrypt.decryptEnvelopedData(config);
74. console.info('[XTS] Decrypt result: success, decPlainText = ' + decPlainText);
75. console.info('decryptEnvelopedData result: success.');
76. } catch (error) {
77. console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
78. }
79. }
```
