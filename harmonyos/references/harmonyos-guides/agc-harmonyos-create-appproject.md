---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject
title: 创建HarmonyOS应用工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建HarmonyOS应用工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:58+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:03de7569ab5b0e89fc94d26ec0a5cee41e69c763fd346b0943af4569559b1fd0
---

## 新建工程

### 前提条件

* 您已完成[开发准备工作](agc-harmonyos-clouddev-prerequisite.md)。
* 您已使用[已实名认证](agc-harmonyos-clouddev-account.md)、且注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为开发者账号登录DevEco Studio。
* 请确保您的华为开发者账号无欠款，账户欠费将导致云存储服务开通失败。

### 选择模板

1. 选择以下任一种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在DevEco Studio的欢迎页点击“Create Project”开始创建一个新工程。
   * 如果已经打开了工程，可以在菜单栏选择“File > New > Create Project”来创建一个新工程。
2. 在“Application”页签，选择合适的云开发模板，然后点击“Next”。

   说明

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/AnpJjvPsSDmZ45ed45UTYg/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=4FD26F94B4DFBE18B6A92F95E8A915E54D55C39A6F12384C0FE446C3E9355443)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](ide-create-new-project.md#section11644183711342)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Oj7b17_VQ9iHGThA3ul46w/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=8EC80E6E1ECC6D7D821C871E6D8F260A3947C012CC85CA6FE30CBD4A9BC62446)

2. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/qklPl_zeQbarbGL52T_V7A/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=F3716C68C977B0DD23DF9CCB250733F6A061FF8F015A89B99AB1C9DA953D9DDE)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/AytnB-GUQvyuvbw642Ktrg/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=3783D89D3837FBA5F8FA4764C29ED56FF7373F3A851DA6B7A895F7948E5B139D)
2. 点击“Team”下拉框，选择开发团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9HF4a8v_QOeYbjt2ifNymQ/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=FC06FD1ACCF99C2A002BA08B3CD48EF40A7D5A8A088FEBD15D915E00DF20A369)
3. 关联应用。

   选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。

   * 如查询到应用，选中该应用，点击“Finish”即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/svOqa4PwR_-ncYQqwm0XcQ/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=5CD979FCB832C157EF0E75B0AF71C08A8FD73BAA5F0AEEBEEB0275A132849515)
   * 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到AGC项目下](agc-harmonyos-create-appproject.md#section152521927193013)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/fh3KMuXcQiuUeeNFoBGTiw/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=07214AB0EDDF70E67993CB1B9646B59FBA4EDCD27A0CF4CD5602A7AFC4E9D74C)
   * 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/zU-nPVW9T1ekkRGmVXx__A/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=E44F28A385190C289CCC52FD063E9473CC07DDD3094BB0098F8E167BFC67B549)刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/4ePICdXISyCzBDd_V-O-0A/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=B70F7899A3D49A1E5FDEDDC3A1A44950DEC62A1FBA1547CC08D1C17ACD2926A7)
   * 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与AGC上同包名应用均为HarmonyOS应用类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/lalTSvo2QrusJ1Zud2Ss9g/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=A743E6829920252381BF8E858727B8820D956B1767D3AACF07F6F6EFB2D9E074)
   * 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
     + 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
     + 如包名无误，则表明当前团队尚未在AGC控制台创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往AGC控制台进行补充创建](agc-harmonyos-create-appproject.md#section397317130308)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/KWLyqjb6Rm-qJ9SWtD8Hcw/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=19E6BC6A2CDD74FE218D6CB8BBEE509FE5C0738D0D708AF7AD86DEFAC7798452)

     完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/QYN0lYHgQGihAdElzbZvkQ/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=423532BC5E195E0178BF5D47437790B1F16745FA0CD9558B9A6BFD0F0D55EEBE)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。

   说明

   只有账号持有者和法务角色才有权限签署协议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/sZ5hhD2LSLiXt2KvtHy9mw/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=DFDCEA0F79EF1B22909DA6E2EDCD5CDB200197C1A83382ED1A2C3C0A3EDEFBAC)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/FD_fJwx9QbCGRb-neVugbw/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=EAEB6986FC76B91B05E21AE496FA668E9B862613E31DCD83E2475921CF726D41)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-appproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/YuLjt3jDQdGXjVomet_Eqw/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=1C6FCA3120CD304C4BA94D72DFFBED1A7BF39728B988461F544E4E7A59E23F4B)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

说明

