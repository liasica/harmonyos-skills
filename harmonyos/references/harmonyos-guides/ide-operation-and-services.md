---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-operation-and-services
title: 运维分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 发布应用 > 运维分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4f17ab76a8c38028ac406076b587c92990b386e9a567dfc5d0ed91b850a951a3
---

DevEco Studio支持对已发布上架的应用在使用过程中出现的崩溃、应用冻屏、OOM、资源泄漏等问题进行定位分析，以及查看崩溃、卡顿、丢帧、能耗等异常问题的趋势和分布情况。

## 使用约束

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 页面布局

在DevEco Studio菜单栏点击**View > Tool Windows > Operation Analyzer**，进入运维服务页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/VcgIO9vOQRO8wvfgeYRg9A/zh-cn_image_0000002779407610.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A35C753957C3FFA730AF2AC8DE53514976605A5D35F822C64B584CE48E0114EA)

点击**Add account**按钮，登录华为账号并授权后，可以查看当前账号下应用异常情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/1bC7iFBgTAuPIDaNwSr5Ow/zh-cn_image_0000002808887235.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E30ABF9A8624F7C90CE4308FBF5BB678E7A8F9A1E4E71674A4BE94B66289E71F)

当前页面共分为两个部分。页面左侧为菜单栏，右侧为数据内容展示区：

1. 菜单栏：
   1. 1号区域：可选择当前账号下存在的应用。
   2. 2号区域：Reports区域展示Crash，OOM，APP Freeze，Resource Leak数据详情，用于定位具体问题。
   3. 3号区域：Metrics区域展示Crash，Frame Loss，Launch，Battery Usage异常数据的变化趋势**。**
2. 内容展示区顶部可选择配置项包含：
   1. 时间：通过时间维度过滤当天到最近一个月的异常情况和数据。
   2. 应用版本：当前存在异常数据的应用版本。
   3. 系统版本：当前存在异常数据的系统版本。
   4. 设备类型：展示当前应用支持的设备类型。
   5. 手机型号：当前存在异常数据的手机型号。
   6. 发布类型：当前系统的发布类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/mNF-oyLPSmWJ4tPePjqupw/zh-cn_image_0000002808887239.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F26EDEE1252B91735B748D2ACB060AE3A06AC7340192850690A348281D0543C1)

## Reports

### Crash分析

**26.0.0及以上版本**

展示崩溃详情。Stack Info页签展示崩溃的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。Context Data页签展示崩溃的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示崩溃问题列表。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个崩溃事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看崩溃发生的分布情况，下半部分显示该崩溃事件的可能原因和最佳实践链接。
* 7号区域：展示崩溃事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OHJLMlC6TRqRAzpb2gCENQ/zh-cn_image_0000002779567582.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA14A30058C41903EA1DDA029F188CD68AD0E5306EE49DA9FC30188C23F19CAD)

* **Stack Info**：展示崩溃的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。
  + **Raw Stack**：展示崩溃的原始堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/GX2fTy0dS56ptx6CoJOHAg/zh-cn_image_0000002808767149.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6E7C0F8B3717E793C23A698D5D9608AC7D0CFF99FFA8DDF9F9DC9FF67896623)
  + **Symbolicated Stack**：展示还原后的堆栈信息，堆栈还原需要先关联本地符号表或将符号表上传到云端进行解析，上传后符号表信息会在**Symbol Table**页签中显示。关联本地符号表或上传到云端成功解析还原后，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Z5157OC2SQSGTIXFyP2Xjw/zh-cn_image_0000002808767159.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=72DA133BB28114F93361D37864E5DF4C69FC094DB9634BC57086CC0E991BBDA4)

    堆栈还原后，点击右上角的**Select related project**，关联堆栈对应的工程，即可通过堆栈中的超链接跳转到对应的源码。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/bF7wtiRKRT6m-qjS-5mJtA/zh-cn_image_0000002808767151.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E95011AF51DE90454FB5FB63A99EAE3EAB72D22A2E9774E2D45B39752ABB9094)
