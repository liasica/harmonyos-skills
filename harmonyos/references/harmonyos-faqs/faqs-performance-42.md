---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-42
title: 在应用内各页面跳转时需要等待加载
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 在应用内各页面跳转时需要等待加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f7047f6fcf9e949025387376b3e545990eae915d7ccd450cbca85f537b46f1d
---

## 问题现象

在应用内各页面相互跳转时，需要等待一段加载时间。

## 背景知识

* ArkWeb分析：应用开发过程中，通过将WebView嵌入APP中以提高开发效率，可能面临ArkWeb加载和丢帧等问题。DevEco Profiler提供ArkWeb分析模板，可以结合ArkWeb执行流程的关键Trace点来定位问题发生的阶段。更多详细内容可以参考[加载丢帧：ArkWeb分析](../harmonyos-guides/ide-profiler-arkweb.md)。
* Launch场景分析：开发应用或元服务过程中，启动速度是一个关键指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。更多详细内容可以看[冷启动分析：Launch分析](../harmonyos-guides/ide-launch-overview.md)。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* DevTools：Web组件支持使用DevTools工具调试前端页面。DevTools是一个Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力。开发者通过setWebDebuggingAccess()接口开启Web组件前端页面调试能力，利用DevTools工具可以在电脑上调试移动设备上的前端网页，设备需为4.1.0及以上版本。更多详细内容可以看[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。

## 问题定位

1. 使用DevEco Profiler ArkWeb模板抓取应用内各页面相互跳转的Trace，搜索关键字H:NWebImpl | CreateNWeb无结果，说明应用内各页面跳转时并未创建新的Web。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/6A9qXISQS9CX00pY9FRD7w/zh-cn_image_0000002658914509.png "点击放大")
2. 使用ArkUI Inspector发现应用从首页开始即为Web页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Zg5dORUcTm60iLTI5FuHhw/zh-cn_image_0000002628395278.png)

   使用DevEco Profiler Launch模板抓取应用启动过程Trace，搜索关键字H:NWebImpl | CreateNWeb，可以找到应用在加载主页面后创建了Web组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/rdGLfjuNSC2AIF6s-wSE5w/zh-cn_image_0000002658794553.png "点击放大")

   结合步骤1可以得出应用在启动时创建此Web，后续应用内的各页面跳转均在此Web中完成。
3. 使用DevTools分析网页内各页面跳转的性能。在“性能”页签下的“网络”模块可以看到存在下载图片资源耗时1秒以上以及执行脚本耗时1.3s以上的情况。是子资源加载、脚本运行耗时导致的页面加载耗时长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/AVnJlTejTlCgeLjs-A9GyA/zh-cn_image_0000002628555190.png "点击放大")

## 分析结论

应用内各页面跳转加载耗时是网页子资源加载、脚本运行耗时较多导致。

## 修改建议

通过[预下载优化](../best-practices/bpta-web-develop-optimization.md#section11708113212514)提前下载页面所需的资源。
