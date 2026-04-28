---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-clouddatabase
title: cloudDatabase (云数据库模块)
breadcrumb: API参考 > 应用服务 > Cloud Foundation Kit（云开发服务） > ArkTS API > cloudDatabase (云数据库模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:32+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:dfbfdce7f90285f985565c2ccc5bf6cd7f7c75cf189b4c029763d7b0a73eff21
---

本模块提供使用云数据库进行数据写入、查询、删除等操作的能力。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
```

## zone

PhonePC/2in1TabletTVWearable

zone(zone: string): DatabaseZone

通过zone名称初始化云数据库实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zone | string | 是 | zone的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseZone](cloudfoundation-clouddatabase.md#databasezone) | 云数据库处理数据的实例。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';

3. let databaseZone = cloudDatabase.zone("storageArea");
```

## DatabaseZone

PhonePC/2in1TabletTVWearable

云数据库处理数据的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

### query

PhonePC/2in1TabletTVWearable

query<T extends DatabaseObject>(condition: DatabaseQuery<T>): Promise<T[]>

通过条件查询数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | 是 | 提供丰富的查询条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，返回查询结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. // 在代码工程中创建BookInfo.ets文件
2. import { cloudDatabase } from '@kit.CloudFoundationKit';

4. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject
5. class BookInfo extends cloudDatabase.DatabaseObject{
6. public naturalbase_ClassName(): string {
7. return 'BookInfo';
8. }
9. public key_string: string | undefined;
10. public key_boolean: boolean | undefined;
11. public key_byte: number | undefined;
12. public key_short: number | undefined;
13. public key_integer: number | undefined;
14. public key_long: number | undefined;
15. public key_float: number | undefined;
16. public key_double: number | undefined;
17. public key_text: string | undefined;
18. public key_date: Date | undefined;
19. public key_byte_array: Uint8Array | undefined;
20. }

22. export { BookInfo };
```

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BookInfo } from 'xx/BookInfo'; // 在云数据库代码工程中引入BookInfo.ets文件，xx是文件的路径

5. try {
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.equalTo('key_string', 'string_123');
9. let bookInfoArray = await databaseZone.query(condition);
10. hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}`);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
13. }
```

### query

PhonePC/2in1TabletTVWearable

query<T extends DatabaseObject>(condition: DatabaseQuery<T>, callback: AsyncCallback<T[]>): void

通过条件查询数据。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | 是 | 提供丰富的查询条件。 |
| callback | AsyncCallback<T[]> | 是 | 回调函数。当查询数据成功，err为undefined，data为查询到的结果数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

6. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
9. condition.equalTo('key_string', 'string_123');
10. databaseZone.query(condition, (err: BusinessError, bookInfoArray) => {
11. if (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
13. } else {
14. hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}`);
15. }
16. });
```

### calculateQuery

PhonePC/2in1TabletTVWearable

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate): Promise<number>

从数据库中查询符合条件的数据，并对指定字段进行算术计算。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | 是 | 提供丰富的查询条件。 |
| fieldName | string | 是 | 指定查询对象中要计算的字段名称。 |
| calculate | [QueryCalculate](cloudfoundation-clouddatabase.md#querycalculate) | 是 | 云数据库查询算术计算的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回查询字段名称算术运算结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. try {
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
9. condition.lessThan('key_integer', 100);
10. let count = await databaseZone.calculateQuery(condition, 'key_integer', cloudDatabase.QueryCalculate.AVERAGE);
11. hilog.info(0x0000, 'testTag', `Succeeded in calculating queried data, result: ${count}`);
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to calculate queried data, code: ${err.code}, message: ${err.message}`);
14. }
```

### calculateQuery

PhonePC/2in1TabletTVWearable

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate, callback: AsyncCallback<number>): void

从数据库中查询符合条件的数据，并对指定字段进行算术计算。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | 是 | 提供丰富的查询条件。 |
| fieldName | string | 是 | 指定查询对象中要计算的字段名称。 |
| calculate | [QueryCalculate](cloudfoundation-clouddatabase.md#querycalculate) | 是 | 云数据库查询算术计算的类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回查询字段名称算术运算结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

6. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
9. condition.lessThan('key_integer', 100);
10. databaseZone.calculateQuery(condition, 'key_integer', cloudDatabase.QueryCalculate.AVERAGE,
11. (err: BusinessError, num) => {
12. if (err) {
13. hilog.error(0x0000, 'testTag', `Failed to calculate queried data, code: ${err.code}, message: ${err.message}`);
14. } else {
15. hilog.info(0x0000, 'testTag', `Succeeded in calculating queried data, result: ${num}`);
16. }
17. });
```

### upsert

PhonePC/2in1TabletTVWearable

upsert<T extends DatabaseObject>(objectList: T[] | T): Promise<number>

向数据库更新数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectList | T[] | T | 是 | 一个或多个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回更新成功的数据数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. try {
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let book = new BookInfo();
9. book.key_string = 'string_12';
10. book.key_integer = 90;
11. let book1 = new BookInfo();
12. book1.key_string = 'string_1234';
13. book1.key_integer = 101;
14. let num = await databaseZone.upsert([book, book1]);
15. hilog.info(0x0000, 'testTag', `Succeeded in upserting data, result: ${num}`);
16. } catch (err) {
17. hilog.error(0x0000, 'testTag', `Failed to upsert data, code: ${err.code}, message: ${err.message}`);
18. }
```

### upsert

PhonePC/2in1TabletTVWearable

upsert<T extends DatabaseObject>(objectList: T[] | T, callback: AsyncCallback<number>): void

向数据库更新数据。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectList | T[] | T | 是 | 一个或多个对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回更新成功的数据数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

6. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let book = new BookInfo();
9. book.key_string = 'string_12';
10. book.key_integer = 90;
11. let book1 = new BookInfo();
12. book1.key_string = 'string_1234';
13. book1.key_integer = 101;
14. databaseZone.upsert([book, book1], (err: BusinessError, num) => {
15. if (err) {
16. hilog.error(0x0000, 'testTag', `Failed to upsert data, code: ${err.code}, message: ${err.message}`);
17. } else {
18. hilog.info(0x0000, 'testTag', `Succeeded in upserting data, result: ${num}`);
19. }
20. });
```

### delete

PhonePC/2in1TabletTVWearable

delete<T extends DatabaseObject>(objectList: T[] | T): Promise<number>

在数据库中删除一条或者多条数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectList | T[] | T | 是 | 一个或多个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回删除成功的数据数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. try {
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
9. condition.lessThan('key_integer', 100);
10. let bookArray = await databaseZone.query(condition);
11. let deleteNum = await databaseZone.delete(bookArray);
12. hilog.info(0x0000, 'testTag', `Succeeded in deleting a book, result: ${deleteNum}`);
13. } catch (err) {
14. hilog.error(0x0000, 'testTag', `Failed to delete a book, code: ${err.code}, message: ${err.message}`);
15. }
```

### delete

PhonePC/2in1TabletTVWearable

delete<T extends DatabaseObject>(objectList: T[] | T, callback: AsyncCallback<number>): void

在数据库中删除一条或者多条数据。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectList | T[] | T | 是 | 一个或多个对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回删除成功的数据数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008230001 | Network connection error. |
| 1008230002 | Schema config error. |
| 1008230003 | Natural object error. |
| 1008230009 | Client internal error. |
| 1008231001 | Server error. |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径

6. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
7. let databaseZone = cloudDatabase.zone('storageArea');
8. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
9. condition.lessThan('key_integer', 100);
10. try {
11. let bookArray = await databaseZone.query(condition);
12. databaseZone.delete(bookArray, (err: BusinessError, num) => {
13. if (err) {
14. hilog.error(0x0000, 'testTag', `Failed to delete a book, code: ${err.code}, message: ${err.message}`);
15. } else {
16. hilog.info(0x0000, 'testTag', `Succeeded in deleting a book, result: ${num}`);
17. }
18. });
19. } catch (err) {
20. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
21. }
```

## DatabaseObject

PhonePC/2in1TabletTVWearable

数据库数据类型基类，在云端生成表结构时继承。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

### naturalbase\_ClassName

PhonePC/2in1TabletTVWearable

naturalbase\_ClassName(): string

数据类型基类名称。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回数据类型基类名称，需要与创建的对象类型名称一致。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';

3. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
4. class BookInfo extends cloudDatabase.DatabaseObject{
5. public naturalbase_ClassName(): string {
6. return "BookInfo";
7. }
8. }

