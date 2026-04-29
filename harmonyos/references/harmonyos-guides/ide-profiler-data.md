---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data
title: 数据区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d33f9e1f2aebddfff56613e6f4fdc8b10b216f2808d28874d9a281f67f8cf05
---

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/YO4mHt1VShuLwO78M72dVw/zh-cn_image_0000002530753252.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=9DC16CF54B50E0822CEC37605280B5F6FF7EBA8AE25CA5C36F3B50EEA77D8F84 "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供标记、收藏、离线符号导入、泳道过滤、泳道启动配置项等辅助功能的管理以及会话状态和时间轴的控制能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/2LNI_eB4SnqMNbr1hi2-9w/zh-cn_image_0000002530753242.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=8E95A1F160741A8ABDCE8974C9DEF651F36EA399A103F9CCB084F7EBDABB1A84)：标记列表按钮，点击后可以看到当前已放置的所有标记。可以查看/跳转到标记描述、时刻，支持修改标记的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4FczzgjMRWmV8QMxlYgPeg/zh-cn_image_0000002530753266.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=FE35CB6C9B0B99AC98DD27DABB3F5ED59C51DDAE08850BFAA694E10AFE6B185B)：收藏泳道隐藏/折叠按钮，激活后隐藏/折叠收藏的泳道，置灰时为展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/g0gLjAzaRVCY1_sQU4KEkw/zh-cn_image_0000002561753171.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=D89C2918BB2305ECAE0E38EA158678BF1C3D7E25FD52A15FB9BD29FDBD376E84)：离线符号导入按钮，点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原，仅在Callstack和Native Allocation泳道中支持使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/g8Glc8X5S3m06KJUdT_Z-w/zh-cn_image_0000002561753165.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=FBD571DD2AB6739291942B1E65FF9775E3157FCFDA46424213AEF22A9EC6A299)：泳道筛选按钮，点击可选择泳道进行过滤。筛选无需录制的泳道，可以降低数据采集本身的开销，但同时会造成数据分析维度的减少。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ckqNWPT-TWOJMfRFrn6N-g/zh-cn_image_0000002530753256.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=C99EA965C51239CBEC6A113594D391120B59B406C47CA30EAA6D937A41C70098)：泳道启动配置项，点击后展示不同泳道对应的插件启动配置信息。支持将配置信息保存到配置文件，后续使用该类型模板默认生效当前配置。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/6BaH2v3SQRK-BIbpWOrcLQ/zh-cn_image_0000002561753177.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=780B01C4B8FFCAB1A72B675AAB71605F897E9BEB5C0F828CCBC6F7A790B53710)

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/fNI1zEGHTMCPpMm3pNa2yQ/zh-cn_image_0000002530913256.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=2CB5E1A914758728ABB64ED7B795C97428A535BFA5006C6465BDBA5C7E11BB53 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/pdhpxsXWTdiS9wzHiIXrkA/zh-cn_image_0000002530913248.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=0A7AF31C210B04E8B37BA0CF73424BAC8D67A1A839BC613F45527A396387A4AB)：数据全量展示按钮，点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/w7I_FljQSxSH-LmQxUhUAA/zh-cn_image_0000002561753189.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=B5C10B9C8E801EC861F8D666AAFA1966050184D3F794C14B6039511F7E77BB74)：时间轴调整按钮（快捷键为W或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变小，更多数据细节会呈现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/dRCvSVlFQ2aLLUYnEQmGIg/zh-cn_image_0000002530913270.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=08DF28F111A60DE11E670081408048345D43D65B2A4C15A1AD3EE10724C1B265)：时间轴调整按钮（快捷键为S或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变大，更易于观测整体数据趋势。

拖动泳道区域下方的滑条(快捷键为A/D或使用Shift+鼠标滚轮)，开发者可以调整时间轴所示的时间范围；拖动泳道右侧滑条（或者滑动鼠标滚轮），可以调整泳道单元上下滚动。具体快捷键使用方式请参见[快捷键](ide-shortcut-key.md)。

