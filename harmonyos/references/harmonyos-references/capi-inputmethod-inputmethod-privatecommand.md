---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-privatecommand
title: InputMethod_PrivateCommand
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 结构体 > InputMethod_PrivateCommand
category: harmonyos-references
scraped_at: 2026-09-02T14:52:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fbeb4c0cc84d6b73ec4834f0e912d37d891deabdfb2061b81cd9f82b061cfdd8
---

```c
typedef struct InputMethod_PrivateCommand InputMethod_PrivateCommand
```

## 概述

私有命令结构体，采用key-value机制，作为输入框与输入法应用之间传递私有数据的载体。可用于传递自定义指令、扩展能力参数和特定场景数据，提升输入法功能的扩展性和兼容性。每个PrivateCommand实例包含一个key（标识符字符串）和一个value（布尔值、整数或字符串，三种类型只能选择一种），value的数据类型由InputMethod\_CommandValueType标识。

用途：在输入法应用与编辑框客户端之间传递私有数据，实现双方的自定义通信。输入法应用通过OH\_InputMethodProxy\_SendPrivateCommand向编辑框客户端发送私有指令；编辑框客户端通过OH\_TextEditorProxy\_ReceivePrivateCommandFunc回调接收来自输入法应用的私有指令。每个PrivateCommand实例携带一条key-value私有数据，最多可同时发送5个实例，单次发送的所有私有数据与key值的大小总和限制为32KB。

使用场景：

* 输入法应用向编辑框发送私有指令：输入法应用创建PrivateCommand实例，设置key和value后，通过[OH\_InputMethodProxy\_SendPrivateCommand](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_sendprivatecommand)发送给编辑框客户端。
* 编辑框客户端接收私有指令：编辑框客户端在[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)回调中接收PrivateCommand实例数组，遍历数组解析每个实例的key和value。

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

**所在头文件：** [inputmethod\_private\_command\_capi.h](capi-inputmethod-private-command-capi-h.md)

相关函数：

| 函数 | 说明 |
| --- | --- |
| [OH\_PrivateCommand\_Create](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_create) | 创建InputMethod\_PrivateCommand实例。 |
| [OH\_PrivateCommand\_Destroy](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_destroy) | 销毁InputMethod\_PrivateCommand实例。 |
| [OH\_PrivateCommand\_SetKey](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setkey) | 设置key值。 |
| [OH\_PrivateCommand\_SetBoolValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setboolvalue) | 设置布尔类型value值。 |
| [OH\_PrivateCommand\_SetIntValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setintvalue) | 设置整数类型value值。 |
| [OH\_PrivateCommand\_SetStrValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_setstrvalue) | 设置字符串类型value值。 |
| [OH\_PrivateCommand\_GetKey](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getkey) | 获取key值。 |
| [OH\_PrivateCommand\_GetValueType](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getvaluetype) | 获取value的数据类型。 |
| [OH\_PrivateCommand\_GetBoolValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getboolvalue) | 获取布尔类型value值。 |
| [OH\_PrivateCommand\_GetIntValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getintvalue) | 获取整数类型value值。 |
| [OH\_PrivateCommand\_GetStrValue](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_getstrvalue) | 获取字符串类型value值。 |

相关接口：

| 接口 | 说明 |
| --- | --- |
| [OH\_InputMethodProxy\_SendPrivateCommand](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_sendprivatecommand) | 输入法应用向编辑框客户端发送私有指令，PrivateCommand实例数组作为参数传入。最多5个实例，数据总大小限制32KB。 |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc) | 编辑框客户端接收私有指令的回调函数，PrivateCommand实例数组作为参数传入。回调返回后实例内存被释放。 |

相关枚举：

| 枚举 | 说明 |
| --- | --- |
| [InputMethod\_CommandValueType](capi-inputmethod-types-capi-h.md#inputmethod_commandvaluetype) | PrivateCommand中value的数据类型枚举（NONE/STRING/BOOL/INT32）。 |
