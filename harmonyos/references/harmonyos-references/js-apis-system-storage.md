---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-storage
title: "@system.storage (数据存储)"
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @system.storage (数据存储)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a8ecccfa3df4338799d8cfd55db2dc25c8e06a3fca768daee6d38141cca4ec61
---

**说明** 

* 模块维护策略：

  + 对于Lite Wearable设备类型，该模块长期维护，可正常使用。
  + 对于支持该模块的其他设备类型，该模块从API version 6开始不再维护，可以使用模块[@ohos.data.storage (轻量级存储)](js-apis-data-storage.md)。在API version 9后，推荐使用新模块[@ohos.data.preferences (用户首选项)](js-apis-data-preferences.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在FA模型下使用。
* 在以下内容中，对于Lite Wearable设备类型，请参考“JS示例”；对于支持该模块的其他设备类型，请参考“ArkTS示例”。

## 导入模块

```js
import storage from '@system.storage';
```

## storage.get

get(options: GetStorageOptions): void

通过索引读取缓存中存储的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetStorageOptions](js-apis-system-storage.md#getstorageoptions) | 是 | 接口配置信息。 |

**示例：**

ArkTS示例：

```js
export default {
  storageGet() {
    storage.get({
      key: 'storage_key',
      success: function(data) {
        console.info('call storage.get success: ' + data);
      },
      fail: function(data, code) {
        console.error('call storage.get fail, code: ' + code + ', data: ' + data);
      },
      complete: function() {
        console.info('call complete');
      },
    });
  }
}
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        Get Data
    </text>
    <input type="button" value="Get Data" style="width: 240px; height: 50px; margin: 5px;" onclick="storageGet"></input>
</div>
```

```css
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
// xxx.js
import storage from '@system.storage';

export default {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    storageGet() {
        storage.get({
            key: 'storage_key',
            success: function(data) {
                console.info('call storage.get success: ' + data);
            },
            fail: function(data, code) {
                console.error('call storage.get fail, code: ' + code + ', data: ' + data);
            }
        });
    },
}
```

## storage.set

set(options: SetStorageOptions): void

修改缓存中索引对应的值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetStorageOptions](js-apis-system-storage.md#setstorageoptions) | 是 | 接口配置信息。 |

**示例：**

ArkTS示例：

```js
export default {
  storageSet() {
    storage.set({
      key: 'storage_key',
      value: 'storage value',
      success: function() {
        console.info('call storage.set success.');
      },
      fail: function(data, code) {
        console.error('call storage.set fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        Set Data
    </text>
    <input type="button" value="Set Data" style="width: 240px; height: 50px; margin: 5px;" onclick="storageSet"></input>
</div>
```

```css
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
// xxx.js
import storage from '@system.storage';

export default {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    storageSet() {
        storage.set({
            key: 'storage_key',
            value: 'test_storage_value',
            success: function() {
                console.info('call storage.set success.');
            },
            fail: function(data, code) {
                console.error('call storage.set fail, code: ' + code + ', data: ' + data);
            },
        });
    }
}
```

## storage.clear

clear(options?: ClearStorageOptions): void

清空缓存中存储的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ClearStorageOptions](js-apis-system-storage.md#clearstorageoptions) | 否 | 接口配置信息。 |

**示例：**

ArkTS示例：

```js
export default {
  storageClear() {
    storage.clear({
      success: function() {
        console.info('call storage.clear success.');
      },
      fail: function(data, code) {
        console.error('call storage.clear fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        Clear Data
    </text>
    <input type="button" value="Clear Data" style="width: 240px; height: 50px; margin: 5px;" onclick="storageClear"></input>
</div>
```

```css
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
// xxx.js
import storage from '@system.storage';

export default {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    storageClear() {
        storage.clear({
            success: function() {
                console.info('call storage.clear success.');
            },
            fail: function(data, code) {
                console.error('call storage.clear fail, code: ' + code + ', data: ' + data);
            },
        });
    }
}
```

## storage.delete

delete(options: DeleteStorageOptions): void

删除缓存中索引对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DeleteStorageOptions](js-apis-system-storage.md#deletestorageoptions) | 是 | 接口配置信息。 |

**示例：**

ArkTS示例：

```js
export default {
  storageDelete() {
    storage.delete({
      key: 'Storage1',
      success: function() {
        console.info('call storage.delete success.');
      },
      fail: function(data, code) {
        console.error('call storage.delete fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        Delete Data
    </text>
    <input type="button" value="Delete Data" style="width: 240px; height: 50px; margin: 5px;" onclick="storageDelete"></input>
</div>
```

```css
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
// xxx.js
import storage from '@system.storage';

export default {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    storageDelete() {
        storage.delete({
            key: 'storage_key',
            success: function() {
                console.info('call storage.delete success.');
            },
            fail: function(data, code) {
                console.error('call storage.delete fail, code: ' + code + ', data: ' + data);
            },
        });
    }
}
```

## GetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 内容索引。 |
| default | string | 否 | key不存在则返回的默认值。 |
| success | (data: any) => void | 否 | 接口调用成功的回调函数，data为返回key对应的value。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## SetStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储值的索引。 |
| value | string | 是 | 新值。长度需小于128字节。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## ClearStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## DeleteStorageOptions

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 内容索引。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数，data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |
