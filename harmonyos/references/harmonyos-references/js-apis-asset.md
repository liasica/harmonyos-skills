---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset
title: @ohos.security.asset (关键资产存储服务)
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > ArkTS API > @ohos.security.asset (关键资产存储服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:be9afbe064acd7347050691de188fe348c648c2850047ee6d2e1cdd2cd256dfa
---

关键资产存储服务提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

说明

本模块首批接口从API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { asset } from '@kit.AssetStoreKit';
```

## asset.add

PhonePC/2in1TabletTVWearable

add(attributes: AssetMap): Promise<void>

新增一条关键资产。使用Promise异步回调。

设置[IS\_PERSISTENT](js-apis-asset.md#tag)属性时，需要申请ohos.permission.STORE\_PERSISTENT\_DATA权限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attributes | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The caller doesn't have the permission. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000003 | The asset already exists. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let attr: asset.AssetMap = new Map();
10. attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
11. attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
12. attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
13. attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
14. asset.add(attr).then(() => {
15. console.info(`Succeeded in adding Asset.`);
16. });
```

## asset.addSync12+

PhonePC/2in1TabletTVWearable

addSync(attributes: AssetMap): void

新增一条关键资产，使用同步方式返回结果。

如果要设置[IS\_PERSISTENT](js-apis-asset.md#tag)属性，需要申请ohos.permission.STORE\_PERSISTENT\_DATA权限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attributes | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The caller doesn't have the permission. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000003 | The asset already exists. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let attr: asset.AssetMap = new Map();
10. attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
11. attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
12. attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
13. attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
14. asset.addSync(attr);
```

## asset.remove

PhonePC/2in1TabletTVWearable

remove(query: AssetMap): Promise<void>

删除符合条件的一条或多条关键资产。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. asset.remove(query).then(() => {
12. console.info(`Succeeded in removing Asset.`);
13. });
```

## asset.removeSync12+

PhonePC/2in1TabletTVWearable

removeSync(query: AssetMap): void

删除符合条件的一条或多条关键资产，使用同步方式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. asset.removeSync(query);
```

## asset.update

PhonePC/2in1TabletTVWearable

update(query: AssetMap, attributesToUpdate: AssetMap): Promise<void>

更新符合条件的一条关键资产。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。 |
| attributesToUpdate | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待更新关键资产的属性集合，如关键资产明文、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. let attrsToUpdate: asset.AssetMap = new Map();
12. attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
13. asset.update(query, attrsToUpdate).then(() => {
14. console.info(`Succeeded in updating Asset.`);
15. });
```

## asset.updateSync12+

PhonePC/2in1TabletTVWearable

updateSync(query: AssetMap, attributesToUpdate: AssetMap): void

更新符合条件的一条关键资产，使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。 |
| attributesToUpdate | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待更新关键资产的属性集合，如关键资产明文、自定义数据等。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. let attrsToUpdate: asset.AssetMap = new Map();
12. attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
13. asset.updateSync(query, attrsToUpdate);
```

## asset.preQuery

PhonePC/2in1TabletTVWearable

preQuery(query: AssetMap): Promise<Uint8Array>

查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.query](js-apis-asset.md#assetquery)和[asset.postQuery](js-apis-asset.md#assetpostquery)接口。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回挑战值。  **说明：** 挑战值用于后续的用户认证。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. asset.preQuery(query).then((challenge: Uint8Array) => {
12. console.info(`Succeeded in pre-querying Asset.`);
13. });
```

## asset.preQuerySync12+

PhonePC/2in1TabletTVWearable

preQuerySync(query: AssetMap): Uint8Array

查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.querySync](js-apis-asset.md#assetquerysync12)、[asset.postQuerySync](js-apis-asset.md#assetpostquerysync12)。使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 挑战值。  **说明：** 挑战值用于后续用户认证。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. let challenge: Uint8Array = asset.preQuerySync(query);
12. console.info(`Succeeded in pre-querying with sync, the challenge is: `, challenge);
```

## asset.query

PhonePC/2in1TabletTVWearable

query(query: AssetMap): Promise<Array<AssetMap>>

查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[asset.preQuery](js-apis-asset.md#assetprequery)接口，在本函数后调用[asset.postQuery](js-apis-asset.md#assetpostquery)接口，开发步骤请参考[开发指导](../harmonyos-guides/asset-js-query-auth.md)。使用Promise异步回调。

如果未查询到符合条件的关键资产，将抛出“未找到关键资产”的异常，而非返回空的查询结果列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<AssetMap>> | Promise对象，返回查询结果列表。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000004 | Access denied. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000017 | The capability is not supported. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. // 如果只需要返回关键资产的属性，可以将RETURN_TYPE设置为ATTRIBUTES。返回属性不需解密，查询时间较短。
12. query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
13. asset.query(query).then((res: Array<asset.AssetMap>) => {
14. for (let i = 0; i < res.length; i++) {
15. // 解析属性。
16. let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
17. console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
18. }
19. console.info(`Succeeded in querying Asset.`);
20. });
```

## asset.querySync12+

PhonePC/2in1TabletTVWearable

querySync(query: AssetMap): Array<AssetMap>

查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[asset.preQuerySync](js-apis-asset.md#assetprequerysync12)，在本函数后调用[asset.postQuerySync](js-apis-asset.md#assetpostquerysync12)，开发步骤请参考[开发指导](../harmonyos-guides/asset-js-query-auth.md)。使用同步方式返回结果。

如果未查询到符合条件的关键资产，将抛出“未找到关键资产”的异常，而非返回空的查询结果列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<AssetMap> | 查询结果列表。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Incorrect parameter types.  2. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000004 | Access denied. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000017 | The capability is not supported. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';
2. import { util } from '@kit.ArkTS';

4. function stringToArray(str: string): Uint8Array {
5. let textEncoder = new util.TextEncoder();
6. return textEncoder.encodeInto(str);
7. }

9. let query: asset.AssetMap = new Map();
10. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
11. // 如果只需要返回关键资产的属性，可以将RETURN_TYPE设置为ATTRIBUTES。返回属性不需解密，查询时间较短。
12. query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
13. let res: Array<asset.AssetMap> = asset.querySync(query);
14. for (let i = 0; i < res.length; i++) {
15. // 解析属性。
16. let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
17. console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
18. }
19. console.info(`Succeeded in querying Asset.`);
```

## asset.postQuery

PhonePC/2in1TabletTVWearable

postQuery(handle: AssetMap): Promise<void>

查询的后置处理，用于需要用户认证的关键资产（与[asset.preQuery](js-apis-asset.md#assetprequery)函数成对出现）。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待处理的查询句柄，包含[asset.preQuery](js-apis-asset.md#assetprequery)执行成功返回的挑战值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';

3. let handle: asset.AssetMap = new Map();
4. // 此处传入的new Uint8Array(32)仅作为示例，实际应传入asset.preQuery执行成功返回的挑战值。
5. handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
6. asset.postQuery(handle).then(() => {
7. console.info(`Succeeded in post-querying Asset.`);
8. });
```

## asset.postQuerySync12+

PhonePC/2in1TabletTVWearable

postQuerySync(handle: AssetMap): void

查询的后置处理，用于需要用户认证的关键资产。需与[asset.preQuerySync](js-apis-asset.md#assetprequerysync12)函数成对出现。使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | [AssetMap](js-apis-asset.md#assetmap) | 是 | 待处理的查询句柄，包含[asset.preQuerySync](js-apis-asset.md#assetprequerysync12)执行成功返回的挑战值。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';

3. let handle: asset.AssetMap = new Map();
4. // 此处传入的new Uint8Array(32)仅作为示例，实际应传入asset.preQuerySync执行成功返回的挑战值。
5. handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
6. asset.postQuerySync(handle)
```

## asset.querySyncResult20+

PhonePC/2in1TabletTVWearable

querySyncResult(query: AssetMap): Promise<SyncResult>

执行同步操作后，查询同步执行结果。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [AssetMap](js-apis-asset.md#assetmap) | 是 | 同步结果查询条件，如关键资产所属群组、业务自定义属性信息是否加密。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SyncResult](js-apis-asset.md#syncresult20)> | Promise对象，返回同步执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000018 | Parameter verification failed. |

**示例：**

```
1. import { asset } from '@kit.AssetStoreKit';

3. let query: asset.AssetMap = new Map();
4. asset.querySyncResult(query).then((res: asset.SyncResult) => {
5. console.info(`Succeeded in querying sync result: ${JSON.stringify(res)}`);
6. });
```

## TagType

PhonePC/2in1TabletTVWearable

枚举，关键资产属性支持的数据类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOOL | 0x01 << 28 | 标识关键资产属性对应的数据类型是布尔。 |
| NUMBER | 0x02 << 28 | 标识关键资产属性对应的数据类型是整型。 |
| BYTES | 0x03 << 28 | 标识关键资产属性对应的数据类型是字节数组。 |

## Tag

PhonePC/2in1TabletTVWearable

枚举，关键资产支持的属性名称类型，用作[AssetMap](js-apis-asset.md#assetmap)的键。

**系统能力：** SystemCapability.Security.Asset

说明

以下为Tag类型的全量枚举值，每个接口可传的Tag枚举及对应的Value取值范围不同，详见[各个场景的开发指导](../harmonyos-guides/asset-store-kit-overview.md)。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECRET | TagType.BYTES | 0x01 | 关键资产明文。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| ALIAS | TagType.BYTES | 0x02 | 关键资产别名，每条关键资产的唯一索引。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| ACCESSIBILITY | TagType.NUMBER | 0x03 | 基于锁屏状态的访问控制。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| REQUIRE\_PASSWORD\_SET | TagType.BOOL | 0x04 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AUTH\_TYPE | TagType.NUMBER | 0x05 | 访问关键资产所需的用户认证类型。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AUTH\_VALIDITY\_PERIOD | TagType.NUMBER | 0x06 | 用户认证的有效期。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AUTH\_CHALLENGE | TagType.BYTES | 0x07 | 用户认证的挑战值。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AUTH\_TOKEN | TagType.BYTES | 0x08 | 用户认证通过的授权令牌。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| SYNC\_TYPE | TagType.NUMBER | 0x10 | 关键资产支持的同步类型。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| IS\_PERSISTENT | TagType.BOOL | 0x11 | 在应用卸载时是否保留关键资产。 |
| DATA\_LABEL\_CRITICAL\_1 | TagType.BYTES | 0x20 | 关键资产附属信息，内容由业务自定义且**有完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_CRITICAL\_2 | TagType.BYTES | 0x21 | 关键资产附属信息，内容由业务自定义且**有完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_CRITICAL\_3 | TagType.BYTES | 0x22 | 关键资产附属信息，内容由业务自定义且**有完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_CRITICAL\_4 | TagType.BYTES | 0x23 | 关键资产附属信息，内容由业务自定义且**有完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_1 | TagType.BYTES | 0x30 | 关键资产附属信息，内容由业务自定义且**无完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_2 | TagType.BYTES | 0x31 | 关键资产附属信息，内容由业务自定义且**无完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_3 | TagType.BYTES | 0x32 | 关键资产附属信息，内容由业务自定义且**无完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_4 | TagType.BYTES | 0x33 | 关键资产附属信息，内容由业务自定义且**无完整性保护**。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_112+ | TagType.BYTES | 0x34 | 关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_212+ | TagType.BYTES | 0x35 | 关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_312+ | TagType.BYTES | 0x36 | 关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_412+ | TagType.BYTES | 0x37 | 关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RETURN\_TYPE | TagType.NUMBER | 0x40 | 关键资产查询返回的结果类型。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RETURN\_LIMIT | TagType.NUMBER | 0x41 | 关键资产查询返回的结果数量。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RETURN\_OFFSET | TagType.NUMBER | 0x42 | 关键资产查询返回的结果偏移量。  **说明：** 用于分批查询场景，指定从第几个开始返回。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RETURN\_ORDERED\_BY | TagType.NUMBER | 0x43 | 关键资产查询返回的结果排序依据，仅支持按照附属信息排序。  **说明：** 默认按照关键资产新增的顺序返回。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| CONFLICT\_RESOLUTION | TagType.NUMBER | 0x44 | 新增关键资产时的冲突（如：别名相同）处理策略。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| UPDATE\_TIME12+ | TagType.BYTES | 0x45 | 数据的更新时间（时间戳形式）。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| OPERATION\_TYPE12+ | TagType.NUMBER | 0x46 | 附加的操作类型。 |
| REQUIRE\_ATTR\_ENCRYPTED14+ | TagType.BOOL | 0x47 | 是否加密业务自定义附属信息。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| GROUP\_ID18+ | TagType.BYTES | 0x48 | 关键资产所属群组。 |
| WRAP\_TYPE18+ | TagType.NUMBER | 0x49 | 关键资产支持的加密导入导出类型。 |

## Value

PhonePC/2in1TabletTVWearable

type Value = boolean | number | Uint8Array

关键资产属性的内容，用作[AssetMap](js-apis-asset.md#assetmap)的值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 类型 | 说明 |
| --- | --- |
| boolean | 表示值类型为布尔类型，取值范围为true或false。 |
| number | 表示值类型为数字，取值范围为Tag对应的枚举值或数值。 |
| Uint8Array | 表示值类型为字节数组，内容由业务自定义。 |

## AssetMap

PhonePC/2in1TabletTVWearable

type AssetMap = Map<Tag, Value>

关键资产属性的键-值对集合。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 类型 | 说明 |
| --- | --- |
| Map<Tag, Value> | 表示值类型是Map，键值对取值范围分别参考[Tag](js-apis-asset.md#tag)和[Value](js-apis-asset.md#value)。 |

## Accessibility

PhonePC/2in1TabletTVWearable

枚举，关键资产基于锁屏状态的访问控制类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_POWERED\_ON | 0 | 开机后可访问。 |
| DEVICE\_FIRST\_UNLOCKED | 1 | 首次解锁后可访问  **说明：** 未设置锁屏密码时，等同于开机后可访问。 |
| DEVICE\_UNLOCKED | 2 | 解锁状态时可访问  **说明：** 未设置锁屏密码时，等同于开机后可访问。 |

## AuthType

PhonePC/2in1TabletTVWearable

枚举，关键资产支持的用户认证类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0x00 | 访问关键资产前无需用户认证。 |
| ANY | 0xFF | 任意一种用户认证方式（PIN码、人脸、指纹等）通过后，均可访问关键资产。 |

## SyncType

PhonePC/2in1TabletTVWearable

枚举，关键资产支持的同步类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEVER | 0 | 不允许同步关键资产。 |
| THIS\_DEVICE | 1 << 0 | 只在本设备进行同步，如仅在本设备还原的备份场景。  **说明：** 本字段是能力预埋，当前不支持。 |
| TRUSTED\_DEVICE | 1 << 1 | 只在可信设备间进行同步，如克隆场景。 |
| TRUSTED\_ACCOUNT12+ | 1 << 2 | 只在登录可信账号的设备间进行同步，如云同步场景。  **说明：** 本字段是能力预埋，当前不支持。 |

## ReturnType

PhonePC/2in1TabletTVWearable

枚举，关键资产查询返回的结果类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 返回关键资产明文及属性。  **说明：** 查询单条关键资产明文时，需设置此类型。 |
| ATTRIBUTES | 1 | 返回关键资产属性，不含关键资产明文。  **说明：** 批量查询关键资产属性时，需设置此类型。 |

## ConflictResolution

PhonePC/2in1TabletTVWearable

枚举，新增关键资产时的冲突（如：别名相同）处理策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERWRITE | 0 | 覆盖原有的关键资产。 |
| THROW\_ERROR | 1 | 抛出异常，由业务进行后续处理。 |

## OperationType12+

PhonePC/2in1TabletTVWearable

枚举，附属的操作类型。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEED\_SYNC | 0 | 需要进行同步操作。 |
| NEED\_LOGOUT | 1 | 需要进行登出操作。 |

## WrapType18+

PhonePC/2in1TabletTVWearable

枚举，关键资产支持的加密导入导出类型。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEVER | 0 | 不允许加密导入导出关键资产。 |
| TRUSTED\_ACCOUNT | 1 | 只在登录可信账号的设备进行加密导入导出关键资产。 |

## SyncResult20+

PhonePC/2in1TabletTVWearable

关键资产同步的结果。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 是 | 否 | 关键资产同步的结果码。同步成功时结果码为0，同步失败时结果码参考[ErrorCode](js-apis-asset.md#errorcode)。 |
| totalCount | number | 是 | 是 | 触发同步的关键资产总数。 |
| failedCount | number | 是 | 是 | 关键资产同步失败的数量。 |

## ErrorCode

PhonePC/2in1TabletTVWearable

表示错误码的枚举。

**系统能力：** SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERMISSION\_DENIED | 201 | 调用方无权限。 |
| NOT\_SYSTEM\_APPLICATION12+ | 202 | 调用方不是一个系统应用。 |
| INVALID\_ARGUMENT | 401 | 参数错误。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| SERVICE\_UNAVAILABLE | 24000001 | 关键资产服务不可用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| NOT\_FOUND | 24000002 | 未找到关键资产。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DUPLICATED | 24000003 | 关键资产已存在。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| ACCESS\_DENIED | 24000004 | 访问被拒绝。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| STATUS\_MISMATCH | 24000005 | 锁屏状态不匹配。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| OUT\_OF\_MEMORY | 24000006 | 系统内存不足。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATA\_CORRUPTED | 24000007 | 关键资产损坏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DATABASE\_ERROR | 24000008 | 数据库操作失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| CRYPTO\_ERROR | 24000009 | 算法库操作失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| IPC\_ERROR | 24000010 | 进程通信错误。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| BMS\_ERROR | 24000011 | 包管理服务异常。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| ACCOUNT\_ERROR | 24000012 | 账号系统服务异常。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| ACCESS\_TOKEN\_ERROR | 24000013 | 访问控制服务异常。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| FILE\_OPERATION\_ERROR | 24000014 | 文件操作失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| GET\_SYSTEM\_TIME\_ERROR | 24000015 | 获取系统时间失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| LIMIT\_EXCEEDED | 24000016 | 缓存数量超限。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| UNSUPPORTED | 24000017 | 该子功能不支持。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| PARAM\_VERIFICATION\_FAILED20+ | 24000018 | 参数校验失败。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
