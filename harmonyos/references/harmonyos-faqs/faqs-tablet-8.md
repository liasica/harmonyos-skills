---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-8
title: 平板设备上应用的Web页面中，字体显示过大或过小
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板设备上应用的Web页面中，字体显示过大或过小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ce3e498628d283688185dfb29fea48011509bfb5b2de2974258a8c39ec3d6386
---

## 问题现象

平板设备上应用的Web页面中的字体尺寸与手机设备相比，显示的过大或过小。

## 背景知识

* [ArkWeb](../harmonyos-guides/web-component-overview.md)：提供了Web组件，用于在应用程序中显示Web页面内容。
* [Web响应式布局](../best-practices/bpta-web-adaptation.md)：介绍Web侧如何进行多设备适配，结合Web组件实现在不同设备上的定制体验。内容涵盖相对单位、媒体查询、监听窗口变化事件等多设备适配能力。

## 问题定位

1. 查看对应Web页面网址，在浏览器打开对应网址调试。检查Web页面代码中Text的fontsize设置的值是否为固定值。当尺寸设置为固定值时，会导致在平板上展示时出现过大或者过小的情况。
2. 建议检查Web页面有没有采用相对单位（%、em、rem、vw/vh）、媒体查询（media）、监听窗口变化事件（通过JavaScript注册resize事件）等多设备适配能力进行页面开发。
3. 查看对应Web网页中的head标签是否包含适配移动端的视口元素。

   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
   ```

## 分析结论

Web页面没有采用相对单位、媒体查询、窗口监听事件等方式做响应式布局适配，导致Web页面在平板上展示时，对比手机设备上的比例，字体显示过大或过小。

## 修改建议

采用Web响应式布局，通过相对单位、媒体查询、窗口尺寸监听事件等方法动态变化页面文本元素大小。具体可参考[Web响应式布局的实现](../best-practices/bpta-web-adaptation.md#section7443131674416)。
