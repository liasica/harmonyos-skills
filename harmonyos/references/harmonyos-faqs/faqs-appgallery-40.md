---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-40
title: AGC上架时如何指定应用版本号
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC上架时如何指定应用版本号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:57c759ecc67434f0a7a570f619dd08a00e06ac1f475a19c071e114e0748d242d
---

## 问题现象

AGC上架时应该怎样实现指定应用版本号？

## 背景知识

* [发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)：完成HarmonyOS应用开发、调试与测试后，开发者即可在AGC正式提交应用上架申请。HarmonyOS应用审核通过上架后，用户可在华为应用市场搜索到该HarmonyOS应用。发布应用时需要配置应用信息、上传软件包、配置版本信息等操作。
* [维护应用](../app/agc-help-maintain-0000002270829401.md)：包括[更新应用信息](../app/agc-help-maintain-update-0000002271413697.md)、[升级版本](../app/agc-help-maintain-upgrade-0000002236494386.md)、[回退版本](../app/agc-help-maintain-rollback-0000002236334578.md)、[分阶段发布](../app/agc-help-maintain-phased-release-0000002271493785.md)、[分阶段发布（7天内自动更新）](../app/agc-help-maintain-phased-release-7day-0000002279615726.md)、关联其他平台应用、[下架应用/元服务](../app/agc-help-maintain-remove-0000002274058145.md)、[删除应用/元服务](../app/agc-help-maintain-delete-0000002271413701.md)、[查看版本历史记录](../app/agc-help-maintain-version-history-0000002236334582.md)等九种使用场景。
* 应用版本信息在工程包的配置文件中声明，具体可参考[应用配置文件概述（Stage模型）](../harmonyos-guides/application-configuration-file-overview-stage.md)。

## 解决方案

在HarmonyOS开发中，应用版本号的起点通常是从1.0.0开始。这是因为从1.0.0作为起始版本号可以帮助开发者明确标识应用的初始发布版本。在后续的版本更新中，版本号可以根据需要增加，以反映新的功能添加、性能优化或bug修复。

上架时，指定应用版本会在上传的软件包中自动解析，对应工程中的app.json5中的versionCode和versionName字段。AGC操作界面上的版本对应versionName，版本号对应versionCode。打包升级前可以手动修改工程的versionCode，必须大于等于在架版本的versionCode，最小步长为1，应用市场显示的是versionName。

## 常见FAQ

Q：app.json5里的versionCode有没有什么限制？

A：versionCode是标识应用的版本号，取值为小于2^31次方的正整数。此数字仅用于确定某个版本是否比另一个版本更新，数值越大表示版本越高，开发者可以将该值设置为任何正整数。

Q：应用首次上架，版本号是否必须从1.0.0开始，能否从其他更高版本开始？

A：是可以的。上架时并没有指定版本号，版本号是在上传的软件包中自动解析的，对应工程中的app.json5中的versionCode和versionName字段。AGC操作界面上的版本对应versionName，版本号对应versionCode。

Q：应用提交新版本时，自动跳转到应用信息页面，应用信息页面提示需要提交新版本才可以更新，导致来回跳转，是什么原因？

A：跳转回应用信息页面是由于没有修改应用信息，直接点击了确认，导致反复跳转，需确保当前提交版本应用信息已正常修改后再确认提交。

Q：应用上架提示HarmonyOS NEXT版本应用要求Compatible SDK 4.0.0（10）以上版本，但是compatibleSdkVersion已经设置了5.0.0(12)是高于4.0.0（10）版本的，为什么还会报此提示？

A：如果开发者在4.0.0（10）以下版本已有相同包名的应用，需先下架并删除原有应用，再使用新的包名重新创建并上架新应用。否则检测到了相同包名的4.0.0（10）以下版本应用，就会提示如上。

Q：应用上架是否可以保持versionName不变？

A：可以的，应用市场展示的版本对应versionName，无强制变更要求，开发者可根据需求决定是否修改versionName，即使功能更新，也可保持versionName不变。为了给用户提供良好的体验，建议升级应用时递增修改软件包的versionName。

Q：应用上架是否可以保持versionCode不变？

A：可以的，应用市场展示的版本号对应versionCode，versionCode是控制版本升级的核心字段，需确保上传的软件包versionCode不低于当前在架版本的versionCode。如果新版本软件包的versionCode和当前在架版本的versionCode相同，已安装相同版本号的用户将无法升级到此版本，建议升级应用时递增修改软件包的versionCode。
