---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11
title: 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
breadcrumb: FAQ > DevEco Studio > 环境准备 > 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e6cfc2386a33f1143a0fdeee1cf401b35014fe8cd7d8311e8727557f87041d1e
---

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Beg2Y-J4SvaQ38g29RaSRA/zh-cn_image_0000002194158336.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=8E05B98C0EAC0A6D1A40767A98D9D6BBEF19CBA35065CCA223C6226032E46EEE)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1. 进入sdkmgr所在的目录。

   ```
   1. cd ${命令行工具根目录}/sdkmanager/bin
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/eVwcojcZTvaOmjq6v2MOZw/zh-cn_image_0000002229603729.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=C141B775082E880988C8E868FDE18BACE8BB20DE0B630D22FD90B1CED6FB966E)
2. 打开sdkmgr文件。

   ```
   1. vim sdkmgr
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/f_8ldZGxT2G6-NbQUG_hMQ/zh-cn_image_0000002229758205.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=1D9436CB2BA093541C140F9696A731264A9FB46A402D493775D284D515510122)
3. 在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/42WaguAOTWiJghtanNHfiQ/zh-cn_image_0000002194317952.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=15795B53FA4EE07207E298B10D2D437ADBF73585C02261527970F89F04DEE2F2)
4. ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
