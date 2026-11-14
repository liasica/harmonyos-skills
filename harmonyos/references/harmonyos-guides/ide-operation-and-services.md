---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-operation-and-services
title: 运维分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 发布应用 > 运维分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:73b3de1baeb9eefa3535c1687b5f59ee08babd176c9027b245c31a83c2f097eb
---

DevEco Studio支持对已发布上架的应用在使用过程中出现的崩溃、应用冻屏、OOM、资源泄漏等问题进行定位分析，以及查看崩溃、卡顿、丢帧、能耗等异常问题的趋势和分布情况。

## 使用约束

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 页面布局

在DevEco Studio菜单栏点击**View > Tool Windows > Operation Analyzer**，进入运维服务页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/VJdk42SmRsCUFVzBc3k8OA/zh-cn_image_0000002779407610.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=E135A9D4EEA09D888407DF2FAC203C2ADD9A797D0DF8EF97AB191B8AE7CEF46F)

点击**Add account**按钮，登录华为账号并授权后，可以查看当前账号下应用异常情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/u446Ci-qS-SO2ckoiOIVEA/zh-cn_image_0000002808887235.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F9CDC8CB7D776C9206D05F2162E4E72DC45D6329CF2B7BF7272D36329E377F3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JwdvA_04TeCLQ-Nr6lmFpA/zh-cn_image_0000002808887239.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=53567751FB1EC209944FEFF549F3014C7E31D5AC5FC46FC8AB4C1B3FF8F8EF46)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/58OlcIxMSC2Lu4abtZCLrA/zh-cn_image_0000002779567582.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDFFB0751490EDE088A149CACB277BFC3852422743F6C34792DF409048AD94E3)

* **Stack Info**：展示崩溃的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。
  + **Raw Stack**：展示崩溃的原始堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/2kDCQbLcRTubEOEoHMGhRA/zh-cn_image_0000002808767149.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2C13F81D9AD8934214E14DE69C7DB90B4988CD9FCE28986277DAC49EFAB0B51)
  + **Symbolicated Stack**：展示还原后的堆栈信息，堆栈还原需要先关联本地符号表或将符号表上传到云端进行解析，上传后符号表信息会在**Symbol Table**页签中显示。关联本地符号表或上传到云端成功解析还原后，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/AgYta2RNTiuh9KKwKCr1_A/zh-cn_image_0000002808767159.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D7C7E797C08CB3AC4F72C55D9D47D60C18670376A7EE499BF1F9EA5648D8111)

    堆栈还原后，点击右上角的**Select related project**，关联堆栈对应的工程，即可通过堆栈中的超链接跳转到对应的源码。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/THhBn6b4TrmHsAhhYpn7wA/zh-cn_image_0000002808767151.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=B17D45295B630E62C535AE5F924ACC500CA4D9B40CCF29E390198B8565F7AF27)
* **Context Data**：崩溃的现场数据，展示栈地址空间、寄存器信息、FD信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/mYjVfN8FSJCNtTyWEtmVPQ/zh-cn_image_0000002808887233.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=A09A8B478FBC39D0B0A973DAD752C64C7664F49F56645BCD7C0F139810CD1191)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/0PLlnCVtRw2WI-KnEb2HiA/zh-cn_image_0000002779407604.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=46CEB54AB9A73D9C610C04DF6D0E37F3E4ED791C87DF08DB3C0D49B1539DF1FC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/vFqhdl1mS5CVYl8dPQzFAw/zh-cn_image_0000002779567578.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=45F9B05DC28F360FC2B41410A1992DD772777C4ECB16327B8F7A49CD75856454)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/dTOjEWZDSVCFvnV6tDREAA/zh-cn_image_0000002779407596.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCE2B27B8319F39CEFC157E214642C0467430F640EA01CE8706D958BB3348398)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/MKAMkjzkThmG9lBm4RnYgA/zh-cn_image_0000002808767161.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=D367556CB57E745283788D273873E987833751E6CB9633F84D6728FEFFD58ECE)

### OOM分析

