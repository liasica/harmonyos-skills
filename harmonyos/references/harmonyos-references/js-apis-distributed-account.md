---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-account
title: @ohos.account.distributedAccount (分布式账号管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 账号管理 > @ohos.account.distributedAccount (分布式账号管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8d60bf89107efb6cbf3f0c696b76be9dfcbcb594ea692f44a040e99b94c2ba92
---

本模块提供管理分布式账号的一些基础功能，主要包括查询和更新账号登录状态。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { distributedAccount } from '@kit.BasicServicesKit';
```

## distributedAccount.getDistributedAccountAbility

PhonePC/2in1TabletTVWearable

getDistributedAccountAbility(): DistributedAccountAbility

获取分布式账号单实例对象。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DistributedAccountAbility](js-apis-distributed-account.md#distributedaccountability) | 返回一个实例，实例提供查询和更新分布式账号登录状态方法。 |

**示例：**

```
1. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
```

## DistributedAccountAbility

PhonePC/2in1TabletTVWearable

提供查询和更新分布式账号登录状态方法（需要先获取分布式账号的单实例对象）。

### getOsAccountDistributedInfo9+

PhonePC/2in1TabletTVWearable

getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void

获取分布式账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.GET\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | 是 | 回调参数。当获取分布式账号信息成功，err为undefined，data为获取到的分布式账号信息对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. try {
5. accountAbility.getOsAccountDistributedInfo(
6. (err: BusinessError, data: distributedAccount.DistributedInfo) => {
7. if (err) {
8. console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('distributed information: ' + JSON.stringify(data));
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### getOsAccountDistributedInfo9+

PhonePC/2in1TabletTVWearable

getOsAccountDistributedInfo(): Promise<DistributedInfo>

获取分布式账号信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.GET\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | Promise对象，返回分布式账号信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | System service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. try {
5. accountAbility.getOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
6. console.info('distributed information: ' + JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### queryOsAccountDistributedInfo(deprecated)

PhonePC/2in1TabletTVWearable

queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void

获取分布式账号信息。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountDistributedInfo](js-apis-distributed-account.md#getosaccountdistributedinfo9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | 是 | 回调函数。当获取分布式账号信息成功，err为undefined，data为获取到的分布式账号信息对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. accountAbility.queryOsAccountDistributedInfo(
5. (err: BusinessError, data: distributedAccount.DistributedInfo) => {
6. if (err) {
7. console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('distributed information: ' + JSON.stringify(data));
10. }
11. });
```

### queryOsAccountDistributedInfo(deprecated)

PhonePC/2in1TabletTVWearable

queryOsAccountDistributedInfo(): Promise<DistributedInfo>

获取分布式账号信息。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountDistributedInfo](js-apis-distributed-account.md#getosaccountdistributedinfo9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | Promise对象，返回分布式账号信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. accountAbility.queryOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
5. console.info('distributed information: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
8. });
```

### setOsAccountDistributedInfo9+

PhonePC/2in1TabletTVWearable

setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void

更新分布式账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新分布式账号信息成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid accountInfo. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. let accountInfo: distributedAccount.DistributedInfo =
5. { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
6. try {
7. accountAbility.setOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
8. if (err) {
9. console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
10. } else {
11. console.info('setOsAccountDistributedInfo successfully');
12. }
13. });
14. } catch (e) {
15. const err = e as BusinessError;
16. console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
17. }
```

### setOsAccountDistributedInfo9+

PhonePC/2in1TabletTVWearable

setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>

更新分布式账号信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid accountInfo. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. let accountInfo: distributedAccount.DistributedInfo =
5. { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
6. try {
7. accountAbility.setOsAccountDistributedInfo(accountInfo).then(() => {
8. console.info('setOsAccountDistributedInfo successfully');
9. }).catch((err: BusinessError) => {
10. console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### updateOsAccountDistributedInfo(deprecated)

PhonePC/2in1TabletTVWearable

updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void

更新分布式账号信息。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setOsAccountDistributedInfo](js-apis-distributed-account.md#setosaccountdistributedinfo9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新分布式账号信息成功时，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. let accountInfo: distributedAccount.DistributedInfo =
5. { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
6. accountAbility.updateOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
7. if (err) {
8. console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('updateOsAccountDistributedInfo successfully');
11. }
12. });
```

### updateOsAccountDistributedInfo(deprecated)

PhonePC/2in1TabletTVWearable

updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>

更新分布式账号信息。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setOsAccountDistributedInfo](js-apis-distributed-account.md#setosaccountdistributedinfo9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
4. let accountInfo: distributedAccount.DistributedInfo =
5. { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
6. accountAbility.updateOsAccountDistributedInfo(accountInfo).then(() => {
7. console.info('updateOsAccountDistributedInfo successfully');
8. }).catch((err: BusinessError) => {
9. console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
10. });
```

## DistributedInfo

PhonePC/2in1TabletTVWearable

提供操作系统账号的分布式信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 分布式账号名称，非空字符串。 |
| id | string | 否 | 否 | 分布式账号UID，非空字符串。 |
| event | string | 否 | 否 | 分布式账号登录状态，包括登录、登出、Token失效和注销，分别对应以下字符串：  - Ohos.account.event.LOGIN  - Ohos.account.event.LOGOUT  - Ohos.account.event.TOKEN\_INVALID  - Ohos.account.event.LOGOFF |
| nickname9+ | string | 否 | 是 | 分布式账号的昵称，默认为空。 |
| avatar9+ | string | 否 | 是 | 分布式账号的头像，默认为空。 |
| status10+ | [DistributedAccountStatus](js-apis-distributed-account.md#distributedaccountstatus10) | 是 | 是 | 分布式账号的状态，枚举类型，默认为未登录状态。 |
| scalableData8+ | object | 否 | 是 | 分布式账号扩展信息，根据业务所需，以k-v形式传递定制化信息，默认为空。 |

## DistributedAccountStatus10+

PhonePC/2in1TabletTVWearable

表示分布式账号状态枚举。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_LOGGED\_IN | 0 | 未登录状态。 |
| LOGGED\_IN | 1 | 已登录状态。 |
