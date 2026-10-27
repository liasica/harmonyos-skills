---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0010
title: DevEco Studio环境配置常见问题
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > DevEco Studio环境配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:281a160c7ce56d9ca5376eee049fe5732c28f9830aa0494f615a4edb7bf865f4
---

**Q：在使用6.0.2.640版本的DevEco Studio和Command Line Tools时，若系统环境中配置使用JDK25，在命令行中执行打包命令会导致打包失败，报错信息如下图所示：**

**A**：

```text
ERROR： 00303153 Configuration Error
```

JDK25版本中JDK-8370216的接口行为变更，导致打包问题。

使用系统命令行终端执行 java --version，判断是否默认使用JDK25版本，如果使用JDK25版本，有以下两种方案可解决本问题：

方案一：系统环境变量配置为低于JDK25的版本。

方案二：升级DevEco Studio和Command Line Tools到6.0.2.642及以上版本（建议）。

**Q：在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ldZLLovgQw6ziiBdd7LL2Q/zh-cn_image_0000002772995676.png "点击放大")

**A**：在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。

将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。

**Q：Command Line Tools版本如何选择？26.0.0和6.0.2有什么差别？是否与DevEco Studio版本号配套使用？**

**A**：Command Line Tools的版本号与DevEco Studio版本号属于同一套版本体系，必须配套使用。26.0.0和6.0.2的核心差别在于配套的DevEco Studio版本不同、内置SDK版本不同（API 26 Release与API 22 Release）。详情参考[DevEco Studio 6.0.2新特性](../harmonyos-releases/deveco-studio-new-features-602.md)和[DevEco Studio 26.0.0新特性](../harmonyos-releases/deveco-studio-new-features-2600.md)。
