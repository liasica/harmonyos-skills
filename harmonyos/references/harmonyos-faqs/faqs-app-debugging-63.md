---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63
title: 2in1设备attach调试失败和增量调试失败
breadcrumb: FAQ > DevEco Studio > 应用调试 > 2in1设备attach调试失败和增量调试失败
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:691c7eec5f29b0ca8e1645808aa54e39b1d27047cd1c1205bb2c464ba7f3803f
---

**问题现象**

1、2in1设备应用调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/5pNhxEOXSYeEyRCq_yFvhw/zh-cn_image_0000002654838125.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BE547BC3E8DC1FF20C29A7DD6600EC8B59821C6581C507C2B9940992C00699F)

2、2in1设备应用使用增量调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/20Njy9EHTcqqKe9uygo4Jg/zh-cn_image_0000002624478808.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=8730DAE6607288F7FA15746C6A632B551095BFAB878A33CF50AADF94F6F34EAB)

**解决措施**

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/50NYNpwiRoyy-C8ky7nHKg/zh-cn_image_0000002654798173.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE80D5A69BC2950BE54555258738A40D97E2FDF7CC86AD834C5D0579C8E04BA1)
