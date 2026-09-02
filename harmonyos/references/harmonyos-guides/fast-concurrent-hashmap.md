---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-concurrent-hashmap
title: 使用ConcurrentHashmap在多线程下完成键值信息的查找维护
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用ConcurrentHashmap在多线程下完成键值信息的查找维护
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:f731e27c20df9883a919a83b15c8ade6941e151d9aa9db066f82a6ff54f46c6a
---

FAST Kit提供的Concurrent HashMap（并发哈希表）专为高并发场景下的键值对数据管理而设计。主要用于实现多线程环境下的安全存储、快速访问与高效更新，适用于对并发吞吐量和数据一致性要求较高的增删改查操作，典型场景包括单点插入、删除、查询及并发修改等。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Create](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_create) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HashFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc) hasher, [HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc) equaler, float maxLoadFac, size\_t numShards) | 使用给定配置创建并发哈希表。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_destroy) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle) | 销毁指定并发哈希表。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Insert](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_insert) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapvalueptr) value, [FAST\_ConcurrentHashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Find](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_find) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Erase](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_erase) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapkeyptr)\* originKey, [FAST\_ConcurrentHashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_TryInsert](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_tryinsert) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmapvalueptr) value) | 将给定的键值对插入并发哈希表中，如果键已经存在、则不做操作。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_Size](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_size) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle) | 返回给定哈希表当前的元素个数。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Clear](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_clear) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle) | 清空给定哈希表中维护的所有元素。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_EraseIf](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_eraseif) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Traverse](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_traverse) ([FAST\_ConcurrentHashmapHandle](../harmonyos-references/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
    find_library(
        lib_fast_ads
        NAMES fast_ads
    )
   target_link_libraries(entry PRIVATE ${lib_fast_ads})
   ```
2. 调用相关接口能力完成键值信息的管理。

   ```cpp
   #include "FASTKit/fast_ads_concurrent_hashmap.h"

   // 定义哈希值如何计算，键如何比较
   uint64_t custom_hash_int(const FAST_ConcurrentHashmapKeyPtr key) {
       static std::hash<int> hasher;
       int* intKey = (int*)key;
       return hasher(*intKey);
   }

   int32_t custom_equal_int(const FAST_ConcurrentHashmapKeyPtr key1, const FAST_ConcurrentHashmapKeyPtr key2) {
       int* intKey1 = (int*)key1;
       int* intKey2 = (int*)key2;
       return (*intKey1) == (*intKey2);
   }

   // 自定义删除条件
   int32_t custom_erase_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
       return 1;
   }

   // 释放键和值指针持有的内存
   int32_t custom_free(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
       int* intKey = (int*)key;
       int* intVal = (int*)val;
       delete intKey;
       delete intVal;
       return 0;
   }

   // 自定义修改条件，也可传入nullptr以对所有元素执行修改
   int32_t custom_modify_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
       return 1;
   }

   int32_t custom_work(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
       int* intVal = (int*)val;
       int* intCtx = (int*)context;
       *intVal += (*intCtx);
       return 1;
   }

   static napi_value RunConcurrentHashmap(napi_env env, napi_callback_info info)
   {
       // 使用合适的配置创建并发哈希表，负载因子（loadfac）和分段数（numShards）的典型值一般为0.8和64。
       // 负载因子主要作用于分段内部，更大的负载因子通常意味着更小的内存消耗和更大的操作开销；
       // 分段数主要作用域并发哈希表全局，更大的分段数通常意味着更好的并发性能和更大的内存消耗
       FAST_ConcurrentHashmapHandle handle;
       HMS_FAST_ConcurrentHashmap_HashFunc hasher = &custom_hash_int;
       HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler = &custom_equal_int;
       float loadfac = 0.8;
       size_t numShards = 64;
       int ret = HMS_FAST_ConcurrentHashmap_Create(&handle, hasher, equaler, loadfac, numShards);

       // 初始化空的哈希表并向其中插入元素
       const int size = 10;
       int keys[size] = {1,2,3,4,5,6,7,8,9,10};
       int vals[size] = {1,2,3,4,5,6,7,8,9,10};
       for (int i = 0; i < size; ++i) {
           ret = HMS_FAST_ConcurrentHashmap_Insert(
               handle,
               (FAST_ConcurrentHashmapKeyPtr)&(keys[i]),
               (FAST_ConcurrentHashmapValuePtr)&(vals[i]),
               nullptr
           );
       } // 完成插入后哈希表中应包含 {1: 1, 2: 2, ..., 10: 10}
       
       // 使用insert覆写已有的key，如果使用tryInsert则不会覆写
       int key2 = 1;
       int val2 = 2;
       int* originVal0;
       ret = HMS_FAST_ConcurrentHashmap_Insert(
           handle,
           (FAST_ConcurrentHashmapKeyPtr)&key2,
           (FAST_ConcurrentHashmapValuePtr)&val2,
           (FAST_ConcurrentHashmapValuePtr*)&originVal0
       ); // {1: 2, ...}, 且originVal0 == &vals[0]

       // 键查找对应的值，并将结果保存在输入指针中。开发者需注意在使用此接口时应校验返回值ret，
       // 如果ret值不等于FAST_ERROR_CODE_SUCCESS，则res获取到的值是无效的
       int targetKey = 1;
       int* res;
       ret = HMS_FAST_ConcurrentHashmap_Find(
           handle,
           (FAST_ConcurrentHashmapKeyPtr)&targetKey,
           (FAST_ConcurrentHashmapValuePtr*)&res
       ); // (*res) == 2

       // 键删除并发哈希表中对应的键值对，并获取关联内存的地址
       // 可以使用originKey/Val获得预先插入的元素地址，便于内存管理，可以使用nullptr作为入参
       int* originKey1;
       int* originVal1;
       int deleteKey = 1;
       ret = HMS_FAST_ConcurrentHashmap_Erase(
           handle,
           (FAST_ConcurrentHashmapKeyPtr)&deleteKey,
           (FAST_ConcurrentHashmapKeyPtr*)&originKey1,
           (FAST_ConcurrentHashmapValuePtr*)&originVal1
       ); // originKey1 == &keys[0] && originVal1 == &val2

       // 查询并发哈希表当前元素个数
       size_t curSize = HMS_FAST_ConcurrentHashmap_Size(handle); // curSize == 9

       // 清空并发哈希表中所有元素
       HMS_FAST_ConcurrentHashmap_Clear(handle);
       curSize = HMS_FAST_ConcurrentHashmap_Size(handle); // curSize == 0

       for (int i = 0; i < 6; i++) {
           int* key = new int{i};
           int* val = new int{i};
           ret = HMS_FAST_ConcurrentHashmap_Insert(
               handle,
               (FAST_ConcurrentHashmapKeyPtr)key,
               (FAST_ConcurrentHashmapValuePtr)val,
               nullptr
           );
       } // {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

       // 使用Traverse接口对符合custom_modify_cond的元素执行custom_work操作
       int context = 10;
       HMS_FAST_ConcurrentHashmap_Traverse(
           handle,
           (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_modify_cond,
           nullptr,
           (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_work,
           (void*)&context
       ); // {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15}

       // 使用EraseIf接口删除所有符合custom_erase_cond的键值对并使用custom_free清理相应的内存
       ret = HMS_FAST_ConcurrentHashmap_EraseIf(
           handle,
           (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_erase_cond,
           nullptr,
           (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_free,
           nullptr
       ); // size == 0 && ret == 6

       // 销毁并发哈希表
       HMS_FAST_ConcurrentHashmap_Destroy(handle);
       return 0;
   }
   ```
