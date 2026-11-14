---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-string-editor
title: string资源可视化编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > string资源可视化编辑
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a88e102c1854fdbaa8824be87c1eda43f69cdabec57edc26eb4bd8e069604624
---

## 功能介绍

在应用开发中，string资源分散于多个目录（如 resources/base/element/string.json、resources/zh\_CN/element/string.json、resources/en\_US/element/string.json 等），手动切换文件查看和编辑资源效率较低。

string资源可视化是以表格形式统一展示所有string资源的名称和值、所在资源目录等，提升可读性。同时，支持在可视化界面新建资源，在可视化表格编辑资源值、复制/粘贴资源、删除资源等，提升开发效率。该功能适用于多语言/多设备、跨工程/跨模块共享string资源、资源定位相关场景。

## 操作步骤

1. 双击资源文件中的string.json文件后，点击编辑界面的**Open editor**，即可进入string资源可视化编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/sjTLjXfmRhmi2mZKbqYixw/zh-cn_image_0000002779407112.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAA51ED67B778FAD2584C177CD0663A848F12720DFDFD0F7981E01256D29440E)
2. string资源可视化表格的示例如下，其中Name列为资源名称，Resource Folder列为资源目录，base列为默认资源目录的资源值，base后的列（如aa\_ET-wearable列）为限定词目录的资源值。

   **说明** 

   限定词目录以字母顺序依次排列在base列之后的各列中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/pfm4TzRmSd6AA3NhGxJ20A/zh-cn_image_0000002779407114.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=13D6487F2E712133CF5E212DD08AAF0A6EBAA4F543C08F914C34700F90A3D535 "点击放大")
