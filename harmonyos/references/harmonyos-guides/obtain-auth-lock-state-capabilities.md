---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-auth-lock-state-capabilities
title: 查询指定认证类型的认证冻结状态
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 查询指定认证类型的认证冻结状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:facb6627cddd1dfd29212b372fb29fd6df3b6d26fbf2d70e367d971c631c45ea
---

从API version 22开始，开发者可以参考下述开发指导，查询指定认证类型的认证冻结状态，以及剩余可认证次数或还需等待的认证冻结时间。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[userAuth.getAuthLockState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetauthlockstate22)。

| 接口名称 | 功能描述 |
| --- | --- |
| getAuthLockState(authType: UserAuthType): Promise<AuthLockState> | 根据指定的认证类型，查询认证冻结状态，用于判断是否可以发起认证。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定认证类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)），并调用[getAuthLockState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetauthlockstate22)接口查询指定认证类型的认证冻结状态。

以查询PIN认证类型的认证冻结状态为例：

```typescript
async obtainingAuthLockState() : Promise<string> {
  try {
    Logger.info(`get auth lock state start`);
    const authLockState : userAuth.AuthLockState = await userAuth.getAuthLockState(userAuth.UserAuthType.PIN);
    if (authLockState.lockoutDuration === userAuth.PERMANENT_LOCKOUT_DURATION) {
      Logger.info('the authentication of given authType is permanent locked.');
    }
    const authLockStateContent : string = JSON.stringify(authLockState);
    Logger.info('get auth lock state successfully.');
    return authLockStateContent;
  } catch (error) {
    const errorMessage : string = `get auth lock state failed, err code is : ${error?.code}, err message is : ${error?.message}`;
    Logger.error(errorMessage);
    return errorMessage;
  }
}
```

## 示例代码

* [查询指定认证类型的认证冻结状态](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)
