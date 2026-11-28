---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:d3a21d144145dd8ffbbc285d7c5e6e93d05e6dbcbcbea9e0473b234e6d2afb4a
---

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/v_IHDMs1SaKZOiNG0V6QCw/zh-cn_image_0000002820720955.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3B53F49121225909156C58B2D0F4BDD871F6671132ED68B3F98F2228590B55F "点击放大")图标，打开断点管理界面进行断点管理。

* 勾选复选框，启用该断点。
* 取消勾选复选框，禁用该断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/W2BfN1DGTOuIR-nNIqE4bQ/zh-cn_image_0000002791841014.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=36E94064A627720C7AD66BF319E005C9F193C6167284D25F3067C64C534C96B7)

## 条件断点

在编辑器行号侧边栏单击鼠标右键，选择**添加条件****断点**并在输入框中设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/uGaOklgKS82qoW-kr9PFwA/zh-cn_image_0000002792000990.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=22B5A9FFA3E3BAC318537BA713E33DF4F6E28FD594F89EFF6174596FBFB6BD09)

## 日志断点

在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点，在输入框中添加表达式，可以使进程运行到断点时在console窗口打印相应日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/RrT9sGcrS4C3Q5mipwREfg/zh-cn_image_0000002791841020.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C4334B1E9CDE8F9E39D9F45E7DD368E601F2EF02DBB342FAE8D2E11850141F8)

**说明** 

未勾选**启用**的断点不会打印日志。

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/EYKhwPwjR6eMbDzJrRu9GA/zh-cn_image_0000002791841012.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=906E5496F8F38688308EDD4E2A51F96A447104750D00ED6460EA4770FA263B68 "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/rpqWIsIdTNKpax4dDLzdcA/zh-cn_image_0000002820680949.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=472156194A7F3AC75BBE3209CF169A5F5379F55A85F558CEF33F1C4C86210641 "点击放大")

## 函数断点

也称为方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/1JPgdIVnSSuEhG1Ew90zEA/zh-cn_image_0000002792000986.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A60BCCE2F26342FDEB5E947BBC08564136B7A1374CF1D21EAA2EA07C2CE6A914)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如SIGSEGV等信号量异常会默认捕获并中断进程。

在断点管理界面中勾选**catch catch**和**catch throw**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/y30Kt0u5SWOzOUdXPvIWYQ/zh-cn_image_0000002820680947.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B1F2095999AD00628EC30B16E87E1FA8E0586A87361784A772022B7330D7EE1)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/vovWm2C9T6Ou298hKSlaiQ/zh-cn_image_0000002791841016.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC2692EF5D05C7CB406E507F2C4ECC8C3DEE6407B9B6F28B81F02B6037366AAC)

在断点管理界面进行查看和禁用/启用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/sCoMQ2PuTQirDp0CgIKqyg/zh-cn_image_0000002820680951.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=6963E344717165F76DE06DD7D3A13B0B916943C6D592557F70E408C109A54FCE)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型size不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置2个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
