---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-editer-overview
title: 代码阅读
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a7b7d6ab6116bb1fd465e693c927b259e0d54b7a3157235cbd6a9d19dd97f06
---

DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码关键字、运算符、字符串、类、标识符、注释等进行高亮显示，您可以打开**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**）面板，在**Editor > Color Scheme**自定义各字段的高亮显示颜色**。**默认情况下，您可以在**Language Defaults**中设置源代码中的各种高亮显示方案，该设置将对所有语言生效；如果您需要针对具体语言的源码高亮显示方案进行定制，可以在左侧边栏选择对应的语言，然后取消“Inherit values from”选项后设置对应的颜色即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/3e-AjCLpQjuwcypFzNTswA/zh-cn_image_0000002530913498.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=F6C42EA5AF5E273AB265CE3CB65D950E18713A3D631356014BB8C857FA6B4E0E)

## 代码跳转

在编辑器中，可以按住**Ctrl**键（macOS为**Command**键），鼠标单击代码中引用的类、方法、参数、变量等名称，自动跳转到定义处。若单击定义处的类、变量等名称，当仅有一处引用时，可直接跳转到引用位置；若有多处引用，在弹窗中可以选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/WBa-4x8TTTSI0oaR48nhNg/zh-cn_image_0000002561833421.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=D46A44BDD5585CE1DE8E6724FE0A9DC52D3A6EE925975F00C0280E0A34401658)

## 跨语言跳转

DevEco Studio支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转其对应的C/C++函数，从而提升混合语言开发时的开发效率。您可以选中接口名称单击右键，在弹出的菜单中选择**Go To > Implementation(s)**（或使用快捷键**Ctrl+Alt+B**，macOS为****Command**+Option+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/nqthZiMUS-6yJO__tG7t0Q/zh-cn_image_0000002530753534.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B44EEC58F39484E8D6D05CB41A320067A417C5496678DE09E8BFEAB905D6B5A3)

## 代码格式化

代码格式化功能可以帮助您快速的调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，您也可以个性化的设置各个文件的格式化规范，设置方式如下：在**File > Settings > Editor > Code Style**（macOS为**DevEco Studio > Preferences/Settings > Editor > Code Style**）下，选择需要定制的文件类型，如ArkTS，然后自定义格式化规范即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/zTulfsOpTOW_3BX9gMEtWQ/zh-cn_image_0000002561753485.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=86C1F27FD1DE5308B926CD41A77E25267032D6ECFF23ED6CC7B19912189BE7FF)

在使用代码格式化功能时，您可以使用快捷键**Ctrl + Alt + L**（macOS为**Option+Command +L**） 快速对选定范围的代码进行格式化。

如果部分代码片段不需要进行自动的格式化处理，可以通过如下方式进行设置：

1. 在**File > Settings >Editor > Code Style**（macOS为**DevEco Studio > Preferences/Settings > Editor > Code Style**），单击“Formatter”，勾选“Turn formatter on/off with markers in code comments”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/5szerndXR922MYThNLzQjg/zh-cn_image_0000002530913514.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B7BEF001E9735E275CD1D4EAFD6A182EEE638EAC5BC876B280406EAC49A48A36)
2. 在不需要进行格式化操作的代码块前增加“//@formatter:off”，并在该代码块的最后增加“//@formatter:on”，即表示对该范围的代码块不需要进行格式化操作。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/wxqHJYRST6ukyX7DHxxOpQ/zh-cn_image_0000002561753423.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=8F11F29300E8CF8AC3BBF3321B59A68E77B7B3CD6335DAC2F7FD928D1DC62AC3)

