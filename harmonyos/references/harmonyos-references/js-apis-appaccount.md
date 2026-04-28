---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appaccount
title: @ohos.account.appAccount (应用账号管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 账号管理 > @ohos.account.appAccount (应用账号管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:26+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:375b6c14b72a09af12180d60f077575cd428798f0eb22f9abbe82e11002542ce
---

本模块提供应用账号信息的添加、删除、修改和查询基础能力，并支持应用间鉴权和分布式数据同步功能。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appAccount } from '@kit.BasicServicesKit';
```

## appAccount.createAppAccountManager

PhonePC/2in1TabletTVWearable

createAppAccountManager(): AppAccountManager

创建应用账号管理器对象。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AppAccountManager](js-apis-appaccount.md#appaccountmanager) | 应用账号管理器对象。 |

**示例：**

```
1. let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
```

## AppAccountManager

PhonePC/2in1TabletTVWearable

应用账号管理器，可用于管理应用自身的账号信息。

### createAccount9+

PhonePC/2in1TabletTVWearable

createAccount(name: string, callback: AsyncCallback<void>): void

根据账号名创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.createAccount('WangWu', (err: BusinessError) => {
5. if (err) {
6. console.error(`createAccount code: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('createAccount successful.');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`createAccount err: code is ${err.code}, message is ${err.message}`);
14. }
```

### createAccount9+

PhonePC/2in1TabletTVWearable

createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void

根据账号名和可选项创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| options | [CreateAccountOptions](js-apis-appaccount.md#createaccountoptions9) | 是 | 创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or options. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: appAccount.CreateAccountOptions = {
4. customData: {
5. age: '10'
6. }
7. }
8. try {
9. appAccountManager.createAccount('LiSi', options, (err: BusinessError) => {
10. if (err) {
11. console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
12. } else {
13. console.info('createAccount successfully');
14. }
15. });
16. } catch (e) {
17. const err = e as BusinessError;
18. console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
19. }
```

### createAccount9+

PhonePC/2in1TabletTVWearable

createAccount(name: string, options?: CreateAccountOptions): Promise<void>

根据账号名和可选项创建应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| options | [CreateAccountOptions](js-apis-appaccount.md#createaccountoptions9) | 否 | 创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。不填无影响，默认为空，表示创建的该账号无额外信息需要添加。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or options. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: appAccount.CreateAccountOptions = {
4. customData: {
5. age: '10'
6. }
7. }
8. try {
9. appAccountManager.createAccount('LiSi', options).then(() => {
10. console.info('createAccount successfully');
11. }).catch((err: BusinessError) => {
12. console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
13. });
14. } catch (e) {
15. const err = e as BusinessError;
16. console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
17. }
```

### createAccountImplicitly9+

PhonePC/2in1TabletTVWearable

createAccountImplicitly(owner: string, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调对象，返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300007 | The number of accounts reaches the upper limit. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, result?: appAccount.AuthResult): void {
10. console.info('resultCode: ' + code);
11. console.info('result: ' + JSON.stringify(result));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. try {
30. appAccountManager.createAccountImplicitly('com.example.accountjsdemo', {
31. onResult: this.onResultCallback,
32. onRequestRedirected: this.onRequestRedirectedCallback
33. });
34. } catch (e) {
35. const err = e as BusinessError;
36. console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
37. }
38. }
39. build() {}
40. }
```

### createAccountImplicitly9+

PhonePC/2in1TabletTVWearable

createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者和可选项隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| options | [CreateAccountImplicitlyOptions](js-apis-appaccount.md#createaccountimplicitlyoptions9) | 是 | 隐式创建账号的选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调对象，返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner or options. |
| 12300007 | The number of accounts reaches the upper limit. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, result?: appAccount.AuthResult): void {
10. console.info('resultCode: ' + code);
11. console.info('result: ' + JSON.stringify(result));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. let options: appAccount.CreateAccountImplicitlyOptions = {
30. authType: 'getSocialData',
31. requiredLabels: ['student']
32. };
33. try {
34. appAccountManager.createAccountImplicitly('com.example.accountjsdemo', options, {
35. onResult: this.onResultCallback,
36. onRequestRedirected: this.onRequestRedirectedCallback
37. });
38. } catch (e) {
39. const err = e as BusinessError;
40. console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
41. }
42. }
43. build() {}
44. }
```

### removeAccount9+

PhonePC/2in1TabletTVWearable

removeAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.removeAccount('ZhaoLiu', (err: BusinessError) => {
5. if (err) {
6. console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('removeAccount successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### removeAccount9+

PhonePC/2in1TabletTVWearable

removeAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.removeAccount('Lisi').then(() => {
5. console.info('removeAccount successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### setAppAccess9+

PhonePC/2in1TabletTVWearable

setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void

设置指定应用对特定账号的访问权限。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| isAccessible | boolean | 是 | 是否可访问。true表示允许访问，false表示禁止访问。 |
| callback | AsyncCallback<void> | 是 | 回调函数，如果设置成功，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true, (err: BusinessError) => {
5. if (err) {
6. console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('setAppAccess successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### setAppAccess9+

PhonePC/2in1TabletTVWearable

setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>

设置指定应用对特定账号的数据访问权限。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| isAccessible | boolean | 是 | 是否可访问。true表示允许访问，false表示禁止访问。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true).then(() => {
5. console.info('setAppAccess successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### checkAppAccess9+

PhonePC/2in1TabletTVWearable

checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用对特定账号的数据是否可访问。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo',
5. (err: BusinessError, isAccessible: boolean) => {
6. if (err) {
7. console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('checkAppAccess successfully');
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### checkAppAccess9+

PhonePC/2in1TabletTVWearable

checkAppAccess(name: string, bundleName: string): Promise<boolean>

检查指定应用对特定账号的数据是否可访问。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo').then((isAccessible: boolean) => {
5. console.info('checkAppAccess successfully, isAccessible: ' + isAccessible);
6. }).catch((err: BusinessError) => {
7. console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### setDataSyncEnabled9+

PhonePC/2in1TabletTVWearable

setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| isEnabled | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当开启或禁止成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setDataSyncEnabled('ZhangSan', true, (err: BusinessError) => {
5. console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
6. });
7. } catch (e) {
8. const err = e as BusinessError;
9. console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
10. }
```

### setDataSyncEnabled9+

PhonePC/2in1TabletTVWearable

setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| isEnabled | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setDataSyncEnabled('ZhangSan', true).then(() => {
5. console.info('setDataSyncEnabled Success');
6. }).catch((err: BusinessError) => {
7. console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
12. }
```

### checkDataSyncEnabled9+

PhonePC/2in1TabletTVWearable

checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkDataSyncEnabled('ZhangSan', (err: BusinessError, isEnabled: boolean) => {
5. if (err) {
6. console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
14. }
```

### checkDataSyncEnabled9+

PhonePC/2in1TabletTVWearable

checkDataSyncEnabled(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkDataSyncEnabled('ZhangSan').then((isEnabled: boolean) => {
5. console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
6. }).catch((err: BusinessError) => {
7. console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
12. }
```

### setCredential9+

PhonePC/2in1TabletTVWearable

setCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当凭据设置成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, credentialType or credential. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx', (err: BusinessError) => {
5. if (err) {
6. console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('setCredential successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### setCredential9+

PhonePC/2in1TabletTVWearable

setCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, credentialType or credential. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx').then(() => {
5. console.info('setCredential successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### getCredential9+

PhonePC/2in1TabletTVWearable

getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getCredential('ZhangSan', 'PIN_SIX', (err: BusinessError, result: string) => {
5. if (err) {
6. console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getCredential successfully, result: ' + result);
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getCredential err: code is ${err.code}, message is ${err.message}`);
14. }
```

### getCredential9+

PhonePC/2in1TabletTVWearable

getCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回指定应用账号的凭据。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getCredential('ZhangSan', 'PIN_SIX').then((credential: string) => {
5. console.info('getCredential successfully, credential: ' + credential);
6. }).catch((err: BusinessError) => {
7. console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`getCredential exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### setCustomData9+

PhonePC/2in1TabletTVWearable

setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| value | string | 是 | 自定义数据的取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置自定义数据成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, key or value. |
| 12300003 | Account not found. |
| 12400003 | The number of custom data reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setCustomData('ZhangSan', 'age', '12', (err: BusinessError) => {
5. if (err) {
6. console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('setCustomData successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### setCustomData9+

PhonePC/2in1TabletTVWearable

setCustomData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| value | string | 是 | 自定义数据的取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, key or value. |
| 12300003 | Account not found. |
| 12400003 | The number of custom data reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setCustomData('ZhangSan', 'age', '12').then(() => {
5. console.info('setCustomData successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### getCustomData9+

PhonePC/2in1TabletTVWearable

getCustomData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为自定义数据的取值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getCustomData('ZhangSan', 'age', (err: BusinessError, data: string) => {
5. if (err) {
6. console.error('getCustomData failed, error: ' + err);
7. } else {
8. console.info('getCustomData successfully, data: ' + data);
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getCustomData9+

PhonePC/2in1TabletTVWearable

getCustomData(name: string, key: string): Promise<string>

根据指定键名获取特定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回自定义数据的取值。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getCustomData('ZhangSan', 'age').then((data: string) => {
5. console.info('getCustomData successfully, data: ' + data);
6. }).catch((err: BusinessError) => {
7. console.error(`getCustomData failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### getCustomDataSync9+

PhonePC/2in1TabletTVWearable

getCustomDataSync(name: string, key: string): string

根据指定键名获取特定应用账号的自定义数据。使用同步方式返回结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 自定义数据的取值。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value = appAccountManager.getCustomDataSync('ZhangSan', 'age');
5. console.info('getCustomDataSync successfully, value: ' + value);
6. } catch (e) {
7. const err = e as BusinessError;
8. console.error(`getCustomDataSync failed, code is ${err.code}, message is ${err.message}`);
9. }
```

### getAllAccounts9+

PhonePC/2in1TabletTVWearable

getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAllAccounts((err: BusinessError, data: appAccount.AppAccountInfo[]) => {
5. if (err) {
6. console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getAllAccounts successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getAllAccounts9+

PhonePC/2in1TabletTVWearable

getAllAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | Promise对象，返回全部应用已授权账号信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | System service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo[]) => {
5. console.info('getAllAccounts successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### getAccountsByOwner9+

PhonePC/2in1TabletTVWearable

getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 回调函数。如果获取成功，err为null，data为获取到的应用账号列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAccountsByOwner('com.example.accountjsdemo2',
5. (err: BusinessError, data: appAccount.AppAccountInfo[]) => {
6. if (err) {
7. console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getAccountsByOwner successfully, data:' + JSON.stringify(data));
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getAccountsByOwner exception:code is ${err.code}, message is ${err.message}`);
15. }
```

### getAccountsByOwner9+

PhonePC/2in1TabletTVWearable

getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | Promise对象，返回获取到的应用账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAccountsByOwner('com.example.accountjsdemo2').then((
5. data: appAccount.AppAccountInfo[]) => {
6. console.info('getAccountsByOwner successfully, data: ' + JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getAccountsByOwner exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### on('accountChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'accountChange' | 是 | 事件回调类型，支持的事件为'accountChange'，当目标应用更新账号信息时，触发该事件。 |
| owners | Array<string> | 是 | 应用账号所有者的包名列表。 |
| callback | Callback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 需要注册的回调函数，返回信息为发生变更的应用账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid type or owners. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
4. console.info('receive change data:' + JSON.stringify(data));
5. }

7. try {
8. appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
12. }
```

### off('accountChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'accountChange' | 是 | 事件回调类型，支持的事件为'accountChange'，当账号所有者更新账号信息时，触发该事件。 |
| callback | Callback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 否 | 需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
4. console.info('receive change data:' + JSON.stringify(data));
5. }

7. try {
8. appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
12. }
13. try {
14. appAccountManager.off('accountChange', changeOnCallback);
15. } catch (e) {
16. const err = e as BusinessError;
17. console.error(`off accountChange failed, code is ${err.code}, message is ${err.message}`);
18. }
```

### auth9+

PhonePC/2in1TabletTVWearable

auth(name: string, owner: string, authType: string, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调对象，返回鉴权结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
10. console.info('resultCode: ' + code);
11. console.info('authResult: ' + JSON.stringify(authResult));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. try {
30. appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', {
31. onResult: this.onResultCallback,
32. onRequestRedirected: this.onRequestRedirectedCallback
33. });
34. } catch (e) {
35. const err = e as BusinessError;
36. console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
37. }
38. }

40. build() {}
41. }
```

### auth9+

PhonePC/2in1TabletTVWearable

auth(name: string, owner: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| options | Record<string, Object> | 是 | 鉴权所需的可选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调对象，返回鉴权结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or options. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
10. console.info('resultCode: ' + code);
11. console.info('authResult: ' + JSON.stringify(authResult));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. let options: Record<string, Object> = {
30. 'password': 'xxxx',
31. };
32. try {
33. appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', options, {
34. onResult: this.onResultCallback,
35. onRequestRedirected: this.onRequestRedirectedCallback
36. });
37. } catch (e) {
38. const err = e as BusinessError;
39. console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
40. }
41. }

43. build() {}
44. }
```

### getAuthToken9+

PhonePC/2in1TabletTVWearable

getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
5. (err: BusinessError, token: string) => {
6. if (err) {
7. console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getAuthToken successfully, token: ' + token);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getAuthToken9+

PhonePC/2in1TabletTVWearable

getAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回授权令牌。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((token: string) => {
5. console.info('getAuthToken successfully, token: ' + token);
6. }).catch((err: BusinessError) => {
7. console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### setAuthToken9+

PhonePC/2in1TabletTVWearable

setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or token. |
| 12300003 | Account not found. |
| 12400004 | The number of tokens reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
5. if (err) {
6. console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('setAuthToken successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### setAuthToken9+

PhonePC/2in1TabletTVWearable

setAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or token. |
| 12300003 | Account not found. |
| 12400004 | The number of tokens reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
5. console.info('setAuthToken successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### deleteAuthToken9+

PhonePC/2in1TabletTVWearable

deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。如果授权令牌不存在，则不执行任何操作。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or token. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
5. (err: BusinessError) => {
6. if (err) {
7. console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('deleteAuthToken successfully');
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### deleteAuthToken9+

PhonePC/2in1TabletTVWearable

deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。如果授权令牌不存在，则不执行任何操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or token. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
5. console.info('deleteAuthToken successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### setAuthTokenVisibility9+

PhonePC/2in1TabletTVWearable

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
5. (err: BusinessError) => {
6. if (err) {
7. console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('setAuthTokenVisibility successfully');
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### setAuthTokenVisibility9+

PhonePC/2in1TabletTVWearable

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
5. console.info('setAuthTokenVisibility successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### checkAuthTokenVisibility9+

PhonePC/2in1TabletTVWearable

checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 检查可见性的应用包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
5. (err: BusinessError, isVisible: boolean) => {
6. if (err) {
7. console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### checkAuthTokenVisibility9+

PhonePC/2in1TabletTVWearable

checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 用于检查可见性的应用包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示授权令牌对指定应用的可见，返回false表示不可见。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
5. isVisible: boolean) => {
6. console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
7. }).catch((err: BusinessError) => {
8. console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getAllAuthTokens9+

PhonePC/2in1TabletTVWearable

getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AuthTokenInfo](js-apis-appaccount.md#authtokeninfo9)>> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo',
5. (err: BusinessError, tokenArr: appAccount.AuthTokenInfo[]) => {
6. if (err) {
7. console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('getAllAuthTokens successfully, tokenArr: ' + tokenArr);
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### getAllAuthTokens9+

PhonePC/2in1TabletTVWearable

getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AuthTokenInfo](js-apis-appaccount.md#authtokeninfo9)>> | Promise对象，返回授权令牌数组。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo').then((
5. tokenArr: appAccount.AuthTokenInfo[]) => {
6. console.info('getAllAuthTokens successfully, tokenArr: ' + JSON.stringify(tokenArr));
7. }).catch((err: BusinessError) => {
8. console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### getAuthList9+

PhonePC/2in1TabletTVWearable

getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](js-apis-appaccount.md#setauthtokenvisibility9)来设置）。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAuthList('LiSi', 'getSocialData', (err: BusinessError, authList: string[]) => {
5. if (err) {
6. console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getAuthList successfully, authList: ' + authList);
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### getAuthList9+

PhonePC/2in1TabletTVWearable

getAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](js-apis-appaccount.md#setauthtokenvisibility9)来设置）。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回被授权的包名数组。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.getAuthList('LiSi', 'getSocialData').then((authList: string[]) => {
5. console.info('getAuthList successfully, authList: ' + authList);
6. }).catch((err: BusinessError) => {
7. console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### getAuthCallback9+

PhonePC/2in1TabletTVWearable

getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void

获取鉴权会话的认证器回调对象。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 鉴权会话的标识。 |
| callback | AsyncCallback<[AuthCallback](js-apis-appaccount.md#authcallback9)> | 是 | 回调函数。当获取成功时，err为null，data为鉴权会话的认证器回调对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid sessionId. |
| 12300108 | Session not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
6. let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
7. try {
8. appAccountManager.getAuthCallback(sessionId, (err: BusinessError, callback: appAccount.AuthCallback) => {
9. if (err != null) {
10. console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
11. return;
12. }
13. let result: appAccount.AuthResult = {
14. account: {
15. name: 'Lisi',
16. owner: 'com.example.accountjsdemo',
17. },
18. tokenInfo: {
19. token: 'xxxxxx',
20. authType: 'getSocialData'
21. }
22. };
23. callback.onResult(0, result);
24. });
25. } catch (e) {
26. const err = e as BusinessError;
27. console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
28. }
29. }
30. }
```

### getAuthCallback9+

PhonePC/2in1TabletTVWearable

getAuthCallback(sessionId: string): Promise<AuthCallback>

获取鉴权会话的认证器回调对象。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 鉴权会话的标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthCallback](js-apis-appaccount.md#authcallback9)> | Promise对象，返回鉴权会话的认证器回调对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid sessionId. |
| 12300108 | Session not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
6. let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
7. try {
8. appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
9. let result: appAccount.AuthResult = {
10. account: {
11. name: 'Lisi',
12. owner: 'com.example.accountjsdemo',
13. },
14. tokenInfo: {
15. token: 'xxxxxx',
16. authType: 'getSocialData'
17. }
18. };
19. callback.onResult(0, result);
20. }).catch((err: BusinessError) => {
21. console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
22. });
23. } catch (e) {
24. const err = e as BusinessError;
25. console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
26. }
27. }
28. }
```

### queryAuthenticatorInfo9+

PhonePC/2in1TabletTVWearable

queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<[AuthenticatorInfo](js-apis-appaccount.md#authenticatorinfo8)> | 是 | 回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300113 | Authenticator service not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo',
5. (err: BusinessError, info: appAccount.AuthenticatorInfo) => {
6. if (err) {
7. console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
8. } else {
9. console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
10. }
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### queryAuthenticatorInfo9+

PhonePC/2in1TabletTVWearable

queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthenticatorInfo](js-apis-appaccount.md#authenticatorinfo8)> | Promise对象，返回指定应用的认证器信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300113 | Authenticator service not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo').then((
5. info: appAccount.AuthenticatorInfo) => {
6. console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
7. }).catch((err: BusinessError) => {
8. console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
9. });
10. } catch (e) {
11. const err = e as BusinessError;
12. console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
13. }
```

### checkAccountLabels9+

PhonePC/2in1TabletTVWearable

checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void

检查指定应用账号是否满足特定的标签集合。使用callback异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| labels | Array<string> | 是 | 标签数组。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示满足特定的标签集合，data为false表示不满足；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or labels. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let labels = ['student'];
4. try {
5. appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels,
6. (err: BusinessError, hasAllLabels: boolean) => {
7. if (err) {
8. console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info('checkAccountLabels successfully, hasAllLabels: ' + hasAllLabels);
11. }
12. });
13. } catch (e) {
14. const err = e as BusinessError;
15. console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
16. }
```

### checkAccountLabels9+

PhonePC/2in1TabletTVWearable

checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>

检查指定应用账号是否满足特定的标签集合。使用Promise异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| labels | Array<string> | 是 | 标签数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定账号满足特定的标签集合，返回false表示不满足。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or labels. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let labels = ['student'];
4. try {
5. appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels).then((
6. hasAllLabels: boolean) => {
7. console.info('checkAccountLabels successfully: ' + hasAllLabels);
8. }).catch((err: BusinessError) => {
9. console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### deleteCredential9+

PhonePC/2in1TabletTVWearable

deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定类型的凭据信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.deleteCredential('zhangsan', 'PIN_SIX', (err: BusinessError) => {
5. if (err) {
6. console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('deleteCredential successfully');
9. }
10. });
11. } catch (e) {
12. const err = e as BusinessError;
13. console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
14. }
```

### deleteCredential9+

PhonePC/2in1TabletTVWearable

deleteCredential(name: string, credentialType: string): Promise<void>

删除指定应用账号的特定类型的凭据信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. appAccountManager.deleteCredential('zhangsan', 'PIN_SIX').then(() => {
5. console.info('deleteCredential successfully');
6. }).catch((err: BusinessError) => {
7. console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
8. });
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
12. }
```

### selectAccountsByOptions9+

PhonePC/2in1TabletTVWearable

selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SelectAccountsOptions](js-apis-appaccount.md#selectaccountsoptions9) | 是 | 选择账号的选项。 |
| callback | AsyncCallback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 回调函数。当根据选项选择请求方可访问的账号列表时，err为null，data为可访问的账号信息对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid options. |
| 12300010 | Account service busy. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: appAccount.SelectAccountsOptions = {
4. allowedOwners: ['com.example.accountjsdemo'],
5. requiredLabels: ['student']
6. };
7. try {
8. appAccountManager.selectAccountsByOptions(options,
9. (err: BusinessError, accountArr: appAccount.AppAccountInfo[]) => {
10. if (err) {
11. console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
12. } else {
13. console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
14. }
15. });
16. } catch (e) {
17. const err = e as BusinessError;
18. console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
19. }
```

### selectAccountsByOptions9+

PhonePC/2in1TabletTVWearable

selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>

根据选项选择调用方可访问的账号列表。使用Promise异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SelectAccountsOptions](js-apis-appaccount.md#selectaccountsoptions9) | 是 | 选择账号的选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | Promise对象，返回调用方可访问的账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid options. |
| 12300010 | Account service busy. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let options: appAccount.SelectAccountsOptions = {
4. allowedOwners: ['com.example.accountjsdemo']
5. };
6. try {
7. appAccountManager.selectAccountsByOptions(options).then((accountArr: appAccount.AppAccountInfo[]) => {
8. console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
9. }).catch((err: BusinessError) => {
10. console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
11. });
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
15. }
```

### verifyCredential9+

PhonePC/2in1TabletTVWearable

verifyCredential(name: string, owner: string, callback: AuthCallback): void

验证指定账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调函数，返回验证结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', {
6. onResult: (resultCode: number, result?: appAccount.AuthResult) => {
7. console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
8. console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
9. },
10. onRequestRedirected: (request: Want) => {
11. console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
12. }
13. });
14. } catch (e) {
15. const err = e as BusinessError;
16. console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
17. }
```

### verifyCredential9+

PhonePC/2in1TabletTVWearable

verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证用户凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| options | [VerifyCredentialOptions](js-apis-appaccount.md#verifycredentialoptions9) | 是 | 验证凭据的选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调函数，返回验证结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or options. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: appAccount.VerifyCredentialOptions = {
5. credentialType: 'pin',
6. credential: '123456'
7. };
8. try {
9. appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', options, {
10. onResult: (resultCode: number, result?: appAccount.AuthResult) => {
11. console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
12. console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
13. },
14. onRequestRedirected: (request: Want) => {
15. console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
16. }
17. });
18. } catch (e) {
19. const err = e as BusinessError;
20. console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
21. }
```

### setAuthenticatorProperties9+

PhonePC/2in1TabletTVWearable

setAuthenticatorProperties(owner: string, callback: AuthCallback): void

设置指定应用的认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 认证器的所有者的包名。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调函数，返回设置属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', {
6. onResult: (resultCode: number, result?: appAccount.AuthResult) => {
7. console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
8. console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
9. },
10. onRequestRedirected: (request: Want) => {
11. console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
12. }
13. });
14. } catch (e) {
15. const err = e as BusinessError;
16. console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
17. }
```

### setAuthenticatorProperties9+

PhonePC/2in1TabletTVWearable

setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 认证器的所有者的包名。 |
| options | [SetPropertiesOptions](js-apis-appaccount.md#setpropertiesoptions9) | 是 | 设置属性的选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调，返回设置属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner or options. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: appAccount.SetPropertiesOptions = {
5. properties: { prop1: 'value1' }
6. };
7. try {
8. appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', options, {
9. onResult: (resultCode: number, result?: appAccount.AuthResult) => {
10. console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
11. console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
12. },
13. onRequestRedirected: (request: Want) => {
14. console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
15. }
16. });
17. } catch (e) {
18. const err = e as BusinessError;
19. console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
20. }
```

### addAccount(deprecated)

PhonePC/2in1TabletTVWearable

addAccount(name: string, callback: AsyncCallback<void>): void

根据账号名添加应用账号。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](js-apis-appaccount.md#createaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.addAccount('WangWu', (err: BusinessError) => {
4. console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
5. });
```

### addAccount(deprecated)

PhonePC/2in1TabletTVWearable

addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void

根据账号名和额外信息添加应用账号。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](js-apis-appaccount.md#createaccount9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.addAccount('LiSi', 'token101', (err: BusinessError) => {
4. console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
5. });
```

### addAccount(deprecated)

PhonePC/2in1TabletTVWearable

addAccount(name: string, extraInfo?: string): Promise<void>

根据账号名和额外信息添加应用账号。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](js-apis-appaccount.md#createaccount9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 否 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等），默认为空，表示创建的该账号无额外信息需要添加。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.addAccount('LiSi', 'token101').then(()=> {
4. console.info('addAccount Success');
5. }).catch((err: BusinessError) => {
6. console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
7. });
```

### addAccountImplicitly(deprecated)

PhonePC/2in1TabletTVWearable

addAccountImplicitly(owner: string, authType: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

根据指定的账号所有者隐式地添加应用账号。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[createAccountImplicitly](js-apis-appaccount.md#createaccountimplicitly9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。鉴权类型为自定义。 |
| options | {[key: string]: any} | 是 | 鉴权所需要的可选项。可选项可根据自己需要设置。 |
| callback | [AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated) | 是 | 认证器回调对象，返回添加结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, result: Record<string, Object>): void {
10. console.info('resultCode: ' + code);
11. console.info('result: ' + JSON.stringify(result));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. appAccountManager.addAccountImplicitly('com.example.accountjsdemo', 'getSocialData', {}, {
30. onResult: this.onResultCallback,
31. onRequestRedirected: this.onRequestRedirectedCallback
32. });
33. }

35. build() {}
36. }
```

### deleteAccount(deprecated)

PhonePC/2in1TabletTVWearable

deleteAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](js-apis-appaccount.md#removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.deleteAccount('ZhaoLiu', (err: BusinessError) => {
4. console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
5. });
```

### deleteAccount(deprecated)

PhonePC/2in1TabletTVWearable

deleteAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](js-apis-appaccount.md#removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.deleteAccount('ZhaoLiu').then(() => {
4. console.info('deleteAccount Success');
5. }).catch((err: BusinessError) => {
6. console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
7. });
```

### disableAppAccess(deprecated)

PhonePC/2in1TabletTVWearable

disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

禁止指定第三方应用账号名称对指定的第三方应用进行访问。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](js-apis-appaccount.md#setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
4. console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
5. });
```

### disableAppAccess(deprecated)

PhonePC/2in1TabletTVWearable

disableAppAccess(name: string, bundleName: string): Promise<void>

禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](js-apis-appaccount.md#setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要禁用访问的第三方应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
4. console.info('disableAppAccess Success');
5. }).catch((err: BusinessError) => {
6. console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
7. });
```

### enableAppAccess(deprecated)

PhonePC/2in1TabletTVWearable

enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

允许指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](js-apis-appaccount.md#setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当允许指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
4. if (err) {
5. console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('enableAppAccess successful.');
8. }
9. });
```

### enableAppAccess(deprecated)

PhonePC/2in1TabletTVWearable

enableAppAccess(name: string, bundleName: string): Promise<void>

允许指定第三方应用账号的名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](js-apis-appaccount.md#setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
4. console.info('enableAppAccess Success');
5. }).catch((err: BusinessError) => {
6. console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
7. });
```

### checkAppAccountSyncEnable(deprecated)

PhonePC/2in1TabletTVWearable

checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](js-apis-appaccount.md#checkdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.checkAppAccountSyncEnable('ZhangSan', (err: BusinessError, result: boolean) => {
4. if (err) {
5. console.error(`checkAppAccountSyncEnable code: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('checkAppAccountSyncEnable result: ' + result);
8. }
9. });
```

### checkAppAccountSyncEnable(deprecated)

PhonePC/2in1TabletTVWearable

checkAppAccountSyncEnable(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](js-apis-appaccount.md#checkdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.checkAppAccountSyncEnable('ZhangSan').then((data: boolean) => {
4. console.info('checkAppAccountSyncEnable, result: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`checkAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setAccountCredential(deprecated)

PhonePC/2in1TabletTVWearable

setAccountCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](js-apis-appaccount.md#setcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置此应用程序账号的凭据成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001', (err: BusinessError) => {
4. if (err) {
5. console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('setAccountCredential successful.');
8. }
9. });
```

### setAccountCredential(deprecated)

PhonePC/2in1TabletTVWearable

setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](js-apis-appaccount.md#setcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001').then(() => {
4. console.info('setAccountCredential Success');
5. }).catch((err: BusinessError) => {
6. console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setAccountExtraInfo(deprecated)

PhonePC/2in1TabletTVWearable

setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void

设置指定应用账号的额外信息。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](js-apis-appaccount.md#setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002', (err: BusinessError) => {
4. if (err) {
5. console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('setAccountExtraInfo successful.');
8. }
9. });
```

### setAccountExtraInfo(deprecated)

PhonePC/2in1TabletTVWearable

setAccountExtraInfo(name: string, extraInfo: string): Promise<void>

设置此应用程序账号的额外信息。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](js-apis-appaccount.md#setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002').then(() => {
4. console.info('setAccountExtraInfo Success');
5. }).catch((err: BusinessError) => {
6. console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setAppAccountSyncEnable(deprecated)

PhonePC/2in1TabletTVWearable

setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](js-apis-appaccount.md#setdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| isEnable | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当开启或禁止成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAppAccountSyncEnable('ZhangSan', true, (err: BusinessError) => {
4. if (err) {
5. console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('setAppAccountSyncEnable successful.');
8. }
9. });
```

### setAppAccountSyncEnable(deprecated)

PhonePC/2in1TabletTVWearable

setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](js-apis-appaccount.md#setdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| isEnable | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAppAccountSyncEnable('ZhangSan', true).then(() => {
4. console.info('setAppAccountSyncEnable Success');
5. }).catch((err: BusinessError) => {
6. console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setAssociatedData(deprecated)

PhonePC/2in1TabletTVWearable

setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的关联数据。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](js-apis-appaccount.md#setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| value | string | 是 | 关联数据的取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置与此应用账号关联的数据成功时，err为null，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001', (err: BusinessError) => {
4. if (err) {
5. console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('setAssociatedData successful.');
8. }
9. });
```

### setAssociatedData(deprecated)

PhonePC/2in1TabletTVWearable

setAssociatedData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的关联数据。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](js-apis-appaccount.md#setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| value | string | 是 | 关联数据的取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001').then(() => {
4. console.info('setAssociatedData Success');
5. }).catch((err: BusinessError) => {
6. console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
7. });
```

### getAllAccessibleAccounts(deprecated)

PhonePC/2in1TabletTVWearable

getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](js-apis-appaccount.md#getallaccounts9)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAllAccessibleAccounts((err: BusinessError, data: appAccount.AppAccountInfo[])=>{
4. if (err) {
5. console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('getAllAccessibleAccounts data: ' + JSON.stringify(data));
8. }
9. });
```

### getAllAccessibleAccounts(deprecated)

PhonePC/2in1TabletTVWearable

getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](js-apis-appaccount.md#getallaccounts9-1)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | Promise对象，返回全部应用已授权账号信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAllAccessibleAccounts().then((data: appAccount.AppAccountInfo[]) => {
4. console.info('getAllAccessibleAccounts: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
7. });
```

### getAllAccounts(deprecated)

PhonePC/2in1TabletTVWearable

getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](js-apis-appaccount.md#getaccountsbyowner9)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 应用账号信息列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const selfBundle = 'com.example.actsgetallaaccounts';
4. appAccountManager.getAllAccounts(selfBundle, (err: BusinessError, data: appAccount.AppAccountInfo[])=>{
5. if (err) {
6. console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getAllAccounts data:' + JSON.stringify(data));
9. }
10. });
```

### getAllAccounts(deprecated)

PhonePC/2in1TabletTVWearable

getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](js-apis-appaccount.md#getaccountsbyowner9-1)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | Promise对象，返回指定应用全部账号信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const selfBundle = 'com.example.actsgetallaaccounts';
4. appAccountManager.getAllAccounts(selfBundle).then((data: appAccount.AppAccountInfo[]) => {
5. console.info('getAllAccounts: ' + data);
6. }).catch((err: BusinessError) => {
7. console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getAccountCredential(deprecated)

PhonePC/2in1TabletTVWearable

getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](js-apis-appaccount.md#getcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAccountCredential('ZhangSan', 'credentialType001', (err: BusinessError, result: string) => {
4. if (err) {
5. console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('getAccountCredential result: ' + result);
8. }
9. });
```

### getAccountCredential(deprecated)

PhonePC/2in1TabletTVWearable

getAccountCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](js-apis-appaccount.md#getcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回指定应用账号的凭据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAccountCredential('ZhangSan', 'credentialType001').then((data: string) => {
4. console.info('getAccountCredential, result: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
7. });
```

### getAccountExtraInfo(deprecated)

PhonePC/2in1TabletTVWearable

getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](js-apis-appaccount.md#getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取此应用账号的额外信息成功时，err为null，data返回此应用账号的额外信息对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAccountExtraInfo('ZhangSan', (err: BusinessError, result: string) => {
4. if (err) {
5. console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('getAccountExtraInfo result: ' + result);
8. }
9. });
```

### getAccountExtraInfo(deprecated)

PhonePC/2in1TabletTVWearable

getAccountExtraInfo(name: string): Promise<string>

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](js-apis-appaccount.md#getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回此应用程序账号的额外信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAccountExtraInfo('ZhangSan').then((data: string) => {
4. console.info('getAccountExtraInfo, result: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
7. });
```

### getAssociatedData(deprecated)

PhonePC/2in1TabletTVWearable

getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的关联数据。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](js-apis-appaccount.md#getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为关联数据的取值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAssociatedData('ZhangSan', 'k001', (err: BusinessError, result: string) => {
4. if (err) {
5. console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('getAssociatedData result: ' + result);
8. }
9. });
```

### getAssociatedData(deprecated)

PhonePC/2in1TabletTVWearable

getAssociatedData(name: string, key: string): Promise<string>

获取与此应用程序账号关联的数据。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](js-apis-appaccount.md#getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回关联数据的取值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAssociatedData('ZhangSan', 'k001').then((data: string) => {
4. console.info('getAssociatedData: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
7. });
```

### on('change')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[on('accountChange')](js-apis-appaccount.md#onaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'change' | 是 | 事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。 |
| owners | Array<string> | 是 | 应用账号所有者的包名列表。 |
| callback | Callback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 是 | 需要注册的回调函数，返回信息发生变更的应用账号列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
4. console.info('receive change data:' + JSON.stringify(data));
5. }

7. try {
8. appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
9. } catch (e) {
10. const err = e as BusinessError;
11. console.error(`on accountOnOffDemo code is ${err.code}, message is ${err.message}`);
12. }
```

### off('change')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[off('accountChange')](js-apis-appaccount.md#offaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'change' | 是 | 事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。 |
| callback | Callback<Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)>> | 否 | 需要注销的回调函数，默认为空，表示取消该类型事件的所有回调。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
4. console.info('receive change data: ' + JSON.stringify(data));
5. appAccountManager.off('change', () => {
6. console.info('off finish');
7. })
8. }

10. try {
11. appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
12. } catch (e) {
13. const err = e as BusinessError;
14. console.error(`on accountOnOffDemo err: code is ${err.code}, message is ${err.message}`);
15. }
```

### authenticate(deprecated)

PhonePC/2in1TabletTVWearable

authenticate(name: string, owner: string, authType: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[auth](js-apis-appaccount.md#auth9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| options | {[key: string]: any} | 是 | 鉴权所需的可选项。 |
| callback | [AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated) | 是 | 回调对象，返回鉴权结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

9. onResultCallback(code: number, result: Record<string, Object>): void {
10. console.info('resultCode: ' + code);
11. console.info('result: ' + JSON.stringify(result));
12. }

14. onRequestRedirectedCallback(request: Want): void {
15. let wantInfo: Want = {
16. deviceId: '',
17. bundleName: 'com.example.accountjsdemo',
18. action: 'ohos.want.action.viewData',
19. entities: ['entity.system.default'],
20. }
21. this.context.startAbility(wantInfo).then(() => {
22. console.info('startAbility successfully');
23. }).catch((err: BusinessError) => {
24. console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
25. })
26. }

28. aboutToAppear(): void {
29. appAccountManager.authenticate('LiSi', 'com.example.accountjsdemo', 'getSocialData', {}, {
30. onResult: this.onResultCallback,
31. onRequestRedirected: this.onRequestRedirectedCallback
32. });
33. }

35. build() {}
36. }
```

### getOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](js-apis-appaccount.md#getauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
4. (err: BusinessError, data: string) => {
5. if (err) {
6. console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getOAuthToken token: ' + data);
9. }
10. });
```

### getOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

getOAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](js-apis-appaccount.md#getauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回授权令牌。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((data: string) => {
4. console.info('getOAuthToken token: ' + data);
5. }).catch((err: BusinessError) => {
6. console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](js-apis-appaccount.md#setauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
4. if (err) {
5. console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('setOAuthToken successful.');
8. }
9. });
```

### setOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

setOAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](js-apis-appaccount.md#setauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
4. console.info('setOAuthToken successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
7. });
```

### deleteOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](js-apis-appaccount.md#deleteauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
4. (err: BusinessError) => {
5. if (err) {
6. console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('deleteOAuthToken successful.');
9. }
10. });
```

### deleteOAuthToken(deprecated)

PhonePC/2in1TabletTVWearable

deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](js-apis-appaccount.md#deleteauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
4. console.info('deleteOAuthToken successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
7. });
```

### setOAuthTokenVisibility(deprecated)

PhonePC/2in1TabletTVWearable

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](js-apis-appaccount.md#setauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
4. (err: BusinessError) => {
5. if (err) {
6. console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('setOAuthTokenVisibility successful.');
9. }
10. });
```

### setOAuthTokenVisibility(deprecated)

PhonePC/2in1TabletTVWearable

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](js-apis-appaccount.md#setauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
4. console.info('setOAuthTokenVisibility successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
7. });
```

### checkOAuthTokenVisibility(deprecated)

PhonePC/2in1TabletTVWearable

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](js-apis-appaccount.md#checkauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 检查可见性的应用包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
4. (err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('checkOAuthTokenVisibility isVisible: ' + data);
9. }
10. });
```

### checkOAuthTokenVisibility(deprecated)

PhonePC/2in1TabletTVWearable

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](js-apis-appaccount.md#checkauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 用于检查可见性的应用包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定鉴权类型的OAuth令牌对特定应用的可见，返回false表示不可见。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
4. data: boolean) => {
5. console.info('checkOAuthTokenVisibility isVisible: ' + data);
6. }).catch((err: BusinessError) => {
7. console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getAllOAuthTokens(deprecated)

PhonePC/2in1TabletTVWearable

getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](js-apis-appaccount.md#getallauthtokens9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[OAuthTokenInfo](js-apis-appaccount.md#oauthtokeninfodeprecated)>> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo',
4. (err: BusinessError, data: appAccount.OAuthTokenInfo[]) => {
5. if (err) {
6. console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
9. }
10. });
```

### getAllOAuthTokens(deprecated)

PhonePC/2in1TabletTVWearable

getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](js-apis-appaccount.md#getallauthtokens9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array< [OAuthTokenInfo](js-apis-appaccount.md#oauthtokeninfodeprecated)>> | Promise对象，返回授权令牌数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo').then((
4. data: appAccount.OAuthTokenInfo[]) => {
5. console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
8. });
```

### getOAuthList(deprecated)

PhonePC/2in1TabletTVWearable

getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](js-apis-appaccount.md#setoauthtokenvisibilitydeprecated)来设置）。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](js-apis-appaccount.md#getauthlist9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getOAuthList('LiSi', 'getSocialData', (err: BusinessError, data: string[]) => {
4. if (err) {
5. console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info('getOAuthList data: ' + JSON.stringify(data));
8. }
9. });
```

### getOAuthList(deprecated)

PhonePC/2in1TabletTVWearable

getOAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](js-apis-appaccount.md#setoauthtokenvisibilitydeprecated)来设置）。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](js-apis-appaccount.md#getauthlist9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回被授权的包名数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getOAuthList('LiSi', 'getSocialData').then((data: string[]) => {
4. console.info('getOAuthList data: ' + JSON.stringify(data));
5. }).catch((err: BusinessError) => {
6. console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
7. });
```

### getAuthenticatorCallback(deprecated)

PhonePC/2in1TabletTVWearable

getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void

获取鉴权会话的认证器回调。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](js-apis-appaccount.md#getauthcallback9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 鉴权会话的标识。 |
| callback | AsyncCallback<[AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated)> | 是 | 回调函数。当获取鉴权会话的认证器回调函数成功时，err为null，data为认证器回调函数；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
6. let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
7. appAccountManager.getAuthenticatorCallback(sessionId,
8. (err: BusinessError, callback: appAccount.AuthenticatorCallback) => {
9. if (err.code != appAccount.ResultCode.SUCCESS) {
10. console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
11. return;
12. }
13. callback.onResult(appAccount.ResultCode.SUCCESS, {
14. name: 'LiSi',
15. owner: 'com.example.accountjsdemo',
16. authType: 'getSocialData',
17. token: 'xxxxxx'
18. });
19. });
20. }
21. }
```

### getAuthenticatorCallback(deprecated)

PhonePC/2in1TabletTVWearable

getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>

获取鉴权会话的认证器回调。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](js-apis-appaccount.md#getauthcallback9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 鉴权会话的标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated)> | Promise对象，返回鉴权会话的认证器回调对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
6. let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
7. appAccountManager.getAuthenticatorCallback(sessionId).then((
8. callback: appAccount.AuthenticatorCallback) => {
9. callback.onResult(appAccount.ResultCode.SUCCESS, {
10. name: 'LiSi',
11. owner: 'com.example.accountjsdemo',
12. authType: 'getSocialData',
13. token: 'xxxxxx'
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
17. });
18. }
19. }
```

### getAuthenticatorInfo(deprecated)

PhonePC/2in1TabletTVWearable

getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](js-apis-appaccount.md#queryauthenticatorinfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<[AuthenticatorInfo](js-apis-appaccount.md#authenticatorinfo8)> | 是 | 回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo',
4. (err: BusinessError, data: appAccount.AuthenticatorInfo) => {
5. if (err) {
6. console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('getAuthenticatorInfo data: ' + JSON.stringify(data));
9. }
10. });
```

### getAuthenticatorInfo(deprecated)

PhonePC/2in1TabletTVWearable

getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](js-apis-appaccount.md#queryauthenticatorinfo9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthenticatorInfo](js-apis-appaccount.md#authenticatorinfo8)> | Promise对象，返回指定应用的认证器信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo').then((
4. data: appAccount.AuthenticatorInfo) => {
5. console.info('getAuthenticatorInfo: ' + JSON.stringify(data));
6. }).catch((err: BusinessError) => {
7. console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
8. });
```

## AppAccountInfo

PhonePC/2in1TabletTVWearable

表示应用账号信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| owner | string | 否 | 否 | 应用账号所有者的包名。 |
| name | string | 否 | 否 | 应用账号的名称。 |

## AuthTokenInfo9+

PhonePC/2in1TabletTVWearable

表示Auth令牌信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authType | string | 否 | 否 | 令牌的鉴权类型。 |
| token | string | 否 | 否 | 令牌的取值。 |
| account | [AppAccountInfo](js-apis-appaccount.md#appaccountinfo) | 否 | 是 | 令牌所属的账号信息，默认为空。 |

## OAuthTokenInfo(deprecated)

PhonePC/2in1TabletTVWearable

表示OAuth令牌信息。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthTokenInfo](js-apis-appaccount.md#authtokeninfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authType | string | 否 | 否 | 令牌的鉴权类型。 |
| token | string | 否 | 否 | 令牌的取值。 |

## AuthenticatorInfo8+

PhonePC/2in1TabletTVWearable

表示OAuth认证器信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| owner | string | 否 | 否 | 认证器的所有者的包名。 |
| iconId | number | 否 | 否 | 认证器的图标标识。 |
| labelId | number | 否 | 否 | 认证器的标签标识。 |

## AuthResult9+

PhonePC/2in1TabletTVWearable

表示认证结果信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| account | [AppAccountInfo](js-apis-appaccount.md#appaccountinfo) | 否 | 是 | 令牌所属的账号信息，默认为空。 |
| tokenInfo | [AuthTokenInfo](js-apis-appaccount.md#authtokeninfo9) | 否 | 是 | 令牌信息，默认为空。 |

## CreateAccountOptions9+

PhonePC/2in1TabletTVWearable

表示创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customData | Record<string, string> | 否 | 是 | 自定义数据，默认为空。 |

## CreateAccountImplicitlyOptions9+

PhonePC/2in1TabletTVWearable

表示隐式创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requiredLabels | Array<string> | 否 | 是 | 所需的标签，默认为空。 |
| authType | string | 否 | 是 | 鉴权类型，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

## SelectAccountsOptions9+

PhonePC/2in1TabletTVWearable

表示用于选择账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| allowedAccounts | Array<[AppAccountInfo](js-apis-appaccount.md#appaccountinfo)> | 否 | 是 | 允许的账号数组，默认为空。 |
| allowedOwners | Array<string> | 否 | 是 | 允许的账号所有者数组，默认为空。 |
| requiredLabels | Array<string> | 否 | 是 | 认证器的标签标识，默认为空。 |

## VerifyCredentialOptions9+

PhonePC/2in1TabletTVWearable

表示用于验证凭据的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialType | string | 否 | 是 | 凭据类型，默认为空。 |
| credential | string | 否 | 是 | 凭据取值，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

## SetPropertiesOptions9+

PhonePC/2in1TabletTVWearable

表示用于设置属性的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties | Record<string, Object> | 否 | 是 | 属性对象，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

## Constants8+

PhonePC/2in1TabletTVWearable

表示常量的枚举。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_ADD\_ACCOUNT\_IMPLICITLY(deprecated) | 'addAccountImplicitly' | 表示操作，隐式添加账号。  \*\*说明：\*\*从API version 8开始支持，从API version 9开始废弃，建议使用ACTION\_CREATE\_ACCOUNT\_IMPLICITLY替代。 |
| ACTION\_AUTHENTICATE(deprecated) | 'authenticate' | 表示操作，鉴权。  \*\*说明：\*\*从API version 8开始支持，从API version 9开始废弃，建议使用ACTION\_AUTH替代。 |
| ACTION\_CREATE\_ACCOUNT\_IMPLICITLY9+ | 'createAccountImplicitly' | 表示操作，隐式创建账号。 |
| ACTION\_AUTH9+ | 'auth' | 表示操作，鉴权。 |
| ACTION\_VERIFY\_CREDENTIAL9+ | 'verifyCredential' | 表示操作，验证凭据。 |
| ACTION\_SET\_AUTHENTICATOR\_PROPERTIES9+ | 'setAuthenticatorProperties' | 表示操作，设置认证器属性。 |
| KEY\_NAME | 'name' | 表示键名，应用账号的名称。 |
| KEY\_OWNER | 'owner' | 表示键名，应用账号所有者的包名。 |
| KEY\_TOKEN | 'token' | 表示键名，令牌。 |
| KEY\_ACTION | 'action' | 表示键名，操作。 |
| KEY\_AUTH\_TYPE | 'authType' | 表示键名，鉴权类型。 |
| KEY\_SESSION\_ID | 'sessionId' | 表示键名，会话标识。 |
| KEY\_CALLER\_PID | 'callerPid' | 表示键名，调用方PID。 |
| KEY\_CALLER\_UID | 'callerUid' | 表示键名，调用方UID。 |
| KEY\_CALLER\_BUNDLE\_NAME | 'callerBundleName' | 表示键名，调用方包名。 |
| KEY\_REQUIRED\_LABELS9+ | 'requiredLabels' | 表示键名，必需的标签。 |
| KEY\_BOOLEAN\_RESULT9+ | 'booleanResult' | 表示键名，布尔返回值。 |

## ResultCode(deprecated)

PhonePC/2in1TabletTVWearable

表示返回码的枚举。

说明

从API version 8开始支持，从API version 9开始废弃。相关信息建议查看[账号管理错误码](errorcode-account.md)替代。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 表示操作成功。 |
| ERROR\_ACCOUNT\_NOT\_EXIST | 10001 | 表示应用账号不存在。 |
| ERROR\_APP\_ACCOUNT\_SERVICE\_EXCEPTION | 10002 | 表示应用账号服务异常。 |
| ERROR\_INVALID\_PASSWORD | 10003 | 表示密码无效。 |
| ERROR\_INVALID\_REQUEST | 10004 | 表示请求无效。 |
| ERROR\_INVALID\_RESPONSE | 10005 | 表示响应无效。 |
| ERROR\_NETWORK\_EXCEPTION | 10006 | 表示网络异常。 |
| ERROR\_OAUTH\_AUTHENTICATOR\_NOT\_EXIST | 10007 | 表示认证器不存在。 |
| ERROR\_OAUTH\_CANCELED | 10008 | 表示鉴权取消。 |
| ERROR\_OAUTH\_LIST\_TOO\_LARGE | 10009 | 表示开放授权列表过大。 |
| ERROR\_OAUTH\_SERVICE\_BUSY | 10010 | 表示开放授权服务忙碌。 |
| ERROR\_OAUTH\_SERVICE\_EXCEPTION | 10011 | 表示开放授权服务异常。 |
| ERROR\_OAUTH\_SESSION\_NOT\_EXIST | 10012 | 表示鉴权会话不存在。 |
| ERROR\_OAUTH\_TIMEOUT | 10013 | 表示鉴权超时。 |
| ERROR\_OAUTH\_TOKEN\_NOT\_EXIST | 10014 | 表示开放授权令牌不存在。 |
| ERROR\_OAUTH\_TOKEN\_TOO\_MANY | 10015 | 表示开放授权令牌过多。 |
| ERROR\_OAUTH\_UNSUPPORT\_ACTION | 10016 | 表示不支持的鉴权操作。 |
| ERROR\_OAUTH\_UNSUPPORT\_AUTH\_TYPE | 10017 | 表示不支持的鉴权类型。 |
| ERROR\_PERMISSION\_DENIED | 10018 | 表示权限不足。 |

## AuthCallback9+

PhonePC/2in1TabletTVWearable

认证器回调类。

### onResult9+

PhonePC/2in1TabletTVWearable

onResult: (code: number, result?: AuthResult) => void

通知请求结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 鉴权结果码。 |
| result | [AuthResult](js-apis-appaccount.md#authresult9) | 否 | 鉴权结果，默认为空，表示不接收认证结果信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
4. let sessionId = '1234';
5. appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
6. let result: appAccount.AuthResult = {
7. account: {
8. name: 'Lisi',
9. owner: 'com.example.accountjsdemo',
10. },
11. tokenInfo: {
12. token: 'xxxxxx',
13. authType: 'getSocialData'
14. }
15. };
16. callback.onResult(appAccount.ResultCode.SUCCESS, result);
17. }).catch((err: BusinessError) => {
18. console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
19. });
```

### onRequestRedirected9+

PhonePC/2in1TabletTVWearable

onRequestRedirected: (request: Want) => void

通知请求被跳转。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Want](js-apis-app-ability-want.md) | 是 | 用于跳转的请求信息。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';

3. class MyAuthenticator extends appAccount.Authenticator {
4. createAccountImplicitly(
5. options: appAccount.CreateAccountImplicitlyOptions, callback: appAccount.AuthCallback) {
6. let want: Want = {
7. bundleName: 'com.example.accountjsdemo',
8. abilityName: 'com.example.accountjsdemo.LoginAbility',
9. };
10. callback.onRequestRedirected(want);
11. }

13. auth(name: string, authType: string,
14. options: Record<string, Object>, callback: appAccount.AuthCallback) {
15. let result: appAccount.AuthResult = {
16. account: {
17. name: 'Lisi',
18. owner: 'com.example.accountjsdemo',
19. },
20. tokenInfo: {
21. token: 'xxxxxx',
22. authType: 'getSocialData'
23. }
24. };
25. callback.onResult(appAccount.ResultCode.SUCCESS, result);
26. }
27. }
```

### onRequestContinued9+

PhonePC/2in1TabletTVWearable

onRequestContinued?: () => void

通知请求被继续处理。

**系统能力：** SystemCapability.Account.AppAccount

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
4. let sessionId = '1234';
5. appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
6. if (callback.onRequestContinued != undefined) {
7. callback.onRequestContinued();
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
11. });
```

## AuthenticatorCallback(deprecated)

PhonePC/2in1TabletTVWearable

OAuth认证器回调接口。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthCallback](js-apis-appaccount.md#authcallback9)替代。

### onResult(deprecated)

PhonePC/2in1TabletTVWearable

onResult: (code: number, result: {[key: string]: any;}) => void

通知请求结果。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[onResult](js-apis-appaccount.md#onresult9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 鉴权结果码。 |
| result | {[key: string]: any} | 是 | 鉴权结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
4. let sessionId = '1234';
5. appAccountManager.getAuthenticatorCallback(sessionId).then((callback: appAccount.AuthenticatorCallback) => {
6. callback.onResult(appAccount.ResultCode.SUCCESS, {
7. name: 'LiSi',
8. owner: 'com.example.accountjsdemo',
9. authType: 'getSocialData',
10. token: 'xxxxxx'
11. });
12. }).catch((err: BusinessError) => {
13. console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
14. });
```

### onRequestRedirected(deprecated)

PhonePC/2in1TabletTVWearable

onRequestRedirected: (request: Want) => void

通知请求被跳转。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[onRequestRedirected](js-apis-appaccount.md#onrequestredirected9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Want](js-apis-app-ability-want.md) | 是 | 用于跳转的请求信息。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';

3. class MyAuthenticator extends appAccount.Authenticator {
4. addAccountImplicitly(authType: string, callerBundleName: string,
5. options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
6. let want: Want = {
7. bundleName: 'com.example.accountjsdemo',
8. abilityName: 'com.example.accountjsdemo.LoginAbility',
9. };
10. callback.onRequestRedirected(want);
11. }

13. authenticate(name: string, authType: string, callerBundleName: string,
14. options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
15. callback.onResult(appAccount.ResultCode.SUCCESS, {
16. name: name,
17. authType: authType,
18. token: 'xxxxxx'
19. });
20. }
21. }
```

## Authenticator8+

PhonePC/2in1TabletTVWearable

认证器基类。

### createAccountImplicitly9+

PhonePC/2in1TabletTVWearable

createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CreateAccountImplicitlyOptions](js-apis-appaccount.md#createaccountimplicitlyoptions9) | 是 | 隐式创建账号的选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调对象，用于返回创建结果。 |

### addAccountImplicitly(deprecated)

PhonePC/2in1TabletTVWearable

addAccountImplicitly(authType: string, callerBundleName: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

根据指定的鉴权类型和可选项，隐式地添加应用账号。使用callback异步回调。

说明

从API version 8开始支持, 从API version 9开始废弃。建议使用[createAccountImplicitly](js-apis-appaccount.md#createaccountimplicitly9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | string | 是 | 应用账号的鉴权类型。 |
| callerBundleName | string | 是 | 鉴权请求方的包名。 |
| options | {[key: string]: any} | 是 | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated) | 是 | 认证器回调，用于返回鉴权结果。 |

### auth9+

PhonePC/2in1TabletTVWearable

auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 应用账号的鉴权类型。 |
| options | Record<string, Object> | 是 | 鉴权所需要的可选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 回调对象，用于返回鉴权结果。 |

### authenticate(deprecated)

PhonePC/2in1TabletTVWearable

authenticate(name: string, authType: string, callerBundleName: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权，获取OAuth令牌。使用callback异步回调。

说明

从API version 8开始支持, 从API version 9开始废弃。建议使用[auth](js-apis-appaccount.md#auth9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 应用账号的鉴权类型。 |
| callerBundleName | string | 是 | 鉴权请求方的包名。 |
| options | {[key: string]: any} | 是 | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](js-apis-appaccount.md#authenticatorcallbackdeprecated) | 是 | 认证器回调，用于返回鉴权结果。 |

### verifyCredential9+

PhonePC/2in1TabletTVWearable

verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| options | [VerifyCredentialOptions](js-apis-appaccount.md#verifycredentialoptions9) | 是 | 验证凭据的可选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调，用于返回验证结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](js-apis-appaccount.md#getremoteobject9)中的示例。

### setProperties9+

PhonePC/2in1TabletTVWearable

setProperties(options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetPropertiesOptions](js-apis-appaccount.md#setpropertiesoptions9) | 是 | 设置属性的可选项。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调，用于返回设置结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](js-apis-appaccount.md#getremoteobject9)中的示例。

### checkAccountLabels9+

PhonePC/2in1TabletTVWearable

checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void

检查账号标签。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| labels | Array<string> | 是 | 标签数组。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调，用于返回检查结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](js-apis-appaccount.md#getremoteobject9)中的示例。

### checkAccountRemovable9+

PhonePC/2in1TabletTVWearable

checkAccountRemovable(name: string, callback: AuthCallback): void

判断账号是否可以删除。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 应用账号的名称。 |
| callback | [AuthCallback](js-apis-appaccount.md#authcallback9) | 是 | 认证器回调，用于返回判断结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](js-apis-appaccount.md#getremoteobject9)中的示例。

### getRemoteObject9+

PhonePC/2in1TabletTVWearable

getRemoteObject(): rpc.RemoteObject

获取认证器的远程对象，不可以重载实现。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [rpc.RemoteObject](js-apis-rpc.md#remoteobject) | 认证器Authenticator的远程对象。用于跨进程通信。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](js-apis-appaccount.md#getremoteobject9)中的示例。

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { Want } from '@kit.AbilityKit';

4. class MyAuthenticator extends appAccount.Authenticator {
5. verifyCredential(name: string,
6. options: appAccount.VerifyCredentialOptions, callback: appAccount.AuthCallback) {
7. let want: Want = {
8. bundleName: 'com.example.accountjsdemo',
9. abilityName: 'com.example.accountjsdemo.VerifyAbility',
10. parameters: {
11. name: name
12. }
13. };
14. callback.onRequestRedirected(want);
15. }

17. setProperties(options: appAccount.SetPropertiesOptions, callback: appAccount.AuthCallback) {
18. let want: Want = {
19. bundleName: 'com.example.accountjsdemo',
20. abilityName: 'com.example.accountjsdemo.SetPropertiesAbility',
21. parameters: {
22. options: options
23. }
24. };
25. callback.onRequestRedirected(want);
26. }

28. checkAccountLabels(name: string, labels: string[], callback: appAccount.AuthCallback) {
29. callback.onResult(0);
30. }

32. checkAccountRemovable(name: string, callback: appAccount.AuthCallback) {
33. callback.onResult(0);
34. }
35. }

37. export default {
38. onConnect(want: Want): rpc.RemoteObject { // serviceAbility 生命周期函数, 需要放在serviceAbility中
39. let authenticator = new MyAuthenticator();
40. return authenticator.getRemoteObject();
41. }
42. }
```
