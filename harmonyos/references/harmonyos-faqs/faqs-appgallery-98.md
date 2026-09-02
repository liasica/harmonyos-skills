---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-98
title: 应用内检查更新实现及常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用内检查更新实现及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d2c8f191deb4277b35b95297f6a6df4d4e0e54a889e6629103adba13f432686f
---

## 问题现象

应用上架应用市场后，有新的版本更新时，如何实现老版本用户打开应用能提示更新版本？

## 背景知识

[应用市场更新功能](../harmonyos-guides/store-update.md)为开发者提供版本检测、显示更新提醒功能。开发者使用应用市场更新功能可以提醒用户及时更新到最新版本。

当应用启动完成或用户在应用中主动检查应用新版本时，开发者可以通过本服务，来查询应用是否有可更新的版本。如果存在可更新版本，可以通过本服务为用户弹窗显示更新提醒。

## 解决方案

* 业务流程：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/orJwstqxRhSfwgPMnXNrlQ/zh-cn_image_0000002653977984.png "点击放大")

  1. 应用调用检查更新接口。
  2. 升级服务API返回是否有新版本。
  3. 调用显示升级对话框接口。
  4. 升级服务API向应用返回显示结果。
* 核心接口有[updateManager.checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)和[updateManager.showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)，功能描述如下：
  + checkAppUpdate：检查更新接口，用于检测当前是否有新版本。
  + showUpdateDialog：显示升级对话框接口，用于提示用户进行升级。
* 开发步骤：
  + 调用checkAppUpdate[检测应用新版本](../harmonyos-guides/store-update.md#检测应用新版本)。

    **须知** 

    注意：

    本地安装版本须低于应用市场在架版本才能检查到更新。

    本地安装版本须和应用市场在架版本签名信息保持一致。

    暂不支持邀请测试和公开测试。
  + 调用showUpdateDialog[显示升级对话框](../harmonyos-guides/store-update.md#显示升级对话框)。

    **须知** 

    注意：

    调用showUpdateDialog需要在执行checkAppUpdate后进行，不能单独执行showUpdateDialog，否则即使应用市场有新版本也无法显示升级框。

## 常见FAQ

Q：应用升级版本号如何定义，是通过versionName还是versionCode来控制的？

A：要实现升级弹窗，更新版本versionCode必须大于老版本versionCode，versionName不做要求。

Q：能否使用邀请测试实现检查更新和升级弹窗功能？

A：暂不支持邀请测试和公开测试，使用邀请测试接口会返回[1009400001 服务异常](../harmonyos-references/errorcode-appgallery.md#section1009400001-服务异常)。需要先正式上架版本才能测试。

Q：是否支持模拟器测试？

A：暂不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。详情可参考[约束与限制](../harmonyos-guides/store-update.md#约束与限制)。

Q：本地安装版本和应用市场在架版本签名保持一致怎么理解？

A：应用升级需要进行[签名证书一致性校验](../harmonyos-guides/install-and-update-consistency-verification.md#签名证书一致性校验)和[配置文件一致性校验](../harmonyos-guides/install-and-update-consistency-verification.md#配置文件一致性校验)。只需要保证[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（对应AGC上应用的APP ID，应用的唯一标识）任一相同即可满足签名信息保持一致。

Q：是否支持强制升级（不升级无法进入应用）？

A：开发者可以自行实现强制更新，通过checkAppUpdate判断用户版本是否需要更新，根据返回的CheckUpdateResult的值来判断是否有新版本，从而可弹窗拉起应用市场的应用详情页更新。

Q：升级弹窗是否能自定义？

A：不可以，检测到有新版本需要更新后，系统弹窗的版本信息和更新说明来源于应用市场客户端应用详情页数据。如果需要修改，需要在上架版本时AGC页面更新。详情可参考[升级版本。](../app/agc-help-maintain-upgrade-0000002236494386.md)

Q：判断版本升级的接口checkAppUpdate是根据versionName还是versionCode来判断的？

A：通过versionCode来判断的。

Q：为什么调用checkAppUpdate接口[UpdateAvailableCode](../harmonyos-references/store-updatemanager.md#updateavailablecode)返回结果为-1？

A：应用只有上架过应用市场，checkAppUpdate接口才能正常返回0或1；如果从来没用上架过应用市场，就返回-1。

Q：非公开上架的应用是否可以用接口updateManager.checkAppUpdate检查到更新？

A：接口updateManager.checkAppUpdate可以用来检查非公开发布应用的版本更新。

Q：自动签名在真机上运行的工程，检查更新一直返回不需要更新。

A：使用自动签名无法满足签名信息和在架版本保持一致，因此无法测试。需要使用调试证书签名。

Q：checkAppUpdate和showUpdateDialog是否支持智慧屏类型的应用？

A：对于API 19之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用；对于API 20及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

Q：In-house发布的应用是否可以支持升级？

A：In-house应用未上架应用市场，调用升级检测接口会报错。In-house应用可以通过[openlink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)的方式去进行应用升级，该方式不会拉起浏览器，会直接拉起企业模块的下载能力，升级场景下可以在应用内直接触发Deeplink。openlink配置地址的就是Deeplink链接，详情可参考[构建Deeplink实现下载应用](../app/agc-help-inhouse-0000002281532696.md#section74503017418)。

Q：应用市场更新应用时是否会触发卸载安装应用？

A：在应用市场更新应用时，不会触发完整的卸载再安装流程，而是采用覆盖安装的方式实现应用更新。

Q：未上架应用如何调试应用市场更新功能？

A：得先正式上架一个不带更新弹窗功能的版本，版本号versionCode设得大于1000000。之后就可以用调测证书，在本地开发环境里，直接调试升级跳转应用市场的功能。可以参考[应用市场更新功能](../harmonyos-guides/store-update.md)。

Q：CheckUpdateResult能否新增字段，用于判断已安装的历史版本是否需要强制更新到最新版本？

A：当前CheckUpdateResult不支持新增字段用于判断是否需要强制更新。建议在应用服务端维护一个"最低允许版本号"或"强制更新版本列表"，应用启动时调用服务端接口获取当前最低允许版本，将本地versionCode与服务端返回的版本号对比，若本地版本过低，则通过[showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)或拉起应用市场详情页，并阻止用户继续使用旧版。
