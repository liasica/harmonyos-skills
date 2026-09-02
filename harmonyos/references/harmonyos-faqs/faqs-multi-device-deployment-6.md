---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-6
title: 折叠屏展开态和折叠态下呈现的内容不一致
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 常见问题 > 折叠屏展开态和折叠态下呈现的内容不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f314bf93b5f1494dc1dd9b565d066bc40cf1c79f916e726d67d1a21932ff13f
---

## 问题现象

折叠屏展开态和折叠态打开同一页面时，展开态部分内容缺失。

## 背景知识

* [Web](../harmonyos-references/ts-basic-components-web.md)：提供具有网页显示能力的Web组件。在Web开发中，使用@media实现自适应布局是响应式设计的核心技术，主要通过媒体查询动态调整样式以适应不同设备屏幕。
* [使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)：Web组件支持使用DevTools工具调试前端页面。DevTools是Web前端开发调试工具，支持在电脑上调试移动设备前端页面。

## 问题定位

1. 使用[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)查看页面布局，发现该页面使用了Web组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/KQR_RTkCRFGwXqQqOAXGJg/zh-cn_image_0000002628392504.png "点击放大")

2. 使用开发者工具或DevTools查看Web页面布局，发现在折叠态尺寸下，使用了@media自适应布局，示例代码如下：

   ```screen
   @media (min-device-width: 320px) and (max-width: 689px), (max-device-width: 480px) {
     .w1200 {
       width: 100%;
     }
   }
   ```

   在展开态尺寸下，使用了固定布局，示例代码如下：

   ```screen
   .w1200 {
     width: 1200px;
     margin: 0 auto;
   }
   ```

## 分析结论

当前Web页面在折叠屏展开态下，使用了固定布局，使部分页面被遮挡，导致与折叠态呈现的内容不一致。

## 修改建议

在折叠屏展开态尺寸下，使用@media媒体查询响应式布局，具体可参考[官方示例](../best-practices/bpta-web-adaptation.md#section767285571317)。
