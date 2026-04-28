---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-deveco-testing
title: 使用DevEco Testing进行稳定性测试
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 稳定性测试 > 使用DevEco Testing进行稳定性测试
category: best-practices
scraped_at: 2026-04-28T08:22:54+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8b7f8b97320b2a8df04d1bf7a630f4c22ecda1db7b69edcb8b76806cdf55decf
---

本文介绍DevEco Testing为HarmonyOS NEXT应用开发者提供的稳定性测试服务，涵盖稳定性基础质量测试和应用探索测试。稳定性基础质量测试依据HarmonyOS NEXT稳定性测试建议，提供应用稳定性基础检测能力，帮助开发者快速上手稳定性测试。应用探索测试采用基于专家经验的智能遍历方法，驱动测试高效执行，构建应用专属测试模型，帮助开发者有效识别应用故障。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/4MdmjCsCQBCIbEUmUdSlCw/zh-cn_image_0000002441736772.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=2FF868C1847001498ABD29A12E057874B44F883E495BC8344F8FEA901EA120AB)

## 稳定性基础质量测试

**稳定性基础质量测试：**根据应用稳定性建议，检测应用运行过程中是否存在应用崩溃、资源过载、内存泄漏等异常情况。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“稳定性基础质量测试”，点击“稳定性基础质量测试”服务卡片，即进入任务创建界面。按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/eEwaKGpKSh6sjFd9bNY5jQ/zh-cn_image_0000002475040597.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=F15B2FADFBD9243C6119DEC1F535BB9DA4E810251EB271E93E7E79B6275CA709)

任务名称：用于标识任务，工具会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备和待测应用。系统版本支持 HarmonyOS 6.0 及以上版本。

选择应用：可选择测试设备上已安装的应用；或安装新的应用，即在测试设备上安装新的应用包。

是否卸载应用：选择卸载应用后，测试时会进行卸载无残留检测，测试任务结束后将自动卸载被测应用。

是否开启多线程检测：打开后，系统支持检测应用多线程安全问题（例如：多个线程并发写入操作）。

是否开启[MemDebug](bpta-stability-hwasan-detection.md#section10791454125320)模式：打开开关以后，会打开被测应用的内存越界检测开关，可以辅助发现和定位内存越界类问题。

说明

**稳定性基础质量测试最佳测试时长建议设置为8****小时。**

**测试执行**

创建任务后，将会跳转到执行页，进入测试环境初始化阶段。待测试环境初始化完成，待测应用被启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uXnmwVGdQw2Fm1HhFRnZUQ/zh-cn_image_0000002475126385.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=73030040DC632A078627227F21876357C86CB76A54E403E6DF1523B68FC446B6)

测试过程中，在测试页面可以看到测试进度、检测状态、实时投屏及执行日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含任务信息、结果统计、检测规则。

任务信息中，可查看当前应用信息、任务执行时长及详细的环境参数（配置信息及环境信息），点击打开目录按钮支持导出 HTML 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/NuEXpGU_QZ6K2_4bKh0mXw/zh-cn_image_0000002475127285.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=E743DA3E681465C23A92238F81736232E545EF28A52CE292700AE90B5E306C0B)

测试概览中，包含结果统计及检测规则，可直观查看本次任务中，测试项检测结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/9pJwnwqjQOilRfZd7ojqHg/zh-cn_image_0000002441728014.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=281E75F11A89D658F5A4F8C893E27CD155834A540F29476F54EADAD63E45ADF0)检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/BfK3lF29TJ29Q87Bt7u7GQ/zh-cn_image_0000002475048409.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=536933FD4DC997F101B48D5A3A4BE64CE3BCEE8666DF50F64652F25562CB8BF3)点击查看按钮，支持查看测试过程中的日志，用户可结合问题描述及日志详情进一步分析。

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->稳定性基础质量测试->任务创建页->测试指南中查询。

更多应用稳定性体验优化建议及问题定位，请查阅：[应用稳定性体验建议](../harmonyos-guides/experience-suggestions-stability.md) 及 [CppCrash问题定位](../architecture-guides/common-v1_26-ts_c25-0000002324993158.md)

## 其他专项测试

请参考：[专项测试](../harmonyos-guides/specialized-testing.md)。

## 探索测试

请参考：[应用探索测试](../harmonyos-guides/exploratory-testing.md#section12324184817324)。
