---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-14
title: 如何解决应用向用户索取权限使用目的说明不明确等问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何解决应用向用户索取权限使用目的说明不明确等问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c8fabfaee2f5470b47bdad550a25c6c50a2c549159964803f0b47881bd4e479a
---

## 问题现象

应用审核被驳回，驳回意见如下：“应用在运行时，向用户索取（位置）等权限，权限申请的使用目的说明不明确、不准确，不符合相关法律法规要求，参考：[应用审核指南-用户隐私](../app/50104.md#section599875815368)”。

## 解决方案

当前案例中，应用需要向用户索取位置权限，基于当前用户位置，展示距离用户最近的银行网点。

参考：[APP常见个人信息保护问题FAQ-权限索取行为-未同步告知权限申请的目的](../app/faq-05.md#section14527552182911)。

* 修改前，向用户索取位置权限时，没有说明权限申请的使用目的，仅说明“获取地理位置信息”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Z086li_RQT-zYKTPHyakBg/zh-cn_image_0000002628394580.png "点击放大")
* 修改后，向用户索取位置权限时，说明“查询附近网点，显示当前位置等功能需要访问您的定位权限，请允许授权后体验更多功能”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/N-SnrOfaT7iQCqfy78fFIA/zh-cn_image_0000002628554470.png "点击放大")

应用需要在module.json5配置文件的requestPermissions标签中声明reason属性，对应上图权限申请的使用目的：

参考：[应用权限管控-申请应用权限-声明权限-声明样例](../harmonyos-guides/declare-permissions.md#声明样例)。

## 总结

1. APP在申请敏感权限时，应同步说明权限申请的使用目的，包括但不限于申请权限的名称、服务的具体功能、用途。
2. 告知方式不限于弹窗、蒙层、浮窗、或者自定义操作系统权限弹框等，且权限申请使用目的说明不应自动消失。
3. 排查应用内所有的权限申请行为，确保不存在类似问题。
