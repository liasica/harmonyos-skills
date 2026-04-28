---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63
title: 2in1设备attach调试失败和增量调试失败
breadcrumb: FAQ > DevEco Studio > 应用调试 > 2in1设备attach调试失败和增量调试失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b673fd8e0befe7e2ea08d72127e16904843547be85ca3a627117f79dfde1619f
---

**问题现象**

1、2in1设备应用调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/ashxlMVIQYGyRC4dw3yL2w/zh-cn_image_0000002557414329.png?HW-CC-KV=V1&HW-CC-Date=20260428T003011Z&HW-CC-Expire=86400&HW-CC-Sign=4087AC71B7A9608DE780FE8608981B8CE4EB1F03CA93163397293C86761CDE8F)

2、2in1设备应用使用增量调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Wh6hj1tfSKq7qsAOD6772A/zh-cn_image_0000002526214500.png?HW-CC-KV=V1&HW-CC-Date=20260428T003011Z&HW-CC-Expire=86400&HW-CC-Sign=637F4E4223E1CA5AFFC68A2B33A1AF36F8C019F300436716256D7A59E4FEFC44)

**解决措施**

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/RdopVVw0T1Krg-5NBP827A/zh-cn_image_0000002557334361.png?HW-CC-KV=V1&HW-CC-Date=20260428T003011Z&HW-CC-Expire=86400&HW-CC-Sign=A339FB2E573A0DE4138DDB291AFD0387A874563079DAB292CC259F2C1F36757B)
