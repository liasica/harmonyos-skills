---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/test-kit-overview
title: Test Kit简介
breadcrumb: 指南 > 系统 > 调测调优 > Test Kit（应用测试服务） > Test Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:12+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:33011899b1d88e69bfc302e7b64f719f1b65b062057b1baeabf28285be5d9544
---

## 能力范围

Test Kit为开发者提供了自动化测试框架，框架提供单元、UI和性能测试能力，支持编写ArkTS语言的单元、UI和性能自动化测试脚本，并通过测试结果查看相应功能的实现效果。从API version 20开始，支持性能测试能力。

* 单元测试能力：提供自动化测试的基础接口和运行机制，具体使用方法请参考[单元测试框架使用指导](unittest-guidelines.md)，主要能力如下：
  + 提供自动化用例定义接口，包括测试套定义、测试用例定义。
  + 提供自动化用例断言接口，支持多种方式的断言能力，支持开发者在自动化脚本中灵活使用进行用例断言。
  + 提供预置动作/清理动作执行接口，且支持测试套层级和测试用例层级的执行方式。
  + 提供多种用例执行模式，包括筛选指定测试用例执行、随机执行、压力执行等。
* UI测试能力：提供UI自动化测试能力，测试脚本需基于单元测试框架开发，具体使用方法请参考[UI测试框架使用指导](uitest-guidelines.md)，主要能力如下：
  + 提供控件查找接口，支持多种控件查找方式，如按照控件属性查找、按照控件相对位置查找等。
  + 提供模拟UI操作接口，支持多种类型如点击、双击、滑动、双指捏合等操作，也支持模拟多种外设如鼠标、键盘的操作。
  + 提供模拟窗口操作接口，支持针对窗口进行模拟调整大小、移动等操作。
  + 提供shell命令方式模拟UI操作能力，支持如点击、双击、滑动等操作。
  + 提供监听系统弹框/toast能力，并可获取提示文本。
* 性能测试能力：提供白盒性能自动化测试能力，测试脚本需基于单元测试框架开发，具体使用方法请参考[白盒性能测试框架使用指导](perftest-guideline.md)，主要能力如下：
  + 提供针对指定代码段执行过程的基础性能数据采集能力，包括执行耗时、执行CPU和内存占用数据等。
  + 提供对应用场景化性能数据的采集，包括应用启动时延、页面切换时延、列表滑动帧率等。
* 辅助测试能力：提供命令行辅助测试工具，支持系统状态管理和环境模拟能力，搭载HarmonyOS 7.0.0及以上版本的设备支持此能力。具体使用方法请参考[辅助测试工具使用指导](testhelper-guidelines.md)。

此外，Test Kit还为开发者提供了如下命令行工具。

* HiSmartPerf Device性能功耗测试：支持FPS、CPU、GPU、RAM、Temp等指标的实时监测与可视化展示（Device hap端），以及通过Shell命令行方式进行无屏/有屏设备的数据采集与报告生成（Device daemon端），具体使用方法请参考[HiSmartPerf Device使用指导](smartperf-guidelines.md)。
* wukong稳定性测试：支持Ability的随机事件注入、控件注入、异常捕获、报告生成和对Ability数据遍历截图等特性，具体使用方法请参考[wukong稳定性工具使用指导](wukong-guidelines.md)。

## 模拟器支持情况

本Kit支持模拟器。模拟器与真机存在通用差异，详情请参见[模拟器与真机的差异](ide-emulator-specification.md)。
