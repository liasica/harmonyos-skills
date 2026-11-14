---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy
title: Clang-Tidy代码检查（C/C++）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Clang-Tidy代码检查（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:96a4bacee6f2f274b2f44c9e0a3561e9c0c29c965c0edea01a10b0b4db9619d8
---

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

## 检查规则配置

当前支持通过三种方式配置检查规则。

### 方式一：在Clang-Tidy Checks中配置

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/DHPOPlNdTxC9U1OYwcn8oA/zh-cn_image_0000002808766579.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=32C7AA9A8512F762F96E851FDA335AC4A9374B928B8CE2B77A732792276E672C)
2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/j4p38TLSQ4CECR3IQu2xDQ/zh-cn_image_0000002779566994.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1A0F20A229976AB134B7453F6F33CA44FE3C2F6E192CB64CD13B27170DF0308)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Jd08bKSwQQ6GeY3xzwiyGA/zh-cn_image_0000002779407016.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=353CBFD2B0D6654B4EE93629B88E8AC06C7F6236347E07945E2B3F0F9B1ECD4A)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/wt-yWVEkQfmtbyyvdriU7Q/zh-cn_image_0000002808886661.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=8605EC79C69CA46BB10F182D971B84B6F73B28F1E53C02BA159B0860F35002AA)

### 方式二：在 .clang-tidy文件中配置

1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WkxtcubTSXWwDQiWVVb6eA/zh-cn_image_0000002779407022.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CC01854DC35C73C19ABF1B0DBEF1FB50713BDAD4AAEB61BDD7B7BA0A1D0F045)

### 方式三：在Inspection-checks中配置

1. 通过如下两种方法进入Inspect Code。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_KNvA7_YRKegcJjCFS-4OA/zh-cn_image_0000002808766577.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A4852E4E273995F0284E76C3A8F8619B249FDA983CFBC602237A53800E407FC)
2. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

   添加检查规则时，可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Ci4kCt9iSDGm2eQ1MvoaUw/zh-cn_image_0000002808886655.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A036DF0D9D33EA2F9CFDDE443FA731FC8C88376580807C7FE85B102D7CC2A9F)按钮展开规则填写框，在不同行添加规则。添加完成后点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/E6jY8uNLQtKvEGXg11EReA/zh-cn_image_0000002779567002.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=60896EA7562BE464DEB098BA1882473161A3B1251863928EE6D56852E89F620F)按钮，多条规则会自动用英文逗号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/9ybYP2qaS4iX8cFwYpdXNA/zh-cn_image_0000002808886663.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=326B898BF849874EE0F9BD708B48E4AE4D94940C690E1FD98C975EEC7C7CDDE3)

## 通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

### 自动实时检查

**生效规则**

若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)、[.clang-tidy文件](ide-clang-tidy.md#section158716295189)和[Inspection-checks中](ide-clang-tidy.md#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](ide-clang-tidy.md#section386618116187)和 [.clang-tidy文件](ide-clang-tidy.md#section158716295189)中配置的规则生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/pCFs89UNR5iZ-IIcFmhMiQ/zh-cn_image_0000002779566996.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=D35FA6E0180AB5EE47B756503EC58990613B5092DC6D619B4CED6D317F4FE1FC)

**操作步骤**

代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。

### 手动检查

**生效规则**

手动检查时，仅[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 通过如下两种方法，进入手动检查入口。
   * 在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
   * 在菜单栏点击**Code >** **Inspect Code**...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/L_myY4lZQz2t9BHmIShSDg/zh-cn_image_0000002808886657.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=32CB63F2B8701DD086AB19B3E2982CBFF1440A577BCC882B0CD5A4F5D5239A2F)
2. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/-9sqrMpmTOaz3gLefORl0A/zh-cn_image_0000002808766575.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=E120CBED3975A2603849316E60AF8EB00E2A7DC318CA1AA88A6C56986C41928B)
3. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Z9okUnz3Q8uQY2JuFUAFJg/zh-cn_image_0000002808766581.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C5282EABB6D645E21D017300AFAC0D735EDB12EFBAEAA2A8B8036430B1C7EE1)

## 通过自定义Clang-Tidy检查代码

从26.0.0版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。

**生效规则**

1. 勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效。
2. 不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。

**操作步骤**

1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use external Clang-Tidy instead of the built-in one**，添加clang-tidy.exe程序文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/pzlnpsqXQ6ipXzwpEqv_gw/zh-cn_image_0000002779407018.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=C02E157F3076586DC8719791871871FC96BD6943EBE2673238632126AE35B685)

   **说明** 

   clang-tidy.exe可从DevEco Studio安装目录中获取。
2. 选择生效规则和开启实时检查。
   * 进入clang-tidy界面，若勾选**Prefer .clang-tidy files over IDE settings**， [.clang-tidy文件中配置的规则](ide-clang-tidy.md#section158716295189)生效；若不勾选**Prefer .clang-tidy files over IDE settings**，[Inspection-checks中配置的规则](ide-clang-tidy.md#section841663417181)生效。
   * 若勾选**live update（show in “Current File”）**，会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考[内置Clang-Tidy的手动检查](ide-clang-tidy.md#section1395112325376)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/J-Pnz4K5RTyLJDZA-gN-jQ/zh-cn_image_0000002808886659.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=48E6DA6D715DAA24D7F2B359E753DC8B98D26B755065D739ADC925F0CFA7E7CA)
