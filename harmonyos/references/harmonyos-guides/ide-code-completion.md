---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-completion
title: 代码生成/补全
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:96d90019808eeec1ea1cb00b716969064175d6d292755e3df023fab38c08c14a
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

自动补全功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Editor > General > Code Completion** 中勾选“Sort suggestions by recently used”。

说明

若已勾选代码补全按最近使用排序但未生效，请检查**Code Completion**页面，确保“Sort suggestions alphabetically”已取消勾选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/zaPyULNHTwGmPQIqEuPFpg/zh-cn_image_0000002561833633.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=16B2076EFD7F21B321C7166D9E549D87208E5F9EB894F0612F2947295206711F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/mlOWzK5nTCevYHTMZS-aAA/zh-cn_image_0000002530753706.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=08310F8814FF1B5B87BB6C28FA4F8FC56EC8133FA134C2CB333141CB1D56B4ED)

## 快速覆写父类

DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类方法，提升开发效率。将光标放于子类定义位置，使用**快捷键Ctrl+O**（macOS为**Control+O**），或右键单击**Generate**...，选择**Override Methods**，指定需要覆写的对象（方法、变量等），点击**OK**将自动生成该对象的覆写代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/yiPJcxFMRWOjI8ePjUzXrQ/zh-cn_image_0000002561833631.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=2B8031BC86B9AB3B4ECC447C592B491D7FBC698447F0F533FCEEB547D52E3C85)

## 快速生成构造器

编辑器支持为类快速生成一个对应的构造函数。

在类中使用**快捷键Alt+Insert**（macOS为**Command+N**），或单击鼠标右键选择**Generate**...，在弹窗中选择**Constructor**，选择一个或多个需要生成构造函数的参数，点击**OK**。若选择**Select None**，则生成不带参数的构造器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/z8DR-t_BTT-UGJAzNa8VFw/zh-cn_image_0000002530913698.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=46FF4194C078D5C21E1F60355048AE45D7A19A6661ED474C7E2F2199A91D483B)

## 快速生成get/set方法

编辑器支持为类成员变量或对象属性快速生成get和set方法。

将光标放置在当前类中，单击右键选择**Generate...>Getter and Setter**，或者使用快捷键**Alt+Insert**（macOS为**Command+N**），在菜单中选择**Getter and Setter**，完成方法快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/SjVhgvm-TXWhICsCtY-UFg/zh-cn_image_0000002561833629.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=AC55C8AEBBBAC593B4CF6205FEC8BF488C8F9B300A72AB2E4B264BE81DD310CD)

## 快速生成声明信息到Index文件

编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过**Generate...>Declarations**功能，批量在Index.ets文件中进行声明，便于其他模块调用。

在HSP或HAR模块内的文件编辑界面，单击右键选择**Generate...>****Declarations**，或者使用快捷键**Alt+Insert**（macOS为****Command+N****），在菜单中选择**Declarations**，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/QR25Ck9iT_C8v4v2J7hzqw/zh-cn_image_0000002561833627.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=8B93E198B5A6FE659F0CD3D0135B6828A689F6A097D8D0D9BA09E832E725CD8B)