3. 在可视化界面可以新建string资源、新建限定词目录（Qualifier）、筛选限定词目录、编辑表格内容等。
   * **新建base目录资源**

     点击顶部 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/whrWv10MSGS7BDPYx9E2AQ/zh-cn_image_0000002779567094.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=5587910B95C4172D082DC674B98364F935C2AE7B43A5BDDFE6501EBC2DAD2A55) 按钮，打开新建string资源向导，填写**Name**（资源名称）和**Value**（资源值），选择**Resource folder**（资源目录），点击**OK**。新建完成后，资源会写入相应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/YXiGvxO7REiSLyVlS9iUVg/zh-cn_image_0000002808886745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=169E1B2B285DA76B3B9773955E39081809CEC27A464DD7F166601E915F190CE0)
   * **新建****限定词目录****资源**

     点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/RKnAqBDBSYSTDiUAby-lHA/zh-cn_image_0000002808766665.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FCCCA081D1908E317E450CF3E2AF3AB49DC7276AB0AFA5F616760E6AC1E5B53)按钮，打开新建Qualifier向导，选择**Source set**（资源目录路径），在**Available qualifiers**下选择[限定词](../doccenter-getting-started/resource-categories-and-access.md#限定词目录)，点击**OK**。新建完成后，限定词资源会在工程目录和表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/VkbTMNGcSVyksANMkBx_WA/zh-cn_image_0000002808766671.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C1ABE273F49FB8C162EDBE145B1BB2FCC02B7CEEF3819C395EFDB59BAF0CB24)
   * **筛选限定词资源****目录**

     顶部筛选框支持过滤限定词目录，默认为Show All Qualifiers。选择某个Qualifier后，表格会展示Name列、Resource Folder列、base列和筛选的Qualifier列。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/u4v1lwYdQm2rG4f8PcwkPw/zh-cn_image_0000002808886753.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9E5E939DDCF6971A0B861486EF98FB3BE5740DCDA5ADD08FFE56C3FF205F9F8)
   * **编辑资源值**

     选中base列或限定词目录列中的单元格后，顶部输入框会显示当前值并支持编辑，或双击资源值单元格直接进入编辑模式，编辑后鼠标离开失焦或点击回车进行保存，资源值会写入对应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Zn2gCASzSte1IXrrnMdw-A/zh-cn_image_0000002779567090.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=42DE8D2FC4CB8C1F78818A716CEC995B3634898D46D70E36BA0C44374847F033)
   * **选择多个资源**

     从26.0.1版本开始支持。通过如下键鼠组合可同时选中表格多行，选中多行后可执行批量复制和粘贴、批量删除等操作。

     + Ctrl+单击（macOS中为Command+单击）：选中某行或取消选中某行，实现切换该行选中状态。
     + Ctrl+Shift+单击（macOS中为Command+Shift+单击）：从当前点击行至目标行连续选中。
     + 单击：取消多行选择，切换为单选单元格模式。

       **说明** 

       点击刷新![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/8X-LlfPLT_a-v-Dfo6SUyg/zh-cn_image_0000002808766669.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=99FCD58F036D8B5B6D76F85377EF8B11588A48A551E3D747D8CFAE277EB1240A)按钮，会取消多行选择。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/LZpYFj2yQ6qp6ls2Kepyzw/zh-cn_image_0000002808886749.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=4602A5F2EF223F9437F3C2232F32770B3362CE7AA922A2AF3B6C55FFBA406C72)
   * **复制资源**

     从26.0.1版本开始支持。选中表格单元格或行后右键，点击**Copy Line**会将选中的数据序列化为JSON格式并写入系统剪贴板，支持单行复制和多行复制。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Xg-Jg-TWThm0FNxdGLQlKA/zh-cn_image_0000002779567088.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=D675E65F0D97ADC69D8A974957CB87A57F0EAFB09AE680BCC576E4A5CFD263B4)
   * **粘贴资源**

     从26.0.1版本开始支持。在目标模块或工程的可视化表格中右键，选择**Create & Paste Line**，即可粘贴已复制的资源内容。粘贴时，资源仅会添加到目标模块或工程中已有的限定词目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/y75vHwmoTt6LFLyzhiY4Vg/zh-cn_image_0000002779567096.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=1146F70E96430C395250DA4CDCAC47F2E50DB75A79FDF134937033C88BDDDCF9)

     当粘贴数据中存在与当前表格同名资源时，会有弹窗提示：

     + Cancel：取消粘贴。
     + Ignore：只创建无冲突项，跳过同名资源。
     + Overwrite：用新值覆盖同名资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yDvFm98ST7evm-ZHkzHE7A/zh-cn_image_0000002808886747.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=B57B158CA628622EF93C12F42C36A4CB03F2FA6E88C099091D7F82A9F49774F4)
   * **跳转至****string.json源文件****和资源声明位置**

     选择非空单元格后右键，点击**Go to Declaration**，可打开对应的string.json源文件并定位到string声明的位置。

     其中，选择Name列、Resource Folder列和base列单元格，会跳转至base目录下的string.json文件中；限定词目录列（如aa）会跳转至限定词目录下的string.json文件中。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/kUT40k4fR36RiucjT5-aOw/zh-cn_image_0000002779407116.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF9E319C0E4FE864FF7021FC074B3BEFA0A0B27017963C708831C56D25761F84)
   * **删除****资源值**

     选中base目录或限定词下的资源值后右键，点击**Delete string**，即可删除选中的资源值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/_UUUHmqTQCGP3-VvdljB6Q/zh-cn_image_0000002779567084.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=A919EBB8779E22EC24AB46350AF680CB7FA4F3A1E6260D7E25742B24E59D9B58)
   * **删除资源**

     选中Name列或Resource Folder列某个单元格后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/21LjHLs9T8eQNjr-Mm8ZhQ/zh-cn_image_0000002808766667.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=913E5D5FBD0C17A24FDFCCC5463F27A62BA90AC3F3FBC4B33BFC7572646D664E)

     从26.0.1版本开始支持。选中可视化表格多行后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可批量删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/VGtqJYpSRYaWyIaWAgeFZQ/zh-cn_image_0000002779407110.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4B35FCAE2A8557FBE86F5E6730EE3639ABC30361784B89ADA5B44973A7C1F42)
