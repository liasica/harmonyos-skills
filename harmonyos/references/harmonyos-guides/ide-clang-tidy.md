---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy
title: Clang-Tidy代码检查（C/C++）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Clang-Tidy代码检查（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e7799bc757cf2a6c52d86a9566388229e1354b24af63f1f8cfb83424404905f6
---

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

## 检查规则配置

当前支持通过三种方式配置检查规则。

### 方式一：在Clang-Tidy Checks中配置

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eQDuJZGWQtafIz0YoryRmw/zh-cn_image_0000002808766579.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=6907CF889F6CC13B9F4B8AB2D2EF5909B43542EB4E6BEC0A479F0D6C57895F3B)
2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/oAV9hs4FRXuFaKx-uxTqOw/zh-cn_image_0000002779566994.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=5138B392C54F22615B27D1F2A72EC275F61B72487E123D8F01165CFA1C12A8DE)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/GoqIq7qNQPCMttWm1RhuLw/zh-cn_image_0000002779407016.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=7208F975F3980BA439B676EA68CB2A17B9EC71263E5C7845D00011B74FA581BB)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/JOHJSBK0QDOVUEYMWTVX_g/zh-cn_image_0000002808886661.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=C46594D8E60AE21786EBEEA55BAD3F3FF01BED9E24580FAD3A22658A56608B96)

### 方式二：在 .clang-tidy文件中配置

1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/EVNlzH3sTT2O2PjC9iNPwA/zh-cn_image_0000002779407022.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A49FB7E5D1F870067D5782D61B1781E45EBDB2721E7FDBF149F55A7B5685D12)

### 方式三：在Inspection-checks中配置

1. 通过如下两种方法进入Inspect Code。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ynBaUNTcRNm7yRdAayLlFw/zh-cn_image_0000002808766577.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBFAF09D36D8DB82E89DAF561E3EB6041F53ED2F409F1C4AA0BBA4B8935F28D8)
2. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Mp1RD2YyTNG8WBR7PqfM_g/zh-cn_image_0000002808886655.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D9C112D584A85186BA9AEEADC7422DF1D952E113D4F24BCEB95F65F02937628)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/tp3LCsAtRpiwpADw0Bqz2w/zh-cn_image_0000002779567002.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=393745F6B3CBAC2273F1AF13517F5F9D2CD55C4FBB024AC73C40A866A86B2C47)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/K8IwgaorRR6nAthuwqaAMw/zh-cn_image_0000002808886663.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D0D0A0F9E5F67952298986487CDC63FF30B8400C7101813C13410D81C0DD14D)

## 通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

### 自动实时检查

**生效规则**

若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)、[.clang-tidy文件](ide-clang-tidy.md#section158716295189)和[Inspection-checks中](ide-clang-tidy.md#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)和 [.clang-tidy文件](ide-clang-tidy.md#section158716295189)中配置的规则生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/LaQR3x6NS7WU_iVYe--69g/zh-cn_image_0000002779566996.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB744CFDAB68A36C2D0B7A033925C6AF9B3579DF16641871F0E00594CB3FE240)

**操作步骤**

代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。

### 手动检查

**生效规则**

手动检查时，仅[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 通过如下两种方法，进入手动检查入口。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/J6CKRDCcQlqkkDEFmEd1Rw/zh-cn_image_0000002808886657.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5E20903B5CFFDCF14273DF6B2E2ACC8CD393E2134D38E1D5067E53FBCBAF7D8)
2. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/RmhxuyiJQzGtz4TkqxlxqA/zh-cn_image_0000002808766575.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=00F3AE22898C563B34F3E3A1B291F423C21A64C928AE9502EC3C275B89986CF0)
3. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/lWPtHdRuQq6YaxTEIYc03g/zh-cn_image_0000002808766581.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EA9B13EB700DFB1FDA362A0B613C2ED96E7AAA68077E158C588B9F7A1FE3A33)

## 通过自定义Clang-Tidy检查代码

从26.0.0版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。

**生效规则**

1. 勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效。
2. 不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use external Clang-Tidy instead of the built-in one**，添加clang-tidy.exe程序文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/0scixbnPSDS22yDK4kbrVw/zh-cn_image_0000002779407018.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3E2160D5F3481A42E5698B9588382C0CB6DE5D84D052AE3D4DE05ABCB9F8493)

   **说明** 

   clang-tidy.exe可从DevEco Studio安装目录中获取。
2. 选择生效规则和开启实时检查。
   * 进入clang-tidy界面，若勾选**Prefer .clang-tidy files over IDE settings**， [.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效；若不勾选**Prefer .clang-tidy files over IDE settings**，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。
   * 若勾选**live update（show in “Current File”）**，会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考[内置Clang-Tidy的手动检查](ide-clang-tidy.md#section1395112325376)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/bwZNIqKASgyTJOdQQRjXmA/zh-cn_image_0000002808886659.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=07A53FDC761C7DF863AC53524965A5CB08F385D71B2A06A48944C73D2C90B33A)