若工程已配置code-linter.json5文件，选中code-linter.json5文件右键选择**Apply CodeLinter Style Rules**，代码格式化规则将与已配置的code-linter.json5文件中相关规则保持一致。code-linter.json5文件配置请参考[配置代码检查规则](ide-code-linter.md#section19310459444)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/B15ttHs_Rk6pKXDTifS9sQ/zh-cn_image_0000002530913568.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=9F0427D0086AD9D269626F034C7F43A3EAFAFDCF62E845BF9BCF32D6698B3D8D)

## 代码折叠

支持对代码块的快速折叠和展开，既可以单击编辑器左侧边栏的折叠和展开按钮对代码块进行折叠和展开操作，还可以对选中的代码块单击鼠标右键选择折叠方式，包括折叠、递归折叠、全部折叠等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/zBCTYMqMTemp5W3ecJOJZw/zh-cn_image_0000002530913546.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=C0725184583CA04E4679820B134BB8E7027CC12B02BBF19C0DDE542CDAFEE498)

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**（macOS为**Command+/**）进行快速注释。对于已注释的代码块，再次使用快捷键**Ctrl+/**（macOS为**Command+/**）取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/cmnbzY6SROalstJuP1y8BA/zh-cn_image_0000002530913518.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=2104472B0ADC55412A79574782ECC8F45FEFCF852F4162FE758C2B4C28B66199)

## 代码结构树

使用快捷键**Alt + 7 / Ctrl + F12**（macOS为**Command+7**）打开代码结构树，快速查看文件代码的结构树，包括全局变量和函数，类成员变量和方法等，并可以跳转到对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/fylqVjlhTz6M0jMddCTfIA/zh-cn_image_0000002530913556.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=73DA58F937FBF96BE46241A17BEEA998521ACCA67DFCC0B1C487DF6754C07013)

## 代码引用查找

提供Find Usages代码引用查找功能，帮助开发者快速查看某个对象（变量、函数或者类等）被引用的地方，用于后续的代码重构，可以极大的提升开发者的开发效率。

使用方法：在要查找的对象上，单击鼠标**右键 > Find Usages**或使用快捷键**Alt +F7**（macOS为**Option +** **F7**）。可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/txJtI1yoReiNvm0JL_H6CQ/zh-cn_image_0000002561753431.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=0E1185B293DCE1B14420AEEC0579EE31974A633A366F04A8908C012DB3D422DF)图标查看变量赋值位置，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Wa3_mrmNQEWwko2scl3qXQ/zh-cn_image_0000002561753429.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=4AE30B62D123824477CC8F5E6C0892482FE4D100FD325B8F1F534FABBE5F6A95)图标查看变量引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/hDUwHIn7Rdm_ZI_LBH2fUQ/zh-cn_image_0000002561753439.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=1C3310BEC4DC9663B33FC687C3E878A72BCAEE00F378DA136EBAB3EFB6866847)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**“/\*\*”+回车键**，快速生成注释信息。

说明

C++文件同时支持使用**“//!”+回车****键**快速生成注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/bc5sKZFDQcisuFz0nzeYaw/zh-cn_image_0000002561833507.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=4623089B0CC57B4A3E0A72FACB07A31C50AD63D78587D8301CF535CD11EB2882)

## 代码查找

通过对符号、类或文件的即时导航来查找代码。检查调用或类型层次结构，轻松地搜索工程里的所有内容。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Uf5wE5WKQt6GN5em_m5n7w/zh-cn_image_0000002530753588.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=D0E5A9869E1AA2E6D8CE9D6A1859FFA66750C00E8987F7C526F2D778BD283D03)

## 快速查阅API接口及组件参考文档

从DevEco Studio 6.0.2 Beta1开始，Show in API Reference新增快捷键功能。

在编辑器中调用ArkTS/JS API或组件时，支持在编辑器中快速、精准调取出对应的参考文档。

可在编辑器中，鼠标悬停在需要查阅的接口或组件，弹窗将显示当前接口/组件在不同API版本下的参数等信息，单击弹窗右下角**Show in API Reference**；或选中接口或组件，右键点击**Show in API Reference**（或使用快捷键**Alt+A**，macOS为**Option+A**），可以快速查阅更详细的API文档。

说明

DevEco Studio集成了离线版API参考类文档，最新版本请参考官网[HarmonyOS API参考](../harmonyos-references/development-intro-api.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ElqDTmbrQU-6IaL5wp4jvA/zh-cn_image_0000002561753437.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=074D3E09618069623970B7C89C1BD4B2A1AD3C700B364F432BCB871DA59B09C9 "点击放大")

在弹窗中可以查看：

1. 使用的API是否涉及权限申请或仅支持在测试框架下使用。
2. 使用的接口状态。**deprecated**标签表示即将废弃的API接口，可使用**useinstead**标记的API进行替代，请开发时关注。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/kfHDZKr2StaSEj-djRWnpA/zh-cn_image_0000002561753455.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=0F8196EBBB2FC564BABCCAB05AC30261D4F0631384087A032A8E43B11C59175C)

## Optimize Imports功能

使用编辑器提供的Optimize Imports，可以快速清除未使用的import，并根据设置的规则对import进行合并或排序。选择文件或目录，使用快捷键**Ctrl+Alt+O**（macOS为**Control+Option+O**），或单击菜单栏**Code > Optimize Imports**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/2hj0zLohT1-XSoiZh4_1PQ/zh-cn_image_0000002561753513.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=45018A0056EE1209FB49A1853CB4420EBF49B817DD1C607407EC2373A253484B)

如需修改优化配置，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> Editor > Code Style**，选择开发语言（当前以ArkTS为例），在**Imports**标签页中，可选择在优化时是否需合并来自同一模块的import，是否需要对同一条import语句导入的元素进行排序，或对多条import语句按模块排序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/BFb9jfoZTe6P43K2P0_NEA/zh-cn_image_0000002561753495.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=13860F95BCDCE2BF043F2ECC0696D71C9942E77E95BB11EDE89E4701CF9F044A)

## API变更查询

从DevEco Studio 5.1.0 Release版本开始，DevEco Studio中支持查询、对比从某个选定的SDK版本开始，当前工程中使用到的ArkTS API是否存在行为变更，并提供相应适配指导链接，帮助开发者完成工程代码适配修改。

从DevEco Studio 5.1.1 Release版本开始，支持对C API的变更情况进行查询，提供跨版本查询能力。

从DevEco Studio 6.0.2 Beta1版本开始，新增扫描进度提示功能，以及变更接口在代码文件中具体位置需在Code Location中查看。

从DevEco Studio 6.1.0 Beta2版本开始，API变更查询接入CodeGenie快速问答功能，CodeGenie提供根据代码文件和变更文档输出非兼容API的修改建议，以及新增筛选API变更类型功能。

### 使用约束

* 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* API废弃情况不在API变更查询的扫描范围。
* ArkTS API函数调用过程中，当开发者使用的API存在泛型参数和包含extends或keyof关键字时，不支持变更查询。示例如下：

  ```
  1. // API定义
  2. interface ProgressInterface {
  3. <Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>;   //包含extends或keyof关键字不支持变更查询
  4. }
  5. // API调用
  6. Progress({ value: 10, type: ProgressType.Capsule })
  7. .style({content:'Install'})
  ```

* 使用C++语法实现的API函数变更，不支持查询。示例如下：

  ```
  1. template <class _Rep, class _Period>
  2. cv_status condition_variable::wait_for(unique_lock<mutex>& __lk,const chrono::duration<_Rep, _Period>& __d)  //C++语法实现的API函数不支持查询
  ```
* C API扫描过程中，若存在与变更接口同名的函数，扫描结果可能会出现误报。
* 特殊调用方式下，不支持API变更查询。示例如下：

  ```
  1. // 反例：函数指针方式
  2. int (*sigptr)(int, const struct sigaction *__restrict, struct sigaction *__restrict) = &sigaction;
  3. sigptr(NULL,NULL);
  4. // 反例：回调方式
  5. callback(sigaction);
  6. // 反例：自定义宏
  7. #define MySig sigaction
  8. MySig(NULL,NULL);
  ```

### 操作步骤

**使用DevEco Studio 6.0.0 Release及以上版本，按以下步骤操作：**

1. 在菜单栏点击**Tools > API Change Assistant**，编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况，选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。同时，有进度条提示扫描进度。

   说明

   API变更查询以选择的起始版本为基线，查询当前工程中所使用的API是否存在行为变更。如选择的SDK版本为5.0.0(12) Release 到 6.0.0(20) Release，查询的是5.0.1(13) Beta3到6.0.0(20) Release版本相比5.0.0(12) Release的API变更。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/wXxvDB8mTRmGJbxtwrKPXw/zh-cn_image_0000002561833511.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=C1257FC79A008C998E35881A4E648403A3E93CABB2C7A4BC404833F440824333)
2. 点击扫描结果中的代码地址，跳转到相应的代码编写位置；点击蓝色高亮的变更描述，跳转至版本说明文档中查看详情；修改完后可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8knM44tFQkOFknpA3OIMxw/zh-cn_image_0000002530913512.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B220589CE04A77A0D3ECF93B08CB9C29C7A32FD7150FD69C17921DA4D16C8B08)图标，标注已修改。同时，可通过如下入口搜索或筛选API变更扫描结果、导出扫描结果数据等。
   * **Search**：支持在Search框中输入API名称或文件路径，对扫描结果搜索。
   * **API Version**：通过选择API版本，对扫描结果筛选。
   * **Language**：通过ArkTS或C语言，对扫描结果筛选。
   * **API ID**：通过行为变更的API接口，对扫描结果筛选。
   * **API Change Type**：API变更类型，取值包括All、UX visual Layout Change（UX视觉布局变更）、UX Interaction Behavior Change（UX交互行为变更）、API Behavior Change（接口行为变更）、API Change Deprecation（接口废弃变更）、API Definition Change（接口定义变更）。
   * **Fix Status**：API变更扫描结果的修复情况，All表示所有，Fixed表示已修复，Unfixed表示未修复。通过修复情况，对扫描结果筛选。
   * **Scan Again**：重新扫描。
   * **Export**：将API变更扫描结果数据导出到本地。
   * **Settings**：设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB。当工程代码量较大导致扫描缓慢时，可以调整该参数。
   * **Code Location**：变更接口在代码文件中的具体位置，点击可跳转至接口所在的代码行。点击位置右侧的**Quick Ask**可打开CodeGenie，在CodeGenie对话框点击发送，会根据代码文件和变更文档输出不兼容API修改建议；若文件中存在多处变更，CodeGenie根据文件中所有变更点输出不兼容API修改建议。

   说明

   通过Quick Ask打开CodeGenie后，仅支持使用HarmonyOS Ask智能体进行快速问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ISlOW7mEROSOjV1BSlj1kQ/zh-cn_image_0000002530913554.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=153160B787CA3C62E0597671D83CFB837936CD61BD1A9B4FF017CDB0DB87D268 "点击放大")

**使用DevEco Studio 6.0.0 Release以下版本，按以下步骤操作：**

1. 在菜单栏点击**Tools > API Change Assistant**，编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况，选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。

   说明

   API变更查询以选择的起始版本为基线，查询当前工程中所使用的API是否存在行为变更。如选择的SDK版本为5.0.0(12) Release 到 6.0.0(20) Release，查询的是5.0.1(13) Beta3到6.0.0(20) Release版本相比5.0.0(12) Release的API变更。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/a1lCyy7CQCeM2DfsCq2dTA/zh-cn_image_0000002530753536.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=93FDB5E45ED3DCFE8983BACFB87652ADBF23F2B483767B980CDC036CCD48B190)
2. 点击Code Location中的代码地址，跳转到相应的代码编写位置；如需更多指导，可点击Guidance link中的链接，跳转至版本说明文档中查看详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/uKObrLIPSgeCj9AXt-D6fg/zh-cn_image_0000002561753433.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=99F8BA14B7026FEE9C114D993043EAFBCFA6FC8919D9A2CA0EC3CF5BA59934D5)
3. 点击**Export**，选择API变更的存放位置后导出变更数据；点击**Scan Again**可重新进行扫描。通过右侧**Settings**按钮，可以设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB，当工程代码量较大导致扫描缓慢时，可以调整该参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/4uzsRVr_TGqbRYnZj8dkYw/zh-cn_image_0000002530913578.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=9C72F5B1A05CAEF807FCFCD2D612CE378280B89C4C30842652D97DFAE58D70EE)

## 父/子类快速跳转

编辑器支持快速跳转至当前接口、类、方法、属性的子类/父类。点击代码编辑区域左侧的Gutter Icons（装订线图标）可以跳转到对应的父/子接口或类。如有多个继承关系，在弹窗的文件列表中选择需要查看的接口/类即可。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/R1KbnnKKSD6WqoTfr8V72Q/zh-cn_image_0000002530913550.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=924A66FD1BF3DA5DFBCDD340D9DE2E0128D2FA2FC63AC9D1B3AD78E86ABC98E7)Implemented：支持跳转到对应的实现类或子接口及其对应的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/j-ouNtejS9CJdz4AIKJoYQ/zh-cn_image_0000002561753531.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=59592CDC044EF85E18C9E39136300475087C63715020FD9013D6F0F14531B920)Implementing：支持跳转到对应的父接口或父接口的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/giJMigBHSsWle9TjTVxGdw/zh-cn_image_0000002561753427.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=9ABFB4A7DE43B05039724715E9A24D61E87560C70E4B9B2C74A84D761264F8B5)Overridden：支持跳转到对应的子类或子类的属性/方法。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/ombkPgXkS7a2RgZkZyS77g/zh-cn_image_0000002561833485.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=59D6F7A85CB967C0DFEA221344ECA1A0198FBBD1B464AB9EE3F8CAAB0606CBDA)Overriding：支持跳转到对应的父类或父类的属性/方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/lfagPRW1Sw68DYwzrutVRQ/zh-cn_image_0000002561833457.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=EE2B85E1B1FA93697F1AB519DAB1A17CD1442CA233DA31593017238BBA33B183 "点击放大")

本功能默认开启，可以通过菜单栏进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> Editor > General > Gutter Icons**，通过勾选或取消勾选Implemented、Implementing、Overridden、Overriding四项可以开启或关闭该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/BliFFB-jQtqQtxTuvNdAbA/zh-cn_image_0000002530913570.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B1843475212D851688ECC3DF6DB53EF64968E421985FE40FC8DBEB16D11AC03D)

## 查看接口/类的层次结构

编辑器支持查看当前接口/类父类或子类的层次结构。选中或将光标放置于类/接口名称处，使用**快捷键Ctrl+H**（macOS为**Control+H**），或在菜单栏**Navigate**页签下选择**Type Hierarchy**，在弹出的Hierarchy窗口中查看接口/类的继承关系结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Ho1KJeq7T7aD-j5rpzXuOQ/zh-cn_image_0000002561753507.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=50BA6ECBB5A38C9FF66C1683B258779326D1BA540C4399B56867F98F7F7B70E2)

Hierarchy窗口按钮功能：

| 图标 | 功能 |
| --- | --- |
|  | 显示所选类的父类和子类。  该功能不支持查看接口的继承关系。 |
|  | 显示当前类/接口的父类。 |
|  | 显示当前类/接口的子类。 |
|  | 按字母顺序对继承关系结构树中的所有同级元素进行排序。 |
|  | 更新显示所有的类/接口的继承关系结构。 |
|  | 默认双击结构树中类/接口名称时，编辑窗口将跳转至所选类/接口所在的代码位置。勾选该选项后，单击结构树中类/接口名称，即可跳转访问。 |
|  | 展开/折叠继承关系结构。 |
|  | 锁定当前Hierarchy窗口显示于编辑窗口上。 |
|  | 将类/接口的继承关系结构导出到文本文件中。 |
|  | 关闭工具窗口。 |

## 添加嵌入提示

从DevEco Studio 6.0.0 Beta2 版本开始，在编辑时启用Inlay Hints嵌入提示功能，可以提供有关参数名称、类型等代码说明信息，提升代码可读性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/SA3LGACfToasJYDyuuyRuA/zh-cn_image_0000002530913540.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=19C3F750DAD6569BF5AE161F6BB7C8F890B2F1D0D298F52DF2C474FE1AD1B98A)

进入**File > Settings**（macOS为**DevEco Studio > Preferences****/Settings**） **> Editor >** **Inlay Hints**，配置勾选希望展示的变量名称、属性、参数、返回值类型，点击**OK**后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0I2DWHUySS6IxIHZuxUWnw/zh-cn_image_0000002561753457.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=05E098449A1CB21F6CDCC674AFE99B2A7CE1A312044FE97E25CB0193C5E4C406)

## Copy Reference

从DevEco Studio 6.0.0 Beta2 版本开始，在编辑页面选中代码行或类、方法、参数、变量等名称，右键选择**Copy / Paste Special > Copy Reference**，将自动复制定义处的地址。复制成功的地址可以在双击**Shift**弹出的搜索框中进行搜索，帮助开发者快速找到该接口的定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qJMoX_4qQw6mEqAfzdNguQ/zh-cn_image_0000002530913544.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=CEDF2A27D8996F437E1D2403DE22910F897540172F9ECF1422FA17785E7FFC3B)
