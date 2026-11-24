---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data
title: 数据区
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:493074a9553416e749f634c4c586732a001854cf2d63c7a83beae8890e4f8782
---

## 简介

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ydWOTNQUSjeA_SQR8MWW5w/zh-cn_image_0000002779407178.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B845250026C5B0FAEC7EC1D78DC6CD8806286FDF9A92F5ABC6301E69C8FA6B3 "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供标记、收藏、离线符号导入、泳道过滤、泳道启动配置项等功能的管理以及会话状态和时间轴的控制能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/VEUZxtIxSD2F3_0nZLcy9w/zh-cn_image_0000002779407158.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=213A090B44E5EAE9E2DED76D9826478F1E6200E31190F62BFFA83523F7921A5F)：标记列表按钮，点击后可以看到当前已放置的所有标记。可以查看/跳转到标记描述、标记时间点，支持修改标记的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/dHWSCk5xTeOLt_DPgBMk8w/zh-cn_image_0000002779567156.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0407D66217CCC1FB113A14B56E4C7D3051707252E4AE40B39E441697BBE4F62F)：收藏泳道的隐藏/折叠按钮，激活后会隐藏/折叠收藏的泳道，置灰时展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/KVv6XH3TSySlYfCcByPTJA/zh-cn_image_0000002808886809.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BFF2C3FB198503676557446F024294F3D64CDB44D747B96EB2F9C31ACF08C3A)：离线符号导入按钮，点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/PWa-jHFmR0SZFjW7LCMbkQ/zh-cn_image_0000002808886797.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=37E7ACD13F4A262CD3AF7477BE2082E17978282AE2CF42175221918EA300FD8D)：泳道筛选按钮，点击可选择泳道进行过滤。筛选无需录制的泳道，可以降低数据采集本身的开销，但同时会造成数据分析维度的减少。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/csoiwcJoSaS7LfJla70W-w/zh-cn_image_0000002779567140.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=C99430FFA0EF95CE046D4E61AC31F24C08974CE3D53C85A057AFAAA2057A4DF4)：泳道启动配置项，点击后展示不同泳道对应的插件启动配置信息。支持将配置信息保存到配置文件，后续使用该类型模板默认生效当前配置。

② 时间轴：提供横向时间轴，用于显示数据时间戳。

③ 标记栏：用于放置标记，能够帮助开发者标记时间点或时间段。

④ 泳道区：泳道图区域。每个场景化模板都会预置一系列泳道（例如上图的“Frame”便是一个泳道）。泳道是整个DevEco Profiler工具内，数据组织的最小独立单元，用于剖析应用某一特定维度的运行数据，每个场景化模板均是由一系列泳道组成，每个泳道都会呈现某一维度的性能数据。开发者可以查看数据随时间变化的特征，发现数据异常的时间段，支持框选时间段后在详情面板查看对应的细节。

**说明** 

* 每个场景化模板的泳道，遵循Top-Down分析原则，越底部的泳道单元观测的性能越接近于系统底层，建议按照自顶而下的顺序分析。
* 同一个泳道中，泳道区中主要展示时间维度的性能变化，帮助开发者首先定位出有问题的时间段；进而通过详情区查看该时段各维度的详细数据，分析具体影响性能的参数或属性。

⑤ 详情区：展示详细的数据细节。开发者在泳道区域选择数据之后，以各类表格的形式呈现该时间段内各项详细数据。**More**面板将对左侧详情区中选中数据进行补充描述。

## 基本操作

### 开启/关闭会话控制

在数据区，首先可以开启和结束会话的录制，点击工具栏的首个按钮即可，如下图所示分别对应开启录制、结束录制功能，第三个状态则代表录制完成。与在会话区域录制的功能效果一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/GoFICaAxQGW3znfgVFrqqQ/zh-cn_image_0000002808886795.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=5795180CA0FE81ACF9603A7283B0DDB7F7251C5F3C9C83190FF52FB06C4C9075)

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/SwnC-YnlS4Cp_98grTjVBg/zh-cn_image_0000002808766723.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D80700D259CA7D5ECBB206E290EC35E7057850F2B6E60A384EAD1973A138F3E "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aWlZIdlqTviNcNwE1Z2anA/zh-cn_image_0000002779407160.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9BCED847F9671960D6D9321B03E60CF8C0C4B54458F63DC4D49556F1F0376BE)：数据全量展示按钮，点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/ZkaPwkRTT6-yOlQtjLvM_A/zh-cn_image_0000002808886799.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2DB7758C52E8FA327C509754502EA944A3E6044FC796953DC562F4C33498EE3)：时间轴调整按钮（快捷键为W或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变小，更多数据细节会呈现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/DprqMsAQQJqwcfUMMFSmmA/zh-cn_image_0000002808766729.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AC042270AA93D1DC412D311E1005AFBC1E42450E307EF6454FE1B59DFD71379)：时间轴调整按钮（快捷键为S或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变大，更易于观测整体数据趋势。

