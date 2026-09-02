---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-3
title: 指纹登录怎么检测设备指纹是否发生变化
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 指纹登录怎么检测设备指纹是否发生变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a01498553f646e2115ba77c7436b01edd8054cd8b46c7ead07cdb1f5d2609c6c
---

## 问题现象

出于安全考虑，指纹登录功能在指纹发生变化时要禁止使用，怎么才能检测指纹的变化？

## 背景知识

* [UserAuthenticationKit（用户认证服务）](../harmonyos-guides/user-authentication-overview.md)提供了基于用户在设备本地注册的锁屏口令、人脸和指纹来认证用户身份的能力。
* [userAuth.getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)：查询凭据注册的状态。
* [EnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#enrolledstate12)：userAuth.getEnrolledState接口的返回值，表示用户注册凭据的状态。结构如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| credentialDigest | number | 注册的凭据摘要，在凭据增加时随机生成。 |
| credentialCount | number | 注册的凭据数量。 |

## 解决方案

1. 首次使用指纹登录时，指定认证类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)），调用[getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口查询用户注册凭据的状态，并将该状态储存。
2. 当调用者需要感知用户凭据变化时，取出上次存储的凭据状态，与调用getEnrolledState接口获取状态做对比，若不同则说明指纹发生变更，处理完成后更新存储凭据状态覆盖原状态。用户凭据含两个字段credentialDigest和credentialCount，凭据对比规则如下：
   * credentialDigest和credentialCount均相同，说明本机指纹未发生变化。
   * credentialDigest不同，无论credentialCount是否相同，说明本机指纹有新增或变更。
   * credentialDigest不变，credentialCount减小，说明本机指纹有删除。

用户认证完整代码示例请参考用户身份认证[开发步骤](../harmonyos-guides/start-authentication.md#开发步骤)。

## 常见FAQ

Q：[User Authentication Kit](../harmonyos-guides/user-authentication-kit.md)（用户认证服务）执行userIAM\_userAuth.getAvailableStatus(userIAM\_userAuth.UserAuthType.FACE, userIAM\_userAuth.AuthTrustLevel.ATL1)，提示凭据类型尚未注册，报错[12500010](../harmonyos-references/errorcode-useriam.md#section12500010-该类型的凭据没有录入)如何解决？

A：该错误码一般表示没有录入对应的认证信息。可以在userAuth模块的getAvailableStatus接口中检查是否录入了该类型的凭据。如果需要录入该类型的凭据，可以通过调用start接口发起人脸认证来完成。录入认证信息可以在【设置->生物识别和密码->生物识别打开对应类型的识别能力（指纹、人脸）】设置。

Q：[User Authentication Kit](../harmonyos-guides/user-authentication-kit.md)（用户认证服务）中的userAuth.UserAuthType.PIN仅支持切换密码校验（锁屏密码校验），不支持切换密码校验（输入的密码，通过云侧接口校验）

A：[User Authentication Kit](../harmonyos-guides/user-authentication-kit.md)（用户认证服务）是本地认证，不支持该能力。可以参考切换[自定义认证](../harmonyos-guides/apply-custom-authentication.md)。

Q：如何在指纹认证前就确认指纹是否发生变化？

A：在调用指纹前使用[getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口查询用户注册凭据的状态即可。
