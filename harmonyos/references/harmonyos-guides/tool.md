---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool
title: 实用工具
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 实用工具
category: harmonyos-guides
scraped_at: 2026-04-29T13:48:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74a79ea2e3f2703d9ea687c269eb62a34df47f75d56b418319a82c6136e22cb8
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/wpxbSrDiSamSbGQczleQmw/zh-cn_image_0000002503553988.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=545F1593F147133086739E88703A2B7898C09B3423FF8AB168E9012AEDC5509B "点击放大")

## 应用图谱管理工具

**应用图谱管理工具：**支持从探索测试执行报告导入和创建空白图谱等多种方式创建图谱，支持通过屏幕录制和从图谱选择方式创建场景，支持对场景路径进行调试对比。

### 应用图谱特性管理

打开DevEco Testing客户端，在左侧菜单栏选择“实用工具”，点击“应用图谱管理工具”卡片进入工具界面。

**创建图谱**

点击“创建图谱”，有以下选项：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6BoLww-ZSdOaBUYY20D-BA/zh-cn_image_0000002524623461.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=F069CC634007C815E2940791DC7E7BF3A35658F39E0594EADA11E0C1884B3000 "点击放大")

探索测试报告：选择相应的探索测试任务，输入待创建的图谱名称和说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/U-5_1-CnQ3eaCBXKkaBCog/zh-cn_image_0000002524623437.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=B92FB1F79155E0589AB308B9D2DC7F340CF08D514E5285385881B429964E5C8B "点击放大")

从现有图谱文件：复用已有的图谱文件。

在用户的DevEco Testing数据路径（DevEco Testing客户端->设置中可查看数据路径）中找到“graphTool”文件夹，找到相应图谱文件夹后；将其中所有打包成zip文件（注意：打包后文件需要直接是图谱文件，不能多加一层目录，如下图所示）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xn2SKbNRSLOnGzIzstn1GA/zh-cn_image_0000002492503772.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=B0125F750585F082F288A6D53A50DE24E81FBD1FCA84A67B1B0828E12CE7863C "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/htlhOXCXTzu5zRfuTcyFKA/zh-cn_image_0000002524503471.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=3C952774E6981CDF80600ACB074BDF9920DDBA08119DC01E30771221C50E11E7 "点击放大")

空白图谱：选择对应的应用创建空白图谱。

图谱名：图谱名称。

图谱说明：增加图谱说明。

设备列表：选择连接的设备。

应用包名：选择设备已安装的应用。

应用描述：对应用增加描述。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/VnfoVKHRSxy1k0QGoKrS1g/zh-cn_image_0000002524623469.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=C8DF41E66B6BAAC03F99555FFD48B41D75F59A88FE4DC06700279C468E2603A3 "点击放大")

说明

在客户端设置->基本设置页面的数据路径下，“graphTool”文件夹存放所有图谱数据。

**特性管理**

新增特性：点击新增特性按钮，输入特性名称和特性描述（非必填），点击提交按钮新增特性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/vqPwIsNVT-OaWb0BrJUptw/zh-cn_image_0000002542128675.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=CE41EBC438CE4D8812B864D63E912A446F08F259FDEF3F2C3A56E1343EC1A452 "点击放大")

删除特性：勾选特性后，点击删除特性按钮，勾选待删除特性，出现删除确认框，点击确定按钮完成删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wJhdAMRAQ66SEbSixo5VCw/zh-cn_image_0000002542128863.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=4A9E7C83C4196369BDC7129CAB515D7BEA40C5B83FB954E9FBF6B73F9EB536F4 "点击放大")

编辑特性：鼠标右键点击特性名称，选择修改特性按钮，修改特性名称、特性描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/sU30YJcKR7KGEH3v4mm87g/zh-cn_image_0000002524623467.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=E26A524E74F0728AA0AF97FFBBDD249EFDB3CA76CE4B5E501CB09BD6518ED14F)

### 应用图谱工具场景路径管理

**新建场景路径**

