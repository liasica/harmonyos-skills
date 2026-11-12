---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cb15851fdfc420da528bea6d7dbc86f282c8e06cf6b6bb6c59ffb2ffe20ff45a
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/tMhgB7gyS72DJAXVFNHn7A/zh-cn_image_0000002808886869.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F85F38E388E0C60FFB6ECBDA9B458538E7C84A3CB5E36F45BD4869498F383716)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/CRO-wTT6T269cHO1UyAlLA/zh-cn_image_0000002808766789.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC323211C42EDF1CFA5CF51CBF3625A1A9A218AA3AC6695EE01FB4D7744E4357)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/1XjRMW2OSZKa81BbjqhqcQ/zh-cn_image_0000002779407228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=42140DC8FBC274242B8C811EB001249B6CBC648F6858414C2007AB2311203292)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
