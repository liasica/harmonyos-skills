---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:541d72b19204d3984848b4d1bc2c71b5de8ae93d7256b18f7a017721e3e77f12
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/GSGbdyqkStK-W3oSXhhF2A/zh-cn_image_0000002701663814.png)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/GOJsWA__S8Gk2VrVTzDHyw/zh-cn_image_0000002701823736.png)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/PctDXaQATnOiOp-DbleFUQ/zh-cn_image_0000002701663812.png)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/RJpOSBDeT9amhuPwSW_n2g/zh-cn_image_0000002731543013.png)
