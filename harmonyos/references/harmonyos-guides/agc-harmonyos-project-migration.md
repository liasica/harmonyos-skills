---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5945debc77575774a1081afade5fb4d80f7a0da8dd30103c57c6ce0099af51d5
---

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到AGC应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/_5UX4jWbS56RtVd52JqWug/zh-cn_image_0000002214858725.png)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/qtcIaskTT_qV4u0z6uNHHA/zh-cn_image_0000002277950390.png)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
