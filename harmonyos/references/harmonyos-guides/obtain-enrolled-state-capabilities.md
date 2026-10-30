---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-enrolled-state-capabilities
title: 查询用户注册凭据的状态
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 查询用户注册凭据的状态
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:19+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:5fd55616952da343e362f84a22d7f8439089a47e451648fb006282642840a909
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

* 可参考[用户认证服务](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)示例代码。
