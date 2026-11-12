---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28
title: ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1cd51794caa64dc05875aa79a1431c81b7b6b5cbe14a8c4cc74de781d74a8c12
---

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/C_SfrmhcRxGMaexoT-bfMA/zh-cn_image_0000002654837807.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=F315BF64565B627F2E0852D53000A75258972364D8559D774351EFF6EC6629E4)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/GiMLqsiLT5a1W1iDlJU4fA/zh-cn_image_0000002624478496.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EBB6336ED91D080CFECCF9EFEEA957929A479B4F1F7C9D0848BB3AFE918FAAA)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1. 删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2. 在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。

   工程迁移后结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Xbo7bsiGQeKKbtBmraDYMQ/zh-cn_image_0000002654797855.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=440549EAE259AA954505F4E2EBF9F1C9C1D2DFB0C9EEF9F67185D76DBAB0573E)
3. 迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/8qrK8S_nTTubO04dU_OgCg/zh-cn_image_0000002624638400.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5201559BB7684C24CC99085D0AC612AF224E8C864C84EBBC25FD8D55B7957CA)