从26.0.0版本开始新增OOM，展示内存溢出详情。Stack Info页签展示内存溢出的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。Context Data页签展示内存溢出的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示内存泄漏问题列表。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个内存泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看内存溢出发生的分布情况，下半部分显示该内存溢出事件的可能原因。
* 7号区域：展示内存泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/3n_tkX4qRXOeyZkFVxOUyw/zh-cn_image_0000002779407598.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=26D3C870586C19FDA198E09C445B163237B58B8FEBDA47B1E2BB7B4519656758)

* **Stack Info**：展示内存泄漏事件的堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。支持堆栈还原，并可跳转到具体的代码行查找问题，具体操作方式请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ldlKTooaTVKlO28evMAagg/zh-cn_image_0000002808767153.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3652BA66A5CA3045BE4DBC3A8E803DDC05DFC493B5C69FB6E252183F8111DB5)

* **Context Data**：内存溢出的现场数据，展示页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/WRy8LVEoTLyffvn5871OrA/zh-cn_image_0000002779407608.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=53DD6742CB6646A544B1D29EC3EEA9518A333F6D4CE19292FB54EB3BC9E0E06F)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/KsTkE1BUR1GrilcVv-dFqw/zh-cn_image_0000002779567572.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A11A2EE0061694BD32BC98BCA7D210EEB659253FA3BA2A6D73D28F5EB2A9FB9)

### APP Freeze分析

从26.0.0版本开始新增APP Freeze，展示应用冻屏详情。Evidence Chain页签展示应用冻屏的证据链信息，包括3s和6s的主线程堆栈信息。Context Data页签展示应用冻屏的现场数据。Sampled Stack Logs页签展示采样栈的原始和还原堆栈。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示应用冻屏问题列表，支持按功能列表和耗时函数筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个应用冻屏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看应用冻屏发生的分布情况，下半部分显示该应用冻屏事件的可能原因。
* 7号区域：展示应用冻屏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/RKOlBmqSRP6hKQpWEEAqpg/zh-cn_image_0000002779567588.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAD16591C591974484FACE73EA60186A386CB77020CAA6088BCCE7611AB7188C)

不同的冻屏类型对应的详情页存在差异，此处以THREAD\_BLOCK\_6S为例。

* **Evidence Chain**：展示该应用冻屏事件的证据链信息，包括3s和6s的主线程堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/bK9dDWRdQQKg664OWmMn3A/zh-cn_image_0000002808887247.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C95BB415A85566076B7DC00278DC79156CA79A2A31C3D1C9CBAC237FA1997BE)
* **Context Data**：展示该应用冻屏事件的现场数据信息，包括堆栈信息（原始堆栈和还原堆栈，堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）、CPU信息、内存信息、热档位信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/KGvGg8yIQomAoK7JnXcEkw/zh-cn_image_0000002779407600.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C4C3F19CBE44FFCF604A76A122672638C6BA79EFB7A7854198FA4BBA0209C24)
* **Sampled Stack Logs**：展示该应用冻屏事件的采样栈日志信息，包括原始堆栈和还原堆栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/U--zDbOsT4a9DbA8bsa74w/zh-cn_image_0000002808887245.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2D66FD3D131E5F3F238F30AFDCD1D12BCCCFC50D3955867FA5DF7630CE87186)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7hLCiEEbTVagquZTo2NboA/zh-cn_image_0000002779407602.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=43470A4144DF67A8E2A54E32546419386FAADDB82BF178E37564D6FDB43C2D0D)

### Resource Leak分析

从26.0.0版本开始新增Resource Leak，展示资源泄漏详情。Evidence Chain页签展示资源泄漏的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。Context Data页签展示资源泄漏的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示资源泄漏问题列表，支持按Top问题和ArkTS泄漏对象聚合筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、灰度任务id、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过灰度任务id搜索具体的某个资源泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看资源泄漏发生的分布情况，下半部分显示该资源泄漏事件的可能原因。
* 7号区域：展示资源泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/rqNFVGziSbqU-o-8oQXOLQ/zh-cn_image_0000002779567576.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=F93796FA87C9C0A744BC121891DE0D07B6415587471A9F2A4062BEC14D737BCC)

不同的泄漏类型对应的详情页存在差异，此处以RSS\_LEAK为例。

