---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject
title: 创建HarmonyOS应用工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建HarmonyOS应用工程
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:00+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:96493fb24bb1074713b0116d79012d3f345a8cc7425b27d3395a053f0d6ad38a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ANFw1SL5SJiSPciSegvP0w/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=6744185621DAB7D7E3EFDE04BCA4822636CBAE8044FC67FFA8A887D7143A2C32)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](ide-create-new-project.md#section11644183711342)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/XIO2YyGQRyecV6JBtrgTaQ/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=AC81298C2FB62F029D7AD0CC3A33B70A2DC2FBBE7F9551A9C5CA7F51359882AC)

2. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/VtsWG63VTJ60742Mvmmlzw/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=7031038360D659CB8D14A3BB329BFD78998796D2FFABAF95708D22A6313AEED0)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/Xgt6gQe4QKCFCtYgnX5-3Q/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=381D113F7B4E5D8680531D76179005A523FEEB0318F2740E8D44A18DAA1B43CF)
2. 点击“Team”下拉框，选择开发团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/1da18QuYQbus3DeaK5Asww/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=185FCFCC3FB2BE5244E91BC5D838E6A810A7FA2D2567BBB213AA67EC3CC950D8)
3. 关联应用。

   选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。

   * 如查询到应用，选中该应用，点击“Finish”即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WPTEIhWGQA61iSJxsqZMAg/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=68A68FD52222958904C6997640DEE2972AC93089CE17F69DEF2A0832A2CFB9E0)
   * 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到AGC项目下](agc-harmonyos-create-appproject.md#section152521927193013)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/HE2SzRQ-Qd-u1bzJ569JxA/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=A51C344598F42DC374ED066B553F0CE19A11E3DA072A9263EC4D0056A59B87DC)
   * 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/6bMEnkfIRvWJn1Q7NvHdpw/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=E9AAD36A046C51EEEDE2BC3F21E667F146C6792788C2D1AAE327A4D65D014790)刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/l2MDRy3BROq36H40Bprhzg/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=385AD84741C5CF00489BCA964F678698E7585D72CEA8B1F270D3E0D9C943DCB4)
   * 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与AGC上同包名应用均为HarmonyOS应用类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/TOEkh_sjQe2LYhPY06C9Tw/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=E6B17506AAEA92465175D83C92F367F6BB050F74E86236B872EEA80834B5AFFB)
   * 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
     + 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
     + 如包名无误，则表明当前团队尚未在AGC控制台创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往AGC控制台进行补充创建](agc-harmonyos-create-appproject.md#section397317130308)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/k4T0IyiOSOqiOyE4DkzJBQ/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=FEB939DBA0EAC0830D44325ED3DA5D9548C9F54C3E61A91B8C193F5848B21529)

     完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/uaTQNao1RSOOTDFyGZ_5nA/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=9FDB3AC4287DC7B36C8778986F29663F8621A20FC0740462B407DDB313A5530B)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。

   说明

   只有账号持有者和法务角色才有权限签署协议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/yJw2oFOMTX-AwyGpK0aY-g/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=F11EE5FF6A8905FF0384ED650CF6C248DE99F361B353455EB9E9A4D29622DAA3)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/gucY3R_mR3Guea0IMFfJWg/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=173FFF7A6DCBE0628860B00E2C2926B95071CFC1CC0D5B2D6D81D90BB79B1874)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-appproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2x5tIjmmTwe3wUi3ZC4dJg/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=57F39DF069A010E03088EE6E61FC3AE2C1D76E1B6E353A66B92E171F66A53461)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/oxko-DneRP6wAG0CoH9bDA/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=904C6890E7B6145DB0295EE79EB4F05B157D0D0DDA55DB043809FDF99D3B527D)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/XtP6fojwQ1qkN6D8wGrbPA/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=E7A8BCBD046E8B805C6D56E24B0D21F38A498B7C92A90E63082AF882CBA8160A)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/VV6a0oJtSmuXgXBwMtKb7g/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=0755D1D4E48D8644BBC8E7EC39F3BB41AD74EFDAC2793DB8247F40677E6105A5)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ap_taAV1SuWHvLKLLqr0Bg/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=554ECDCF287A7E31A43366B215BD102D150EA3379C396049F37BFC08C896CC4F)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ghQXSg3bTKe0od1Cfe86UA/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=D6EE04F3F84D302A11083F79FF80AB20545F1F5342D72156951CCB4BEEF914DD)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开AGC控制台页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/fImOfH5AS42KVpOBaOE61g/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=E49137936F5139F90BC4E5A98E01DD5A08B7C582A92938327D1F88C3E3B5A1FD)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/t2NRSJyQQrqbHykVNf4E2Q/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=0A1613AB68323E8D05D149F8E111FF06DE8F994534D65243B4EDD484F96F924C)

   | 参数 | 说明 |
   | --- | --- |
   | 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
   | 应用名称 | 应用在华为应用市场详情页展示的名称。 |
   | 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
   | 应用分类 | 请选择普通应用或游戏类应用。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
   * 如需将应用添加到已有项目，点击下拉框进行选择。
   * 如需将应用添加到新项目，直接在框中填写新项目名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/AUDOdNyIQX6jmSAATRSiMg/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=B351C62DC4B98A50D4BAF5FB2187D4ACBFDAA69B4F319E7410FC9AC8019CE02C)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/hISkXzb4S6yGZzauOKc4FQ/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=6D4A5167DF0E839FB61546E500F5AF214401973142EE28EA3A9E1F2983037A8D)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/FlBLe7cBTnmWX5D9r-M32Q/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=5E608DD4CFF7F55FF564429FFEEB47EC7914A2E76D3CC19A1D1FFEC45AD44755)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/oe-3svzNR4q12qIVXmkV4g/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=4FFF7427AB0CDCDBAB8F5DBC178A6F341DD15F112916EE7262FDA370BA600803)
