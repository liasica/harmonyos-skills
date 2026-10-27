---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-30
title: 上传应用图标到HarmonyOS 开发者中心报错文件类型不对
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 上传应用图标到HarmonyOS 开发者中心报错文件类型不对
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d95b8403b2747dcf6dce6b3588673496e628a1ee40d9c59f99c5367e5c4c2f07
---

## 问题现象

发布应用时，上传应用图标到HarmonyOS 开发者中心失败，报错“文件类型错误，请上传PNG、WEBP格式的文件”。但是检查文件类型是PNG，这是什么原因？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/WqubB-rxSXG9Ub8fKKrU-w/zh-cn_image_0000002628394596.png "点击放大")

## 解决方案

检查是否对图片进行了修改。常见的错误是手动将其他格式的图标修改后缀成.PNG。系统是校验原始图片的二进制编码格式，仅仅手动修改图片的后缀名不能修改文件二进制编码类型。需要通过专业软件修改图片类型，如使用画图软件打开图片，点击文件另存为需要的图片类型：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/A0ikErLwTXWNu2ji5QnJOg/zh-cn_image_0000002628554486.png "点击放大")

## 总结

可以通过专业工具（如DevEco Studio）查看图片的原始二进制编码格式，如下图片手动修改了后缀名为PNG，但实际是JPEG格式。上传至HarmonyOS 开发者中心就会报文件类型错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/JqF3s948SCipQlJDyPRZDw/zh-cn_image_0000002658913815.png "点击放大")