步骤1：选择已有特性，点击新建场景路径按钮或鼠标右键选择新建场景路径，进入场景路径编辑页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2kqjHLVHT0SOuIc3CfbL1w/zh-cn_image_0000002510528426.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=DE2FA194D89069AF5154AB0130E830234C66924ED69B4F0193E8E10A7053857E) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/T7exFjnoRI2orSvakN_Knw/zh-cn_image_0000002510568464.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=FB638060481495E1B5D9EF0F66ABC7E02FB6833F33092F5EF3AE11FE44B0630B "点击放大")

步骤2：“编辑模式”窗口中的首个页面为设备桌面截图。点击窗口中的“➕”号创建场景路径，支持“通过屏幕录制添加”和“从已有图谱事件选择添加”两种方式。

步骤3：添加场景路径。

（1）通过屏幕录制添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/2C7QGaNeTQa3v3t1OmMu0Q/zh-cn_image_0000002492343776.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=BDCD91192053E0C2D0D3B8DBD60FE30565E2EEA56A62F7916C57DD20F1F3D2CB "点击放大")

在点击“➕”号之后，选择“通过屏幕录制添加”。

通过在左侧投屏设备的区域内，执行点击、滑动或者右键弹窗输入文本动作，添加相应的场景步骤，点击保存按钮完成场景创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ahSP3PrESYaTw1qJtJnkag/zh-cn_image_0000002492343790.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=7B6B7A1ACD94EBB5F989DE2F92557DCF0C2B8856B77331522C5194F55ACB31F4 "点击放大")

将鼠标移动到设备投屏上，右键单击后会出现以下功能选项：

在此控件上输入内容并回车：用于搜索场景，输入文本并搜索。

在此控件上仅输入内容：用于搜索和文本框场景，仅输入文本。

重新获取当前页面控件：当页面控件识别不准确，或未识别到预期控件时，重新获取当前界面的控件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/3rjBBys_QEGgnjHA7e7zrA/zh-cn_image_0000002524623433.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=633D405D6026214C41828A7D68D3FEEBD4ECD3EB4602645F52A0979FAEA86E09 "点击放大")

（2）从已有图谱事件选择添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/siZFkHMeTEqxCZODv9baEA/zh-cn_image_0000002492343798.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=F42AB82B6287FF9146EBA50F8423BFAE92A1E5B19D2DE7B97A5B6483CC0F0A37 "点击放大")

如下图所示：

①：展示当前页面。

②③：展示对应选框点击前后的页面。

点击“➕”号之后，选择“从已有图谱事件选择添加”，将出现图谱中记录的事件，选择图谱事件创建路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/60ZvilmqT3ihJnWNmdcCYA/zh-cn_image_0000002524503449.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=09D9E47DBA7DE6AA62B86F65FD1B0B3D0B6A9D77C491C0181FA1FB2AA9C637E9 "点击放大")

步骤4：调试场景路径。

场景路径创建完成后，支持对其进行调试，验证创建的场景路径能否在设备上运行正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/iTU79pKUSLKbZCT9LOdi8g/zh-cn_image_0000002524623443.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=61168E8F965FDE934BF83E25A6EB82A4D9AB2E55033FA15FDBF715F2CCEF97F2 "点击放大")

**编辑场景路径**

选择已有的场景路径，点击鼠标右键或点击窗口右上角的按钮进行编辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/eu1OTO-NTPeD3QsUo-f4vQ/zh-cn_image_0000002492503756.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=4476D8ADA5DB35983E1144F7826B3652DCA702EC019D92A04B760D4E5ECE597E "点击放大")

屏幕录制场景路径编辑：支持删除、刷新旧页面和“插入新节点”（注意：需手动将测试设备保持在所需页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5YnsulD0Sn2zflDGQlllwA/zh-cn_image_0000002492503750.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=27BDA1FF65B63994987DB75EDC9455C081D0C2B19DB4E9BA01F1BB75F484E6A2 "点击放大")

