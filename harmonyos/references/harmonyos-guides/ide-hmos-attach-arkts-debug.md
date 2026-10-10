---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-attach-arkts-debug
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ce6d3dee2beafa58a32bd0685db34d96b7a31da70e5b33145bed2b77cad3b27f
---

开发者也可以通过将调试程序附加到已运行的应用进行调试。

附加调试和调试的区别在于，附加调试可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而调试是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被附加调试的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

附加调试不支持的场景：

* 本地无源码。
* 应用包名不匹配，将出现提示“**所选进程与当前项目的包名不匹配！**”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/WoM-Tv-rRkWAqEFOAoSfHA/zh-cn_image_0000002779608583.png)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/To7H6GkFT9uJH6tTodNfNQ/zh-cn_image_0000002779608585.png)
2. 选择要调试的应用进程，若应用包名与当前工程不一致，则需勾选**显示所有进程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/tJ6wV4RERouEcFf6MYyZfA/zh-cn_image_0000002779728735.png)
3. 选择需要使用的调试配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/g1ULCtV_TUqetOpoO9MH0w/zh-cn_image_0000002750009670.png)
4. 选择好调试配置进行附加调试后，**调试类型**不可改变，只可在**运行/调试配置**界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/OYuuEUYmTciH2VSjsrkwWQ/zh-cn_image_0000002750169560.png)
5. 点击**确定**开始附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/MbGNqryyRcuOVvVbz-L71w/zh-cn_image_0000002779728733.png)
