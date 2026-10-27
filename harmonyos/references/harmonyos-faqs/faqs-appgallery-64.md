---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-64
title: 已经修改SDK版本但上架仍提示应用含有beta版的API该如何处理
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 已经修改SDK版本但上架仍提示应用含有beta版的API该如何处理
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb1f8f34d53cbcab5f2d9c97d90dcb3dbb9d5830c967f6538741a4e4928f393f
---

## 问题现象

应用上架提示应用含有beta版的API，使用的是beta版本的开发工具，但是已经把所有的SDK改成release版本了，而且检查了一遍没有调用beta版API的地方，应该如何检查？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Jh90IZRbS92syY0y3RO1SA/zh-cn_image_0000002628394628.png "点击放大")

## 解决方案

beta版的API依赖于开发工具，不是手动就能修改成release版本。如果开发工具是beta版，构建出来的软件包中就会含有beta的API，这种软件包是无法上架应用市场的。

检查构建出来的软件包中pack.info文件中的releaseType是否为beta，若为beta，说明是使用了beta版的开发工具。建议前往[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载release版开发工具。
