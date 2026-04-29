---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-completion
title: 代码生成/补全
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ccb46d4737d9dd71773bbbac3306b92fc9222014bdac7dd76db73be42a4e898a
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

自动补全功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Editor > General > Code Completion** 中勾选“Sort suggestions by recently used”。

说明

若已勾选代码补全按最近使用排序但未生效，请检查**Code Completion**页面，确保“Sort suggestions alphabetically”已取消勾选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/zMcZsWVfQQyhQG2GXf46XQ/zh-cn_image_0000002561833633.png?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=69690A0EBC042EB52B6A2B169A95DF11EBC9C91C0E8293D5B276F7DA6835B06A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/vMS-7JsSR0qoJmvQJfqeug/zh-cn_image_0000002530753706.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=4F6C8EC0ADC19E976AD69C2DCE8CF74D06D43352C27D7FE8BD96853C9E7AE55E)

## 快速覆写父类

DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类方法，提升开发效率。将光标放于子类定义位置，使用**快捷键Ctrl+O**（macOS为**Control+O**），或右键单击**Generate**...，选择**Override Methods**，指定需要覆写的对象（方法、变量等），点击**OK**将自动生成该对象的覆写代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/u7ddKy8TSM6W0qrALU3Y2w/zh-cn_image_0000002561833631.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=EE4EB2BC0BB2C70BA8A05393D0B48313FE4D41B17FD49FD6B30DA9E4C1A35FFF)

## 快速生成构造器

编辑器支持为类快速生成一个对应的构造函数。

在类中使用**快捷键Alt+Insert**（macOS为**Command+N**），或单击鼠标右键选择**Generate**...，在弹窗中选择**Constructor**，选择一个或多个需要生成构造函数的参数，点击**OK**。若选择**Select None**，则生成不带参数的构造器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/GxWdUkYDQFCsTncWCWaXUw/zh-cn_image_0000002530913698.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=C945C3BFDB705196000260C929C98435CD8EEF5C90989800341BB44D588AAEFF)

## 快速生成get/set方法

编辑器支持为类成员变量或对象属性快速生成get和set方法。

将光标放置在当前类中，单击右键选择**Generate...>Getter and Setter**，或者使用快捷键**Alt+Insert**（macOS为**Command+N**），在菜单中选择**Getter and Setter**，完成方法快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/qVbv2uJuTIyfj7fQDRG3mA/zh-cn_image_0000002561833629.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=9085944E38A8D5F2C2EB03E17A9EDC4226D555033A2721041EBF632F8F2CA482)

## 快速生成声明信息到Index文件

编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过**Generate...>Declarations**功能，批量在Index.ets文件中进行声明，便于其他模块调用。

在HSP或HAR模块内的文件编辑界面，单击右键选择**Generate...>****Declarations**，或者使用快捷键**Alt+Insert**（macOS为****Command+N****），在菜单中选择**Declarations**，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/aNWRPQROTA2qzZy9vautRA/zh-cn_image_0000002561833627.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=7264B9ABC11464C58E5F77009BA6639512B8974F6F6FDFC7029AD41D0FC10424)
