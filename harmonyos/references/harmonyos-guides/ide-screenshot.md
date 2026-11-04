---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7107532a82dc669fb1cbb038c377a4dc810ba16b442b7b7137f71a0d805458ca
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/WTWx_2RgQjC0vZG13UEopQ/zh-cn_image_0000002701663696.png)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/kPCCo2RrROipVsjkLOfteQ/zh-cn_image_0000002731382919.png)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Hv8E7Q_EQoK_RxeyzzzNrg/zh-cn_image_0000002731542891.png)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
