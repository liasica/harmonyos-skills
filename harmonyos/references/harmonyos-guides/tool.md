---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool
title: 实用工具
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 实用工具
category: harmonyos-guides
scraped_at: 2026-11-25T11:28:44+08:00
doc_updated_at: 2026-11-25
content_hash: sha256:3cd863e98871eba48136641413a2ddd48622e7458e21c7dcd785bef51e5ab3f8
---

## 应用图谱管理工具

**应用图谱管理工具：**支持从探索测试执行报告导入和创建空白图谱等多种方式创建图谱，支持通过屏幕录制和从图谱选择方式创建场景，支持对场景路径进行调试对比。

### 应用图谱特性管理

打开DevEco Testing客户端，在左侧菜单栏选择“实用工具”，点击“应用图谱管理工具”卡片进入工具界面。

**创建图谱**

点击“创建图谱”，有以下选项：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/yF2drCXDTOis_gUIoMvQ6A/zh-cn_image_0000002663932239.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=29F39F0BD6B8BC7521434446A3E674009A0B1E5358875FDE5113CDF0518DD2E7 "点击放大")

探索测试报告：选择相应的探索测试任务，输入待创建的图谱名称和说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/txvWhX-rSHu9qpg0zwvpKw/zh-cn_image_0000002663932223.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E0E0D5F240CE9C5ACF1338A143344C0285BD9C74208C97DBBF50F42B47AD567 "点击放大")

从现有图谱文件：复用已有的图谱文件。

在用户的DevEco Testing数据路径（DevEco Testing客户端->设置中可查看数据路径）中找到“graphTool”文件夹，找到相应图谱文件夹后；将其中所有打包成zip文件。

**注意** 

打包后zip文件，需要打开后直接是图谱文件，不能多一层目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/B0ADZMhVSouAVC5bIMQRCw/zh-cn_image_0000002664012325.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=17DFC5A4AC90A54A752D84D12FA75DF324DCF1F6AD410CBCAFD42524E75B87E2 "点击放大")

空白图谱：选择对应的应用创建空白图谱。

图谱名：图谱名称。

图谱说明：增加图谱说明。

设备列表：选择连接的设备。

应用包名：选择设备已安装的应用。

应用描述：对应用增加描述。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/AH5_bMHVTfSl4PczvSGNaQ/zh-cn_image_0000002664012319.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=8340AC99301DA111DCFA9775ABB09E8091D35D8AF03B54BD36F488FE6749E1B3 "点击放大")

**说明** 

在客户端设置->基本设置页面的数据路径下，“graphTool”文件夹存放所有图谱数据。

**特性管理**

新增特性：点击新增特性按钮，输入特性名称和特性描述（非必填），点击提交按钮新增特性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BqhchiRXRy6B8a7jvMOihg/zh-cn_image_0000002645251092.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=42D1565831F85B35D855045E7B07EDEFC94C4948277246766096E1E8BF00030D "点击放大")

删除特性：勾选特性后，点击删除特性按钮，勾选待删除特性，出现删除确认框，点击确定按钮完成删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ECoM-79dSDKE5ibSnuQjKA/zh-cn_image_0000002645251734.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B8C652452410B64B9F98B9D0C029E7421E40EAF876A339E6222B38687954CAC "点击放大")

编辑特性：鼠标右键点击特性名称，选择修改特性按钮，修改特性名称、特性描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/dGQliJoxSfWih3NYG7R0kw/zh-cn_image_0000002633693092.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=4254075F5A78ECA0204AB2E88F4CB599EF678C6B9CD1FBCFA6F34675FDF1F2C3 "点击放大")

### 应用图谱工具场景路径管理

**新建场景路径**

步骤1：选择已有特性，点击新建场景路径按钮或鼠标右键选择新建场景路径，进入场景路径编辑页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/k8aE2SSHSDWpAz7fDEWN9g/zh-cn_image_0000002645224958.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0C889940A34516435BBFCC2CEB99E26B517D66552C1B8ACBB8FFF77FC4627D7)

步骤2：“编辑模式”窗口中的首个页面为设备桌面截图。点击窗口中的“➕”号创建场景路径，支持“通过屏幕录制添加”和“从已有图谱事件选择添加”两种方式。

步骤3：添加场景路径。

