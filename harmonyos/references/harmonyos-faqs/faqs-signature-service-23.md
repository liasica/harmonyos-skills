---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-23
title: 安装应用时提示“安装失败，请重试”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 安装应用时提示“安装失败，请重试”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21894cd8b554a84a2e9690f81acbb757c905b9e7cbad37a016dbcc12f39f02a8
---

## 问题现象

通过应用市场下载安装应用时，提示“安装失败，请重试”该如何解决？

## 背景知识

* [调试证书](../harmonyos-guides/ide-signing.md#section081822416419)：用于应用/元服务调试场景。
* [发布证书](../harmonyos-guides/ide-publish-app.md#section178461193713)：发布证书用于应用/元服务发布的场景。当发布应用/元服务至华为应用市场时，需要申请、下载发布证书，用于后续打包正式发布包。

## 解决方案

导致安装失败的原因是本地存在包名相同但是签名信息不同的应用，常见场景就是本地安装了签名是调试证书（包括自动签名）的应用，把这个应用卸载掉再在应用市场重新下载安装即可。

## 常见FAQ

Q：已经卸载了调试应用，安装时还是报同样错误是为什么？

A：需要确认一下本机是否开启了隐私空间存在多个用户，确认后把每个用户下面同包名应用卸载掉。
