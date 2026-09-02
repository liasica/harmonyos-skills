---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-36
title: 应用更新无法拉起升级对话框
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用更新无法拉起升级对话框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:0e175336b5390f689280c681913a3f7824bff0855d07e2a94060e364c77532f3
---

## 问题现象

使用应用市场提供的更新功能测试版本升级检测时，一直无法拉起升级对话框，报错updateAvailable:0。

## 背景知识

* 应用市场更新功能为开发者提供版本检测、显示更新提醒功能。开发者使用应用市场更新功能可以提醒用户及时更新到最新版本。
* 应用市场提供了[checkAppUpdate](../harmonyos-guides/store-update.md#接口说明)接口用于新版本检测，[showUpdateDialog](../harmonyos-guides/store-update.md#接口说明)接口用于显示升级对话框。

## 问题定位

1. 按照流程，先检查checkAppUpdate接口返回，updateAvailable一直是0，代表没有检查出来新版本。
2. 查看本地调试版本号是否低于在架版本，版本是否能升级取决于versionCode，配置在app.json5中，如下versionCode为1000000：

   ```json
      {
     "app": {
       "bundleName": "com.example.huawei",
       "vendor": "example",
       "versionCode": 1000000,
       "versionName": "1.0.0",
       "icon": "$media:layered_image",
       "label": "$string:app_name"
     }
   }
   ```
3. 如果本地版本确实低于在架版本，则需要抓取hilog进行分析，搜索"app invalid"查看报错信息，如下报错，显示本地调试应用的appid和在架版本不一致，这就是问题原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/wBFmMmuxSuGA-8vx-XF9jg/zh-cn_image_0000002705154589.png "点击放大")

## 分析结论

应用升级失败的根本原因是本地调试应用的appid和在架版本appid不一致，很有可能是本地调试应用使用了自动签名导致的。

## 修改建议

应用更新需要满足本地调试应用的appid和在架版本一致，不要使用自动签名调试，需要使用手动签名，保证签名的profile文件中的appid和在架版本一致。

## 常见FAQ

Q：应用升级需要满足哪些基本条件？

A：需要满足两个条件：

* 测试版本versionCode小于在架版本的versionCode。
* 测试版本的appid和在架版本appid一致。

Q：versionCode和versionName是什么关系，升级看哪个字段？

A：控制版本能否升级的字段是versionCode，是正整数，如1001；对外展示的版本号是versionName，如1.0.1。

Q：应用发布新版本后用户手机如何更新？

A：静默更新：在满足WIFI、闲时（代指设备状态，非凌晨的概念）和自动更新开关开启三个前置条件下触发更新，一般隔天更新。

Q：发布证书不支持本地测试时，如何调试应用市场更新功能？

A：可以先上架一个不含更新功能的版本，后续再使用调测证书本地调测更新功能。本地安装版本和应用市场在架版本签名信息保持一致，只需要保证[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（对应AGC上应用的App ID，应用的唯一标识）任一相同即可。