说明

仅在已激活的泳道区域可以使用快捷键操作（泳道区域中存在亮蓝色的选中边框即为激活状态）。

### 查看详情面板

当开发者在泳道区域观察到可疑数据后，便可以通过框选或者点选的方式，将相关详细数据展示到详情面板中。泳道中条块状的数据支持点选查看，在泳道区域鼠标点击拖动再释放完成框选。可以在框选的同时按住Alt键，完成框选后时间轴尺度将会自动适应，整个框选时段会充满整个泳道区域，方便聚焦观察被选择的时段。

由于不同的泳道单元会展示不同维度的数据，因此详情面板展示的数据是来自于泳道区域中被选择的泳道单元。被选中的泳道单元会呈现蓝色，与其他泳道单元有明显差异。此外，当开发者直接选中泳道单元，而未进行框选或点选时，详情面板中会展示整个泳道单元的完整详细数据（效果等同于完整框选该泳道单元）。

### 添加/编辑标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了标记功能供开发者使用。

DevEco Profiler支持两种时间标记：

* 单点时间标记：单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/8WXwq74mT_uWvM6V6quxfQ/zh-cn_image_0000002561753175.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=3D72316185886C34896E8B85F2A09136F4F972CC95517E88893F7B30C498D671)（快捷键为M，颜色可自定义）。
* 时间段时间标记：鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Ikg05viLT2Oi2X25SiLTJg/zh-cn_image_0000002530753262.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=D7DD6670AB23D472190962B9263760DB287FA12FE29C6D6352C64806AA6DECCE)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/FwzDUoy_R3G6KNnE2LMd7Q/zh-cn_image_0000002530913266.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=10449050A9A0B60E72026A780CF5EE57C5A23AE3340FEE41C4F8A803B8F481D3)

开发者可以在时间轴下方的标记区域点击放置单个标记，也可以在框选时间段后，点击旗子按钮放置该时间段的标记，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/UGl_I0PmS3WMJyqgVAhM9w/zh-cn_image_0000002530913268.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=11280C3D93F4414F61DAA621804A7DB483DB78C861FE7C26400578062BBEF3C5 "点击放大")

支持使用“Ctrl+, ”向前选中单个标记，“Ctrl+. ”向后选中单个标记；“Ctrl+[ ”向前选中时间段的标记，“Ctrl+]”向后选中时间段时间标记。

标记放置完成后，可以通过双击标记按钮，在弹出的标记属性框中修改标记的描述和颜色信息，或者删除标记。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Q_LB0tS4T-SsyiiLQC9auA/zh-cn_image_0000002561833177.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=2BE9428B6D00132EC15E0AD854997C785E8A49FDB46E2E0394A9E3CCF2808CD0)

此外，工具还提供了查看不同标记之间时间差的能力，只需要先选中一个标记，再鼠标悬浮在其他标记点上，便可在面板右下角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/QOHzR4w4QYKPT2V8iVbvPA/zh-cn_image_0000002561753179.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=51D9D47DD2E350F97FEB2F1F28A90D6EC1E1E623BBFB0499CDBB946360E671EA)后看到被悬浮的标记点和被选择的标记点的时间差。借助这个能力，开发者能够快速获知一些特定时刻的时间差，这对于分析时间敏感的性能问题尤其有用。

### 收藏泳道单元

在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Se935X1bRmmHmPhSxLbDsQ/zh-cn_image_0000002561753205.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=C514368AF91AF8AA254F68B41192D956196D75D8ABB29F390CCC8AF23CA31ED1)，点击该按钮即可完成收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/DpDRNBhORDeAeXWkC-1u6A/zh-cn_image_0000002530753282.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=ADA63C7756D74874641A9A81686F7AFFDC6355ACC45B3EBD20240C03CD7364BC)

