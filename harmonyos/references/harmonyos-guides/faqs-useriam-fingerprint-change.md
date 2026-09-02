---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-useriam-fingerprint-change
title: 指纹登录怎么检测设备指纹是否发生变化
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > User Authentication Kit常见问题 > 指纹登录怎么检测设备指纹是否发生变化
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:a28595deeb9e460b5ae318ab326af52c6e76cb8d48f8bc9683f19183f3229434
---

## 问题现象

出于安全风险管控需求，当设备指纹信息发生变更时，系统需禁用指纹登录功能。本文将介绍如何检测指纹变更。

## 背景知识

* [UserAuthenticationKit（用户认证服务）](user-authentication-overview.md)提供了基于用户在设备本地注册的锁屏口令、人脸和指纹来认证用户身份的能力。
* [userAuth.getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口提供查询凭据注册状态的能力，其返回值[EnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#enrolledstate12)表示用户注册凭据的状态。结构如下：

  | 名称 | 类型 | 说明 |
  | --- | --- | --- |
  | credentialDigest | number | 注册的凭据摘要，在凭据增加时随机生成。 |
  | credentialCount | number | 注册的凭据数量。 |

## 解决方案

1. 业务在首次开通指纹登录时，指定了认证类型（[UserAuthType](../harmonyos-references/js-apis-useriam-userauth.md#userauthtype8)），调用[getEnrolledState](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口查询用户凭据的状态，并将该状态储存。
2. 当调用者需要感知用户凭据变化时，取出上次存储的凭据状态，与当前调用getEnrolledState接口获取的用户注册凭据状态做对比。若不同则说明指纹发生变更，处理完成后更新存储凭据状态覆盖原状态。凭据状态对比规则如下：

   * credentialDigest和credentialCount均相同，说明本机指纹未发生变化。
   * credentialDigest不同，无论credentialCount是否相同，说明本机指纹有新增或变更。
   * credentialDigest不变，credentialCount减小，说明本机指纹有删除。

用户认证完整代码示例请参考用户身份认证[开发步骤](start-authentication.md#开发步骤)。
