---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data
title: 数据区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6494f6923b0a9fc2c3fc39434c728679cbd0319b99a01435c7da18899e4e468
---

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/X6yOKfXUQrSSYdlqBhDjlg/zh-cn_image_0000002530753252.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=F8F9B04CF345CCAD3689A4789DD4FDF1D70C608AE8277CF5E0E0ED0197118BCF "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供标记、收藏、离线符号导入、泳道过滤、泳道启动配置项等辅助功能的管理以及会话状态和时间轴的控制能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/6cQUK--jQMm5ikqP6Li17g/zh-cn_image_0000002530753242.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=43FAB6AFAD65D7440C274F11A8163B51C94B0A04DFDC2F419177F9D9E85255B0)：标记列表按钮，点击后可以看到当前已放置的所有标记。可以查看/跳转到标记描述、时刻，支持修改标记的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ycf56-smSqKm4500xiimuA/zh-cn_image_0000002530753266.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=4972579FBAE8CBCD1764D0629A2742E7DCF77112E4392478DFD319B7B9D448A8)：收藏泳道隐藏/折叠按钮，激活后隐藏/折叠收藏的泳道，置灰时为展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/hh8m8FBsTuOiAUznfsa8ew/zh-cn_image_0000002561753171.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=54193AAFBCCAB1DE8A06B99D00B48759F937E29948E75974CCE2E8A355E1A9FE)：离线符号导入按钮，点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原，仅在Callstack和Native Allocation泳道中支持使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/uhAGTlpNT0e_rMPSSd-_cQ/zh-cn_image_0000002561753165.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=655B7E2271624FBDEB665A7CB3C2D32361BB19AEAD8C6C2D72EAA2886A64A002)：泳道筛选按钮，点击可选择泳道进行过滤。筛选无需录制的泳道，可以降低数据采集本身的开销，但同时会造成数据分析维度的减少。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/_jS_yBtmQuCquO2I7HoAYg/zh-cn_image_0000002530753256.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=7D542EF4383179AC6719AF5F62F3FBA37B2860D09CBBE322535001BD66758243)：泳道启动配置项，点击后展示不同泳道对应的插件启动配置信息。支持将配置信息保存到配置文件，后续使用该类型模板默认生效当前配置。

② 时间轴：提供横向时间轴，用于显示数据时间戳。

③ 标记栏：用于放置标记，能够帮助开发者标记时间点或时间段。

④ 泳道区：泳道图区域。每个场景化模板都会预置一系列泳道单元（例如上图的“Frame”便是一个泳道单元）。泳道单元是整个DevEco Profiler工具内，数据组织的最小独立单元，用于剖析应用某一特定维度的运行数据，每个场景化模板均是由一系列泳道单元组成，每个泳道单元都会呈现某一维度的性能数据。开发者可以查看数据随时间变化的特征，发现数据异常的时间段，支持框选时间段后在详情面板查看对应的细节。

说明

* 每个场景化模板的泳道单元，遵循Top-Down分析原则，越底部的泳道单元观测的性能越接近于系统底层，建议按照自顶而下的顺序分析。
* 同一个泳道单元中，泳道区中主要展示时间维度的性能变化，帮助开发者首先定位出有问题的时间段；进而通过详情区查看该时段各维度的详细数据，分析具体影响性能的参数或属性。

⑤ 详情区：展示详细的数据细节。开发者在泳道区域选择数据之后，以各类表格的形式呈现该时间段内各项详细数据。**More**面板将对左侧详情区中选中数据进行补充描述。

## 基本操作

### 开启/关闭会话控制

在数据区，首先可以开启和结束会话的录制，点击工具栏的首个按钮即可，如下图所示分别对应开启录制、结束录制功能，第三个状态则代表录制完成。与在会话区域录制的功能效果一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/4t9eRt_XQY6o_NdMxc08xg/zh-cn_image_0000002561753177.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=FC8289378E7D323CA738FFFB3E59781AD62593331C1365F53040AF94AB70F662)

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/5LRJYLa9SrC_CI3MhsJjoA/zh-cn_image_0000002530913256.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=2EAC4A6670A38D333A0E784C14699B097D5D760B43B7E902EF24C833DB79E1CE "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/8ZuZ1svLRMm-2m8KyqfWLQ/zh-cn_image_0000002530913248.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=8B025FB19E5D3F2AFE7C2986FC25DDAD18D4540D58E6F4744546CBCF9DF15325)：数据全量展示按钮，点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/NcZICVR4RMmCdezKFHIAMw/zh-cn_image_0000002561753189.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=3C81BE29EEC617AD889A415BB007B309695A04373D181B944117CB15562FF750)：时间轴调整按钮（快捷键为W或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变小，更多数据细节会呈现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KNqv6am4TzG-XkBzJOExuA/zh-cn_image_0000002530913270.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=538301B77BCE9B0B93F93CAC976CF03A7A6776F28FB30A0E958B76D8645E0E3C)：时间轴调整按钮（快捷键为S或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变大，更易于观测整体数据趋势。