（1）通过屏幕录制添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uMbsgBciRzmkEE6RSBp_Ww/zh-cn_image_0000002675384643.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BB23D326C41921A46C62383C57D4F46E77FDD06F220678FCE35DAE334CDB91A "点击放大")

在点击“➕”号之后，选择“通过屏幕录制添加”。

通过在左侧投屏设备的区域内，执行点击、滑动或者右键弹窗输入文本动作，添加相应的场景步骤，点击保存按钮完成场景创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/w2ebGSDHQPe0l9M8opRpAQ/zh-cn_image_0000002645380782.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=8782CB52FEC8C1C039C8F2AF2A75841B872B5D9987E641C7E750F0F750F2D1F2 "点击放大")

将鼠标移动到设备投屏上，右键单击后会出现以下功能选项：

在此控件上输入内容并回车：用于搜索场景，输入文本并搜索。

在此控件上仅输入内容：用于搜索和文本框场景，仅输入文本。

重新获取当前页面控件：当页面控件识别不准确，或未识别到预期控件时，重新获取当前界面的控件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Idlbyn00TRWezcetc-HWkg/zh-cn_image_0000002645220930.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=B225D4F58EE8A7E7A823EA2F5DFD33456643606984B29D5A4BDEAE8B542F6F5A "点击放大")

（2）从已有图谱事件选择添加

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xDt1gMPlRZWT6j3DMZyrZA/zh-cn_image_0000002675260835.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FD4D561A46A66D0BE1F464719A329F1852FDAA17AC1C2D9032E5E82BF86966E "点击放大")

如下图所示：展示对应选框点击前后的页面。

点击“➕”号之后，选择“从已有图谱事件选择添加”，将出现图谱中记录的事件，选择图谱事件创建路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/sYmXQDPSQLmtPcKevwylzg/zh-cn_image_0000002645381166.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC8457550692AE7E422C840D17B4962D5325CBA8803DF16746F9D5A2CDF46FA3 "点击放大")

步骤4：调试场景路径。

场景路径创建完成后，支持对其进行调试，验证创建的场景路径能否在设备上运行正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ncSv2qY-QySb6fuX3WGh2w/zh-cn_image_0000002675381513.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=21F1418AAE072E30A6ED31FD41F44DC30FB33EA407BE18AB0CFD2E1412B643A6 "点击放大")

**编辑场景路径**

选择已有的场景路径，点击鼠标右键或点击窗口右上角的按钮进行编辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/GYV3GoWAQ6yJ1tBv-udHLA/zh-cn_image_0000002675261781.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE8881FCE1D7B760B754CFFA304F1D05BE792418AC8139C2BBC385756050C563 "点击放大")

屏幕录制场景路径编辑：支持删除、刷新旧页面和“插入新节点”（注意：需手动将测试设备保持在所需页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/YdjsiBOtTpWT9WIMRBBI5g/zh-cn_image_0000002675263185.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A858C2D463712935F08B6B222504B259821BE5D867E1973B1115A381C149349 "点击放大")

**场景路径压测**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/0bVNDTcZT42jAKMlvmopBg/zh-cn_image_0000002633693094.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6F6B525926E01A627F57430EAF145CB08E6D2AAC3CB252D77F594000765B24A "点击放大")

探索测试服务创建场景压测任务**：**

选择测试服务：打开DevEco Testing客户端，在左侧菜单栏选择“测试服务”，点击“探索测试”卡片，进入探索测试服务创建页面。

选择应用：选择应用图谱对应的应用。

选择图谱测试的路径：选择所需的测试时长、模式类型等配置信息。

模式类型：场景压测模式会出现场景选择选项。

图谱选择：选择编辑的图谱。

场景选择：选择已创建的场景路径。

创建任务：点击创建任务按钮，探索测试将在设定时间里循环对该路径进行压测。

### 应用图谱工具黑名单控件管理

新建控件黑名单

步骤1：选择已有特性，点击新建控件黑名单或鼠标右键选择新控件黑名单，进入黑名单控件编辑页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/8jIoaQ3KRjOwmMNKZVIKUg/zh-cn_image_0000002675267229.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=E44D59F4F61B11844D909D03227A970901D6C64EE5A85D70518A107D9776219F "点击放大")

步骤2：进入编辑窗口后根据右边灰色字体提示右击屏幕上的控件选择添加关键字和XPath；现提供关键字以及XPath两种方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/cpjO9MojTrSnYcAYtXeZbA/zh-cn_image_0000002645387578.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=80937AC46225338D17368305955619BB28E593240B7428FD84A081DC6EC44371 "点击放大")

