---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63
title: 2in1设备attach调试失败和增量调试失败
breadcrumb: FAQ > DevEco Studio > 应用调试 > 2in1设备attach调试失败和增量调试失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a70c85945bf23fbc83e5b56d853d7ba04f6c5c63cad83004bc91472e425ad664
---

**问题现象**

1、2in1设备应用调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/ashxlMVIQYGyRC4dw3yL2w/zh-cn_image_0000002557414329.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=E94C37C88F91A312A400CA683CE497B1031F1BB664503B59EBD6D1CF79F69229)

2、2in1设备应用使用增量调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Wh6hj1tfSKq7qsAOD6772A/zh-cn_image_0000002526214500.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=D38B4C082CC3F4E5F4145C6CEFCDF5106934D65F2FAFE800DA94DAB3B8E8D137)

**解决措施**

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/RdopVVw0T1Krg-5NBP827A/zh-cn_image_0000002557334361.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=465FC5777A3FD0616325D9A3391F655C36BA1B0B607A2463F3620CAEF79745FF)
