---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-operation-and-services
title: 运维分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 发布应用 > 运维分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:46+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f6583f27a04dbff2f9ecb4d09a477ce80a7271a39403dbe58c9c514f377ff9fb
---

DevEco Studio支持对已发布上架的应用在使用过程中出现的崩溃、应用冻屏、OOM、资源泄漏等问题进行定位分析，以及查看崩溃、卡顿、丢帧、能耗等异常问题的趋势和分布情况。

## 使用约束

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 页面布局

在DevEco Studio菜单栏点击**View > Tool Windows > Operation Analyzer**，进入运维服务页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/MgUmdKQBT1CjD2RGHSmTzA/zh-cn_image_0000002779407610.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F111B51119DCB08D549C40DD23D62F11E96C6F66F72F164509E30153C866E2B)

点击**Add account**按钮，登录华为账号并授权后，可以查看当前账号下应用异常情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/aWuxfvJiRZOf20AmwP8YcQ/zh-cn_image_0000002808887235.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=545FA6BF9BA423441E283B176C430A9231BB9EB6860D82B4A582296239A96F7C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/1tSRl3ILQ9WXTgcGsCeUAA/zh-cn_image_0000002808887239.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EC93E31D0D15EE8C276844935AF39B657B0EE26E6260BCAFC9CEB92A69FCF78)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/e1mrDrKMTga195srQ-YYfA/zh-cn_image_0000002779567582.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C3B98CBBF4D8A37FBA9F42D3445A172291A51998F5E1F02E9E906A6007AC450)

* **Stack Info**：展示崩溃的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。
  + **Raw Stack**：展示崩溃的原始堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/oUzyGgo2TNic1l_FdnSBRg/zh-cn_image_0000002808767149.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF74B5FA7B25FCE2BD9C593450B102C34E5232C845750FFA5FF248561F97C7F1)
  + **Symbolicated Stack**：展示还原后的堆栈信息，堆栈还原需要先关联本地符号表或将符号表上传到云端进行解析，上传后符号表信息会在**Symbol Table**页签中显示。关联本地符号表或上传到云端成功解析还原后，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/O6jv3PlsQNG9UO2tqJFzZw/zh-cn_image_0000002808767159.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=85ABB7B8F99752BBB67E2880C72833DA6C651742F4766BCFBAA9E7A98F72ED9C)

    堆栈还原后，点击右上角的**Select related project**，关联堆栈对应的工程，即可通过堆栈中的超链接跳转到对应的源码。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/TTOmcCvsSJWoKJfuy3q_Cg/zh-cn_image_0000002808767151.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1AD0A0CD64839F19525A0BDD653683E0B10549476F0BE62F9E7E9BD10EE6C5F)
* **Context Data**：崩溃的现场数据，展示栈地址空间、寄存器信息、FD信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/IpmgEgoGSduj0CUD96w5Rw/zh-cn_image_0000002808887233.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5621AE522509E2E88E26A5D992EEDF4D052CA9F7F13D9536F7F6E3F0CDD5AF4)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/TlUupZNYT2eDPaBaR-n1aw/zh-cn_image_0000002779407604.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D87166DCA3652CFFF1313A95C8C66003610235D9B6A23EC8DF3F8DA777FC76)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/-08giuEmSSmMJYPlPqJaNA/zh-cn_image_0000002779567578.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAE4EBDBC41FC5E795FCD23A0B52C4ACF5F4527FBE9F28A4EB09FCAFF10C88F3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/EB9uLw5JQg-C_wSpofFIhQ/zh-cn_image_0000002779407596.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0BF64D84A92CD5C676213B8C3086DAA0AE45BDF78B3389073450BC6E726DE7B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ekykzp-4R9-GgOBX0jJYLQ/zh-cn_image_0000002808767161.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=34FF31D17CB6A46DE3F07CBEAF556F4877BA394BCA6AF347ACE66C83B085EB82)

### OOM分析

从26.0.0版本开始新增OOM，展示内存溢出详情。Stack Info页签展示内存溢出的堆栈日志信息，支持堆栈还原，并可跳转到具体的代码行查找问题。Context Data页签展示内存溢出的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示内存泄漏问题列表。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个内存泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看内存溢出发生的分布情况，下半部分显示该内存溢出事件的可能原因。
* 7号区域：展示内存泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/aTS1UOi8TVe6x6eXNN_PdA/zh-cn_image_0000002779407598.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=32DC16831FC1D19637512D34B1E1151955E5261BB5867B2C23827BCF04A1B330)

