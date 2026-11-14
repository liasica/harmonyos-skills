---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ba5f3a189a0d28b0e1b2c738379715d425da097c8b3ec61162e34ce48562eeba
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备。
2. 点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Rvg7yXMQQTGoITBH6EiHrQ/zh-cn_image_0000002781311424.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C5EC82F1F303BFD367E3C9BBC29303750095A9E6FCAAFE54A854CEFADAC174C "点击放大")图标打开日志面板，选择HiLog。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/I-xW8EwWR3Kf_nRtNA4Nxw/zh-cn_image_0000002781471360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF9FD3BF91F67B63B6A750B9D0512D47AB5A486010346364AC5797E79CC7A4E1 "点击放大")，选择保存路径后即可截取屏幕截图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/phWrTII8SJGLwBUoLj_bwA/zh-cn_image_0000002810630911.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1001E4C09FB36C39E5B6B1C63C85BB6082EF050A05072212C7B597B8330BD6A3)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
