---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-17
title: 场景化性能测试任务创建及执行失败的常见问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 场景化性能测试任务创建及执行失败的常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:282c186c9ce4d64eb0509caad9d8da5aa67b73f2ffe7ef3ca923ca9b29e81578
---

## 问题现象

pycharm中运行官网的Demo，hypium版本是5.1.5.300，提示如下错误：

```py
from hypium.advance.pop_up_window_handler import PopWindowService
ModuleNotFoundError: No module named 'hypium.advance.pop_up_window_handler'
```

## 背景知识

[自定义性能脚本测试（基于Python）](../harmonyos-guides/hypium-perf-python-guidelines.md)：支持开发者使用Python语言为应用编写自动化测试性能脚本，在DevEco Testing提供的场景化性能测试进行性能指标检测并查看测试报告。本指南主要介绍性能测试脚本的开发。

## 问题定位

1. 根据报错hypium.advance.pop\_up\_window\_handler import PopWindowService ModuleNotFoundError: No module named 'hypium.advance.pop\_up\_window\_handle，推断当前hypium框架中没有pop\_up\_window\_handler这个模块。
2. 打开hypium安装目录的下面文件夹：hypium-5.1.5.300.tar.gz\hypium-5.1.5.300\hypium\advance，发现的确没有pop\_up\_window\_handler模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/QbDzi4nISEeDINu2zMleWw/zh-cn_image_0000002658803279.png "点击放大")

## 分析结论

5.1.5.300版本的hypium无pop\_up\_window\_handler模块，导致在使用该模块时报错。

## 修改建议

通过DevEco Testing客户端场景化性能测试获取安装包。操作如下：

1. 进入DevEco Testing客户端-场景化性能测试：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/rNjJhubqRbGH1hbOUZAkXQ/zh-cn_image_0000002628404020.png "点击放大")
2. 选择自定义场景测试，点击获取安装包后，出现新的文件夹目录：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/Ux3k5okyTi21Y5E-TpwQLA/zh-cn_image_0000002628563920.png "点击放大")

   hypium-6.0.1.20b0.tar.gz中存在pop\_up\_window\_handler模块：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/XyZoufS8Rm2bFfiEFF51Lw/zh-cn_image_0000002658923235.png "点击放大")
3. 根据[自定义性能脚本测试（基于Python）](../harmonyos-guides/hypium-perf-python-guidelines.md)重新安装hypium并运行自定义性能Demo。

## 常见FAQ

Q：基于[应用UI测试（基于Python）](../harmonyos-guides/hypium-python-guidelines.md)执行测试用例，报错ModuleNotFoundError: No module named 'telnetlib'。

A：检查Python版本是否是3.10版本，其他版本可能会出现兼容性问题。

## 总结

自定义性能脚本测试（基于Python）需要hypium\_perf能力，目前需要使用DevEco Testing客户端获取安装包，并按照[自定义性能脚本测试（基于Python）](../harmonyos-guides/hypium-perf-python-guidelines.md)指导进行构建性能脚本。
