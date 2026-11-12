---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-string-editor
title: string资源可视化编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > string资源可视化编辑
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fdeb7eea65965af2fdecb714d212df6f69c2cacdfd5b3aa568280baf428ebf13
---

## 功能介绍

在应用开发中，string资源分散于多个目录（如 resources/base/element/string.json、resources/zh\_CN/element/string.json、resources/en\_US/element/string.json 等），手动切换文件查看和编辑资源效率较低。

string资源可视化是以表格形式统一展示所有string资源的名称和值、所在资源目录等，提升可读性。同时，支持在可视化界面新建资源，在可视化表格编辑资源值、复制/粘贴资源、删除资源等，提升开发效率。该功能适用于多语言/多设备、跨工程/跨模块共享string资源、资源定位相关场景。

## 操作步骤

1. 双击资源文件中的string.json文件后，点击编辑界面的**Open editor**，即可进入string资源可视化编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/SMA6lpquTnOqUtEYnYHHJg/zh-cn_image_0000002779407112.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=85202F7F5E59C6DBCF6BE5CAB72F5FBB8B8588C6FBEC70E732766B5A3FB80CC1)
2. string资源可视化表格的示例如下，其中Name列为资源名称，Resource Folder列为资源目录，base列为默认资源目录的资源值，base后的列（如aa\_ET-wearable列）为限定词目录的资源值。

   **说明** 

   限定词目录以字母顺序依次排列在base列之后的各列中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/zByWDdnrSXefEwrVAS653w/zh-cn_image_0000002779407114.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=56BF7DE12BCC37AB66451E1E0DF953444B61F5C1A5139590ED7A26C38FD1A282 "点击放大")
