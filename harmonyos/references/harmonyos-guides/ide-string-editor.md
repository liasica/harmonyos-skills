---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-string-editor
title: string资源可视化编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > string资源可视化编辑
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f0d1000e3f06f4037fbfc156af2cf40519f7889f06715cddc8be5d3393a9997a
---

## 功能介绍

在应用开发中，string资源分散于多个目录（如 resources/base/element/string.json、resources/zh\_CN/element/string.json、resources/en\_US/element/string.json 等），手动切换文件查看和编辑资源效率较低。

string资源可视化是以表格形式统一展示所有string资源的名称和值、所在资源目录等，提升可读性。同时，支持在可视化界面新建资源，在可视化表格编辑资源值、复制/粘贴资源、删除资源等，提升开发效率。该功能适用于多语言/多设备、跨工程/跨模块共享string资源、资源定位相关场景。

## 操作步骤

1. 双击资源文件中的string.json文件后，点击编辑界面的**Open editor**，即可进入string资源可视化编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/XA9HjwdsTGmWyUsMFgv4Pg/zh-cn_image_0000002779407112.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=13CE16F145B390B788ADA1D119996197AA0AB8CE108B871CAB3DD75A9312D508)
2. string资源可视化表格的示例如下，其中Name列为资源名称，Resource Folder列为资源目录，base列为默认资源目录的资源值，base后的列（如aa\_ET-wearable列）为限定词目录的资源值。

   **说明** 

   限定词目录以字母顺序依次排列在base列之后的各列中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/T4C4sMPlQVe6YxY3InBv8A/zh-cn_image_0000002779407114.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=5212F8372AB445A06D1BAD8AF5F672F005E1DD10AB66EE342EEBC0554D18C234 "点击放大")
