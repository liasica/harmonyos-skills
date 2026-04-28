---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-quick-login-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51530fdf9f6dab9092e74f442286dd7475e0fc9ef0e84bd7f942a755ce646c24
---

Account Kit提供了[华为账号一键登录](account-phone-unionid-login.md)、[华为账号登录](account-unionid-login-button.md)、[静默登录](account-silent-login.md)等多种登录方式，其中华为账号一键登录**仅支持企业开发者**使用，华为账号登录和静默登录**既支持企业开发者也支持个人开发者**使用，应用可根据实际场景选择使用其中一种或多种方式进行账号登录。

## 基础概念

华为账号用户身份标识包含UnionID和OpenID，具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)，注意OpenID和UnionID严格区分大小写。两者的定义与使用场景：

| 项目/ID类型 | UnionID | OpenID |
| --- | --- | --- |
| 定义 | UnionID是华为账号用户同一开发者账号下的唯一标识。开发者有多个HarmonyOS应用时，同一个开发者账号下的HarmonyOS应用获取到用户的UnionID相同。 | OpenID是华为账号用户在HarmonyOS应用的唯一标识。不同HarmonyOS应用（不管是否在同一个开发者账号下）获取到用户的OpenID不同。 |
| 使用场景 | 在同一个开发者账号下标识用户的唯一性。**建议使用UnionID**。 | 在同一个应用下标识用户的唯一性。 |

说明

在开发HarmonyOS应用时，您需要考虑同一用户在非HarmonyOS应用和HarmonyOS应用的用户数据是否互通。如果您之前使用OpenID来关联用户数据，我们建议将用户数据关系切换成UnionID，以确保用户使用HarmonyOS应用后可以继承老版本的用户数据。具体切换指导可以参考：[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。

## 场景介绍

* **获取手机号和UnionID登录，即华为账号一键登录**

  若应用需要同时获取手机号和UnionID，推荐使用此场景，用户仅需一次点击操作，应用即可获取用户**手机号和UnionID**。应用获取到用户手机号和UnionID后，**可同时通过手机号和UnionID与应用原有用户体系进行关联**。本场景仅支持企业开发者使用，个人开发者请使用华为账号登录或静默登录方式。
* **华为账号登录**

  若应用只需要获取UnionID可以使用此场景。应用获取到用户UnionID后，**可通过UnionID与应用原有用户体系进行关联**。
* **静默登录**

  在应用卸载重装、用户换机等场景，应用可通过Account Kit提供的静默登录方式即不需要用户点击登录/注册按钮，即可获取用户的身份标识UnionID，完成用户的静默登录。
* **订阅华为账号登录/登出事件**

  当应用需要跟随华为账号的登录状态进行登录登出时，可以通过订阅华为账号的登录登出事件进行判断。
