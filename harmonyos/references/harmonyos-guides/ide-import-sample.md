---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-sample
title: 导入Sample工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 导入Sample工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3ae76b6c0396110eeaf9ab7757f1ff819582cfec4208714d4f0040a12a21ecd1
---

DevEco Studio支持Sample工程的导入功能，通过对接Gitee开源社区中的Sample资源，可一键导入Sample工程到DevEco Studio中。下面介绍导入Sample的方法。

## 约束与限制

### 支持的国家/地区

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 操作步骤

1. 在DevEco Studio的欢迎页，进入**Customize** **> All Settings... > Version Control > Git**界面，单击**Test**按钮检测是否安装Git工具。

   说明

   在打开工程的情况下，可以单击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）进入设置界面。

   * 已安装，请根据[2](ide-import-sample.md#li1599692216194)开始导入Sample。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JBBEVw-lSziLN1eMsxwbjw/zh-cn_image_0000002530913250.png)
   * 未安装，请单击**Download and Install**，DevEco Studio会自动下载并安装。安装完成后，请根据[2](ide-import-sample.md#li1599692216194)开始导入Sample。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/6WXGVGE8TSKCRMTxAxhwkg/zh-cn_image_0000002530753254.png)
2. 在DevEco Studio的欢迎页，在**Projects**页签下，单击**M****ore Action >** **Import Sample**按钮，导入Sample工程。

   说明

   在打开工程的情况下，可以单击**File > New > Import > Import Sample**来进行导入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/p0mthHYxQ_2B-BfmzvDWHQ/zh-cn_image_0000002530753260.png)
3. 选择需要导入的Sample工程，然后单击**Next**。
4. 设置**Project name**和**Project location**，然后单击**Finish**，等待Sample工程导入完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/xFgCB-YcQiyAnND7gNCvrQ/zh-cn_image_0000002532477844.png)
5. 导入Sample后，等待工程同步完成即可。

   说明

   如果网络受限，导入时会提示“Failed to connect to gitee.com port 443: Time out”连接超时错误，请[配置Git代理信息](../harmonyos-faqs/faqs-development-environment-2.md)。
