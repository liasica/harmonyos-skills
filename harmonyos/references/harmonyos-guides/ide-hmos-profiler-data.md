---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-data
title: 数据区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4c33017ef29722afb5dee4ffa8293dfdf5625caabd9e341dd73c515a8d3f0d27
---

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/ALI4GZuFR46GBARTctcdRg/zh-cn_image_0000002810751005.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B1A66BB8FCACE223EFF04500DFEC6140EE4CCD84BBA59870A8FFA120C017D32 "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供收藏、离线符号导入、泳道过滤和数据全量展示等辅助功能的管理能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Tm083nxRQ_W7DVizEXerOg/zh-cn_image_0000002781311404.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=EADC1C4D537BA07325FB1A062030B00D88B859265606E58C12E1E4E250273CF5)：离线符号导入按钮。点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/nwPt75tQRVmW0XpP4JSDkg/zh-cn_image_0000002781471350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8C432F6FFFECBCE33F5C25E1A0FAFA987E3AB7D7296B4E567C2F91853564921)：收藏泳道的隐藏/折叠按钮。激活后会隐藏/折叠收藏的泳道，高亮时展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/d7vqVIl9TNaynixzfmzveQ/zh-cn_image_0000002781471340.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA73C71B149085C062418C177AA53F85AC3DC562CA7B8807704CC5F03B29D693)：泳道筛选按钮。点击可选择泳道进行过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/fQV-mGsmSxWx09fcJwFImw/zh-cn_image_0000002781471352.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EC71D23069DE02B83563353A13E3774B84AC01581DCDC8C8EA4952494C5978B)：数据全量展示按钮。点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/1GSlBnx7TDqBEcJLGwUukg/zh-cn_image_0000002781311414.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B8591BCC92A8BCC73B2E1945F7689D9A6187E045321A6977DF6B5FE33B73E59 "点击放大")

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IAPuUkjhTVmLFre8D9AVYg/zh-cn_image_0000002810751011.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=D50906D131C3D24D714ECC65086EDB4D19DD66B35F13AB17496B6E92CD1F9769)按钮展示全量数据，时间轴尺度会自动调整，展示会话完整时间范围内的数据。
* 鼠标单击右侧泳道数据区后，使用快捷键A/D或使用Shift+鼠标滚轮，可以调整时间轴所示的时间范围；通过快捷键W/S或使用Ctrl+鼠标滚轮，可以调整时间轴所示的时间范围的大小。
* 拖动泳道右侧滑条或者滑动鼠标滚轮，可以控制泳道上下滚动。

更多快捷键使用方式请参见[快捷键](ide-hmos-shortcut-key.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qK-PZZKDSOqGrPAYvoliIg/zh-cn_image_0000002781471346.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9D2743145E99CA3F4A4146A8BAEADE7CD46CBA28704448FC37DCC5D8BB8BF96 "点击放大")

**说明** 

使用W/A/S/D等纯键盘的快捷键操作，仅在已激活的泳道区域生效。泳道区域中存在亮蓝色的选中边框即为激活状态。

### 添加/编辑时间标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了两种时间标记功能供开发者使用。

* 方式一：单点时间标记。单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/z4ZZgmo9QJ6vb3Wnyl1DLg/zh-cn_image_0000002810751009.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FC43438F66871C0F5A2992E942BF5C9A7B18E6E0803AE331D33CADE14C61EF4)（快捷键为M，颜色可自定义）。
* 方式二：时间段时间标记。鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/OMZprO3tQUKYIMf9uRzgww/zh-cn_image_0000002781311402.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=A157845529FEDA58AFB6A634FFC0B13F610C96822D1719486E317969A54F6DB2)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/21H0-lpPTzG1-OXEMc4Utg/zh-cn_image_0000002781471342.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C5A75E1E516BDB8CAA72179C250674E0CB202126ADFDF9CF4BCC1FCED6FBC86 "点击放大")

标记放置完成后，支持使用**C****trl+**，向前选中单个标记，**C****trl+.** 向后选中单个标记；**Ctrl+[**向前选中时间段的标记，**Ctrl+]**向后选中时间段时间标记。同时，支持通过单击鼠标右键点击**编辑****标记**，在弹出的标记属性框中修改标记的描述和颜色信息，或者**删除标记**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/MxQHoF-jSKm8Ki48YcYwoQ/zh-cn_image_0000002810630893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB6CC8A3D80444F77D891C918BA2BA5FB3C595AF0F5A707C93BEAF748CDE0EE2 "点击放大")

### 收藏泳道单元

在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/k0sQ_V-RS32ItNwaaKIWWw/zh-cn_image_0000002781471348.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=D04A0D8548B95BC3B131D892CDA40FF4B27ACD2130300B7720C997A471DEF3D7)，点击该按钮即可完成收藏，再次点击该按钮则取消收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/uvTb09iWRoq5kWFhB04DYA/zh-cn_image_0000002810630899.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=532DA0EF684DD93321458279BCBB991351BEA5E2333A460E2293F19C8BCA7E53 "点击放大")

此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wv-lb2gQTEOcSYdvju5avw/zh-cn_image_0000002810630895.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDEFE775D0DFCB352EB101AA60BB7F66018C8CB9415614D59705B73D82F4BCB0)图标，可以将收藏的泳道单元进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/PF3Q4fRvRNaUFH4atOzAPA/zh-cn_image_0000002781311408.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EB96077E4A7C322D3D2CB65ABBA4FEBA6A4E4BBE504DD0F39BD79A1CE5486A5 "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/7JY-oOg3TiC_M8XpgJzTig/zh-cn_image_0000002810751003.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=255C69720554DA8A5495FBB42FBF1D69BF73F97FC2287F585A5B5C0DE8EB2F71 "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/I-DWVBunTXqlYZW12mSe9w/zh-cn_image_0000002810630897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAFD235FC1695FF4A1684E97DB85AAF6A33140D8E2358A8F0B31F79E79651F1E)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库、用户自编译的so库、三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/IuHKAjtPTkKQXrgzMHTuag/zh-cn_image_0000002781311410.png?HW-CC-KV=V1&HW-CC-Date=20261114T004919Z&HW-CC-Expire=31536000000&HW-CC-Sign=86DE732EA319232BC632B7C8507060AE10CE8FBAF4A250B07CD9C24FB3332E8D "点击放大")

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等），可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。
