---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-data
title: 查看资源包分发数据
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 查看资源包分发数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f294f36fffef4a4939c4928edb534ec545668ad98f93adb6298c8eda401a9fa
---

资源包下载任务正式发布后，开发者可以前往AppGallery Connect查看资源包分发情况。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“分析”，在应用列表中选择对应的游戏。
2. 选择“分发分析 > 资源包后台下载分析”，在页面右侧切换“资源包版本”和“日期”为展示依据查看资源包下载数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/K2sVgBk0QSaAjhO7Tpe--w/zh-cn_image_0000002736313839.png)

   | 参数 | 单位 | 说明 |
   | --- | --- | --- |
   | 累计下载设备数 | - | 触发下载的总设备数。 |
   | 累计下载成功设备数 | - | 下载成功的总设备数。 |
   | 累计前台下载流量大小 | MB | 处于前台阶段下载资源包的累计大小。 |
   | 累计后台下载流量大小 | MB | 处于后台阶段下载资源包的累计大小。  **说明**：下载一个资源包时，其前台下载的包大小+后台下载的包大小=资源包文件的大小。比如前台下载500MB，后台下载500MB，一个资源包文件总计为1000MB。 |
