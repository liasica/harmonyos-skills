---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-4
title: 关于实况窗模板使用的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗模板使用的问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ab646ff818610765749dc7b6acb52ca34826e08feed62454d72cfcf232020dd
---

## 采用进度可视化模板并且indicatorType为INDICATOR\_TYPE\_OVERLAY时，图片较宽，无法完全覆盖进度条

当indicatorType=INDICATOR\_TYPE\_OVERLAY时，图标区域为64\*56vp，图片较宽时会按比例进行缩放。应用需要自己修改图片大小和样式来达到想要的效果。

理想效果图 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/pbsN-83bSUm8c7d1Jd-F8Q/zh-cn_image_0000002817507553.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD09ADD1E4C45ED6B1D1755D54D270DC49631DEC5A0C73FC8AD0261251A92F68)

## 如何修改 "实况窗左上角图标"

除导航模板通过[currentNavigationIcon](../harmonyos-references/liveview-liveviewmanager.md#navigationlayout)设置左上角图标外，其他模板不支持修改实况窗左上角图标，默认展示为应用Logo图标。