* **Context Data**：崩溃的现场数据，展示栈地址空间、寄存器信息、FD信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/XnJBgF8cQ5ySHzPEu_Uwhw/zh-cn_image_0000002808887233.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BF78019C32749913600CE6D6A91BC54C3216682F38DD2D6352BB60CA4724E17)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4Lcym0y0TMaWBIk9I7I7cA/zh-cn_image_0000002779407604.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D9CB5CC7130A2620E29DDE4D46A47509C212F74260C9A58C5896B558594B32A)

**26.0.0以下版本**

展示崩溃详情。Stack页签支持混淆的代码还原，并可跳转到具体的代码行查找问题。System load页签展示崩溃的CPU和内存信息。FaultLog页签展示崩溃的故障日志信息，添加符号表后支持还原日志的堆栈。

* 1号区域：展示崩溃问题列表。
* 2号区域：通过tab切换展示堆栈、系统内存的具体信息、故障日志信息。
* 3号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 4号区域：符号表配置按钮。点击按钮将当前选中的堆栈还原为原始代码，选中带有路径的代码行，然后可以点击最右侧的**Open in project**按钮跳转到应用中问题所在位置。
* 5号区域：展示当前设备信息。
* 6号区域：可以切换不同设备型号及时间段查看崩溃发生的分布情况。
* 7号区域：展示崩溃日志的CPU以及内存信息。该功能从DevEco Studio 5.1.0 Release版本开始支持。
* 8号区域：展示故障日志的所有信息。支持[上传符号表](ide-publish-app.md#section4486164416341)后将现有堆栈信息还原为源码的堆栈。该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/wjhNfGk5Q4mdS93cGAuSOw/zh-cn_image_0000002779567578.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E84A06BE1357C02EA30437DBCAEF16446C1F886CA274EE5C22E68F3420C7EDC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/DfrSGc32Tbe_CjbXeNnApg/zh-cn_image_0000002779407596.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BAEB9A73A6C52605EC676DB61D988ED9E901257D6E4F5A3064503D107BF53AB)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/NAiGtYenQuS2N5mEzPhoRw/zh-cn_image_0000002808767161.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE77A35DB272C39E5AC6598D2484668DD6446F109E0CC2EB2080C75BCB276DBC)

### OOM分析

从26.0.0版本开始新增OOM，展示内存溢出详情。Stack Info页签展示内存溢出的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。Context Data页签展示内存溢出的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示内存泄漏问题列表。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个内存泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看内存溢出发生的分布情况，下半部分显示该内存溢出事件的可能原因。
* 7号区域：展示内存泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/KwZl3799QyW3ljdqSSgwRA/zh-cn_image_0000002779407598.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2E8BC9681CF0D2F4982FAAAB08134F0151A543903CE0067DC9A040783961141)

* **Stack Info**：展示内存泄漏事件的堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。支持堆栈还原，并可跳转到具体的代码行查找问题，具体操作方式请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/t7SRaNP6SCWjTYR0ULUpAQ/zh-cn_image_0000002808767153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=13366A0D50329979DE9AE4371D36E864E7C6DBD234352D9881BCC290E2742DDE)

* **Context Data**：内存溢出的现场数据，展示页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/VFHZUGlSTZ6i7qmi-7qa0w/zh-cn_image_0000002779407608.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=722F14196402A2DD1B68BE4237C36FFF66A7170806E4FBF7EBCF30B4D239B9DB)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/AvFTwQQwSti8KPRKcm2DbQ/zh-cn_image_0000002779567572.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C54D4CCCC32963C406005CC76E7403836F7A6D5826A57C6810A3C91B7E76F055)

### APP Freeze分析

