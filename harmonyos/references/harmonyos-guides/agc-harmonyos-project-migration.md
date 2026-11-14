---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:8005e1943270076595554950002ab46d59ab5daf9058802507cff0adcf56115d
---

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到HarmonyOS 开发者中心应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Bkaj2LyDSXmwCUm53gDr3g/zh-cn_image_0000002214858725.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=5994DCD89DC22FCEEFE2B3E158E5E240BDB02438E149625B6C14142026C956A1)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/8DyPY2_cRWWRFvpFt3Tjpw/zh-cn_image_0000002277950390.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=35B251850753767FBEB51DD25C618B5B206389287B05087A080A3FC99B43BF53)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
