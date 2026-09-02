---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-24
title: 多端适配场景下不同设备ACL权限分别配置的打包方案
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 多端适配场景下不同设备ACL权限分别配置的打包方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:b31934ac55edbc25eb19def09ab91bb85b014940eb69a610b83a2e5cb99a667c
---

## 问题现象

多端适配场景下，应用在平板和PC端需要使用JIT能力（需申请[ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY](../harmonyos-guides/restricted-permissions.md#ohospermissionkernelallow_writable_code_memory)权限），但手机端不支持JIT。若将平板/PC端和手机端分别打包为不同应用上架，可能因功能类似被审核拒绝。如何在同一个应用中实现不同设备类型配置不同ACL权限？

## 背景知识

ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY是受限开放权限，需要通过ACL权限申请流程获取。在多端适配场景下，可以通过同一个appID上传一个app包，在app包内为不同设备的hap包分别配置ACL权限，应用市场会根据设备类型推送对应的安装包。具体打包操作可参考[编译打包](../guidebook/develop-once-deploy-everwhere-4-4-0000002594673002.md#section991111189316)模块。

## 解决方案

按设备类型分别配置ACL权限。

通过同一个appID上传一个app包，在app包内为不同设备的hap包分别配置ACL权限，具体步骤如下：

1. 使用同一个appID创建应用，在app包中分别构建手机端hap包和平板/PC端hap包。
2. 手机端的hap包不配置ACL权限，平板和PC端的hap包配置ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY权限的ACL。
3. 在申请ACL权限时，说明权限使用场景，例如"手机与平板/PC使用不同包，该权限仅在平板/PC使用"。
4. 前端提交上架审核，应用市场会根据设备类型推送对应的安装包。
