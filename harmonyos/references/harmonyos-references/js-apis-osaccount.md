---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount
title: @ohos.account.osAccount (系统账号管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 账号管理 > @ohos.account.osAccount (系统账号管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7970e2ac2a9af1f02a1865eea414dd262a98f5412944d60142764bc92f1a99ad
---

本模块提供管理系统账号的基础能力，包括系统账号的添加、删除、查询、设置、订阅、启动等功能。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { osAccount } from '@kit.BasicServicesKit';
```

## osAccount.getAccountManager

PhonePC/2in1TabletTVWearable

getAccountManager(): AccountManager

获取系统账号管理对象。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AccountManager](js-apis-osaccount.md#accountmanager) | 系统账号管理对象。 |

**示例：**

```
1. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```

## OsAccountType

PhonePC/2in1TabletTVWearable

表示系统账号类型的枚举。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN | 0 | 管理员账号。 |
| NORMAL | 1 | 普通账号。 |
| GUEST | 2 | 访客账号。 |

## AccountManager

PhonePC/2in1TabletTVWearable

系统账号管理类。

### checkMultiOsAccountEnabled9+

PhonePC/2in1TabletTVWearable

checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void

判断是否支持多系统账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持多系统账号；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.checkMultiOsAccountEnabled((err: BusinessError, isEnabled: boolean) => {
6. if (err) {
7. console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
15. }
```

### checkMultiOsAccountEnabled9+

PhonePC/2in1TabletTVWearable

checkMultiOsAccountEnabled(): Promise<boolean>

判断是否支持多系统账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持多系统账号；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
5. accountManager.checkMultiOsAccountEnabled().then((isEnabled: boolean) => {
6. console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
7. }).catch((err: BusinessError) => {
8. console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
13. }
```

### checkOsAccountActivated(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void

判断指定系统账号是否处于激活状态。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示账号已激活；返回false表示账号未激活。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否处于激活状态

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.checkOsAccountActivated(localId, (err: BusinessError, isActivated: boolean) => {
7. if (err) {
8. console.error(`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('checkOsAccountActivated successfully, isActivated:' + isActivated);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### checkOsAccountActivated(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountActivated(localId: number): Promise<boolean>

判断指定系统账号是否处于激活状态。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示账号已激活；返回false表示账号未激活。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否处于激活状态

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.checkOsAccountActivated(localId).then((isActivated: boolean) => {
7. console.info('checkOsAccountActivated successfully, isActivated: ' + isActivated);
8. }).catch((err: BusinessError) => {
9. console.error(`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### isOsAccountConstraintEnabled11+

PhonePC/2in1TabletTVWearable

isOsAccountConstraintEnabled(constraint: string): Promise<boolean>

判断当前系统账号是否使能指定约束。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | string | 是 | 指定的[约束](js-apis-osaccount.md#系统账号约束列表)名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let constraint: string = 'constraint.wifi';
5. try {
6. accountManager.isOsAccountConstraintEnabled(constraint).then((isEnabled: boolean) => {
7. console.info('isOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
8. }).catch((err: BusinessError) => {
9. console.error(`isOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`isOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### checkOsAccountConstraintEnabled(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

判断指定系统账号是否具有指定约束。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的[约束](js-apis-osaccount.md#系统账号约束列表)名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. let constraint: string = 'constraint.wifi';
6. try {
7. accountManager.checkOsAccountConstraintEnabled(localId, constraint, (err: BusinessError, isEnabled: boolean)=>{
8. if (err) {
9. console.error(`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
10. } else {
11. console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
12. }
13. });
14. } catch (e) {
15. const err = e as BusinessError;
16. console.error(`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
17. }
```

### checkOsAccountConstraintEnabled(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>

判断指定系统账号是否具有指定约束。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的[约束](js-apis-osaccount.md#系统账号约束列表)名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. let constraint: string = 'constraint.wifi';
6. try {
7. accountManager.checkOsAccountConstraintEnabled(localId, constraint).then((isEnabled: boolean) => {
8. console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
9. }).catch((err: BusinessError) => {
10. console.error(`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### checkOsAccountTestable9+

PhonePC/2in1TabletTVWearable

checkOsAccountTestable(callback: AsyncCallback<boolean>): void

检查当前系统账号是否为测试账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.checkOsAccountTestable((err: BusinessError, isTestable: boolean) => {
6. if (err) {
7. console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkOsAccountTestable code is ${err.code}, message is ${err.message}`);
15. }
```

### checkOsAccountTestable9+

PhonePC/2in1TabletTVWearable

checkOsAccountTestable(): Promise<boolean>

检查当前系统账号是否为测试账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.checkOsAccountTestable().then((isTestable: boolean) => {
6. console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
7. }).catch((err: BusinessError) => {
8. console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`checkOsAccountTestable exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### isOsAccountUnlocked11+

PhonePC/2in1TabletTVWearable

isOsAccountUnlocked(): Promise<boolean>

检查当前系统账号是否已认证解锁。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.isOsAccountUnlocked().then((isVerified: boolean) => {
6. console.info('isOsAccountUnlocked successfully, isVerified: ' + isVerified);
7. }).catch((err: BusinessError) => {
8. console.error(`isOsAccountUnlocked failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`isOsAccountUnlocked exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### checkOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountVerified(callback: AsyncCallback<boolean>): void

检查当前系统账号是否已认证解锁。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[isOsAccountUnlocked](js-apis-osaccount.md#isosaccountunlocked11)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.checkOsAccountVerified((err: BusinessError, isVerified: boolean) => {
6. if (err) {
7. console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### checkOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountVerified(): Promise<boolean>

检查当前系统账号是否已认证解锁。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[isOsAccountUnlocked](js-apis-osaccount.md#isosaccountunlocked11)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.checkOsAccountVerified().then((isVerified: boolean) => {
6. console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
7. }).catch((err: BusinessError) => {
8. console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### checkOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

检查指定系统账号是否已验证。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.checkOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
7. if (err) {
8. console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### checkOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

checkOsAccountVerified(localId: number): Promise<boolean>

检查指定系统账号是否已验证。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。不填则检查当前系统账号是否已验证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.checkOsAccountVerified(localId).then((isVerified: boolean) => {
7. console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
8. }).catch((err: BusinessError) => {
9. console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getOsAccountCount9+

PhonePC/2in1TabletTVWearable

getOsAccountCount(callback: AsyncCallback<number>): void

获取已创建的系统账号数量。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为已创建的系统账号的数量；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountCount((err: BusinessError, count: number) => {
6. if (err) {
7. console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountCount successfully, count: ' + count);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getOsAccountCount9+

PhonePC/2in1TabletTVWearable

getOsAccountCount(): Promise<number>

获取已创建的系统账号数量。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已创建的系统账号的数量。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountCount().then((count: number) => {
6. console.info('getOsAccountCount successfully, count: ' + count);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getOsAccountLocalId9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalId(callback: AsyncCallback<number>): void

获取当前进程所属的系统账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为当前进程所属的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountLocalId((err: BusinessError, localId: number) => {
6. if (err) {
7. console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountLocalId successfully, localId: ' + localId);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getOsAccountLocalId9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalId(): Promise<number>

获取当前进程所属的系统账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前进程所属的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountLocalId().then((localId: number) => {
6. console.info('getOsAccountLocalId successfully, localId: ' + localId);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getOsAccountLocalIdForUid9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void

根据uid查询对应的系统账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为对应的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号的账号ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let uid: number = 12345678;
5. try {
6. accountManager.getOsAccountLocalIdForUid(uid, (err: BusinessError, localId: number) => {
7. if (err) {
8. console.error(`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}`);
9. }
10. console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getOsAccountLocalIdForUid9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForUid(uid: number): Promise<number>

根据uid查询对应的系统账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回指定uid对应的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let uid: number = 12345678;
5. try {
6. accountManager.getOsAccountLocalIdForUid(uid).then((localId: number) => {
7. console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
8. }).catch((err: BusinessError) => {
9. console.error(`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getOsAccountLocalIdForUidSync10+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForUidSync(uid: number): number

根据uid查询对应的系统账号ID。使用同步方式返回结果。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定uid对应的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let uid: number = 12345678;
5. try {
6. let localId : number = accountManager.getOsAccountLocalIdForUidSync(uid);
7. console.info('getOsAccountLocalIdForUidSync successfully, localId: ' + localId);
8. } catch (e) {
9. const err = e as BusinessError;
10. console.error(`getOsAccountLocalIdForUidSync exception: code is ${err.code}, message is ${err.message}`);
11. }
```

### getOsAccountLocalIdForDomain9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

根据域账号信息，获取与其关联的系统账号ID。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 域账号信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为域账号关联的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
5. try {
6. accountManager.getOsAccountLocalIdForDomain(domainInfo, (err: BusinessError, localId: number) => {
7. if (err) {
8. console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### getOsAccountLocalIdForDomain9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回域账号关联的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
5. try {
6. accountManager.getOsAccountLocalIdForDomain(domainInfo).then((localId: number) => {
7. console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
8. }).catch((err: BusinessError) => {
9. console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getOsAccountConstraints(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

获取指定系统账号的全部约束。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，如果获取成功，err为null，data为该系统账号的全部[约束](js-apis-osaccount.md#系统账号约束列表)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号的全部约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.getOsAccountConstraints(localId, (err: BusinessError, constraints: string[]) => {
7. if (err) {
8. console.error(`getOsAccountConstraints failed, err: code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('getOsAccountConstraints successfully, constraints: ' + JSON.stringify(constraints));
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### getOsAccountConstraints(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountConstraints(localId: number): Promise<Array<string>>

获取指定系统账号的全部约束。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回指定系统账号的全部[约束](js-apis-osaccount.md#系统账号约束列表)。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号的全部约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.getOsAccountConstraints(localId).then((constraints: string[]) => {
7. console.info('getOsAccountConstraints, constraints: ' + constraints);
8. }).catch((err: BusinessError) => {
9. console.error(`getOsAccountConstraints err: code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getActivatedOsAccountLocalIds9+

PhonePC/2in1TabletTVWearable

getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。如果查询成功，err为null，data为当前处于激活状态的系统账号的ID列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getActivatedOsAccountLocalIds((err: BusinessError, idArray: number[])=>{
6. if (err) {
7. console.error(`getActivatedOsAccountLocalIds code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getActivatedOsAccountLocalIds idArray length:' + idArray.length);
10. for(let i=0;i<idArray.length;i++) {
11. console.info('activated os account id: ' + idArray[i]);
12. }
13. }
14. });
15. } catch (e) {
16. const err = e as BusinessError;
17. console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
18. }
```

### getActivatedOsAccountLocalIds9+

PhonePC/2in1TabletTVWearable

getActivatedOsAccountLocalIds(): Promise<Array<number>>

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回当前处于激活状态的系统账号的ID列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getActivatedOsAccountLocalIds().then((idArray: number[]) => {
6. console.info('getActivatedOsAccountLocalIds, idArray: ' + idArray);
7. }).catch((err: BusinessError) => {
8. console.error(`getActivatedOsAccountLocalIds err: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getCurrentOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

查询当前进程所属的系统账号的信息。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.GET\_LOCAL\_ACCOUNTS10+，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OsAccountInfo](js-apis-osaccount.md#osaccountinfo)> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
6. if (err) {
7. console.error(`getCurrentOsAccount code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getCurrentOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentOsAccount(): Promise<OsAccountInfo>

查询当前进程所属的系统账号的信息。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.GET\_LOCAL\_ACCOUNTS10+，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OsAccountInfo](js-apis-osaccount.md#osaccountinfo)> | Promise对象，返回当前进程所属的系统账号信息。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
6. console.info('getCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
7. }).catch((err: BusinessError) => {
8. console.error(`getCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getOsAccountType9+

PhonePC/2in1TabletTVWearable

getOsAccountType(callback: AsyncCallback<OsAccountType>): void

查询当前进程所属的系统账号的账号类型。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OsAccountType](js-apis-osaccount.md#osaccounttype)> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号的账号类型；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountType((err: BusinessError, accountType: osAccount.OsAccountType) => {
6. if (err) {
7. console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountType accountType: ' + accountType);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getOsAccountType9+

PhonePC/2in1TabletTVWearable

getOsAccountType(): Promise<OsAccountType>

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OsAccountType](js-apis-osaccount.md#osaccounttype)> | Promise对象，返回当前进程所属的系统账号的账号类型。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountType().then((accountType: osAccount.OsAccountType) => {
6. console.info('getOsAccountType, accountType: ' + accountType);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### queryDistributedVirtualDeviceId9+

PhonePC/2in1TabletTVWearable

queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

获取分布式虚拟设备ID。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。如果获取成功，err为null，data为分布式虚拟设备ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.queryDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
6. if (err) {
7. console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('queryDistributedVirtualDeviceId virtualID: ' + virtualID);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### queryDistributedVirtualDeviceId9+

PhonePC/2in1TabletTVWearable

queryDistributedVirtualDeviceId(): Promise<string>

获取分布式虚拟设备ID。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回分布式虚拟设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.queryDistributedVirtualDeviceId().then((virtualID: string) => {
6. console.info('queryDistributedVirtualDeviceId, virtualID: ' + virtualID);
7. }).catch((err: BusinessError) => {
8. console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getOsAccountLocalIdForSerialNumber9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果成功，err为null，data为与SN码关联的系统账号的账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**示例：** 查询与SN码12345关联的系统账号的ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let serialNumber: number = 12345;
5. try {
6. accountManager.getOsAccountLocalIdForSerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
7. if (err) {
8. console.error(`get localId code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`get localId exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### getOsAccountLocalIdForSerialNumber9+

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与SN码关联的系统账号的账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**示例：** 查询与SN码12345关联的系统账号的ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let serialNumber: number = 12345;
5. try {
6. accountManager.getOsAccountLocalIdForSerialNumber(serialNumber).then((localId: number) => {
7. console.info('getOsAccountLocalIdForSerialNumber localId: ' + localId);
8. }).catch((err: BusinessError) => {
9. console.error(`getOsAccountLocalIdForSerialNumber err: code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getOsAccountLocalIdForSerialNumber exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getSerialNumberForOsAccountLocalId9+

PhonePC/2in1TabletTVWearable

getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为与该系统账号关联的SN码；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号关联的SN码

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.getSerialNumberForOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
7. if (err) {
8. console.error(`get serialNumber code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`get serialNumber exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### getSerialNumberForOsAccountLocalId9+

PhonePC/2in1TabletTVWearable

getSerialNumberForOsAccountLocalId(localId: number): Promise<number>

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与该系统账号关联的SN码。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号关联的SN码

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. try {
6. accountManager.getSerialNumberForOsAccountLocalId(localId).then((serialNumber: number) => {
7. console.info('getSerialNumberForOsAccountLocalId serialNumber: ' + serialNumber);
8. }).catch((err: BusinessError) => {
9. console.error(`getSerialNumberForOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getSerialNumberForOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### isMultiOsAccountEnable(deprecated)

PhonePC/2in1TabletTVWearable

isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void

判断是否支持多系统账号。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkMultiOsAccountEnabled](js-apis-osaccount.md#checkmultiosaccountenabled9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持多系统账号；返回false表示不支持。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isMultiOsAccountEnable((err: BusinessError, isEnabled: boolean) => {
5. if (err) {
6. console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
9. }
10. });
```

### isMultiOsAccountEnable(deprecated)

PhonePC/2in1TabletTVWearable

isMultiOsAccountEnable(): Promise<boolean>

判断是否支持多系统账号。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkMultiOsAccountEnabled](js-apis-osaccount.md#checkmultiosaccountenabled9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持多系统账号；返回false表示不支持。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isMultiOsAccountEnable().then((isEnabled: boolean) => {
5. console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
6. }).catch((err: BusinessError) => {
7. console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
8. });
```

### isOsAccountActived(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void

判断指定系统账号是否处于激活状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示账号已激活；返回false表示账号未激活。 |

**示例：** 判断ID为100的系统账号是否处于激活状态

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.isOsAccountActived(localId, (err: BusinessError, isActived: boolean) => {
6. if (err) {
7. console.error(`isOsAccountActived failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('isOsAccountActived successfully, isActived:' + isActived);
10. }
11. });
```

### isOsAccountActived(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountActived(localId: number): Promise<boolean>

判断指定系统账号是否处于激活状态。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示账号已激活；返回false表示账号未激活。 |

**示例：** 判断ID为100的系统账号是否处于激活状态

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.isOsAccountActived(localId).then((isActived: boolean) => {
6. console.info('isOsAccountActived successfully, isActived: ' + isActived);
7. }).catch((err: BusinessError) => {
8. console.error(`isOsAccountActived failed, code is ${err.code}, message is ${err.message}`);
9. });
```

### isOsAccountConstraintEnable(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

判断指定系统账号是否具有指定约束。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的[约束](js-apis-osaccount.md#系统账号约束列表)名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. let constraint: string = 'constraint.wifi';
6. accountManager.isOsAccountConstraintEnable(localId, constraint, (err: BusinessError, isEnabled: boolean) => {
7. if (err) {
8. console.error(`isOsAccountConstraintEnable failed, code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
11. }
12. });
```

### isOsAccountConstraintEnable(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>

判断指定系统账号是否具有指定约束。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的[约束](js-apis-osaccount.md#系统账号约束列表)名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. let constraint: string = 'constraint.wifi';
6. accountManager.isOsAccountConstraintEnable(localId, constraint).then((isEnabled: boolean) => {
7. console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
8. }).catch((err: BusinessError) => {
9. console.error(`isOsAccountConstraintEnable err: code is ${err.code}, message is ${err.message}`);
10. });
```

### isTestOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

isTestOsAccount(callback: AsyncCallback<boolean>): void

检查当前系统账号是否为测试账号。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountTestable](js-apis-osaccount.md#checkosaccounttestable9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isTestOsAccount((err: BusinessError, isTestable: boolean) => {
5. if (err) {
6. console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
9. }
10. });
```

### isTestOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

isTestOsAccount(): Promise<boolean>

检查当前系统账号是否为测试账号。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountTestable](js-apis-osaccount.md#checkosaccounttestable9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isTestOsAccount().then((isTestable: boolean) => {
5. console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
6. }).catch((err: BusinessError) => {
7. console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
8. });
```

### isOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountVerified(callback: AsyncCallback<boolean>): void

检查当前系统账号是否已验证。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountVerified](js-apis-osaccount.md#checkosaccountverifieddeprecated)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isOsAccountVerified((err: BusinessError, isVerified: boolean) => {
5. if (err) {
6. console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
9. }
10. });
```

### isOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

检查指定系统账号是否已验证。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.isOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
6. if (err) {
7. console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
10. }
11. });
```

### isOsAccountVerified(deprecated)

PhonePC/2in1TabletTVWearable

isOsAccountVerified(localId?: number): Promise<boolean>

检查指定系统账号是否已验证。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 否 | 系统账号ID。不填则检查当前系统账号是否已验证，默认为-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.isOsAccountVerified().then((isVerified: boolean) => {
5. console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
6. }).catch((err: BusinessError) => {
7. console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
8. });
```

### getCreatedOsAccountsCount(deprecated)

PhonePC/2in1TabletTVWearable

getCreatedOsAccountsCount(callback: AsyncCallback<number>): void

获取已创建的系统账号数量。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountCount](js-apis-osaccount.md#getosaccountcount9)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为已创建的系统账号的数量；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getCreatedOsAccountsCount((err: BusinessError, count: number)=>{
5. if (err) {
6. console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getCreatedOsAccountsCount successfully, count: ' + count);
9. }
10. });
```

### getCreatedOsAccountsCount(deprecated)

PhonePC/2in1TabletTVWearable

getCreatedOsAccountsCount(): Promise<number>

获取已创建的系统账号数量。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountCount](js-apis-osaccount.md#getosaccountcount9-1)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已创建的系统账号的数量。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getCreatedOsAccountsCount().then((count: number) => {
5. console.info('getCreatedOsAccountsCount successfully, count: ' + count);
6. }).catch((err: BusinessError) => {
7. console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
8. });
```

### getOsAccountLocalIdFromProcess(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void

获取当前进程所属的系统账号ID。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为当前进程所属的系统账号ID；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getOsAccountLocalIdFromProcess((err: BusinessError, localId: number) => {
5. if (err) {
6. console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getOsAccountLocalIdFromProcess id:: ' + localId);
9. }
10. });
```

### getOsAccountLocalIdFromProcess(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromProcess(): Promise<number>

获取当前进程所属的系统账号ID。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前进程所属的系统账号ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getOsAccountLocalIdFromProcess().then((localId: number) => {
5. console.info('getOsAccountLocalIdFromProcess successfully, localId: ' + localId);
6. }).catch((err: BusinessError) => {
7. console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
8. });
```

### getOsAccountLocalIdFromUid(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void

根据uid查询对应的系统账号ID。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForUid](js-apis-osaccount.md#getosaccountlocalidforuid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为对应的系统账号ID；否则为错误对象。 |

**示例：** 查询值为12345678的uid所属的系统账号ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let uid: number = 12345678;
5. accountManager.getOsAccountLocalIdFromUid(uid, (err: BusinessError, localId: number) => {
6. if (err) {
7. console.error(`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
10. }
11. });
```

### getOsAccountLocalIdFromUid(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromUid(uid: number): Promise<number>

根据uid查询对应的系统账号ID。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForUid](js-apis-osaccount.md#getosaccountlocalidforuid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回uid对应的系统账号ID。 |

**示例：** 查询值为12345678的uid所属的系统账号ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let uid: number = 12345678;
5. accountManager.getOsAccountLocalIdFromUid(uid).then((localId: number) => {
6. console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}`);
9. });
```

### getOsAccountLocalIdFromDomain(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

根据域账号信息，获取与其关联的系统账号的账号ID。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForDomain](js-apis-osaccount.md#getosaccountlocalidfordomain9)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 域账号信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数，如果获取成功，err为null，data为域账号关联的系统账号ID；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
4. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
5. accountManager.getOsAccountLocalIdFromDomain(domainInfo, (err: BusinessError, localId: number) => {
6. if (err) {
7. console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
10. }
11. });
```

### getOsAccountLocalIdFromDomain(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForDomain](js-apis-osaccount.md#getosaccountlocalidfordomain9-1)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回域账号关联的系统账号ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
5. accountManager.getOsAccountLocalIdFromDomain(domainInfo).then((localId: number) => {
6. console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
9. });
```

### getOsAccountAllConstraints(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

获取指定系统账号的全部约束。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。如果获取成功，err为null，data为指定系统账号的全部[约束](js-apis-osaccount.md#系统账号约束列表)；否则为错误对象。 |

**示例：** 获取ID为100的系统账号的全部约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.getOsAccountAllConstraints(localId, (err: BusinessError, constraints: string[])=>{
6. if (err) {
7. console.error(`getOsAccountAllConstraints code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getOsAccountAllConstraints:' + JSON.stringify(constraints));
10. }
11. });
```

### getOsAccountAllConstraints(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountAllConstraints(localId: number): Promise<Array<string>>

获取指定系统账号的全部约束。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回指定系统账号的全部[约束](js-apis-osaccount.md#系统账号约束列表)。 |

**示例：** 获取ID为100的系统账号的全部约束

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.getOsAccountAllConstraints(localId).then((constraints: string[]) => {
6. console.info('getOsAccountAllConstraints, constraints: ' + constraints);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountAllConstraints err: code is ${err.code}, message is ${err.message}`);
9. });
```

### queryActivatedOsAccountIds(deprecated)

PhonePC/2in1TabletTVWearable

queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getActivatedOsAccountLocalIds](js-apis-osaccount.md#getactivatedosaccountlocalids9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。如果查询成功，err为null，data为当前处于激活状态的系统账号的ID列表；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.queryActivatedOsAccountIds((err: BusinessError, idArray: number[]) => {
5. if (err) {
6. console.error(`queryActivatedOsAccountIds code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('queryActivatedOsAccountIds idArray length:' + idArray.length);
9. for (let i = 0; i < idArray.length; i++) {
10. console.info('activated os account id: ' + idArray[i]);
11. }
12. }
13. });
```

### queryActivatedOsAccountIds(deprecated)

PhonePC/2in1TabletTVWearable

queryActivatedOsAccountIds(): Promise<Array<number>>

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getActivatedOsAccountLocalIds](js-apis-osaccount.md#getactivatedosaccountlocalids9-1)替代。

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回当前处于激活状态的系统账号的ID列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.queryActivatedOsAccountIds().then((idArray: number[]) => {
5. console.info('queryActivatedOsAccountIds, idArray: ' + idArray);
6. }).catch((err: BusinessError) => {
7. console.error(`queryActivatedOsAccountIds err: code is ${err.code}, message is ${err.message}`);
8. });
```

### queryCurrentOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

查询当前进程所属的系统账号的信息。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OsAccountInfo](js-apis-osaccount.md#osaccountinfo)> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.queryCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
5. if (err) {
6. console.error(`queryCurrentOsAccount code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('queryCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
9. }
10. });
```

### queryCurrentOsAccount(deprecated)

PhonePC/2in1TabletTVWearable

queryCurrentOsAccount(): Promise<OsAccountInfo>

查询当前进程所属的系统账号的信息。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OsAccountInfo](js-apis-osaccount.md#osaccountinfo)> | Promise对象，返回当前进程所属的系统账号信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.queryCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
5. console.info('queryCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
6. }).catch((err: BusinessError) => {
7. console.error(`queryCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getOsAccountTypeFromProcess(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void

查询当前进程所属的系统账号的账号类型。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OsAccountType](js-apis-osaccount.md#osaccounttype)> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号的账号类型；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getOsAccountTypeFromProcess((err: BusinessError, accountType: osAccount.OsAccountType) => {
5. if (err) {
6. console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getOsAccountTypeFromProcess accountType: ' + accountType);
9. }
10. });
```

### getOsAccountTypeFromProcess(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountTypeFromProcess(): Promise<OsAccountType>

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OsAccountType](js-apis-osaccount.md#osaccounttype)> | Promise对象，返回当前进程所属的系统账号的账号类型。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getOsAccountTypeFromProcess().then((accountType: osAccount.OsAccountType) => {
5. console.info('getOsAccountTypeFromProcess, accountType: ' + accountType);
6. }).catch((err: BusinessError) => {
7. console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getDistributedVirtualDeviceId(deprecated)

PhonePC/2in1TabletTVWearable

getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

获取分布式虚拟设备ID。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[queryDistributedVirtualDeviceId](js-apis-osaccount.md#querydistributedvirtualdeviceid9)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。如果获取成功，err为null，data为分布式虚拟设备ID；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
5. if (err) {
6. console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getDistributedVirtualDeviceId virtualID: ' + virtualID);
9. }
10. });
```

### getDistributedVirtualDeviceId(deprecated)

PhonePC/2in1TabletTVWearable

getDistributedVirtualDeviceId(): Promise<string>

获取分布式虚拟设备ID。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[queryDistributedVirtualDeviceId](js-apis-osaccount.md#querydistributedvirtualdeviceid9-1)替代。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回分布式虚拟设备ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. accountManager.getDistributedVirtualDeviceId().then((virtualID: string) => {
5. console.info('getDistributedVirtualDeviceId, virtualID: ' + virtualID);
6. }).catch((err: BusinessError) => {
7. console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getOsAccountLocalIdBySerialNumber(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForSerialNumber](js-apis-osaccount.md#getosaccountlocalidforserialnumber9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为与SN码关联的系统账号的账号ID；否则为错误对象。 |

**示例：** 查询与SN码12345关联的系统账号的ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let serialNumber: number = 12345;
5. accountManager.getOsAccountLocalIdBySerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
6. if (err) {
7. console.error(`get localId code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
10. }
11. });
```

### getOsAccountLocalIdBySerialNumber(deprecated)

PhonePC/2in1TabletTVWearable

getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForSerialNumber](js-apis-osaccount.md#getosaccountlocalidforserialnumber9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与SN码关联的系统账号的账号ID。 |

**示例：** 查询与SN码12345关联的系统账号的ID

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let serialNumber: number = 12345;
5. accountManager.getOsAccountLocalIdBySerialNumber(serialNumber).then((localId: number) => {
6. console.info('getOsAccountLocalIdBySerialNumber localId: ' + localId);
7. }).catch((err: BusinessError) => {
8. console.error(`getOsAccountLocalIdBySerialNumber err: code is ${err.code}, message is ${err.message}`);
9. });
```

### getSerialNumberByOsAccountLocalId(deprecated)

PhonePC/2in1TabletTVWearable

getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getSerialNumberForOsAccountLocalId](js-apis-osaccount.md#getserialnumberforosaccountlocalid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为与该系统账号关联的SN码；否则为错误对象。 |

**示例：** 获取ID为100的系统账号关联的SN码

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.getSerialNumberByOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
6. if (err) {
7. console.error(`get serialNumber code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
10. }
11. });
```

### getSerialNumberByOsAccountLocalId(deprecated)

PhonePC/2in1TabletTVWearable

getSerialNumberByOsAccountLocalId(localId: number): Promise<number>

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getSerialNumberForOsAccountLocalId](js-apis-osaccount.md#getserialnumberforosaccountlocalid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与该系统账号关联的SN码。 |

**示例：** 获取ID为100的系统账号关联的SN码

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.getSerialNumberByOsAccountLocalId(localId).then((serialNumber: number) => {
6. console.info('getSerialNumberByOsAccountLocalId serialNumber: ' + serialNumber);
7. }).catch((err: BusinessError) => {
8. console.error(`getSerialNumberByOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
9. });
```

### getOsAccountName12+

PhonePC/2in1TabletTVWearable

getOsAccountName(): Promise<string>

查询调用方所属系统账号的名称。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回调用方所属系统账号的名称。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getOsAccountName().then((name: string) => {
6. console.info('getOsAccountName, name: ' + name);
7. }).catch((err: BusinessError) => {
8. console.error('getOsAccountName err: ' + err);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getOsAccountName exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getForegroundOsAccountLocalId15+

PhonePC/2in1TabletTVWearable

getForegroundOsAccountLocalId(): Promise<number>

获取前台系统账号的ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回前台系统账号的ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. try {
5. accountManager.getForegroundOsAccountLocalId().then((localId: number) => {
6. console.info('getForegroundOsAccountLocalId, localId: ' + localId);
7. }).catch((err: BusinessError) => {
8. console.error(`getForegroundOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getForegroundOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getOsAccountDomainInfo15+

PhonePC/2in1TabletTVWearable

getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>

获取指定系统账号关联的域账号信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_DOMAIN\_ACCOUNTS 和 ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，以上权限允许系统应用和企业应用进行申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8)> | Promise对象。返回与指定系统账号关联的域账号信息。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300003 | OS account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
4. let localId: number = 100;
5. accountManager.getOsAccountDomainInfo(localId).then((domainAccountInfo: osAccount.DomainAccountInfo) => {
6. if (domainAccountInfo === null) {
7. console.info('The target OS account is not a domain account.')
8. } else {
9. console.info('getOsAccountDomainInfo domain: ' + domainAccountInfo.domain);
10. console.info('getOsAccountDomainInfo accountName: ' + domainAccountInfo.accountName);
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`getOsAccountDomainInfo err: code is ${err.code}, message is ${err.message}`);
14. })
```

## DomainAccountManager18+

PhonePC/2in1TabletTVWearable

域账号管理类。

### updateAccountInfo18+

PhonePC/2in1TabletTVWearable

updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>

修改指定域账号信息。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS或ohos.permission.MANAGE\_DOMAIN\_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldAccountInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 表示旧域账号信息。 |
| newAccountInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 表示新域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | The new account info is invalid. |
| 12300003 | The old account not found. |
| 12300004 | The new account already exists. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let oldDomainInfo: osAccount.DomainAccountInfo =
4. {domain: 'testDomain', accountName: 'oldtestAccountName'};
5. let newDomainInfo: osAccount.DomainAccountInfo =
6. {domain: 'testDomain', accountName: 'newtestAccountName'};
7. try {
8. osAccount.DomainAccountManager.updateAccountInfo(oldDomainInfo, newDomainInfo).then(() => {
9. console.info('updateAccountInfo, success');
10. }).catch((err: BusinessError) => {
11. console.error('updateAccountInfo err: ' + err);
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`updateAccountInfo exception: code is ${err.code}, message is ${err.message}`);
16. }
```

## OsAccountInfo

PhonePC/2in1TabletTVWearable

表示系统账号信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localId | number | 否 | 否 | 系统账号ID。 |
| localName | string | 否 | 否 | 系统账号名称。 |
| type | [OsAccountType](js-apis-osaccount.md#osaccounttype) | 否 | 否 | 系统账号类型。 |
| constraints | Array<string> | 否 | 否 | 系统账号[约束](js-apis-osaccount.md#系统账号约束列表)，默认为空。 |
| isVerified(deprecated) | boolean | 否 | 否 | 账号是否验证。true表示指定账号已验证；false表示指定账号未验证。  \*\*说明：\*\*从API version 7开始支持，从API version 11开始废弃，建议使用isUnlocked。 |
| isUnlocked11+ | boolean | 否 | 否 | 账号是否已解锁（EL2级别目录是否解密）。true表示指定账号已解锁；false表示指定账号未解锁。 |
| photo8+ | string | 否 | 否 | 系统账号头像，默认为空。 |
| createTime8+ | number | 否 | 否 | 系统账号创建时间。 |
| lastLoginTime8+ | number | 否 | 否 | 系统账号最后一次登录时间，默认为空。 |
| serialNumber8+ | number | 否 | 否 | 系统账号SN码。 |
| isActived(deprecated) | boolean | 否 | 否 | 系统账号激活状态。true表示指定账号处于激活状态；false表示指定账号处于未激活状态。  \*\*说明：\*\*从API version 7开始支持，从API version 11开始废弃，建议使用isActivated。 |
| isActivated11+ | boolean | 否 | 否 | 系统账号是否激活。true表示指定账号已激活；false表示指定账号未激活。 |
| isCreateCompleted8+ | boolean | 否 | 否 | 系统账号创建是否完整。true表示指定账号已创建完整；false表示指定账号未创建完整。 |
| distributedInfo | [distributedAccount.DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 否 | 否 | 分布式账号信息，默认为空。 |
| domainInfo8+ | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 否 | 否 | 域账号信息，默认为空。 |

## DomainAccountInfo8+

PhonePC/2in1TabletTVWearable

表示域账号信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| domain | string | 否 | 否 | 域名。 |
| accountName | string | 否 | 否 | 域账号名。 |
| serverConfigId18+ | string | 否 | 是 | 域账号配置ID，默认为空字符串。 |

## DomainServerConfig18+

PhonePC/2in1TabletTVWearable

域服务器配置。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parameters | Record<string, Object> | 否 | 否 | 服务器配置参数。 |
| id | string | 否 | 否 | 服务器配置标识。 |
| domain | string | 否 | 否 | 服务器所属的域。 |

## DomainServerConfigManager18+

PhonePC/2in1TabletTVWearable

域服务器配置管理类。

### addServerConfig18+

PhonePC/2in1TabletTVWearable

static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>

添加域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameters | Record<string, Object> | 是 | 表示域服务器配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DomainServerConfig](js-apis-osaccount.md#domainserverconfig18)> | Promise对象，返回新添加的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300213 | Server config already exists. |
| 12300215 | The number of server config reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let configParams: Record<string, Object> = {
4. 'uri': 'test.example.com',
5. 'port': 100
6. };
7. osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('add server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
10. }).catch((err: BusinessError) => {
11. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
12. });
```

### removeServerConfig18+

PhonePC/2in1TabletTVWearable

static removeServerConfig(configId: string): Promise<void>

删除域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |
| 12300214 | Server config has been associated with an account. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let configParams: Record<string, Object> = {
4. 'uri': 'test.example.com',
5. 'port': 100
6. };
7. osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
10. osAccount.DomainServerConfigManager.removeServerConfig(serverConfig.id);
11. console.info('remove domain server configuration successfully');
12. }).catch((err: BusinessError) => {
13. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
14. });
```

### updateServerConfig18+

PhonePC/2in1TabletTVWearable

static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>

更新域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |
| parameters | Record<string, Object> | 是 | 表示域服务器配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DomainServerConfig](js-apis-osaccount.md#domainserverconfig18)> | Promise对象，返回更新后的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300212 | Server config not found. |
| 12300213 | Server config already exists. |
| 12300214 | Server config has been associated with an account. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let configParams: Record<string, Object> = {
4. 'uri': 'test.example.com',
5. 'port': 100
6. };
7. osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
10. osAccount.DomainServerConfigManager.updateServerConfig(serverConfig.id, configParams).then((data) => {
11. console.info('update domain server configuration successfully, return config: ' + JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. console.error(`update domain server configuration failed, code is ${err.code}, message is ${err.message}`);
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
17. });
```

### getServerConfig18+

PhonePC/2in1TabletTVWearable

static getServerConfig(configId: string): Promise<DomainServerConfig>

获取域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DomainServerConfig](js-apis-osaccount.md#domainserverconfig18)> | Promise对象，返回获取的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let configParams: Record<string, Object> = {
4. 'uri': 'test.example.com',
5. 'port': 100
6. };
7. osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
10. osAccount.DomainServerConfigManager.getServerConfig(serverConfig.id).then((data: osAccount.DomainServerConfig) => {
11. console.info('get domain server configuration successfully, return config: ' + JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. console.error(`get domain server configuration failed, code is ${err.code}, message is ${err.message}`);
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
17. });
```

### getAllServerConfigs18+

PhonePC/2in1TabletTVWearable

static getAllServerConfigs(): Promise<Array<DomainServerConfig>>

获取所有域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[DomainServerConfig](js-apis-osaccount.md#domainserverconfig18)>> | Promise对象，返回获取的所有域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let configParams: Record<string, Object> = {
4. 'uri': 'test.example.com',
5. 'port': 100
6. };
7. osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
10. osAccount.DomainServerConfigManager.getAllServerConfigs().then((data: Array<osAccount.DomainServerConfig>) => {
11. console.info('get all domain server configuration successfully, return config: ' + JSON.stringify(data));
12. }).catch((err: BusinessError) => {
13. console.error(`get all domain server configuration failed, code is ${err.code}, message is ${err.message}`);
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
17. });
```

### getAccountServerConfig18+

PhonePC/2in1TabletTVWearable

static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>

获取目标域账号的服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](js-apis-osaccount.md#domainaccountinfo8) | 是 | 表示目标域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DomainServerConfig](js-apis-osaccount.md#domainserverconfig18)> | Promise对象，返回目标账号的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300003 | Domain account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let accountInfo: osAccount.DomainAccountInfo = {
4. 'accountName': 'demoName',
5. 'domain': 'demoDomain'
6. };
7. osAccount.DomainServerConfigManager.getAccountServerConfig(accountInfo).then((
8. serverConfig: osAccount.DomainServerConfig) => {
9. console.info('get account server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
10. }).catch((err: BusinessError) => {
11. console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
12. });
```

## 系统账号约束列表

PhonePC/2in1TabletTVWearable

| 约束 | 说明 |
| --- | --- |
| constraint.wifi | 禁止使用Wi-Fi |
| constraint.wifi.set | 禁止配置Wi-Fi |
| constraint.locale.set | 禁止配置设备语言 |
| constraint.app.accounts | 禁止添加和删除应用账号 |
| constraint.apps.install | 禁止安装应用 |
| constraint.apps.uninstall | 禁止卸载应用 |
| constraint.location.shared | 禁止打开位置共享 |
| constraint.unknown.sources.install | 禁止安装未知来源的应用 |
| constraint.global.unknown.app.install | 禁止所有用户安装未知来源的应用 |
| constraint.bluetooth.set | 禁止配置蓝牙 |
| constraint.bluetooth | 禁止使用蓝牙 |
| constraint.bluetooth.share | 禁止共享使用蓝牙 |
| constraint.usb.file.transfer | 禁止通过USB传输文件 |
| constraint.credentials.set | 禁止配置用户凭据 |
| constraint.os.account.remove | 禁止删除用户 |
| constraint.managed.profile.remove | 禁止删除此用户的托管配置文件 |
| constraint.debug.features.use | 禁止启用或访问调试功能 |
| constraint.vpn.set | 禁止配置VPN |
| constraint.date.time.set | 禁止配置日期时间和时区 |
| constraint.tethering.config | 禁止配置Tethering |
| constraint.network.reset | 禁止重置网络设置 |
| constraint.factory.reset | 禁止出厂设置 |
| constraint.os.account.create | 禁止创建新用户 |
| constraint.add.managed.profile | 禁止添加托管配置文件 |
| constraint.apps.verify.disable | 强制应用程序验证 |
| constraint.cell.broadcasts.set | 禁止配置小区广播 |
| constraint.mobile.networks.set | 禁止配置移动网络 |
| constraint.control.apps | 禁止在设置或启动模块中修改应用程序 |
| constraint.physical.media | 禁止装载物理外部介质 |
| constraint.microphone | 禁止使用麦克风 |
| constraint.microphone.unmute | 禁止取消麦克风静音 |
| constraint.volume.adjust | 禁止调整音量 |
| constraint.calls.outgoing | 禁止拨打外呼电话 |
| constraint.sms.use | 禁止发送或接收短信 |
| constraint.fun | 禁止享受乐趣 |
| constraint.windows.create | 禁止创建应用程序窗口以外的窗口 |
| constraint.system.error.dialogs | 禁止显示崩溃或无响应应用程序的系统错误对话框 |
| constraint.cross.profile.copy.paste | 禁止通过将数据粘贴到其他用户或配置文件来导出剪贴板内容 |
| constraint.beam.outgoing | 禁止使用NFC从应用程序传送数据 |
| constraint.wallpaper | 禁止管理壁纸 |
| constraint.safe.boot | 禁止进入安全引导模式 |
| constraint.parent.profile.app.linking | 禁止父配置文件中的应用程序处理来自托管配置文件的Web链接 |
| constraint.audio.record | 禁止录制音频 |
| constraint.camera.use | 禁止使用摄像机 |
| constraint.os.account.background.run | 禁止在后台运行 |
| constraint.data.roam | 禁止漫游通话时使用蜂窝数据 |
| constraint.os.account.set.icon | 禁止修改用户头像 |
| constraint.wallpaper.set | 禁止设置壁纸 |
| constraint.oem.unlock | 禁止启用oem解锁 |
| constraint.device.unmute | 禁止取消设备静音 |
| constraint.password.unified | 禁止托管配置文件与主用户进行统一锁屏质询 |
| constraint.autofill | 禁止使用自动填充服务 |
| constraint.content.capture | 禁止捕获用户屏幕 |
| constraint.content.suggestions | 禁止接收内容建议 |
| constraint.os.account.activate | 禁止前台启动用户 |
| constraint.location.set | 禁止配置位置服务 |
| constraint.airplane.mode.set | 禁止飞行模式 |
| constraint.brightness.set | 禁止配置亮度 |
| constraint.share.into.profile | 禁止将主要用户的文件/图片/数据共享到托管配置文件中 |
| constraint.ambient.display | 禁止显示环境 |
| constraint.screen.timeout.set | 禁止配置屏幕关闭的超时 |
| constraint.print | 禁止打印 |
| constraint.private.dns.set | 禁止配置专用DNS |
