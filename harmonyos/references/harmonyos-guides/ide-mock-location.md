---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mock-location
title: 位置模拟
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 位置模拟
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fc2b3f3eac19dbe20865715a57a75f35f3717c2b16672b24e998456dad5544db
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/KyWwExZ8QAu-m7KkXvkPLA/zh-cn_image_0000002808886757.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=91D54238F7367C715558EB2474E259DC22F69BECB37182222F1BA9DA70ED7210)
2. 点击图示按钮，打开位置模拟窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/PsCatOlXRaejQcJ-JQttKA/zh-cn_image_0000002808766673.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=1179E78A2942B6547F21C745D9F8ACCE2B59A2FCAEEF413D3545EFBF9F5B4377)
3. 设置位置信息，提供两种模式。
   * **Manual**：适用于模拟静态位置。手动输入此时所处位置的经度、纬度、海拔以及方位角。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/6iq1eb76TEyL00yPcANutg/zh-cn_image_0000002808886755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=E58A678A18CC8ABC096E4844A6A785B4B626264171CADCD807B9CD2FF1BEDFCF)
   * **Replay**：适用于模拟移动轨迹或连续位置变化。点击**Open**导入本地的GPX文件，设置时间间隔后，点击**Apply**即可按设定的时间间隔上报GPX文件中的轨迹信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/QgMrAw9lTNuYr9SgNye2cw/zh-cn_image_0000002779567092.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=967D89C4CBA7183E7569ADEB06D7AB96285A8EA5F128E35DEC5E217B819FA018)
4. 如需取消位置模拟能力，将**Virtual location**去勾选，即可恢复使用设备的真实地理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/b8v0_PxvR56h4wNpvD3QYQ/zh-cn_image_0000002808766675.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E0DEECAEE7733D546975F9D8F96DA8CDDD09D3396B445F7070E46A83CBF9C8A)
