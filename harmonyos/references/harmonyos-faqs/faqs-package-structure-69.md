---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69
title: 如何在应用内共享HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何在应用内共享HSP
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0e220d25ff389ef31e1eab6ae1c9e650f9ac460daba2062ce8bca64275b3d5f3
---

如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1. 将编译模式设为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/9fbTO-ghQCCA2xV2GkNhpA/zh-cn_image_0000002215625442.png?HW-CC-KV=V1&HW-CC-Date=20260428T002338Z&HW-CC-Expire=86400&HW-CC-Sign=CECEDB6AE85C41A9DF719095F94FB702C269A06E5BB1815E23A447D694238D1E "点击放大")
2. 选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/G4ea9wuRR6GWtp5J8S9FNw/zh-cn_image_0000002215465626.png?HW-CC-KV=V1&HW-CC-Date=20260428T002338Z&HW-CC-Expire=86400&HW-CC-Sign=E6E9F424BC551C201BFD3759E4F0EAFDACF8DE136F077B4F996605D9944744AC)
3. 构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](../harmonyos-guides/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/zdcSo4tLRzCGV3M93eMaHg/zh-cn_image_0000002250545457.png?HW-CC-KV=V1&HW-CC-Date=20260428T002338Z&HW-CC-Expire=86400&HW-CC-Sign=88B19FAD9825ADFD811A0E027B3F89165EB9E3C08DDC7F99190896492C838818 "点击放大")
4. 上传到仓库，然后使用 `ohpm install` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](../harmonyos-guides/ide-hsp.md#section79378499185)
