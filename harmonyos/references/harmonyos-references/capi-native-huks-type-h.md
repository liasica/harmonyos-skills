---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h
title: native_huks_type.h
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 头文件 > native_huks_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee09b561710a1c63c575a6c5a0f1136736e557f9f6672e430457be725b0853e4
---

## 概述

PhonePC/2in1TabletTVWearable

提供huks中的枚举变量、结构体定义与宏定义。

**引用文件：** <huks/native\_huks\_type.h>

**库：** libhuks\_ndk.z.so

**系统能力：** SystemCapability.Security.Huks.Core

在API 9-19，系统能力为SystemCapability.Security.Huks；从API 20起，系统能力变更为SystemCapability.Security.Huks.Core

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 表示状态返回数据，包括返回码和消息。 |
| [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) | 定义存放数据的结构体类型。 |
| [OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) | 定义参数集中的参数结构体类型。 |
| [OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) | 定义参数集的结构体类型。 |
| [OH\_Huks\_CertChain](capi-hukstypeapi-oh-huks-certchain.md) | 定义证书链的结构体类型。 |
| [OH\_Huks\_KeyInfo](capi-hukstypeapi-oh-huks-keyinfo.md) | 定义密钥信息的结构体类型。 |
| [OH\_Huks\_PubKeyInfo](capi-hukstypeapi-oh-huks-pubkeyinfo.md) | 定义公钥信息的结构体类型。 |
| [OH\_Huks\_KeyMaterialRsa](capi-hukstypeapi-oh-huks-keymaterialrsa.md) | 定义Rsa密钥的结构体类型。 |
| [OH\_Huks\_KeyMaterialEcc](capi-hukstypeapi-oh-huks-keymaterialecc.md) | 定义Ecc密钥的结构体类型。 |
| [OH\_Huks\_KeyMaterialDsa](capi-hukstypeapi-oh-huks-keymaterialdsa.md) | 定义Dsa密钥的结构体类型。 |
| [OH\_Huks\_KeyMaterialDh](capi-hukstypeapi-oh-huks-keymaterialdh.md) | 定义Dh密钥的结构体类型。 |
| [OH\_Huks\_KeyMaterial25519](capi-hukstypeapi-oh-huks-keymaterial25519.md) | 定义25519类型密钥的结构体类型。 |
| [OH\_Huks\_KeyAliasSet](capi-hukstypeapi-oh-huks-keyaliasset.md) | 定义密钥别名集的结构体类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Huks\_KeyPurpose](capi-native-huks-type-h.md#oh_huks_keypurpose) | - | 密钥用途类型。 |
| [OH\_Huks\_KeyDigest](capi-native-huks-type-h.md#oh_huks_keydigest) | - | 摘要算法类型。 |
| [OH\_Huks\_KeyPadding](capi-native-huks-type-h.md#oh_huks_keypadding) | - | 填充算法类型。 |
| [OH\_Huks\_CipherMode](capi-native-huks-type-h.md#oh_huks_ciphermode) | - | 加密模式。 |
| [OH\_Huks\_KeySize](capi-native-huks-type-h.md#oh_huks_keysize) | - | 算法密钥长度。 |
| [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) | - | 密钥使用的算法。 |
| [OH\_Huks\_AlgSuite](capi-native-huks-type-h.md#oh_huks_algsuite) | - | 密文导入所需的算法套件类型。 |
| [OH\_Huks\_KeyGenerateType](capi-native-huks-type-h.md#oh_huks_keygeneratetype) | - | 生成的密钥类型。 |
| [OH\_Huks\_KeyFlag](capi-native-huks-type-h.md#oh_huks_keyflag) | - | 密钥的产生方式。 |
| [OH\_Huks\_KeyStorageType](capi-native-huks-type-h.md#oh_huks_keystoragetype) | - | 密钥的存储方式。 |
| [OH\_Huks\_ImportKeyType](capi-native-huks-type-h.md#oh_huks_importkeytype) | - | 导入密钥的类型，默认为导入公钥，导入对称密钥时不需要该字段。 |
| [OH\_Huks\_RsaPssSaltLenType](capi-native-huks-type-h.md#oh_huks_rsapsssaltlentype) | - | PSS填充模式下盐值长度类型。 |
| [OH\_Huks\_ErrCode](capi-native-huks-type-h.md#oh_huks_errcode) | - | 错误码。 |
| [OH\_Huks\_TagType](capi-native-huks-type-h.md#oh_huks_tagtype) | - | 参数集中参数的类型。 |
| [OH\_Huks\_UserAuthType](capi-native-huks-type-h.md#oh_huks_userauthtype) | - | 密钥访问控制中的用户认证类型。 |
| [OH\_Huks\_AuthAccessType](capi-native-huks-type-h.md#oh_huks_authaccesstype) | - | 安全访问控制类型，表示密钥失效的原则。 |
| [OH\_Huks\_AuthStorageLevel](capi-native-huks-type-h.md#oh_huks_authstoragelevel) | - | 表示生成或导入密钥时，指定该密钥的存储安全等级。 |
| [OH\_Huks\_ChallengeType](capi-native-huks-type-h.md#oh_huks_challengetype) | - | 密钥使用时生成challenge的类型。 |
| [OH\_Huks\_UserAuthMode](capi-native-huks-type-h.md#oh_huks_userauthmode) | - | 密钥访问控制中的用户认证模式。 |
| [OH\_Huks\_ChallengePosition](capi-native-huks-type-h.md#oh_huks_challengeposition) | - | challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置。 |
| [OH\_Huks\_SecureSignType](capi-native-huks-type-h.md#oh_huks_securesigntype) | - | 生成或导入密钥时，指定该密钥的安全签名类型。 |
| [OH\_Huks\_KeyClassType](capi-native-huks-type-h.md#oh_huks_keyclasstype) | OH\_Huks\_KeyClassType | 密钥类型。 |
| [OH\_Huks\_KeyWrapType](capi-native-huks-type-h.md#oh_huks_keywraptype) | - | 生成或导入密钥时，指定该密钥的封装类型。 |
| [OH\_Huks\_Tag](capi-native-huks-type-h.md#oh_huks_tag) | - | 参数集所用的TAG值枚举。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_HUKS\_AE\_TAG\_LEN 16 | AEAD认证标签的字节长度。  **起始版本：** 9 |
| OH\_HUKS\_BITS\_PER\_BYTE 8 | 每个字节的比特位数。  **起始版本：** 9 |
| OH\_HUKS\_MAX\_KEY\_SIZE 2048 | 密钥最大字节长度。  **起始版本：** 9 |
| OH\_HUKS\_AE\_NONCE\_LEN 12 | AEAD一次性随机数的字节长度。  **起始版本：** 9 |
| OH\_HUKS\_MAX\_KEY\_ALIAS\_LEN 64 | 密钥别名最大字节长度。  **起始版本：** 9 |
| OH\_HUKS\_MAX\_PROCESS\_NAME\_LEN 50 | 进程名最大字节长度。  **起始版本：** 9 |
| OH\_HUKS\_MAX\_RANDOM\_LEN 1024 | 随机数的最大字节长度。  **起始版本：** 9 |
| OH\_HUKS\_SIGNATURE\_MIN\_SIZE 64 | 签名结果的最小字节长度。  **起始版本：** 9 |
| OH\_HUKS\_MAX\_OUT\_BLOB\_SIZE (5 \* 1024 \* 1024) | 导出数据最大字节数。  **起始版本：** 9 |
| OH\_HUKS\_WRAPPED\_FORMAT\_MAX\_SIZE (1024 \* 1024) | 待导入加密密钥的最大字节数。  **起始版本：** 9 |
| OH\_HUKS\_IMPORT\_WRAPPED\_KEY\_TOTAL\_BLOBS 10 | 待导入加密密钥传入数据的数据块最大数量。  **起始版本：** 9 |
| TOKEN\_CHALLENGE\_LEN 32 | 在进行访问控制时挑战值的字节长度。  **起始版本：** 9 |
| SHA256\_SIGN\_LEN 32 | SHA256签名的字节长度。  **起始版本：** 9 |
| TOKEN\_SIZE 32 | 在进行访问控制时挑战值的字节长度。  **起始版本：** 9 |
| MAX\_AUTH\_TIMEOUT\_SECOND 60 | 最大用户认证超时时间。  **起始版本：** 9 |
| SECURE\_SIGN\_VERSION 0x01000001 | 安全签名数据的版本。  **起始版本：** 9 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Huks\_KeyPurpose

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyPurpose
```

**描述**

密钥用途类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT = 1 | 表示密钥用于对明文进行加密操作。 |
| OH\_HUKS\_KEY\_PURPOSE\_DECRYPT = 2 | 表示密钥用于对密文进行解密操作。 |
| OH\_HUKS\_KEY\_PURPOSE\_SIGN = 4 | 表示密钥用于对数据进行签名。 |
| OH\_HUKS\_KEY\_PURPOSE\_VERIFY = 8 | 表示密钥用于验证签名后的数据。 |
| OH\_HUKS\_KEY\_PURPOSE\_DERIVE = 16 | 表示密钥用于派生密钥。 |
| OH\_HUKS\_KEY\_PURPOSE\_WRAP = 32 | 表示密钥用于加密导出。 |
| OH\_HUKS\_KEY\_PURPOSE\_UNWRAP = 64 | 表示密钥加密导入。 |
| OH\_HUKS\_KEY\_PURPOSE\_MAC = 128 | 表示密钥用于生成mac消息验证码。 |
| OH\_HUKS\_KEY\_PURPOSE\_AGREE = 256 | 表示密钥用于进行密钥协商。 |

### OH\_Huks\_KeyDigest

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyDigest
```

**描述**

摘要算法类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_DIGEST\_NONE = 0 | 无摘要算法。 |
| OH\_HUKS\_DIGEST\_MD5 = 1 | MD5摘要算法。 |
| OH\_HUKS\_DIGEST\_SM3 = 2 | SM3摘要算法。 |
| OH\_HUKS\_DIGEST\_SHA1 = 10 | SHA1摘要算法。 |
| OH\_HUKS\_DIGEST\_SHA224 = 11 | SHA224摘要算法。 |
| OH\_HUKS\_DIGEST\_SHA256 = 12 | SHA256摘要算法。 |
| OH\_HUKS\_DIGEST\_SHA384 = 13 | SHA384摘要算法。 |
| OH\_HUKS\_DIGEST\_SHA512 = 14 | SHA512摘要算法。 |

### OH\_Huks\_KeyPadding

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyPadding
```

**描述**

填充算法类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_PADDING\_NONE = 0 | 不使用填充算法。 |
| OH\_HUKS\_PADDING\_OAEP = 1 | 使用OAEP填充算法。 |
| OH\_HUKS\_PADDING\_PSS = 2 | 使用PSS填充算法。 |
| OH\_HUKS\_PADDING\_PKCS1\_V1\_5 = 3 | 使用PKCS1\_V1\_5填充算法。 |
| OH\_HUKS\_PADDING\_PKCS5 = 4 | 使用PKCS5填充算法。 |
| OH\_HUKS\_PADDING\_PKCS7 = 5 | 使用PKCS7填充算法。 |
| OH\_HUKS\_PADDING\_ISO\_IEC\_9796\_2 = 6 | 使用ISO IEC 9796-2填充算法。  **起始版本：** 18 |
| OH\_HUKS\_PADDING\_ISO\_IEC\_9797\_1 = 7 | 使用ISO IEC 9797-1填充算法。  **起始版本：** 18 |

### OH\_Huks\_CipherMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_CipherMode
```

**描述**

加密模式。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_MODE\_ECB = 1 | 使用ECB模式。 |
| OH\_HUKS\_MODE\_CBC = 2 | 使用CBC模式。 |
| OH\_HUKS\_MODE\_CTR = 3 | 使用CTR模式。 |
| OH\_HUKS\_MODE\_OFB = 4 | 使用OFB模式。 |
| OH\_HUKS\_MODE\_CFB = 5 | 使用CFB模式。  **起始版本：** 12 |
| OH\_HUKS\_MODE\_CCM = 31 | 使用CCM模式。 |
| OH\_HUKS\_MODE\_GCM = 32 | 使用GCM模式。 |

### OH\_Huks\_KeySize

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeySize
```

**描述**

算法密钥长度。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_RSA\_KEY\_SIZE\_512 = 512 | 使用RSA算法的密钥长度为512bit。 |
| OH\_HUKS\_RSA\_KEY\_SIZE\_768 = 768 | 使用RSA算法的密钥长度为768bit。 |
| OH\_HUKS\_RSA\_KEY\_SIZE\_1024 = 1024 | 使用RSA算法的密钥长度为1024bit。 |
| OH\_HUKS\_RSA\_KEY\_SIZE\_2048 = 2048 | 使用RSA算法的密钥长度为2048bit。 |
| OH\_HUKS\_RSA\_KEY\_SIZE\_3072 = 3072 | 使用RSA算法的密钥长度为3072bit。 |
| OH\_HUKS\_RSA\_KEY\_SIZE\_4096 = 4096 | 使用RSA算法的密钥长度为4096bit。 |
| OH\_HUKS\_ECC\_KEY\_SIZE\_224 = 224 | 使用ECC算法的密钥长度为224bit。 |
| OH\_HUKS\_ECC\_KEY\_SIZE\_256 = 256 | 使用ECC算法的密钥长度为256bit。 |
| OH\_HUKS\_ECC\_KEY\_SIZE\_384 = 384 | 使用ECC算法的密钥长度为384bit。 |
| OH\_HUKS\_ECC\_KEY\_SIZE\_521 = 521 | 使用ECC算法的密钥长度为521bit。 |
| OH\_HUKS\_AES\_KEY\_SIZE\_128 = 128 | 使用AES算法的密钥长度为128bit。 |
| OH\_HUKS\_AES\_KEY\_SIZE\_192 = 192 | 使用AES算法的密钥长度为192bit。 |
| OH\_HUKS\_AES\_KEY\_SIZE\_256 = 256 | 使用AES算法的密钥长度为256bit。 |
| OH\_HUKS\_AES\_KEY\_SIZE\_512 = 512 | 使用AES算法的密钥长度为512bit。 |
| OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256 = 256 | 使用CURVE25519算法的密钥长度为256bit。 |
| OH\_HUKS\_DH\_KEY\_SIZE\_2048 = 2048 | 使用DH算法的密钥长度为2048bit。 |
| OH\_HUKS\_DH\_KEY\_SIZE\_3072 = 3072 | 使用DH算法的密钥长度为3072bit。 |
| OH\_HUKS\_DH\_KEY\_SIZE\_4096 = 4096 | 使用DH算法的密钥长度为4096bit。 |
| OH\_HUKS\_SM2\_KEY\_SIZE\_256 = 256 | 使用SM2算法的密钥长度为256bit。 |
| OH\_HUKS\_SM4\_KEY\_SIZE\_128 = 128 | 使用SM4算法支持的密钥长度为128位。 |
| OH\_HUKS\_DES\_KEY\_SIZE\_64 = 64 | 使用DES算法的密钥长度为64bit。  **起始版本：** 18 |
| OH\_HUKS\_3DES\_KEY\_SIZE\_128 = 128 | 使用3DES算法的密钥长度为128bit。  **起始版本：** 18 |
| OH\_HUKS\_3DES\_KEY\_SIZE\_192 = 192 | 使用3DES算法的密钥长度为192bit。  **起始版本：** 18 |

### OH\_Huks\_KeyAlg

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyAlg
```

**描述**

密钥使用的算法。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_ALG\_RSA = 1 | 使用RSA算法。 |
| OH\_HUKS\_ALG\_ECC = 2 | 使用ECC算法。 |
| OH\_HUKS\_ALG\_DSA = 3 | 使用DSA算法。 |
| OH\_HUKS\_ALG\_AES = 20 | 使用AES算法。 |
| OH\_HUKS\_ALG\_HMAC = 50 | 使用HMAC算法。 |
| OH\_HUKS\_ALG\_HKDF = 51 | 使用HKDF算法。 |
| OH\_HUKS\_ALG\_PBKDF2 = 52 | 使用PBKDF2算法。 |
| OH\_HUKS\_ALG\_ECDH = 100 | 使用ECDH算法。 |
| OH\_HUKS\_ALG\_X25519 = 101 | 使用X25519算法。 |
| OH\_HUKS\_ALG\_ED25519 = 102 | 使用ED25519算法。 |
| OH\_HUKS\_ALG\_DH = 103 | 使用DH算法。 |
| OH\_HUKS\_ALG\_SM2 = 150 | 使用SM2算法。 |
| OH\_HUKS\_ALG\_SM3 = 151 | 使用SM3算法。 |
| OH\_HUKS\_ALG\_SM4 = 152 | 使用SM4算法。 |
| OH\_HUKS\_ALG\_DES = 160 | 使用DES算法。  **起始版本：** 18 |
| OH\_HUKS\_ALG\_3DES = 161 | 使用3DES算法。  **起始版本：** 18 |
| OH\_HUKS\_ALG\_CMAC = 162 | 使用CMAC算法。  **起始版本：** 18 |

### OH\_Huks\_AlgSuite

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_AlgSuite
```

**描述**

密文导入所需的算法套件类型。

OH\_HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING对应的密钥材料格式：

```
1. | x25519_plain_pubkey_length  (4 Byte) | x25519_plain_pubkey |  agreekey_aad_length (4 Byte) | agreekey_aad
2. |   agreekey_nonce_length     (4 Byte) |   agreekey_nonce    | agreekey_aead_tag_len(4 Byte) | agreekey_aead_tag
3. |    kek_enc_data_length      (4 Byte) |    kek_enc_data     |    kek_aad_length    (4 Byte) | kek_aad
4. |      kek_nonce_length       (4 Byte) |      kek_nonce      |   kek_aead_tag_len   (4 Byte) | kek_aead_tag
5. |   key_material_size_len     (4 Byte) |  key_material_size  |   key_mat_enc_length (4 Byte) | key_mat_enc_data
```

OH\_HUKS\_UNWRAP\_SUITE\_ECDH\_AES\_256\_GCM\_NOPADDING对应的密钥材料格式：

```
1. |  ECC_plain_pubkey_length    (4 Byte) |  ECC_plain_pubkey   |  agreekey_aad_length (4 Byte) | agreekey_aad
2. |   agreekey_nonce_length     (4 Byte) |   agreekey_nonce    | agreekey_aead_tag_len(4 Byte) | agreekey_aead_tag
3. |    kek_enc_data_length      (4 Byte) |    kek_enc_data     |    kek_aad_length    (4 Byte) | kek_aad
4. |      kek_nonce_length       (4 Byte) |      kek_nonce      |   kek_aead_tag_len   (4 Byte) | kek_aead_tag
5. |   key_material_size_len     (4 Byte) |  key_material_size  |   key_mat_enc_length (4 Byte) | key_mat_enc_data
```

OH\_HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING对应的密钥材料格式：

```
1. | kek_SM4_enc_length (4 Byte) | EN_SM4_key | importkey_enc_length (4 Byte) | importkey_enc |
```

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING = 1 | 密文导入密钥材料格式（Length-Value格式）采用X25519密钥协商同时采用AES-256-GCM加解密。具体材料格式见上方枚举描述。 |
| OH\_HUKS\_UNWRAP\_SUITE\_ECDH\_AES\_256\_GCM\_NOPADDING = 2 | 密文导入密钥材料格式（Length-Value格式）采用ECDH-p256密钥协商同时采用AES-256-GCM加解密。具体材料格式见上方枚举描述。 |
| OH\_HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING = 5 | 密文导入密钥材料格式（Length-Value格式）使用临时SM4密钥加密导入密钥，使用已导入HUKS的SM2密钥加密SM4密钥。具体材料格式见上方枚举描述。  \*\*起始版本：\*\*23 |

### OH\_Huks\_KeyGenerateType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyGenerateType
```

**描述**

生成的密钥类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_DEFAULT = 0 | 默认生成的密钥。 |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_DERIVE = 1 | 派生生成的密钥。 |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_AGREE = 2 | 协商生成的密钥。 |

### OH\_Huks\_KeyFlag

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyFlag
```

**描述**

密钥的产生方式。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_FLAG\_IMPORT\_KEY = 1 | 通过导入公钥接口导入的密钥。 |
| OH\_HUKS\_KEY\_FLAG\_GENERATE\_KEY = 2 | 通过生成密钥接口生成的密钥。 |
| OH\_HUKS\_KEY\_FLAG\_AGREE\_KEY = 3 | 通过生成密钥协商接口生成的密钥。 |
| OH\_HUKS\_KEY\_FLAG\_DERIVE\_KEY = 4 | 通过生成密钥派生接口生成的密钥。 |

### OH\_Huks\_KeyStorageType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyStorageType
```

**描述**

密钥的存储方式。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_STORAGE\_TEMP = 0 | 通过接口返回给业务。 |
| OH\_HUKS\_STORAGE\_PERSISTENT = 1 | 密钥托管在HUKS中。 |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS = 2 | 在进行密钥派生或协商时，结果密钥托管在HUKS中。 |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED = 3 | 在进行密钥派生或协商时，结果密钥可以返回给业务。 |

### OH\_Huks\_ImportKeyType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_ImportKeyType
```

**描述**

导入密钥的类型，默认为导入公钥，导入对称密钥时不需要该字段。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_TYPE\_PUBLIC\_KEY = 0 | 导入的密钥类型为公钥。 |
| OH\_HUKS\_KEY\_TYPE\_PRIVATE\_KEY = 1 | 导入的密钥类型为私钥。 |
| OH\_HUKS\_KEY\_TYPE\_KEY\_PAIR = 2 | 导入的密钥类型为公私钥对。 |

### OH\_Huks\_RsaPssSaltLenType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_RsaPssSaltLenType
```

**描述**

PSS填充模式下盐值长度类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_RSA\_PSS\_SALT\_LEN\_DIGEST = 0 | 以摘要长度设置盐值长度。 |
| OH\_HUKS\_RSA\_PSS\_SALT\_LEN\_MAX = 1 | 以最大长度设置盐值长度。 |

### OH\_Huks\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_ErrCode
```

**描述**

错误码。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_SUCCESS = 0 | 成功。 |
| OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201 | 权限校验失败。 |
| OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 | 非法参数（通用）。 |
| OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801 | 不支持该API。 |
| OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 | 不支持该子功能（特性）。 |
| OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 | 缺少密钥算法参数。 |
| OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 | 无效的密钥算法参数。 |
| OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 | 文件错误。 |
| OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 | 进程通信错误。 |
| OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 | 算法库操作失败。 |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007 | 密钥访问失败 - 密钥已失效。 |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008 | 密钥访问失败 - 密钥认证失败。 |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009 | 密钥访问失败 - 密钥访问超时。 |
| OH\_HUKS\_ERR\_CODE\_SESSION\_LIMIT = 12000010 | 密钥操作会话数已达上限。 |
| OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 | 该项实体不存在。 |
| OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 | 内部错误。 |
| OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013 | 认证凭据不存在。 |
| OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 | 内存不足。 |
| OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 | 调用服务失败。 |
| OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016 | 需要锁屏密码，但没有设置。  **起始版本：** 11 |
| OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 | 同名密钥已存在。  **起始版本：** 20 |
| OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 | 输入的参数无效。  **起始版本：** 20 |
| OH\_HUKS\_ERR\_CODE\_ITEM\_EXISTS = 12000019 | 该项实体已存在。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 | 提供者或Ukey内部执行失败。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021 | Pin码被锁定。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_PIN\_INCORRECT = 12000022 | Pin码错误。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023 | Pin码未认证通过。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 | 提供者或Ukey中的资源正在被使用。  **起始版本：** 22 |
| OH\_HUKS\_ERR\_CODE\_EXCEED\_LIMIT = 12000025 | 资源超过限制。  **起始版本：** 22 |

### OH\_Huks\_TagType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_TagType
```

**描述**

参数集中参数的类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_TAG\_TYPE\_INVALID = 0 << 28 | 非法的Tag类型。 |
| OH\_HUKS\_TAG\_TYPE\_INT = 1 << 28 | 该Tag的数据类型为int32\_t类型。 |
| OH\_HUKS\_TAG\_TYPE\_UINT = 2 << 28 | 该Tag的数据类型为uin32\_t类型。 |
| OH\_HUKS\_TAG\_TYPE\_ULONG = 3 << 28 | 该Tag的数据类型为uin64\_t类型。 |
| OH\_HUKS\_TAG\_TYPE\_BOOL = 4 << 28 | 该Tag的数据类型为bool类型。 |
| OH\_HUKS\_TAG\_TYPE\_BYTES = 5 << 28 | 该Tag的数据类型为[OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md)类型。 |

**参考：**

[OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md)

### OH\_Huks\_UserAuthType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_UserAuthType
```

**描述**

密钥访问控制中的用户认证类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT = 1 << 0 | 用户认证类型为指纹。 |
| OH\_HUKS\_USER\_AUTH\_TYPE\_FACE = 1 << 1 | 用户认证类型为人脸。 |
| OH\_HUKS\_USER\_AUTH\_TYPE\_PIN = 1 << 2 | 用户认证类型为PIN码。 |
| OH\_HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN = 1 << 5 | 用户认证类型为TUI PIN码。  **起始版本：** 20 |

### OH\_Huks\_AuthAccessType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_AuthAccessType
```

**描述**

安全访问控制类型，表示密钥失效的原则。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_AUTH\_ACCESS\_INVALID\_CLEAR\_PASSWORD = 1 << 0 | 安全访问控制类型为清除密码后密钥无效。 |
| OH\_HUKS\_AUTH\_ACCESS\_INVALID\_NEW\_BIO\_ENROLL = 1 << 1 | 安全访问控制类型为新录入生物特征后密钥无效。 |
| OH\_HUKS\_AUTH\_ACCESS\_ALWAYS\_VALID = 1 << 2 | 安全访问控制类型为该密钥总是有效。  **起始版本：** 11 |

### OH\_Huks\_AuthStorageLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_AuthStorageLevel
```

**描述**

表示生成或导入密钥时，指定该密钥的存储安全等级。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_DE = 0 | 表示密钥仅在开机后可访问。 |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_CE = 1 | 表示密钥仅在首次解锁后可访问。 |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_ECE = 2 | 表示密钥仅在解锁状态时可访问。 |

说明

业务在使用存储等级为ECE的密钥时，建议通过感知[锁屏事件](commoneventmanager-definitions.md#common_event_screen_locked)来清理使用该密钥创建的会话资源，以保证安全性。

### OH\_Huks\_ChallengeType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_ChallengeType
```

**描述**

密钥使用时生成challenge的类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_CHALLENGE\_TYPE\_NORMAL = 0 | challenge为普通类型，默认32字节。 |
| OH\_HUKS\_CHALLENGE\_TYPE\_CUSTOM = 1 | challenge为用户自定义类型。支持使用多个密钥仅一次认证，challenge长度8字节有效。 |
| OH\_HUKS\_CHALLENGE\_TYPE\_NONE = 2 | 免challenge类型。 |

**参考：**

[OH\_Huks\_ChallengePosition](capi-native-huks-type-h.md#oh_huks_challengeposition)

### OH\_Huks\_UserAuthMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_UserAuthMode
```

**描述**

密钥访问控制中的用户认证模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_USER\_AUTH\_MODE\_LOCAL = 0 | 本地认证模式。 |
| OH\_HUKS\_USER\_AUTH\_MODE\_COAUTH = 1 | 跨端协同认证模式。 |

### OH\_Huks\_ChallengePosition

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_ChallengePosition
```

**描述**

challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_CHALLENGE\_POS\_0 = 0 | 0~7字节为当前密钥的有效challenge。 |
| OH\_HUKS\_CHALLENGE\_POS\_1 | 8~15字节为当前密钥的有效challenge。 |
| OH\_HUKS\_CHALLENGE\_POS\_2 | 16~23字节为当前密钥的有效challenge。 |
| OH\_HUKS\_CHALLENGE\_POS\_3 | 24~31字节为当前密钥的有效challenge。 |

### OH\_Huks\_SecureSignType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_SecureSignType
```

**描述**

生成或导入密钥时，指定该密钥的安全签名类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO = 1 | 签名类型为携带认证信息。生成或导入密钥时指定该字段，则在使用密钥进行签名时，对待签名的数据添加认证信息后进行签名。注意：携带的认证信息包含身份信息，开发者需在其隐私声明中对此身份信息的使用目的、存留策略和销毁方式进行说明。 |

### OH\_Huks\_KeyClassType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyClassType
```

**描述**

密钥类型。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_CLASS\_DEFAULT = 0 | 默认类型，指定密钥存储在HUKS中。 |
| OH\_HUKS\_KEY\_CLASS\_EXTENSION = 1 | 密钥存储在外部加密提供者中。 |

### OH\_Huks\_KeyWrapType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_KeyWrapType
```

**描述**

生成或导入密钥时，指定该密钥的封装类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_KEY\_WRAP\_TYPE\_HUK\_BASED = 2 | 硬件唯一密钥的封装类型。 |

### OH\_Huks\_Tag

PhonePC/2in1TabletTVWearable

```
1. enum OH_Huks_Tag
```

**描述**

参数集所用的TAG值枚举。

1-200：密钥参数标签值。

301-500：密钥使用访问控制和使用认证相关的标签值。

501-600：密钥认证相关的标签值。

601-1000：其他类型的标签值预留值。

1001-9999：扩展标签值。

11000-12000：预留值。

20001-N：其他标签预留值。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_TAG\_ALGORITHM = OH\_HUKS\_TAG\_TYPE\_UINT | 1 | 算法类型。 |
| OH\_HUKS\_TAG\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_UINT | 2 | 密钥用途。 |
| OH\_HUKS\_TAG\_KEY\_SIZE = OH\_HUKS\_TAG\_TYPE\_UINT | 3 | 密钥长度 。 |
| OH\_HUKS\_TAG\_DIGEST = OH\_HUKS\_TAG\_TYPE\_UINT | 4 | 摘要算法。 |
| OH\_HUKS\_TAG\_PADDING = OH\_HUKS\_TAG\_TYPE\_UINT | 5 | 填充算法。 |
| OH\_HUKS\_TAG\_BLOCK\_MODE = OH\_HUKS\_TAG\_TYPE\_UINT | 6 | 加密模式。 |
| OH\_HUKS\_TAG\_KEY\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 7 | 密钥类型。 |
| OH\_HUKS\_TAG\_ASSOCIATED\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 8 | 附加身份验证数据。 |
| OH\_HUKS\_TAG\_NONCE = OH\_HUKS\_TAG\_TYPE\_BYTES | 9 | 密钥加解密的NONCE字段。 |
| OH\_HUKS\_TAG\_IV = OH\_HUKS\_TAG\_TYPE\_BYTES | 10 | 初始化的向量。 |
| OH\_HUKS\_TAG\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 11 | 密钥派生时的信息。 |
| OH\_HUKS\_TAG\_SALT = OH\_HUKS\_TAG\_TYPE\_BYTES | 12 | 派生盐值。 |
| OH\_HUKS\_TAG\_ITERATION = OH\_HUKS\_TAG\_TYPE\_UINT | 14 | 派生迭代次数。 |
| OH\_HUKS\_TAG\_KEY\_GENERATE\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 15 | 生成密钥的类型，类型可在枚举[OH\_Huks\_KeyGenerateType](capi-native-huks-type-h.md#oh_huks_keygeneratetype)中选择。 |
| OH\_HUKS\_TAG\_AGREE\_ALG = OH\_HUKS\_TAG\_TYPE\_UINT | 19 | 密钥协商时的算法类型。 |
| OH\_HUKS\_TAG\_AGREE\_PUBLIC\_KEY\_IS\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BOOL | 20 | 密钥协商时的公钥别名。 |
| OH\_HUKS\_TAG\_AGREE\_PRIVATE\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 21 | 密钥协商时的私钥别名。 |
| OH\_HUKS\_TAG\_AGREE\_PUBLIC\_KEY = OH\_HUKS\_TAG\_TYPE\_BYTES | 22 | 用于协商的公钥。 |
| OH\_HUKS\_TAG\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 23 | 密钥别名。 |
| OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE = OH\_HUKS\_TAG\_TYPE\_UINT | 24 | 派生密钥大小。 |
| OH\_HUKS\_TAG\_IMPORT\_KEY\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 25 | 导入密钥类型，类型可在枚举[OH\_Huks\_ImportKeyType](capi-native-huks-type-h.md#oh_huks_importkeytype)中选择。 |
| OH\_HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE = OH\_HUKS\_TAG\_TYPE\_UINT | 26 | 导入加密密钥的套件。 |
| OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 29 | 派生密钥/协商密钥的存储类型，类型可在枚举[OH\_Huks\_KeyStorageType](capi-native-huks-type-h.md#oh_huks_keystoragetype)中选择。 |
| OH\_HUKS\_TAG\_RSA\_PSS\_SALT\_LEN\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 30 | RSA算法，填充模式为PSS时的盐值长度类型。 |
| OH\_HUKS\_TAG\_ALL\_USERS = OH\_HUKS\_TAG\_TYPE\_BOOL | 301 | 多用户中的所有用户。 |
| OH\_HUKS\_TAG\_USER\_ID = OH\_HUKS\_TAG\_TYPE\_UINT | 302 | 表示多用户id。 |
| OH\_HUKS\_TAG\_NO\_AUTH\_REQUIRED = OH\_HUKS\_TAG\_TYPE\_BOOL | 303 | 表示是否需要密钥访问控制。 |
| OH\_HUKS\_TAG\_USER\_AUTH\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 304 | 表示密钥访问控制中用户认证类型。 |
| OH\_HUKS\_TAG\_AUTH\_TIMEOUT = OH\_HUKS\_TAG\_TYPE\_UINT | 305 | 表示密钥访问控制类型中密钥访问的超时时间。 |
| OH\_HUKS\_TAG\_AUTH\_TOKEN = OH\_HUKS\_TAG\_TYPE\_BYTES | 306 | 表示密钥访问控制中使用密钥时传入的authtoken的类型。 |
| OH\_HUKS\_TAG\_KEY\_AUTH\_ACCESS\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 307 | 表示安全访问控制类型，需要和用户认证类型同时设置，类型可在枚举[OH\_Huks\_AuthAccessType](capi-native-huks-type-h.md#oh_huks_authaccesstype)中选择。 |
| OH\_HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 308 | 表示生成或导入密钥时，指定该密钥的签名类型。 |
| OH\_HUKS\_TAG\_CHALLENGE\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 309 | 表示密钥使用时生成的challenge类型，类型可在枚举[OH\_Huks\_ChallengeType](capi-native-huks-type-h.md#oh_huks_challengetype)中选择。 |
| OH\_HUKS\_TAG\_CHALLENGE\_POS = OH\_HUKS\_TAG\_TYPE\_UINT | 310 | 表示challenge类型为用户自定义类型时，huks产生的challenge有效长度仅为8字节连续的数据的位置，类型可在枚举[OH\_Huks\_ChallengePosition](capi-native-huks-type-h.md#oh_huks_challengeposition)中选择。 |
| OH\_HUKS\_TAG\_KEY\_AUTH\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_UINT | 311 | 表示密钥认证用途的类型。 |
| OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL = OH\_HUKS\_TAG\_TYPE\_UINT | 316 | 密钥文件存储访问控制的类别，类型可在枚举[OH\_Huks\_AuthStorageLevel](capi-native-huks-type-h.md#oh_huks_authstoragelevel)中选择。  **起始版本：** 11 |
| OH\_HUKS\_TAG\_USER\_AUTH\_MODE = OH\_HUKS\_TAG\_TYPE\_UINT | 319 | 表示密钥访问控制中用户认证模式，类型可在枚举[OH\_Huks\_UserAuthMode](capi-native-huks-type-h.md#oh_huks_userauthmode)中选择。  **起始版本：** 12 |
| OH\_HUKS\_TAG\_ATTESTATION\_CHALLENGE = OH\_HUKS\_TAG\_TYPE\_BYTES | 501 | 密钥认证时的挑战值。 |
| OH\_HUKS\_TAG\_ATTESTATION\_APPLICATION\_ID = OH\_HUKS\_TAG\_TYPE\_BYTES | 502 | 密钥认证时拥有该密钥的application的Id。 |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 511 | 密钥认证时的别名。 |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_SEC\_LEVEL\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 514 | 密钥认证时的安全凭据。 |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 515 | 密钥认证时的版本号。 |
| OH\_HUKS\_TAG\_KEY\_OVERRIDE = OH\_HUKS\_TAG\_TYPE\_BOOL | 520 | 是否覆写同名密钥。  **起始版本：** 20 |
| OH\_HUKS\_TAG\_AE\_TAG\_LEN = OH\_HUKS\_TAG\_TYPE\_UINT | 521 | CCM模式下指定的AEAD长度。  **起始版本：** 22 |
| OH\_HUKS\_TAG\_KEY\_CLASS = OH\_HUKS\_TAG\_TYPE\_UINT | 522 | 密钥类别，用于区分设备本地由HUKS管理的密钥或者外部装置中存储的密钥。  **起始版本：** 22 |
| OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP = OH\_HUKS\_TAG\_TYPE\_BYTES | 523 | 表示群组标识，在同一开发者ID下归属于相同的群组可共享该群组下的密钥。  **起始版本：** 23 |
| OH\_HUKS\_TAG\_IS\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BOOL | 1001 | 是否是密钥别名。 |
| OH\_HUKS\_TAG\_KEY\_STORAGE\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 1002 | 密钥存储方式的标签，类型可在枚举 [OH\_Huks\_KeyStorageType](capi-native-huks-type-h.md#oh_huks_keystoragetype)选择。 |
| OH\_HUKS\_TAG\_IS\_ALLOWED\_WRAP = OH\_HUKS\_TAG\_TYPE\_BOOL | 1003 | 是否允许密钥封装。 |
| OH\_HUKS\_TAG\_KEY\_WRAP\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 1004 | 密钥封装的类型。 |
| OH\_HUKS\_TAG\_KEY\_AUTH\_ID = OH\_HUKS\_TAG\_TYPE\_BYTES | 1005 | 密钥认证的ID。 |
| OH\_HUKS\_TAG\_KEY\_ROLE = OH\_HUKS\_TAG\_TYPE\_UINT | 1006 | 密钥角色。 |
| OH\_HUKS\_TAG\_KEY\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 1007 | 密钥标记，类型可在枚举[OH\_Huks\_KeyFlag](capi-native-huks-type-h.md#oh_huks_keyflag)选择。 |
| OH\_HUKS\_TAG\_IS\_ASYNCHRONIZED = OH\_HUKS\_TAG\_TYPE\_UINT | 1008 | 是否异步。 |
| OH\_HUKS\_TAG\_KEY\_DOMAIN = OH\_HUKS\_TAG\_TYPE\_UINT | 1011 | 密钥域。 |
| OH\_HUKS\_TAG\_IS\_DEVICE\_PASSWORD\_SET = OH\_HUKS\_TAG\_TYPE\_BOOL | 1012 | 表示密钥锁屏密码访问控制字段，可限制密钥只有在用户设置了锁屏密码时可用。  True表示只有在密码设置时才能生成和使用密钥。  **起始版本：** 11 |
| OH\_HUKS\_TAG\_AE\_TAG = OH\_HUKS\_TAG\_TYPE\_BYTES | 10009 | 用于传入GCM模式中的AEAD数据的字段。 |
| OH\_HUKS\_TAG\_SYMMETRIC\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20001 | 对称密钥数据。 |
| OH\_HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20002 | 非对称密钥公钥数据。 |
| OH\_HUKS\_TAG\_ASYMMETRIC\_PRIVATE\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20003 | 非对称密钥私钥数据。 |
