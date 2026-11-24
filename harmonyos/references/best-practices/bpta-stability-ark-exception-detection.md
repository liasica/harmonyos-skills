---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-exception-detection
title: 使用方舟异常信息增强检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 使用方舟异常信息增强检测
category: best-practices
scraped_at: 2026-11-24T12:47:55+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:aace075530971a858f75f4d91573d53a062eb9235fc524d9fee2e172e0b3e42a
---

## 概述

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

## 启用方舟native模块加载异常信息增强

可以通过以下两种方式启用方舟native模块加载异常信息增强：

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/5MIHRYMGSM66u-dqlF7oOg/zh-cn_image_0000002404125161.png?HW-CC-KV=V1&HW-CC-Date=20261124T044755Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FE13C0B38EB80ED6F84E2D092A5E612BA5581FE49D63152F603AA26B2CD9C7B)

* 方式二

  通过命令行开启。

  ```screen
  aa start {abilityName} {bundleName} -E
  ```

## 启用方舟native模块加载异常信息增强后报错信息显示

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/mX6n77QFR4q40eYIdeBjqQ/zh-cn_image_0000002370405608.png?HW-CC-KV=V1&HW-CC-Date=20261124T044755Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBDCC5082C84631A1527EE05CFFFA25C8B5584A66183DA6B58F8E4597F9CB34C)