* **Stack Info**：展示内存泄漏事件的堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。支持堆栈还原，并可跳转到具体的代码行查找问题，具体操作方式请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/1XB9aqX-T4OMZYTqHB4jCA/zh-cn_image_0000002808767153.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=3185433D6458AFAEDEF34DAACF98CFCFACE0B6E4175B53CB54A35F69E9E02D59)

* **Context Data**：内存溢出的现场数据，展示页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/YdDzybA1T9OtInYji8_6BA/zh-cn_image_0000002779407608.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB97B9A866B842D2A060C4BDC1D579F1886003ABE7A65538BCD0A101C43226C6)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/6dsRMC4zTnS_i5w4IDAxwQ/zh-cn_image_0000002779567572.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=B735AB94A316488E92D6E88AB1067446AC8B71DEC3FBBB80575CC66C78DD1A80)

### APP Freeze分析

从26.0.0版本开始新增APP Freeze，展示应用冻屏详情。Evidence Chain页签展示应用冻屏的证据链信息，包括3s和6s的主线程堆栈信息。Context Data页签展示应用冻屏的现场数据。Sampled Stack Logs页签展示采样栈的原始和还原堆栈。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示应用冻屏问题列表，支持按功能列表和耗时函数筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、故障指纹、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过故障指纹搜索具体的某个应用冻屏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看应用冻屏发生的分布情况，下半部分显示该应用冻屏事件的可能原因。
* 7号区域：展示应用冻屏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/L_wX681QQVWjaeLM_jMtrw/zh-cn_image_0000002779567588.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=D21CAD1DA9E0DF7B87E339DC95F92AAF7DBF9E1D96A629C71AEC8A442745265B)

不同的冻屏类型对应的详情页存在差异，此处以THREAD\_BLOCK\_6S为例。

* **Evidence Chain**：展示该应用冻屏事件的证据链信息，包括3s和6s的主线程堆栈信息，其中蓝色圆点代表系统栈，绿色圆点代表应用栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Nze2b10wRWmk1ysRLNROIw/zh-cn_image_0000002808887247.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=E94891C59BD64CD7044633ACEAF614232DD42C893352743472B65EE190DCAF1C)
* **Context Data**：展示该应用冻屏事件的现场数据信息，包括堆栈信息（原始堆栈和还原堆栈，堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）、CPU信息、内存信息、热档位信息、页面跟踪信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/8Xd5Zu5sTGGZaaTrwHKfaQ/zh-cn_image_0000002779407600.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D9CB77D23C000DEFF9082C7A59D4C54D3707FF4C5674A8459C4739823F29F58)
* **Sampled Stack Logs**：展示该应用冻屏事件的采样栈日志信息，包括原始堆栈和还原堆栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Ym5ECZ9vQNmnaQir9UlfRw/zh-cn_image_0000002808887245.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=690E75C247553999CD1F40DDEB5ADC4368C14599C6C8E22F99B5048F2FA50C19)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/qEvHJ8hBTkaQZK6_iQlsDQ/zh-cn_image_0000002779407602.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE6BECDE0F475AB4B9C551D49CE3573192543356C6B64C9B37575214127FEF8A)

### Resource Leak分析

从26.0.0版本开始新增Resource Leak，展示资源泄漏详情。Evidence Chain页签展示资源泄漏的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。Context Data页签展示资源泄漏的现场数据。Symbol Table页签支持上传符号表到云端和关联本地符号表。

* 1号区域：展示资源泄漏问题列表，支持按Top问题和ArkTS泄漏对象聚合筛选排序。
* 2号区域：从上到下，从左到右依次显示问题特征id、灰度任务id、设备型号、系统版本、事件发生时间、应用版本号、构建号。
* 3号区域：可以通过灰度任务id搜索具体的某个资源泄漏事件。
* 4号区域：点击可以关闭该问题，关闭后按钮置灰，但是该问题不会删除。
* 5号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位**。**
* 6号区域：上半部分可以通过切换应用版本/设备型号/系统版本来查看资源泄漏发生的分布情况，下半部分显示该资源泄漏事件的可能原因。
* 7号区域：展示资源泄漏事件详情页，请查看下文说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/0nZOZlGwQkugZgHHuAlKIg/zh-cn_image_0000002779567576.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=B752B8751E0693F14640E37E62904494DB8B27CF71652C6B6205E860BB390C9E)

不同的泄漏类型对应的详情页存在差异，此处以RSS\_LEAK为例。