拖动泳道区域下方的滑条(快捷键为A/D或使用Shift+鼠标滚轮)，开发者可以调整时间轴所示的时间范围；拖动泳道右侧滑条（或者滑动鼠标滚轮），可以调整泳道单元上下滚动。具体快捷键使用方式请参见[快捷键](ide-shortcut-key.md)。

说明

仅在已激活的泳道区域可以使用快捷键操作（泳道区域中存在亮蓝色的选中边框即为激活状态）。

### 查看详情面板

当开发者在泳道区域观察到可疑数据后，便可以通过框选或者点选的方式，将相关详细数据展示到详情面板中。泳道中条块状的数据支持点选查看，在泳道区域鼠标点击拖动再释放完成框选。可以在框选的同时按住Alt键，完成框选后时间轴尺度将会自动适应，整个框选时段会充满整个泳道区域，方便聚焦观察被选择的时段。

由于不同的泳道单元会展示不同维度的数据，因此详情面板展示的数据是来自于泳道区域中被选择的泳道单元。被选中的泳道单元会呈现蓝色，与其他泳道单元有明显差异。此外，当开发者直接选中泳道单元，而未进行框选或点选时，详情面板中会展示整个泳道单元的完整详细数据（效果等同于完整框选该泳道单元）。

### 添加/编辑标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了标记功能供开发者使用。

DevEco Profiler支持两种时间标记：

* 单点时间标记：单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/WbWlZJgWTDe1fNbcw6oIlA/zh-cn_image_0000002561753175.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=3B504014F31825AE575C7D96754CA90F64F919E39CD221B54F620F55BA570203)（快捷键为M，颜色可自定义）。
* 时间段时间标记：鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/x9J3IqSOTieMD-cWHpJzyQ/zh-cn_image_0000002530753262.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=0BFB169FD63AF5B0EAA150955118B553E8D836B4FEA0D9BD9713DD19771772C2)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/tdxNooCtSi6Y-E3Ss3_0vg/zh-cn_image_0000002530913266.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=F90278C34471FEA5C3EDB99C460CE83B25D6531CFEE5328E7F7F287DD79BF28A)

开发者可以在时间轴下方的标记区域点击放置单个标记，也可以在框选时间段后，点击旗子按钮放置该时间段的标记，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/fSKBMwyeSs6BvFAiZRa8rA/zh-cn_image_0000002530913268.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=899C422DF7B47F415FAE471137E1CD2FDCA4BDF6B97DFEAE54DCC10CDFFDB53E "点击放大")

支持使用“Ctrl+, ”向前选中单个标记，“Ctrl+. ”向后选中单个标记；“Ctrl+[ ”向前选中时间段的标记，“Ctrl+]”向后选中时间段时间标记。

标记放置完成后，可以通过双击标记按钮，在弹出的标记属性框中修改标记的描述和颜色信息，或者删除标记。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/28iXwgLNSOKvqJVD-aO-ZA/zh-cn_image_0000002561833177.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=DD3991FE7AB54D9F91183A76C8E985DAFC93010BED195B02C3250587C0F2D437)

此外，工具还提供了查看不同标记之间时间差的能力，只需要先选中一个标记，再鼠标悬浮在其他标记点上，便可在面板右下角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/p-Kx6ME5ROqXmCf98qo2fg/zh-cn_image_0000002561753179.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=01C76A46786B074DEED7D7E6C70F540395C7FBD1A3B5C151CDD3124BED4D6BBB)后看到被悬浮的标记点和被选择的标记点的时间差。借助这个能力，开发者能够快速获知一些特定时刻的时间差，这对于分析时间敏感的性能问题尤其有用。

### 收藏泳道单元

