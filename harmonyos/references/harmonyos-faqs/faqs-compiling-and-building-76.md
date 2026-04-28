---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-76
title: 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a4cca9527940b88025c28cc48e42a79a1964072503a27394b2013a48e2d30812
---

**问**

使用 commandline-tools 工具在 Linux 上时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”，请检查网络连接是否正常，确保可以访问该 URL。如果网络无问题，尝试更新 commandline-tools到最新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/cGC6UWKMQRS7J-yHXe9WSw/zh-cn_image_0000002229603881.png?HW-CC-KV=V1&HW-CC-Date=20260428T002922Z&HW-CC-Expire=86400&HW-CC-Sign=379C909D3172E0BBF2C23E845FE396D63F5E5A48A25B2F0A46B52CBDEEB149A2 "点击放大")

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区所致。

请参考以下方法解决：

1. 进入sdkmgr脚本所在的文件夹：${命令行工具根目录}/sdkmanager/bin。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/BKZJtcfrQKSe7M-3YnN_9A/zh-cn_image_0000002194158460.png?HW-CC-KV=V1&HW-CC-Date=20260428T002922Z&HW-CC-Expire=86400&HW-CC-Sign=C2373428D5B90D5A9592512E8A9C5308D625675931CA2600C8143B114CB9BE0A "点击放大")
2. 打开sdkmgr文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/fpLym3GER1-KmqOKWAJMiA/zh-cn_image_0000002229603849.png?HW-CC-KV=V1&HW-CC-Date=20260428T002922Z&HW-CC-Expire=86400&HW-CC-Sign=7DB0F636D7F927F1416EE2C17A7F1C0EC597C8DAF6D9D291456535F0C9A0976D "点击放大")
3. 在文件的最后一行，-Dfile.encoding=UTF-8 后面添加 -Duser.country=CN。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/znYGCh2iRu24jLX4ybvoJA/zh-cn_image_0000002194318088.png?HW-CC-KV=V1&HW-CC-Date=20260428T002922Z&HW-CC-Expire=86400&HW-CC-Sign=44934026E2DBFFAB8313AE8D0FCA4431583C3BFB1F31490F5D5D6B1809568B5E "点击放大")
4. 保存修改，再次执行sdkmgr相关命令即可。
