---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b0545d0c88dc6553ee41e3ff466c999823e4c3caaeeb659ad783ba11c17d8483
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备。
2. 点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Hd-T7ddOQkmcfK4guyQkaA/zh-cn_image_0000002792000896.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0554186A0441A2B1BECA40B4EF2B7BF8327E6A526EEAF5CD0BFC703F0C9AD425 "点击放大")图标打开日志面板，选择HiLog。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/TRTFQyrTT6KPTcgt-lairg/zh-cn_image_0000002791840930.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=43423B8D8D21C9AEA73E24D68C9901F4F90B160F4573FBBBA747495A0D4F2EDA "点击放大")，选择保存路径后即可截取屏幕截图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/FhlLIPtORnyCx6A52nYj9g/zh-cn_image_0000002820720865.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=26C3E0ED258261F60587FB54C081590A3D5BE1EA4DDDBE71AF77EF10E18C5486)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
