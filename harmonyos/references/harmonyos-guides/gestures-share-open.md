---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-open
title: 打开设备侧隔空传送开关
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 隔空传送 > 打开设备侧隔空传送开关
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:141b5de24e7a5900d291c22954499f88145deef84905795bc1ef1ae314f5a41a
---

使用隔空传送功能前，需要先打开隔空传送开关。

开启路径：设置 > 系统 > 快捷启动和手势 > 隔空传送。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/qQZ0p5jDRFiXZnDRhmKpQA/zh-cn_image_0000002583439239.png?HW-CC-KV=V1&HW-CC-Date=20260427T235104Z&HW-CC-Expire=86400&HW-CC-Sign=B83150826A59D7236756F535FC0B67C679440DE864A450F8CD0E55659805E58A)

## 隔空传送与隔空截屏的联动

隔空传送与隔空截屏使用相同的手势触发，开关是否开启影响如下：

| 隔空传送开启 | 隔空传送关闭 |
| --- | --- |
| 隔空截屏开启：图库场景传输原图；其他场景传送截屏。  隔空截屏关闭：图库场景传送原图；其他场景无截屏，不传送。 | 隔空截屏开启：仅截屏，不传送。  隔空截屏关闭：无截屏，不传送。 |

当隔空传送和隔空截屏开关同时开启，且当前界面已注册隔空传送事件时，用户抓取握拳会同时触发隔空传送和隔空截屏，此时隔空传送的卡片下方同步出现保存截屏的提示（首次默认不保存）。

用户可手动勾选“保存截屏至本机”，则传送的同时截屏图片会被保存至图库。系统会记录本次选择结果，并作为下次操作的默认值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/7sY4bKNVT7qgEomGhGzw_A/zh-cn_image_0000002552959194.png?HW-CC-KV=V1&HW-CC-Date=20260427T235104Z&HW-CC-Expire=86400&HW-CC-Sign=3B5840C9445DE41BF5113C97DF112C38ADF065543C7DC666ABE031F3DA6BB38F)
