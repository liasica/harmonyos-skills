---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-types-capi-h
title: inputmethod_types_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_types_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:55f2d97fa6d65442477de86c1aa60ab5e0dcdab1a8eb39c4e70c7a6f8e042e7c
---

## 概述

PhonePC/2in1TabletTVWearable

提供了输入法相关的类型定义。

**引用文件：** <inputmethod/inputmethod\_types\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_KeyboardStatus](capi-inputmethod-types-capi-h.md#inputmethod_keyboardstatus) | InputMethod\_KeyboardStatus | 键盘状态。 |
| [InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype) | InputMethod\_EnterKeyType | 回车键功能类型。 |
| [InputMethod\_Direction](capi-inputmethod-types-capi-h.md#inputmethod_direction) | InputMethod\_Direction | 移动方向。 |
| [InputMethod\_ExtendAction](capi-inputmethod-types-capi-h.md#inputmethod_extendaction) | InputMethod\_ExtendAction | 编辑框中文本的扩展编辑操作类型。 |
| [InputMethod\_TextInputType](capi-inputmethod-types-capi-h.md#inputmethod_textinputtype) | InputMethod\_TextInputType | 文本输入类型。 |
| [InputMethod\_CommandValueType](capi-inputmethod-types-capi-h.md#inputmethod_commandvaluetype) | InputMethod\_CommandValueType | 私有数据类型。 |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | InputMethod\_ErrorCode | 输入法错误码。 |
| [InputMethod\_RequestKeyboardReason](capi-inputmethod-types-capi-h.md#inputmethod_requestkeyboardreason) | InputMethod\_RequestKeyboardReason | 表示请求键盘输入的原因。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### InputMethod\_KeyboardStatus

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_KeyboardStatus
```

**描述**

键盘状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_KEYBOARD\_STATUS\_NONE = 0 | 键盘状态为NONE。 |
| IME\_KEYBOARD\_STATUS\_HIDE = 1 | 键盘状态为隐藏。 |
| IME\_KEYBOARD\_STATUS\_SHOW = 2 | 键盘状态为显示。 |

### InputMethod\_EnterKeyType

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_EnterKeyType
```

**描述**

回车键功能类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_ENTER\_KEY\_UNSPECIFIED = 0 | 未指定。 |
| IME\_ENTER\_KEY\_NONE = 1 | 回车键功能类型为NONE。 |
| IME\_ENTER\_KEY\_GO = 2 | 前往。 |
| IME\_ENTER\_KEY\_SEARCH = 3 | 搜索。 |
| IME\_ENTER\_KEY\_SEND = 4 | 发送。 |
| IME\_ENTER\_KEY\_NEXT = 5 | 下一步。 |
| IME\_ENTER\_KEY\_DONE = 6 | 完成。 |
| IME\_ENTER\_KEY\_PREVIOUS = 7 | 上一步。 |
| IME\_ENTER\_KEY\_NEWLINE = 8 | 换行。 |

### InputMethod\_Direction

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_Direction
```

**描述**

移动方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_DIRECTION\_NONE = 0 | 移动方向为NONE。 |
| IME\_DIRECTION\_UP = 1 | 向上。 |
| IME\_DIRECTION\_DOWN = 2 | 向下。 |
| IME\_DIRECTION\_LEFT = 3 | 向左。 |
| IME\_DIRECTION\_RIGHT = 4 | 向右。 |

### InputMethod\_ExtendAction

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_ExtendAction
```

**描述**

编辑框中文本的扩展编辑操作类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_EXTEND\_ACTION\_SELECT\_ALL = 0 | 全选。 |
| IME\_EXTEND\_ACTION\_CUT = 3 | 剪切。 |
| IME\_EXTEND\_ACTION\_COPY = 4 | 复制。 |
| IME\_EXTEND\_ACTION\_PASTE = 5 | 粘贴。 |

### InputMethod\_TextInputType

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_TextInputType
```

**描述**

文本输入类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_TEXT\_INPUT\_TYPE\_NONE = -1 | 文本输入类型为NONE。 |
| IME\_TEXT\_INPUT\_TYPE\_TEXT = 0 | 文本类型。 |
| IME\_TEXT\_INPUT\_TYPE\_MULTILINE = 1 | 多行类型。 |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER = 2 | 数字类型。 |
| IME\_TEXT\_INPUT\_TYPE\_PHONE = 3 | 电话号码类型。 |
| IME\_TEXT\_INPUT\_TYPE\_DATETIME = 4 | 日期类型。 |
| IME\_TEXT\_INPUT\_TYPE\_EMAIL\_ADDRESS = 5 | 邮箱地址类型。 |
| IME\_TEXT\_INPUT\_TYPE\_URL = 6 | 链接类型。 |
| IME\_TEXT\_INPUT\_TYPE\_VISIBLE\_PASSWORD = 7 | 密码类型。 |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER\_PASSWORD = 8 | 数字密码类型。 |
| IME\_TEXT\_INPUT\_TYPE\_SCREEN\_LOCK\_PASSWORD = 9 | 锁屏密码类型。 |
| IME\_TEXT\_INPUT\_TYPE\_USER\_NAME = 10 | 用户名类型。 |
| IME\_TEXT\_INPUT\_TYPE\_NEW\_PASSWORD = 11 | 新密码类型。 |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER\_DECIMAL = 12 | 数字小数类型。 |
| IME\_TEXT\_INPUT\_TYPE\_ONE\_TIME\_CODE = 13 | 验证码类型。**起始版本：** 20 |

### InputMethod\_CommandValueType

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_CommandValueType
```

**描述**

私有数据类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_COMMAND\_VALUE\_TYPE\_NONE = 0 | 私有数据类型为NONE。 |
| IME\_COMMAND\_VALUE\_TYPE\_STRING = 1 | 字符串类型。 |
| IME\_COMMAND\_VALUE\_TYPE\_BOOL = 2 | 布尔类型。 |
| IME\_COMMAND\_VALUE\_TYPE\_INT32 = 3 | 32位带符号整数类型。 |

### InputMethod\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_ErrorCode
```

**描述**

输入法错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IME\_ERR\_OK = 0 | 成功。 |
| IME\_ERR\_UNDEFINED = 1 | 未定义错误。 |
| IME\_ERR\_PARAMCHECK = 401 | 参数检查失败。 |
| IME\_ERR\_PACKAGEMANAGER = 12800001 | 包管理异常。 |
| IME\_ERR\_IMENGINE = 12800002 | 输入法应用异常。 |
| IME\_ERR\_IMCLIENT = 12800003 | 输入框客户端异常。 |
| IME\_ERR\_CONFIG\_PERSIST = 12800005 | 配置固化失败。当保存配置失败时，会报此错误码。 |
| IME\_ERR\_CONTROLLER = 12800006 | 输入法控制器异常。 |
| IME\_ERR\_SETTINGS = 12800007 | 输入法设置器异常。 |
| IME\_ERR\_IMMS = 12800008 | 输入法管理服务异常。 |
| IME\_ERR\_DETACHED = 12800009 | 输入框未绑定。 |
| IME\_ERR\_NULL\_POINTER = 12802000 | 空指针异常。 |
| IME\_ERR\_QUERY\_FAILED = 12802001 | 查询失败。 |

### InputMethod\_RequestKeyboardReason

PhonePC/2in1TabletTVWearable

```
1. enum InputMethod_RequestKeyboardReason
```

**描述**

表示请求键盘输入的原因。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| IME\_REQUEST\_REASON\_NONE = 0 | 表示没有特定的原因触发键盘请求。 |
| IME\_REQUEST\_REASON\_MOUSE = 1 | 表示键盘请求是由鼠标操作触发的。 |
| IME\_REQUEST\_REASON\_TOUCH = 2 | 表示键盘请求是由触摸操作触发的。 |
| IME\_REQUEST\_REASON\_OTHER = 20 | 表示键盘请求是由其他原因触发的。 |
