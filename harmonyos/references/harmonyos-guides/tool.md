---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool
title: 实用工具
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 实用工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cf44560822d12ed64285cf3f6831326508a19fecb291d9f4e20c9d33f6368e2
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/wpxbSrDiSamSbGQczleQmw/zh-cn_image_0000002503553988.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=307290112CF5D2B5EE0925DD65851CC255A5CACD469CBFA10613DF9E1E428953 "点击放大")

## 应用图谱管理工具

**应用图谱管理工具：**支持从探索测试执行报告导入和创建空白图谱等多种方式创建图谱，支持通过屏幕录制和从图谱选择方式创建场景，支持对场景路径进行调试对比。

### 应用图谱特性管理

打开DevEco Testing客户端，在左侧菜单栏选择“实用工具”，点击“应用图谱管理工具”卡片进入工具界面。

**创建图谱**

点击“创建图谱”，有以下选项：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6BoLww-ZSdOaBUYY20D-BA/zh-cn_image_0000002524623461.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=B56257EC474081B756719B2A1AE069A5B3FFF175096CE9CA6D11AF2042FD95C9 "点击放大")

探索测试报告：选择相应的探索测试任务，输入待创建的图谱名称和说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/U-5_1-CnQ3eaCBXKkaBCog/zh-cn_image_0000002524623437.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=886043187061DE449E1955D0C05A3116EE619011E207B68577D982B63035CF1F "点击放大")

从现有图谱文件：复用已有的图谱文件。

在用户的DevEco Testing数据路径（DevEco Testing客户端->设置中可查看数据路径）中找到“graphTool”文件夹，找到相应图谱文件夹后；将其中所有打包成zip文件（注意：打包后文件需要直接是图谱文件，不能多加一层目录，如下图所示）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xn2SKbNRSLOnGzIzstn1GA/zh-cn_image_0000002492503772.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=158FADCC6AF973BBA6E318A81AEB0BA2D43FC222639A42CEC1C5DC0737752EE9 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/htlhOXCXTzu5zRfuTcyFKA/zh-cn_image_0000002524503471.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=F4D62D241E7B093D7D990407C6F956FB2C4393A948AB03494F19317030E6A0E3 "点击放大")

空白图谱：选择对应的应用创建空白图谱。

图谱名：图谱名称。

图谱说明：增加图谱说明。

设备列表：选择连接的设备。

应用包名：选择设备已安装的应用。

应用描述：对应用增加描述。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/VnfoVKHRSxy1k0QGoKrS1g/zh-cn_image_0000002524623469.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=EB285FABB7CE20EF5DFB35B1F422BCB24750D8887E368315A2BA45B00BB22E08 "点击放大")

说明

在客户端设置->基本设置页面的数据路径下，“graphTool”文件夹存放所有图谱数据。

**特性管理**

新增特性：点击新增特性按钮，输入特性名称和特性描述（非必填），点击提交按钮新增特性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/vqPwIsNVT-OaWb0BrJUptw/zh-cn_image_0000002542128675.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=FFDD4651115B789E6DB888612A3FDE9B1C5C78F89BDC21CBD5BD63240C11FAF5 "点击放大")

删除特性：勾选特性后，点击删除特性按钮，勾选待删除特性，出现删除确认框，点击确定按钮完成删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wJhdAMRAQ66SEbSixo5VCw/zh-cn_image_0000002542128863.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=2CA6F39D880A80FF251D03529B6B7DC2638F9E2FA6060BE7096BA59862523AD9 "点击放大")

编辑特性：鼠标右键点击特性名称，选择修改特性按钮，修改特性名称、特性描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/sU30YJcKR7KGEH3v4mm87g/zh-cn_image_0000002524623467.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=DACA24401FC318B6124DCC8D6EB8EE1D41B9A0368F538BDC2BD50859EABA3783)

### 应用图谱工具场景路径管理

**新建场景路径**

步骤1：选择已有特性，点击新建场景路径按钮或鼠标右键选择新建场景路径，进入场景路径编辑页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2kqjHLVHT0SOuIc3CfbL1w/zh-cn_image_0000002510528426.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=58A39D0F502E9887F36ED19390D0C0E52F45E0FEBFE236F06F2E4E37210BCE57) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/T7exFjnoRI2orSvakN_Knw/zh-cn_image_0000002510568464.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=B1F482DC499E4410B3DB7EE59D7C8B855F6D061D2920878B6AEFC2C089A49CD8 "点击放大")