**场景路径压测**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/boYbQkwsRoWHE-1tK8bDww/zh-cn_image_0000002492503776.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=CFBFFEC0E267D5B58947D37A3698CADFD99A0A55E9FD42EC5571A0B0EFE8A812 "点击放大")

探索测试服务创建场景压测任务**：**

选择测试服务：打开DevEco Testing客户端，在左侧菜单栏选择“探索测试”，点击“探索测试”卡片，进入探索测试服务创建页面。

选择应用：选择应用图谱对应的应用。

选择图谱测试的路径：选择所需的测试时长、模式类型等配置信息。

模式类型：场景压测模式会出现场景选择选项。

图谱选择：选择编辑的图谱。

场景选择：选择已创建的场景路径。

创建任务：点击创建任务按钮，探索测试将在设定时间里循环对该路径进行压测。

## 性能测试报告对比

**性能测试报告对比：**提供同类性能测试服务的报告对比分析，涵盖场景化性能测试、性能基础质量测试及性能指标监控测试三大服务。

**选择测试报告**

按需选择同类性能测试服务报告对比分析，支持按任务名、备注信息或任务状态筛选。点击开始对比，即可一键生成对比报告。

性能测试报告对比有两个任务创建通道。

（1）从实用工具创建任务

步骤1：进入工具任务创建页面。

点击导航栏的实用工具，点击“性能测试报告对比”进入任务创建页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/pXor6rL8SlO0MEjrWseiRg/zh-cn_image_0000002492503724.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=0289EA27A2962677809065C8B91DF4553C0A9F394DFD35EC5DFF941F67364325 "点击放大")

步骤2：点击选择需要分析的测试任务报告，再点击开始对比即可。

注意

性能测试报告对比只支持场景化性能测试、性能基础质量测试和性能指标监控测试生成的报告。

（2）从性能报告页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“报告对比”按钮，点击后跳转至性能测试报告对比工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/kn7NN4bKTmSMVO47XtsNqA/zh-cn_image_0000002492503722.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=FACAC430D31D0D502FE93D98402DEED66A9693DE3CCC5D1E42AB63F6224CD751 "点击放大")

步骤2**：**跳转到性能测试报告对比创建任务界面后，会自动选中刚执行完的任务；选择基线报告后，点击开始对比。

**查看对比报告**

性能基础质量测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/CNhIgRI3T6ePvoAb4TMncw/zh-cn_image_0000002492343766.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=0126CD644AE71480FB5B9629DD5AB6036F2AD7BD9850AB7E816F22653874D176 "点击放大")

场景化性能测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/rXPz55y5SJe2ehLIFEvqRg/zh-cn_image_0000002492343760.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=9373CDB105579BFD769A01B18C5EB3FE6F6235A3DEA78C5D3DD1F7B8ACE6E74B "点击放大")

性能指标监控测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/jCFzJg5ISlGN2SCVM4gt-w/zh-cn_image_0000002492503728.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=18A75D6DF953BEA6A57F7348E085315EB54FCC5BD39DBE8629B47BD3A56AD769 "点击放大")

## 性能报告自动分析

**性能报告自动分析：**工具通过自动化手段深入分析测试数据，运用高级算法和技术自动识别异常情况，并尝试定位问题的根本原因，帮助用户快速找到影响应用性能的关键因素。该工具支持分析场景化性能测试和性能基础质量测试两种服务生成的报告。

**工具使用场景：**用户在日常测试开发中遇到场景化性能测试或性能基础质量测试检测出的问题时，可使用本工具进一步分析问题原因。

性能报告自动分析会将检测指标分为以下几类，仅支持对部分指标进行诊断，具体如下：

|  |  |
| --- | --- |
| **指标大类** | **指标名称** |
| 时延 | 响应时延 |
| 完成时延 |
| 卡顿 | 最大连续丢帧数 |
| 卡顿率 |

**任务创建**

性能报告自动分析测试服务有两个创建通道。

（1）从实用工具创建任务

步骤1：进入工具任务创建页面，点击导航栏的实用工具，点击“性能报告自动分析卡片”进入任务创建页。

