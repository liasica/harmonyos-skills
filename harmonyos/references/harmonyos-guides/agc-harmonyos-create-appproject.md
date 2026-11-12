---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject
title: 创建HarmonyOS应用工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建HarmonyOS应用工程
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:345bc52441b2e04b381bcdf406154ef0715f95a80efa40cb0de8fdd51fa4c686
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

   **说明** 

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/iglupTfxQo6FdKEKDDK_OQ/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=846F950AE562600F623F433440A869B5BFA9E5956A2E0ABE7852F2517B93473D)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](ide-create-new-project.md#section181328285169)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/x2b8THTDTiumnIz_nBxNPA/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=179EDA347F56C7EE178362B36FB455B260DFEFF4A153E379D02BD37AC74E7B4F)

2. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在HarmonyOS 开发者中心创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/oES8CmdvRPivUJFrrjyEbA/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A55E99F61588F85F36DF8DDA03BB1D82CAA35E73D8FC1ABDCEBDFE785570FFC8)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/uJMAemWCROG9h8NzKpf9jg/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=31DF03167D554B9E4A70BEB605F910A737E64BA32D449945CCE6AC64305CB0F2)
2. 点击“Team”下拉框，选择开发团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aX1dcwBnRE65pxQ3EVqIqg/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=178AC8A0DC5C6E920ADAE120B5BE6A811C9BBB3D3FC9093673D2F2498496359A)
3. 关联应用。

   选中团队后，系统根据工程Bundle name在该团队中自动查询HarmonyOS 开发者中心的同包名应用。

   * 如查询到应用，选中该应用，点击“Finish”即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Tij04ZO-Q3iKgsAVfeMvzw/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4344D9E55F4ADBC0175A1DB16C9E9A881BB31D343C48F2EF33A4EB0B80727314)
   * 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到项目下](agc-harmonyos-create-appproject.md#section152521927193013)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/GMeDlIoLQ9mENpA_Un5TsQ/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E83DCBBCECD0B319194D2FF3C2163836F331E106625B47D4A55273AB77662AB)
   * 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/xugLKBUgTfSWDEf876MIEw/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=61F068235FE96E74BA8B47B4AF77811D7DB2402ADBFA093F3CE5BBDEB99CE5BA)刷新当前APP ID列表，即可看到设置的数据处理位置。

     **注意** 

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/xnvnywtNQYqGmjsBubX69w/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FA6EA3165E34F76FF1BBCD807291D8B5CA499A3644442605C7652D55123DCCF)
   * 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与HarmonyOS 开发者中心同包名应用均为HarmonyOS应用类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4Ddo5hROTYWb_gJjqN9yJA/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F6940E898856FD4B18CE2F01253F12B4366EB9CB4B66D309CC80A7183F01DD7)
   * 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
     + 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
     + 如包名无误，则表明当前团队尚未在HarmonyOS 开发者中心创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往HarmonyOS 开发者中心进行补充创建](agc-harmonyos-create-appproject.md#section397317130308)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/E5PspwccQiitZBRgGA7TdA/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F9C3E7BA13C7353B59811ECD71320A51CE4649395A8A7F50A5C10EDDBF3C74C)

     完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/zKrTtLwRS5qMuKja86nywg/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=46F333DB3CDDC3D01B487F7C3F5AF16FB521F68B034230173EB0AB1FEE8BF9E0)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。

   **说明** 

   只有账号持有者和法务角色才有权限签署协议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/cE4OcjU8RyWW60NJwLQ6Ew/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AFFA54521BD1B9BED237582138306B84801BAAC34CA61030EA4B1F6619E5042)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   **说明** 

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/eGmG3YW7RrWkV98S8wVUqA/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B85DBD753CA6289D6EBC90D4EDFD84AB0AC2A9BFE8295DE8C8D8AE4A6A45A7F)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-appproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/CkE9DAbTTauvM-v8Tqx9Pg/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CA7B1024BAC22FB5EC8E906DB330C71CE8A8E030688691ABDCE993C7B62BEE3)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

**说明** 

* 如服务开通失败，您可通过[CloudDev云开发管理面板](agc-harmonyos-clouddev-console.md)快捷进入HarmonyOS 开发者中心进行手动开通。
* 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](../app/agc-help-set-balance-notify-0000002247531780.md)，[补齐欠款](../AppGallery-connect-Guides/agc-account-recharge-0000001126625360.md)后再前往HarmonyOS 开发者中心进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。

“Application/cloud\_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/O4o3pdS1TCOg64pXIKh44w/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=03739EEE5B9EC08F466A180280330353ED43A764572E224F1592D0527CD1ECED)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/w8TlTejTTwabOWmqpfWbqQ/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0340E25C0F9452DA35BEF1B120BE760DF5979CF016D10448614EED9E32259F0)