步骤2：“编辑模式”窗口中的首个页面为设备桌面截图。点击窗口中的“➕”号创建场景路径，支持“通过屏幕录制添加”和“从已有图谱事件选择添加”两种方式。

步骤3：添加场景路径。

（1）通过屏幕录制添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/2C7QGaNeTQa3v3t1OmMu0Q/zh-cn_image_0000002492343776.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=B5765B50D7E20DBA885879FFBCAFEE6A782D8637BBF68C45D6D30E20DD4E86D2 "点击放大")

在点击“➕”号之后，选择“通过屏幕录制添加”。

通过在左侧投屏设备的区域内，执行点击、滑动或者右键弹窗输入文本动作，添加相应的场景步骤，点击保存按钮完成场景创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ahSP3PrESYaTw1qJtJnkag/zh-cn_image_0000002492343790.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=FEB231BD0D497541E22E1727A1CA388FB10CCFE8F12FDB0BA3CED26BB7470E05 "点击放大")

将鼠标移动到设备投屏上，右键单击后会出现以下功能选项：

在此控件上输入内容并回车：用于搜索场景，输入文本并搜索。

在此控件上仅输入内容：用于搜索和文本框场景，仅输入文本。

重新获取当前页面控件：当页面控件识别不准确，或未识别到预期控件时，重新获取当前界面的控件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/3rjBBys_QEGgnjHA7e7zrA/zh-cn_image_0000002524623433.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=E3A6FC327ACB69BEF19F1281CE023246330E74D26D7B5FE29F80C8F64EAB8010 "点击放大")

（2）从已有图谱事件选择添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/siZFkHMeTEqxCZODv9baEA/zh-cn_image_0000002492343798.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=3B0109C93F0B0A07A8AAAF79C19B40E8C9677360808AEA6078280747E2DDC843 "点击放大")

如下图所示：

①：展示当前页面。

②③：展示对应选框点击前后的页面。

点击“➕”号之后，选择“从已有图谱事件选择添加”，将出现图谱中记录的事件，选择图谱事件创建路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/60ZvilmqT3ihJnWNmdcCYA/zh-cn_image_0000002524503449.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=C3BA7EDBBD3806CA0120030FE0AF54DC8A19B9D40FB7A283AC5AD78307A17A57 "点击放大")

步骤4：调试场景路径。

场景路径创建完成后，支持对其进行调试，验证创建的场景路径能否在设备上运行正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/iTU79pKUSLKbZCT9LOdi8g/zh-cn_image_0000002524623443.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=9AE929DE3F99EFE023D46BB72B69468624949A818C091E897321129110B64DA8 "点击放大")

**编辑场景路径**

选择已有的场景路径，点击鼠标右键或点击窗口右上角的按钮进行编辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/eu1OTO-NTPeD3QsUo-f4vQ/zh-cn_image_0000002492503756.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=07FD2DAB50BF9A2B0F51051A4A3BB5A8B21CC56C5DF30251BF577B20BF56D2B6 "点击放大")

屏幕录制场景路径编辑：支持删除、刷新旧页面和“插入新节点”（注意：需手动将测试设备保持在所需页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5YnsulD0Sn2zflDGQlllwA/zh-cn_image_0000002492503750.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=39BC161E153048BF77A0DD735F5320E764D7E8EED243FA3ED44308580104712C "点击放大")

**场景路径压测**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/boYbQkwsRoWHE-1tK8bDww/zh-cn_image_0000002492503776.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=24B2404017262AB384C877FD0C35EB77B6A9DA730160C987D5E3FC0A42E7F787 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/pXor6rL8SlO0MEjrWseiRg/zh-cn_image_0000002492503724.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=3F990C2C93531529884D53993B16B09ECDABB9700959ECA90086152480395F64 "点击放大")

步骤2：点击选择需要分析的测试任务报告，再点击开始对比即可。

注意

性能测试报告对比只支持场景化性能测试、性能基础质量测试和性能指标监控测试生成的报告。

（2）从性能报告页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“报告对比”按钮，点击后跳转至性能测试报告对比工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/kn7NN4bKTmSMVO47XtsNqA/zh-cn_image_0000002492503722.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=2D0A287580154E242BF46666D4E57BD9ADEA38764D238CC463DE86E026B53062 "点击放大")

步骤2**：**跳转到性能测试报告对比创建任务界面后，会自动选中刚执行完的任务；选择基线报告后，点击开始对比。

**查看对比报告**

