---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f77412b93b0abe8b0a6093c2b487fdbc8972d9565890be58b6bf7ee60585cd09
---

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/gJ4SfbO2QVWpSrQEH7F10A/zh-cn_image_0000002781311202.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8405A1DD2159D70BCFF742FE0858873FBA19F4AA7743439EB62A59C7219D7551 "点击放大")图标，打开断点管理界面进行断点管理。

* 勾选复选框，使能该断点。
* 取消勾选复选框，禁用该断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/3UgFyi4EQ3uEkR4lgKI4Sg/zh-cn_image_0000002810630683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=978C7321D115AA9B23D5212B070105C36FF268C7E616966A041044A7926D972D)

## 条件断点

在编辑器行号侧边栏单击鼠标右键，选择**添加条件****断点**并在输入框中设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/ZKrr-CG3RAmclHLlmqD04w/zh-cn_image_0000002810630689.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FDFE7CA0B15FE16F19FBFC6DB91B84CCE5C3F1BA328E91055A7894A1343C2EC)

## 日志断点

在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点，在输入框中添加表达式，可以使进程运行到断点时在console窗口打印相应日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/jABepRZjQtGqJG3x3ZMDDw/zh-cn_image_0000002810750795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=83884491F1E011F4F34AD13391168102875E2691CD4BC9E9CFBE04178B87EFFE)

**说明** 

未勾选**启用**的断点不会打印日志。

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BzKmfks9TfqO3DFd7NxGug/zh-cn_image_0000002781471132.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9F036BDE6D496810B185DF4502A28E2A9CE38E9B250E682496F56648BC2C5AF "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Wj-nV3v_R8-yjmVJZELk3w/zh-cn_image_0000002781471136.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED76D2D6B6E1160A260A96C65AF8AB5CBA505FF2FC1F8FF9D906308B3959A877 "点击放大")

## 函数断点

也称为方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/6kBGia0JSqq3t555aCZHmg/zh-cn_image_0000002810750789.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7DDB4BFBD3292B16F98BB316CE70F6B199F4ABE3E513A66DAF699E3D204602E)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如SIGSEGV等信号量异常会默认捕获并中断进程。

在断点管理界面中勾选**catch catch**和**catch throw**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/5CrAejpyRQW5N-oS11su8g/zh-cn_image_0000002810750797.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=82B0E8176F4EABC09F382FD9B8DE97304952DB4342E8F6154B5930E1E172FD3A)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/-s61_bBMTcqSabTKg0zatg/zh-cn_image_0000002781311200.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BAE321D0DD3149F7D72AA99DC43EFDB0F402A383EB879817EB8622E48E6042C)

在断点管理界面进行查看和禁用/使能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/EWNQMi5MR7uXS2-_w5BoNA/zh-cn_image_0000002810750793.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B982CAD66A283983F0B80F638223B86B10EB78BED53CF470C552E6C1DD944656)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型size不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置2个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