从26.0.0版本开始新增APP Freeze，展示应用冻屏详情。Evidence Chain页签展示应用冻屏的证据链信息，包括3s和6s的主线程堆栈信息。Context Data页签展示应用冻屏的现场数据。Sampled Stack Logs页签展示采样栈的原始和还原堆栈。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示应用冻屏问题列表，支持按功能列表和耗时函数筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个应用冻屏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看应用冻屏发生的分布情况，下半部分显示该应用冻屏事件的可能原因。
* 7号区域：展示应用冻屏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/qS6YtM3dSBeBfgUu2JUqyA/zh-cn_image_0000002779567588.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC667005BA079D7B43AC8846E97052248DCB0E91FE7D29C4AD0B1AF810CD671C)

不同的冻屏类型对应的详情页存在差异，此处以THREAD\_BLOCK\_6S为例。

* **Evidence Chain**：展示该应用冻屏事件的证据链信息，包括3s和6s的主线程堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uEeaNrVfTC-HOsL3oaO_2w/zh-cn_image_0000002808887247.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=20D0927DC2927BAD3E3BDDD4FFB1E4539E94AFF9D0EE011B91B923310BB041DE)
* **Context Data**：展示该应用冻屏事件的现场数据信息，包括堆栈信息（原始堆栈和还原堆栈，堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）、CPU信息、内存信息、热档位信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/j4D7ClJKRfiPeLCTIM3QiQ/zh-cn_image_0000002779407600.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA502DB8B4395C2B940651FDC3AAE9E7C32CB0F5E468E3A426D1CAED6B5C64F7)
* **Sampled Stack Logs**：展示该应用冻屏事件的采样栈日志信息，包括原始堆栈和还原堆栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/kuRANuOWSdCbWugwK-LDyg/zh-cn_image_0000002808887245.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7ABDD01A513AA8CE590D2F26689446DBBE7153568D1BF7EF69D76B1B2294C8A1)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/4oTBiqj8RYC51VUwJPQXTQ/zh-cn_image_0000002779407602.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A4A10CCA7F593404CEE509BE8E5C24F7F47C02C670877371C366BBCAD873557)

### Resource Leak分析

从26.0.0版本开始新增Resource Leak，展示资源泄漏详情。Evidence Chain页签展示资源泄漏的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。Context Data页签展示资源泄漏的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示资源泄漏问题列表，支持按Top问题和ArkTS泄漏对象聚合筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、灰度任务id、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过灰度任务id搜索具体的某个资源泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看资源泄漏发生的分布情况，下半部分显示该资源泄漏事件的可能原因。
* 7号区域：展示资源泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/a2QKsdDoSziLa72E8-BMHg/zh-cn_image_0000002779567576.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=23579D5262A5525F7728F5CDDC274F6B5BAABDEC108A21856D60C77594CCD58B)

不同的泄漏类型对应的详情页存在差异，此处以RSS\_LEAK为例。

* **Evidence Chain**：展示该资源泄漏事件的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。每个泄漏方法下会显示堆栈分配详情、堆栈树分配、火焰树、原始/还原堆栈。

  堆栈分配详情：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZvmeD0yoRQGey-ZwK2RgiA/zh-cn_image_0000002808767145.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5C9EC45E56731FEDF13AF1BDA832A0B1EB11988C4E9FD5B6C48366E5260C50C)

  堆栈树分配：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Uf_ku35MRxev5aGd_hFRdg/zh-cn_image_0000002779567586.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7183B19D2B8E8DB820C96F8DD31B0F5859483917EC0773854C76D92E2FFDF0A)

  火焰树：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/65nF3Y2sTGqwyXvREsU4iA/zh-cn_image_0000002808887237.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D3967618D2EF92AC700EF137268D7570D948D07A3E767B003BCAA5DA069A3D8)

  原始/还原堆栈（堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/9tcBqY8BSOywVyIe2NIaOw/zh-cn_image_0000002808887243.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA88652457D177B6EB92235E8CF580B4BFE9700861B7888CE37B9804DB1749C1)
