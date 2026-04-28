---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-power-basic-quality-test
title: 功耗基础质量测试
breadcrumb: 最佳实践 > 功耗 > 应用功耗检测 > 开发态功耗检测 > 功耗基础质量测试
category: best-practices
scraped_at: 2026-04-28T08:22:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:248793a02b823ac292e75d96ccfd11b5210e682085181afbf96a4863668725bc
---

功耗基础质量测试的适用场景：保障HarmonyOS应用功耗质量和体验满足商用要求，识别应用存在的明显功耗异常，应用上架时，应用市场也会进行功耗基础质量测试，避免应用上架后出现因高耗电导致设备快速发热、续航缩短的严重问题。常用的工具有DevEco Studio开发工具中Tools->AppAnalyzer、[DevEco Testing](../harmonyos-guides/deveco-testing.md)，开发者也可以在上架前进行基础质量测试，提高应用上架的效率。

在应用开发过程中，由于未及时释放资源或接口不合理的使用等因素，常常会出现如下典型的功耗问题。

1. 应用前台不可见动效使用资源未及时停止。应用动画被遮挡或处于屏幕顶层的时候，应用未及时停止动画渲染。
2. 申请长时任务的应用退后台CPU负载大于80%。应用开发过程申请长时任务退后台后未及时释放系统资源。如异常资源持续打印、多线程调用异常资源导致系统负载高等情况。

应用功耗基础质量测试主要涉及前台和后台功耗管控两种场景：

* 后台场景指的是当应用未处于设备屏幕顶层时，用户无法直接看到或进行操作的场景，应用需满足最基本的后台功耗体验要求： 如应用退后台对蓝牙、麦克风、定位等器件的合理使用，持锁资源的及时释放，以及申请长/短时任务的应用退后台后CPU负载约束等。
* 前台场景指的是当应用处于设备屏幕的顶层时，用户可以直接看到并进行操作的场景，应用需满足最基本的前台功耗体验要求：如不可见动效及时停止刷新，音乐类、导航类正确配置应用类型，正确使用平台的视频硬件编码器等。

应用功耗测试需要检测应用前后台功耗管控行为，可以使用DevEco Testing提供的“应用功耗基础质量测试”服务进行自动化检测。为了确保业务场景测试覆盖充分，测试前需进行应用账号登录以及相关业务预置操作，整个测试过程前后台累计操作需持续30分钟以上。

测试完成后，功耗测试报告如下图所示，客观呈现了前后台功耗管控规则整体达成情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/t8cJjvD8QEy93G3SHGn6qg/zh-cn_image_0000002370565348.png?HW-CC-KV=V1&HW-CC-Date=20260428T002236Z&HW-CC-Expire=86400&HW-CC-Sign=F4EEC45FDDB0C49FACF0E0C1A1F72BA3BD9392D19E93138AAC6027BC9F6E57D9 "点击放大")

其中，检测未通过项和异常项可以进一步查询详细的测试数据与日志，用户可通过测试过程截图进行问题复现，查看日志进行问题分析定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/bqu6ceHBSPy9BGu54d6iUw/zh-cn_image_0000002372036910.png?HW-CC-KV=V1&HW-CC-Date=20260428T002236Z&HW-CC-Expire=86400&HW-CC-Sign=F73BF264DA0409EA6F7C53DAFC4612ADB5B0C3944250CDBE98EABB6549752E51 "点击放大")

注意

为了确保功耗测试准确性和稳定性，在测试前需清理设备后台应用、检查应用账号是否登录，测试过程中保持USB稳定连接不断开。
