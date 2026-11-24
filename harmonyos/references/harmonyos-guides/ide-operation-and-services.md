---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-operation-and-services
title: 运维分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 发布应用 > 运维分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4fc7ded2a763fc877735d88718fe794816c847c30c55682d26a833906b9840ef
---

DevEco Studio支持对已发布上架的应用在使用过程中出现的崩溃、应用冻屏、OOM、资源泄漏等问题进行定位分析，以及查看崩溃、卡顿、丢帧、能耗等异常问题的趋势和分布情况。

## 使用约束

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 页面布局

在DevEco Studio菜单栏点击**View > Tool Windows > Operation Analyzer**，进入运维服务页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/cB14KMs2Q0S1xjgua1KSog/zh-cn_image_0000002779407610.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D20E285DBFB52BFBFAF4AF9CB9186C16C3287E2A20770C9E948DF1E67D34C28)

点击**Add account**按钮，登录华为账号并授权后，可以查看当前账号下应用异常情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/XUqSKU9tTFe5UFDMeEMLVQ/zh-cn_image_0000002808887235.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F4E4F9210654FDEE647A1D557867ED0A602492607D07AE61140579746E3CEB4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/bP3WA_6NTAW3A7gYwC9M2g/zh-cn_image_0000002808887239.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=17A31C4E553E29667F9DA7EFD06846D6FC56BBC287CF34A8B8B68647B85EFC32)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/X7NOyDFhRYa22pYec5L5Tw/zh-cn_image_0000002779567582.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BA8944CD842430468EE4BAF3EEDE9AD21EBB74CE21D0802E4879A6EE3EE8CD4)

* **Stack Info**：展示崩溃的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。
  + **Raw Stack**：展示崩溃的原始堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Epu_L1V2Q4OqxgR5ro0cww/zh-cn_image_0000002808767149.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEA956F6D9DC05C1EE613F8455AA7A07A5909A695B331611A8894684DE82B580)
  + **Symbolicated Stack**：展示还原后的堆栈信息，堆栈还原需要先关联本地符号表或将符号表上传到云端进行解析，上传后符号表信息会在**Symbol Table**页签中显示。关联本地符号表或上传到云端成功解析还原后，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/EdcuZZX4Rye-oQ9NWfs4FQ/zh-cn_image_0000002808767159.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFABEAA4DF279F033AA9F08FE92B16F4A2116932A430CFD62C7C896499DDD516)

    堆栈还原后，点击右上角的**Select related project**，关联堆栈对应的工程，即可通过堆栈中的超链接跳转到对应的源码。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_LTpn_7ATIe2EFyruddhKQ/zh-cn_image_0000002808767151.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5D4F5EFE349A18518CE53A0BEC85B52EC27612A3EE61332DE5A45BF59197482)
* **Context Data**：崩溃的现场数据，展示栈地址空间、寄存器信息、FD信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ldXrShmsRGSH9R8IL7VCFg/zh-cn_image_0000002808887233.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E086A680C5A0D8D72AA9C42CB58C268314A244B7143BBB8574E20EA9AADF955)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/N0KqocOTTXiRk4IyRAUncg/zh-cn_image_0000002779407604.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2AC5BD2615A2B61574D684E4D2D0CB5682D307C9389FED33F06A759A3C9FFC1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/enSveSZQRtSYsLnQjzlyWQ/zh-cn_image_0000002779567578.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=706C0D14D5558F82FFE19E8834840B0CCE5A313A99E80C81A5A517092D224AC8)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Hqz3dzirQ4iH-1jWsvRnJQ/zh-cn_image_0000002779407596.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D04EEC471B85139F813C7782E72A0B26CD28960DD94DE7A415A802BC0E7FD18)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/iwPqBsxiRtWso5NLN6hM1A/zh-cn_image_0000002808767161.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=620699116E0256D2261D334553BCDECAE03999C55A9CD1C7D138F7C5E7C0A9FD)

### OOM分析

