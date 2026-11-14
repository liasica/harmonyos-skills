---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-exception-detection
title: 使用方舟异常信息增强检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 使用方舟异常信息增强检测
category: best-practices
scraped_at: 2026-11-14T08:54:17+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:b62fe0a2886739c1800286c3057f864be6b05a8641f1c05e96f43a15e56afe63
---

## 概述

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

## 启用方舟native模块加载异常信息增强

可以通过以下两种方式启用方舟native模块加载异常信息增强：

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/bw-CKJtGR1yYH_I_l7jIzw/zh-cn_image_0000002404125161.png?HW-CC-KV=V1&HW-CC-Date=20261114T005132Z&HW-CC-Expire=31536000000&HW-CC-Sign=647D66C3AED3A4AD693B3904C7D7336C336AEC3A2E4BE8C26F556A3FEEBC011B)

* 方式二

  通过命令行开启。

  ```screen
  aa start {abilityName} {bundleName} -E
  ```

## 启用方舟native模块加载异常信息增强后报错信息显示

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/GB0PQvyNQsSF_q-fX16xdg/zh-cn_image_0000002370405608.png?HW-CC-KV=V1&HW-CC-Date=20261114T005132Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCB32A5B28FCA8187316E3BEA38771590DD8F712B298760910D9E9E411EAB3BC)
