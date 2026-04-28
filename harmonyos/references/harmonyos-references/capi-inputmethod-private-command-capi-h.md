---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-private-command-capi-h
title: inputmethod_private_command_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_private_command_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:11+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:df609572a496e356b1a9ef82743f815507bdfe92222355af7969b56495ed0bef
---

## 概述

PhonePC/2in1TabletTVWearable

提供私有数据对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod\_private\_command\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) | InputMethod\_PrivateCommand | 表示私有数据的结构体类型。输入框和输入法应用之间交互的私有数据。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand \*OH\_PrivateCommand\_Create(char key[], size\_t keyLength)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-private-command-capi-h#oh_privatecommand_create) | 创建一个新的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例。 |
| [void OH\_PrivateCommand\_Destroy(InputMethod\_PrivateCommand \*command)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_destroy) | 销毁一个[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetKey(InputMethod\_PrivateCommand \*command, char key[], size\_t keyLength)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-private-command-capi-h#oh_privatecommand_setkey) | 设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的key值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetBoolValue(InputMethod\_PrivateCommand \*command, bool value)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setboolvalue) | 设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的布尔类型value值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetIntValue(InputMethod\_PrivateCommand \*command, int32\_t value)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setintvalue) | 设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的整数类型value值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetStrValue(InputMethod\_PrivateCommand \*command, char value[], size\_t valueLength)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-private-command-capi-h#oh_privatecommand_setstrvalue) | 设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的字符串类型value值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetKey(InputMethod\_PrivateCommand \*command, const char \*\*key, size\_t \*keyLength)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getkey) | 从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取key值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetValueType(InputMethod\_PrivateCommand \*command, InputMethod\_CommandValueType \*type)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getvaluetype) | 从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取value的数据类型。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetBoolValue(InputMethod\_PrivateCommand \*command, bool \*value)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getboolvalue) | 从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取布尔类型的value的值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetIntValue(InputMethod\_PrivateCommand \*command, int32\_t \*value)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getintvalue) | 从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取整数类型的value的值。 |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetStrValue(InputMethod\_PrivateCommand \*command, const char \*\*value, size\_t \*valueLength)](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getstrvalue) | 从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取字符串类型的value的值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PrivateCommand\_Create()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_PrivateCommand *OH_PrivateCommand_Create(char key[], size_t keyLength)
```

**描述**

创建一个新的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char key[] | 私有数据的key值。 |
| size\_t keyLength | key长度，单次所有私有数据与key值的大小限制32KB。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \* | 如果创建成功，返回一个指向新创建的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

### OH\_PrivateCommand\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_PrivateCommand_Destroy(InputMethod_PrivateCommand *command)
```

**描述**

销毁一个[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被销毁的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |

### OH\_PrivateCommand\_SetKey()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_SetKey(InputMethod_PrivateCommand *command, char key[], size_t keyLength)
```

**描述**

设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的key值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被设置的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| char key[] | key值。 |
| size\_t keyLength | key长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_SetBoolValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_SetBoolValue(InputMethod_PrivateCommand *command, bool value)
```

**描述**

设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的布尔类型value值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被设置的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| bool value | 布尔类型value值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_SetIntValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_SetIntValue(InputMethod_PrivateCommand *command, int32_t value)
```

**描述**

设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的整数类型value值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被设置的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| int32\_t value | 整数类型的value的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_SetStrValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_SetStrValue(InputMethod_PrivateCommand *command, char value[], size_t valueLength)
```

**描述**

设置[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)的字符串类型value值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被设置的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| char value[] | 字符串类型value值。 |
| size\_t valueLength | 表示字符串数据值的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_GetKey()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_GetKey(InputMethod_PrivateCommand *command, const char **key, size_t *keyLength)
```

**描述**

从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取key值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被获取key值的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| const char \*\*key | key的生命周期和command一致。不要直接保存key地址，或者直接写key。建议拷贝后使用。 |
| size\_t \*keyLength | key长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_GetValueType()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_GetValueType(InputMethod_PrivateCommand *command, InputMethod_CommandValueType *type)
```

**描述**

从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取value的数据类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被获取value值的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| [InputMethod\_CommandValueType](capi-inputmethod-types-capi-h.md#inputmethod_commandvaluetype) \*type | 表示指向 [InputMethod\_CommandValueType](capi-inputmethod-types-capi-h.md#inputmethod_commandvaluetype) 实例的指针。 用于value值的数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_GetBoolValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_GetBoolValue(InputMethod_PrivateCommand *command, bool *value)
```

**描述**

从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取布尔类型的value的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被获取value值的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| bool \*value | 布尔类型的value的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  [IME\_ERR\_QUERY\_FAILED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 查询失败，命令中没有布尔值。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_GetIntValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_GetIntValue(InputMethod_PrivateCommand *command, int32_t *value)
```

**描述**

从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取整数类型的value的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被获取value值的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| int32\_t \*value | 整数类型的value的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  [IME\_ERR\_QUERY\_FAILED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 查询失败，命令中没有整数值。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_PrivateCommand\_GetStrValue()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_PrivateCommand_GetStrValue(InputMethod_PrivateCommand *command, const char **value, size_t *valueLength)
```

**描述**

从[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)获取字符串类型的value的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*command | 指向即将被获取value值的[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。 |
| const char \*\*value | 字符串类型的value的值。 |
| size\_t \*valueLength | value的生命周期和command一致。不要直接保存value地址，或者直接写value。建议拷贝后使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  [IME\_ERR\_QUERY\_FAILED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 查询失败，命令中没有字符串值。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
