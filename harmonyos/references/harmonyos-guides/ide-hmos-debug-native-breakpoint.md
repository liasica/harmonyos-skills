---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:728f8612be911133fac310f34f3528d353cad5e865eefeb063290b245719b982
---

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/YdUiYQDiRCmLRNRxKHqV2w/zh-cn_image_0000002820720955.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7829227CF73DCB132F9514070DFE58F4446CCA733C8FAE9C0581A10FF56F870C "点击放大")图标，打开断点管理界面进行断点管理。

* 勾选复选框，启用该断点。
* 取消勾选复选框，禁用该断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/L6YbfK79SNWFSv6HDkcIxw/zh-cn_image_0000002791841014.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CE66F06D62AA4B25BDC6130C732E1F4EBB0CDB9A17EDB6F9D1A319D5086097E)

## 条件断点

在编辑器行号侧边栏单击鼠标右键，选择**添加条件****断点**并在输入框中设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Nvf8WVzIQ7GmDVcOB2vRfQ/zh-cn_image_0000002792000990.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3558ACF485E60E868929734005B2EDE4E22C9ECBC8FE032B0B379D708BC93DE)

## 日志断点

在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点，在输入框中添加表达式，可以使进程运行到断点时在console窗口打印相应日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Z5-mSOUGQr2CegnPNbll9w/zh-cn_image_0000002791841020.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0EBEB0C5CDFC7CD2559861884C854E4B1882369250674571B369F3A8B89B2A7)

**说明** 

未勾选**启用**的断点不会打印日志。

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/oaS7OMAGShi_ZGo6ZMIT2w/zh-cn_image_0000002791841012.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=61205F8947C1329B760D375D44BE2A03B9B9C2C1105ACE9060DF3130B5F33B00 "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/5ycrw_vdRxa-qugO40Oh2Q/zh-cn_image_0000002820680949.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C9564668A40E00DB0C224D42DC10AE438D3ECF1329DEBEE9F89F993E89FD298 "点击放大")

## 函数断点

也称为方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Vu84cP7ETZ-YkBsFKL6Q0A/zh-cn_image_0000002792000986.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A865D9D1C7F274C025F22AF2B6BC8D33EF2A287A30CD81EEF60A847635B1EF83)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如SIGSEGV等信号量异常会默认捕获并中断进程。

在断点管理界面中勾选**catch catch**和**catch throw**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/KAZ6UgfrTqCTIpk3A6S6Mw/zh-cn_image_0000002820680947.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=53E46404A79F65046D364DDBC1E0FDC13556371AF7FF588752A4338F47E12E6C)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/ppKeTsfzRJOWRGo7CiGe6Q/zh-cn_image_0000002791841016.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8DD6790A05CD6469047C55470959BCFE817DCD454D9338BDF8E0BA570C99417)

在断点管理界面进行查看和禁用/启用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/yqgGV4fmTda7zF7KCFCVHw/zh-cn_image_0000002820680951.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2CA31DB2358A1FCFA477DD96447E174944F595CA19F442C54AAF5655760D9DA)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型size不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置2个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
