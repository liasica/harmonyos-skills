---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data
title: 数据区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5cf9beae76367d6f824af0749abf9440fd2a1d747bde46e206029460a872f7df
---

## 简介

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/w8SWCxkxTSugj30KiFKGBg/zh-cn_image_0000002701823478.png "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供标记、收藏、离线符号导入、泳道过滤、泳道启动配置项等功能的管理以及会话状态和时间轴的控制能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/YdWnLGZoT2-4sqTEw_tSUA/zh-cn_image_0000002701663558.png)：标记列表按钮，点击后可以看到当前已放置的所有标记。可以查看/跳转到标记描述、标记时间点，支持修改标记的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/O_ISsoehTX-tfhAK8HMX5Q/zh-cn_image_0000002731382791.png)：收藏泳道的隐藏/折叠按钮，激活后会隐藏/折叠收藏的泳道，置灰时展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/fVK3JNhdSCadypOCVwoDCw/zh-cn_image_0000002701663556.png)：离线符号导入按钮，点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/UzBXx1W-RFWSTjeDkZIVKA/zh-cn_image_0000002701663568.png)：泳道筛选按钮，点击可选择泳道进行过滤。筛选无需录制的泳道，可以降低数据采集本身的开销，但同时会造成数据分析维度的减少。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/XZIpAKDvTrGid-UFshWgsQ/zh-cn_image_0000002731542755.png)：泳道启动配置项，点击后展示不同泳道对应的插件启动配置信息。支持将配置信息保存到配置文件，后续使用该类型模板默认生效当前配置。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ROBWptJFRhWUKFDTz4n7vQ/zh-cn_image_0000002701663540.png)

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/GkblNrTTRE25cXfpMVWayQ/zh-cn_image_0000002731542739.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/I-fTRzSCRb2sC5jedEdB9Q/zh-cn_image_0000002731542753.png)：数据全量展示按钮，点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/R2akAQskT-25kadoOVU2Aw/zh-cn_image_0000002731542747.png)：时间轴调整按钮（快捷键为W或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变小，更多数据细节会呈现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/54r1rJAHS0ue7Ej4OwgSiA/zh-cn_image_0000002701663534.png)：时间轴调整按钮（快捷键为S或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变大，更易于观测整体数据趋势。

拖动泳道区域下方的滑条（快捷键为A/D或使用Shift+鼠标滚轮），开发者可以调整时间轴所示的时间范围；拖动泳道右侧滑条（或者滑动鼠标滚轮），可以调整泳道上下滚动。具体快捷键使用方式请参见[快捷键](ide-shortcut-key.md)。

**说明** 

仅在已激活的泳道区域可以使用快捷键操作（泳道区域中存在亮蓝色的选中边框即为激活状态）。

### 查看详情面板

当开发者在泳道区域观察到可疑数据后，便可以通过框选或者点选的方式，将相关详细数据展示到详情面板中。泳道中条块状的数据支持点选查看，在泳道区域鼠标点击拖动再释放完成框选。可以在框选的同时按住Alt键，完成框选后时间轴尺度将会自动适应，整个框选时段会充满整个泳道区域，方便聚焦观察被选择的时段。

由于不同的泳道会展示不同维度的数据，因此详情面板展示的数据是来自于泳道区域中被选择的泳道单元。被选中的泳道单元会呈现蓝色，与其他泳道单元有明显差异。此外，当开发者直接选中泳道单元，而未进行框选或点选时，详情面板中会展示整个泳道单元的完整详细数据（效果等同于完整框选该泳道单元）。

### 添加/编辑标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了标记功能供开发者使用。DevEco Profiler支持两种时间标记：

* 单点时间标记：单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/n513YJhDTuWJd1G5WqMPSA/zh-cn_image_0000002731542757.png)（快捷键为M，颜色可自定义）。
* 时间段时间标记：鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/sEvscHPTTIG79UU_hJ_S4A/zh-cn_image_0000002731542737.png)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/4SGuc7DBT_mjj9S7bF9Dpg/zh-cn_image_0000002731382769.png "点击放大")

