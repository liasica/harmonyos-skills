---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4cb15316c34a4f6195be49359c5c64b9d9cb70c9e627e6e8d615ae78ec2af9d2
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备。
2. 点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GUdCffIcTn-DcJnbrtpojA/zh-cn_image_0000002781311424.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=00BDACBA8F8D35DFB355CE846E91198359A7E64E27D251B76B280866DB6BE12B "点击放大")图标打开日志面板，选择HiLog。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/cjMvzSu1ToukUbdO9qiUdg/zh-cn_image_0000002781471360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=85EE80C5F9D7C37AE6FAA83D96E26A4607EF7DE63795D334E4D56A83D4757A4D "点击放大")，选择保存路径后即可截取屏幕截图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/06qFCPsOTb25c5XXlv0bzw/zh-cn_image_0000002810630911.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E5743B023F1B88FC099A5A4A091BE47389118467FE57B6C365B85A95DE95E6A)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
