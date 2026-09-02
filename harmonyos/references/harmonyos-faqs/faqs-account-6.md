---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-6
title: HarmonyOS账号登录的OpenID和UnionID使用说明
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > HarmonyOS账号登录的OpenID和UnionID使用说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:0abb06fa2dbda876a230708b6988e04b7c968d59301a37546fe2edb05cd47b59
---

## 问题现象

**场景一**：华为账号登录流程中服务端需要存什么凭据，使用什么字段作为唯一标识？

**场景二**：HarmonyOS 4.3及以下版本授权登录使用的是OpenID作为唯一标识，HarmonyOS 5及以上版本设备下获取到的OpenID和之前的不一样。

**场景三**：HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本获取的OpenID不相同，UnionID相同，如何通过用户OpenID获取UnionID？

**场景四**：用户更换绑定华为账号的手机号码，华为账号一键登录返回的UnionID是否会变？

**场景五**：应用在主体迁移后，UnionID是否会改变？

## 解决方案

**场景一：**

华为账号登录会向服务端返回UnionID 、OpenID 、authorization Code 、ID token，建议都存储，其中UnionID、OpenID是唯一标识。参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。

* 开发者账号下管理了多个应用时，针对同一个华为账号，不同的应用返回的OpenID值不同，但返回的UnionID相同，所以建议使用OpenID来作为唯一ID。
* 如果开发者账号下管理了多个应用，并且这些应用需要共享同一个华为账号的用户信息，可以使用UnionID作为用户标识。

**场景二：**

1. HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本获取的OpenID确实不相同，首先用户OpenID的生成规则是：由用户账号和应用ID加密生成的；在这个基础上HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本的应用ID是不相同的，所以获取的OpenID是不同的。
2. 推荐使用UnionID，其生成规则是：由用户账号和应用开发者账号签名而成，如果开发者账号下管理了多个应用，并且这些应用需要共享同一个华为账号的用户信息，可以使用UnionID作为用户标识。

**场景三：**

可调用REST API接口[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。

**场景四：**

用户更换绑定华为账号的手机号码，华为账号一键登录返回的UnionID不会变，可以作为用户的唯一标识。

**场景五：**

UnionID是同一个开发者账号下的用户唯一标识，当应用转移到另外一个账号主体后，UnionID值也会变化。参考[UnionID介绍](../HMSCore-Guides/unionid-introduction-0000001125697651.md)。
