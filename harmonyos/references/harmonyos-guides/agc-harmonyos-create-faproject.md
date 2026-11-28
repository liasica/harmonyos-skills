---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:5a70e28b21f539a920055d6f6b83f39412434ab9724724f4d3fe167db83fbf0b
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/tpsJQAdhSJKXFrv4tnn8gw/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=9ABCEE129B85A100E1A199907F49A7555C677A08DA38279A0B64A3AE2339E578)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在HarmonyOS 开发者中心创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/zH1qAuQjSquowVHWk6_vGg/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=449EC023C8DD1C49ABACBDFCC7AED6E274D7BC53716B5B7B3C2694AD3F028CC0)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/TjcuvnneS0StQ9aKoH4srg/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C8E1FEF110BB09DC448A173DB228A6564AD5FC81CC88BEE1B3EBCAC8A3F4ACB)
2. 选择已登录账号下的APP ID，以关联HarmonyOS 开发者中心的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在HarmonyOS 开发者中心的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     **说明** 

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/fXDmWeN7SyykEEC9pgsZKA/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1716D268DF225451AD23E14D33D3137F494317FF738D310710FC02744130D03)
   * 当出现以下场景时，您可点击“Register App ID”，[前往HarmonyOS 开发者中心补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在HarmonyOS 开发者中心创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/S5-LKC2ETkm7Rha90cEOpg/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5948EDDBA0E766EEDA2C52704DE04F5C4437A54EBC13C69FE2ABFAF39F3C77C)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/nBVXiBS9Rym7BktP51WMCw/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=286F49708B66E429479BD56A0791515A46BE43B35E3B4EC66A8214931423A399)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     **注意** 

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/7UOD5ZADS66fQ47yZELgaA/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0F04A938A7916361DEC31D5AF97A97C677AC75755715A831AF498D9D6A8764E)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](../atomic-guides/atomic-service-create-project.md)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/7-etsdceS6WikejbKxA68g/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A30A1AD5C7A5D6C9340E5565425328A9C974389A569E7B5DAB2C8CA1EF0E27F)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   **说明** 

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/v0XPRUmQR7ijcEZvrE6nHw/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3AE3EB9262CFABCDC96CDD9F20177C040C730D079C2C6D64B65DE5F09BF52D3)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/7fYxHKNySciDdcJBIU12lg/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E008A04C4E2792B1C180CF14EBCE985DD8A72C8458DCF54DE8EDFB8876FA6077)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/baL--366SzOzFR0SLMsWZA/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=90AB299223F768443EF2423A636364C319F133A6621EABFDB2D4404F7DF0E297)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/WIIE8E3hSb20kVQ23-EN-g/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACB617BDB64CE145AD76FC4CE9B408F1777ECDA8CEB463567C9F46E3EDA873A9)

* clouddb：云数据库目录，包含数据条目目录（dataentry）、对象类型目录（objecttype）以及云数据库配置文件 （db-config.json）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/4uX2OOneR86WC7iQdEFXhg/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=266D52D91AA9424897DB458FC480B56BB4A1579C8BBE7C2EF1F16100F156F458)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/vfV5igFYTwKdpqZ9naGQHg/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=94E5F82FF6F8064C0F04A599F3A59CE36DC08441F4C14D14EB94266CAFB4E995)
  + db-config.json：配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/oPS8Y8dsQLyOb7AQD-Jrxg/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C847FC271CE8FC0D9AE1652566B8A066B5C1EF360DB54BDC06C93EC5F99D103D)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）HarmonyOS 开发者中心元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在HarmonyOS 开发者中心创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ZXRq_I4gRIW3kh9FuEYl-g/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=05A8130F1D63AEF12046B0FB2E44559D486F168EBAA170420BD09CB7A549A58F)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/nm-DDlYnTq2-ChZa80WALA/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=739D54CCD091E6FF89A9CCE3F65EBF9B9510FCA3D6664CAB0C4F25487A4FA7F8)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明：  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   **说明** 

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/uEChsG3HQF2gt-yxbM3PMA/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=41DF590723FAB734FC5A21BEE655AE0E46624E5FB85FE252F95FFF12BF7FB495)

### 将游离元服务添加到项目下

游离元服务指未关联任何项目的元服务。创建工程时，如需要关联的元服务为游离状态，则您需要将该元服务添加到您的项目下。

**注意** 

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开HarmonyOS 开发者中心“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/mspL5Cu6T-S0BM6L5l7Law/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=1279F8FAF6973C335CE18F5039195C0E53DBBA42EC0D7DD35338E344FF5BA37A)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/QZktf_nhReierXZsgSSa0g/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9A77F06F288DAD62CDE0F52E5231E7435DE43BA30BC0BC5EB83289637F4610B)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/OfugI0boSHSRLXHZQDN46g/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=907583568C0CAF7FB5DDDA6E1BF467732C5FB173E002682C35941478E40D2AC7)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/GUmaydCMTD2KI1V2-RvlsA/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D8C50725B5F4EE75265A805579B5083B3649E6824A119455524532D544C89E3)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/XMLm3yckTDmNtHm9spkJ7A/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6739587BDB57601FC0BF0826766DB884EBBC94634E225C5F6C382C689FFB810)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/rs-w5h5ZSliS2nouR8qwDw/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9B5957FB00A0B8C21676C500E912AEDBEEB9E93711B86AFE49B127A1250CBBA)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/luRgB1BNQvKYe1wJvYWx2g/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9A81209FC960AAA38412B1712D0298897C51C136F54DBC0F3CCF00F6C8B7D7B)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/hVLCO7LYTSupcRdfdMe8oQ/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=967EBA994031FCD3560E5E78591B321489D7E100A74434465E44A1EA87B76A56)
