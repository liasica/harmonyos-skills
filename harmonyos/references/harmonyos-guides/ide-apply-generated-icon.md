---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-apply-generated-icon
title: 生成单层图标
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 生成单层图标
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20e22ad19757be1b8fb3c0d7b46a13f40c74cfda2c5938e760d7b860e5fd33c8
---

DevEco Studio支持Image Asset功能，帮助开发者生成适应不同设备、不同屏幕密度的图标，并展示图标在目录中的具体位置。

说明

当前Image Asset功能支持为Phone、Tablet、2in1应用生成单层、圆角图标。

Image Asset支持生成以下两种类型图标：

* icon：应用图标（设备桌面及设置>应用中出现的应用图标）。
* start window icon：启动页图标。

1. 在工程中选中模块或文件，右键单击**New > Image Asset**，进入图标配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/YTFbdp0GTpCf3if0TYEgYQ/zh-cn_image_0000002530752764.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=5366DFBA15E49778ECE3393A15AD590324B3174A16B0C7157FA5CFB8584F5B78 "点击放大")

   说明

   若在模块级目录（Entry或其他模块）下新建Image Asset，将创建Icon and start window icon类型图标，用于在module.json5文件中配置icon及startWindowIcon字段；在工程级目录（AppScope或其他目录）下新建Image Asset，将创建Icon类型图标，用于在app.json5文件中配置icon字段。
2. 需要根据向导配置图标样式、大小等基本信息。
   * **Device**：选择当前配置的图标生效的设备类型。
   * **Icon Type**：展示当前图标的类型。
   * **Name**：配置图标名称。命名支持使用字母、数字、下划线，长度最多128个字符，不支持中文命名。
   * **Foreground Layer**：分层图标资源前景层。可配置下列字段信息：
     + **Path**：选择前景Image存放路径。推荐使用的图标尺寸为1024px\*1024px，保证图标整体的清晰性。
     + **Trim**：选择Yes，将调整图标图形与边框之间的距离，同时会去除图片周围多余的透明空间。
     + **Resize**：拖动滑块，设置图形的缩放比例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/PRIygb14TrO6pO-gzCDBNg/zh-cn_image_0000002561832681.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=9778FDBED41846DA5E40EFE1C10B1FD0BF2EE1AD16B8570E21F8299E8B2F0937)

   * **Background Layer**：分层图标资源背景层。请配置下列字段信息：
     + **Asset Type**：设置图标背景类型。可以选择颜色（**Color**）或图像（**Image**）。
     + **Color**：点击色块区域，选择适当的背景色。
     + **Path**：选择背景Image路径。推荐使用的图标尺寸为1024px\*1024px，保证图标整体的清晰性。
     + **Trim**：选择Yes，将调整图标图形与边框之间的距离，同时会去除图片周围多余的透明空间。
     + **Resize**：拖动滑块，设置图形的缩放比例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/KjJcYozWT2G9hF1t5c9J6Q/zh-cn_image_0000002561752703.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=E27C492A12F9DBE7764DA341764A595D6CCACCE73506E393BE11B4D40E6F9EB7)
3. 点击**Next**，确认图标的存储路径和相应的尺寸信息，图标将默认存放在**resources** 目录下。点击**Finish**完成图标生成。

   icon.png为桌面图标，icon\_start window.png为启动页图标，Size为图标的尺寸信息，不同尺寸对照关系如下：
   * sdpi：表示小规模的屏幕密度（Small-scale Dots Per Inch），适用于dpi取值为(0, 120]的设备。
   * mdpi：表示中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120, 160]的设备。
   * ldpi：表示大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160, 240]的设备。
   * xldpi：表示特大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240, 320]的设备。
   * xxldpi：表示超大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320, 480]的设备。
   * xxxldpi：表示超特大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/WAQHhLVyQaWShO40y3pWCA/zh-cn_image_0000002561752701.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=FF9CF870D3170B012D949813FB19514C5E99578EF6404EB7ACADA5C2AE9643EF)
4. 如需配置桌面或设置页面出现的应用图标，可将module.json5文件中icon字段修改为新生成的图标名称；如需修改启动页的icon图标，可将module.json5文件中startWindowIcon字段修改为新生成的图标名称。

   说明

   * 当上述字段配置了新生成的图标名称后，系统会根据当前设备状态优先从相匹配的限定词目录，即步骤3生成的不同尺寸的图标文件中寻找资源。具体请参考[资源匹配](resource-categories-and-access.md)。
   * 若module.json5文件中未配置icon字段，系统将使用app.json5中icon字段配置的图标。
