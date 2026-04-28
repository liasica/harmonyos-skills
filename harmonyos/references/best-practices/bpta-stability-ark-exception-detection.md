---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-exception-detection
title: 使用方舟异常信息增强检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 使用方舟异常信息增强检测
category: best-practices
scraped_at: 2026-04-28T08:22:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:13d030257b75ebcfa6fa1855a735b68ee18d2411eef14b9f7e28efffc5b807ef
---

## 概述

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

## 启用方舟native模块加载异常信息增强

可以通过以下两种方式启用方舟native模块加载异常信息增强

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/J_sivSo9TSCg3kFqpCpReQ/zh-cn_image_0000002404125161.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=D4EBDFBF57EF8FE622A73C3C5ACBE2943D4FA2FA175526492A426B5FB552A8C4)

* 方式二

  通过命令行开启。

  ```
  1. aa start {abilityName} {bundleName} -E
  ```

## 启用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/AYqYrVXGQ2myGU8FO1TMnA/zh-cn_image_0000002370405608.png?HW-CC-KV=V1&HW-CC-Date=20260428T002252Z&HW-CC-Expire=86400&HW-CC-Sign=2BA7C38FBDB669A1B5A0DADE4B63B9DEDED8D50F922C1063FC4C2F9632FC997A)
