---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-data-process
title: 设置数据处理位置
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 设置数据处理位置
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:11+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3ff10727cf98a0fdc7948c8a0d436cd599639ab87ce6f17506edded875f353f7
---

若开发者要[通过Push Kit更新实况窗](liveview-update-by-push.md)，需要设置默认数据处理位置为“中国”，否则可能导致推送消息无法正常下发，从而影响通过Push Kit更新实况窗的功能。

在“项目设置 > 数据处理位置”页面设置数据处理位置，设置步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表中点击需要设置数据处理位置的项目。
3. 进入“项目设置 > 数据处理位置”页面，点击“管理”。
4. 在“是否已启用”栏勾选“中国”，并在“是否设为默认”栏将中国设置为默认数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/z9Rz0Sl9QvKQuL4HfXy5zw/zh-cn_image_0000002712245230.png)
5. 设置完成后，点击“保存”。

**说明** 

如果设置的数据处理位置与开发者的服务器位置不一致，或者设置的数据处理位置与应用所服务的用户所在地不一致，都会导致推送消息无法下发。