再次点击该按钮则取消收藏。此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/3dzOHos5R0qgloQkZa7sDw/zh-cn_image_0000002530913238.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=CD0FB90E644BF72A57C61396870D795BE29A6E8E8144196BE77D18138C96F903)图标，可以将收藏的泳道单元进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/fppKcwQyRQGDIQzNGukHqw/zh-cn_image_0000002561753207.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=71C5679EA183D20573CFB661E1B431EACE01C90E055B370CD0A453077AE3DF77 "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/dK-ZRQDVTr-weCwB_K94Kw/zh-cn_image_0000002561753221.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=D4E83DC39FABB01822F461FCE4F2A0651D0013AE2DB016B0C26EBAD561396A63 "点击放大")

### 展开/折叠子泳道

工具提供了两种方式展开/折叠子泳道：

1、点击父泳道左边小三角符号![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/IIkRNwvtS8e8hhgiCUFLeA/zh-cn_image_0000002530913274.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=3D0A94C466FE8D47B23640F6BA8C0625887DA97D8DBBF3DAB60C06C95D24740A)。

2、双击父泳道表头区展开泳道。

### 全局搜索

为了帮助开发者迅速查找关心的性能数据，DevEco Profiler工具提供了全局搜索功能。

1. 在搜索框选项区可选择搜索类型，支持搜索泳道和搜索泳道数据，默认搜索泳道数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/dqU5IMYrSDisvZyoOLdEeg/zh-cn_image_0000002561753199.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=6C70986F769B862AB754CEDF6EEAE1248155DCB5A972938F8D30ECFFF0588C3C "点击放大")
2. 搜索泳道数据，在输入内容前或搜索到结果后希望进一步确认搜索范围，可以选择在全时段内搜索或者在框选的时间范围内搜索；也可以选择在所有泳道内搜索或者在选择的泳道范围内搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/9qdY1nIiTfKfPo1EZqffEg/zh-cn_image_0000002561753169.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=0BA10A9C5DF9209FDC5083787502D23B0D224A42B4637D2DAB2ADFF6E3770993 "点击放大")
3. 可以点击Cc按钮，设置输入的关键字是否忽略大小写，默认为忽略大小写，点击时可自动重新触发搜索，搜索结果数量会显示在搜索栏右侧。有搜索结果的关键字会自动被记录到历史记录中，开发者可以通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Lnn4vjLLTPuPnxuSZVQE4Q/zh-cn_image_0000002561753167.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=AA71FC29C1A2AC4C895283B514E48F3835F7A4CCE5D9E1524B59597C43AE1A3C)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/EM8C75nVQKuKFbf5qn0S8Q/zh-cn_image_0000002561833171.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=9720000A5BA09BD69F6D3E1221F29963D79ABFEC1F38EF300B8868AD0A8E3213)按钮，向前向后查看搜索结果，泳道区域会自动跳转到对应的结果位置并为开发者选中该结果，详情面板中会自动刷新出相应详细数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/N-zGQf5PS-uEC3F5LewnCA/zh-cn_image_0000002561833167.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=A2A6451FD71DD50EBC5BC128548F264288E61776A0710F4E01E5631A10FE223C "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/j5FafM7VS7SYviWHQ-AP0A/zh-cn_image_0000002530753268.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=19AB95379F5BAA8502C1B17D6F30FB2A14F60156CBA6DC30E1F38EA22D257805)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库，用户自编译的so库，三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/fcUl8wCnQbaIN6R-cFIxcw/zh-cn_image_0000002561753225.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=473C81864617AC803F9B9DE8004338F148B79AA127967437B58FB9A0EB964983 "点击放大")

说明

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等）。可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

### 源码跳转

找到问题源码是调优过程中最为关键的一环。针对详情面板中所展示的函数栈帧信息（如下图所示），双击栈帧节点，工具便会在编辑器中打开相关源码文件，并定位到对应行号。此功能正常使用的前提是用于抓取性能数据的应用，是在DevEco Studio的当前工程开发编译，且相关源文件位置并未改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MWB5fK5uT0CZb8xP73CvAQ/zh-cn_image_0000002561833205.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=DD4376CF589A48C3DC951D7313885EE2CBCA15801ABBC40C29F2242A25252007)
