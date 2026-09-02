---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-38
title: 应用市场评论互动服务账号使用问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用市场评论互动服务账号使用问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4576cf937997b0780b42438d42910222698b9746ec5fa97947ecb8ad5b49afa9
---

## 问题现象

在使用[应用推广引擎-用户互动](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/accountList)进行用户评论管理时，登录账号有角色权限问题，如何注册使用正确的账号。

## 背景知识

应用推广引擎-用户互动平台可用于查看、回复和导出用户评论，以更好地了解用户的意见，进一步处理用户反馈和分析数据，持续优化应用体验。

## 解决方案

* 账号持有者登录：

  应用市场应用评论评分能力，已完成升级。您可以通过[华为应用市场评论互动服务](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/home)查看及管理应用评论评分。在访问之前请务必确认您的登录账号为持有者账号（即在AGC上【开发者ID】关联账号，【角色管理】为“账号持有者”）。
* 注册账号持有者：

  如您【角色管理】为空，您可以先[注册为账号持有者](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/home)。首次登录时，将会自动识别登录账号为账号持有者并完成注册。当您查看右上角登录信息，账号显示【主账号】则代表已注册完成。您可以直接在平台内通过用户互动服务查看和管理评论评分。
* 团队成员登录：

  如您角色管理为团队成员，您可以先联系应用关联的账号持有者，[登录平台](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/home)通过【账号管理】对团队成员进行授权。授权完成后，其他团队成员可登录平台使用评论评分能力。

## 常见FAQ

Q：是否有提供API接口供三方调用获取评论信息来做评论聚合平台？

A：可以通过[Comments API](../AppGallery-connect-References/agcapi-commentapi-0000001115868340.md)开放的接口来获取评论相关信息和回复评论。
