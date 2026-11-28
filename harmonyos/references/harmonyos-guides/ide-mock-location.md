---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mock-location
title: 位置模拟
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 位置模拟
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0433315fe701ec47680d927fe10b4372c4fd3337f7ef9775f83f11c705c894c2
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ZFqZrOXERhmts82EJ_DbOw/zh-cn_image_0000002808886757.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=70F15D452E23891970A43E00F7CC603AB605EF1BFC8072B1A004B8BE72CEDC15)
2. 点击图示按钮，打开位置模拟窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/4e35Q76_Tbi_RDBzSMY0KQ/zh-cn_image_0000002808766673.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=41BE0F72613771E7014BE789CC3A985039E5A865B1C71B188A3AB4EFF24AADE1)
3. 设置位置信息，提供两种模式。
   * **Manual**：适用于模拟静态位置。手动输入此时所处位置的经度、纬度、海拔以及方位角。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/pNxLGTU7QmO-fr3L4bU89A/zh-cn_image_0000002808886755.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=1905BEC3258CCE5A5D061B56652D7409E7EB41A3FF0AD0BF5D3A0CC467021428)
   * **Replay**：适用于模拟移动轨迹或连续位置变化。点击**Open**导入本地的GPX文件，设置时间间隔后，点击**Apply**即可按设定的时间间隔上报GPX文件中的轨迹信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/pwJZi0q2QmO0kZ5pIlcdUw/zh-cn_image_0000002779567092.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=C215DC6A5C386F157AAAA50B525306C56C4FD9ACBECFAFF707BAEE7AB75A15F4)
4. 如需取消位置模拟能力，将**Virtual location**去勾选，即可恢复使用设备的真实地理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/p3GcHBdgSSmUj_i1DEg0GA/zh-cn_image_0000002808766675.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=F246315E0ECD9D521EB6A18A504142B5441A48AAE8550923CD9A07368899E03B)
