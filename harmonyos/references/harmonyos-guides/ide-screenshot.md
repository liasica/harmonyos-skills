---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4160b760d18f79649bcdc9836af9d4341277380b52b987ffc9c2b887a1c43182
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/GQfApdDwRfynpueovuG4Tg/zh-cn_image_0000002561833341.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=E1CFC4634D3A6FBF94B004010B4127EC5182DA441785A3D211AE6B30D5A0083B)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/0gtSVfeGTN6u2cOhFC-2Yg/zh-cn_image_0000002530913418.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=69C1F86728C469849842535F1A28CD05A9A3E5FBB9B54B8D00809425CE3AF6A1)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/S4ee5NdAQ-mTIu7CdQiJeg/zh-cn_image_0000002530913412.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=19166528DA9069CCCD6A883134DA9997ABE42EF533F74B2A00B88221039992A1)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

### 方式一：hdc shell snapshot\_display

```
1. hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
2. hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```

### 方式二：hdc shell wukong special -p

wukong是系统稳定性测试工具，通过指定参数-p可以实现截图功能。更多关于稳定性测试工具wukong的说明请参见[wukong工具使用指导](wukong-guidelines.md)。

```
1. hdc shell wukong special -p
```

命令执行效果如下图所示，其中Report currentTestDir为结果存储路径，包含截屏图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/vZggJUBWTbmSoQymaODWOg/zh-cn_image_0000002530753420.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=95AFCE6F8246EA141EC11FFFD5ACB265C458BA98F83BBC8E0167DA4247BCEC7F)

通过hdc命令可以将该路径文件发送到本地，例如发送到当前执行hdc命令的目录。

```
1. hdc file recv /data/local/tmp/wukong/report/20231010_141610/
```
