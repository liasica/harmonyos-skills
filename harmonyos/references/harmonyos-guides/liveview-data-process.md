---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-data-process
title: 设置数据处理位置
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 设置数据处理位置
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b0b11214570623b5a0711dfa2c6e781487c0e637ee47a8fa302dffaf104d3d08
---

若开发者要[通过Push Kit更新实况窗](liveview-update-by-push.md)，需要设置默认数据处理位置为“中国”。

在“项目设置 > 数据处理位置”页面设置数据处理位置，设置步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表中点击需要设置数据处理位置的项目。
3. 进入“项目设置 > 数据处理位置”页面，点击“管理”。
4. 在“是否已启用”栏勾选“中国”，并在“是否设为默认”栏将中国设置为默认数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/-b6JGKw1TFOIhGfO8KrfCA/zh-cn_image_0000002552958970.png?HW-CC-KV=V1&HW-CC-Date=20260427T234935Z&HW-CC-Expire=86400&HW-CC-Sign=78B69F41C772360165325676B5CA11B8BF8533913669196626E94945E654173F)
5. 设置完成后，点击“保存”。

说明

如果设置的数据处理位置与开发者的服务器位置不一致，或者设置的数据处理位置与应用所服务的用户所在地不一致，都会导致推送消息无法下发。