拖动泳道区域下方的滑条（快捷键为A/D或使用Shift+鼠标滚轮），开发者可以调整时间轴所示的时间范围；拖动泳道右侧滑条（或者滑动鼠标滚轮），可以调整泳道上下滚动。具体快捷键使用方式请参见[快捷键](ide-shortcut-key.md)。

**说明** 

仅在已激活的泳道区域可以使用快捷键操作（泳道区域中存在亮蓝色的选中边框即为激活状态）。

### 查看详情面板

当开发者在泳道区域观察到可疑数据后，便可以通过框选或者点选的方式，将相关详细数据展示到详情面板中。泳道中条块状的数据支持点选查看，在泳道区域鼠标点击拖动再释放完成框选。可以在框选的同时按住Alt键，完成框选后时间轴尺度将会自动适应，整个框选时段会充满整个泳道区域，方便聚焦观察被选择的时段。

由于不同的泳道会展示不同维度的数据，因此详情面板展示的数据是来自于泳道区域中被选择的泳道单元。被选中的泳道单元会呈现蓝色，与其他泳道单元有明显差异。此外，当开发者直接选中泳道单元，而未进行框选或点选时，详情面板中会展示整个泳道单元的完整详细数据（效果等同于完整框选该泳道单元）。

### 添加/编辑时间标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了两种时间标记功能供开发者使用。

* 方式一：单点时间标记。单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/xbZempQlT0mBt-q0qyR88Q/zh-cn_image_0000002779567132.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B9822B3A6C945682602BB8ADE49409D674595BAD74A002AE2F604FCC63F5B43)（快捷键为M，颜色可自定义）。
* 方式二：时间段时间标记。鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/eBkU57nHReW7F0s1nuyeKw/zh-cn_image_0000002808886803.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=94E910D079A53F927F027618B50F4E5F4FEFA32B9BB640CA1A0CAD1BFD82C210)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/gmAPz_T4SPuMkLBw7TpTTg/zh-cn_image_0000002779407168.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F41DA0DD8F55996A0B6E23F883B0F2E0E129484F7DE419668828219ABA5954C "点击放大")

标记放置完成后，支持通过快捷键“Ctrl+, ”向前选中单个标记，“Ctrl+. ”向后选中单个标记；“Ctrl+[ ”向前选中时间段的标记，“Ctrl+]”向后选中时间段时间标记。同时，支持通过单击鼠标右键标记按钮，在弹出的标记属性框中修改标记的描述和颜色信息，或者删除标记。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/75hTD22VS1CXtofI0xsG8A/zh-cn_image_0000002808766715.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=91AF662E6B80710467F1D56F4AEE373BEE4DFB67890BAC2A6D0A0E431F49DE0F "点击放大")

此外，工具还提供了查看不同标记之间时间差的能力，只需要先选中一个标记，再将鼠标悬浮在其他标记点上，便可在面板右下角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/endcch8xT0KEg1NtQmg9PA/zh-cn_image_0000002779567136.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=23FABF4AC12D6F42EF38527871A6C832C30F318EC7EA22D4E208CE7A6011E40F)后看到被悬浮的标记点和被选择的标记点的时间差。借助这个能力，开发者能够快速获知一些特定时刻的时间差，这对于分析时间敏感的性能问题尤其有用。

### 收藏泳道

在使用工具分析，可能会遇到泳道过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/SufIUeHMQ3m-qOI_XKOaSA/zh-cn_image_0000002808886805.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=B350B63D3FFD0930EA6944E593B72A379A71D3916C0C7A2709EED2FE91888AD7)，点击该按钮即可完成收藏，再次点击该按钮则取消收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/KmO6-THxSmiGrfk69MVnWg/zh-cn_image_0000002808886813.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=382B219FE46C433522F4F0EF16476E23050D6BD096678C327893C7175EE0359D)