3. 在可视化界面可以新建string资源、新建限定词目录（Qualifier）、筛选限定词目录、编辑表格内容等。
   * **新建base目录资源**

     点击顶部 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/5ETbpOc7TiK4Tx3Qv2q8tQ/zh-cn_image_0000002779567094.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A43CC89B92C45B419B7D5B63A6F0A4542E46A9F4C042E5952AFECEC71E7E5890) 按钮，打开新建string资源向导，填写**Name**（资源名称）和**Value**（资源值），选择**Resource folder**（资源目录），点击**OK**。新建完成后，资源会写入相应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/0wptPjJzTPmdPehLkdf0AA/zh-cn_image_0000002808886745.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=26C87AD7026859DDC2A244DCB4097BE2A090197C10F70475F8587C28173E8C76)
   * **新建****限定词目录****资源**

     点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/gn5Wp0nDStOsrIqP5ZSGog/zh-cn_image_0000002808766665.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDB437C09A222F9A9705F4C2C7E91CD8973EE3CEFE677A59F0652271BBD85DF5)按钮，打开新建Qualifier向导，选择**Source set**（资源目录路径），在**Available qualifiers**下选择[限定词](../doccenter-getting-started/resource-categories-and-access.md#限定词目录)，点击**OK**。新建完成后，限定词资源会在工程目录和表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/4_aVeCdzS5KhuyBNsV2mhQ/zh-cn_image_0000002808766671.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A17916875B4D39F865092862A6173E6286B694C7FF39DA8A6F709F4570FFA24A)
   * **筛选限定词资源****目录**

     顶部筛选框支持过滤限定词目录，默认为Show All Qualifiers。选择某个Qualifier后，表格会展示Name列、Resource Folder列、base列和筛选的Qualifier列。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/B1fvrlKsS2S4NQoV24RwlQ/zh-cn_image_0000002808886753.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA8446FCACA53751E68FAC576FA762335B2AA7B4415A9E7A9A976A568F29834F)
   * **编辑资源值**

     选中base列或限定词目录列中的单元格后，顶部输入框会显示当前值并支持编辑，或双击资源值单元格直接进入编辑模式，编辑后鼠标离开失焦或点击回车进行保存，资源值会写入对应的string.json文件以及在可视化表格中同步展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/hOSWoyvuQBmlJQ0wsuV7XQ/zh-cn_image_0000002779567090.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=84C228FD995E4BC1FED0945C917A29F0CCF97B9739CCE8132858B3DDE8AA94EF)
   * **选择多个资源**

     从26.0.1版本开始支持。通过如下键鼠组合可同时选中表格多行，选中多行后可执行批量复制和粘贴、批量删除等操作。

     + Ctrl+单击（macOS中为Command+单击）：选中某行或取消选中某行，实现切换该行选中状态。
     + Ctrl+Shift+单击（macOS中为Command+Shift+单击）：从当前点击行至目标行连续选中。
     + 单击：取消多行选择，切换为单选单元格模式。

       **说明** 

       点击刷新![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/bn5kd7MwQkW94q6h3L0rYw/zh-cn_image_0000002808766669.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD383872730674C850016FE5656F55C864D524C5F3C59C7FDA8137A061B59FB2)按钮，会取消多行选择。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/wZubpWfSTa6DJqImq-pCzw/zh-cn_image_0000002808886749.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4382140A834BB086401FC819622F7DEF3A58A2AB54F8C21B7E5AD2CBC0C746A)
   * **复制资源**

     从26.0.1版本开始支持。选中表格单元格或行后右键，点击**Copy Line**会将选中的数据序列化为JSON格式并写入系统剪贴板，支持单行复制和多行复制。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/uRsgY8OHSp-R6VGvHNUFlw/zh-cn_image_0000002779567088.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=789C7937C3552003E53C803C27043FEA26E0DC4489CB96CA0EB46BDB1B8EDE7E)
   * **粘贴资源**

     从26.0.1版本开始支持。在目标模块或工程的可视化表格中右键，选择**Create & Paste Line**，即可粘贴已复制的资源内容。粘贴时，资源仅会添加到目标模块或工程中已有的限定词目录下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/XhW_f6vTT9eiqpaN6lqLOw/zh-cn_image_0000002779567096.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7817802BA8E4EF5337AE73DDA8B75859D91F9C3004565941A553309B15FF0077)

     当粘贴数据中存在与当前表格同名资源时，会有弹窗提示：

     + Cancel：取消粘贴。
     + Ignore：只创建无冲突项，跳过同名资源。
     + Overwrite：用新值覆盖同名资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ed7d117LSUuwQd8Ta6DZmQ/zh-cn_image_0000002808886747.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E18831BCB596E45AD640E7C714ABDF55E7CEFBBE25C8C7E4D18053EFD29DE40)
   * **跳转至****string.json源文件****和资源声明位置**

     选择非空单元格后右键，点击**Go to Declaration**，可打开对应的string.json源文件并定位到string声明的位置。

     其中，选择Name列、Resource Folder列和base列单元格，会跳转至base目录下的string.json文件中；限定词目录列（如aa）会跳转至限定词目录下的string.json文件中。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/lPcwUOo9SjOMU039mCxVmg/zh-cn_image_0000002779407116.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=200B126B72DE288F54AE7C4E1C47921D1BD7E749A463440AE1FC236FE76312F5)
   * **删除****资源值**

     选中base目录或限定词下的资源值后右键，点击**Delete string**，即可删除选中的资源值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/OMo0NrpvT9q5e8XskF23HQ/zh-cn_image_0000002779567084.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=6752AC519A901453EC24DEF57FF4E41675B7463C4F4BEEFBF95BE65AF9DA440B)
   * **删除资源**

     选中Name列或Resource Folder列某个单元格后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Go0g4h95QTKI5pXb1p8DHw/zh-cn_image_0000002808766667.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9F752AF2A2D7007CA80FDB3D4279A02E84D18A24D05E60A8F6FE7617926507A)

     从26.0.1版本开始支持。选中可视化表格多行后右键，点击**Delete key**，在弹出的确认对话框中点击**OK**，即可批量删除base目录和限定词目录下的对应资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/46O6h_eZSKGuVue7gIBAbQ/zh-cn_image_0000002779407110.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E70E3959C3C177730F4ED9ED40D0B8FC8C21D7511DC27F1EE5E0C0F33CE7A7C4)
