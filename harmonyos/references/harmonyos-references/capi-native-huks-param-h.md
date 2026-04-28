---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h
title: native_huks_param.h
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 头文件 > native_huks_param.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:49+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:c440b18316cf04982fa0a4e78af59ff909ae0192100a92c7d7b23ad24b44212f
---

## 概述

PhonePC/2in1TabletTVWearable

提供参数集构造、使用和销毁的API。

**引用文件：** <huks/native\_huks\_param.h>

**库：** libhuks\_ndk.z.so

**系统能力：** SystemCapability.Security.Huks.Core

在API 9-19，系统能力为SystemCapability.Security.Huks；从API 20起，系统能力变更为SystemCapability.Security.Huks.Core

**起始版本：** 9

**相关模块：** [HuksParamSetApi](capi-huksparamsetapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [struct OH\_Huks\_Result OH\_Huks\_InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](capi-native-huks-param-h.md#oh_huks_initparamset) | 初始化参数集，无参数信息，分配参数集默认可用内存空间。初始化后的参数集需要通过[OH\_Huks\_FreeParamSet](capi-native-huks-param-h.md#oh_huks_freeparamset)释放。添加参数的参数集需要使用[OH\_Huks\_AddParams](capi-native-huks-param-h.md#oh_huks_addparams)添加参数并且必须使用[OH\_Huks\_BuildParamSet](capi-native-huks-param-h.md#oh_huks_buildparamset)构造参数集。 |
| [struct OH\_Huks\_Result OH\_Huks\_AddParams(struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Param \*params, uint32\_t paramCnt)](capi-native-huks-param-h.md#oh_huks_addparams) | 添加参数到参数集里面。 |
| [struct OH\_Huks\_Result OH\_Huks\_BuildParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](capi-native-huks-param-h.md#oh_huks_buildparamset) | 构造参数集，在初始化参数集和添加参数操作之后，序列化参数集，将blob类型的数据拷贝到paramSet结构尾部相邻内存区域。 |
| [void OH\_Huks\_FreeParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](capi-native-huks-param-h.md#oh_huks_freeparamset) | 销毁参数集。 |
| [struct OH\_Huks\_Result OH\_Huks\_CopyParamSet(const struct OH\_Huks\_ParamSet \*fromParamSet, uint32\_t fromParamSetSize, struct OH\_Huks\_ParamSet \*\*paramSet)](capi-native-huks-param-h.md#oh_huks_copyparamset) | 复制参数集（深拷贝）。 |
| [struct OH\_Huks\_Result OH\_Huks\_GetParam(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t tag, struct OH\_Huks\_Param \*\*param)](capi-native-huks-param-h.md#oh_huks_getparam) | 从参数集中获取参数。 |
| [struct OH\_Huks\_Result OH\_Huks\_FreshParamSet(struct OH\_Huks\_ParamSet \*paramSet, bool isCopy)](capi-native-huks-param-h.md#oh_huks_freshparamset) | 刷新参数集内[OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md)类型的数据。 |
| [struct OH\_Huks\_Result OH\_Huks\_IsParamSetTagValid(const struct OH\_Huks\_ParamSet \*paramSet)](capi-native-huks-param-h.md#oh_huks_isparamsettagvalid) | 检查参数集中的参数是否有效、是否有重复。 |
| [struct OH\_Huks\_Result OH\_Huks\_IsParamSetValid(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t size)](capi-native-huks-param-h.md#oh_huks_isparamsetvalid) | 检查参数集大小是否有效。 |
| [struct OH\_Huks\_Result OH\_Huks\_CheckParamMatch(const struct OH\_Huks\_Param \*baseParam, const struct OH\_Huks\_Param \*param)](capi-native-huks-param-h.md#oh_huks_checkparammatch) | 比较两个参数是否相同。 |
| [void OH\_Huks\_FreeKeyAliasSet(struct OH\_Huks\_KeyAliasSet \*keyAliasSet)](capi-native-huks-param-h.md#oh_huks_freekeyaliasset) | 销毁密钥别名的参数集。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Huks\_InitParamSet()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_InitParamSet(struct OH_Huks_ParamSet **paramSet)
```

**描述**

初始化参数集，无参数信息，分配参数集默认可用内存空间。初始化后的参数集需要通过[OH\_Huks\_FreeParamSet](capi-native-huks-param-h.md#oh_huks_freeparamset)释放。添加参数的参数集需要使用[OH\_Huks\_AddParams](capi-native-huks-param-h.md#oh_huks_addparams)添加参数并且必须使用[OH\_Huks\_BuildParamSet](capi-native-huks-param-h.md#oh_huks_buildparamset)构造参数集。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*\*paramSet | 指向要初始化的参数集的指针地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：初始化操作成功。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet无效。 |

### OH\_Huks\_AddParams()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_AddParams(struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Param *params, uint32_t paramCnt)
```

**描述**

添加参数到参数集里面。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向要被添加参数的参数集的指针。 |
| [const struct OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) \*params | 指向要添加的参数数组的指针。 |
| uint32\_t paramCnt | 待添加参数数组的参数个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：params为null或者paramSet无效。 |

### OH\_Huks\_BuildParamSet()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_BuildParamSet(struct OH_Huks_ParamSet **paramSet)
```

**描述**

构造参数集，在初始化参数集和添加参数操作之后，序列化参数集，将blob类型的数据拷贝到paramSet结构尾部相邻内存区域。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*\*paramSet | 指向要被正式构造的参数集的指针地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet无效。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。 |

### OH\_Huks\_FreeParamSet()

PhonePC/2in1TabletTVWearable

```
1. void OH_Huks_FreeParamSet(struct OH_Huks_ParamSet **paramSet)
```

**描述**

销毁参数集。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*\*paramSet | 指向要被销毁的参数集的指针地址。 |

### OH\_Huks\_CopyParamSet()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_CopyParamSet(const struct OH_Huks_ParamSet *fromParamSet, uint32_t fromParamSetSize, struct OH_Huks_ParamSet **paramSet)
```

**描述**

复制参数集（深拷贝）。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*fromParamSet | 指向要被复制的参数集的指针。 |
| uint32\_t fromParamSetSize | 被复制的参数集占用内存的大小。 |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*\*paramSet | 指向生成新的参数集的指针地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数fromParamSet、fromParamSetSize、paramSet有一个无效。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。 |

### OH\_Huks\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_GetParam(const struct OH_Huks_ParamSet *paramSet, uint32_t tag, struct OH_Huks_Param **param)
```

**描述**

从参数集中获取参数。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向参数集的指针。 |
| uint32\_t tag | 要获取的对应参数的值。 |
| [struct OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) \*\*param | 指向获取到的参数的指针地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet或者param无效，或者参数param不在paramSet里面。 |

### OH\_Huks\_FreshParamSet()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_FreshParamSet(struct OH_Huks_ParamSet *paramSet, bool isCopy)
```

**描述**

刷新参数集内[OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md)类型的数据。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向参数集的指针。 |
| bool isCopy | 如果为true，刷新[OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md)类型数据的地址并复制到参数集。如果为false，只会刷新[OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md)类型数据的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：操作成功。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet无效。  OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 ：内存不足。 |

### OH\_Huks\_IsParamSetTagValid()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_IsParamSetTagValid(const struct OH_Huks_ParamSet *paramSet)
```

**描述**

检查参数集中的参数是否有效、是否有重复。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向参数集的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：paramSet中的参数都有效。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet无效或者参数集中有无效、重复、不正确的标签。 |

### OH\_Huks\_IsParamSetValid()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_IsParamSetValid(const struct OH_Huks_ParamSet *paramSet, uint32_t size)
```

**描述**

检查参数集大小是否有效。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向参数集的指针。 |
| uint32\_t size | 参数集占用的内存大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：参数集大小合法。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：参数paramSet无效。 |

### OH\_Huks\_CheckParamMatch()

PhonePC/2in1TabletTVWearable

```
1. struct OH_Huks_Result OH_Huks_CheckParamMatch(const struct OH_Huks_Param *baseParam, const struct OH_Huks_Param *param)
```

**描述**

比较两个参数是否相同。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) \*baseParam | 指向被比较的参数的指针。 |
| [const struct OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) \*param | 指向比较的参数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_Huks\_Result](capi-hukstypeapi-oh-huks-result.md) | 可能的返回码（errorCode）：  OH\_HUKS\_SUCCESS = 0 ：比较的两个参数相同。  OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 ：其中一个参数集是无效的，或者参数不匹配，  或者内部有无效标签。 |

### OH\_Huks\_FreeKeyAliasSet()

PhonePC/2in1TabletTVWearable

```
1. void OH_Huks_FreeKeyAliasSet(struct OH_Huks_KeyAliasSet *keyAliasSet)
```

**描述**

销毁密钥别名的参数集。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_Huks\_KeyAliasSet](capi-hukstypeapi-oh-huks-keyaliasset.md) \*keyAliasSet | 指向要被销毁的密钥别名的参数集的指针地址。 |
