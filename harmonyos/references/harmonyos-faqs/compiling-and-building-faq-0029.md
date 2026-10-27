---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0029
title: 流水线搭建sdkmgr下载报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 流水线搭建sdkmgr下载报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:83238f01359261390b188036e1d91422444ab3d7200f24b808277c9575c21c04
---

**Q：如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错？**

**A**：使用 commandline-tools 工具在 Linux 上时，如果提示Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList，请检查网络连接是否正常，确保可以访问该 URL。如果网络无问题，尝试更新 commandline-tools到最新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/2H6UpXzKT7qUtm2LKjWrHA/zh-cn_image_0000002772920648.png "点击放大")

该问题通常是因为Linux的国家码未设置为中国区所致。

请参考以下方法解决：

1. 进入sdkmgr脚本所在的文件夹：${命令行工具根目录}/sdkmanager/bin。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/XgSWXG3-TjCOM2PXLvUOVQ/zh-cn_image_0000002773080608.png "点击放大")
2. 打开sdkmgr文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Ae2Ta7NmSUWHIs0nSzsLJA/zh-cn_image_0000002772920650.png "点击放大")
3. 在文件的最后一行，-Dfile.encoding=UTF-8 后面添加 -Duser.country=CN。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/nqjcBvqITiGyi9Jn9Zm9KQ/zh-cn_image_0000002772920654.png "点击放大")
4. 保存修改，再次执行sdkmgr相关命令即可。
