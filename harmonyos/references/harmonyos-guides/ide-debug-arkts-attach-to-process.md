---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b1901829d2ebe7beddd791e0a764f21e5cf2cfc7780bc18bc88b697b4840565b
---

开发者可以通过将某个应用设置为“等待调试模式”，需要调试时拉起应用，即可快速进入调试状态。

**说明** 

* 应用设置为“等待调试模式”后，此时如果启动debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并点击**Run > Attach to Process by Name**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/43M-AYYQTxSY3Qswc7u1Ag/zh-cn_image_0000002779567310.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=A16B2334E64793AC7299FC8DBAA94E2B28F8AA7E2046759D1A8C989BB939094E)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择调试类型，点击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/crb6LPZASU6NQR2KXQKqxA/zh-cn_image_0000002779567308.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=2769EB70C3E92FE1A0F5E85B0848BC8AC8859D8A2E56727C928708F88F6E55D4)

   此时DevEco Studio底部会显示一个等待进度条，在应用被拉起之前，一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/yfClMJE9S4Kj0LKkT5gZfw/zh-cn_image_0000002779407328.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=17452FDFD57D9C5FD949F4D23B066E04E555905E78907658CC4AF20184A32FB6)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/ALVhc-QeQ6GAEHdq5k2reA/zh-cn_image_0000002808766889.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D3289F851701D75E6139B64A6E429A2080D9D3E395221F9408EE62313B0C5E4)
