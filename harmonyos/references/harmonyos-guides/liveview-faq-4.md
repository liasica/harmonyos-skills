---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-4
title: 关于实况窗模板使用的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗模板使用的问题
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c17c4d39fcf3e3367ac660b2d148f71b6cf5ef8d680eb84ced38e3812687935b
---

## 采用进度可视化模板并且indicatorType为INDICATOR\_TYPE\_OVERLAY时，图片较宽，无法完全覆盖进度条

当indicatorType=INDICATOR\_TYPE\_OVERLAY时，图标区域为64\*56vp，图片较宽时会按比例进行缩放。应用需要自己修改图片大小和样式来达到想要的效果。

理想效果图 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/vBNkd4l2RZ2AEE3lZvWM9Q/zh-cn_image_0000002815399893.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=14E00A8FA9A594639BC87437A4E501E8E106B2D381CAEB39E944B5956D0D43FF)

## 如何修改 "实况窗左上角图标"

除导航模板通过[currentNavigationIcon](../harmonyos-references/liveview-liveviewmanager.md#navigationlayout)设置左上角图标外，其他模板不支持修改实况窗左上角图标，默认展示为应用Logo图标。
