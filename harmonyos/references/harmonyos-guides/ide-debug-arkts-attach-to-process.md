---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:15+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e4ee1cf75b2ac8dc3391e0ee8cdb85ce81a44f5a6263d08ce74d1fc444cd12e5
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/p7jBsEt8Qbyj-DiYnQOdoA/zh-cn_image_0000002701663814.png)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/aT6CYbIjRkirY_QnIyiP2A/zh-cn_image_0000002701823736.png)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/DItsOcI8QXOfjMNlYid1bA/zh-cn_image_0000002701663812.png)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/C0xdXkOcTtGSUYxy8ZVmsw/zh-cn_image_0000002731543013.png)
