---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-faq
title: 常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:751cebf2071f01917e61bfd3399c962dc50fb6585400b697d81d05181a85ca0b
---

## Native Leaks泳道录制捕获的泄露数据减少或丢失

**问题现象**

应用生命周期中，使用Allocation模板在当前会话录制ArkTS Snapshot泳道后，未重启应用在后续会话直接录制Native Leaks泳道，可能会导致捕获的泄露数据减少或丢失问题。

**解决措施**

录制ArkTS Snapshot泳道后，需重启应用，再录制Native Leaks泳道。

## Allocation模板录制时，仅能录制Memory泳道数据，重启应用后应用的进程号不变

**问题现象**

使用Allocation模板录制时，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/G6Hb5p21QL6rVNZbwGBiKg/zh-cn_image_0000002824684381.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB8A7A64A4639B52327EDF249040778D1606440FD88D988CAC2DACF7F023009D)开启启动模式后，单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/k9-geiZYRg6n77_I2iKv-g/zh-cn_image_0000002824564393.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAC9E9C92FDB993775F2EC733F21C2E1C1A36677E7E5A3BD006D5E1D8817AF99)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/YkJamvcUQuyYe0lImREoPA/zh-cn_image_0000002796204354.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=080AEFAA904BE4F5EC49ED9050FADD124D2C1F34D3578E5AFD93DF0E4D6D1756)，启动录制。当前仅能录制Memory泳道数据，不录制其它泳道数据；以及重启应用后，应用的进程号不变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/GdMFtsBDQXyGSq9ZxA67Nw/zh-cn_image_0000002796044410.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0F1E08988D1FE90452D6D98CC5DD75A25E8CC7522AB919D02169584B23911C4 "点击放大")

**可能原因**

启动录制时，应用会先退出[快启启动](../doccenter-references/api/js-apis-app-ability-hypersnapmanager.md)，再按常规方式启动，此时可正常抓取数据。当前启动录制时，应用未能退出快启模式，导致数据抓取失败。

**解决措施**

重启手机，或卸载并重新安装应用。

完成上述操作后，DevEco Profiler能够识别当前为录制数据场景，启动录制时，应用会退出快启启动（表现为每次启动应用后进程号发生改变），随后即可正常录制数据。
