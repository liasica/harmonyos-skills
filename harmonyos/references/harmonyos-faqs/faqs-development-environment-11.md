---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11
title: 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
breadcrumb: FAQ > DevEco Studio > 环境准备 > 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:265b7b926e0b5ddca33399024f2a44c5f38313ffaccb61e883c6f869263db8f8
---

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/RKRZOcNUQnikjhwGT8YEyA/zh-cn_image_0000002624638308.png)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1. 进入sdkmgr所在的目录。

   ```powershell
   cd ${命令行工具根目录}/sdkmanager/bin
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/UI7UespjQYmHSgWPwFoGIQ/zh-cn_image_0000002654837717.png)
2. 打开sdkmgr文件。

   ```powershell
   vim sdkmgr
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/YEwYea-ZSXaeu3XzKUxxFg/zh-cn_image_0000002624478404.png)
3. 在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/6k3nXIoxQKWfnhxomD6VKA/zh-cn_image_0000002654797771.png)
4. ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
