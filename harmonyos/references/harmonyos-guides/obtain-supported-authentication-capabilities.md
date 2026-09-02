---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-authentication-capabilities
title: 查询支持的认证能力
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 查询支持的认证能力
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bfc083606427635c3f6a37b8dbf736e8525e380ddec0d87beb31d39559edf078
---

不同的设备对于认证能力（人脸、指纹、口令）的支持性各有差异，开发者在发起认证前应当先查询当前设备支持的用户认证能力。

## 接口说明

具体参数、返回值、错误码等描述，请参考对应的[userAuth.getAvailableStatus](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetavailablestatus9)。

| 接口名称 | 功能描述 |
| --- | --- |
| getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void | 根据指定的认证类型、认证等级，检测当前设备是否支持相应的认证能力。 |

## 开发步骤

1. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
2. 指定认证类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)）和认证等级（[AuthTrustLevel](../harmonyos-references/js-apis-useriam-userauth.md#authtrustlevel8)），调用[getAvailableStatus](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetavailablestatus9)接口查询当前的设备是否支持相应的认证能力。

   认证可信等级的详细介绍请参见[认证可信等级划分原则](user-authentication-overview.md#生物认证可信等级划分原则)。

以查询设备是否支持认证可信等级≥ATL3的人脸认证功能为例：

```typescript
obtainingSupported() {
  try {
    // 查询认证能力是否支持
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
    Logger.info('current auth trust level is supported.');
    return true;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`current auth trust level is not supported, code is ${err?.code}, message is ${err?.message}`);
    return false;
  }
}
```

## 示例代码

* [查询支持的认证能力](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/UserAuthentication)
