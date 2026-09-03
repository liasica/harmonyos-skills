---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mock-location
title: 位置模拟
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 位置模拟
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9063df3db4922dafca5c25d5bdb18699e9d0f3a7cfed06a81c0c1151410907d9
---

从26.0.0版本开始，新增位置模拟能力，帮助开发者调试和测试与地理位置相关的应用功能。

## 使用场景

* 功能测试：验证地图应用、基于位置的推荐服务、签到打卡、天气应用等功能的正确性，确保应用能准确获取和处理位置信息。
* 覆盖边界场景：无需实地前往，即可模拟应用在全球不同城市或地标的表现。例如，测试应用在东京、伦敦等地的本地化内容是否正确。
* 调试问题：复现仅在特定地理位置出现的Bug，便于快速定位和修复问题。

## 使用约束

* 已通过USB或Wi-Fi连接设备，设备系统要求：API 26.0.0及以上版本。

## 操作步骤

1. 点击菜单栏**View > Tool Windows > Device File Browser**，打开Device File Browser。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/IEpukAX_SIKhTUTMv70hSQ/zh-cn_image_0000002731382515.png)
2. 点击图示按钮，打开位置模拟窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/87vwZNIsTnCWediB0i2KRw/zh-cn_image_0000002701663292.png)
3. 设置位置信息，提供两种模式。
   * **Manual**：适用于模拟静态位置。手动输入此时所处位置的经度、纬度、海拔以及方位角。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/wypAGlXYS0SMX6XQO-LpPw/zh-cn_image_0000002731542489.png)
   * **Replay**：适用于模拟移动轨迹或连续位置变化。点击**Open**导入本地的GPX文件，设置时间间隔后，点击**Apply**即可按设定的时间间隔上报GPX文件中的轨迹信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/O0dWlMWST3q8YrSGxBClaQ/zh-cn_image_0000002731382513.png)
4. 如需取消位置模拟能力，将**Virtual location**去勾选，即可恢复使用设备的真实地理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/vdJkjPd9RKO42qWFpKu2pg/zh-cn_image_0000002731542485.png)
