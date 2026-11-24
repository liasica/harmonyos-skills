---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:32ad2c79f575231eb3f95f32b2dfbd286fbb1d1899fa04af61f650dd169c454d
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/HZ_b-FW-Q0ODsFKsDVBmPg/zh-cn_image_0000002779567310.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=42D27B32FEC7F559882AAD729E6A0595866A4FFAA2A7A9693A48823067D3F960)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/PHwi0-CgRPuZQEUu0dDcoQ/zh-cn_image_0000002779567308.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=175A2478599FC5D1E035B95D8CD2797F4A1104BC3D846C01D731B7B5C6B17DD7)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/CsLKr_FVT3mautziULlBRw/zh-cn_image_0000002779407328.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D638E782E5D55171CEDD88E8A838B4B03BC112F3F076545ABDCBA68425DB2D5F)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/-vG9w71hTEuEcAYWYDvSew/zh-cn_image_0000002808766889.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E104CB6840C6A6F187759F5D0CD0CDEBCF14E632C02719A6CE4B95C3B0A754D)
