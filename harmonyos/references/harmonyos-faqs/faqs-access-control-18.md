---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-18
title: 系统中关闭已开启的权限，应用被重启
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 系统中关闭已开启的权限，应用被重启
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f4bfe1ae875d631d672b850f6b25b03950bfe4625376633bfc86dfc7c71f28a7
---

## 问题现象

在应用中请求相机、位置等系统相关权限，然后跳转到应用的权限设置页面，先打开权限，然后再关闭权限，应用会重启。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/w5kHBwpDS8yFBtjk_HEGbg/zh-cn_image_0000002658967681.gif "点击放大")

## 背景知识

* 当前系统规格是权限移除（也就是权限从允许到拒绝），会重启进程。
* 如果在进行此操作的同时，于module.json5配置文件中配置removeMissionAfterTerminate参数的值为true，会从任务列表中移除任务，详情可参考[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)。
* 关闭权限应用退出时，不会触发[onWindowStageDestroy](../harmonyos-guides/uiability-lifecycle.md#onwindowstagedestroy)和[onDestroy](../harmonyos-guides/uiability-lifecycle.md#ondestroy)回调。

## 解决方案

权限移除（即权限从允许到拒绝）后，应用会按照当前系统规格重启，无法避免。如果希望在执行此操作后，在最近任务列表中保存应用快照（即仅重启），则无需配置removeMissionAfterTerminate字段，或者将其设置为false。
