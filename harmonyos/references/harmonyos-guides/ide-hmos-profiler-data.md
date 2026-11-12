---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-data
title: 数据区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 数据区
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0f89e8a00d18caff485fb1ec81a8a7286008fd68bfc1e71eaf26cf158e28c7bf
---

在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节对所有模板的通用能力展开介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/jrmo7mqwQBS8XG5xJCp0dg/zh-cn_image_0000002810751005.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=476D22FF8B3F03E994BA90DE51B4280EC1507244E4A7B720134AA8F2729CA927 "点击放大")

整个数据区可以分为五个区域：

① 工具控制栏：提供收藏、离线符号导入、泳道过滤和数据全量展示等辅助功能的管理能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/3XE6TJNvQAyZWFTdKbMoDA/zh-cn_image_0000002781311404.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=821D6374C79AE1DA4E172F4D7BCD1CA85F378022C18AB589C19F6FD3C95630BE)：离线符号导入按钮。点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/GeZ3LHjTRiKUCtINRe_wwg/zh-cn_image_0000002781471350.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=40155C4D7D3C2B8731AD66C3B611F95258D97690906673F0BD56C2D2F2D26F51)：收藏泳道的隐藏/折叠按钮。激活后会隐藏/折叠收藏的泳道，高亮时展示收藏的泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/unztLan5Re-Oaj61UzF4FQ/zh-cn_image_0000002781471340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B579E238C9BCEDAD0CF9469AAB954C1FA0CC6CE0B120B07A8E46804B6B85DB74)：泳道筛选按钮。点击可选择泳道进行过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/aSkRuTkBRjWdj1AX4PMiQg/zh-cn_image_0000002781471352.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0914ADBF07AB048FAAA1F145A0038BAA8848385C1FD6D0B539400D5F6D5EAA76)：数据全量展示按钮。点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/y_eUC4VjQze5B71z5tWlTg/zh-cn_image_0000002781311414.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC8088BE3B714DF57D8CF8AC675E3945516D3F5924308629BE902CC1D230FFDD "点击放大")

### 时间轴控制

DevEco Profiler工具提供了各种丰富的时间轴操作功能：

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/XoeiEfDaQ46uvXm7OKRI6Q/zh-cn_image_0000002810751011.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDB97CDC835037CF87C1CA2A13D8505DA236A367C681DB2F9B140BAEA2AA2270)按钮展示全量数据，时间轴尺度会自动调整，展示会话完整时间范围内的数据。
* 鼠标单击右侧泳道数据区后，使用快捷键A/D或使用Shift+鼠标滚轮，可以调整时间轴所示的时间范围；通过快捷键W/S或使用Ctrl+鼠标滚轮，可以调整时间轴所示的时间范围的大小。
* 拖动泳道右侧滑条或者滑动鼠标滚轮，可以控制泳道上下滚动。

更多快捷键使用方式请参见[快捷键](ide-hmos-shortcut-key.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Qyzcu9BrSUatMuEFpNL4Bw/zh-cn_image_0000002781471346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E51C67F8DBDE5994A5AA03C00B03EC50E8044E29E7A6E5B5D9BEAD37824FF507 "点击放大")

**说明** 

使用W/A/S/D等纯键盘的快捷键操作，仅在已激活的泳道区域生效。泳道区域中存在亮蓝色的选中边框即为激活状态。

### 添加/编辑时间标记

为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了两种时间标记功能供开发者使用。

* 方式一：单点时间标记。单击需要关注的时间点，添加的时间标记显示为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/B8K_KVUNS4StE0iVqZJdmA/zh-cn_image_0000002810751009.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F628A2FBFDA50FF90AAC8B12B417B156A6940D7FD077779879B870E859850F71)（快捷键为M，颜色可自定义）。
* 方式二：时间段时间标记。鼠标框选要关注的时间段，单击该时间段右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/flUXPnBUS1CJRh2824qXuw/zh-cn_image_0000002781311402.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0341A555E05C035005E73B51736E8F97C6CE718721EFB5141317D69913B4A866)添加时间段起始标记（快捷键为Shift+M，颜色可自定义），如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/PCqmRknVSHqGEoxGGB-HIg/zh-cn_image_0000002781471342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=33BA5B4AE4A3A9172D348F7EEE83DE47392F88544D29521D1AFB71C40B4D40BC "点击放大")

标记放置完成后，支持使用**C****trl+**，向前选中单个标记，**C****trl+.** 向后选中单个标记；**Ctrl+[**向前选中时间段的标记，**Ctrl+]**向后选中时间段时间标记。同时，支持通过单击鼠标右键点击**编辑****标记**，在弹出的标记属性框中修改标记的描述和颜色信息，或者**删除标记**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/5zdZ-sjVRKGOzBSlbmVchQ/zh-cn_image_0000002810630893.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=43ECB1603B6EB261EF92373137B4CC5132B5976C216EC4D39D52D674F9316532 "点击放大")

### 收藏泳道单元

在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gbYWl6OdSDa5SoV207sa_Q/zh-cn_image_0000002781471348.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A724C9141803084FB0929F1FFB4DA4F952C4540727626BAD58A0ED79CCF7EE2D)，点击该按钮即可完成收藏，再次点击该按钮则取消收藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/jrsrlFGESxakLb7Ng8pruQ/zh-cn_image_0000002810630899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB32ADF3A263DB755FCF71E10BC2F8619558B648162F905DF164FE422379F2F7 "点击放大")

此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-FTFC1f7SPqQDBwPQyjCpQ/zh-cn_image_0000002810630895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=088BDE37F10662347E66EA94F53081A183D271C85A1AF2C02E612C4AD1CDD482)图标，可以将收藏的泳道单元进行折叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/OsiAo6BVSM-ykdEyX7Nz_A/zh-cn_image_0000002781311408.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA281CED135A85D26AC18284129F8CDF95AF6FD6988746F5B68BBABE4282062A "点击放大")

如果收藏的是父泳道，且泳道标题展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道标题信息。

如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道和子泳道标题信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/zx_R6XuPThCW1hgJWUt43Q/zh-cn_image_0000002810751003.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4503D05E7C5AB8A34B1D6AAE853B1C7D147CFE57D1151DE8F2787A2E3C7A69DA "点击放大")

### 离线符号解析

为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/AWEID8mXSNuRjkUWjybeIA/zh-cn_image_0000002810630897.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B8B11C695FB4BC53FB7131292E7BEE75A35512FB831E66A9DCF25697331307B)按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库、用户自编译的so库、三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/O7mE6B5XT5ym-3WUr3LC5A/zh-cn_image_0000002781311410.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=65FBEBC8C1EC972FBDB4B03DAE83C2E825FFD8F1F680C0DAD2C4BF3676442DA5 "点击放大")

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等），可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。