此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Ls0QAl4nQzqqHq_wE3Y3ag/zh-cn_image_0000002808766717.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=247CF475C6A1F361C0DE9D03B35041F5697F5BB3251DA849359534922D72CAF2)图标，可以将收藏的泳道进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/6aSM6yB1SKKT2RXzF2Dozw/zh-cn_image_0000002779567146.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=18F268551CFE820DBFA110415C2CF3EEE20E020997A5E801101D3C329DE5886D "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/SJNrimWJQT-3OiSveXf1hw/zh-cn_image_0000002808766733.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D50D843EFBFB4C751C4F164FD2E442D8CC31AE147FD9F8F4E974423AB371132 "点击放大")

### 展开/折叠子泳道

工具提供了两种方式展开/折叠子泳道：

1、点击父泳道左边小三角符号![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/6hFx9Y1-QxuTLc0N7bm0SA/zh-cn_image_0000002779567150.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A97AF441942D06279B075A7BA3EA75D25DF30F50F4D686445E395C4D8162B8D)。

2、双击父泳道表头区展开泳道。

### 全局搜索

为了帮助开发者迅速查找关心的性能数据，DevEco Profiler工具提供了全局搜索功能。

1. 在搜索框选项区可选择搜索类型，支持搜索泳道和搜索泳道数据，默认搜索泳道数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/onjjh66TTwq6Z0SYdwni_A/zh-cn_image_0000002779407162.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=48A4A293538B87166290FCAB06C4288E6609162E746F004EF390CBA3289DBE55 "点击放大")
2. 搜索泳道数据，在输入内容前或搜索到结果后希望进一步确认搜索范围，可以选择在全时段内搜索或者在框选的时间范围内搜索；也可以选择在所有泳道内搜索或者在选择的泳道范围内搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/I6oCT28yS3qZkP0kXFBzSw/zh-cn_image_0000002808886793.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=41E7C4BFEF14468DA6728F437E7648E1693B33753E8ED66772BD67012F5B74D7 "点击放大")
3. 可以点击**Cc**按钮，设置输入的关键字是否忽略大小写，默认为忽略大小写，点击时可自动重新触发搜索，搜索结果数量会显示在搜索栏右侧。有搜索结果的关键字会自动被记录到历史记录中，开发者可以通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/SxEBE9AYSvqSz1EmLqJFQg/zh-cn_image_0000002808766711.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BCB1B740EB868DE0A0FBDEE11786B3A16BB4FC8483C14B2A9B58A1C5781F394)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/lIZTKgaMSS-HT6XjlHLZiw/zh-cn_image_0000002779567138.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=137A53ED87DD5F57389529637494C115AFA764172E0921B6EEC405E9C9DAEEB6)按钮，向前向后查看搜索结果，泳道区域会自动跳转到对应的结果位置并为开发者选中该结果，详情面板中会自动刷新出相应详细数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8WQhfjzdSECTIJ_pMlY17Q/zh-cn_image_0000002808766727.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=928FD5CFD6547F828649B7C39A3821DE8181E922ED6FBE867F04AE87C50E7404 "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Hm5dYRRxQlKAVUZQ2Fu_RQ/zh-cn_image_0000002808766725.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6B5F6490F93C7221216DDA7FA4F8B377BFCE93F4863CBA59C4B047DA9636E1B)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库、用户自编译的so库、三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/8LUPBX9pQQWLZTuu4rLpOw/zh-cn_image_0000002808886817.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=A942FD64B045D8BF016B2615DB68631056B1FDCCB0F589A47CE79D7043707ABE "点击放大")

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等），可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

### 源码跳转

找到问题源码是调优过程中最为关键的一环。针对详情面板中所展示的函数栈帧信息（如下图所示），双击栈帧节点，工具便会在编辑器中打开相关源码文件，并定位到对应行号。此功能正常使用的前提是用于抓取性能数据的应用，是在DevEco Studio的当前工程开发编译，且相关源文件位置并未改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/lWHWKgW-SQ2_q_wYlehsDg/zh-cn_image_0000002779567154.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=3560EAD44CBD235CB156E16535DA8232A7B5CE5D82FBD0BFF0986BD7F0A90F67)
