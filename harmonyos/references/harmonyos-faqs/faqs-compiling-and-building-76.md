---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-76
title: 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:efe70ec021af10bea128a8a8a011b4f8af8f5824d7fb469c558f97dc056e9e49
---

**问题描述**

使用 commandline-tools 工具在 Linux 上时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”，请检查网络连接是否正常，确保可以访问该 URL。如果网络无问题，尝试更新 commandline-tools到最新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/8UpeRxnDTRuj5KgtrTEQ6A/zh-cn_image_0000002654797895.png "点击放大")

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区所致。

请参考以下方法解决：

1. 进入sdkmgr脚本所在的文件夹：${命令行工具根目录}/sdkmanager/bin。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/D-y03OHRTMOEW-BfWP0E2g/zh-cn_image_0000002624638442.png "点击放大")
2. 打开sdkmgr文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Z9xrp7nvQgyrku_PrFlBXQ/zh-cn_image_0000002654837849.png "点击放大")
3. 在文件的最后一行，-Dfile.encoding=UTF-8 后面添加 -Duser.country=CN。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/i7_l-8JaQaqDqrUz9lLZ0A/zh-cn_image_0000002624478538.png "点击放大")
4. 保存修改，再次执行sdkmgr相关命令即可。
