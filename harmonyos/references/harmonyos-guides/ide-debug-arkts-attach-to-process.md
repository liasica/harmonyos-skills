---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:cf74810feabef26a462d40b2dbba2f64aef392ba0caea5e2cc945b9d3c7cfd31
---

开发者可以通过将某个应用设置为“等待调试模式”，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。

说明

* 应用设置为“等待调试模式”后，此时如果启动普通的debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并单击Run > Attach to Process by Name。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/nb1C2Y3jSD-sWD0VxCBvVg/zh-cn_image_0000002561753735.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=27810A474E95B8BBD35C5E666DC88884784EC236F3C89F445FF41A080C7C51A9)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择需要进行调试的调试类型。然后单击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/pEZob1UQQ7iCohD7F0s2ug/zh-cn_image_0000002561753733.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=06ABF7E2B9B778F19F83DD1AE2A842A55F54001BD7AD72C96ED29855EAB02FE0)

   此时会在DevEco Studio底部显示一个等待进度条，在应用被拉起之前，将一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/BzjpQbjgRjSBbW24gJQ6iw/zh-cn_image_0000002530913786.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=1470B759BFCEE6A5975A8191C8600C25429A65C7B1DDEB4AEA087E424D83EF26)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/OBCii6SbS52Ff1OgIkAnfg/zh-cn_image_0000002530753796.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=0274665ECC2EAE0F428271D02410EE118DF1D84B8EE43BFAC34E2CD51DC7D4A5)
