---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-glossary
title: XEngine Kit术语
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > XEngine Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:24834bb098dfada521617e41702543e4207697987d6de2b298aadd4db41b8cbd
---

## A

### Adaptive VRS；自适应可变速率着色

可变速率着色（VRS）是一项先进的图形渲染技术，允许开发者以低于传统逐像素的密度调用像素着色器。自适应可变速率着色（Adaptive VRS）在VRS的基础上，利用实时图像分析结果动态识别并区分画面内容，在高细节区域保持高着色率以保障清晰度，简单区域降低着色率以提升效能。这种基于内容的精细调控，能在人眼不易察觉画质损失的前提下，降低GPU负载，提升帧率与能效比。

## C

### Control-Display Separation；控显分离

基于设备展开态将屏幕划分为独立区域，通过显示与交互解耦，实现上半屏承载核心渲染画面、下半屏集中交互触控的复古掌机级操控体验。

## S

### Subpass Shading；子通道着色

子通道着色是一种延迟渲染技术，将渲染过程拆分为多个子通道，先执行几何Pass再执行着色Pass，可减少过度绘制提升性能。

## T

### Tile-Based Deferred Rendering（TBDR）；基于瓦片的延迟渲染

基于瓦片的延迟渲染（TBDR）是一种渲染技术，它结合了即时渲染（Immediate Mode Rendering, IMR）和延迟渲染（Deferred Rendering）的优点，旨在提高渲染效率和减少内存访问。
