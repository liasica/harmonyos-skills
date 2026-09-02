---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-47
title: 如何在Petal Maps Studio编辑器中修改水的颜色
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何在Petal Maps Studio编辑器中修改水的颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:7d72ab8e392c9dff0b49dd7fd09c41a9d30fe17ff2e39c0262622a820606ee0c
---

## 问题现象

使用Petal Maps Studio编辑器无法手动修改水的颜色，配置JSON的方式则自定义不够精细。

## 背景知识

在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/StyleEditor)编辑器上创建新样式，或导入现有样式定义（JSON格式），可实现将地图样式修改为自定义样式。

## 解决方案

登录Petal Maps Studio平台，以Standard为例，鼠标点击水域部分，在弹窗中点击Water，左侧会显示设置元素和样式的菜单，点击Color下方的调色盘选个颜色，松开鼠标，点击任意位置，颜色值有变化，Color右侧的开关按钮会自动开启，同时右侧水域颜色变化。

导入JSON的方式，参考示例代码[设置样式内容](../harmonyos-guides/map-style.md#设置样式内容)，精细程度可根据[样式参考](../harmonyos-guides/map-style.md#样式参考)自行配置。
