---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:79305d00ab91f33bc9af890dc87e3f92d49fe5943d737b159f831d0d8a727cb6
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/7dlzfOGoSyejo4UoLm9W_g/zh-cn_image_0000002808887191.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6066DD4FFDDEA79D735C869BAF6863726F39C3D1CC324C8378E9B2BB2B90444)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/lfQqZvLyRFqlqSkx9LJtQA/zh-cn_image_0000002808887189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B257AC15F15CEFCE6ED995FCEB52435E412C87FA3583088171C0BC9B2E2CFF70)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/PSQnuZtQRmyBm0lhGsafYw/zh-cn_image_0000002779407550.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C8317A9C64C224B383064BA443A0B215FD4941235EBC929F3A76748A9E31B1B)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/l2cw4CyoSzO5fi5dwQyGlA/zh-cn_image_0000002779407548.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=14382C633D37AB008D4CC139C49D720B025022F2D8B023B32BDE9DDCE21E366B)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/1a-0wdMyQg2FdRSuUzl-QA/zh-cn_image_0000002808767105.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=47D4850BA30C1B8DF2DBDBA1CCFC339B748C0EE9FD0FF6A15C823CFDFC808B1F)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/_-TwLg-CSSyENiXLYpgmjg/zh-cn_image_0000002779567526.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FA86B35697F7A381465386085D04ABE944F1991C39B19B7E7A4790C6B7EDC1A)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/4DZfKJzZRiSkeZx-wLBz0A/zh-cn_image_0000002808767103.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=954F2D76D18D2C163C21ED3FAB1125F38D609346CDB2F017E00A77FDF5AC0E8D)
