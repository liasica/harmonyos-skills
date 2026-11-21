---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69
title: 如何在应用内共享HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何在应用内共享HSP
category: harmonyos-faqs
scraped_at: 2026-11-21T09:17:36+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:65c0e70598bba670aee7023dd8adeaa1d9ac4013a52f9f948ee93a8c6b212647
---

如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1. 将编译模式设为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/gbHC1v87Rz6BO7RHOXwngQ/zh-cn_image_0000002654835175.png?HW-CC-KV=V1&HW-CC-Date=20261121T011736Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB36927490D680E3CAA8E948C8686CB14BD77A9F401D91AFA7C36B705938372A "点击放大")
2. 选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/jcGHoysfSqqqX2Yn__w8jg/zh-cn_image_0000002654795239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011736Z&HW-CC-Expire=31536000000&HW-CC-Sign=D08F86E01A6BEC2A04BC0AECD9A206C6B3B224C8846FD5DEE3393304CB618AE0 "点击放大")
3. 构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](../doccenter-deveco-studio/ide-ohpm-repo-quickstart.md#section1710514092415)）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8cjOtj46Qe-m8caI02LLFw/zh-cn_image_0000002624635772.png?HW-CC-KV=V1&HW-CC-Date=20261121T011736Z&HW-CC-Expire=31536000000&HW-CC-Sign=395162AD63E7E93F44B7538BD3332C412CD957695B3996FB56669C648F5B6595 "点击放大")
4. 上传到仓库，然后使用 `ohpm install` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](../harmonyos-guides/ide-hsp.md#section79378499185)
