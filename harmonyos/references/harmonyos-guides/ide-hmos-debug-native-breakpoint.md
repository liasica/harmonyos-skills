---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c52b4bc28c74086e48b0e02bc2a03fec43c1fad60dd9a6bb8aaa6413f3b5fdc5
---

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/xs0SFkweRkWd9awOZlHQDw/zh-cn_image_0000002781311202.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF28E705FFDCA1D5F5D5E100B2E707DD2261D9954DBDF11A83CFA6DBB9F2D31A "点击放大")图标，打开断点管理界面进行断点管理。

* 勾选复选框，使能该断点。
* 取消勾选复选框，禁用该断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/i7JHFtRYTCypKCk3YHCVSQ/zh-cn_image_0000002810630683.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=14A8D926A4A4AB7554D92E15736BBCCCE92F62C4753E238F7B68A00D36F7DF76)

## 条件断点

在编辑器行号侧边栏单击鼠标右键，选择**添加条件****断点**并在输入框中设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/pWyRy2eARjuQO8xaaEflTg/zh-cn_image_0000002810630689.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E0D32A49FC59F8AFB7CB2CC2CC4A26E06B65DB1F0A5C57001B4563E283C54C2)

## 日志断点

在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点，在输入框中添加表达式，可以使进程运行到断点时在console窗口打印相应日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/nORKmqM5St-1p4CQDqjMrw/zh-cn_image_0000002810750795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=E83920CE67DB1C2E4A67E5A31428927D31E4CC0204429D3AAAA644D477E5D0CA)

**说明** 

未勾选**启用**的断点不会打印日志。

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Zbs59pJjQPutCXG43w1rZg/zh-cn_image_0000002781471132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C8A1BEBB63FDB93236E59D1AE27770EB00E5E50DE6E5DE985C94EC5CF96CA53 "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Y-dCI0QdTAuxEz70bpGAtA/zh-cn_image_0000002781471136.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EF879451768669A195611C573BDDB80C60EE6D441DAFC26A8738C28C2917BAA "点击放大")

## 函数断点

也称为方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/iHX4ZzRyQHmODh7t2H3HfA/zh-cn_image_0000002810750789.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=9846C4528C735C07CBF04C87E3F95CB897180A26D0C522751AE511A29F6830F9)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如SIGSEGV等信号量异常会默认捕获并中断进程。

在断点管理界面中勾选**catch catch**和**catch throw**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/WJ7TnndtT9KXw4rDgywvpA/zh-cn_image_0000002810750797.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=44DAFCEA8DB0B946327614CFAA8515D3277DD2C9EBE6CF81BB7F7639CF5B9CD4)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tZWIjXyzRmCIRXL6M95vjQ/zh-cn_image_0000002781311200.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A40D1EFDA444A482A2F535CF880EA414B33E7795D414C05A0433E29BD8FB264F)

在断点管理界面进行查看和禁用/使能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Fv36DED1QRWWmjfxbRcHXw/zh-cn_image_0000002810750793.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD5D26574029A3768BE37056729944D048C6BFDD7FA2323BDFEF24C14CF7EBF1)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型size不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置2个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