3. 在可视化界面可以新建string资源、新建限定词目录（Qualifier）、筛选限定词目录、编辑表格内容等。
   * **新建base目录资源**

     点击顶部 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/iMNqisB5RomVX20g_xfXBQ/zh-cn_image_0000002779567094.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5153EEA8464708EA90BEC90F10141A9351EE6A8F538C83FCFD3F795339C6950) 按钮，打开新建string资源向导，填写**Name**（资源名称）和**Value**（资源值），选择**Resource folder**（资源目录），点击**OK**。新建完成后，资源会写入相应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/TY8uWu6WQYubm8OK6389zw/zh-cn_image_0000002808886745.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BA7341F535221FB39B2A48D5EDECF2EBEA600C410606587E77EDE35602C184F)
   * **新建****限定词目录****资源**

     点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/T1r-JVNXS4i9MZkjguj0aQ/zh-cn_image_0000002808766665.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5C4BB39F57D04725B4B050A8DF0A53E940947B388C0DAD3AAEFF5B02216895C)按钮，打开新建Qualifier向导，选择**Source set**（资源目录路径），在**Available qualifiers**下选择[限定词](../doccenter-getting-started/resource-categories-and-access.md#限定词目录)，点击**OK**。新建完成后，限定词资源会在工程目录和表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/aR-RtcAWSsSh6KpYU7-3dA/zh-cn_image_0000002808766671.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E89908330F7E49CFB2B9E502F549382EC08F021B0A96458618C562B4158120E)
   * **筛选限定词资源****目录**

     顶部筛选框支持过滤限定词目录，默认为Show All Qualifiers。选择某个Qualifier后，表格会展示Name列、Resource Folder列、base列和筛选的Qualifier列。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/6LiYs9nFRnqjB27uaj94ww/zh-cn_image_0000002808886753.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CB5A595BA858A59631C29D3936FFD8C9801C63A5A4284DC344E103B4D1F67EF)
   * **编辑资源值**

     选中base列或限定词目录列中的单元格后，顶部输入框会显示当前值并支持编辑，或双击资源值单元格直接进入编辑模式，编辑后鼠标离开失焦或点击回车进行保存，资源值会写入对应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DH8MMnteSKe3aVpTS5-bCQ/zh-cn_image_0000002779567090.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=4313B9AEC6E1E4F7330862BBEA005F0172F767D826A4F5C05AD85E82DFA07639)
   * **选择多个资源**

     从26.0.1版本开始支持。通过如下键鼠组合可同时选中表格多行，选中多行后可执行批量复制和粘贴、批量删除等操作。

     + Ctrl+单击（macOS中为Command+单击）：选中某行或取消选中某行，实现切换该行选中状态。
     + Ctrl+Shift+单击（macOS中为Command+Shift+单击）：从当前点击行至目标行连续选中。
     + 单击：取消多行选择，切换为单选单元格模式。

       **说明** 

       点击刷新![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/OsGa_2vjQ5q9u1rvYUXl0w/zh-cn_image_0000002808766669.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=C37400A996682652C166B83220F0517060DF2911F39B7D467B3D147A045000D0)按钮，会取消多行选择。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/gBTRr-9oRheZIPCYCW0f-w/zh-cn_image_0000002808886749.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=4082142C4AADF4C2387383316BB03DE065351E457C774CB4F14E636DA4D5DDD0)
   * **复制资源**

     从26.0.1版本开始支持。选中表格单元格或行后右键，点击**Copy Line**会将选中的数据序列化为JSON格式并写入系统剪贴板，支持单行复制和多行复制。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/JnII41BXR2iALDhTDU-trg/zh-cn_image_0000002779567088.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4E9D231C611CBB71FA24752D357310E2AADAD4DDDC0CBE994D4596F9D8B200F)
   * **粘贴资源**

     从26.0.1版本开始支持。在目标模块或工程的可视化表格中右键，选择**Create & Paste Line**，即可粘贴已复制的资源内容。粘贴时，资源仅会添加到目标模块或工程中已有的限定词目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/dpR46yipR-i-FrUZMirg0g/zh-cn_image_0000002779567096.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EF8C7B8A0FECDAAC48F57DA8A289530FDAFA1EBDBDAA86FE6407FC125AF9EF5)

     当粘贴数据中存在与当前表格同名资源时，会有弹窗提示：

     + Cancel：取消粘贴。
     + Ignore：只创建无冲突项，跳过同名资源。
     + Overwrite：用新值覆盖同名资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/U9SLFviaTbOB0YJNhsDOTg/zh-cn_image_0000002808886747.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C807D6FC1B79D7C1126E430DDC51910A5F4BD687F4D74FDD073C15EB8FD3D1B)
   * **跳转至****string.json源文件****和资源声明位置**

     选择非空单元格后右键，点击**Go to Declaration**，可打开对应的string.json源文件并定位到string声明的位置。

     其中，选择Name列、Resource Folder列和base列单元格，会跳转至base目录下的string.json文件中；限定词目录列（如aa）会跳转至限定词目录下的string.json文件中。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/qNbI7zWwSn2koBMok-hBrA/zh-cn_image_0000002779407116.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0DFFD7A3982D9C32A8A8A2EBE47FE7C563130FD3C7D4D7CED81E27A2CA48241)
   * **删除****资源值**

     选中base目录或限定词下的资源值后右键，点击**Delete string**，即可删除选中的资源值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/pCOz1fj7RDGLkxl17Kp6Ag/zh-cn_image_0000002779567084.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=C57A36C430512DFE30824CE588AB41BFBCE097DB5C08096F2C1175FF7E600A04)
   * **删除资源**

     选中Name列或Resource Folder列某个单元格后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/BskcKj0IRv-bI8U-Qh-HWQ/zh-cn_image_0000002808766667.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=465FB4CCF64E8826178563D1EC1A389AE0A36ED83C77AEB7FEED7AE017EC4F6B)

     从26.0.1版本开始支持。选中可视化表格多行后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可批量删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/RcG6zfklSze12QChPW2MKw/zh-cn_image_0000002779407110.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAEEB7CBA4916160B3826E49C709D6DE3C930B6F099247D1B9082D0BA2738E9C)
