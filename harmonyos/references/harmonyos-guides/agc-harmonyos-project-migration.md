---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-11-01T07:12:46+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:4da3b06f73d7fc5b09cf720600ef1ae61fd20eb3ec62afe7a662a33d6a514ec3
---

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到HarmonyOS 开发者中心应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/lCMhTdLqQMK3E5_BG_QAQw/zh-cn_image_0000002214858725.png)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/v1exYn6ASYyYVf52F79XIQ/zh-cn_image_0000002277950390.png)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
