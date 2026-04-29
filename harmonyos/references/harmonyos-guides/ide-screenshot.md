---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8bad14fd6f00559af3dda93b85a10b03cd167d95aa674717b003602cccfd68d3
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/eQKYLPdwS_6b_1mXU_5c1w/zh-cn_image_0000002561833341.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=EC6A110296002BEF5B40E92C1AFF76FF602C47A01D2FEEEF84CF8E8186F43290)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/jneHmqj7Rn2RBmrbpvtGrQ/zh-cn_image_0000002530913418.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=77F6FA1882EF3B1D7E96A12441B2B0E06397CEC3505CD7E2E9B7D46AA61DEAEF)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Ak9SNRNIQ1eOs47__C5Ozg/zh-cn_image_0000002530913412.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=B5E3EEE5D181AB51C1C08D4C546EEEE133638C8123935DD9B82DCDDBDB82D99A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/yScHWXLhTqCzGOw8RAxeGA/zh-cn_image_0000002530753420.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=EB4A6F3973C89FB0E81D2D8A12C8587AEFEEE8675ADED33F1293BEE489DC4ED7)

通过hdc命令可以将该路径文件发送到本地，例如发送到当前执行hdc命令的目录。

```
1. hdc file recv /data/local/tmp/wukong/report/20231010_141610/
```
