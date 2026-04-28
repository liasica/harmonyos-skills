---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult
title: Interface (FetchResult)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (FetchResult)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fddac4cfa92ffc81d2b59f1ba5eaf1b51411bc9356664987e5f96bdc0614546b
---

文件检索结果集。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getCount

PhonePC/2in1TabletTV

getCount(): number

获取文件检索结果中的文件总数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 检索到的文件总数。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getCountDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let fetchCount = fetchResult.getCount();
12. console.info('fetchCount = ', fetchCount);
13. }
```

## isAfterLast

PhonePC/2in1TabletTV

isAfterLast(): boolean

检查结果集是否指向最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当读到最后一条记录后，后续没有记录返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
5. let fetchOption: photoAccessHelper.FetchOptions = {
6. fetchColumns: [],
7. predicates: predicates
8. };
9. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
10. let fetchCount = fetchResult.getCount();
11. console.info('count:' + fetchCount);
12. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
13. if (fetchResult.isAfterLast()) {
14. console.info('photoAsset isAfterLast displayName = ', photoAsset.displayName);
15. } else {
16. console.info('photoAsset not isAfterLast.');
17. }
18. }
```

## close

PhonePC/2in1TabletTV

close(): void

释放FetchResult实例并使其失效，无法再调用其他方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('fetchResultCloseDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. fetchResult.close();
13. console.info('close succeed.');
14. } catch (err) {
15. console.error(`close fail. error: ${err.code}, ${err.message}`);
16. }
17. }
```

## getFirstObject

PhonePC/2in1TabletTV

getFirstObject(callback: AsyncCallback<T>): void

获取文件检索结果中的第一个文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<T> | 是 | 回调函数。当获取结果集中的第一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getFirstObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. fetchResult.getFirstObject((err, photoAsset) => {
12. if (photoAsset !== undefined) {
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. } else {
15. console.error(`photoAsset failed with err:${err.code}, ${err.message}`);
16. }
17. });
18. }
```

## getFirstObject

PhonePC/2in1TabletTV

getFirstObject(): Promise<T>

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中第一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getFirstObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. console.info('photoAsset displayName: ', photoAsset.displayName);
13. }
```

## getNextObject

PhonePC/2in1TabletTV

getNextObject(callback: AsyncCallback<T>): void

获取文件检索结果中的下一个文件资产。使用callback异步回调。

在调用此方法之前，必须使用[isAfterLast()](arkts-apis-photoaccesshelper-fetchresult.md#isafterlast)来检查当前位置是否为最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<T> | 是 | 回调函数。当获取结果集中的下一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getNextObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. await fetchResult.getFirstObject();
12. if (!fetchResult.isAfterLast()) {
13. fetchResult.getNextObject((err, photoAsset) => {
14. if (photoAsset !== undefined) {
15. console.info('photoAsset displayName: ', photoAsset.displayName);
16. } else {
17. console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
18. }
19. });
20. }
21. }
```

## getNextObject

PhonePC/2in1TabletTV

getNextObject(): Promise<T>

获取文件检索结果中的下一个文件资产。使用Promise异步回调。

在调用此方法之前，必须使用[isAfterLast()](arkts-apis-photoaccesshelper-fetchresult.md#isafterlast)来检查当前位置是否为最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中下一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getNextObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. await fetchResult.getFirstObject();
12. if (!fetchResult.isAfterLast()) {
13. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getNextObject();
14. console.info('photoAsset displayName: ', photoAsset.displayName);
15. }
16. }
```

## getLastObject

PhonePC/2in1TabletTV

getLastObject(callback: AsyncCallback<T>): void

获取文件检索结果中的最后一个文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<T> | 是 | 回调函数。当获取结果集中的最后一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getLastObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. fetchResult.getLastObject((err, photoAsset) => {
12. if (photoAsset !== undefined) {
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. } else {
15. console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
16. }
17. });
18. }
```

## getLastObject

PhonePC/2in1TabletTV

getLastObject(): Promise<T>

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中的最后一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getLastObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
12. console.info('photoAsset displayName: ', photoAsset.displayName);
13. }
```

## getObjectByPosition

PhonePC/2in1TabletTV

getObjectByPosition(index: number, callback: AsyncCallback<T>): void

获取文件检索结果中具有指定索引的文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取的文件的索引，从0开始。 |
| callback | AsyncCallback<T> | 是 | 回调函数。当获取结果集中指定索引的文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getObjectByPositionDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. fetchResult.getObjectByPosition(0, (err, photoAsset) => {
12. if (photoAsset !== undefined) {
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. } else {
15. console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
16. }
17. });
18. }
```

## getObjectByPosition

PhonePC/2in1TabletTV

getObjectByPosition(index: number): Promise<T>

