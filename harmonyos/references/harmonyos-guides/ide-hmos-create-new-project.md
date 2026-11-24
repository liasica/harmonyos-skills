---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-create-new-project
title: 创建一个新的工程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 创建一个新的工程
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:b589113b692ea7e1990644805235315dbb72a1cadfa03d57a0c834ed8843e662
---

当开发者开始开发一个应用/元服务时，首先需要根据工程创建向导，创建一个新的工程。工具会自动生成对应的代码和资源模板。

**说明** 

在运行DevEco Studio工程时，建议每一个运行窗口有2GB以上的可用内存空间。

## 创建应用工程

1. 通过如下两种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在鸿蒙电脑DevEco Studio的欢迎页，选择**新建工程**。
   * 如果已经打开了工程，可以在菜单栏选择**新建 > 工程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/JRFcg-hkQ3mt96wQcO4puA/zh-cn_image_0000002791841292.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=91870233FD50A21F582E9F8A4AF676D19EDD0489FAE461F97A6DC50098A9FA4E "点击放大")
2. 根据工程创建向导，在应用下所需的Ability工程模板，填写工程的基本信息。
   * **工程名**：工程的名称，可以自定义，由大小写字母、数字和下划线组成，必须由大小写字母开头，长度为1~200个字符。
   * **包名**：标识应用的包名，用于标识应用的唯一性。

     **说明** 

     应用包名要求：

     + 必须为以点号（.）分隔的字符串，且至少包含三段，每段中仅允许使用英文字母、数字、下划线（\_），如“com.example.myapplication ”。
     + 首段以英文字母开头，非首段以数字或英文字母开头，每一段以数字或者英文字母结尾，如“com.01example.myapplication”。
     + 不允许多个点号（.）连续出现，如“com.example..myapplication ”。
     + 长度为7~128个字符。
   * **保存位置**：工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。
   * **兼容SDK**：兼容的最低API Version。
   * **模块名**： 模块的名称。
   * **设备类型：**该工程模板支持的设备类型。设备类型说明请参考[deviceTypes标签](module-configuration-file.md#devicetypes标签)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/QibqWtfAS0OjOzxZ-JEmGA/zh-cn_image_0000002791844076.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=77B7114B2F7B5B9B7158CBDE4153E3446427D4681C3D7AECCD6F0483EC328CF0)
3. 单击**确认**，工具会自动生成示例代码和相关资源。

## 创建元服务工程

1. 若首次打开DevEco Studio，请选择**新建工程**。若已经打开了一个工程，请在菜单栏选择**新建** > **工程**。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/i3lhywJ3QVWWHoKB3CP_iA/zh-cn_image_0000002820721233.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=346DD94D42A4CB797FCBDC41FF7CCF6D4E6D0BACAE6E7318D65C0751936083E2 "点击放大")
2. 在元服务下选择所需的模板。

   选择**华为账号**后点击**登录**，登录华为开发者账号进行开发，或选择**访客模式**后点击**确认**。

   **说明** 

   访客模式无需登录华为账号。

   访客模式仅用于体验元服务开发功能。如需将访客模式下开发的元服务工程或历史元服务工程在真机上运行并安装，需在**AppScope > app.json5**文件中补充当前开发者账号下已在AppGallery注册且真实存在的包名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zM1kUKLmTtudx5NyE7OiGA/zh-cn_image_0000002792001264.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A09C767FBC0EE9BF21AAE808CEE05B2BEDBCE73CED2EB6E0A8B1FE14945E238 "点击放大")
3. 若您DevEco Studio中登录的华为账号尚未进行实名制认证，请点击**实名认证**进行认证。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/6mYcz0A1SiaQtZ365pBAhg/zh-cn_image_0000002820724723.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D63AE48B63142C8386E9D7A3FE1FB23B694809BD84B8D80DEDC843C4C6F05E8D "点击放大")
4. 选择登录华为账号下已经在AppGallery中注册的应用ID。如您未在AppGallery中注册元服务应用，或者需要使用新应用ID时，请点击**注册应用ID**进行注册。

   **说明** 

   仅元服务应用的应用ID在界面展示。

   在AppGallery注册应用ID时应用分类请选择“元服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/BTuge-qWTR6uA5SKaqItSA/zh-cn_image_0000002820681229.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=E58CDB5AAF2C3D4E6D59A60D23E3353F13A81B83561F532C5147032390719A32 "点击放大")
5. 点击**注册应用ID**，在弹窗中填写元服务的基本信息后，点击**确认**。
   * **项目**：项目名称。可以输入一个新项目名称，或在下拉框中选择已有项目。
   * **应用类型**：应用类型为元服务。此处不支持修改。
   * **应用名称：**元服务在华为应用市场详情页展示的名称。关于元服务名称要求请参考[为元服务创建APP ID](../doccenter-getting-started/agc-help-create-atomic-service-0000002247795706.md)。
   * **应用分类：**应用和游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ix5BhbVUSkSbTcDZBPiqhA/zh-cn_image_0000002820681227.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=3912BAAB80EF24CC55A3F85C889D296DFE273406304DEB53A0FFBB23213D00DE "点击放大")
6. 完成注册后，返回DevEco Studio界面刷新，选择所需的应用ID。填写**工程名**，其他参数保持默认设置即可。点击**确认**，工具会自动生成示例代码和相关资源，等待工程创建完成。

   **说明** 

   元服务的包名自动生成，采用固定前缀和应用ID组合方式命名（com.atomicservice.应用ID），开发者无法手动修改。
