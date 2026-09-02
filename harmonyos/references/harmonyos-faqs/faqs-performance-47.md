---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-47
title: 移动滑块拼图验证慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 移动滑块拼图验证慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1f6a1ece1a8da660ce21d9b43b72d49791c1beb7d6b5d0e87b75c8ec1188ec87
---

## 问题现象

在移动滑块到图片中指定地方松手后，安全验证较慢，等待一段时间图片验证码才消失。

## 背景知识

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevTools：一个Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力。开发者通过[setWebDebuggingAccess](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口开启Web组件前端页面调试能力，利用DevTools工具可以在电脑上调试移动设备上的前端网页，更多详细内容可以看[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。

## 问题定位

1. 使用ArkUI Inspector抓取图片验证码页面，发现该页面为Web页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/idXajyS1QPS_TAFI16dseA/zh-cn_image_0000002658794565.png "点击放大")
2. 使用DevTools录制图片验证码验证过程，在搜索框中输入touchend找到手指从屏幕移开的时间点为03.270左右，查看该时间点后未发现有较长耗时的网络请求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/HgceNMsmS5uHaUQWZKJdZg/zh-cn_image_0000002628555200.png "点击放大")
3. 排查图片验证码开始消失之前网页执行的任务，发现在05.049时间点有触发计时器，推测是在执行安全验证时有延迟操作，同时在该时间点附近有进行query（查询）网络请求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Ttp81itRSk69ErI1Qo3GYA/zh-cn_image_0000002658914521.png "点击放大")
4. 在搜索框中输入setTimeout，发现在03.548时间有设置超时1.5s的计时器，与上述触发计时器的时间点吻合。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/OCeVCGS7S7yRb0xZ5afFgw/zh-cn_image_0000002628395290.png "点击放大")

   查看手指离开屏幕到设置计时器的过程，发现有进行网络请求，耗时257ms左右。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JV7pBA0uTBew62Mb-pQnvw/zh-cn_image_0000002658794567.png "点击放大")

   综上可知在手指离开屏幕后，应用网页有触发网络请求进行验证，然后延迟1.5s后才隐藏图片验证码，导致验证慢的问题。

## 分析结论

在移动滑块拼图验证时执行了延迟操作，等待一段时间才隐藏图片验证码，引起拼图验证慢的问题。

## 修改建议

1. 减少计时器的超时时长。
2. 添加验证过程中的状态提示。