* clouddb：云数据库目录，包含数据条目目录（dataentry）、对象类型目录（objecttype）和模块配置文件（db-config.json）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/fSazQS_RRRSTwtVsViGEuw/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=704238D5D344BE0D80706E7778E7DA8CBF195B798BF629822FC522030ECA3F91)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Bi1F03WtR--hLVgRJULTIg/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=077F25524A757BCB953CDA13F67D3AAA48F34622129267026153BF2D278D51B2)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Cx0PL-ggSUeJF5rDF0lfCg/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBFB1E768798F3D8D3091A2771C88BEF02CC92E287DD438B74460CC0480FFF7A)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）HarmonyOS 开发者中心应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在HarmonyOS 开发者中心创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开HarmonyOS 开发者中心页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/TIABxRd9RMeiY3CIttmaQw/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6B88A9BE3ED966B9E5F631B29E69EB17DBF1085C4332EC7836E8CFFC03083A3)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/fQt-5_kDQbeg0eAQiLbCUg/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=24C7747B435A98B834996763BE84D45C4E09C323FD1A35521082E353087289D6)

   | 参数 | 说明 |
   | --- | --- |
   | 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
   | 应用名称 | 应用在华为应用市场详情页展示的名称。 |
   | 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
   | 应用分类 | 请选择普通应用或游戏类应用。  说明：  应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
   * 如需将应用添加到已有项目，点击下拉框进行选择。
   * 如需将应用添加到新项目，直接在框中填写新项目名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/JZeX3BXOTAy7CiKMVJllDw/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8D3EF39FC3F4703EBEBED3C2068F056C32FB6293E59ECE0E44DB4C6F1C7DE7C)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/JnXv-MzEQg6XR20txIvfYg/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE88217B1D5A4C746F98795285A2B0C4047BA2C5C1E51C5D1F68DD3C0E6CF43C)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/9S3ahW_oSBCYNEQKmne-RA/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D4A44C7ACAF553F42E1D806CCEED72538FD0C2DFF1EC87E8D7851C8895E2FAD)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Cvtpv8OPQ-qq493d60ODjg/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=907CF3F7A965CD631AE57B452E7ABC851BDCDA01E07699F91EB0C0BD8BC4C4E2)
5. 点击“确认”，应用创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Msdvr29nSQiDI2WhfrEiPw/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B1363B144591C26804C9F7A6B6D9078D0BF2BC1F0619FD54C2F604677330AA3)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/XxCSX6u4QtixGlE2bspRBQ/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C9EE217EB4F3C37D95CCC2D6858B0DDD82D731CE829873BC5FB22BEF72DDE01)刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/2T4TaGx1TEmDjpGrGrmQHw/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2EFFBD8D8319E9E9718F702DAFAA67DC159AE4DAB0F92B42445B06C2B502267)

### 将游离应用添加到项目下

游离应用指未关联任何项目的应用。创建工程时，如需要关联的应用为游离应用，则您需要将该应用添加到您的项目下。

**注意** 

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开HarmonyOS 开发者中心“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/139LsyZTTe6otUXfaw0wPQ/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFE10BC46C30DDA0F147B94AA47D8FB51AD8595E9A706C41206C4AB2B33CC0AA)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/g4LB7OPsRtWiDpEzdMJiaw/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D38322DCAB6D74C3CFA81A2BBD137EAA54ABE2A3018F99742F9C7F42D6BF2D16)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/tHyQx5voTx2AkaSlgcKm8g/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F636360D7BF0B23A6023BA023E20AA71DD3391B465042ABCEA1C0B3D94D9A78)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/GeUpnTklSF2717agTQJvrg/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4130BCFCCF7FA7A2415679BA2E5AB0CE6E9550183C51DE2096122721D99C0B3)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/j2HspySERLisMfvKaKXlTg/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=71BEFFBA095E7152C0DF028E0AD19BB633AFDF242EF97ACBF72E36F516C7617C)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ZXNsvFbjR1eyls9ZTHwCFg/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C052ADE58572D1929CF5087DBFA697F0D4B29EA8D56BE100E00A4D3BFCF60B0A)
5. 点击“确认”，应用成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/2r1pDfBDRjOXf0i_eFrU8Q/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A863B64E80605AF9B8A0D54B921F3BCF006C2656FCE3CC8C94D7BA04540B265)
6. 返回DevEco Studio，可看到应用已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/SUyzm1UdQA6xDDjUb0oXdg/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2182B7A52B9DE5E5822ED194A31F133930E7204BEEF52DE1D114BE3E8FB27F11)
