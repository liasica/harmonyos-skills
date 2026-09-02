---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-enrolled-state-capabilities
title: 查询用户注册凭据的状态
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 查询用户注册凭据的状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f71c8efa2d32e2c3e1534e0a61a9294c29641a0d5053aaa2af8a933f7330759b
---

调用者需感知用户注册凭据（人脸、指纹、口令）的变化，可使用该接口查询当前用户注册凭据的状态。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[userAuth.getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)。

| 接口名称 | 功能描述 |
| --- | --- |
| getEnrolledState(authType : UserAuthType): EnrolledState | 根据指定的认证类型，查询用户注册凭据的状态，用于感知注册凭据变化。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定认证类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)），调用[getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口查询用户注册凭据的状态。

以查询用户人脸注册凭据的状态为例：

```typescript
obtainingEnrolledCredentialInformation() {
  try {
    let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
    Logger.info('get current enrolled state successfully.');
    return enrolledState.credentialDigest;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`get current enrolled state failed, code is ${err?.code}, message is ${err?.message}`);
    return false;
  }
}
```

## 示例代码

* [查询用户注册凭据的状态](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)
