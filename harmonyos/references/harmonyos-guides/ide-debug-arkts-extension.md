---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:32294913c599c81df86abe9c5cec89ce1d71b07fc4a20042f2d48dab2ccaaf5b
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/qOxtBjX0RfK9q6M1JHwXaA/zh-cn_image_0000002808887191.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=819964011878EFF4858132C881E70CA7DA52725ECAF88EEEA3A952896A37D18F)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Os5B6Q7NTrKRJI2dSwT0Eg/zh-cn_image_0000002808887189.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=5231832EFD403313AB35DC30BD7E14D2970499F23166C378F72404C5BD075476)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/kyQIrhZURzGrdJ3szpQz2w/zh-cn_image_0000002779407550.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9277049C457D28B5BB3E688E076CFEA7C1D4055B268AE722F2D042CDBEF19AF)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/gGkbE_7oQpmxkiJeEfJp1g/zh-cn_image_0000002779407548.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=C212636AD591D910D861821F019BF4712BF7F75FB2FF7387D18514FF457EEF12)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/KrkcpE3tTmC3mazl9fipTw/zh-cn_image_0000002808767105.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F31BE645C54EF48E8C50677EA8DD7C808D1F2059A4ABC24CB21DD12FEFA9DAD)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/fpJs5jfBRCKkrToceYKh3Q/zh-cn_image_0000002779567526.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=25F9121AE4CF0A1BAEB875CACF53188E3806F39B1C0545C6B1EE95397F930D28)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/U7MX-KYHSy2eXT1Q5nPATg/zh-cn_image_0000002808767103.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0384680A027443F2855431619CD62AE9A589C656E55BD50F4556AAF97143EA8)