5. 点击“确认”，应用创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/d381uEMZTpiqEekyk-A50A/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=7DEDCBE9D8E85B4113FD863CD70C89ECE0373998590A90EFE397867B36A2E1E4)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/wAQmabI6RYS5w0r6anw_2Q/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=D6CC507834E0A73A39DA040F7C06A1236FCD101D69960033EA540A63B19C1FF9)刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Kag0s08cSoKPd7m_GNWT5A/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=979C15FE9CDC9AC567B89AC98188EDC54868AAEE6B11FDD9B9723261A022C077)

### 将游离应用添加到AGC项目下

游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。

注意

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/feXMQ5OmQUCVwnPaNXj1Dg/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=9AC6E9448D3E9D118930D96C4F2214B1D4C9CB5F0C58FE6771F4BC3826091A3D)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/uINW0BuQSVy_N66WZ5A1Hw/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=EB0FE3C0CB0DCDE47641CB260A24AE9C3C714DD1CC0529A73D62130533C55149)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/aYpD4O1aRRO50Ikx67LusA/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=C42E8CCA9925BF2E4B56CA03A33F4A7E9C63F49F7364909C0059A317EDB31271)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/MVcDBafBS3-aiucZJy7qog/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=B48308F6DA0EAC24C3CC2A733B61885F71AFF7EBFA8751A2BF262BBD892FE0CD)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/QWhaCAj2T2SeMbPapWOXwA/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=A1CD92E540906844EEF6C0EF4302EAFECC35D051097C180207E0ECE62302764E)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/lLY2mWMdS4mEk7y5tWG3qw/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=5298D0BBD535D3EDC9AA5CA1D23C7AB45DF61416467AA623F152232662E9665A)
5. 点击“确认”，应用成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/ptgWTDj9T8irFLqamDMoeQ/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=8FF2339AF845652F3481FB9AB1D99D1EF83DE00367B1600ABE390BFE77E303EA)
6. 返回DevEco Studio，可看到应用已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/5f5-brOFSOSwXFi5fefYTA/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=0B8CB369F4C659E5B11883F5FE18BFD5F26A8E07BD6DCA247884A400F170AF18)
