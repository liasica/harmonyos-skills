---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-collections-hashmap-8h
title: fast_collections_hashmap.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_collections_hashmap.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91e0045365eb52f5666eadf960ccfc6218892e6f235b13ad238ebb1c24c65918
---

## 概述

哈希表相关数据结构及函数定义。

**引用文件：** <FASTKit/fast\_collections\_hashmap.h>

**库：** libfast\_collections.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef void\* [FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) | 哈希表的句柄。 |
| typedef void\* [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) | 哈希表键指针。 |
| typedef void\* [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) | 哈希表的值指针。 |
| typedef uint64\_t(\* [HMS\_FAST\_Hashmap\_HashFunc](fast-kit-fast.md#hms_fast_hashmap_hashfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key) | 自定义的哈希值计算函数。 |
| typedef int32\_t(\* [HMS\_FAST\_Hashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_hashmap_keyequalfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) leftKey, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) rightKey) | 自定义的键比较函数。 |
| typedef int32\_t(\* [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value, void\* context) | 自定义的通用回调函数形式。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Create](fast-kit-fast.md#hms_fast_hashmap_create) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle)\* handle, [HMS\_FAST\_Hashmap\_HashFunc](fast-kit-fast.md#hms_fast_hashmap_hashfunc) hasher, [HMS\_FAST\_Hashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_hashmap_keyequalfunc) equaler) | 创建哈希表实例。 |
| void [HMS\_FAST\_Hashmap\_Destroy](fast-kit-fast.md#hms_fast_hashmap_destroy) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 销毁哈希表实例。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Insert](fast-kit-fast.md#hms_fast_hashmap_insert) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 将给定的键值对插入哈希表中，如果键已经存在，则使用value覆写原有的值，并将原有值的地址保存在originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Find](fast-kit-fast.md#hms_fast_hashmap_find) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* value) | 检索与给定键关联的值，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Erase](fast-kit-fast.md#hms_fast_hashmap_erase) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr)\* originKey, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_TryInsert](fast-kit-fast.md#hms_fast_hashmap_tryinsert) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value) | 将给定的键值对插入哈希表中，如果键已经存在、则不做操作。 |
| size\_t [HMS\_FAST\_Hashmap\_Size](fast-kit-fast.md#hms_fast_hashmap_size) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 返回哈希表中的元素个数。 |
| void [HMS\_FAST\_Hashmap\_Clear](fast-kit-fast.md#hms_fast_hashmap_clear) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 从哈希表中删除所有元素。 |
| size\_t [HMS\_FAST\_Hashmap\_EraseIf](fast-kit-fast.md#hms_fast_hashmap_eraseif) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合输入条件的所有元素，并使用自定义的方式释放其内存。 |
| void [HMS\_FAST\_Hashmap\_Traverse](fast-kit-fast.md#hms_fast_hashmap_traverse) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合输入条件的键值对按开发者给定的方式修改。 |
