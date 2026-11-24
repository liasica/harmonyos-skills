---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:65b39aea8e98381a6609b68f49971b2e89818837254a5d3792175566aedec963
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

自动补全功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Editor > General > Code Completion** 中勾选“Sort suggestions by recently used”。

**说明** 

若已勾选代码补全按最近使用排序但未生效，请检查**Code Completion**页面，确保“Sort suggestions alphabetically”已取消勾选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/bDeOhQnOSCa_WFe060E7cw/zh-cn_image_0000002808887075.png?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=97B5C1F3EAEC2179D9E5BFE2B1410751BEFB0F24095CE4690F00465A5302753D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/AZux_UKKRhuUgUFBtlGSHA/zh-cn_image_0000002779407432.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=36CDC2FA625B1EF1E8CBC54EAC2AD9C2ECEB82A6CF12D39735C9BABF746D3EF2)

## 快速覆写父类

DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类中的方法，提升开发效率。将光标放于子类定义位置，使用**快捷键Ctrl+O**（macOS为**Control+O**），或右键单击**Generate**...，选择**Override Methods**，指定需要覆写的对象（方法、变量等），点击**OK**将自动生成该对象的覆写代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/8tfchpv3Qh6Ed3zbXyxmXA/zh-cn_image_0000002808887069.png?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2D4BA50572F9F9899F09D1D88227A440EB1F90CD1742DBB0A897147B3B6441B)

## 快速生成构造器

编辑器支持为类快速生成一个对应的构造函数。

在类中使用**快捷键Alt+Insert**（macOS为**Command+N**），或单击鼠标右键选择**Generate**...，在弹窗中选择**Constructor**，选择一个或多个需要生成构造函数的参数，点击**OK**。若选择**Select None**，则生成不带参数的构造器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/b0Cn9BCFSuKPdxyzZfUkKg/zh-cn_image_0000002779567406.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB504471484279E81AE8B30B2D8B7FBF458DFAE10AC76467EB29ECAED54958EF)

## 快速生成get和set方法

编辑器支持为类成员变量或对象属性快速生成get和set方法。

将光标放置在当前类中，单击右键选择**Generate...>Getter and Setter**，或者使用快捷键**Alt+Insert**（macOS为**Command+N**），在菜单中选择**Getter and Setter**，快速生成get()和set()方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/0E_mUQMPQLKen_F_djACRA/zh-cn_image_0000002779567412.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=39D5CA87734AF452EB9CC9D7643880C2336C55C5F3C0CCD541C462890E42D5D3)

## 快速生成声明信息到Index文件

编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过**Generate...>Declarations**功能，批量在Index.ets文件中进行声明，便于其他模块调用。

在HSP或HAR模块内的文件编辑界面，单击右键选择**Generate...>****Declarations**，或者使用快捷键**Alt+Insert**（macOS为****Command+N****），在菜单中选择**Declarations**，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/74UO2iWgSfi2Xvoia2c73Q/zh-cn_image_0000002808766991.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044222Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC606A90160E9093681ED8F412B68C5A10E0AE3E1F2DC89AB10903CFCFCED4A6)
