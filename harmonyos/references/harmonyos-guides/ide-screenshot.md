---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8a18fe2e06daf696ef90bd07ec942feed378d104680636cf4af1c91ff282cf55
---

在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/fA0l-xk1QrebYUVC0airGQ/zh-cn_image_0000002808886869.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=935DAF0C2AD0ED05E3E186ADC3BCE4FE7EC001614061AE24A329828E0BEBF1ED)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/FdjydSztTK2SrzMbCAjbjg/zh-cn_image_0000002808766789.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=184EA5D91DF639467AEF756E2022D9385D655338AA5BD9401189AE6655BCFE67)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/oUlzbak6QVGb7PPcWqCkaA/zh-cn_image_0000002779407228.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=83555054FCA1A5786A9EFCF017B5D988C25D8AB1E5728CD0CEB2C0E60081C6A6)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

```bash
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