10. export { BookInfo };
```

## FieldType

PhonePC/2in1TabletTVWearable

type FieldType = string | number | boolean | Uint8Array | Date

云数据库支持的数据类型。取值类型为下表类型中的并集/交集。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| string | 表示值类型为字符，可取任意值。 |
| number | 表示值类型为数字，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或者false。 |
| Uint8Array | 表示值类型为8位无符号整型数组，可取任意值。 |
| Date | 表示值类型为日期，值固定格式为“YYYY-MM-DD”。 |

## QueryCalculate

PhonePC/2in1TabletTVWearable

枚举， 查询算术计算类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AVERAGE | 0 | 计算平均数。 |
| SUM | 1 | 计算总和。 |
| MAXIMUM | 2 | 计算最大值。 |
| MINIMUM | 3 | 计算最小值。 |
| COUNT | 4 | 计算记录总数。 |

## DatabaseQuery

PhonePC/2in1TabletTVWearable

DatabaseQuery<T extends DatabaseObject>

提供丰富的谓词查询来构建查询条件。根据谓词查询方法构造自己的DatabaseQuery对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

### constructor

PhonePC/2in1TabletTVWearable

constructor(entityClass: new () => T)

构造查询实体类信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entityClass | new () => T | 是 | 数据对象的实体类。 |

### equalTo

PhonePC/2in1TabletTVWearable

equalTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中某个字段的值等于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.equalTo('key_string', 'string_123');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### notEqualTo

PhonePC/2in1TabletTVWearable

notEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中某个字段的值不等于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.notEqualTo('key_string', 'string_123');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### beginsWith

PhonePC/2in1TabletTVWearable

beginsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中string类型字段值以指定子串开头的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.beginsWith('key_string', 'key');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### endsWith

PhonePC/2in1TabletTVWearable

endsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中string类型字段值以指定子串结尾的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.endsWith('key_string', 'string');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### contains

PhonePC/2in1TabletTVWearable

contains(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类中字符串类型字段值包含指定子字符串的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.contains('key_string', 'string');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值大于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.greaterThan('key_integer', 100);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值大于或等于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.greaterThanOrEqualTo('key_integer', 100);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### lessThan

PhonePC/2in1TabletTVWearable

lessThan(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值小于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.lessThan('key_integer', 100);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

添加实体类字段值小于或等于指定值的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| value | [FieldType](cloudfoundation-clouddatabase.md#fieldtype) | 是 | 云数据库中支持的数据类型的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.lessThanOrEqualTo('key_integer', 100);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### in

PhonePC/2in1TabletTVWearable

in(fieldName: string, values: FieldType[]): DatabaseQuery<T>

添加实体类字段值包含在指定数组中的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |
| values | [FieldType](cloudfoundation-clouddatabase.md#fieldtype)[] | 是 | 云数据库中支持的数据类型的值的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.in('key_integer', [100, 200]);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### isNull

PhonePC/2in1TabletTVWearable

isNull(fieldName: string): DatabaseQuery<T>

添加实体类某字段值为空的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.isNull('key_date');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### isNotNull

PhonePC/2in1TabletTVWearable

isNotNull(fieldName: string): DatabaseQuery<T>

添加实体类某字段值不为空的查询条件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.isNotNull('key_date');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### orderByAsc

PhonePC/2in1TabletTVWearable

orderByAsc(fieldName: string): DatabaseQuery<T>

按指定字段升序对查询结果进行排序。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.orderByAsc('key_integer');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### orderByDesc

PhonePC/2in1TabletTVWearable

orderByDesc(fieldName: string): DatabaseQuery<T>

按指定字段降序对查询结果进行排序。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fieldName | string | 是 | 实体类中的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.orderByDesc('key_integer');
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### orderByRandom

PhonePC/2in1TabletTVWearable

orderByRandom(): DatabaseQuery<T>

调用此方法可以将查询结果按随机顺序展示。

说明

使用orderByRandom()对数据进行排序时，建议与limit()配合使用。否则，当该对象类型的数据记录数量过多时，可能会影响查询效率，导致查询超时或失败。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 6.0.1(21)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.orderByRandom().limit(10);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### limit

PhonePC/2in1TabletTVWearable

limit(count: number, offset?: number): DatabaseQuery<T>

指定返回的查询结果集中的数据记录条数。如果不设置offset，则默认从首个对象开始获取前count个对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 限制可以获得的数据记录数量。 |
| offset | number | 否 | 指定数据记录的起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.lessThan('key_integer', 100);
9. condition.limit(4, 1);
10. try {
11. let bookInfoArray = await databaseZone.query(condition);
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
14. }
```

