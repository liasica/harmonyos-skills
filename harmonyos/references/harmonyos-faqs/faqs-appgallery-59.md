---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-59
title: 应用在不同系统版本下应用市场的下载规则
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用在不同系统版本下应用市场的下载规则
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:fd03e0b7da3fba336af0193fb09de9f2163b535bdf4f791f18f7833905665ff6
---

## 问题现象

如果应用的HarmonyOS NEXT版本上架了，华为应用市场非NEXT的系统下载的还是其他平台的版本吗，只有搭载HarmonyOS NEXT手机才会下载新上架的HarmonyOS NEXT版？

## 解决方案

华为应用市场会根据设备系统类型自动分发对应版本。HarmonyOS5.0+设备仅能下载HarmonyOS版；HarmonyOS4.3及以下设备默认下载其他平台版（若存在）；若应用仅适配HarmonyOS版，则低版本系统设备会提示不兼容。开发者需通过HarmonyOS 开发者中心分别管理不同版本的分发策略。
