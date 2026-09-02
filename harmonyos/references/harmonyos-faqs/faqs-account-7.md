---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-7
title: 华为账号登录退出登录后路由栈清空问题
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号登录退出登录后路由栈清空问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:14e74fae4b3aa0cbd34f308e48b707462dfe408fdb89460d819ee69ca0ec4d82
---

## 问题现象

华为账号登录点击退出登录，调用logout接口清空Token，跳转登录页后，是否需要手动清空路由栈？当Token过期跳转至登录页时，是否也需要清空路由栈？

## 解决方案

当点击退出登录或Token过期跳转至登录页时都需要显式清空路由栈，HarmonyOS路由栈（通过NavDestination组件管理）默认不会自动清空历史页面，即使调用logout接口跳转到登录页，原栈中的页面实例（如多个首页）依然存在。

不清空路由栈，会导致以下问题。

* 内存泄漏：未销毁的页面持续占用资源。
* 接口重复调用：若栈中存在多个首页实例，每个实例的aboutToAppear生命周期都触发接口请求，导致多次调用（如用户遇到的首页接口请求数十次的问题）。
