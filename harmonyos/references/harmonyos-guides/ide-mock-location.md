---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mock-location
title: 位置模拟
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 位置模拟
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a1bde7777efe716a4719c7e644e3efde2c40170c9c6548af890c236762a5d4ee
---

从26.0.0版本开始，新增位置模拟能力，帮助开发者调试和测试与地理位置相关的应用功能。

## 使用场景

* 功能测试：验证地图应用、基于位置的推荐服务、签到打卡、天气应用等功能的正确性，确保应用能准确获取和处理位置信息。
* 覆盖边界场景：无需实地前往，即可模拟应用在全球不同城市或地标的表现。例如，测试应用在东京、伦敦等地的本地化内容是否正确。
* 调试问题：复现仅在特定地理位置出现的Bug，便于快速定位和修复问题。

## 使用约束

* 已通过USB或Wi-Fi连接设备，设备系统要求：API 26.0.0及以上版本。
* 设备需要开启[开发者选项](ide-developer-mode.md)。
* 仅支持debug签名的应用，不支持应用市场上架的release签名应用。

## 操作步骤

1. 点击菜单栏**View > Tool Windows > Device File Browser**，打开Device File Browser。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/i6avEAhJQXmnzag8pmxKOQ/zh-cn_image_0000002808886757.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=38F15078801502D236FE369696D4B054CB16F1FAA7FB234254B49E9F4E9C6E2B)
2. 点击图示按钮，打开位置模拟窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/ODGufm4_SKeSz8OeeZsOFQ/zh-cn_image_0000002808766673.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=61B290051210FA06C99AA89AE3395D3E21DC7621FC37649A8282C0EEF1706C7C)
3. 设置位置信息，提供两种模式。
   * **Manual**：适用于模拟静态位置。手动输入此时所处位置的经度、纬度、海拔以及方位角。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/xIHjuJq5TLu-VPvU0CmpYw/zh-cn_image_0000002808886755.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=70AABBBFFFE92880C7C33076B17B374D8AAC91470783FAE8D0073C45C45D900B)
   * **Replay**：适用于模拟移动轨迹或连续位置变化。点击**Open**导入本地的GPX文件，设置时间间隔后，点击**Apply**即可按设定的时间间隔上报GPX文件中的轨迹信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/cflgWPnuQX-KE6J1VHKe8A/zh-cn_image_0000002779567092.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=E29DED7DC73B337F1F53CBF134D5160BF9A8BA067705E0069888949B9B8CE21B)
4. 如需取消位置模拟能力，将**Virtual location**去勾选，即可恢复使用设备的真实地理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ZDfhHIC3RDGza-avAr2xdA/zh-cn_image_0000002808766675.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=C762EEBDDDE41650355ED5DCF4EFAB2CA68C16AE57B6DCB1F4EE666FC0280291)