* **Context Data**：展示该资源泄漏事件的现场数据信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/mb_jxsEdSOWCbFNtcdHrHg/zh-cn_image_0000002779567584.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DE4C85AB6AC22927B20D077DF17B5B8DFCEA6624875F0BC69B56AB1ACB1D6FF)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/baEOU8FeQqK8KQlox88gHg/zh-cn_image_0000002808887241.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=04DC678A8EA96C0F7F51BC3F3956E6419E858F9BA9BAD8F905AE619E59777E1B)

## Metrics

### Crash分析

展示应用崩溃次数和崩溃率情况。

1号区域：通过tab页签可切换All，JsError（JavaScript崩溃错误），CppCrash（C++崩溃错误），OOM（内存导致的崩溃），ProcessKill（系统被强制终止），查看不同维度的崩溃次数、崩溃率进行分析。

2号区域：通过柱状图展示不同维度在所有的崩溃异常中的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/n9YYMf8nSt6N_rbnxyilWw/zh-cn_image_0000002808767155.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FA46A75A9C4E1A55CA37BBF45FF23BADC22A46D6811C40990BA520CF9482ABB)

**说明** 

ProcessKill将通过柱状图和饼图联动，点击柱状图，通过饼图展示具体某个时间段的ProcessKill的类型分布。

### Frame Loss分析

对连续丢帧情况进行多维度统计，便于快速定位问题所在位置。

1号区域：丢帧总览是统计最大维度的连续丢帧率。

* <6：连续低于6帧的丢帧率。
* 6-15：连续大于6帧，小于15帧的丢帧率。
* >15：连续大于15帧的连续丢帧率。

2号区域：按照Page，Scenes两个维度展示丢帧异常率TOP N的页面或者场景。点击饼图上的某个区域，将展示具体页面或者场景的连续丢帧率情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/rhjHX5EpRPaCMOG6u_Hb1g/zh-cn_image_0000002779567580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C10A24B53855BDCEB63DD86DF9175B544371E6EEEA40FBDF4251D2FD8BE5CB2)

### Launch分析

统计设备启动在不同维度的情况，帮助分析异常问题的分布情况。

1号区域：通过页签可切换查看启动整体耗时（All）、冷启动（Cold Launch）耗时、热启动（Hot Launch）耗时。

2号区域：通过折线图形式展示整体耗时趋势。以下图为例：

* AVG表示当前时间节点下各启动阶段的平均耗时。
* P50表示当前时间节点下，50%的启动阶段耗时低于纵坐标显示的579ms。
* P75表示当前时间节点下，75%的启动阶段耗时低于纵坐标显示的582ms。
* P90表示当前时间节点下，90%的启动阶段耗时低于纵坐标显示的585ms。
* P99表示当前时间节点下，99%的启动阶段耗时低于纵坐标显示的585ms。

柱状图展示耗时异常的上报量（Reported Quantity）。

3号区域：展示各启动阶段的耗时，通过点击阶段名可查看各时间段具体耗时情况。

4号区域：展示启动当前阶段在不同时间段的耗时趋势。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/X_mc5oU0R72Y-800vlv0Xg/zh-cn_image_0000002808767157.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C1CE4A383B3A1CE8C92EF715A6115BEBA21A535281622E05F743076950F529E)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qhC7X-9aRKuG41J5BBtQ2Q/zh-cn_image_0000002779407606.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=85E4BE0CF6D9E730EFA9C7F5B4141578A14752E058CC12CA9A80933B3D3CE9F8)

### Battery Usage分析

用于统计设备的总能耗以及前后台的能耗和耗电时长。

1号区域：能耗概览。通过折线图展示总能耗，前台能耗，后台能耗。

2号区域：展示前台能耗和耗电时长随Top 5设备器件分布情况。

3号区域：展示后台能耗和耗电时长随Top 5设备器件分布情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/mYvlGgGyRAO6NPxgeC2xQg/zh-cn_image_0000002779567570.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=594D621B08352682EF6BC1DC484C7810BEB20D2C5FDC759BE8B638DC59D5D302)
