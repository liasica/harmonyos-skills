---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-4
title: 应用配置图标不符合UX设计规范要求尺寸1024px*1024px该如何解决
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用配置图标不符合UX设计规范要求尺寸1024px*1024px该如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cdf0161f11690fbcf2675d412ca5e4a8c3a36ceec7ce4af3e600dc87a9efe9f
---

## 问题现象

应用审核过程中，会提示【应用未配置图标的前景图和后景图，标准要求尺寸1024px\*1024px且需下载使用最新版本HUAWEI DevEco Studio进行图标再处理】的问题，不符合UX设计规范。

## 背景知识

* [配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)：应用图标如果采用分层图标（包括前景图和背景图两层），可以参考本文档进行配置。图标规范详见[图标资源规范](../design-guides/application-icon-0000001953444009.md#section634668113212)。
* [配置优先级和生成策略](../harmonyos-guides/layered-image.md#配置优先级和生成策略)：图标和标签通常一起配置，对应app.json5配置文件和module.json5配置文件中的icon和label标签。系统将优先返回module.json5中的icon与label，如果在module.json5配置文件的abilities标签中未设置icon和label，系统将返回app.json5中的icon和label。
* 前景图背景图：在HarmonyOS应用开发中，前景图（Foreground）和背景图（Background）是应用图标的分层设计概念，用于满足UX设计规范中的视觉一致性要求。

  **前景图**：通常是应用图标的主体部分，例如应用的主要图形、Logo或文字，需为透明的PNG格式。

  **背景图**：作为背景层，需为纯色（不能透明且不能包含其他图形），用于与前景图叠加形成完整的应用图标。具体请参考：[通用应用 UX 体验标准](../design-guides/ux-guidelines-general-0000001760708152.md)。

## 解决方案

* 审核出现问题中的提示是因为应用中配置的图标不符合UX设计规范。应用图标资源需分层，尺寸需满足规范要求：应用图标资源必须分为前景图和背景图两层，尺寸要求必须为1024px\*1024px，资源不允许自行裁剪圆角，不允许在资源内添加内间距。可参照通用应用UX体验标准中‘[视觉风格](../design-guides/ux-guidelines-general-0000001760708152.md#section1353515481417)-2.1.4.3图标’章节里的判定标准。
* 官方文档[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)引导开发者在app.json5配置文件中配置icon和label，由于module.json5配置文件中配置的icon会覆盖app.json5配置文件中的icon，需要检查是否在module.json5配置文件中也配置了icon和label：
  + 如果module.json5配置文件中的icon和label非必需，可以直接删去，减少冗余配置和错误几率。在DevEco Studio 5.0.3.800版本及之后，module.json5配置文件中的icon和label不再强制要求配置。
  + 如果使用到的某些系统API，对module.json5配置文件中的icon和label存在依赖，例如：[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)，则需要在app.json5和module.json5配置文件都配置正确的icon和label。
* 下载使用HUAWEI DevEco Studio 5.0.5.315或以上版本进行再打包，发布应用。
* 处理步骤可参考[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)和[配置优先级和生成策略](../harmonyos-guides/layered-image.md#配置优先级和生成策略)。

## 常见FAQ

Q：按照[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)配置图标后，上架审核时还是会出现应用未配置图标的前景图和背景图问题。

A：module.json5中的图标和标签配置优先级高于app.json5中的图标和标签配置，需确认应用的图标和标签配置引用。

Q：应用配置图标不符合UX设计规范问题在本地解决后，如何确认已修复完成？

A：可以使用AppGallery Connect平台上的[UX测试](../app/agc-help-cloudtest-uxtest-0000002289534109.md)，UX测试完成后，可从测试报告获知修复结果。

Q：背景图一定要纯色的吗？

A：背景图要纯色的，但不能是透明的。

Q：配置前景图背景图后，应用图标出现细微的栅格点，是什么原因？如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/iXy2BfmVTa-np3thE6FOvA/zh-cn_image_0000002658793845.png "点击放大")

A：查看前景图后发现透明区域都是栅格点，且图片不是PNG格式，导致透明区域的栅格点都显现出来，整改图片确保透明区域100%透明度，图片格式为PNG后，可解决问题。
