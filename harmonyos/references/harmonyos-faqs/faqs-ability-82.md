---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-82
title: 有了代码签名特性后，开发者的so文件在调试、发布等阶段该如何部署
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 有了代码签名特性后，开发者的so文件在调试、发布等阶段该如何部署
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:49+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:8849daa982defa2f9c4679f03478c4bd0a1ef6f62764bc57a9fd1942baa6122a
---

安全原则：HarmonyOS NEXT版本已部署强制代码签名机制。所有上架应用市场和开发者调试的应用，必须使用合法证书对代码文件进行签名，才能在设备端正常执行。直接推送到设备端的so文件，如果签名不合法，将被系统拦截，导致加载失败。

针对开发者so文件的部署：

* 发布阶段，普通三方应用的所有so文件需打包在应用HAP包内，随应用一同上架应用市场并进行强制代码签名。通过热更新下载的so文件因缺乏合法签名会被系统拦截。
* 调试阶段，在开发态下，HAP文件及包内的so文件使用开发者证书进行代码签名，并在安装时由包管理完成签名使能。最新的DevEco Studio提供热重载功能，支持将代码文件（包括so文件等）快速推送到设备端安装并签名使能。DevEco Studio支持将项目目录内新增或修改的代码文件打包到hqf包，使用开发者证书对包进行签名，然后通过HDC推送到设备侧，最后通过包管理触发HQF的安装及签名使能，完成新代码文件的端侧部署。
