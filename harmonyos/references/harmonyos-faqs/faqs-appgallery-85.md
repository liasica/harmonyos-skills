---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-85
title: AGC应用自检结果的不一致问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC应用自检结果的不一致问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de724d825bc858b8b8b51b411b2dada67a7a8549d74aae3b760f0c3465a99a59
---

## 问题现象

应用在“软件包管理”页面“上架自检”列显示通过，而同一个软件包在“应用测试”-“版本列表”页面的“上架自检”列显示“上架自检不通过，详情请查看测试报告”。

对于不同路径下同样的“上架自检”有两种不同的结果，原因是什么？

## 解决方案

1. 两个路径下的上架自检结果的使用场景和拦截规则不同：

   在“软件包管理”页面的“上架自检”是为提高应用审核通过率，按照华为应用市场上架标准对应用进行兼容性、稳定性、性能、功耗、UX、隐私等测试，是在开发完成阶段的自查。让开发者快速验证软件包的基础合规性，提前发现问题，为了避免进入后续流程后被驳回。

   在“应用测试”-“版本列表”页面的“上架自检”是将提交邀请测试时选择使用，会按照应用正式上架的审核要求自检，需要确认这个应用版本是否具备被分发给用户（邀请测试用户）的资格。
2. 建议开发者根据场景选择：

   若需测试分发，使用邀请测试自检即可；

   若为正式发布做准备，应通过软件包管理执行上架自检。
3. 自检结果不影响您邀请测试的上架结果和不会影响应用提交上架申请，但存在被审核驳回的风险，故最终结果以提交正式上架审核结果为准。
4. 两个自检路径：
   1. 邀请测试上架自检[发布测试版本](../app/agc-help-appgallery-release-testapp-0000002258174266.md#section6326193918558)：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/mPTJNxJYRG2CfOykYYeCdg/zh-cn_image_0000002658913855.png "点击放大")
   2. 软件包管理启动自检[（推荐）上架自检](../app/agc-help-release-app-upload-pkg-0000002277983368.md#section15203163921310)：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/CgbvxTkFRWygxW1laStKmA/zh-cn_image_0000002658793915.png "点击放大")
