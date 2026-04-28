---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-authentication-capabilities
title: 查询支持的认证能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e5d2844036ea6d087b252c40e60ac608a96bcd5bcdb0a84413f3332677f2b1a
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

```
1. obtainingSupported() {
2. try {
3. // 查询认证能力是否支持
4. userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
5. Logger.info('current auth trust level is supported');
6. return true;
7. } catch (error) {
8. const err: BusinessError = error as BusinessError;
9. Logger.error(`current auth trust level is not supported, code is ${err?.code}, message is ${err?.message}`);
10. return false;
11. }
12. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/UserAuthentication/entry/src/main/ets/pages/Index.ets#L99-L113)

## 示例代码

* [查询支持的认证能力](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
