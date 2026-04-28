---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d8c06b53e6fdf947089761a1ac8b432fbac803c8921a4c6149344bfad1e40ad1
---

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到AGC应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/iaGDFLToRrmT2uspf6Rg7g/zh-cn_image_0000002214858725.png?HW-CC-KV=V1&HW-CC-Date=20260427T235459Z&HW-CC-Expire=86400&HW-CC-Sign=B488B39FBF739359EEF5758A9E08356387A4D16602C5A8B868FDF0B3AA9217DB)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/VRs_PbWbRS6TY8BS9hxGYQ/zh-cn_image_0000002277950390.png?HW-CC-KV=V1&HW-CC-Date=20260427T235459Z&HW-CC-Expire=86400&HW-CC-Sign=3EF99225338D8A9AC87A1B402E94081D7B9630F600F65AD49E3FD54E64EA628F)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