### beginGroup

PhonePC/2in1TabletTVWearable

beginGroup(): DatabaseQuery<T>

调用此方法是为了放置左括号“(”附加到任何查询条件并将右括号“)”与相同的查询连接起来组合使用。

说明

* beginGroup()和endGroup()必须成对出现，并且必须与其他查询条件一起使用。
* 在beginGroup()和endGroup()之间，必须存在以下查询条件中的一个或多个：

  equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()。
* beginGroup()不能直接用在and()和or()之前。即不支持beginGroup().and()、beginGroup().and().endGroup()、beginGroup().or()和beginGroup().or().endGroup()。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.beginGroup().equalTo('string_string', 'string_123').endGroup();
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### endGroup

PhonePC/2in1TabletTVWearable

endGroup(): DatabaseQuery<T>

调用此方法是为了放置右括号“)”附加到任何查询条件并将左括号“(”与相同的查询连接起来组合使用。

说明

* beginGroup()和endGroup()必须成对出现，并且必须与其他查询条件一起使用。
* 在beginGroup()和endGroup()之间，必须存在以下查询条件中的一个或多个：

  equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()。
* endGroup()不能直接用在and()和or()之前。即不支持and().endGroup()、beginGroup().and().endGroup()、or().endGroup()和beginGroup().or().endGroup()。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.beginGroup().equalTo('string_string', 'string_123').endGroup();
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### or

PhonePC/2in1TabletTVWearable

or(): DatabaseQuery<T>

使用or运算组合两个条件并返回两个查询结果的并集。

说明

* or()只能与其他查询条件一起使用。
* 当和equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()一起使用时，返回两个查询结果的交集。
* 当or()与and()一起使用时，or()前面不能直接跟and()，即不支持and().or()。
* 与beginGroup()和endGroup()结合使用时：

  + 支持多层嵌套，beginGroup()和endGroup()必须成对出现。
  + beginGroup()不能在or()之前使用，endGroup()不能在or()之后使用。
  + 即不支持beginGroup().or()、beginGroup().or().endGroup()和or().endGroup()。
  + 不能与orderByAsc()、orderByDesc()或limit()一起使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.equalTo('string_string', 'string_123').or().lessThan('key_integer', 50);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```

### and

PhonePC/2in1TabletTVWearable

and(): DatabaseQuery<T>

使用and运算组合两个条件并返回两个查询结果的交集。

说明

* and()只能与其他查询条件一起使用。
* 当和equalTo()、notEqualTo()、greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、in()、beginsWith()、endsWith()、isNull()、isNotNull()和contains()一起使用时，返回两个查询结果的交集。
* 当and()与or()一起使用时，and()后面不能直接跟or()，即不支持and().or()。
* 与beginGroup()和endGroup()结合使用时：

  + 支持多层嵌套，beginGroup()和endGroup()必须成对出现。
  + beginGroup()不能在and()之前使用，endGroup()不能在and()之后使用。
  + 即不支持beginGroup().and()、beginGroup().and().endGroup()和and().endGroup()。
  + 不能与orderByAsc()、orderByDesc()或limit()一起使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DatabaseQuery](cloudfoundation-clouddatabase.md#databasequery)<T> | DatabaseQuery对象。 |

**示例：**

```
1. import { cloudDatabase } from '@kit.CloudFoundationKit';
2. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的路径
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 创建一个BookInfo的类继承 cloudDatabase.DatabaseObject ，内容与使用Promise异步回调的query接口示例一致
6. let databaseZone = cloudDatabase.zone('storageArea');
7. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
8. condition.equalTo('string_string', 'string_123').and().lessThan('key_integer', 50);
9. try {
10. let bookInfoArray = await databaseZone.query(condition);
11. } catch (err) {
12. hilog.error(0x0000, 'testTag', `Failed to query books, code: ${err.code}, message: ${err.message}`);
13. }
```
