---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3c830901a3738834170b55aa48397831b511b4efc6c1cfcc819fdef7fbbee6e2
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备。
2. 点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/sACpzF6SQ5CKKH4aJJos5Q/zh-cn_image_0000002779608885.png "点击放大")图标打开日志面板，选择HiLog。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/yM2YV1X5T6qE0oB2IFThfA/zh-cn_image_0000002750009968.png "点击放大")，选择保存路径后即可截取屏幕截图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/CISydzgRRyKeR_PtiuuAUQ/zh-cn_image_0000002779729031.png)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
