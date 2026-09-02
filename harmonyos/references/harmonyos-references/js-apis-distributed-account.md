---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-account
title: "@ohos.account.distributedAccount (分布式账号管理)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 账号管理 > @ohos.account.distributedAccount (分布式账号管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8f9f13991cbc7e1996c6b30e08d68875444bc680b78c24cfe9530c4dfeeb110
---

本模块提供管理分布式账号的一些基础功能，主要包括查询和更新账号登录状态。适用于多设备协同场景，提升跨设备账号管理的一致性和用户体验。典型使用场景包括多设备协同、分布式数据同步、跨设备能力调用等。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { distributedAccount } from '@kit.BasicServicesKit';
```

## distributedAccount.getDistributedAccountAbility

getDistributedAccountAbility(): DistributedAccountAbility

获取分布式账号的单实例对象。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DistributedAccountAbility](js-apis-distributed-account.md#distributedaccountability) | 返回一个实例，实例提供查询和更新分布式账号登录状态方法。 |

**示例：**

```ts
// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
```

## DistributedAccountAbility

提供查询和更新分布式账号登录状态方法（使用前需要先获取分布式账号的单实例对象）。

### getOsAccountDistributedInfo9+

getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void

获取分布式账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.GET\_DISTRIBUTED\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | 是 | 回调函数。当获取分布式账号信息成功时，err为undefined，data为获取到的分布式账号信息对象；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfo(
    (err: BusinessError, data: distributedAccount.DistributedInfo) => {
      if (err) {
        console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('distributed information: ' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

### getOsAccountDistributedInfo9+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
    console.info('distributed information: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

### queryOsAccountDistributedInfo(deprecated)

queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void

获取分布式账号信息。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getOsAccountDistributedInfo](js-apis-distributed-account.md#getosaccountdistributedinfo9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | 是 | 回调函数。当获取分布式账号信息成功时，err为undefined，data为获取到的分布式账号信息对象；否则err为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
accountAbility.queryOsAccountDistributedInfo(
  (err: BusinessError, data: distributedAccount.DistributedInfo) => {
    if (err) {
      console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('distributed information: ' + JSON.stringify(data));
    }
  });
```

### queryOsAccountDistributedInfo(deprecated)

queryOsAccountDistributedInfo(): Promise<DistributedInfo>

获取分布式账号信息。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getOsAccountDistributedInfo](js-apis-distributed-account.md#getosaccountdistributedinfo9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED\_DATASYNC

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DistributedInfo](js-apis-distributed-account.md#distributedinfo)> | Promise对象，返回分布式账号信息对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
accountAbility.queryOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
  console.info('distributed information: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
});
```

### setOsAccountDistributedInfo9+

setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void

更新分布式账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_DISTRIBUTED\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新分布式账号信息成功时，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid accountInfo. |
| 12300003 | Account not found. |
| 12300406 | The distributed account information has already been bound to a sub-profile of the same OS account.  适用版本：26.0.0+ |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// 示例值，实际使用时请通过getOsAccountDistributedInfo获取真实分布式账号信息
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
    if (err) {
      console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountDistributedInfo successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

### setOsAccountDistributedInfo9+

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
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid accountInfo. |
| 12300003 | Account not found. |
| 12300406 | The distributed account information has already been bound to a sub-profile of the same OS account.  适用版本：26.0.0+ |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// 示例值，实际使用时请通过getOsAccountDistributedInfo获取真实分布式账号信息
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfo(accountInfo).then(() => {
    console.info('setOsAccountDistributedInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

### updateOsAccountDistributedInfo(deprecated)

updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void

更新分布式账号信息。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[setOsAccountDistributedInfo](js-apis-distributed-account.md#setosaccountdistributedinfo9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新分布式账号信息成功时，err为undefined，否则err为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// 示例值，实际使用时请通过getOsAccountDistributedInfo获取真实分布式账号信息
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
accountAbility.updateOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
  if (err) {
    console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('updateOsAccountDistributedInfo successfully');
  }
});
```

### updateOsAccountDistributedInfo(deprecated)

updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>

更新分布式账号信息。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[setOsAccountDistributedInfo](js-apis-distributed-account.md#setosaccountdistributedinfo9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountInfo | [DistributedInfo](js-apis-distributed-account.md#distributedinfo) | 是 | 分布式账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取分布式账号的单实例对象
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// 示例值，实际使用时请通过getOsAccountDistributedInfo获取真实分布式账号信息
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
accountAbility.updateOsAccountDistributedInfo(accountInfo).then(() => {
  console.info('updateOsAccountDistributedInfo successfully');
}).catch((err: BusinessError) => {
  console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
});
```

## DistributedInfo

提供操作系统账号的分布式账号信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 分布式账号名称，非空字符串。最大长度为256个字节。 |
| id | string | 否 | 否 | 分布式账号UID，非空字符串。最大长度为512个字节。 |
| event | string | 否 | 否 | 分布式账号登录状态，包括登录、登出、Token失效和注销，分别对应以下字符串：  - Ohos.account.event.LOGIN  - Ohos.account.event.LOGOUT  - Ohos.account.event.TOKEN\_INVALID  - Ohos.account.event.LOGOFF |
| nickname9+ | string | 否 | 是 | 分布式账号的昵称，当需要显示用户昵称时设置。不设置时默认为空，不影响账号功能使用。最大长度为1024个字节。 |
| avatar9+ | string | 否 | 是 | 分布式账号的头像，当需要显示用户头像时设置。不设置时默认为空，不影响账号功能使用。 最大长度为10M（10485760个字节）。 |
| status10+ | [DistributedAccountStatus](js-apis-distributed-account.md#distributedaccountstatus10) | 是 | 是 | 分布式账号的状态，枚举类型。当需要查询或设置账号登录状态时使用。不设置时默认为NOT\_LOGGED\_IN（未登录状态）。 |
| scalableData8+ | object | 否 | 是 | 分布式账号扩展信息，当需要传递定制化业务信息时设置，以k-v形式传递。不设置时默认为空，不影响账号基本功能。 |

## DistributedAccountStatus10+

表示分布式账号状态枚举。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_LOGGED\_IN | 0 | 未登录状态。 |
| LOGGED\_IN | 1 | 已登录状态。 |
