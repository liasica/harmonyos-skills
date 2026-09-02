---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-hashmap
title: 使用Hashmap完成键值数据的维护
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用Hashmap完成键值数据的维护
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:c88bc3978249130509fa9aa8868bdc87ec1875bea46e1048e404b74d5f2d9e94
---

从API版本26.0.0版本开始，新增高性能哈希表数据结构，适用于单线程场景。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Create](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_create) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle)\* handle, [HMS\_FAST\_Hashmap\_HashFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_hashfunc) hasher, [HMS\_FAST\_Hashmap\_KeyEqualFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_keyequalfunc) equaler) | 创建哈希表实例。 |
| void [HMS\_FAST\_Hashmap\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_destroy) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle) | 销毁哈希表实例。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Insert](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_insert) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapvalueptr) value, [FAST\_HashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 将给定的键值对插入哈希表中，如果键已经存在，则使用value覆写原有的值，并将原有值的地址保存在originValue中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Find](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_find) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapvalueptr)\* value) | 检索与给定键关联的值，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Erase](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_erase) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapkeyptr)\* originKey, [FAST\_HashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_TryInsert](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_tryinsert) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_hashmapvalueptr) value) | 将给定的键值对插入哈希表中，如果键已经存在、则不做操作。 |
| size\_t [HMS\_FAST\_Hashmap\_Size](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_size) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle) | 返回哈希表中的元素个数。 |
| void [HMS\_FAST\_Hashmap\_Clear](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_clear) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle) | 从哈希表中删除所有元素。 |
| size\_t [HMS\_FAST\_Hashmap\_EraseIf](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_eraseif) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合输入条件的所有元素，并使用自定义的方式释放其内存。 |
| void [HMS\_FAST\_Hashmap\_Traverse](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_traverse) ([FAST\_HashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_hashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合输入条件的键值对按自定义的方式修改。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
    find_library(
        lib_fast_collection
        NAMES fast_collection
    )
    target_link_libraries(entry PRIVATE ${lib_fast_collection})
   ```
2. 定义哈希值如何计算，键如何比较。

   ```cpp
   #include "FASTKit/fast_collections_hashmap.h"

   // 定义哈希值如何计算，键如何比较
   uint64_t custom_hash_int(const FAST_HashmapKeyPtr key) {
       static std::hash<int> hasher;
       int* intKey = (int*)key;
       return hasher(*intKey);
   }

   int32_t custom_equal_int(const FAST_HashmapKeyPtr key1, const FAST_HashmapKeyPtr key2) {
       int* intKey1 = (int*)key1;
       int* intKey2 = (int*)key2;
       return (*intKey1) == (*intKey2);
   }

   // 自定义删除条件
   int32_t custom_erase_cond(FAST_HashmapKeyPtr key, FAST_HashmapValuePtr val, void* context) {
       return 1;
   }

   // 释放键和值指针持有的内存
   int32_t custom_free(FAST_HashmapKeyPtr key, FAST_HashmapValuePtr val, void* context) {
       int* intKey = (int*)key;
       int* intVal = (int*)val;
       delete intKey;
       delete intVal;
       return 0;
   }

   // 自定义修改条件，也可传入nullptr以对所有元素执行修改
   int32_t custom_modify_cond(FAST_HashmapKeyPtr key, FAST_HashmapValuePtr val, void* context) {
       return 1;
   }

   int32_t custom_work(FAST_HashmapKeyPtr key, FAST_HashmapValuePtr val, void* context) {
       int* intVal = (int*)val;
       int* intCtx = (int*)context;
       *intVal += (*intCtx);
       return 1;
   }

   static napi_value RunHashmap(napi_env env, napi_callback_info info)
   {
       // 创建哈希表
       FAST_HashmapHandle handle;
       HMS_FAST_Hashmap_HashFunc hasher = &custom_hash_int;
       HMS_FAST_Hashmap_KeyEqualFunc equaler = &custom_equal_int;
       int ret = HMS_FAST_Hashmap_Create(&handle, hasher, equaler);

       // 初始化空的哈希表并向其中插入元素
       const int size = 10;
       int keys[size] = {1,2,3,4,5,6,7,8,9,10};
       int vals[size] = {1,2,3,4,5,6,7,8,9,10};
       for (int i = 0; i < size; ++i) {
           ret = HMS_FAST_Hashmap_Insert(
               handle,
               (FAST_HashmapKeyPtr)&(keys[i]),
               (FAST_HashmapValuePtr)&(vals[i]),
               nullptr
           );
       } // 完成插入后哈希表中应包含 {1: 1, 2: 2, ..., 10: 10}
       
       // 使用insert覆写已有的key，如果使用tryInsert则不会覆写
       int key2 = 1;
       int val2 = 2;
       int* originVal0;
       ret = HMS_FAST_Hashmap_Insert(
           handle,
           (FAST_HashmapKeyPtr)&key2,
           (FAST_HashmapValuePtr)&val2,
           (FAST_HashmapValuePtr*)&originVal0
       ); // {1: 2, ...}, 且originVal0 == &vals[0]

       // 键查找对应的值，并将结果保存在输入指针中。开发者需注意在使用此接口时应校验返回值ret，
       // 如果ret值不等于FAST_ERROR_CODE_SUCCESS，则res获取到的值是无效的
       int targetKey = 1;
       int* res;
       ret = HMS_FAST_Hashmap_Find(
           handle,
           (FAST_HashmapKeyPtr)&targetKey,
           (FAST_HashmapValuePtr*)&res
       ); // (*res) == 2

       // 键删除哈希表中对应的键值对，并获取关联内存的地址
       // 可以使用originKey/Val获得预先插入的元素地址，便于内存管理，可以使用nullptr作为入参
       int* originKey1;
       int* originVal1;
       int deleteKey = 1;
       ret = HMS_FAST_Hashmap_Erase(
           handle,
           (FAST_HashmapKeyPtr)&deleteKey,
           (FAST_HashmapKeyPtr*)&originKey1,
           (FAST_HashmapValuePtr*)&originVal1
       ); // originKey1 == &keys[0] && originVal1 == &val2

       // 查询哈希表当前元素个数
       size_t curSize = HMS_FAST_Hashmap_Size(handle); // curSize == 9

       // 清空哈希表中所有元素
       HMS_FAST_Hashmap_Clear(handle);
       curSize = HMS_FAST_Hashmap_Size(handle); // curSize == 0

       for (int i = 0; i < 6; i++) {
           int* key = new int{i};
           int* val = new int{i};
           ret = HMS_FAST_Hashmap_Insert(
               handle,
               (FAST_HashmapKeyPtr)key,
               (FAST_HashmapValuePtr)val,
               nullptr
           );
       } // {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

       // 使用Traverse接口对符合custom_modify_cond的元素执行custom_work操作
       int context = 10;
       HMS_FAST_Hashmap_Traverse(
           handle,
           (HMS_FAST_Hashmap_HookFunc)&custom_modify_cond,
           nullptr,
           (HMS_FAST_Hashmap_HookFunc)&custom_work,
           (void*)&context
       ); // {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15}

       // 使用EraseIf接口删除所有符合custom_erase_cond的键值对并使用custom_free清理相应的内存
       ret = HMS_FAST_Hashmap_EraseIf(
           handle,
           (HMS_FAST_Hashmap_HookFunc)&custom_erase_cond,
           nullptr,
           (HMS_FAST_Hashmap_HookFunc)&custom_free,
           nullptr
       ); // size == 0 && ret == 6

       // 销毁哈希表
       HMS_FAST_Hashmap_Destroy(handle);
       return 0;
   }
   ```

## 注意事项

1. **内存管理**：HashMap仅存储指针，不负责内存管理。调用者需要自行管理键和值指向的内存，确保在条目生命周期内内存有效。
2. **单线程场景**：此HashMap专为单线程场景设计，不支持多线程并发访问。如需多线程支持，请使用[ConcurrentHashMap](fast-concurrent-hashmap.md)。
3. **返回值校验**：所有返回FAST\_ErrorCode的API都应检查返回值，确保操作成功后再使用输出参数。
4. **回调函数**：Traverse和EraseIf中的回调函数应在内部锁下执行，避免在回调中阻塞或重新进入HashMap API。
