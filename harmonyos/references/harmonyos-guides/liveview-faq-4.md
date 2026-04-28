---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-4
title: 关于实况窗模板使用的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗模板使用的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6fbc3e99397c7e91b2a812daa81eb1e7c3cb9d066984fa9a73b10b5b713680d
---

## 采用进度可视化模板并且indicatorType为INDICATOR\_TYPE\_OVERLAY时，图片较宽，无法完全覆盖进度条

当indicatorType=INDICATOR\_TYPE\_OVERLAY时，图标区域为64\*56vp，图片较宽时会按比例进行缩放。应用需要自己修改图片大小和样式来达到想要的效果。

理想效果图 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/eX7H_WScSiiesI39Mz5kEA/zh-cn_image_0000002552958986.png?HW-CC-KV=V1&HW-CC-Date=20260427T234938Z&HW-CC-Expire=86400&HW-CC-Sign=99428F3997F430B8F4B8F3681FF89E5F10180C90B5F9A7A08F4312AB899AF2A9)

## 如何修改 "实况窗左上角图标"

除导航模板通过[currentNavigationIcon](../harmonyos-references/liveview-liveviewmanager.md#navigationlayout)设置左上角图标外，其他模板不支持修改实况窗左上角图标，默认展示为应用Logo图标。
