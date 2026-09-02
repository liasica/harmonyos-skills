---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-exception-detection
title: 使用方舟异常信息增强检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 使用方舟异常信息增强检测
category: best-practices
scraped_at: 2026-04-29T14:14:04+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9d18e14fe8504700698bd7dfdf84888db850e0aca7eee8d3c86c84505c87889a
---

## 概述

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

## 启用方舟native模块加载异常信息增强

可以通过以下两种方式启用方舟native模块加载异常信息增强

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/J_sivSo9TSCg3kFqpCpReQ/zh-cn_image_0000002404125161.png)

* 方式二

  通过命令行开启。

  ```
  1. aa start {abilityName} {bundleName} -E
  ```

## 启用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/AYqYrVXGQ2myGU8FO1TMnA/zh-cn_image_0000002370405608.png)
