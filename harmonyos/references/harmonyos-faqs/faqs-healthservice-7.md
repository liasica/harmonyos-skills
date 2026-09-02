---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-7
title: 申请运动健康权限被拒问题排查定位
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 申请运动健康权限被拒问题排查定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cbf103a400347eb222771f73ed9a341de225b4f457b27204a8a15523682a0f0d
---

## 问题现象

1. 申请运动健康权限被驳回，驳回原因：“应用类型包括其他平台，技术自检中接入方式麻烦增加Cloud API，请修改申请资料后重新提交”，问题该如何排查处理？
2. 申请华为运动健康权限，提交应用信息时，上传开发者申请资料清单失败，提示“上传失败，点击重新上传”，如何排查原因？![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/G_K_pyVHQpq2y_LNMM0jEw/zh-cn_image_0000002628554628.png "点击放大")

## 背景知识

* [Health Service Kit（运动健康服务）](../harmonyos-guides/health-service-kit-guide.md)是为华为生态应用打造的基于华为账号和用户授权的运动健康数据开放平台。在获取用户授权后，开发者可以使用Health Service Kit提供的开放能力获取运动健康数据，基于多种类型数据构建运动健康领域应用与服务，为用户打造丰富、便捷、专业的运动健康场景体验。
* 开发准备接入：[申请运动健康服务权限](../harmonyos-guides/health-apply.md)。
* 常见申请驳回场景参考：[申请被驳回的常见问题](../harmonyos-guides/health-apply.md#申请被驳回的常见问题)。

## 解决方案

1. 优先排查提交的申请材料中，应用类型是否存在有其他平台。如果存在，需要在技术自检中接入方式增加Cloud API。如果不需要其他平台，可以将描述从申请资料中删掉并重新提交审核。
2. 上传材料请参考如下注意点。
   * Excel文件限制：
     + 只支持xlsx后缀的文件，且后缀名字符小写。
     + 文件中不可以有图片外的其他形式的附件，如pdf、word等，否则会上传失败。
     + 单元格不能是单个的“-”，“+”，“=”，“@”字符，且不能用以上字符作为内容开头。
     + Excel文件中不能有公式格式的单元格。
     + 文件大小不超过10M；表格sheet页数量、行、列都不能超过100。
   * ZIP文件内容限制：
     + 只支持png，mp4，jpg，xlsx，apk，docx格式文件压缩。
     + 文件大小不能超过100M。
   * 视频文件限制：
     + 文件后缀需要为mp4（小写）。
     + 文件大小不能超过100M。
