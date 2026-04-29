---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration
title: 历史工程转换为端云一体化开发工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 历史工程转换为端云一体化开发工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:59+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:07289b518624e6a45d70b59d21631783a79f989f706c0c1549cfbedf5f9b8ab3
---

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

1. [创建一个端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到AGC应用、项目等云端资源。
2. 打开创建的端云一体化开发工程，右击端开发工程“Application”，选择“Open In > Explorer”，打开工程文件所在的目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/3xmdb94jQmazIDxOCxMYiw/zh-cn_image_0000002214858725.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=6C5BDE48C2E00837E4AC4D18C49B2A390886D41705F0B7BF66B2806D08CD20A4)
3. 删除端云一体化开发工程的端侧工程目录“Application”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/MNdoTSW_SCawIZv6GYXDDg/zh-cn_image_0000002277950390.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=7209BA2F0A4A1FC9B95910B7896BD79FE9F49939A6B7C9B38AC5B1D198CD4749)
4. 将历史工程目录（如“MyApplication30”）拷贝至[步骤3](agc-harmonyos-project-migration.md#li104559101267)的端云一体化开发工程目录下，并改名为“Application”。
5. 重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