获取文件检索结果中指定索引的文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取的文件的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中指定索引的一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getObjectByPositionDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. if (fetchResult === undefined) {
12. console.error('fetchResult is undefined');
13. return;
14. }
15. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getObjectByPosition(0);
16. console.info('photoAsset displayName: ', photoAsset.displayName);
17. }
```

## getAllObjects

PhonePC/2in1TabletTV

getAllObjects(callback: AsyncCallback<Array<T>>): void

获取文件检索结果中的所有文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<T>> | 是 | 回调函数。当获取结果集中的所有文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getAllObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. fetchResult.getAllObjects((err, photoAssetList) => {
12. if (photoAssetList !== undefined) {
13. console.info('photoAssetList length: ', photoAssetList.length);
14. } else {
15. console.error(`photoAssetList failed with err:${err.code}, ${err.message}`);
16. }
17. });
18. }
```

## getAllObjects

PhonePC/2in1TabletTV

getAllObjects(): Promise<Array<T>>

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<T>> | Promise对象，返回所有文件资产的数组。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getAllObjectDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
12. console.info('photoAssetList length: ', photoAssetList.length);
13. }
```

## contains23+

PhonePC/2in1TabletTV

contains(object: T): Promise<boolean>

判断文件检索结果中是否包含指定的文件资产。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | T | 是 | 指定的文件资产。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定的文件资产在文件检索结果中；返回false表示指定的文件资产不在文件检索结果中。 |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('fetchResultContainsDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let ret: boolean = await fetchResult.contains(asset);
14. console.info(`succeed. ${ret}`);
15. } catch (err) {
16. console.error(`fail. error: ${err.code}, ${err.message}`);
17. }
18. }
```

## getObjectsByIndexSet23+

PhonePC/2in1TabletTV

getObjectsByIndexSet(indexSet: number[]): Promise<T[]>

获取文件检索结果中指定索引集合对应的文件资产数组。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indexSet | number[] | 是 | 指定的索引集合。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，返回指定索引集合所对应的文件资产数组。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | The scenario parameter verification fails. Possible causes: 1.The indexSet is null,undefined or empty. 2.The indexSet length is bigger than 500. 3.The max value of indexSet is equal or bigger than the fetch result length. 4.The min value of indexSet is less than 0. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('fetchResultGetObjectsByIndexSetDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let indexSet: number[] = [0, 1];
13. let ret: photoAccessHelper.PhotoAsset[] = await fetchResult.getObjectsByIndexSet(indexSet);
14. console.info(`succeed. ${ret.length}`);
15. } catch (err) {
16. console.error(`fail. error: ${err.code}, ${err.message}`);
17. }
18. }
```

## getIndex23+

PhonePC/2in1TabletTV

getIndex(object: T): Promise<number>

获取指定文件资产在文件检索结果中的索引。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | T | 是 | 指定的文件资产。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回查询结果。如果对象在文件检索结果中则返回对应的索引，不存在则返回-1。 |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('fetchResultGetIndexDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let ret: number = await fetchResult.getIndex(asset);
14. console.info(`succeed. ${ret}`);
15. } catch (err) {
16. console.error(`fail. error: ${err.code}, ${err.message}`);
17. }
18. }
```

## getRangeObjects23+

PhonePC/2in1TabletTV

getRangeObjects(index: number, offset: number): Promise<T[]>

在文件检索结果中，从指定索引（第一个参数）开始，获取指定长度（第二个参数）的文件资产数组。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 开始获取的文件资产索引，大于等于0，小于文件检索结果中对象数量。 |
| offset | number | 是 | 要获取的文件资产数量，大于0。  index和offset之和需要小于检索结果中的对象数量，否则抛出23800151错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | 返回Promise异步回调数组。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | The scenario parameter verification fails. Possible causes: index or offset validity check failed. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper} from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('getRangeObjectsDemo');
6. type PhotoAsset = photoAccessHelper.PhotoAsset;
7. let testNum: string = "getRangeObjects_test_003";
8. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
9. let fetchOptions: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: predicates
12. };
13. let fetchResult1: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
14. await phAccessHelper.getAssets(fetchOptions);
15. let fetchResult2: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
16. await phAccessHelper.getAssets(fetchOptions);
17. let count: number = fetchResult1.getCount();
18. const half: number = Math.ceil(count / 2);
19. let promises: Promise<PhotoAsset[]>[] = [];
20. promises[0] = fetchResult1.getRangeObjects(0, half);
21. promises[1] = fetchResult2.getRangeObjects(half, count - half);
22. let photoAssetsArray: PhotoAsset[][] = await Promise.all(promises);
23. let photoAssets: PhotoAsset[] = photoAssetsArray[0].concat(photoAssetsArray[1]);
24. console.info('photoAssets length: ', photoAssets.length);
25. }
```
