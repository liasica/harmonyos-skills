---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69
title: 如何在应用内共享HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何在应用内共享HSP
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:46+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:fd6bf614214d38ce2d72a48c81d06e351eb23ecdf5a7b7d538dd2f982cc2c450
---

如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1. 将编译模式设为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/e6eS7fTERFaQn81rP00u7Q/zh-cn_image_0000002654835175.png "点击放大")
2. 选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Tw8dR2cBQ062fU3yZwM0bQ/zh-cn_image_0000002654795239.png "点击放大")
3. 构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](../harmonyos-guides/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/YeIfMu3UTNCwzmPWHUNbHw/zh-cn_image_0000002624635772.png "点击放大")
4. 上传到仓库，然后使用 `ohpm install` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](../harmonyos-guides/ide-hsp.md#section79378499185)
