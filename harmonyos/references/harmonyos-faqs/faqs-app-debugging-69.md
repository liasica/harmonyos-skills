---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-69
title: 编译构建问题如何获取关键日志
breadcrumb: FAQ > DevEco Studio > 应用调试 > 编译构建问题如何获取关键日志
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:efc42f47256e3f468b2fde283f9c29b8ec3092548275fea8b599ce9b9da00414
---

## 问题现象

在日常开发过程中，会经常使用IDE开发运行项目，也会碰到很多与IDE编译构建相关的问题和报错，那么如何收集信息来定位问题原因？

## 背景知识

* [hvigor-config.json5文件](../harmonyos-guides/ide-hvigor-set-options.md)主要包含以下内容：
  + 指定当前工程的开发态构建工具版本号、构建任务和脚本的依赖版本等。
  + 指定构建工具的相关能力，包括日志级别、执行策略等。
  + 指定构建的运行时node的相关配置参数，以及其他传递给构建脚本的额外参数等。
* [守护进程](../harmonyos-guides/ide-hvigor-daemon.md)是作为后台进程运行而不是在交互式用户的直接控制下运行的计算机程序。Hvigor守护进程是一个持续存在的后台进程，可以减少运行构建所需的时间。
* [Build Analyzer](../harmonyos-guides/ide-hvigor-build-analyzer.md)是一款用于分析和优化项目构建过程的工具，它可以帮助开发者可视化地分析和排查构建过程中的性能和内存问题。

## 解决方案

**Build窗口中编译报错**：

1. 首先获取IDE版本、SDK版本（编译工具链版本，与hvigor强相关）、hvigor版本，以及hvigor-config.json5配置信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7AS4yUWSQiWBpAffWAJZxw/zh-cn_image_0000002628569314.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=861C62946AA86C485FAB3A1C7DB969745D6BFD9AABE7624EED3E5D79403589FF "点击放大")
2. 将stacktrace设置为true，并重新编译，详见步骤3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/nA1Wr7ISS-KYM9UAlU8qwg/zh-cn_image_0000002658928629.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=875C7C926C175C7F315969536BF90E1B1784BD92461B97FC5ECE115CAF7EDD7D "点击放大")
3. 再次编译，给出Build窗口的编译报错信息（含堆栈）。需要完整的包含报错堆栈上下文的完整构建日志（最好是构建报错完整txt文本）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/k3Qp-UXoTtCZT2xoAxHkQQ/zh-cn_image_0000002628409408.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=131298E8F5DF96A624ECE44294CDAC811FA64229491242DF2B0DFB8A16DCFA78 "点击放大")

**daemon类问题**：

1. 获取hvigor版本，需要hvigor-config.json5截图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/fDveDiG-Q1O81oAsI4JkdA/zh-cn_image_0000002658808677.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=7416C3BA0B0DD689CF2031F3854656721CA99A5F5820A3EEEA9D429CA54558AF "点击放大")
2. 在Build窗口获取daemon日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/iT70I3IZRLOKIMB9qws2Jw/zh-cn_image_0000002628569316.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=87C4C9C6DB3698541D75D45EFA1B567D2AB5DD3C8DEEBB5EF21B73207ACB1801 "点击放大")

   如果出现上图报错给出了daemon具体地方，获取该daemon日志即可，如果没出现需要复现问题并重新获取daemon日志。如下获取路径为：C:\Users\xxxxx\.hvigor\daemon\log\5.19.0。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/bOFRlkxjTZSb3LBJ9F_Iag/zh-cn_image_0000002658928631.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=007B649CF162E26F6A4A9502B69F681AED3DF0DF82E6D30DEC125D369ABCA404 "点击放大")
3. 获取idea.log的日志。点击IDE上方选项：Help->Show Log in Explorer。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/3WrtA5VtTh6mVf4qT0UhNw/zh-cn_image_0000002628409410.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7472329097679B062C3F57A719C5921C62BB0F4085FACA283BA731466BF5349 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/XBWdb3M-TD6qLhjcMcqq4Q/zh-cn_image_0000002658808679.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F83F3DBD2D523346060DFC747EED4FB390685E6531CE250B70C003B72CC9E07 "点击放大")

**构建耗时问题**：

1. 获取IDE和hvigor版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/nCMTCAINQpGsMpI2KhRgbw/zh-cn_image_0000002628569318.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=75DFF27DD556EE7877A60762D8A31FE27E7F622BA530407C4CF76EECA044539D "点击放大")
2. 勾选高级模式，并重新构建工程获取新的分析日志。在Settings中搜索Hvigor，勾选Use build analysis mode，选择verbose（旧版本）/advanced（新版本）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/xen2eUULRR22M30P3vlW6Q/zh-cn_image_0000002658928633.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=54DD3B29541E197DEC6D17E6FA34EB8AD0D1FF84983C33AB198B2B059B9FEB74 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/e3YmIcp1SUC_TUTo2L4P_A/zh-cn_image_0000002628409412.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3829B4396EDE93556C3B5B7A64763944436AB4D914144B868A9928A62AB3366 "点击放大")
3. 找到耗时久的任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/BLjhJVTOTGS3iAO2sOaZRA/zh-cn_image_0000002658808681.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=855F86E00438A31AACD0878238F8AC3870FE58CCAFC2F276C149FCA00A174D24 "点击放大")
4. 一直展开，找到耗时最久的几个小任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/biU7tx-aTWKGDB0TpDcP6g/zh-cn_image_0000002628569320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=78F220FF08449DBF643874768A2236F44A984297B5ED8744EC416A39F6E8CACB "点击放大")
5. 最后获取report.json（最好找到此次编译的report.json），点击右上角导出按钮，导出report。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/x6StFFM7QDaL1vUOtmwS2Q/zh-cn_image_0000002658928637.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=88F26485577357124FB7A4BE9768C10F1C5926229A3C172EF409E4A2965462DD "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/VXcbmZHLQiOOGWVfxyJrGA/zh-cn_image_0000002628409414.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC94BE5BC38778077DA8813EA1662DE6C2C16118E57C09EB7ACBBD2D6906E743 "点击放大")

## 常见FAQ

Q：IDE编译项目报错构建信息较多，如何快速定位报错信息？

A：在IDE的Build中搜索“hvigor ERROR”可快速定位到hvigor构建的相关报错信息。

Q：IDE编译的错误信息在build Output输出窗口中会淹没在warning信息，如何快速过滤出来？

A：Build Output下的左边第二个open Build Analyzer下的Tasks，可以点击Error看到具体的报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/D6dWsN1WSxmhBNkLOJfLBA/zh-cn_image_0000002658808683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6ECEDA11048A2A3D1D329A1206386AA201B508CD6229E580B70FFC09BFE5CF9 "点击放大")

## 总结

大部分问题可以通过分析日志发现问题根因，还有部分问题需要结合运行场景和条件进行分析，在收集日志时还需要注意：

* 日志时效性：设备重启后部分日志可能丢失，建议发现问题后立即导出分析。
* 混淆工程：Release包崩溃需通过IDE反混淆工具还原符号表，确保可关联源码。
