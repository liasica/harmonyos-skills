---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-security-basic-quality-test-2
title: 如何执行安全基础质量测试和查看测试结果
breadcrumb: FAQ > DevEco Testing > 专项测试 > 安全基础质量测试 > 如何执行安全基础质量测试和查看测试结果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-30
content_hash: sha256:bcc49269750813d1a96474faf39a3874b733222a6084976854de0aed1b1923c4
---

## 问题现象

* **问题一：**

  安全基础质量测试如何测试？有什么注意点？测试报告如何查看分析？
* **问题二：**

  DevEco Testing的安全基础质量测试为什么需要选择应用包，不能选择已安装应用？
* **问题三：**

  测试报告中“应用权限申请遵循最小化原则”测试结果不通过如何定位？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ZeB9FbN0Scu4LoEUUgCC8g/zh-cn_image_0000002661536953.png "点击放大")
* **问题四：**

  测试报告中“应用所需权限必须在应用的配置文件中严格按照权限开发指导逐个声明”测试结果不通过如何定位？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/nznr87KZTH6gRpaIrovq1A/zh-cn_image_0000002631177822.png "点击放大")

## 解决方案

* **问题一解决方案：**
  1. 进入DevEco Testing客户端，左侧菜单栏点击专项测试-[安全基础质量测试](../harmonyos-guides/other-test.md#section2492910181110)，选择设备（连接单台设备默认展示设备SN号，连接多台设备时可根据SN号选择执行设备），上传应用包，点击创建任务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/SQ1cFkvlRRitb3U-zu1eOQ/zh-cn_image_0000002631178272.png "点击放大")

     注意点：

     + 支持多台设备同时执行，测试设备中根据SN号选择对应的设备，然后创建任务。
     + 安装包支持hap、app、zip类型，多个hap包的应用可以直接使用app包或者打包成zip来执行安全测试。
     + 系统版本支持HarmonyOS 5.0及以上版本。
  2. 执行完成，如果有检测不通过项，详细日志列点击查看，问题列表-问题描述中可以查看到具体报错信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/4ust8x60SuaEStEY90GzCw/zh-cn_image_0000002631338306.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/DUn5AHoxRx2EvVFcoxOi2A/zh-cn_image_0000002661417607.png "点击放大")
  3. 问题列表中修复指南列点击查看，可以跳转到对应文档，参考文档进行修改。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/kM70WddyRs64WohKUFJdhA/zh-cn_image_0000002631338422.png "点击放大")
* **问题二解决方案：**

  安全基础质量测试会对应用的组件安全、配置安全、通知、选择和同意、向第三方披露等规则进行测试，所以需要选择应用包。
* **问题三解决方案：**
  1. 查看问题描述中所列的异常权限：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/KCuVSCQ2T--gV_q8jto2kw/zh-cn_image_0000002631338492.png "点击放大")
  2. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中requestPermissions字段下面找到问题描述所列的权限，在[应用权限列表](../harmonyos-guides/app-permissions.md)中查找权限名称：确认是否支持、权限是否废弃、权限拼写是否有误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/UXSbq65hS-aeUIQpCuv-Lw/zh-cn_image_0000002661417831.png "点击放大")
* **问题四解决方案：**
  1. 查看问题描述中报错原因（以下为举例）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/ViavN5xuSpiHrwZjrIh87A/zh-cn_image_0000002661537833.png "点击放大")
  2. 在module.json5配置文件中查找该权限，因为ohos.permission.ACCESS\_BLUETOOTH是UserGrant权限，所以usedScene是必填项，需要补充usedScene属性。参考文档[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/54RVQFOARdmL6dEB9Ous2g/zh-cn_image_0000002631178734.png "点击放大")

权限类型确认可查看[应用权限列表](../harmonyos-guides/app-permissions.md)。