* **Evidence Chain**：展示该资源泄漏事件的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。每个泄漏方法下会显示堆栈分配详情、堆栈树分配、火焰树、原始/还原堆栈。

  堆栈分配详情：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Rv1AQOLJR8O8OByEdOCmJg/zh-cn_image_0000002808767145.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CA0366C663F21070BBA1928D5F5240C086D4B77F4D7BDF26DBECD2A23C3BB8D)

  堆栈树分配：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/5PZNP_SlRzur1Hy4Re26AQ/zh-cn_image_0000002779567586.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2FA06BCB56F85C3BBE4F3A78E7B894E0E3CA87C8C5445FDF5AD5D09582596A6)

  火焰树：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/-D-afsmMS0eJP6Z6IORPIQ/zh-cn_image_0000002808887237.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E65B0FC7AFDE0404F944A94D91EE2466A9B80BB6989D2BBBDB62DF70DA8F837)

  原始/还原堆栈（堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/gCTn8MVsRRi5MttLYty2NQ/zh-cn_image_0000002808887243.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5DD86961B17CA201E177696102FAD9A3DE25AE8A8D64DFEFDC9A3A95EEFCF8D)
* **Context Data**：展示该资源泄漏事件的现场数据信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/X80TUBBCR3e4uNDGb1HYVQ/zh-cn_image_0000002779567584.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=D90258BA5A8909C8F04CB5028B10CCB5BB1ABBAADF3F24BF53E1FFFA56C67170)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/3tP_zIkUTGSFQdVooNZKqA/zh-cn_image_0000002808887241.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=156183B997F6734E4302D9DE6499AA828B853460975D54F0AC2D5B114AAC7E49)

## Metrics

### Crash分析

展示应用崩溃次数和崩溃率情况。

1号区域：通过tab页签可切换All，JsError（JavaScript崩溃错误），CppCrash（C++崩溃错误），OOM（内存导致的崩溃），ProcessKill（系统被强制终止），查看不同维度的崩溃次数、崩溃率进行分析。

2号区域：通过柱状图展示不同维度在所有的崩溃异常中的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ocTOUocgRpyW5Krc_dK50g/zh-cn_image_0000002808767155.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6CD5FF627ACF585F2B377B97D3073095950E0BCE17FF223C95851738612584B)

**说明** 

ProcessKill将通过柱状图和饼图联动，点击柱状图，通过饼图展示具体某个时间段的ProcessKill的类型分布。

### Frame Loss分析

对连续丢帧情况进行多维度统计，便于快速定位问题所在位置。

1号区域：丢帧总览是统计最大维度的连续丢帧率。

* <6：连续低于6帧的丢帧率。
* 6-15：连续大于6帧，小于15帧的丢帧率。
* >15：连续大于15帧的连续丢帧率。

2号区域：按照Page，Scenes两个维度展示丢帧异常率TOP N的页面或者场景。点击饼图上的某个区域，将展示具体页面或者场景的连续丢帧率情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/PzBam5wkTS6fT5YVupfRqQ/zh-cn_image_0000002779567580.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=6396D294C7CD0668513AF6E7C86E194C94CF2E5203B48797A7E37D6CF4B5AFE4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/FMabu4pTRtun5kyvzcia1w/zh-cn_image_0000002808767157.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8BEF2747EB79C1122BA403ACCDBBD50FDD968F50EAC79705C39F68481723237)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ZjKqqX4XQF-TGMnKjp_f3A/zh-cn_image_0000002779407606.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F70496FAB91B8CE78CA04CB2C344120EAC33785298ED3123D288D0B23567C2B)

### Battery Usage分析

用于统计设备的总能耗以及前后台的能耗和耗电时长。

1号区域：能耗概览。通过折线图展示总能耗，前台能耗，后台能耗。

2号区域：展示前台能耗和耗电时长随Top 5设备器件分布情况。

3号区域：展示后台能耗和耗电时长随Top 5设备器件分布情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/9z_Nhq60R7KDWHhZMSgrkw/zh-cn_image_0000002779567570.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF44FA602C5523F3C2F845A858FAD1B92EEBFD6EF815B00817D9A475CF6C1479)
