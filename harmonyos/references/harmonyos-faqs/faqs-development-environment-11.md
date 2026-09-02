---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11
title: 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
breadcrumb: FAQ > DevEco Studio > 环境准备 > 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bae4bb4a3da64db1eb31e219d8de0760bc12754514a4b563c6b77f24a2fd76ee
---

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Beg2Y-J4SvaQ38g29RaSRA/zh-cn_image_0000002194158336.png)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1. 进入sdkmgr所在的目录。

   ```
   1. cd ${命令行工具根目录}/sdkmanager/bin
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/eVwcojcZTvaOmjq6v2MOZw/zh-cn_image_0000002229603729.png)
2. 打开sdkmgr文件。

   ```
   1. vim sdkmgr
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/f_8ldZGxT2G6-NbQUG_hMQ/zh-cn_image_0000002229758205.png)
3. 在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/42WaguAOTWiJghtanNHfiQ/zh-cn_image_0000002194317952.png)
4. ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
