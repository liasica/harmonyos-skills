---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11
title: 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
breadcrumb: FAQ > DevEco Studio > 环境准备 > 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7caec71f2ca202a896ac3b3a7069bf0133d6f5c09c5340f50e115f2444c741a8
---

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Beg2Y-J4SvaQ38g29RaSRA/zh-cn_image_0000002194158336.png?HW-CC-KV=V1&HW-CC-Date=20260428T002853Z&HW-CC-Expire=86400&HW-CC-Sign=1357C561FEFD580A403C8D88819BDF654CB0469B0849F5AD5F6D055AAEB1E470)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1. 进入sdkmgr所在的目录。

   ```
   1. cd ${命令行工具根目录}/sdkmanager/bin
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/eVwcojcZTvaOmjq6v2MOZw/zh-cn_image_0000002229603729.png?HW-CC-KV=V1&HW-CC-Date=20260428T002853Z&HW-CC-Expire=86400&HW-CC-Sign=DA831C3E4D730F6B33A35457575B13BC8B0D27CA3CCEC9E3F26B3F3A0F15D473)
2. 打开sdkmgr文件。

   ```
   1. vim sdkmgr
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/f_8ldZGxT2G6-NbQUG_hMQ/zh-cn_image_0000002229758205.png?HW-CC-KV=V1&HW-CC-Date=20260428T002853Z&HW-CC-Expire=86400&HW-CC-Sign=8771DA6742963E269EF4D7A004446A843311A474A9FCD7E841E08CD02231EB72)
3. 在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/42WaguAOTWiJghtanNHfiQ/zh-cn_image_0000002194317952.png?HW-CC-KV=V1&HW-CC-Date=20260428T002853Z&HW-CC-Expire=86400&HW-CC-Sign=885E3C40EACB895324AB21C57FBEBEBF6024FDE27286C81E372E00B9399020E3)
4. ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