* 如服务开通失败，您可通过[CloudDev云开发管理面板](agc-harmonyos-clouddev-console.md)快捷进入AGC控制台进行手动开通。
* 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](../AppGallery-connect-Guides/agc-account-bill-0000001200817917.md#section813072912208)，[补齐欠款](../AppGallery-connect-Guides/agc-account-recharge-0000001126625360.md)后再前往AGC控制台进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/22xyo9-TQIaYhS07_XIECQ/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=259294FF615690769119A153394DBF4F4FB42E01EEA50A4543EC4EFCC64C9630)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/dkRfkEVoQKCywqbahtNiPA/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=0DF256DA37D1015923807E7878DF5ACDCF04AF50A183B338B24A09BB400F6E1D)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/RKGomOPHRS-H86AFTA-rxw/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=4A2249AA32192C929C2C32F9B283543835A6E3635AC4BE26BC7FBAE58FDBEAFE)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/f9pIUVpkTBq2R1ayHV4eZg/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=5DB76FFD4BE98D2B86334CFB4AA5B1F4F4346AA4EB8F462E9B022FB6493F4FBF)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/cODR6bNXRMO2lIcpL41XPQ/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=9B4570DC3DD9D30A77B4FA98980856FCE69B74E8D9DF0762F7D7D87801E21F15)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开AGC控制台页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/VuI2qYKzSTO8oDZCBHXrWw/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=3F6B022701C33121DB27D746F36C4C47A5B06698273D6F842E1785C26F59BBF6)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KiYn6-4EQV2xYhLgHaCXvQ/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=55EBB22478B6A25E16779097942BDAACBE9EE67BDC6CB617B5DC8D37BBC0068F)

   | 参数 | 说明 |
   | --- | --- |
   | 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
   | 应用名称 | 应用在华为应用市场详情页展示的名称。 |
   | 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
   | 应用分类 | 请选择普通应用或游戏类应用。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
   * 如需将应用添加到已有项目，点击下拉框进行选择。
   * 如需将应用添加到新项目，直接在框中填写新项目名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/rYnoiIdGR3yk9KWfr_39Ig/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=7E2771A1E86BD9608AB39E9ECCF465CC854A2DFD925FC76477C3C72167C8405B)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/9s9ZTgYGSxKHbx38G_q3UA/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=AEC52B944CF8A175DF85424637AA904CAD1002DC8DE982704FB199241B86B51A)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/jwFRf23sRpyAVmhwUd_LjQ/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=84AD86C8F77126DBB83BA3AFD26E82CBE40CC74635E7F439B66FE5AF3F8AD01A)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/oQ3PbsquSWmLhLXDEfDlzw/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=085528768F2FCFEBCD95FDD741DE8635FE159DA0E58DCEE23B28BA279CCD7FCB)
5. 点击“确认”，应用创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/JPV8K8zsTwaOIc1E3hW4Rw/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=FC192E03F1141859546BD4E59785B3F3A23A1C70E779AD71825DA928D7FCA006)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/hmOu9KsVT8mFOIbvBPWyLA/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=AE11AEABF163B50F964E1BD8FE0AF8125EFC441A15E67CCC7DB3905CCCFE4859)刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/TgAKNDpmSoW1Goxv1cFbeQ/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=A777CF4E8BF02EDCEEBFBAB5217A6D08DEC98A7D79BBF0F42ECDAC596184594D)

### 将游离应用添加到AGC项目下

游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。

注意

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/4L5sv7H4Sxi0-_kjXwl-kQ/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=6BE94640CC3EADEB02B1546D64F14F5CAE1F0C51D1D7D78E23FFCA2524F14BAE)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nWRTPkFNQTWf3RKS9AX8bg/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=1B90F4AB6E532A8F5B8AF00D23C6AD4BB893F7E5722E9907CE3E577184888A24)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/JW2cV_ShS_awcuL7Cnz8sA/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=6048978A146C08CAA801935E23039A7ED2212D501C48022867E1B24D301C5349)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/SCa1bpTbRReNhNSUxQEF7w/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=2EF25488974710843162787FE033C1D2048B95F084AFC001E9C3789D81C4899C)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/5727Ms1lS4eQRe6fU47jtw/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=2A5575C42D9F61FA28E05E78F833AEDC4E07B46DFD29F0B436386C3540899A1A)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/GYlXc0mmTBa-l13z1j-P2w/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=D18196A37BEEEB1D2AA23DA8E022DBC6F948DB344D66C4CA90BB0C3084A6F0D3)
5. 点击“确认”，应用成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6jRp9d8xTDGr8e5YYxb3BA/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=947E3D9BDAF889E189ED20FD4AC61B3DED2BEA1CE18D28935E75E9B7E892F073)
6. 返回DevEco Studio，可看到应用已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/rJ99vFjhTyOjIdL1CYZvjg/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=0A7B35FA3E3E2463A7392C124CF0B85D6F079A25B5AB5F633C5B7EF103C13341)
