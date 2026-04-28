---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h
title: native_huks_api.h
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 头文件 > native_huks_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:218e34a7acef5fcb1dffe565214954937f519a9db8ca7f0c007ad204e3f18df9
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问HUKS的API。

**引用文件：** <huks/native\_huks\_api.h>

**库：** libhuks\_ndk.z.so

**系统能力：** SystemCapability.Security.Huks.Core

在API version 9-19，系统能力为SystemCapability.Security.Huks；从API version 20起，系统能力变更为SystemCapability.Security.Huks.Core

**起始版本：** 9

**相关模块：** [HuksKeyApi](capi-hukskeyapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [struct OH\_Huks\_Result OH\_Huks\_GetSdkVersion(struct OH\_Huks\_Blob \*sdkVersion)](capi-native-huks-api-h.md#oh_huks_getsdkversion) | 获取当前Huks sdk版本号。 |
| [struct OH\_Huks\_Result OH\_Huks\_GenerateKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)](capi-native-huks-api-h.md#oh_huks_generatekeyitem) | 生成密钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_ImportKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*key)](capi-native-huks-api-h.md#oh_huks_importkeyitem) | 导入明文密钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_ImportWrappedKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*wrappingKeyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*wrappedKeyData)](capi-native-huks-api-h.md#oh_huks_importwrappedkeyitem) | 导入密文密钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_ExportPublicKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*key)](capi-native-huks-api-h.md#oh_huks_exportpublickeyitem) | 导出公钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_DeleteKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)](capi-native-huks-api-h.md#oh_huks_deletekeyitem) | 删除密钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_GetKeyItemParamSet(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)](capi-native-huks-api-h.md#oh_huks_getkeyitemparamset) | 获取密钥的属性集。 |
| [struct OH\_Huks\_Result OH\_Huks\_IsKeyItemExist(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)](capi-native-huks-api-h.md#oh_huks_iskeyitemexist) | 判断密钥是否存在。 |
| [struct OH\_Huks\_Result OH\_Huks\_AttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)](capi-native-huks-api-h.md#oh_huks_attestkeyitem) | 获取密钥证书链。该API仅面向系统应用开放。 |
| [struct OH\_Huks\_Result OH\_Huks\_AnonAttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)](capi-native-huks-api-h.md#oh_huks_anonattestkeyitem) | 获取密钥证书链。  这是一个涉及网络的耗时接口，调用方可以通过异步线程获取证书链。 |
| [struct OH\_Huks\_Result OH\_Huks\_InitSession(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*handle, struct OH\_Huks\_Blob \*token)](capi-native-huks-api-h.md#oh_huks_initsession) | 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选）。 |
| [struct OH\_Huks\_Result OH\_Huks\_UpdateSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)](capi-native-huks-api-h.md#oh_huks_updatesession) | 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据。 |
| [struct OH\_Huks\_Result OH\_Huks\_FinishSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)](capi-native-huks-api-h.md#oh_huks_finishsession) | 结束密钥会话并进行相应的密钥操作，输出处理数据。 |
| [struct OH\_Huks\_Result OH\_Huks\_AbortSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet)](capi-native-huks-api-h.md#oh_huks_abortsession) | 取消密钥会话。 |
| [struct OH\_Huks\_Result OH\_Huks\_ListAliases(const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_KeyAliasSet \*\*outData)](capi-native-huks-api-h.md#oh_huks_listaliases) | 获取密钥别名集。 |
| [struct OH\_Huks\_Result OH\_Huks\_WrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)](capi-native-huks-api-h.md#oh_huks_wrapkey) | 导出由特定密钥加密的封装密钥。 |
| [struct OH\_Huks\_Result OH\_Huks\_UnwrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)](capi-native-huks-api-h.md#oh_huks_unwrapkey) | 导入由特定密钥加密的封装密钥。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Huks\_GetSdkVersion()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_GetSdkVersion(struct OH_Huks_Blob *sdkVersion)
```

**描述**

获取当前Huks sdk版本号。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*sdkVersion | 用于存放获取到的版本信息（字符串格式）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：sdkVersion或者sdkVersion->data是null，或者sdkVersion->size太小。 |

### OH\_Huks\_GenerateKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_GenerateKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)
```

**描述**

生成密钥。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 给要生成的密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSetIn | 生成密钥的属性信息的参数集。 |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSetOut | 生成密钥为临时类型时，存放着密钥数据；非临时类型可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSetIn、paramSetOut有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 ：删除或者写文件失败。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：基础密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 ：连接用户IAM失败。  OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016 ：需要设备密码但没有设置。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 ：（API 20新增）同名密钥已存在。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_ImportKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_ImportKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *key)
```

**描述**

导入明文密钥。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 待导入密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 待导入密钥的属性参数。 |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*key | 待导入密钥数据，需符合Huks的格式要求，具体见[native\_huks\_type.h](capi-native-huks-type-h.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet、key有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 ：删除或者写文件失败。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 ：连接用户IAM失败。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 ：（API 20新增）同名密钥已存在。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_ImportWrappedKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_ImportWrappedKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *wrappingKeyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *wrappedKeyData)
```

**描述**

导入密文密钥。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 待导入密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。 |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*wrappingKeyAlias | 密钥别名，该对应密钥用于密钥协商出密钥解密待导入密钥。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 待导入加密密钥的属性参数。 |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*wrappedKeyData | 需要导入的加密的密钥数据，需要符合Huks定义的格式，具体见[OH\_Huks\_AlgSuite](capi-native-huks-type-h.md#oh_huks_algsuite)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、wrappingKeyAlias、paramSet、wrappedKeyData有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 ：删除或者写文件失败。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 ：连接用户IAM失败。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 ：（API 20新增）同名密钥已存在。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_ExportPublicKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_ExportPublicKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *key)
```

**描述**

导出公钥。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 待导出公钥的密钥别名，应与所用密钥生成时使用的别名相同。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 导出公钥需要的属性参数。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*key | 存放导出的公钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet、key有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_DeleteKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_DeleteKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

删除密钥。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 待删除密钥的别名，应与密钥生成时使用的别名相同。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 删除密钥需要属性参数（默认传空）。若不指定则默认要删除的密钥存储等级为[OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_CE](capi-native-huks-type-h.md#oh_huks_authstoragelevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_GetKeyItemParamSet()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_GetKeyItemParamSet(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)
```

**描述**

获取密钥的属性集。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 要获取参数集的密钥别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSetIn | 要获取参数集需要的属性TAG（默认传空）。 |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSetOut | 获取到的输出参数集。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSetIn、paramSetOut有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_IsKeyItemExist()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_IsKeyItemExist(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

判断密钥是否存在。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 要查找的密钥的别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 查询密钥需要的属性TAG（默认传空）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_AttestKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_AttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)
```

**描述**

获取密钥证书链。该API仅面向系统应用开放。

**需要权限：** ohos.permission.ATTEST\_KEY，该权限仅系统应用可申请。

**起始版本：** 9

说明

使用非匿名证书密钥证明时生成的证书链包含设备标识符，设备标识符的使用、留存、销毁由开发者决定，开发者需在隐私声明中对其使用目的，留存策略和销毁方式进行说明。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 要获取证书的密钥的别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 获取密钥证书需要的参数。 |
| [struct OH\_Huks\_CertChain](capi-hukstypeapi-oh-huks-certchain.md) \*certChain | 存放输出的密钥证书链。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet、certChain有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201 ：权限检查失败，请先申请请求权限。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_AnonAttestKeyItem()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_AnonAttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)
```

**描述**

获取密钥证书链。

这是一个涉及网络的耗时接口，调用方可以通过异步线程获取证书链。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 要获取证书的密钥的别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 获取密钥证书需要的参数。 |
| [struct OH\_Huks\_CertChain](capi-hukstypeapi-oh-huks-certchain.md) \*certChain | 存放输出的密钥证书链。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数keyAlias、paramSet、certChain有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201 ：权限检查失败，请先申请请求权限。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_InitSession()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_InitSession(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *handle, struct OH_Huks_Blob *token)
```

**描述**

初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选）。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 操作的密钥的别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 初始化操作的密钥参数集合。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*handle | 密钥会话的句柄，后续其他操作时传入该句柄，包括[OH\_Huks\_UpdateSession](capi-native-huks-api-h.md#oh_huks_updatesession)，[OH\_Huks\_FinishSession](capi-native-huks-api-h.md#oh_huks_finishsession)，[OH\_Huks\_AbortSession](capi-native-huks-api-h.md#oh_huks_abortsession)。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*token | 存放安全访问控制时传回的token。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数 keyAlias、paramSet、handle、token有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_SESSION\_LIMIT = 12000010 ：已达最大会话限制。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 22新增）指定的aead长度无效或者通过访问群组标签指定的群组名无效。  OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 ：（API 22新增）提供者或Ukey内部执行失败。  OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021 ：（API 22新增）PIN码被锁定。  OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023 ：（API 22新增）PIN码未认证通过。  OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 ：（API 22新增）提供者或Ukey中的资源正在被使用。 |

**参考：**

[OH\_Huks\_UpdateSession](capi-native-huks-api-h.md#oh_huks_updatesession)

[OH\_Huks\_FinishSession](capi-native-huks-api-h.md#oh_huks_finishsession)

[OH\_Huks\_AbortSession](capi-native-huks-api-h.md#oh_huks_abortsession)

### OH\_Huks\_UpdateSession()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_UpdateSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
```

**描述**

分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*handle | 密钥会话句柄，通过[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)接口生成。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 密钥操作对应的输入参数集。 |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*inData | 要处理的输入数据，如果数据过大，可分片多次调用。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*outData | 经过对应的密钥操作后输出的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在，或handle不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013 ：证书不存在。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008 ：认证令牌校验失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007 ：认证令牌信息校验失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009 ：认证令牌超时。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016 ：需要设备密码但没有设置。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 ：（API 22新增）提供者或Ukey内部执行失败。  OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021 ：（API 22新增）PIN码被锁定。  OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023 ：（API 22新增）PIN码未认证通过。  OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 ：（API 22新增）提供者或Ukey中的资源正在被使用。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

**参考：**

[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)

[OH\_Huks\_FinishSession](capi-native-huks-api-h.md#oh_huks_finishsession)

[OH\_Huks\_AbortSession](capi-native-huks-api-h.md#oh_huks_abortsession)

### OH\_Huks\_FinishSession()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_FinishSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
```

**描述**

结束密钥会话并进行相应的密钥操作，输出处理数据。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*handle | 密钥会话句柄，通过[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)接口生成。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 密钥操作对应的输入参数集。 |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*inData | 要处理的输入数据。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*outData | 经过对应的密钥操作后输出的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在，或handle不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013 ：证书不存在。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 ：加密引擎失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008 ：认证令牌校验失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007 ：认证令牌信息校验失败。  OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009 ：认证令牌超时。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016 ：需要设备密码但没有设置。  OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 ：暂不支持该功能。  OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 ：（API 20新增）同名密钥已存在。  OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 ：（API 22新增）提供者或Ukey内部执行失败。  OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021 ：（API 22新增）PIN码被锁定。  OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023 ：（API 22新增）PIN码未认证通过。  OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 ：（API 22新增）提供者或Ukey中的资源正在被使用。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

**参考：**

[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)

[OH\_Huks\_UpdateSession](capi-native-huks-api-h.md#oh_huks_updatesession)

[OH\_Huks\_AbortSession](capi-native-huks-api-h.md#oh_huks_abortsession)

### OH\_Huks\_AbortSession()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_AbortSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

取消密钥会话。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*handle | 密钥会话句柄，通过[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)接口生成。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 取消密钥会话需要的输入参数集（默认传空）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 ：密钥参数无效。  OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 ：密钥文件不存在，或handle不存在。  OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 ：获取密钥参数失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013 ：证书不存在。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 ：（API 22新增）提供者或Ukey内部执行失败。  OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 ：（API 22新增）提供者或Ukey中的资源正在被使用。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

**参考：**

[OH\_Huks\_InitSession](capi-native-huks-api-h.md#oh_huks_initsession)

[OH\_Huks\_UpdateSession](capi-native-huks-api-h.md#oh_huks_updatesession)

[OH\_Huks\_FinishSession](capi-native-huks-api-h.md#oh_huks_finishsession)

### OH\_Huks\_ListAliases()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_ListAliases(const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_KeyAliasSet **outData)
```

**描述**

获取密钥别名集。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 获取密钥别名集需要的输入参数集（默认传空）。 |
| [struct OH\_Huks\_KeyAliasSet](capi-hukstypeapi-oh-huks-keyaliasset.md) \*\*outData | 经过对应的密钥操作后输出的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet、outData有一个无效。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：（API 23新增）通过访问群组标签指定的群组名无效。 |

### OH\_Huks\_WrapKey()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_WrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)
```

**描述**

导出由特定密钥加密的封装密钥。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 表示要导出的密钥别名。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 表示加密导出密钥的参数集。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*wrappedKey | 表示要导出的封装好的密钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801 ：接口不支持。  OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 ：删除或者写文件失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000011 ：密钥文件不存在。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：密钥别名、参数集或者封装密钥不合法。 |

### OH\_Huks\_UnwrapKey()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_UnwrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)
```

**描述**

导入由特定密钥加密的封装密钥。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*keyAlias | 表示要导入的密钥别名。在服务进程中，别名必须唯一。否则，密钥将被覆盖。 |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 表示加密导入密钥的参数集。 |
| [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*wrappedKey | 表示要导入的封装好的密钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801 ：接口不支持。  OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 ：删除或者写文件失败。  OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 ：IPC通信失败。  OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 ：设备环境或输入参数异常。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 ：连接用户IAM失败。  OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 ：密钥别名、参数集或者封装密钥不合法。 |
