---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69
title: 如何在应用内共享HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何在应用内共享HSP
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:33bec6d24974cf25df0d5d353a363abef96e84c08837ba7098042d3660e1edce
---

如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1. 将编译模式设为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/9fbTO-ghQCCA2xV2GkNhpA/zh-cn_image_0000002215625442.png?HW-CC-KV=V1&HW-CC-Date=20260429T061454Z&HW-CC-Expire=86400&HW-CC-Sign=17C1A7DE54CB9F473F86333E8CA81A50891AF2E6B95496CE29AA879C4E8C2870 "点击放大")
2. 选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/G4ea9wuRR6GWtp5J8S9FNw/zh-cn_image_0000002215465626.png?HW-CC-KV=V1&HW-CC-Date=20260429T061454Z&HW-CC-Expire=86400&HW-CC-Sign=5260E93893F661E28B0F9C1914E0C6A7BC6165144442FBCC472F7C48916ED215)
3. 构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](../harmonyos-guides/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/zdcSo4tLRzCGV3M93eMaHg/zh-cn_image_0000002250545457.png?HW-CC-KV=V1&HW-CC-Date=20260429T061454Z&HW-CC-Expire=86400&HW-CC-Sign=1B903C7E3D25360BD23E3A0C7CC82E3C0B74FEDB5E4756782412C5F877F4D99C "点击放大")
4. 上传到仓库，然后使用 `ohpm install` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](../harmonyos-guides/ide-hsp.md#section79378499185)
