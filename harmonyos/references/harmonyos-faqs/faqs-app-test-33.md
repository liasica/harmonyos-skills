---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-33
title: wukong测试中的常见问题
breadcrumb: FAQ > DevEco Studio > 应用测试 > wukong测试中的常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63d09b16c75cf8ba135b0f4975df7d100f939d8930f8103b2e8e812c46ab8579
---

## 问题现象

1. 执行命令：

   ```txt
   wukong exec -s 10 -i 1000 -a 0.28 -t 0.72 -c 100
   ```

   报错信息：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ZeYiGpJlRmWjzc0Slb9C9A/zh-cn_image_0000002628569520.png "点击放大")
2. 运行单元测试时报错"Error in testUiExample, Can not connect to AAMS"。

## 背景知识

[wukong](../harmonyos-guides/wukong-guidelines.md#功能介绍)、[Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)、[DevEco Testing](../harmonyos-guides/deveco-testing.md)等软件都依赖无障碍子系统，无障碍当前同一时间只允许一个程序进行连接，所以当发生冲突时，会出现报错。

## 解决方案

1. 重启手机。
2. 终止不需要执行的进程。

   比如，要终止对应的单元测试进程，具体步骤如下：

   ```txt
   hdc shell
   ps -ef | grep uitest
   kill -9 uitest的进程号
   ```

   如果要终止对应的DevEco Testing进程，可以按下面步骤执行：

   ```txt
   hdc shell
   ps -ef | grep uitest
   kill -9 uitest start-daemon singleness的进程号
   ```

## 常见FAQ

Q：wukong测试时出现Errorcode:(4005)或Errorcode:(4007)报错，该如何处理？

A：因屏幕显示区域大小变化，导致无障碍获取页面信息失败。该错误不影响测试流程，无需处理。

Q：wukong测试时出现Crash reporting enabled for process:XXX是什么含义？

A：Crash reporting enabled for process:{进程类型}表示crashpad初始化完成，以及进程类型。

渲染/GPU进程创建或销毁：

| 级别 | domain/Tag | 文件名 | 日志内容 | 日志含义 |
| --- | --- | --- | --- | --- |
| INFO | C04500/chromium | crash\_reporting.cc | Crash reporting enabled for process:{进程类型} | crashpad初始化完成，以及进程类型。 |

Q：wukong工具测试过程中如何停止测试？

A：建议在wukong测试执行前提前设置好测试次数、总时长等参数，避免任务长时间执行。执行过程中需要停止wukong测试任务的话，可以使用键盘Ctrl+C进行停止任务，或者使用以下hdc命令重启测试设备：hdc shell reboot。