步骤2：点击选择需要分析的测试任务报告，再点击创建任务即可。

注意

性能报告自动分析只支持场景化性能测试服务和性能基础质量测试服务生成的报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/sQPQxtx7Riil4ml7zpEm2w/zh-cn_image_0000002492343778.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=BE260E794FD9F9A95789AF6A98BCAE5ACC09CD18A98284538A4FEBDE0DEB7C0C "点击放大")

（2）从性能报告页页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“性能报告自动分析”按钮，点击后跳转至性能报告自动分析工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2gbMj1wOQe6fzk52BPj0QQ/zh-cn_image_0000002492503748.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=1E4060A82B45AD0A9B026EC7925300D9A10C7668A0059485672D5EEC6035A89B "点击放大")

步骤2：跳转到性能报告自动分析创建任务界面后，会自动选中跳转前的任务；点击创建任务开始分析。

**报告解读**

**基础信息**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/myFVzjq3RsWzOdp6sBWXvg/zh-cn_image_0000002492343806.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=DCEF876DEAF83E2EF0B204B84B38D57E8CA93BCAA85D0D16A0DCD72C36A17F18 "点击放大")

报告基础信息中主要包括如下部分**：**

* 任务信息：任务名称、开始时间、持续时间、执行人。
* 工程路径：分析的测试任务所在位置。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

**概览**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2Rz1FwA1TSm2r3hxAHg-VA/zh-cn_image_0000002492503734.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=EE3CF3C3A6D4B7B048E9C9FF007F0225F080F38859CD3C3877455A9EC28E0418 "点击放大")

测试服务：分析的任务类型。

测试报告名称：分析的任务名称，点击可跳转至该报告。

支持问题分析数/问题总数：如上文介绍，部分问题不支持分析，因此分析数会存在小于总数的情况。

根因统计：所有分析问题的根因统计列表，由于一个问题可能存在多个根因，因此总数可能大于问题数。

分析结果导出：将所有支持分析的问题步骤打包归类在导出目录下，并生成excel文件存储每个文件对应的分析结论，每个问题步骤会打包成zip文件，每个 zip 文件包含 perfdata，视频和帧图片集。

导出的目录内容结构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nBjApW9DRiSX6kELiGmKeA/zh-cn_image_0000002492503720.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=6554ABDE82DBE9852A0AA3C9827A53755FC2F045713783DFC7AF2D36F8DBE04A "点击放大")

**分析详情**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dEaPscd_Ri-rgHxFvIuSXg/zh-cn_image_0000002524503501.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=D9AC823F629248417F458503727997CF510425CB18C06B695BEC4BD767767575 "点击放大")

用例场景：测试用例名称。

操作步骤：测试步骤名称。

指标类型：不达标的问题类型。

根因：导致不达标的主要原因。

指标值：指标具体的测试值。

分析结果：成功表示存在分析结论详情，失败表示该任务未分析出具体结果。

维测数据：点击打开按钮可以跳转到问题步骤对应的资源文件目录。

分析详情：点击展开可以看到对应问题的详细分析结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/IE_niNGYT4moAHi8WchQNA/zh-cn_image_0000002524503483.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=E0CB669C9D3F0FD79CCBB30B5E73F05FBBBB53452B6A56A34F3D51DFE342960A "点击放大")

根因归属：导致此问题的主要原因在于应用还是系统。

根因描述：问题产生的原因描述，从上到下根因归类更细。

分析详情：详细的分析结果，如哪段函数耗时异常、节点创建过多等问题。

耗时分段拆解：自顶向下逐步分解性能问题，聚焦真正影响性能的问题。橙色区块代表影响性能的主要原因，需要重点关注；蓝色区块代表耗时拆解的次要原因，对性能问题影响较小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1CZGidyLSaOewYAh85UqCA/zh-cn_image_0000002524503493.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=EC3345195909A0ABA00E426309178830190202F20BDCE538DDEF2EAE45425997 "点击放大")