* **Evidence Chain**：展示该资源泄漏事件的证据链信息，包括主泄漏堆块和次泄漏堆块，每个泄漏堆块下又包含主泄漏方法和次泄漏方法。每个泄漏方法下会显示堆栈分配详情、堆栈树分配、火焰树、原始/还原堆栈。

  堆栈分配详情：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GiWB6W4hTEeiSP9WPqhvPA/zh-cn_image_0000002808767145.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D7EE0BECB3D66D2AEE59956DBC29A02C686193F51CE00BF7C2BBE0CED4AB678)

  堆栈树分配：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/gpEC8z2bRg6AiuwfLP1myQ/zh-cn_image_0000002779567586.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=B507ED3679A91246AF909A62FDABB4B650EF36FC950024230541794353A9FD5F)

  火焰树：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/WIjFwdZqTieI48WjksKhig/zh-cn_image_0000002808887237.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=021E7D11307DC617AB82492256CED0EEF08586D82FB8964D81FAEF4B4B88688F)

  原始/还原堆栈（堆栈还原方法请参考[Crash堆栈还原](ide-operation-and-services.md#li37692225178)）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/grZTaCWHSFaoiFhOpNVOwg/zh-cn_image_0000002808887243.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=5406BDC17C9F620E64F44CD9A3432C22354BF241E87876B35BADA82EE85C9983)
* **Context Data**：展示该资源泄漏事件的现场数据信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/0qpQMr-2TJufVjhYtO5HwQ/zh-cn_image_0000002779567584.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E4F95329FFF8C06DA9CA9668340BBD26C9BBC15CD7BD70E5E2BB5A13AD9521D)
* **Symbol Table**：展示云端的符号表和本地关联的符号表信息，此处也支持上传符号表到云端和关联本地符号表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/se77BEAYR8eBeru664HCaQ/zh-cn_image_0000002808887241.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=35401E53D8F54CF9F749EBD8D18CA18D49347E4D6F66A2E439DBDB1B766B3401)

## Metrics

### Crash分析

展示应用崩溃次数和崩溃率情况。

1号区域：通过tab页签可切换All，JsError（JavaScript崩溃错误），CppCrash（C++崩溃错误），OOM（内存导致的崩溃），ProcessKill（系统被强制终止），查看不同维度的崩溃次数、崩溃率进行分析。

2号区域：通过柱状图展示不同维度在所有的崩溃异常中的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/hDC8wue_TTqvyGP3O6hmkw/zh-cn_image_0000002808767155.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C97434DF9420007440997AD82A9396754AF9DD9F118D0E4294DB3DFDEC2D5BB)

**说明** 

ProcessKill将通过柱状图和饼图联动，点击柱状图，通过饼图展示具体某个时间段的ProcessKill的类型分布。

### Frame Loss分析

对连续丢帧情况进行多维度统计，便于快速定位问题所在位置。

1号区域：丢帧总览是统计最大维度的连续丢帧率。

* <6：连续低于6帧的丢帧率。
* 6-15：连续大于6帧，小于15帧的丢帧率。
* >15：连续大于15帧的连续丢帧率。

2号区域：按照Page，Scenes两个维度展示丢帧异常率TOP N的页面或者场景。点击饼图上的某个区域，将展示具体页面或者场景的连续丢帧率情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/QFW2MwhfT_qvu9TV3eVGjw/zh-cn_image_0000002779567580.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AFAEB4C22C371D13F9F831D086BFAFC8CF039EE83422CB83C78D52F3B3E875B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/QbZcfCBIR7WfrKokuDjzzQ/zh-cn_image_0000002808767157.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=152F84CFFC9192838C31D848E9668804F768C328692DAF77B7C9996D3472712B)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/qgcav1bnSoa480zLEOlXOQ/zh-cn_image_0000002779407606.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F62EC66F02B395183F3814448459020585E53A899F0E24557DF4BB4545D7A90)

### Battery Usage分析

用于统计设备的总能耗以及前后台的能耗和耗电时长。

1号区域：能耗概览。通过折线图展示总能耗，前台能耗，后台能耗。

2号区域：展示前台能耗和耗电时长随Top 5设备器件分布情况。

3号区域：展示后台能耗和耗电时长随Top 5设备器件分布情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/8GjMEo5TSGCra1CsHYDaIw/zh-cn_image_0000002779567570.png?HW-CC-KV=V1&HW-CC-Date=20261128T023446Z&HW-CC-Expire=31536000000&HW-CC-Sign=678A0D40B98ECDF861BC07B8F5FD23894E72716C59357D7442133294E8C03159)
