---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:f52fa2c01636e382d5c60dae7d76259e13f2ef8810f893751ba3b6de5e1f2b16
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
2. 点击“Atomic Service”页签，选择合适的云开发模板，然后点击“Next”。

   **说明** 

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/SaF4QnXAQIajZsKBYbXovg/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=694DD9F1FB20B712FD0763FCADF695CD9F6ED6EC2FD3CFE7445BA57506D82984)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在HarmonyOS 开发者中心创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/QpNRM9o5QB-uFVpAeppfUg/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FCA9E1375DEA4FAA9FB8E931DED2B93E528DEE44D37E999334F582FB0EE95E6)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4CZWz0CjSb6NPPL9ryPQKw/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DFFD5C4F571A7D353E5739B9143E98B58A0C3AD9C0F82E31B7DB93A5C5DA576)
2. 选择已登录账号下的APP ID，以关联HarmonyOS 开发者中心的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在HarmonyOS 开发者中心的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     **说明** 

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/45TAgqdlSnm3Dwbao8qYhw/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=85ACB6488C167C54821D756F7531CE7441A5B68BFD4AB16FF6D5DD415226F81F)
   * 当出现以下场景时，您可点击“Register App ID”，[前往HarmonyOS 开发者中心补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在HarmonyOS 开发者中心创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/nes-s_0tQMupLna_SyjRIg/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=FACD797CE4308505732F93063450CDD46C6632594E23FD44D7EE06E259694BD2)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/D2azxfhSRISst9kbH_PYcw/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=35EEA2578700E28F68C716EA11824A27FB8A63B08BBD9645C19E932933C14F77)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     **注意** 

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/MB-yuZ_mRjqckhKXLG9maw/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C01475ACD22131DC785F7E06874AB8A33FD4EC70512F04B7A0798B20C72C937)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](../atomic-guides/atomic-service-create-project.md)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/OxOCJ5pES9GViq7Rl7HXow/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=109E09BBC6BF65FDCD18F1F2E0D332314AE30E9249971A12AD5B940F465CB532)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   **说明** 

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/u6BdtaekSCCOeJKykAZOtA/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E54F8E77C438F746CB93C5B809D39935949FFFA0C3575AEBF806DF473003CFBA)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/QqPxLe-_RYSt_3I3YowA2Q/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F7509E0F8F2FCBED4B62A9ACECF5664D69128FF00F5640B7608DA9C8DF40297)

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

“Application/cloud\_objects”模块用于存放云对象的调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/4gCsWI_3SWeZzjPk8SpCxA/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=96A9056DD817297E3E7375834F62FD9BD3FE7586CB6C3BE88EA2821895CB2B2C)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/BTic_jz_TeufU1wSmw81jQ/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E698D234285B43A93E7380502B3891799E5F5B93C217A3D9BE0B195E66EBF4F)

* clouddb：云数据库目录，包含数据条目目录（dataentry）、对象类型目录（objecttype）以及云数据库配置文件 （db-config.json）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/avRu4lvTTqes6yne2ccUlg/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=989F19C90BD84BCE4137C097B80755EF653D1CBD48D85634126361F8524638F6)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/JnMEaXfrRd2IcTCbKDjL4w/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E42CA52E1CCDEB49F14C056332C2B433F3BBD7BF12ECB0B7BAF840BA0CCEF975)
  + db-config.json：配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/GkagW6ujQvaATZC9llsMcg/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=729C6DD9555E7244D91DDEBBD05B1064BC93A114D5E5AF85917D86010ABAF75F)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）HarmonyOS 开发者中心元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在HarmonyOS 开发者中心创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/xi5XAfFjT1iVDeXkvmeGLg/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=842609CABE07C9D9680F010330C4E9E8C707CF08ED8393DEAC9729AEA1CC48DD)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ymFFw-nwQMaOOApjiRoaNg/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E7038DC11F181B6D6A3DC2A5D8C3CE76394B6DC2C279BF7466D9D2CB78DE01F)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明：  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   **说明** 

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/LmnBsAwmRIuBBZbvzyk_UA/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=0010B7954FF136B03C41A2D04CF4638F67D185A10B5AE8DE5D71BF84C29A60BF)

### 将游离元服务添加到项目下

游离元服务指未关联任何项目的元服务。创建工程时，如需要关联的元服务为游离状态，则您需要将该元服务添加到您的项目下。

**注意** 

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开HarmonyOS 开发者中心“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gihQfLbiSjeEvlm4IYhLXw/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE4FBB2DA88D14D912CC38446656310FAE380E117FF33A43173FB783B3DEE9F0)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/qJuGcBhjQbuCL6OeDSSgnA/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B9F0B20E7C600BFF2416505D53EADE0E5A02777B59E46FAB8503490ABF5B112)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/AqnA7mU-R2SedsYHeFA5Xg/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=88CF353FDEB46313960E5CFB8E9039023019AF47F9F33EC98BA5E39C1E9A5476)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/shLpUSpMQ9iVUdAIkbS1LA/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=5600B12E479E95EB38473F23A574DAB1D8397D4D8181374BCA80588329E3653D)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ZFU2H0BsQ46B3TcZal5e4g/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7422F0F213FD2B8DF62A86408EECF539C4097117386071239F923E3DA73422DD)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/PMlMw6JUSe6hxJFBprFAoQ/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=3752F4A8E43A6FFF775DB659D7D11B2EC69E954A20C2F227D8A2E7073F5D2459)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/WF8wQ66yQI-J2-grS2QzOg/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A22BAB95DFFB9454560F16AA3AEEB3F81541E64FAA5AA22D3FA13E62F951EC6)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/XThjv5ZMSt6uuoERYs8aeA/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A52B76AEC556579C22D9D07B776CB1473FEAFCD1B774E2C0B460449DD851CBE)
