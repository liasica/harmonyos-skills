---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ece5238df33d88d3cc1dca8adafcdb477bd2cd8254ba0635e1824df6a992f3dc
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/vzsv15ddR8SE5JaYfSlrAw/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=50A25CD4BA800C3C623E34616CBB79DE2478DF8B2D9C36A7D1DEBB741A770400)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在HarmonyOS 开发者中心创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/oC854tjGSZWgzqMvFkS00Q/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9B2B4C072DCBEF8EECF3C67F491B3BB5012864D87BD052166BEC71FB713C543)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/s3uOqVKvTo2HUpi7cNYlbQ/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFEA0B744AD1D2C39FC70055949681753A3B0F83BBB0A09B4439A55030627E91)
2. 选择已登录账号下的APP ID，以关联HarmonyOS 开发者中心的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在HarmonyOS 开发者中心的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     **说明** 

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ubPtHf01QYWGBAobZbuICg/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=845F631867D773085E548984CD05E838FBFB0C67EA5BD5ED9E61FE32C48DC243)
   * 当出现以下场景时，您可点击“Register App ID”，[前往HarmonyOS 开发者中心补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在HarmonyOS 开发者中心创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/9hCYtBg6TUqfTO37QODPFA/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=73F92B926A8316BA26198F9DCF647B455821C59BEDF4F4D757EEAA85D8D5D9F0)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/QOHRiJLcSIOFEvHOFcU65Q/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2818FFA3AE8C4C084A384C225A4A15385EB7CC577FE9BCABF990A24243DDB638)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     **注意** 

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/pcc2hYjGRIKuZP8u8Ds30g/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B22FE13124FEBC569847F3E20D20619FFD80BA873A22503391B0644C1826586)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](../atomic-guides/atomic-service-create-project.md)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/f9wf_XM-SveKlam4zuxN7A/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D29F8337100BDEB52F00E0113E982D12E783F5348E293F92D8507E8B5BD2AE01)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   **说明** 

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/n26ifBnUSm-YlOBvejsE-A/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=F40E5C33A96CCDBE88935178C7C47788A82A87B41EF419B3FF64BCD4D8CCCBF5)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/8OCRHGSRSZyHIX_9krcTmg/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9E7695C58EF39DA24128D0E9FF209322025324B9CA99C763056CFA5BB0A482B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ugPa0fXhSfOfQCWIa0KmCQ/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B235B182BC1F8B669AB275A9E82341134118602F2176F3358BF73A7C2FE5B850)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/DjdAQaCZTg6cNBcs4Y63Bw/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF528C23BA39E4F1D003E422C23C9138D9382B2341E4648FBFEED93B8CF22742)

* clouddb：云数据库目录，包含数据条目目录（dataentry）、对象类型目录（objecttype）和模块配置文件（db-config.json）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/PJL-dzr6RaeqA3KJ1BI_Jg/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EDE61184FE325DD6B46BC47AE203EDFD49A5E67D1B51157C705846DB0F14A2B)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/q11KsyL_QqOEYCpyU3y9CA/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FA0D4A3BE63D3A0306AF05C9E1080300A5F9E78C87D6E0B42C228AE012EF671)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ibXBonpMQ-mqO2LsAFJYvw/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E07C4B2375FA3619C2F5DE9B4C47F24B8B572E914DFA6502E68F8D8FEFA387B)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）HarmonyOS 开发者中心元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在HarmonyOS 开发者中心创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/a9aQwG_zRl6R3HX4v6MGWQ/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=51A057427014E1D8EC933A43B38CC4C03909E2957062DD2E1826DBE24048A683)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Sxbs6MmFQWWyql9nlDEKuQ/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D93CB381267C32C9EA8324946FE110E8D630C2F64E54D269D3C20705D106F58)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明：  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   **说明** 

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/KmkCAu2dQviis20EOH-csw/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5868E42D6F0DC2B73DF21CD461BB1973C3F38C8069E6BE7B65A558C06707C024)

### 将游离元服务添加到项目下

游离元服务指未关联任何项目的元服务。创建工程时，如需要关联的元服务为游离状态，则您需要将该元服务添加到您的项目下。

**注意** 

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开HarmonyOS 开发者中心“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/1mmp1UUlT3SG4z65EzUqEg/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=510AF0E676918C02B4CE5CFF4681CF77D7183A0E65C27248CE54928CA5C0AB1A)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/DzfB4DACQD2-8BJxb_vj1Q/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B12A39AE5F4CB2970B6732FD261DBB2D0BB0F696A6ADAD559D55308ECE595308)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/AT4hOLjETWmIFYScv_VaBw/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B3EF70BDC500ED445E3CAEBB5DC23C017A954CD0B9EC0D588BF500E7BC9D069)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/X-uar0o2T5qx3OqMPOssLA/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E36B83EC33FB2E7B19349181DEBFF733C51CB088765BD974541988416CA010AC)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/UqFXbvtpTcupCKdLa57IAg/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AACF5AC55588EF8FF58A4C84065B54AF244C0AD682E63E3C2CC91C677610345)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/_17uC6seTHyC9bQjampOLg/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC34471B9C801A8A2697800BADBF5874627520DE9A7542ABEED6E049EBBF2349)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DYodeTZLQ1SEPJ9rw8HcOg/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AEC963920C968E38DFA8B1B46CD6B4145B757AEBE4699C982CCB80E68DFF3F5)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/u_5W3ZnQSASzWZMaQUq0ww/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=091F9DAB7399787A5BABE123457EB93BA1C3AA25A714E69AAF50FB6205596B4A)
