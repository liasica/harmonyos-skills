---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-attach-arkts-debug
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1f84c6bb7dde4a0fdfc5bdd8af75b814aaeb2997ef337dab60e4d949cf5e0ac5
---

开发者也可以通过将调试程序附加到已运行的应用进行调试。

附加调试和调试的区别在于，附加调试可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而调试是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被附加调试的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

附加调试不支持的场景：

* 本地无源码。
* 应用包名不匹配，将出现提示“**所选进程与当前项目的包名不匹配！**”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/4wyiel8vRZSGH7wa7lFhIA/zh-cn_image_0000002781311070.png)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/cr-nXQkXQtaQQSyYtg37GA/zh-cn_image_0000002810750669.png)
2. 选择要调试的应用进程，若应用包名与当前工程不一致，则需勾选**显示所有进程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/TT_QSyM1R3WPXa1vgy8lRQ/zh-cn_image_0000002810750685.png)
3. 选择需要使用的调试配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/RvApsTeGQ-u7MPJZd6ltZg/zh-cn_image_0000002781471006.png)
4. 选择好调试配置进行附加调试后，**调试类型**不可改变，只可在**运行/调试配置**界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/W7DcSpUUQMWlbpBDLPkZwg/zh-cn_image_0000002781311076.png)
5. 点击**确定**开始附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/AqFWa1QaQmWT8t5Hqvg2ig/zh-cn_image_0000002810630559.png)
