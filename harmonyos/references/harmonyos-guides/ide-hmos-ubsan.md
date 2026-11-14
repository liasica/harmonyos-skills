---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ubsan
title: 使用UBSan检测未定义行为
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用UBSan检测未定义行为
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:e6d67f0af66aee9252e5371b76de255fd29a0dfc565a7453b7bfa601d850faf7
---

代码中出现未定义行为，最初可能不会产生任何问题，但是随着代码的复杂度提高，未定义行为可能造成程序崩溃或发生错误，检测出根源会变得更加困难。UBSan（Undefined Behavior Sanitizer）可以检测代码中出现的未定义行为，帮助用户清除未定义行为引起的运行时错误。

常见的未定义行为有：

* 除数为零。
* 使用未对齐的指针，或未对齐的引用。
* 浮点数转换导致的溢出。
* 访问空指针。

## 使用约束

ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启UBSan

可通过以下两种方式开启UBSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/CNFZ4mjHRvGZ1huROJ1HmA/zh-cn_image_0000002781311260.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=F44C8A57A7668D501D9F32E13693E90E249B3370A39728E51C5B8060E3B2F7BA)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/c5QqbpSkThmtljHBCaHnKA/zh-cn_image_0000002781471196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B8B81676682B1263C175534D79E2F82A961EB85D0F4C71182CB32AE111B6A99 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/SKI3HHH8QEygBKZqAnC_Hw/zh-cn_image_0000002781311262.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=42DCACAA39EC8D111451C16675E97F09243656A2FA3E43482F26381D6C69FD24)
2. 在配置界面点击**故障分析**，勾选**未定义行为检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/0nraURBMT9S3NuMNYwq2eA/zh-cn_image_0000002781471192.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=F87A711C311EAD92140DB73A9F755C492181F2F7980B704431A8E65C39E6E3DE)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加UBSan配置开关。

   ```screen
    "ubsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/7HHncMWGSkG0elHN9kDADg/zh-cn_image_0000002781471194.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF761C0123FC0EFEF7C63F4858EA9E66081F2375634FF594167F5C6ED5013ABE)
2. 在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_UBSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/qPnzw4faRWSEXKh7L5kqaw/zh-cn_image_0000002781311264.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B2F2D5317C5D6DEE1382B4B04DDCA8344F09527B93CF40FA3236E3D8F4F1398)

## 使用UBSan

1. 运行或调试当前应用。
2. 当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](../best-practices/bpta-stability-ubsan-detection.md#section124211321406)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/2EHjwsGvTE-VzIXMRr0EWA/zh-cn_image_0000002781471198.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=088CBB1C9CC9DBC5FCBB7FFAB245DBD85887DA1745C68C6EECBEBD04BBCA446E)
