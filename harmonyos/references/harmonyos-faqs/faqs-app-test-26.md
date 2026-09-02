---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-26
title: 使用命令行执行单元测试脚本常见问题和解决方案
breadcrumb: FAQ > DevEco Studio > 应用测试 > 使用命令行执行单元测试脚本常见问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0b8ee947596e8b13ad361474bfc2ad6d1baaa28ded045e6d9a32294b2977afed
---

## 问题现象

* **问题一：**

  使用cmd方式首次执行单元测试：hdc shell aa test -b com.example.myapplication -m entry\_test -s unittest OpenHarmonyTestRunner -s class ActsAbilityTest -s timeout 15000执行失败，报错：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/oMxFyOU4QrO2w2tBIvVeOA/zh-cn_image_0000002628409558.png "点击放大")
* **问题二：**

  使用命令行执行Local Test的时候，使用shell脚本或者在Python脚本的os.system()执行hvigorw test命令，单元测试用例不会执行；直接在Terminal下执行命令hvigorw test命令则可以正常执行。

## 解决方案

* **问题一解决方案：**

  **报错原因**：直接在cmd窗口执行脚本时需连接硬件设备，并将应用包entry-default-signed.hap和测试文件包entry-ohosTest-signed.hap安装到测试设备上，然后在cmd窗口中输入命令执行。在连接设备后，如果直接输入aa命令，由于设备上没有安装应用包和对应的测试文件包则会报错。

  **解决方案**：对于上述报错，可以通过以下两种方法解决：

  1. 先通过[DevEco Studio执行测试脚本](../harmonyos-guides/unittest-guidelines.md#deveco-studio执行测试脚本)，会自动把应用包和测试文件包安装在设备上并完成测试，然后在cmd中输入命令执行，即可执行成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/UScgPwbsS1CelGdQVPGrpA/zh-cn_image_0000002628569456.png "点击放大")
  2. 手动把包安装到设备上，在菜单栏的右上角点击run按钮完成包的编译。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/mGvzIw9ZQiaV56bKQ-k-SA/zh-cn_image_0000002658928775.png)

     然后执行下面的命令手动把包安装在测试设备上，然后在cmd窗口输入命令即可执行成功，安装命令如下：

     hdc install工程存放的本地路径\工程名\entry\build\default\outputs\default\entry-default-signed.hap

     hdc install工程存放的本地路径\工程名\entry\build\default\outputs\ohosTest\entry-ohosTest-signed.hap

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/g0e0t7RxQiq13cyAHD-AHQ/zh-cn_image_0000002658808827.png "点击放大")
* **问题二解决方案：**

  因为脚本执行环境缺少必要的环境变量，测试用例的路径解析依赖当前工作目录，脚本执行需切换到项目根目录。Terminal中执行hvigor、ohpm等命令时，默认使用内置的环境变量，无需额外配置。