在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/xRi2JkqjS6CB4A29ad_bzg/zh-cn_image_0000002561753205.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=BAC4239107EE6B04805967A7341C12F16E5365C8C2F0E2CA3F779C21F0B36899)，点击该按钮即可完成收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/kLC4iX4yRra6YRcNvo4wFQ/zh-cn_image_0000002530753282.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=21A08125B1C2710F2FD8F5FB6443B9BE31562ACBC2BD45D64DB9042A63EDA01D)

再次点击该按钮则取消收藏。此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/60TwDcxWT4WGRaG8Q75zKg/zh-cn_image_0000002530913238.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=93476C447BCB45F662814B429782E7022934F7509600B54F6DBC3EC72EFAB74A)图标，可以将收藏的泳道单元进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/QZsB-SOISvKSEtR88Fqiug/zh-cn_image_0000002561753207.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=E6C7D237011FD0AF5D08FA55EE17BF8167F95E18E476033F9035A730BA7582E2 "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/haz4RJioSP6lhqzzPYI-hQ/zh-cn_image_0000002561753221.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=6FE58DA099340EEF1CAEFCADF63686546646181F9CB4720BD35F9B8A79CF2469 "点击放大")

### 展开/折叠子泳道

工具提供了两种方式展开/折叠子泳道：

1、点击父泳道左边小三角符号![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/s0kH08QvTGmHc6xzhIPXAg/zh-cn_image_0000002530913274.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=D11BA8B1D48C4E11350B84F0BB22DF9DDA61F97B4E33AED185926A5942E3CB68)。

2、双击父泳道表头区展开泳道。

### 全局搜索

为了帮助开发者迅速查找关心的性能数据，DevEco Profiler工具提供了全局搜索功能。

1. 在搜索框选项区可选择搜索类型，支持搜索泳道和搜索泳道数据，默认搜索泳道数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UjQuxQrXQuu7mTbKN7kx8Q/zh-cn_image_0000002561753199.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=C47D6D3158633CB2AEB6C210C112D16B8FB33F8DB935AFC888C627C8A6144562 "点击放大")
2. 搜索泳道数据，在输入内容前或搜索到结果后希望进一步确认搜索范围，可以选择在全时段内搜索或者在框选的时间范围内搜索；也可以选择在所有泳道内搜索或者在选择的泳道范围内搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Qvi6bVXeQP6bVFK1HEIKag/zh-cn_image_0000002561753169.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=8FA94674C1BD90004BEF464C1EE8715025424D74EF1C94B47283C6EEE690F18D "点击放大")
3. 可以点击Cc按钮，设置输入的关键字是否忽略大小写，默认为忽略大小写，点击时可自动重新触发搜索，搜索结果数量会显示在搜索栏右侧。有搜索结果的关键字会自动被记录到历史记录中，开发者可以通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/gsUcGBFvSeifAailiLiIkA/zh-cn_image_0000002561753167.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=99CE2B5D7379383A220EC5CDB0C82611BDB0EC40AB70263227AFA64AF5EBAEAF)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/GEsSY_sRQEeDAFOLvx4Dsg/zh-cn_image_0000002561833171.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=EC7ED9068445708089FAAF35F06A93856B30D96759865645346288166B92142D)按钮，向前向后查看搜索结果，泳道区域会自动跳转到对应的结果位置并为开发者选中该结果，详情面板中会自动刷新出相应详细数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/T8coKu6JQm-0bsSlFCk3Mg/zh-cn_image_0000002561833167.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=5B61F34DB9AAF561CA5444B54919B0CE36CF9CE18333673F8A9BCE053D0B4BF6 "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/EAXutRCmTQelnhaaE40zgw/zh-cn_image_0000002530753268.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=94E430BB30B2B13F2B8259F019AF0025F3F6D161E420FF8CB391AE9BE0AA8B57)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库，用户自编译的so库，三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/6oC0zdxSS6CS4BexPWBBOQ/zh-cn_image_0000002561753225.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=DB3A51E1B3797AEA73A7A4015941929743917ADE61E11E1CCAC46A5806A30CA0 "点击放大")

说明

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等）。可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

### 源码跳转

找到问题源码是调优过程中最为关键的一环。针对详情面板中所展示的函数栈帧信息（如下图所示），双击栈帧节点，工具便会在编辑器中打开相关源码文件，并定位到对应行号。此功能正常使用的前提是用于抓取性能数据的应用，是在DevEco Studio的当前工程开发编译，且相关源文件位置并未改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/x4AGnYMZTE-nsOnpBgprBw/zh-cn_image_0000002561833205.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=81AD5A46120E9196670762C219F79103DF6F8194D2E6A16E0D05F84B3C698362)
