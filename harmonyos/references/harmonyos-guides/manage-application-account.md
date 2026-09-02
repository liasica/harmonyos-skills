---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/manage-application-account
title: 管理应用账号
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 账号管理 > 应用账号 > 管理应用账号
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cd557e04e01ccc464a1cf59a28cb24c7260f122bf240759ac92bbeaac3d6e7c9
---

应用开发者可以使用[@ohos.account.appAccount](../harmonyos-references/js-apis-appaccount.md)管理本应用的账号数据。

能力限制：应用卸载场景下，被卸载应用的账号数据会被删除；本地账号删除场景下，被删除本地账号下的所有应用的账号数据会被删除。

## 模拟器支持情况

本模块支持模拟器。

## 开发准备

1. 导入应用账号模块。

```typescript
import { appAccount, BusinessError } from '@kit.BasicServicesKit';
```

1. 获取应用账号的实例对象。

```typescript
const appAccountManager = appAccount.createAppAccountManager();
```

## 创建应用账号

用户在应用中登录后，开发者可以在系统中创建一个关联的应用账号，后续可以基于此账号进行数据管理。

具体开发实例如下：

1. 参数准备，指定账号名和可选配置。

```typescript
    let name: string = 'ZhangSan';
    let options: appAccount.CreateAccountOptions = {
      customData: {
        age: '10'
      }
    };
```

1. 调用[createAccount](../harmonyos-references/js-apis-appaccount.md#createaccount9)接口，根据名称和选项创建应用账号。

```typescript
    appAccountManager.createAccount(name, options).then(()=>{
      console.info('createAccount successfully');
    // ···
    }).catch((err: BusinessError)=>{
       console.error(`createAccount failed, error: code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 查询应用账号列表

具体开发实例如下：

调用[getAllAccounts](../harmonyos-references/js-apis-appaccount.md#getallaccounts9)接口查询账号列表。

```typescript
    appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo[]) => {
      console.info('getAllAccounts successfully, data: ' + JSON.stringify(data));
    // ···
    }).catch((err: BusinessError) => {
      console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 存取账号的凭据

具体开发实例如下：

1. 准备参数，指定账号名、凭据类型和凭据。

```typescript
    let name: string = 'ZhangSan';
    let credentialType: string = 'PIN_SIX';
    let credential: string = 'xxxxxx';
```

1. 调用[getCredential](../harmonyos-references/js-apis-appaccount.md#getcredential9)接口，获取账号的凭据。

```typescript
    appAccountManager.getCredential(name, credentialType).then((data: string) => {
      console.info('getCredential successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

1. 调用[setCredential](../harmonyos-references/js-apis-appaccount.md#setcredential9)接口，设置账号的凭据。

```typescript
    await appAccountManager.setCredential(name, credentialType, credential).then(() => {
      console.info('setCredential successfully');
    }).catch((err: BusinessError) => {
      console.error(`setCredential failed: code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 存取账号的自定义数据

具体开发实例如下：

1. 准备参数，指定账号名和自定义键值。

```typescript
    let name: string = 'ZhangSan';
    let key: string = 'age';
    let value: string = '12';
```

1. 调用[setCustomData](../harmonyos-references/js-apis-appaccount.md#setcustomdata9)接口，设置账号的自定义数据。

```typescript
    await appAccountManager.setCustomData(name, key, value).then(() => {
      console.info('setCustomData successfully');
    }).catch((err: BusinessError) => {
      console.error(`setCustomData failed: code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

1. 调用[getCustomData](../harmonyos-references/js-apis-appaccount.md#getcustomdata9)接口，获取账号的自定义数据。

```typescript
    appAccountManager.getCustomData(name, key).then((data: string) => {
      console.info('getCustomData successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(`getCustomData failed, code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 存取账号的授权令牌

具体开发实例如下：

1. 准备参数，指定账号名、账号所有者、授权类型和授权令牌。

```typescript
    let name: string = 'ZhangSan';
    let owner: string = 'com.samples.managerapplicationaccount';
    let authType: string = 'getSocialData';
    let token: string = 'xxxxxx';
```

1. 调用[setAuthToken](../harmonyos-references/js-apis-appaccount.md#setauthtoken9)接口，设置指定授权类型的授权令牌。

```typescript
    await appAccountManager.setAuthToken(name, authType, token).then(() => {
      console.info('setAuthToken successfully');
    }).catch((err: BusinessError) => {
      console.error(`setAuthToken failed: code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

1. 调用[getAuthToken](../harmonyos-references/js-apis-appaccount.md#getauthtoken9)接口，获取指定授权类型的授权令牌。

```typescript
    await appAccountManager.getAuthToken(name, owner, authType).then((data: string) => {
      console.info('getAuthToken successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 删除应用账号

用户退出登录后，应用需及时将相应的应用账号从系统中删除。

具体开发实例如下：

指定要删除的账号名称，调用[removeAccount](../harmonyos-references/js-apis-appaccount.md#removeaccount9)接口删除账号。

```typescript
    let name: string = 'ZhangSan';
    appAccountManager.removeAccount(name).then(() => {
      console.info('removeAccount successfully');
    // ···
    }).catch((err: BusinessError) => {
      console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
    // ···
    });
```

## 示例代码

* [应用账号管理](https://gitcode.com/HarmonyOS_Samples/app-account-manager)
