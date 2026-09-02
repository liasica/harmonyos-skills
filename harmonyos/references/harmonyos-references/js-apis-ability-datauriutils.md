---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-datauriutils
title: "@ohos.ability.dataUriUtils (DataUriUtils模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.ability.dataUriUtils (DataUriUtils模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:42c2fe199da3a7c17527489aeceb48df85e0d040ba0a910508dd01bb8c421a28
---

DataUriUtils模块提供用于处理uri对象的能力，包括获取、绑定、删除和更新指定uri对象的路径末尾的ID。

**说明** 

本模块首批接口从API version 7开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.dataUriUtils](js-apis-app-ability-datauriutils.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';
```

## dataUriUtils.getId

getId(uri: string): number

获取指定uri路径末尾的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示uri对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回uri路径末尾的ID。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = dataUriUtils.getId('com.example.dataUriUtils/1221');
```

## dataUriUtils.attachId

attachId(uri: string, id: number): string

将ID附加到uri的路径末尾。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示uri对象。 |
| id | number | 是 | 表示要附加的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回附加ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
    id,
);
```

## dataUriUtils.deleteId

deleteId(uri: string): string

删除指定uri路径末尾的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要从中删除ID的uri对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回删除ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let uri = dataUriUtils.deleteId('com.example.dataUriUtils/1221');
```

## dataUriUtils.updateId

updateId(uri: string, id: number): string

更新指定uri中的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示uri对象。 |
| id | number | 是 | 表示要更新的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回更新ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.updateId(
    'com.example.dataUriUtils/1221',
    id
);
```