步骤3：将鼠标移动到设备投屏上，右键单击后会出现以下功能选项：

添加控件XPath黑名单：用于添加控件的XPath作为黑名单。

添加控件关键字黑名单：用于添加控件的text属性值作为黑名单。

重新获取当前页面控件：当页面控件识别不准确，或未识别到预期控件时，重新获取当前界面的控件。

步骤4：添加黑名单控件。

（1）关键字

选择关键字控件后，会展示所选控件text属性值以及图片，点击图片可查看所选控件在整个屏幕中的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/TN-MOv6UQA2LpKQLNTdu-g/zh-cn_image_0000002675388793.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=74FF4C6A235FAA0F1D13486E720F00240FC72381F61EC78FD61FB3E578EB909E "点击放大")

（2）XPath

选择XPath控件后，会展示所选控件的XPath路径以及图片，点击图片可查看所选控件在整个屏幕中的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/KQUsk_i8QVKzQRTKiv30Wg/zh-cn_image_0000002675393627.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA4C423367895CB12A2E54639DADC6885512A5B035922227E571261F93051268 "点击放大")

步骤5：选择控件黑名单后点击保存即可保存控件黑名单。

步骤6：查看所选黑名单信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/l9tTnKg0ScSXzimpW54AqA/zh-cn_image_0000002645393570.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=E61DEAF2F9865C63DBECC3A118C01AFCE3E40E990B953D3A70325155BC9041B4 "点击放大")

保存黑名单后展示了所选关键字以及XPath控件黑名单信息。点击图片放大可查看对应控件在整个屏幕中的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0z4Q34LRSrmXGW5y8n9DxA/zh-cn_image_0000002645235614.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=5548E90E9154C69186CA233BC07DAA76FB4C1870007C927CCC739F10E0255DAC "点击放大")

**编辑控件黑名单**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/okBp-urqRVKu3BYDrIS0eA/zh-cn_image_0000002645235976.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C08DD7C4F00E1713F10CD1028F55EB26625293C68994DDF5FC8C8408A71B4B9 "点击放大")

选择已有的黑名单，点击鼠标右键或点击窗口右上角的按钮进行编辑。

## 性能测试报告对比

**性能测试报告对比：**提供同类性能测试服务的报告对比分析，涵盖场景化性能测试、性能基础质量测试及性能指标监控测试三大服务。

**选择测试报告**

按需选择同类性能测试服务报告对比分析，支持按任务名、备注信息或任务状态筛选。点击开始对比，即可一键生成对比报告。

性能测试报告对比有两个任务创建通道。

（1）从实用工具创建任务

步骤1：进入工具任务创建页面。

点击导航栏的实用工具，点击“性能测试报告对比”进入任务创建页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/fPRof-lVRLCH3Hqi7bJuCg/zh-cn_image_0000002663932269.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EAA64E5DD54A1FDB8D50C9E3A6056827E12CD758DD172D14590A49605878079 "点击放大")

步骤2：点击选择需要分析的测试任务报告，再点击开始对比即可。

**注意** 

性能测试报告对比只支持场景化性能测试、性能基础质量测试和性能指标监控测试生成的报告。

（2）从性能报告页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“报告对比”按钮，点击后跳转至性能测试报告对比工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/3s1P1ypcTyW36gmchcGBXQ/zh-cn_image_0000002663932219.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=E75B815F700D5C712A9FB0D858319B08FB5803627175841344FCA7E450FB6A1A "点击放大")

步骤2**：**跳转到性能测试报告对比创建任务界面后，会自动选中刚执行完的任务；选择基线报告后，点击开始对比。

**查看对比报告**

性能基础质量测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/9-RopF9TS2quLLIyIwozQA/zh-cn_image_0000002663932231.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D8692C0A80CDE56E55B572C1AE83C70F0567CC8883AB3337D48B44CFED9052C "点击放大")

场景化性能测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/rRPJOaHBT9WxSZIQ-MNelA/zh-cn_image_0000002633693098.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C4B939781F14079DCE9DA0A09F2004EF14D76DFC8168595F828C41442791B02 "点击放大")

