---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy
title: Clang-Tidy代码检查
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Clang-Tidy代码检查
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5e5eb4a4a08ebbf3afaee7954d2d9e9ba59ab12e223daceddb21def66207a092
---

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

## 检查规则配置

当前支持通过三种方式配置检查规则。

### 方式一：在Clang-Tidy Checks中配置

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/LxwbXUS5RrGE6aT0oZBWxA/zh-cn_image_0000002731382587.png)
2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/HMSnvktpSxeBPXiQ67Yldw/zh-cn_image_0000002701823284.png)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/JbzSoJ_3QFK-8mwCZjv7SA/zh-cn_image_0000002701823288.png)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Kayg4-VGQPCnqz7ro5C3nw/zh-cn_image_0000002731382599.png)

### 方式二：在 .clang-tidy文件中配置

1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/3-KrN0t8QOKLsFK-JV-xaA/zh-cn_image_0000002701663374.png)

### 方式三：在Inspection-checks中配置

1. 通过如下两种方法进入Inspect Code。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/8buumEMpRDKbXx5Eb21Mmg/zh-cn_image_0000002701663366.png)
2. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/_WKVS63QRcy7PN6sGcAzaQ/zh-cn_image_0000002731542561.png)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/oL37HLgdRQmwYMyzL2ZO6g/zh-cn_image_0000002701823294.png)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/SYHdJPZHRGaGTalWrbFvuw/zh-cn_image_0000002731382591.png)

## 通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

### 自动实时检查

**生效规则**

若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)、[.clang-tidy文件](ide-clang-tidy.md#section158716295189)和[Inspection-checks中](ide-clang-tidy.md#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)和 [.clang-tidy文件](ide-clang-tidy.md#section158716295189)中配置的规则生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/-ZVChMlcTq2KfOOrzMLYnA/zh-cn_image_0000002701663364.png)

**操作步骤**

代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。

### 手动检查

**生效规则**

手动检查时，仅[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 通过如下两种方法，进入手动检查入口。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/7yBmiJ_GTUCyR5-2kj8Q5Q/zh-cn_image_0000002731382589.png)
2. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/1xY8txULRQ6RaNG5cyxDnw/zh-cn_image_0000002701823282.png)
3. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/mQ5h4cdcQ7ypjWl0TsoX-g/zh-cn_image_0000002731382595.png)

## 通过自定义Clang-Tidy检查代码

从26.0.0版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。

**生效规则**

1. 勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效。
2. 不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use external Clang-Tidy instead of the built-in one**，添加clang-tidy.exe程序文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/N5jK3yZEQse8LPmXb4KyPA/zh-cn_image_0000002731382593.png)

   **说明** 

   clang-tidy.exe可从DevEco Studio安装目录中获取。
2. 选择生效规则和开启实时检查。
   * 进入clang-tidy界面，若勾选**Prefer .clang-tidy files over IDE settings**， [.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效；若不勾选**Prefer .clang-tidy files over IDE settings**，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。
   * 若勾选**live update（show in “Current File”）**，会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考[内置Clang-Tidy的手动检查](ide-clang-tidy.md#section1395112325376)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/CM1Gl1IjRIqmIc2qonVU6A/zh-cn_image_0000002731542559.png)
