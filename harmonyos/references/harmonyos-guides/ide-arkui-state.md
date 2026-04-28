---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state
title: 查看ArkUI状态变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 查看ArkUI状态变量
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f9ad0a94517e96fcad46738befd7a3209b8fcb9b96641338dc12ef69377fc6b
---

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Bsn1pYtPSdew_2qFJncDBQ/zh-cn_image_0000002561832669.png?HW-CC-KV=V1&HW-CC-Date=20260427T235651Z&HW-CC-Expire=86400&HW-CC-Sign=41207D62F4742D842D2E1624D3DCE84AC0E3B341FF2A7302756E929A66377D6F)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/4ap9cfgRSP-R5haQNOIAKQ/zh-cn_image_0000002561752693.png?HW-CC-KV=V1&HW-CC-Date=20260427T235651Z&HW-CC-Expire=86400&HW-CC-Sign=47E3D7A2243BA4031A555E202A56463C0979ACF738733EF055C797E2AB13552D)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

* 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/T4nVjufxTRml1bezGR--oQ/zh-cn_image_0000002530912750.png?HW-CC-KV=V1&HW-CC-Date=20260427T235651Z&HW-CC-Expire=86400&HW-CC-Sign=F41CD73351489DE9C1DD8CB4AB1E0923589F066DD51EF4FBA16F7DFBFF91699F)
* 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/DktH43POTiuPVmm4YgPk7w/zh-cn_image_0000002530752746.png?HW-CC-KV=V1&HW-CC-Date=20260427T235651Z&HW-CC-Expire=86400&HW-CC-Sign=A6CC7D5CA82D5D68E00B9B9E9275AFB86BEB4982A26E8091AB804FD59E68DBBD)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/YcY5ZF3RTyeJ3bUqJLtX0g/zh-cn_image_0000002561752689.png?HW-CC-KV=V1&HW-CC-Date=20260427T235651Z&HW-CC-Expire=86400&HW-CC-Sign=D7735FA2D5CFD54AC4034330AED1AB23EBA408D32617C986F6B0052BB9319A0C)

说明

* 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
* 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
