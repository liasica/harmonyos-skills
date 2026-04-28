---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-storage
title: @system.storage (数据存储)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @system.storage (数据存储)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9e71faf299c6441dafc0331e1254ddc6583caa9cb61e4be94e7c650854c3a66
---

说明

* 模块维护策略：

  + 对于Lite Wearable设备类型，该模块长期维护，可正常使用。
  + 对于支持该模块的其他设备类型，该模块从API version 6开始不再维护，可以使用模块[@ohos.data.storage](js-apis-data-storage.md)。在API version 9后，推荐使用新模块[@ohos.data.preferences](js-apis-data-preferences.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在FA模型下使用。

## 导入模块

WearableLite Wearable

```
1. import storage from '@system.storage';
```

## storage.get

WearableLite Wearable

get(options: GetStorageOptions): void

通过索引读取缓存中存储的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetStorageOptions](js-apis-system-storage.md#getstorageoptions) | 是 | 接口配置信息。 |

**示例：**

```
1. export default {
2. storageGet() {
3. storage.get({
4. key: 'storage_key',
5. success: function(data) {
6. console.log('call storage.get success: ' + data);
7. },
8. fail: function(data, code) {
9. console.log('call storage.get fail, code: ' + code + ', data: ' + data);
10. },
11. complete: function() {
12. console.log('call complete');
13. },
14. });
15. }
16. }
```

## storage.set

WearableLite Wearable

set(options: SetStorageOptions): void

修改缓存中索引对应的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetStorageOptions](js-apis-system-storage.md#setstorageoptions) | 是 | 接口配置信息。 |

**示例：**

```
1. export default {
2. storageSet() {
3. storage.set({
4. key: 'storage_key',
5. value: 'storage value',
6. success: function() {
7. console.log('call storage.set success.');
8. },
9. fail: function(data, code) {
10. console.log('call storage.set fail, code: ' + code + ', data: ' + data);
11. },
12. });
13. }
14. }
```

## storage.clear

WearableLite Wearable

clear(options?: ClearStorageOptions): void

清空缓存中存储的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ClearStorageOptions](js-apis-system-storage.md#clearstorageoptions) | 否 | 接口配置信息。 |

**示例：**

```
1. export default {
2. storageClear() {
3. storage.clear({
4. success: function() {
5. console.log('call storage.clear success.');
6. },
7. fail: function(data, code) {
8. console.log('call storage.clear fail, code: ' + code + ', data: ' + data);
9. },
10. });
11. }
12. }
```

## storage.delete

WearableLite Wearable

delete(options: DeleteStorageOptions): void

删除缓存中索引对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DeleteStorageOptions](js-apis-system-storage.md#deletestorageoptions) | 是 | 接口配置信息。 |

**示例：**

```
1. export default {
2. storageDelete() {
3. storage.delete({
4. key: 'Storage1',
5. success: function() {
6. console.log('call storage.delete success.');
7. },
8. fail: function(data, code) {
9. console.log('call storage.delete fail, code: ' + code + ', data: ' + data);
10. },
11. });
12. }
13. }
```

## GetStorageOptions

WearableLite Wearable

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 内容索引。 |
| default | string | 否 | key不存在则返回的默认值。 |
| success | (data: any) => void | 否 | 接口调用成功的回调函数，data为返回key对应的value。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## SetStorageOptions

WearableLite Wearable

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储值的索引。 |
| value | string | 是 | 新值。长度需小于128字节。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## ClearStorageOptions

WearableLite Wearable

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## DeleteStorageOptions

WearableLite Wearable

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 内容索引。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |
