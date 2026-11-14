---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:50+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:98535fb129b6baf46f9c70ce98373f52b619e62c8612c8da8680498e21a00ed9
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

自动补全功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Editor > General > Code Completion** 中勾选“Sort suggestions by recently used”。

**说明** 

若已勾选代码补全按最近使用排序但未生效，请检查**Code Completion**页面，确保“Sort suggestions alphabetically”已取消勾选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/JCASH3_GSqml3tP7fvB99g/zh-cn_image_0000002808887075.png?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA3DC0387F99039EA543FC8F936BA3179A9D1BC090FA1D2DAA0CB7D21CEEDD17)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/coMS7IABRLi4Rnikm7_yfw/zh-cn_image_0000002779407432.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0FBF27C9F0C94406BB06C9616070AF8E05D061EC69F379F216E2D20897E3BA0)

## 快速覆写父类

DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类中的方法，提升开发效率。将光标放于子类定义位置，使用**快捷键Ctrl+O**（macOS为**Control+O**），或右键单击**Generate**...，选择**Override Methods**，指定需要覆写的对象（方法、变量等），点击**OK**将自动生成该对象的覆写代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/IFtKH4VvSPGthGBsxifVHQ/zh-cn_image_0000002808887069.png?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=1333F16051A5F697ECCC8766561600EC3E28C60EDF2D39D551596B3E32E29EA1)

## 快速生成构造器

编辑器支持为类快速生成一个对应的构造函数。

在类中使用**快捷键Alt+Insert**（macOS为**Command+N**），或单击鼠标右键选择**Generate**...，在弹窗中选择**Constructor**，选择一个或多个需要生成构造函数的参数，点击**OK**。若选择**Select None**，则生成不带参数的构造器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/sCA0rKXwT46Gw2J1y-UvKg/zh-cn_image_0000002779567406.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=C266216D2FA64837D03AE0026332948A8157501B072E037E80F701A460F1E943)

## 快速生成get和set方法

编辑器支持为类成员变量或对象属性快速生成get和set方法。

将光标放置在当前类中，单击右键选择**Generate...>Getter and Setter**，或者使用快捷键**Alt+Insert**（macOS为**Command+N**），在菜单中选择**Getter and Setter**，快速生成get()和set()方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/NrE2_7TyQZKY2-snrKNLwg/zh-cn_image_0000002779567412.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=B13FB8C91DD9608989AFAD71ECF43BD02FD125C5F5921B05B7F4A40330B54FC9)

## 快速生成声明信息到Index文件

编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过**Generate...>Declarations**功能，批量在Index.ets文件中进行声明，便于其他模块调用。

在HSP或HAR模块内的文件编辑界面，单击右键选择**Generate...>****Declarations**，或者使用快捷键**Alt+Insert**（macOS为****Command+N****），在菜单中选择**Declarations**，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/R2qpug8-TR-w0W0ljNfmTQ/zh-cn_image_0000002808766991.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004704Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F717ABA42AD3260927DB9683E82CEC96D02B9C23EA1B86ADFCDAFFFD4DF2E98)
