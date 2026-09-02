---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-216
title: 编译报错daemon connections达到上限
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错daemon connections达到上限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:71dfe4a4feb65f364c0693061801e828cbcf722f306bb4c382e71922ebca4eb7
---

## 问题现象

项目编译构建报错，报错信息如下：

```txt
hvigor ERROR: hvigor daemon: The number of hvigor daemon connections has reached the upper limit, this socket will be disconnect. Please wait for one of the connections to be disconnected and then try again.
```

## 背景知识

[守护进程](../harmonyos-guides/ide-hvigor-daemon.md)是在后台持续运行的非交互式程序。Hvigor守护进程是一个持续存在的后台进程，可以减少运行构建所需的时间。

## 问题定位

根据报错提示，Hvigor守护进程连接数已达到上限，使用hvigorw --status-daemon命令查看开启的Hvigor守护进程数量。

## 分析结论

正在运行的守护进程同时最多开启8个，处于运行或忙状态的守护进程最多开启6个。如果开启的数量多于上述数量，则会报错守护进程连接数达到上限。

## 修改建议

取消使用守护进程，在IDE的设置中，点击File > Settings > Build, Execution, Deployment > Build Tools > Hvigor，取消勾选字段Enable the Daemon for tasks。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/hXOhcUBrT6aKrYYA55T4Eg/zh-cn_image_0000002628409286.png "点击放大")

## 常见FAQ

Q：热部署没成功就点击运行，会报如下错误：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/6wbG_qubRIicrjUeB2RKWQ/zh-cn_image_0000002658808557.png "点击放大")

这种报错除了重启IDE还能怎么解决？

A：根据报错内容，正在运行的[守护进程状态](../harmonyos-guides/ide-hvigor-daemon.md#section13943113123411)为busy，上次的构建还未完成。此时可以先用--stop-daemon参数[停止守护进程](../harmonyos-guides/ide-hvigor-daemon.md#section298519112359)，然后用--no-daemon参数在重新运行时[禁用守护进程](../harmonyos-guides/ide-hvigor-daemon.md#section16318421606)。也可以按报错提示直接删除对应文件重新运行。
