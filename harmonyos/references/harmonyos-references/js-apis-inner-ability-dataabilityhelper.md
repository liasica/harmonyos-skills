---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper
title: DataAbilityHelper
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > ability > DataAbilityHelper
category: harmonyos-references
scraped_at: 2026-04-28T07:58:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e504fc4ed1dc2112c7838bde65c73c63eb1ac945d392e6f3ac9e2a5f779659ce
---

可以通过[acquireDataAbilityHelper](js-apis-ability-featureability.md#featureabilityacquiredataabilityhelper7)接口获取DataAbilityHelper对象。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import ability from '@ohos.ability.ability';
```

## 使用说明

PhonePC/2in1TabletTVWearable

使用前根据具体情况引入如下模块

```
1. import ohos_data_ability from '@ohos.data.dataAbility';
2. import relationalStore from '@ohos.data.relationalStore';
```

## DataAbilityHelper.openFile

PhonePC/2in1TabletTVWearable

openFile(uri: string, mode: string, callback: AsyncCallback<number>): void

打开指定uri对应的文件，返回文件描述符。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的uri。 |
| mode | string | 是 | 表示文件打开模式，可以设置为‘r’表示只读访问，‘w’表示只写访问，‘rw’表示读写访问等。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回文件描述符。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. let mode = 'rw';
8. DAHelper.openFile('dataability:///com.example.DataAbility', mode, (error, data) => {
9. if (error && error.code !== 0) {
10. console.error(`openFile fail, error: ${JSON.stringify(error)}`);
11. } else {
12. console.info(`openFile success, data: ${JSON.stringify(data)}`);
13. }
14. });
```

## DataAbilityHelper.openFile

PhonePC/2in1TabletTVWearable

openFile(uri: string, mode: string): Promise<number>

打开指定uri对应的文件，返回文件描述符。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的uri。 |
| mode | string | 是 | 表示文件打开模式，可以设置为‘r’表示只读访问，‘w’表示只写访问，‘rw’表示读写访问等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件说明符。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. let mode = 'rw';
8. DAHelper.openFile('dataability:///com.example.DataAbility', mode).then((data) => {
9. console.info(`openFile data: ${JSON.stringify(data)}`);
10. });
```

## DataAbilityHelper.on('dataChange')

PhonePC/2in1TabletTVWearable

on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void

注册观察者以监听uri指定数据的数据变化通知。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示监听操作类型，'dataChange'表示数据变化操作。 |
| uri | string | 是 | 表示待监听数据变化的uri。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当注册观察者以监听uri指定数据的数据变化通知成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. function onChangeNotify() {
8. console.info('onChangeNotify call back');
9. };
10. DAHelper.on(
11. 'dataChange',
12. 'dataability:///com.example.DataAbility',
13. onChangeNotify
14. );
```

## DataAbilityHelper.off('dataChange')

PhonePC/2in1TabletTVWearable

off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void

注销观察者以停止监听uri指定数据的数据变化通知。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示监听操作类型，'dataChange'表示数据变化操作。 |
| uri | string | 是 | 表示待取消监听数据变化的uri。 |
| callback | AsyncCallback<void> | 否 | 回调函数。当注销观察者以停止监听uri指定数据的数据变化通知成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. function onChangeNotify() {
8. console.info('onChangeNotify call back');
9. };
10. DAHelper.off(
11. 'dataChange',
12. 'dataability:///com.example.DataAbility',
13. onChangeNotify
14. );
15. DAHelper.off(
16. 'dataChange',
17. 'dataability:///com.example.DataAbility',
18. );
```

## DataAbilityHelper.getType

PhonePC/2in1TabletTVWearable

getType(uri: string, callback: AsyncCallback<string>): void

获取给定uri指向数据的媒体资源类型。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取数据的uri。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回与uri指向数据匹配的媒体资源类型。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.getType('dataability:///com.example.DataAbility', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`getType fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`getType success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.getType

PhonePC/2in1TabletTVWearable

getType(uri: string): Promise<string>

获取给定uri指向数据的媒体资源类型。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取数据的uri。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回与uri指向数据匹配的媒体资源类型。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.getType('dataability:///com.example.DataAbility').then((data) => {
8. console.info(`getType data: ${JSON.stringify(data)}`);
9. });
```

## DataAbilityHelper.getFileTypes

PhonePC/2in1TabletTVWearable

getFileTypes(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void

获取支持的文件媒体资源类型。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取文件的uri。 |
| mimeTypeFilter | string | 是 | 表示待获取文件的媒体资源类型。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回匹配的媒体资源类型数组。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.getFileTypes( 'dataability:///com.example.DataAbility', 'image/*', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`getFileTypes fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`getFileTypes success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.getFileTypes

PhonePC/2in1TabletTVWearable

getFileTypes(uri: string, mimeTypeFilter: string): Promise<Array<string>>

获取支持的文件媒体资源类型。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取文件的uri。 |
| mimeTypeFilter | string | 是 | 表示待获取文件的媒体资源类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回匹配的媒体资源类型数组。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.getFileTypes('dataability:///com.example.DataAbility', 'image/*').then((data) => {
8. console.info(`getFileTypes data: ${JSON.stringify(data)}`);
9. });
```

## DataAbilityHelper.normalizeUri

PhonePC/2in1TabletTVWearable

normalizeUri(uri: string, callback: AsyncCallback<string>): void

将引用数据功能的给定uri转换为规范化uri。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |
| callback | AsyncCallback<string> | 是 | 回调函数，如果数据功能支持uri规范化，则返回规范化uri对象；否则返回null。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.normalizeUri('dataability:///com.example.DataAbility', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`normalizeUri fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`normalizeUri success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.normalizeUri

PhonePC/2in1TabletTVWearable

normalizeUri(uri: string): Promise<string>

将引用数据功能的给定uri转换为规范化uri。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，如果数据功能支持uri规范化，则返回规范化uri对象；否则返回null。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.normalizeUri('dataability:///com.example.DataAbility').then((data) => {
8. console.info(`normalizeUri data: ${JSON.stringify(data)}`);
9. });
```

## DataAbilityHelper.denormalizeUri

PhonePC/2in1TabletTVWearable

denormalizeUri(uri: string, callback: AsyncCallback<string>): void

将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要反规范化的uri对象。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回反规范化uri对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.denormalizeUri('dataability:///com.example.DataAbility', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`denormalizeUri fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`denormalizeUri success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.denormalizeUri

PhonePC/2in1TabletTVWearable

denormalizeUri(uri: string): Promise<string>

将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回反规范化uri对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.denormalizeUri('dataability:///com.example.DataAbility').then((data) => {
8. console.info(`denormalizeUri data: ${JSON.stringify(data)}`);
9. });
```

## DataAbilityHelper.notifyChange

PhonePC/2in1TabletTVWearable

notifyChange(uri: string, callback: AsyncCallback<void>): void

通知注册的观察者，uri指定数据的数据变化。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示数据变化的uri。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知注册的观察者成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.notifyChange('dataability:///com.example.DataAbility', (error) => {
8. if (error && error.code !== 0) {
9. console.error(`notifyChange fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info('notifyChange success');
12. }
13. });
```

## DataAbilityHelper.notifyChange

PhonePC/2in1TabletTVWearable

notifyChange(uri: string): Promise<void>

通知注册的观察者，uri指定数据的数据变化。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示数据变化的uri。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.notifyChange('dataability:///com.example.DataAbility').then(() => {
8. console.info('================>notifyChangeCallback================>');
9. });
```

## DataAbilityHelper.insert

PhonePC/2in1TabletTVWearable

insert(uri: string, valuesBucket: [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket), callback: AsyncCallback<number>): void

将单个数据记录插入数据库。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBucket | [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要插入的数据记录。如果此参数为空，将插入一个空行。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回插入数据记录的索引。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. const valueBucket: rdb.ValuesBucket = {
9. 'name': 'rose',
10. 'age': 22,
11. 'salary': 200.5,
12. 'blobType': 'u8',
13. };
14. DAHelper.insert('dataability:///com.example.DataAbility', valueBucket, (error, data) => {
15. if (error && error.code !== 0) {
16. console.error(`insert fail, error: ${JSON.stringify(error)}`);
17. } else {
18. console.info(`insert success, data: ${JSON.stringify(data)}`);
19. }
20. });
```

## DataAbilityHelper.insert

PhonePC/2in1TabletTVWearable

insert(uri: string, valuesBucket: [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket)): Promise<number>

将单个数据记录插入数据库。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBucket | [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要插入的数据记录。如果此参数为空，将插入一个空行。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回插入数据记录的索引。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. const valueBucket: rdb.ValuesBucket = {
9. 'name': 'rose1',
10. 'age': 221,
11. 'salary': 20.5,
12. 'blobType': 'u8',
13. };
14. DAHelper.insert('dataability:///com.example.DataAbility', valueBucket).then((data) => {
15. console.info(`insert data: ${JSON.stringify(data)}`);
16. });
```

## DataAbilityHelper.batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void

将多个数据记录插入数据库。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBuckets | Array<[rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket)> | 是 | 表示要插入的数据记录数组。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回插入的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let cars = new Array({'name': 'roe11', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
9. {'name': 'roe12', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
10. {'name': 'roe13', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket);
11. DAHelper.batchInsert('dataability:///com.example.DataAbility', cars, (error, data) => {
12. if (error && error.code !== 0) {
13. console.error(`batchInsert fail, error: ${JSON.stringify(error)}`);
14. } else {
15. console.info(`batchInsert success, data: ${JSON.stringify(data)}`);
16. }
17. });
```

## DataAbilityHelper.batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>): Promise<number>

将多个数据记录插入数据库。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBuckets | Array<[rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket)> | 是 | 表示要插入的数据记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回插入的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let cars = new Array({'name': 'roe11', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
9. {'name': 'roe12', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
10. {'name': 'roe13', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket);
11. DAHelper.batchInsert('dataability:///com.example.DataAbility', cars).then((data) => {
12. console.info(`batchInsert data: ${JSON.stringify(data)}`);
13. });
```

## DataAbilityHelper.delete

PhonePC/2in1TabletTVWearable

delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void

从数据库中删除一个或多个数据记录。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回已删除的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let da = new ohos_data_ability.DataAbilityPredicates();
9. DAHelper.delete('dataability:///com.example.DataAbility', da, (error, data) => {
10. if (error && error.code !== 0) {
11. console.error(`delete fail, error: ${JSON.stringify(error)}`);
12. } else {
13. console.info(`delete success, data: ${JSON.stringify(data)}`);
14. }
15. });
```

## DataAbilityHelper.delete

PhonePC/2in1TabletTVWearable

delete(uri: string, predicates?: dataAbility.DataAbilityPredicates): Promise<number>

从数据库中删除一个或多个数据记录。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已删除的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let da = new ohos_data_ability.DataAbilityPredicates();
9. DAHelper.delete('dataability:///com.example.DataAbility', da).then((data) => {
10. console.info(`delete data: ${JSON.stringify(data)}`);
11. });
```

## DataAbilityHelper.delete

PhonePC/2in1TabletTVWearable

delete(uri: string, callback: AsyncCallback<number>): void

predicates筛选条件为空，自定义数据库删除数据记录的处理逻辑。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回已删除的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.delete('dataability:///com.example.DataAbility', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`delete fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`delete success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.update

PhonePC/2in1TabletTVWearable

update(uri: string, valuesBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void

更新数据库中的数据记录。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要更新的数据。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回更新的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';
4. import rdb from '@ohos.data.rdb';

6. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
7. 'dataability:///com.example.DataAbility'
8. );
9. const va: rdb.ValuesBucket = {
10. 'name': 'roe1',
11. 'age': 21,
12. 'salary': 20.5,
13. 'blobType': 'u8',
14. };
15. let da = new ohos_data_ability.DataAbilityPredicates();
16. DAHelper.update('dataability:///com.example.DataAbility', va, da, (error, data) => {
17. if (error && error.code !== 0) {
18. console.error(`update fail, error: ${JSON.stringify(error)}`);
19. } else {
20. console.info(`update success, data: ${JSON.stringify(data)}`);
21. }
22. });
```

## DataAbilityHelper.update

PhonePC/2in1TabletTVWearable

update(uri: string, valuesBucket: rdb.ValuesBucket, predicates?: dataAbility.DataAbilityPredicates): Promise<number>

更新数据库中的数据记录。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要更新的数据。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回更新的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';
4. import rdb from '@ohos.data.rdb';

6. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
7. 'dataability:///com.example.DataAbility'
8. );
9. const va: rdb.ValuesBucket = {
10. 'name': 'roe1',
11. 'age': 21,
12. 'salary': 20.5,
13. 'blobType': 'u8',
14. };
15. let da = new ohos_data_ability.DataAbilityPredicates();
16. DAHelper.update('dataability:///com.example.DataAbility', va, da).then((data) => {
17. console.info(`update data: ${JSON.stringify(data)}`);
18. });
```

## DataAbilityHelper.update

PhonePC/2in1TabletTVWearable

update(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void

predicates筛选条件为空，自定义更新数据库的处理逻辑。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | [rdb.ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要更新的数据。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回更新的数据记录数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. const va: rdb.ValuesBucket = {
9. 'name': 'roe1',
10. 'age': 21,
11. 'salary': 20.5,
12. 'blobType': 'u8',
13. };
14. DAHelper.update('dataability:///com.example.DataAbility', va, (error, data) => {
15. if (error && error.code !== 0) {
16. console.error(`update fail, error: ${JSON.stringify(error)}`);
17. } else {
18. console.info(`update success, data: ${JSON.stringify(data)}`);
19. }
20. });
```

## DataAbilityHelper.query

PhonePC/2in1TabletTVWearable

query(uri: string, columns: Array<string>, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void

查询数据库中的数据。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array<string> | 是 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 回调函数，返回查询结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let cars=new Array('value1', 'value2', 'value3', 'value4');
9. let da = new ohos_data_ability.DataAbilityPredicates();
10. DAHelper.query('dataability:///com.example.DataAbility', cars, da, (error, data) => {
11. if (error && error.code !== 0) {
12. console.error(`query fail, error: ${JSON.stringify(error)}`);
13. } else {
14. console.info(`query success, data: ${JSON.stringify(data)}`);
15. }
16. });
```

## DataAbilityHelper.query

PhonePC/2in1TabletTVWearable

query(uri: string, callback: AsyncCallback<ResultSet>): void

查询数据库中的数据。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 回调函数，返回查询结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. DAHelper.query('dataability:///com.example.DataAbility', (error, data) => {
8. if (error && error.code !== 0) {
9. console.error(`query fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`query success, data: ${JSON.stringify(data)}`);
12. }
13. });
```

## DataAbilityHelper.query

PhonePC/2in1TabletTVWearable

query(uri: string, columns: Array<string>, callback: AsyncCallback<ResultSet>): void

查询数据库中的数据。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array<string> | 是 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 回调函数，返回查询结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.DataAbility'
6. );
7. let cars = new Array('value1', 'value2', 'value3', 'value4');
8. DAHelper.query('dataability:///com.example.DataAbility', cars, (error, data) => {
9. if (error && error.code !== 0) {
10. console.error(`query fail, error: ${JSON.stringify(error)}`);
11. } else {
12. console.info(`query success, data: ${JSON.stringify(data)}`);
13. }
14. });
```

## DataAbilityHelper.query

PhonePC/2in1TabletTVWearable

query(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void

查询数据库中的数据。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 回调函数，返回查询结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let da = new ohos_data_ability.DataAbilityPredicates();
9. DAHelper.query('dataability:///com.example.DataAbility', da, (error, data) => {
10. if (error && error.code !== 0) {
11. console.error(`query fail, error: ${JSON.stringify(error)}`);
12. } else {
13. console.info(`query success, data: ${JSON.stringify(data)}`);
14. }
15. });
```

## DataAbilityHelper.query

PhonePC/2in1TabletTVWearable

query(uri: string, columns?: Array<string>, predicates?: dataAbility.DataAbilityPredicates): Promise<ResultSet>

查询数据库中的数据。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array<string> | 否 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象，返回查询结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import ohos_data_ability from '@ohos.data.dataAbility';

5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.DataAbility'
7. );
8. let cars = new Array('value1', 'value2', 'value3', 'value4');
9. let da = new ohos_data_ability.DataAbilityPredicates();
10. DAHelper.query('dataability:///com.example.DataAbility', cars, da).then((data) => {
11. console.info(`query data: ${JSON.stringify(data)}`);
12. });
```

## DataAbilityHelper.call

PhonePC/2in1TabletTVWearable

call(uri: string, method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void

调用DataAbility的扩展接口。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx' |
| method | string | 是 | 表示被调用的方法名。 |
| arg | string | 是 | 表示需传入的参数。 |
| extras | [PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap) | 是 | 表示扩展的键值对参数。 |
| callback | AsyncCallback<[PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap)> | 是 | 回调函数，返回扩展的键值对参数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
5. 'dataability:///com.example.jsapidemo.UserDataAbility'
6. );
7. dataAbilityHelper.call('dataability:///com.example.jsapidemo.UserDataAbility',
8. 'method', 'arg', {'key1':'value1'}, (error, data) => {
9. if (error && error.code !== 0) {
10. console.error(`call fail, error: ${JSON.stringify(error)}`);
11. } else {
12. console.info(`call success, data: ${JSON.stringify(data)}`);
13. }
14. });
```

## DataAbilityHelper.call

PhonePC/2in1TabletTVWearable

call(uri: string, method: string, arg: string, extras: PacMap): Promise<PacMap>

调用DataAbility的扩展接口。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx' |
| method | string | 是 | 表示被调用的方法名。 |
| arg | string | 是 | 表示需传入的参数。 |
| extras | [PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap) | 是 | 表示扩展的键值对参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap)> | Promise对象，返回扩展的键值对参数。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import { BusinessError } from '@ohos.base';

5. let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
6. 'dataability:///com.example.jsapidemo.UserDataAbility'
7. );
8. dataAbilityHelper.call('dataability:///com.example.jsapidemo.UserDataAbility',
9. 'method', 'arg', {'key1':'value1'}).then((data) => {
10. console.info(`call success, data: ${data}`);
11. }).catch((error: BusinessError) => {
12. console.error(`call failed, error: ${error}`);
13. });
```

## DataAbilityHelper.executeBatch

PhonePC/2in1TabletTVWearable

executeBatch(uri: string, operations: Array<DataAbilityOperation>, callback: AsyncCallback<Array<DataAbilityResult>>): void

批量操作数据库中的数据。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| operations | Array<[DataAbilityOperation](js-apis-inner-ability-dataabilityoperation.md)> | 是 | 表示数据操作数组，其中可以包含对数据库的多个不同操作。 |
| callback | AsyncCallback<Array<[DataAbilityResult](js-apis-inner-ability-dataabilityresult.md)>> | 是 | 回调函数，在DataAbilityResult数组中返回每个操作的结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';

4. // 根据DataAbilityOperation列表选择要对数据库做的操作
5. let op: Array<ability.DataAbilityOperation> = new Array();
6. let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
7. 'dataability:///com.example.jsapidemo.UserDataAbility'
8. );
9. dataAbilityHelper.executeBatch('dataability:///com.example.jsapidemo.UserDataAbility', op, (error, data) => {
10. if (error && error.code !== 0) {
11. console.error(`executeBatch fail, error: ${JSON.stringify(error)}`);
12. } else {
13. console.info(`executeBatch success, data: ${JSON.stringify(data)}`);
14. }
15. });
```

## DataAbilityHelper.executeBatch

PhonePC/2in1TabletTVWearable

executeBatch(uri: string, operations: Array<DataAbilityOperation>): Promise<Array<DataAbilityResult>>

批量操作数据库中的数据。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| operations | Array<[DataAbilityOperation](js-apis-inner-ability-dataabilityoperation.md)> | 是 | 表示数据操作数组，其中可以包含对数据库的多个不同操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[DataAbilityResult](js-apis-inner-ability-dataabilityresult.md)>> | Promise对象，在DataAbilityResult数组中返回每个操作的结果。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import { BusinessError } from '@ohos.base';

5. // 根据DataAbilityOperation列表选择要对数据库做的操作
6. let op: Array<ability.DataAbilityOperation> = new Array();
7. let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
8. 'dataability:///com.example.jsapidemo.UserDataAbility'
9. );
10. dataAbilityHelper.executeBatch('dataability:///com.example.jsapidemo.UserDataAbility', op).then((data) => {
11. console.info(`executeBatch success, data: ${data}`);
12. }).catch((error: BusinessError) => {
13. console.error(`executeBatch failed, error: ${error}`);
14. });
```

## PacMap

PhonePC/2in1TabletTVWearable

用于存储数据的PacMap类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [key: string] | number | string | boolean | Array<string | number | boolean> | null | 否 | 是 | 数据存储在键值对中。 |