性能指标监控测试报告对比样例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/WWG5jqqUQjmY99QapMLHAQ/zh-cn_image_0000002664012299.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB9A19B243B4E6BB3E14FCA4868448149F872ABC3F12B9B1CCB5DEDE8668B52 "点击放大")

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

**注意** 

性能报告自动分析只支持场景化性能测试服务和性能基础质量测试服务生成的报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ukx22J_kRbSUQNyC4TaixA/zh-cn_image_0000002633533154.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=49ABBC5799B0BC28E69C012C3FBE057AC7B83165732D56088051EF7F095413A3 "点击放大")

（2）从性能报告页页面创建任务

步骤1：在场景化性能测试和性能基础质量测试执行分析结束后，以性能基础质量测试为例，报告页面上会有“性能报告自动分析”按钮，点击后跳转至性能报告自动分析工具。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/lfW0VA3EThi0blubWf9HEA/zh-cn_image_0000002633533162.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=29745F88EE706D3CFB5D35A18700D45B3475F6DC6EC051E529EA75BEAA5BDB30 "点击放大")

步骤2：跳转到性能报告自动分析创建任务界面后，会自动选中跳转前的任务；点击创建任务开始分析。

**报告解读**

**基础信息**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/thI1aK1CRrGX34kLVfQXpw/zh-cn_image_0000002663932263.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A8B504BF06C5A7602A212F622E3CDDB8B127A2E1F3BEF13202AA2787AFA7D09 "点击放大")

报告基础信息中主要包括如下部分**：**

* 任务信息：任务名称、开始时间、持续时间、执行人。
* 工程路径：分析的测试任务所在位置。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

**概览**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZEyGvc9mSW6PNuobB_0O9A/zh-cn_image_0000002664012317.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=8863C5FFB826F015D6903F10C72281BCA6AD9F88B460FDCBDC0349DAFF350D3D "点击放大")

测试服务：分析的任务类型。

测试报告名称：分析的任务名称，点击可跳转至该报告。

支持问题分析数/问题总数：如上文介绍，部分问题不支持分析，因此分析数会存在小于总数的情况。

根因统计：所有分析问题的根因统计列表，由于一个问题可能存在多个根因，因此总数可能大于问题数。

分析结果导出：将所有支持分析的问题步骤打包归类在导出目录下，并生成excel文件存储每个文件对应的分析结论，每个问题步骤会打包成zip文件，每个 zip 文件包含 perfdata，视频和帧图片集。

导出的目录内容结构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/_rp7iWNsQu6ERIlb8cEhUw/zh-cn_image_0000002633533178.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=A14AE02F94C0C9D0AACF82B0F7571FC41DDC341E690346C505302F73AD1CE4ED "点击放大")

**分析详情**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/DDlzuBGQQ9iqo1HIx1ryuA/zh-cn_image_0000002633693062.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=6861290E4017BF7371EB0F8106EAF77CDD33162B511486F70FE873041E3E2146 "点击放大")

用例场景：测试用例名称。

操作步骤：测试步骤名称。

指标类型：不达标的问题类型。

根因：导致不达标的主要原因。

指标值：指标具体的测试值。

分析结果：成功表示存在分析结论详情，失败表示该任务未分析出具体结果。

维测数据：点击打开按钮可以跳转到问题步骤对应的资源文件目录。

分析详情：点击展开可以看到对应问题的详细分析结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/VMuAlkb6T_eXL_ipI251og/zh-cn_image_0000002664012323.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=955D24C337E1F0AD4707D9793435411E6F2907BB2CA3EC870CFDD2B60552F8A9 "点击放大")

根因归属：导致此问题的主要原因在于应用还是系统。

根因描述：问题产生的原因描述，从上到下根因归类更细。

分析详情：详细的分析结果，如哪段函数耗时异常、节点创建过多等问题。

耗时分段拆解：自顶向下逐步分解性能问题，聚焦真正影响性能的问题。橙色区块代表影响性能的主要原因，需要重点关注；蓝色区块代表耗时拆解的次要原因，对性能问题影响较小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/b6tahESeTrazM0KQR8G3JA/zh-cn_image_0000002633693090.png?HW-CC-KV=V1&HW-CC-Date=20261125T032843Z&HW-CC-Expire=31536000000&HW-CC-Sign=57B74563CD29F8E50CDEFD7491B78F3D9F2C1D085B79F3E8FA0113FBEFEE77CC "点击放大")