从26.0.0版本开始新增OOM，展示内存溢出详情。Stack Info页签展示内存溢出的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。Context Data页签展示内存溢出的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示内存泄漏问题列表。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个内存泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看内存溢出发生的分布情况，下半部分显示该内存溢出事件的可能原因。
* 7号区域：展示内存泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/U7z2G96kQRiqCVYNo2dwsQ/zh-cn_image_0000002779407598.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C054F9EAC9510C50CE8A71B8B7E1F8B90FEDE31A5D4149E0E1491B36F1202075)

* **Stack Info**：展示内存泄漏事件的堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。支持堆栈还原，并可跳转到具体的代码行查找问题，具体操作方式请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/EmdH3wIyRzSZWXr7HVrIqw/zh-cn_image_0000002808767153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA02B3E8D1D25D5AF28CB71698207AD7A0DD142088227F05809A9E1BA29C5A6C)

* **Context Data**：内存溢出的现场数据，展示页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QfksemXWSr23fEDKLUvhBw/zh-cn_image_0000002779407608.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=22E31B4EFE2EBF0FFD17D97F91C805156E5EF66A9B852ED055474DC924EFAA37)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Fb31hQ6bS1Sqe7jAkdGvjQ/zh-cn_image_0000002779567572.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=065508257B0E164FAB9DA5F2703013CE9F956590383637A13F58F088C0227175)

### APP Freeze分析

从26.0.0版本开始新增APP Freeze，展示应用冻屏详情。Evidence Chain页签展示应用冻屏的证据链信息，包括3s和6s的主线程堆栈信息。Context Data页签展示应用冻屏的现场数据。Sampled Stack Logs页签展示采样栈的原始和还原堆栈。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示应用冻屏问题列表，支持按功能列表和耗时函数筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个应用冻屏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看应用冻屏发生的分布情况，下半部分显示该应用冻屏事件的可能原因。
* 7号区域：展示应用冻屏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/DV0RZHlASWunSGlhADpWyQ/zh-cn_image_0000002779567588.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=57D7AB5865B45BEA53381D748D8F57F689B2D101644FE0D7C4A62797F60B3F53)

不同的冻屏类型对应的详情页存在差异，此处以THREAD\_BLOCK\_6S为例。

* **Evidence Chain**：展示该应用冻屏事件的证据链信息，包括3s和6s的主线程堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/fPFKDjbkSD-QCpVjdNGysw/zh-cn_image_0000002808887247.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F39EAB6064C06B7E94F0F80BF8908CEB526A1A78B98C551A7E6F1DC4CE736A7D)
* **Context Data**：展示该应用冻屏事件的现场数据信息，包括堆栈信息（原始堆栈和还原堆栈，堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）、CPU信息、内存信息、热档位信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/8v1WxS0BQVOuzSN0RadRTg/zh-cn_image_0000002779407600.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=A10B7A69C9F0B5B61267590C460DCED8EF5F7354DA70D9FE434E53723DCC545A)
* **Sampled Stack Logs**：展示该应用冻屏事件的采样栈日志信息，包括原始堆栈和还原堆栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/eS9Cj6lsQmqVZ2z0_1xeMA/zh-cn_image_0000002808887245.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=76591D2824A6AA5E1475D3EEA53CB0BA37B18F77661128D0121E2C13919156B4)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/WL_DK9vfRUWdgakuLwFyWw/zh-cn_image_0000002779407602.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DE080CAFD2DAA9EE5992BF459B6954B136E89C2EF01248FC61E68B72E2DD427)

### Resource Leak分析

从26.0.0版本开始新增Resource Leak，展示资源泄漏详情。Evidence Chain页签展示资源泄漏的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。Context Data页签展示资源泄漏的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示资源泄漏问题列表，支持按Top问题和ArkTS泄漏对象聚合筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、灰度任务id、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过灰度任务id搜索具体的某个资源泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看资源泄漏发生的分布情况，下半部分显示该资源泄漏事件的可能原因。
* 7号区域：展示资源泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Uwk3O1ZXSzmCbyd_-xVhBw/zh-cn_image_0000002779567576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C28673F0DF306125A953223985F9680ECF9D78AB35C8BD6A2421DB20F59FACAE)

不同的泄漏类型对应的详情页存在差异，此处以RSS\_LEAK为例。

