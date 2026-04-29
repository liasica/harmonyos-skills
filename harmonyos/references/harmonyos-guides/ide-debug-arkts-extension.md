---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0edf0a9ffb7128f4509dab89e321838b1b57cb4ce5da1e5a7d1c0eac56819a50
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/KYjL9sjBSqGVvFpah-jzTg/zh-cn_image_0000002530913458.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=7D847FB5FDDDE7779025A8DE89EDA762BD5A7290CB9E5612CA0BA9BF847F01A8)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_Qni8r4CRk-CzpU5CtSbWA/zh-cn_image_0000002530913452.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=735CD4DFEEAE1EF39C553E09063A57B344D9EBFFEFF1BB89EDEAF6BE4FE78B58)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/7nQtv4PDQWGEpBY-tOzdxQ/zh-cn_image_0000002561833381.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=F43E57BAB0081FEAB4DCE4E488BED66D85A4AAD6D40C4EEDC8FED2370BECAA36)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/NktqqAXcT36_YzdHijOxng/zh-cn_image_0000002561833375.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=B3988A74E685319B18A42E5962916820937E229D2A7984A6079624EB8E549E20)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/nROp_gdkTEuwtHnDdv5Ptg/zh-cn_image_0000002530913454.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=34450290F3729F2A2F98193B7041ABF2239F2DF50B1CAE5CDA8CA2CBCFE262A8)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/SfwIvSyISAew8YS5Z8bRrw/zh-cn_image_0000002561833379.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=BC584E8F8DB48C266B13B3B3315FAC55FF86F9B6140D4A9F091AE99256F1787E)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/8jz03IfsQQyWbF5Puxga0w/zh-cn_image_0000002530913448.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=DC4DFDAD96F6E8187AFE81EE8A43CD596BF9012AC93B135C2EA63032CC7517F0)
