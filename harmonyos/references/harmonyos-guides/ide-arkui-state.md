---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state
title: 查看ArkUI状态变量
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 查看ArkUI状态变量
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e5d800725877756240d61cf5f90a205f7b13fa44492e16dd4c1bcf666a583f93
---

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lLMHh2wHR724_qGWYfQy7A/zh-cn_image_0000002808766215.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=F95F2EF01A5E6BC924503DCC70D0B95D5F4B9CD04741E477BF203E7C64645DCA)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/okkZlwphRFaGp4nDxoVsVw/zh-cn_image_0000002808886299.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=07202FC704D1C2E33CBDF8F1BB00632EEAFD89F314FA0A1553CBF13E9DC6B4E5)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

* 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/o_nqd-mAT-iIWuwK78b5xQ/zh-cn_image_0000002808766221.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3D0E23747E7872B01EA43DCFE770505DC13B1E1755BAC102C57571B74B1BBB6)
* 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/D_Zy9kv6SQanHPwEUvWS9A/zh-cn_image_0000002808886295.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EBAF001738C36CAD9912E25D9BB3B9721ADC4FB6BC79A5D88AD0D41043026DC)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/zySp-W37QP6z6o_bpJDvfQ/zh-cn_image_0000002808886297.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=B97C4BB5A3F4CA3AD92A82BAD7BF30D444050271758A6FF29F6B54D292E5954E)

**说明** 

* 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
* 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