* **Evidence Chain**：展示该资源泄漏事件的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。每个泄漏方法下会显示堆栈分配详情、堆栈树分配、火焰树、原始/还原堆栈。

  堆栈分配详情：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/XyCRnIdPT3KiA1DIbqS7ag/zh-cn_image_0000002808767145.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=627C3074E60F6D511422F25888F21022A896C721C3F127AC757F9A8209486CE4)

  堆栈树分配：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/MXTq2yp_QnGxBfPydtw0vQ/zh-cn_image_0000002779567586.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=18DF4619064DA17F201D4DEF7681420F166ED18DA4CD86D5DA0002FB3D4D918D)

  火焰树：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/2WR1zka_SO68oBskE5dYvg/zh-cn_image_0000002808887237.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C3765E5FDB0A8CC046975ADBE65426C138FD84A3372477F1A3876083335FD9B)

  原始/还原堆栈（堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/kCDAMuojQh2kUJGsLKyh0w/zh-cn_image_0000002808887243.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6558E0ABF473A3F935412E0E988F81F20C20CB29101A22CBCEC422D94631FB4C)
* **Context Data**：展示该资源泄漏事件的现场数据信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/iKBzHNfnQ5GyXL-1KHN5xw/zh-cn_image_0000002779567584.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9F097C5D9289126451CF7F36E55250530C38FA817286E6B99EBD84A6AAA3867)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/uUBY8g_dS5yL6Aa7czq6aQ/zh-cn_image_0000002808887241.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C14D23B9208D069F9D7D14E3B763BB00ACED7F92A0C64F116BA94409D88A5A0A)

## Metrics

### Crash分析

展示应用崩溃次数和崩溃率情况。

1号区域：通过tab页签可切换All，JsError（JavaScript崩溃错误），CppCrash（C++崩溃错误），OOM（内存导致的崩溃），ProcessKill（系统被强制终止），查看不同维度的崩溃次数、崩溃率进行分析。

2号区域：通过柱状图展示不同维度在所有的崩溃异常中的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9qQ4MsE5R9C8oyys94hlFw/zh-cn_image_0000002808767155.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=49E24470194511C059B46DED0D012D63CC32ADF1D5BBC2D3F5C0CCD15CFF64CD)

**说明** 

ProcessKill将通过柱状图和饼图联动，点击柱状图，通过饼图展示具体某个时间段的ProcessKill的类型分布。

### Frame Loss分析

对连续丢帧情况进行多维度统计，便于快速定位问题所在位置。

1号区域：丢帧总览是统计最大维度的连续丢帧率。

* <6：连续低于6帧的丢帧率。
* 6-15：连续大于6帧，小于15帧的丢帧率。
* >15：连续大于15帧的连续丢帧率。

2号区域：按照Page，Scenes两个维度展示丢帧异常率TOP N的页面或者场景。点击饼图上的某个区域，将展示具体页面或者场景的连续丢帧率情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/biaqJxZpQNCoqiq-bwVbLA/zh-cn_image_0000002779567580.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2A3117F59F7F3B01E01946977A14787A70C6B2E5F86CD8AAC495A9DF2AC511E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/DTuLqBCZSziEq6cZluuY0A/zh-cn_image_0000002808767157.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=754CF84E69825401A2B9E45395ED354CF08A56BDB65825016CEA43857B889976)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/THrN3fWCQZuGx8Q8_l5GaQ/zh-cn_image_0000002779407606.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=96026D755C79F768B9D1D690ECDFFF986AD3F85247440234D170B35D0A03ABF9)

### Battery Usage分析

用于统计设备的总能耗以及前后台的能耗和耗电时长。

1号区域：能耗概览。通过折线图展示总能耗，前台能耗，后台能耗。

2号区域：展示前台能耗和耗电时长随Top 5设备器件分布情况。

3号区域：展示后台能耗和耗电时长随Top 5设备器件分布情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/QlwgPodwSnCDpQsKQqPSmQ/zh-cn_image_0000002779567570.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D22F1E72BA86184EE3C1B24CF80DF9DCE9BE99E079478AFDC19B1B6FA2E0ACF)
