---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-1
title: 华为分享将应用的页面分享到另一个手机后不能引导下载应用
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 华为分享将应用的页面分享到另一个手机后不能引导下载应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:2d64c18f7b07e5904a06c260c67811f52a3c09255264a87ecad2bbda0a373177
---

## 问题现象

应用内点击分享，可通过华为分享将页面链接分享到其他华为手机，但是在手机收到的就是一个链接文字，而且只有WPS能打开，并不能跳转应用市场下载该应用，从应用内打开页面，方便阅读。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/krC7A31lR9WAPPPminLUdQ/zh-cn_image_0000002628554414.png "点击放大")

## 背景知识

* [使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)：使用App Linking进行跳转时，系统会根据接口传入的uri信息（https链接）将用户引导至目标应用中的特定内容，无论应用是否已安装，用户都可以访问到链接对应的内容，跳转体验相比Deep Linking方式更加顺畅。
* [Share Kit](../harmonyos-guides/share-introduction.md)：Share Kit（分享服务）为应用提供文本、图片、视频等内容跨应用、跨端分享能力。应用把需要分享的内容和预览样式配置给Share Kit，Share Kit将根据不同的场景进行使用：
  + 针对应用间分享的场景，根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。
  + 针对跨端分享的场景，根据分享的数据类型、数量等信息构建预览界面，用于跨端分享。
* [User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)：UA是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。在Web开发中，这个字符串使服务器能够识别请求的来源设备及其特性，从而根据这些信息提供定制化的内容和服务。如果页面无法正确识别UA，可能会导致多种异常情况。

## 问题定位

* 对端设备接收到分享内容后，会得到一个txt文本，只有WPS能打开txt文件的原因可能是手机上除了WPS，未安装其他可以打开txt文件的应用。
* 打开文本里面只有一个https链接，该链接可以用浏览器打开。链接在手机上打开后不能直接跳转到应用市场中该应用的详情页，可能是分享的内容只是一个普通的H5页面。

## 分析结论

应用的分享功能只是分享一个包含网页链接的txt文本，并且H5页面User-Agent并没有适配HarmonyOS设备，也就无法识别并跳转应用市场。

## 修改建议

* 建议使用分享App Linking直达应用方式，目标设备接收后可直达应用。在配置App Linking服务后，宿主应用需要[通过分享面板发起分享](../harmonyos-guides/share-mobilephone-app-share.md)，目标应用在[应用内处理分享内容](../harmonyos-guides/share-interface-description.md)并跳转指定页面。
* [配置直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)：为提升用户未安装应用时的体验，可配置直达应用市场功能，引导用户下载安装应用。在AGC控制台的App Linking服务中，开启"直达应用市场"功能。配置完成后，当用户点击应用中分享的App Linking链接时，若设备未安装目标应用，系统将直接跳转至应用市场的应用详情页，支持一键下载安装。
* 当应用未安装且未配置直达应用市场时，系统会打开浏览器Web页面。Web页面可以通过UserAgent中的{OSName}和{OSVersion}字段[识别HarmonyOS系统及版本](../harmonyos-guides/web-default-useragent.md#如何通过user-agent来识别harmonyos操作系统中不同设备)，然后[跳转应用市场应用详情页](../harmonyos-guides/social-sharing-redirection.md#场景三目标应用未安装未配置直达应用市场有web页面)。
