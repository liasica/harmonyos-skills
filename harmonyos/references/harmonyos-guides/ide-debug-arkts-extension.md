---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b48cf45de8abef54d7edb87de8c171b6c250381ee49f3b067be5601639651124
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/BhrERiU9TeuMr5ik377z9A/zh-cn_image_0000002808887191.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC422430C332327A0DB023B0FB4CE9D88AAD7E65DD5D8E3323A4BA1B40A3AF2F)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/QJoDtvrNQPS6OOdh5IW3vQ/zh-cn_image_0000002808887189.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BF217F164B874E83411BB80644568C5C1B66F2E7864F8701F97CAC818F0D8C0)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/8_dKRLu7SB-7A6bTqGi90Q/zh-cn_image_0000002779407550.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ECD5307AA1D6D08EF4415CAD34A9F35862C39BFD17483B3059E1745EB9E17A9)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/auJ0nMwLQ4ejVEnU-2QrXA/zh-cn_image_0000002779407548.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1D1AC96B617979D2F7329F6CA49C5563C107FD62FA86AACD2BC194EA56A9A5E)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/iQUs0IXZRQmF-Bz--pOkGw/zh-cn_image_0000002808767105.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A691AABFD3EDD46B0636E5D792A6FC1E53EBF390DF59FC8FA96CE03E9AC9183)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Ya-AJGjkT1-S6RAcmWKUqA/zh-cn_image_0000002779567526.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8BE64A953D09563E17A5F3C3F4668E416843D0F7A3817FA24B3A75190F185C5)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/WnwL1rFrT4KNRL39VzZU5A/zh-cn_image_0000002808767103.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AE1F03FF07B2EB32030BAA8A510BFD2B69EA2DD0BAB0841EE922EF113770908)
