---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-new-00002
title: 企业屏保检查及锁屏壁纸设置实现方式
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 企业屏保检查及锁屏壁纸设置实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:9e9c87e9752fb384367da495afdb75602581eeacb3b23a0a2df50b677e56dbdf
---

## 问题现象

终端是否支持检查屏保是否符合要求，对比企业屏保要求？

## 背景知识

在企业MDM（移动设备管理）场景中，通常需要通过后台统一下发壁纸文件，确保终端展示一致的内容。HarmonyOS提供了设备设置相关的接口，用于管理锁屏壁纸等系统配置。

## 解决方案

当前系统不提供独立的“屏保”概念，设置屏保文件即设置锁屏下的壁纸。可以通过MDM提供的[deviceSettings.setUnlockWallpaper](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetunlockwallpaper20)接口设置锁屏壁纸，实现统一屏保内容的下发。
