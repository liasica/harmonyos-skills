---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-data
title: 数据区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:24+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:264a5109574bdf4804285b90b0da356476e41e8bf75b929e8cdd53f0c26457fb
---

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/bMPCKODBSIGJ5OplbCYtSA/zh-cn_image_0000002750009952.png "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供收藏、离线符号导入、泳道过滤和数据全量展示等辅助功能的管理能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/b_KaJhmPRTGOyFofKXHlTw/zh-cn_image_0000002750169838.png)：离线符号导入按钮。点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VxXMNlYkQAKOSHNuOX9U7Q/zh-cn_image_0000002750009956.png)：收藏泳道的隐藏/折叠按钮。激活后会隐藏/折叠收藏的泳道，高亮时展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/W0NuM2IIQbSy6h2Fee2E7g/zh-cn_image_0000002779608859.png)：泳道筛选按钮。点击可选择泳道进行过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/IpdcEyffS_-2OZe2Nn2tKg/zh-cn_image_0000002750169854.png)：数据全量展示按钮。点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

② 时间轴：提供横向时间轴，用于显示数据时间戳。

③ 标记栏：用于放置标记，能够帮助开发者标记时间点或时间段。

④ 泳道区：泳道图区域。每个场景化模板都会预置一系列泳道单元（例如上图的**Memory**便是一个泳道单元）。泳道单元是整个DevEco Profiler工具内，数据组织的最小独立单元，用于剖析应用某一特定维度的运行数据，每个场景化模板均是由一系列泳道单元组成，每个泳道单元都会呈现某一维度的性能数据。开发者可以查看数据随时间变化的特征，发现数据异常的时间段，支持框选时间段后在详情面板查看对应的细节。

**说明** 

* 每个场景化模板的泳道单元，遵循Top-Down分析原则，越接近顶部的泳道单元，所观测的性能维度越抽象，越顶层；越底部的泳道单元观测的性能维度则越接近于系统底层，建议按照自顶而下的顺序去分析泳道单元呈现的数据内容。
* 同一个泳道单元中，泳道区中主要展示时间维度的性能变化，帮助开发者首先定位出有问题的时间段；进而通过详情区查看该时段各维度的详细数据，分析具体影响性能的参数或属性。

⑤ 详情区：展示详细的数据细节。开发者在泳道区域选择数据之后，以各类表格的形式呈现该时间段内各项详细数据。More面板将对左侧详情区中选中数据进行补充描述。

## 基本操作

### 开启/关闭会话控制

可以开启和结束会话的录制，点击工具栏的首个按钮即可，如下图所示分别对应开启录制、结束录制功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/pPZtoljQTIW7OTXJS8cgQQ/zh-cn_image_0000002750009958.png "点击放大")

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/s24-nAnfQ_yE6ZNyy9n3dg/zh-cn_image_0000002779608875.png)按钮展示全量数据，时间轴尺度会自动调整，展示会话完整时间范围内的数据。
* 鼠标单击右侧泳道数据区后，使用快捷键A/D或使用Shift+鼠标滚轮，可以调整时间轴所示的时间范围；通过快捷键W/S或使用Ctrl+鼠标滚轮，可以调整时间轴所示的时间范围的大小。
* 拖动泳道右侧滑条或者滑动鼠标滚轮，可以控制泳道上下滚动。

更多快捷键使用方式请参见[快捷键](ide-hmos-shortcut-key.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/eK1mUuteStWa11G5mIPXug/zh-cn_image_0000002779608865.png "点击放大")

**说明** 

使用W/A/S/D等纯键盘的快捷键操作，仅在已激活的泳道区域生效。泳道区域中存在亮蓝色的选中边框即为激活状态。

### 添加/编辑时间标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了两种时间标记功能供开发者使用。

* 方式一：单点时间标记。单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/2S697FFLRjS_Ec6ljdI6fg/zh-cn_image_0000002779608871.png)（快捷键为M，颜色可自定义）。
* 方式二：时间段时间标记。鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/yYPlwK9UTpyzLA6Y8lT97w/zh-cn_image_0000002779729005.png)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/qwNKMwDpTUGnnzWJCF4mzw/zh-cn_image_0000002779608861.png "点击放大")

标记放置完成后，支持使用**C****trl+**，向前选中单个标记，**C****trl+.** 向后选中单个标记；**Ctrl+[**向前选中时间段的标记，**Ctrl+]**向后选中时间段时间标记。同时，支持通过单击鼠标右键点击**编辑****标记**，在弹出的标记属性框中修改标记的描述和颜色信息，或者**删除标记**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/e4iKS-ygSTSRr3aR7FlTzQ/zh-cn_image_0000002750009946.png "点击放大")

### 收藏泳道单元

在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/I9325JJBR5eerIpAUMBJUg/zh-cn_image_0000002779608869.png)，点击该按钮即可完成收藏，再次点击该按钮则取消收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/RHmgfxoZR-eqvTAARtsuhg/zh-cn_image_0000002779608873.png "点击放大")

此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/siowJzSDRvy6DrKH9mPIbQ/zh-cn_image_0000002750169844.png)图标，可以将收藏的泳道单元进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZMmjTT3eRTKEUznAWoCfMg/zh-cn_image_0000002779608863.png "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/FXyCR41URHi_nvjX5x_TaQ/zh-cn_image_0000002750009948.png "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/JJXFRaXsRXudsjVKfWC-CQ/zh-cn_image_0000002750009954.png)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库、用户自编译的so库、三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/hsVlGtpFRpCHiXYgEzh7vQ/zh-cn_image_0000002779608867.png "点击放大")

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等），可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。
