---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy
title: Clang-Tidy代码检查（C/C++）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Clang-Tidy代码检查（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:741d4ae602ae1091d9a3adcab0f462c0c55eca161ff9e0ae2c435c82b3b7d096
---

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

## 检查规则配置

当前支持通过三种方式配置检查规则。

### 方式一：在Clang-Tidy Checks中配置

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Xq_PhLwxRxO51QHRDR9VXg/zh-cn_image_0000002808766579.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B436F96260C8D75CF194F0D3D8FA44B983994DA647E9A27452F3D9210DDF9319)
2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/P8Zj6YkrT6qSZRl3CxyqtQ/zh-cn_image_0000002779566994.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=751E2AEDFE987394BEE834C8F7ED833582984BFD4EBE28EE49D960FA595D9D77)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/WabFLNspT664ajXdmKY7Fg/zh-cn_image_0000002779407016.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=50E07690357AACE97FB56601CB84A565975F775EE687A4347803CBA7373B4663)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/OGULYJ5YQ02b6fCLRxn9CQ/zh-cn_image_0000002808886661.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=18159081B94E0E594E09DD473C6AACEAF5B083EF3C9A8E7103F7642A79DB86CA)

### 方式二：在 .clang-tidy文件中配置

1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4-mH3tXmQqOtyjQW3AxzHQ/zh-cn_image_0000002779407022.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=425816C6E603C3C11BBDCA17BC0B6204FDB9F420F830F7AC7E816FC5D5AA0EC9)

### 方式三：在Inspection-checks中配置

1. 通过如下两种方法进入Inspect Code。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/N2ticAg4SQWLDueVmNvByw/zh-cn_image_0000002808766577.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7EDB57453D00CC93C89754D6845B99A32DA8D9C7CC6F8F8F460B964C0502C68)
2. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/cath9oPJQYGSSj2tvHHgOA/zh-cn_image_0000002808886655.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB9CB66F0E99D367254A466C63581470D5C8F057AC94AA0F662AF357964FFE02)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/AskpGKsTSNy8vcFqLdieiQ/zh-cn_image_0000002779567002.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7D5D7DF42798B3FFA4FF8C3C53A76F5E61BA06215E2C36CA2B9B85B726187C9)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/dT3VJjlzRmamT7ev2KqEkA/zh-cn_image_0000002808886663.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=90A9EC248E192F198A8273BA376CD23AF37A9B5FE37BF3A41A6E0608BA3B97FC)

## 通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

### 自动实时检查

**生效规则**

若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)、[.clang-tidy文件](ide-clang-tidy.md#section158716295189)和[Inspection-checks中](ide-clang-tidy.md#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)和 [.clang-tidy文件](ide-clang-tidy.md#section158716295189)中配置的规则生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/YKtHLD44Rd-8ZNcYd3NGgQ/zh-cn_image_0000002779566996.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AED1F696CF9167BFD669525E04898D3EA111465F2D50D11ED0B44D41E6EAB69E)

**操作步骤**

代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。

### 手动检查

**生效规则**

手动检查时，仅[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 通过如下两种方法，进入手动检查入口。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/iC1QcfdfRVy6BfRw08C7IQ/zh-cn_image_0000002808886657.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8BEE9E349A0EAE787A06D3B8F549B58F501F71BE18AF7FEC82D167AEED395C6)
2. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/0ye1pY7HSeCeOsNLbsMknA/zh-cn_image_0000002808766575.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EA6FDD0967C167DADC5642DEC1D74B08E3A25FA04EE69FE552980DB0EBE5165)
3. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/2Va40YB_SYCwh8M_8UTIfw/zh-cn_image_0000002808766581.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9410C9F45D6CA018A6D5887AC263C562FE6A2C2214A8CE16C81B6EE6C0D5D72A)

## 通过自定义Clang-Tidy检查代码

从26.0.0版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。

**生效规则**

1. 勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效。
2. 不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use external Clang-Tidy instead of the built-in one**，添加clang-tidy.exe程序文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/qcmbM0dRSAW_m5y3bbBdtw/zh-cn_image_0000002779407018.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=72EFBC3B63278460493C00357A22D356F1675145BDFC543C50F72C9557339BDB)

   **说明** 

   clang-tidy.exe可从DevEco Studio安装目录中获取。
2. 选择生效规则和开启实时检查。
   * 进入clang-tidy界面，若勾选**Prefer .clang-tidy files over IDE settings**， [.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效；若不勾选**Prefer .clang-tidy files over IDE settings**，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。
   * 若勾选**live update（show in “Current File”）**，会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考[内置Clang-Tidy的手动检查](ide-clang-tidy.md#section1395112325376)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/MNTeInuKRF6zhumGMpfQJA/zh-cn_image_0000002808886659.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2A6DC35185055C8D6C8455C041A1B8DDC970A6A5935A6D3622D802C418F51ED)
