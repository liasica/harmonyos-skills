---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-1
title: 穿戴应用如何获取对应手表侧指纹
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > 穿戴应用如何获取对应手表侧指纹
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:07+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:de63675f2a525bf603dff0d4efa5f3027a42715e748d9dbb19b8850cb2b3c5d8
---

## 问题现象

穿戴应用如何获取对应手表侧指纹，本地调试与正式发布是否有所不同。

## 解决方案

* 正式发布指纹可在[证书、APP ID和Profile](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)查看，其中APP ID为穿戴应用指纹信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/wKZOBzTXQvahCLkeCfy04A/zh-cn_image_0000002658854363.png "点击放大")
* 参考[使用AppInfo模块时，如何获取应用身份标识](../harmonyos-guides/wearengine_faq-9.md)。
* 本地调试所用指纹可使用以下命令获取：hdc shell bm dump -n应用bundleName | grep appIdentifier。
