---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-open
title: 打开设备侧隔空传送开关
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 隔空传送 > 打开设备侧隔空传送开关
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7dd968274d10591c72affb01f69c12871dcaf0416165e3c60c2be7fba6e5fd98
---

使用隔空传送功能前，需要先打开隔空传送开关。

开启路径：设置 > 系统 > 快捷启动和手势 > 隔空传送。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sUtQJBPhQsS3XL5kv_F-Uw/zh-cn_image_0000002788308342.png?HW-CC-KV=V1&HW-CC-Date=20261114T004832Z&HW-CC-Expire=31536000000&HW-CC-Sign=18C58928181D7F818474D6BA42DC044539E76BE2ED9A41B52DFB84B9B6652BBB)

## 隔空传送与隔空截屏的联动

隔空传送与隔空截屏使用相同的手势触发，开关是否开启影响如下：

| 隔空传送开启 | 隔空传送关闭 |
| --- | --- |
| 隔空截屏开启：图库场景传输原图；其他场景传送截屏。  隔空截屏关闭：图库场景传送原图；其他场景无截屏，不传送。 | 隔空截屏开启：仅截屏，不传送。  隔空截屏关闭：无截屏，不传送。 |

当隔空传送和隔空截屏开关同时开启，且当前界面已注册隔空传送事件时，用户抓取握拳会同时触发隔空传送和隔空截屏，此时隔空传送的卡片下方同步出现保存截屏的提示（首次默认不保存）。

用户可手动勾选“保存截屏至本机”，则传送的同时截屏图片会被保存至图库。系统会记录本次选择结果，并作为下次操作的默认值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/KVG868UuSbmTbSMHlX5OwA/zh-cn_image_0000002817427705.png?HW-CC-KV=V1&HW-CC-Date=20261114T004832Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5CFF6D084ECA1DF3F40E725D5E500179554780CB92625C9F8DBFD77C0E18609)
