---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-101
title: 无权限签署华为开发者服务协议
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 无权限签署华为开发者服务协议
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:da1503023ac03d32ab28452e16a9f8ac3295037c998a00b98413f6225e559aff
---

## 问题现象

在华为AGC平台签署《关于华为AGC与隐私的声明》时，勾选“我已阅读并同意”选项后，按钮呈灰色不可点击状态。页面提示："请联系您所在团队的账号持有者或者有法务权限的管理员签署协议"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Z1V_h1gHQtmTICghfvt_Ww/zh-cn_image_0000002658913931.png "点击放大")

## 解决方案

当前账号角色没有协议签署权限。根据AGC平台权限规则，只有“账号持有者”或“法务”角色可以签署《关于华为AGC与隐私的声明》。参考文档：[角色与权限](../app/agc-help-rolepermission-0000002271930352.md)。

查看当前账号角色与权限：AGC后台-用户与访问-个人信息-角色管理-查看权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VQ-l1_osRiCoA2gRa7USYA/zh-cn_image_0000002628394720.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/BrMcasXdQeuDsH6W3fra-A/zh-cn_image_0000002658793995.png "点击放大")
