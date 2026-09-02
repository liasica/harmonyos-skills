---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24373f5de3db35544dfa341a117034836ac6ad2d51cb6919f3f77db22e88eb71
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/eQKYLPdwS_6b_1mXU_5c1w/zh-cn_image_0000002561833341.png)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/jneHmqj7Rn2RBmrbpvtGrQ/zh-cn_image_0000002530913418.png)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Ak9SNRNIQ1eOs47__C5Ozg/zh-cn_image_0000002530913412.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/yScHWXLhTqCzGOw8RAxeGA/zh-cn_image_0000002530753420.png)

通过hdc命令可以将该路径文件发送到本地，例如发送到当前执行hdc命令的目录。

```
1. hdc file recv /data/local/tmp/wukong/report/20231010_141610/
```
