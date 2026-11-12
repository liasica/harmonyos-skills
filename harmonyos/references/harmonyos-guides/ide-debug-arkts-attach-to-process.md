---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:315508f4c4360ded75e008bd4260b7220d51feff9b4f7777356003adf6c00a0a
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/beE1O-FhT3u-o4PoluefEQ/zh-cn_image_0000002779567310.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E5D59A46DD7D414B07F2400142F2E66CAA90FDED65AAD6798A99D20A5519B37)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/KXvTo8SFRg2ljGJyBUJBrg/zh-cn_image_0000002779567308.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F1729E58094FDABE4D96F908C28DD29590C3B516DBF0D623DE9FF98E3AEA42A)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/TK5awwRDRhC3Lg179bsX6Q/zh-cn_image_0000002779407328.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9020E266EE5E5E7E021D0E380592670F29BBA38BF2BAF566CE9E2DFE7DAB271)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/1TMZZIkpQ3ygkhafUmL5QQ/zh-cn_image_0000002808766889.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=32054E9E42AF40EC61E1461A7D73C3D438CD6C4B7C480AD1D9596BF411B4B210)