性能基础质量测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/CNhIgRI3T6ePvoAb4TMncw/zh-cn_image_0000002492343766.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=1558EFAB2A3C64747BA2A27840F082D96C0ED0ADF7C16C8D7324F39661464C25 "点击放大")

场景化性能测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/rXPz55y5SJe2ehLIFEvqRg/zh-cn_image_0000002492343760.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=14DE8343599C2A24B3F537542A878937679AD84A296677BA7AB496CBEBD03174 "点击放大")

性能指标监控测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/jCFzJg5ISlGN2SCVM4gt-w/zh-cn_image_0000002492503728.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=DA0A1F95C1E47C5798E7FCB3FA9303A2BA6A3B1BD1B12F082E07BC4E37971690 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/sQPQxtx7Riil4ml7zpEm2w/zh-cn_image_0000002492343778.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=527245A4E2037F4777ADFF1DDAD875AB6542739C6BA56244B2A365ECE37B7419 "点击放大")

（2）从性能报告页页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“性能报告自动分析”按钮，点击后跳转至性能报告自动分析工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2gbMj1wOQe6fzk52BPj0QQ/zh-cn_image_0000002492503748.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=0237CFF85CEC5598256A15D37CC7002D3657A9AE9178238AB56A152184F951F2 "点击放大")

步骤2：跳转到性能报告自动分析创建任务界面后，会自动选中跳转前的任务；点击创建任务开始分析。

**报告解读**

**基础信息**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/myFVzjq3RsWzOdp6sBWXvg/zh-cn_image_0000002492343806.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=731204CD258771E2067FAF0346C7330D8B3AAE7608477DB89FA74B178EBE0238 "点击放大")

报告基础信息中主要包括如下部分**：**

* 任务信息：任务名称、开始时间、持续时间、执行人。
* 工程路径：分析的测试任务所在位置。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

**概览**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2Rz1FwA1TSm2r3hxAHg-VA/zh-cn_image_0000002492503734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=6C91D7FC6B35F83767F2401764E590A293CF5156AE61828139C12B8A720E833B "点击放大")

测试服务：分析的任务类型。

测试报告名称：分析的任务名称，点击可跳转至该报告。

支持问题分析数/问题总数：如上文介绍，部分问题不支持分析，因此分析数会存在小于总数的情况。

根因统计：所有分析问题的根因统计列表，由于一个问题可能存在多个根因，因此总数可能大于问题数。

分析结果导出：将所有支持分析的问题步骤打包归类在导出目录下，并生成excel文件存储每个文件对应的分析结论，每个问题步骤会打包成zip文件，每个 zip 文件包含 perfdata，视频和帧图片集。

导出的目录内容结构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nBjApW9DRiSX6kELiGmKeA/zh-cn_image_0000002492503720.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=229555B5B6DDAFC2D498680EDFD53AF2F73E009938863587FBB50FD8D9F351C9 "点击放大")

**分析详情**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dEaPscd_Ri-rgHxFvIuSXg/zh-cn_image_0000002524503501.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=BA05C238A83D43A98280560EB65E558777AD2F7D1A62D3E7BF8F6E18EAA46360 "点击放大")

用例场景：测试用例名称。

操作步骤：测试步骤名称。

指标类型：不达标的问题类型。

根因：导致不达标的主要原因。

指标值：指标具体的测试值。

分析结果：成功表示存在分析结论详情，失败表示该任务未分析出具体结果。

维测数据：点击打开按钮可以跳转到问题步骤对应的资源文件目录。

分析详情：点击展开可以看到对应问题的详细分析结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/IE_niNGYT4moAHi8WchQNA/zh-cn_image_0000002524503483.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=248FF3CA283C7997F5850C5EE692496E098ECF91A20FAD24BA33D689DBDA92A7 "点击放大")

根因归属：导致此问题的主要原因在于应用还是系统。

根因描述：问题产生的原因描述，从上到下根因归类更细。

分析详情：详细的分析结果，如哪段函数耗时异常、节点创建过多等问题。

耗时分段拆解：自顶向下逐步分解性能问题，聚焦真正影响性能的问题。橙色区块代表影响性能的主要原因，需要重点关注；蓝色区块代表耗时拆解的次要原因，对性能问题影响较小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1CZGidyLSaOewYAh85UqCA/zh-cn_image_0000002524503493.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=323962AD48A602433314144B10558E3CFBC60D406370A1CA70A1A4FCC0A59707 "点击放大")
