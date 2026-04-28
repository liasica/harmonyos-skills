---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-auth-lock-state-capabilities
title: 查询指定认证类型的认证冻结状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:638f33a8a6f42afdbbedf7bceb96f2e629b2b2fde78fa51e1ea019158e893cc1
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

```
1. async obtainingAuthLockState() : Promise<string> {
2. try {
3. Logger.info(`get auth lock state start`);
4. const authLockState : userAuth.AuthLockState = await userAuth.getAuthLockState(userAuth.UserAuthType.PIN);
5. if (authLockState.lockoutDuration === userAuth.PERMANENT_LOCKOUT_DURATION) {
6. Logger.info('the authentication of given authType is permanent locked');
7. }
8. const authLockStateContent : string = JSON.stringify(authLockState);
9. Logger.info('get auth lock state successfully');
10. return authLockStateContent;
11. } catch (error) {
12. const errorMessage : string = `get auth lock state failed, err code is : ${error?.code}, err message is : ${error?.message}`;
13. Logger.error(errorMessage);
14. return errorMessage;
15. }
16. }
```

## 示例代码

* [查询指定认证类型的认证冻结状态](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
