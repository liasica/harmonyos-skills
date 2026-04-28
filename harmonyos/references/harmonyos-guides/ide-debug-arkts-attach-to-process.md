---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8decc242ff4401b9a268a3aeb72608a3c732413983e18958d18b66fb8a2da46f
---

开发者可以通过将某个应用设置为“等待调试模式”，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。

说明

* 应用设置为“等待调试模式”后，此时如果启动普通的debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并单击Run > Attach to Process by Name。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/eu8SoOEDRkiU-SE0dgqPPQ/zh-cn_image_0000002561753735.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=FA3378DA1294221EF7200655C5B17DF5A32B0677BD97514967EA43A425AD7606)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择需要进行调试的调试类型。然后单击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/PC6mzTh8RuCa2SpGirpQTA/zh-cn_image_0000002561753733.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=555CAEB94433A5617C14023923D3F679B53B5E64656694CC38E6CFDCAF151B70)

   此时会在DevEco Studio底部显示一个等待进度条，在应用被拉起之前，将一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ltwjRtSRQ-WlqUlMXu25FQ/zh-cn_image_0000002530913786.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=6C0701BCE3EED78A052057EE85FD07BA06839FFBE19AA5E6592CC39F360E842C)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/No_ALSdmR-2_z5fY8Cw4UA/zh-cn_image_0000002530753796.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=D60995FD6FBE3531650E5A04514C95F851D8A6B99E19D829732ABB94F755CD2B)
