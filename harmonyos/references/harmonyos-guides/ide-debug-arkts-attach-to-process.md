---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:28d6d7ed8b0b07b7b8fcead12b767439433e771942ed9b2d67ed58b49936e8b1
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/JSCjHgERQ36aQxkTH0y1lA/zh-cn_image_0000002779567310.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=430832999BDA9786C9024459A76F4B8B63E56A2E4BDA197034315110DAEAAF12)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/jS8gVu3jT7-zCWQKsteCrA/zh-cn_image_0000002779567308.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=338795EAF88877C6B8A68ACE0E4C32D930D7E353D98D80CC6264BD33E9C1F888)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/3HdSHMByRmutcNGfZSr4ZA/zh-cn_image_0000002779407328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B57DE9ACDB910421D56B8407A10153B02E0F4E4A9F851B9914F8300ACF549DF)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/2nYOIYt9SOupgjX4_k1Keg/zh-cn_image_0000002808766889.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFD7F87A6C0B77E4CE9C5C1DA95A68ECCDDD8B25753A224E8F888EF56D9ABCDB)
