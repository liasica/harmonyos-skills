---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-7
title: 碰一碰分享提示暂无可用打开方式
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 碰一碰分享提示暂无可用打开方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:121402d76bbb9dffdf160da5af1087406fe8436c8016743a346fbe92ce07630d
---

## 问题现象

使用碰一碰进行内容分享，一直提示暂无可用打开方式，如何排查？

## 背景知识

* HarmonyOS提供了[Share Kit（分享服务）](../harmonyos-guides/share-introduction.md)，并结合[App Linking](../harmonyos-guides/applinking-introduction.md)技术，可实现内容的快速跨设备分享，直达目标应用，无需依赖第三方应用中转，提供高效、便捷、无缝的分享体验。
* 目标应用可以通过[ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md)构建接收分享内容的分享详情页，并将应用显示到分享面板应用推荐区内，通过分享详情页便捷的处理分享内容。开发时需要接入方实现ShareExtensionAbility并于module.json5中注册支持分享内容的能力。

## 解决方案

碰一碰分享提示暂无可用打开方式，可排查以下情况是否满足：

* 手机应用发起碰一碰分享时，双端设备需要在亮屏、解锁的状态下并且都已开启华为分享服务（系统默认开启），设备顶部轻碰即可触发。
* 当前支持手机与手机、手机与PC/2in1碰一碰分享，且手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 集成开发环境：DevEco Studio NEXT Beta1及以上版本。
* 支持的手机系统：HarmonyOS NEXT Release及以上版本。可使用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)进行判断：canIUse('SystemCapability.Collaboration.HarmonyShare')。
* 使用碰一碰进行应用间跳转，不能使用DevEco Studio的自动签名功能，必须使用手动签名，否则无法拉起应用。详情参考[验证应用被拉起效果](../harmonyos-guides/app-startup-overview.md)。
* 构建完分享能力Ability，需要在应用配置文件（src/main/module.json5）的skills配置中注册。配置actions为ohos.want.action.sendData，并且uris需穷举所有支持的数据类型。详情参考[分享详情页处理分享内容](../harmonyos-guides/share-sec-panel.md)。

## 常见FAQ

Q：应用内是否可以模仿“游戏组队”通过碰一碰直接实现数据互传，不拉起分享界面等任何碰一碰的界面。

A：组队功能也是需要设置预览界面的，并非不需要设置预览分享卡片界面，参考文档：[设置组队邀请预览](../harmonyos-guides/knock-share-between-phones-group.md#设置组队邀请预览)。