标记放置完成后，可以通过双击标记按钮，在弹出的标记属性框中修改标记的描述和颜色信息，或者删除标记。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/l1AZvTFaTCeqWTYX-7IbaA/zh-cn_image_0000002701823486.png "点击放大")

通过快捷键“Ctrl+, ”向前选中单个标记，“Ctrl+. ”向后选中单个标记；“Ctrl+[ ”向前选中时间段的标记，“Ctrl+]”向后选中时间段时间标记。

此外，工具还提供了查看不同标记之间时间差的能力，只需要先选中一个标记，再将鼠标悬浮在其他标记点上，便可在面板右下角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Kz_c0MGlRkmWfi7fZ-_Wiw/zh-cn_image_0000002701663550.png)后看到被悬浮的标记点和被选择的标记点的时间差。借助这个能力，开发者能够快速获知一些特定时刻的时间差，这对于分析时间敏感的性能问题尤其有用。

### 收藏泳道

在使用工具分析，可能会遇到泳道过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Vw3yh3HURIaqfa3FfPXq9A/zh-cn_image_0000002701823470.png)，点击该按钮即可完成收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/GyBAk7aNSpm7433ZHEgRtA/zh-cn_image_0000002701823472.png)

再次点击该按钮则取消收藏。此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/-ccaOKbMRFqfa7f4_lE6EQ/zh-cn_image_0000002731382763.png)图标，可以将收藏的泳道进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/rlb92gzzS7WFOsqcFsNO1A/zh-cn_image_0000002701663542.png "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fen_tXcDSeafb4jr4yG6Hg/zh-cn_image_0000002731382785.png "点击放大")

### 展开/折叠子泳道

工具提供了两种方式展开/折叠子泳道：

1、点击父泳道左边小三角符号![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/p60KCo4uQvut1fnQlTc24g/zh-cn_image_0000002731382787.png)。

2、双击父泳道表头区展开泳道。

### 全局搜索

为了帮助开发者迅速查找关心的性能数据，DevEco Profiler工具提供了全局搜索功能。

1. 在搜索框选项区可选择搜索类型，支持搜索泳道和搜索泳道数据，默认搜索泳道数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/mcECBDqXQySOTUluuQ8okg/zh-cn_image_0000002731542729.png "点击放大")
2. 搜索泳道数据，在输入内容前或搜索到结果后希望进一步确认搜索范围，可以选择在全时段内搜索或者在框选的时间范围内搜索；也可以选择在所有泳道内搜索或者在选择的泳道范围内搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/dKszeZ1oTu6EZMF0nXrVdA/zh-cn_image_0000002731382777.png "点击放大")
3. 可以点击**Cc**按钮，设置输入的关键字是否忽略大小写，默认为忽略大小写，点击时可自动重新触发搜索，搜索结果数量会显示在搜索栏右侧。有搜索结果的关键字会自动被记录到历史记录中，开发者可以通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/I93kgtRUT0KU2bh78fXHxA/zh-cn_image_0000002731542749.png)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3KkYIXGbT3uMaryIykpWLw/zh-cn_image_0000002731542763.png)按钮，向前向后查看搜索结果，泳道区域会自动跳转到对应的结果位置并为开发者选中该结果，详情面板中会自动刷新出相应详细数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/fiqQdU4kQ5CJbJypb44a-A/zh-cn_image_0000002701663548.png "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/wEaOIFS4SEW-N4SNgVBhJA/zh-cn_image_0000002731382771.png)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库、用户自编译的so库、三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/H4IO4-P3QTqaBvzyUMxqCA/zh-cn_image_0000002701823458.png "点击放大")

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等），可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

### 源码跳转

找到问题源码是调优过程中最为关键的一环。针对详情面板中所展示的函数栈帧信息（如下图所示），双击栈帧节点，工具便会在编辑器中打开相关源码文件，并定位到对应行号。此功能正常使用的前提是用于抓取性能数据的应用，是在DevEco Studio的当前工程开发编译，且相关源文件位置并未改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/A9Dy09PyRGaLZDc3crRBDA/zh-cn_image_0000002701663554.png)
