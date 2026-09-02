---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-1
title: 智能体如何获取华为账号手机号
breadcrumb: FAQ > AI功能开发 > 计算平台 > 智能体框架（Agent Framework） > 智能体如何获取华为账号手机号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:302eee27c155d4784ddcfebf6c5edfeab6c7d0d99d35ccadcd742056cde54ea2
---

## 问题现象

智能体绑定了华为账号，如何通过华为账号获取到用户的手机号？

## 背景知识

* [Account Kit](../harmonyos-guides/account-introduction.md)（华为账号服务）提供简单、快速、安全的登录功能，让用户快捷地使用华为账号登录应用。用户授权后，Account Kit可提供头像、昵称、手机号码等信息，帮助应用更了解用户。
* Agent Framework Kit（智能体框架服务）提供了拉起指定智能体的能力。应用在[小艺开放平台](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/)上线智能体后，向用户提供应用+智能体组合的服务，让用户可以在适当的场景下通过Agent Framework Kit的UI控件能力主动拉起智能体。

## 解决方案

1. 在华为开发者联盟账号服务获取一个appId，并将appId在华为开发者联盟小艺开放平台智能体开发页面注册保存。
2. 小艺APP在加载三方智能体页面时会从小艺开放平台获取到智能体的appId。
3. 在使用三方智能体时，可以在智能体内点击账号授权，发起账号授权流程：
   * 首先，三方智能体服务器携带授权码向华为账号服务器获取用户Access Token，华为账号服务器返回用户Access Token给三方智能体服务器。
   * 然后，三方智能体服务器使用用户Access Token向华为账号服务器获取用户信息，华为账号服务器返回用户信息给三方智能体服务器。
   * 最后，解析出手机号。

   如果用户已经授权过，则静默发起授权流程到三方智能体服务器，三方智能体服务器返回新的账号登录会话标识符agentLoginSessionId；如果用户未授权过，则给用户弹框获取用户授权，三方智能体服务器基于华为账号分配的授权码获取用户手机号，然后返回新的agentLoginSessionId。
4. 小艺APP保存该智能体的agentLoginSessionId，后续用户给该智能体发消息时携带该字段给三方智能体服务器。
5. 小艺APP会在agentLoginSessionId超期失效或不存在时重新发起账号授权流程，从三方智能体服务器申请新的agentLoginSessionId。

华为账号信息获取参考[获取华为账号用户信息](../harmonyos-guides/account-get-user-info.md)。
