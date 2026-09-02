---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-65
title: 如何解决关闭开发者选项后应用白屏问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何解决关闭开发者选项后应用白屏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fefa0d44094ad7ca79652257286372f7c18095bddb24c816d0051868968c17ad
---

## 问题现象

手机升级系统后，原先安装在手机上的应用白屏/卡在启动页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/DkDB8U6RRBSm-pknp_KDlg/zh-cn_image_0000002658928627.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w79uUf4zR2CNfiR0tdiiHw/zh-cn_image_0000002628409406.png "点击放大")

## 背景知识

[开发者选项](../harmonyos-guides/ide-developer-mode.md)：HarmonyOS系统上的“设置”包含开发者选项的界面，用于辅助HarmonyOS应用程序开发、测试及优化，面向开发人员提供商业发行版之外的功能（如API能力），提供更多的调试选项及能力；开发者可在该界面中通过配置选项来分析和调试应用。

## 解决方案

* **方案一**：开启开发者选项。

  定位问题时抓取日志，开启[开发者选项](../harmonyos-guides/ide-developer-mode.md)后，应用正常打开，问题修复。原因是Debug证书编译打包的应用，仅适用于调试应用，需要真机开启开发者选项。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nQvQ9Y3PQQSY6G3qzvHRrQ/zh-cn_image_0000002658808675.png "点击放大")
* **方案二**：邀请测试。

  问题定位期间，推荐开发者使用[邀请测试](../app/agc-help-invite-test-0000002270829393.md)来测试应用效果，邀请测试需要上传Release模式编译的APP包。

## 常见FAQ

Q：升级到最新版本之后，使用有异常，比如：左右滑动屏幕时，屏幕上会出现闪烁的黑线。

A：可能存在缓存问题，建议尝试重启手机。

## 总结

1. 样机升级系统后，建议先开启开发者选项。
2. DevEco Studio识别不了样机，先检查开发者选项，再[排查HDC](faqs-performance-analysis-kit-32.md)。
