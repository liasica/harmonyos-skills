---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:59+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:51697aec82b3e355a2f5e742ab47e4cfa78c043a9f2a162ae727333c2f1b01fa
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

   说明

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/MULC9Jg9Qj6Ed4nR88i30g/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=F708E43390B9F093B6765D90898CF6EFCF0B0F9180382CC4F29A43FABBC1C911)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/3Sp9SxRrTRWtOIH-EJ1uXw/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=0290DDCC19A74C41ABF44BE91C1111B5C0E969AE5CF6F9A09061676B1715B7BA)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bM5ge3SARJiFu-vCZSxiKQ/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=A5D1C8FD314098DC70A3256088550B8423882BBF5898C9F72484D9CB3BB4ABBC)
2. 选择已登录账号下的APP ID，以关联AGC上的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在AGC控制台的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     说明

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3XvMKG6wQtaMkNjO1H6zeA/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=DEB618784FDA72E859F38B6B099493F9962A9D1088E6A1925199DA4CDB0BFFCE)
   * 当出现以下场景时，您可点击“Register App ID”，[前往AGC控制台补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在AGC控制台创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Y0W977lqQp6fqIacwWw9OA/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=CBE467BBBF770E48E355A5E47C280EB16D9D879162565BEDFB6666BA21E142AF)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到AGC项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/J5sE7hseSayyEnNFJfqCjg/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=395975C8E34D9AE50A9F85BD54C137E18209E40F56D871D982C6CDB4AE2A018E)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7pn0ci1WS6GTduMWIccT4g/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=E37F623012189652EFA639F7DBF8E6C77248D83E1A6BDF3998930C5309C5509B)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](../atomic-guides/atomic-service-create-project.md)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/3eCAOqW5RvaUlj_diPndJw/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=E14963CD83989DF9025B41FBE37B87D3C1D7F6B1714E47983CEFC9E7805C8FFD)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/dbm2tGZhTH-NlHQzkwo8Yw/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=21054A09EA79AC1396E58FC439C958C7F49A84BA357413C6D581A3445D57F6ED)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/OaSiBLjkTgS-XtDm-2JkcQ/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=E64F8963A10DD65F967E9FC0E02D399CD6F3301E65D2500BFEB31AF09208CB06)

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

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/vZLEsc3mSrWFkjcV4RUnRA/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=49D9CA57C92A57D8E13F6CC0CE37E567143560210A6017D62ACE33627C6EC33F)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/QnoWKgLrRqGDqxPVFz-Hyg/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=3001193D380BB960BFD3B4088EC6961D1C6C3BFC9366862AB34DC7048867F819)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/59wihwq9Q7-s08Tmp8hJKA/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=B1EB5F552B47D8EDCB6B1A06D126C27DEC5828C82E15C8AAF9ACDF49B47240CF)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/m_loF6NLRl-5ANUgk_fBrw/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=5AE67CAD132E4CED9DE7F8D5F44C3C5C14B24BEFD0019DFEC9E9A2483B32863E)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/m-K0lY6sRMSs55jNtFxPnA/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=963B66DECC0034CEB1C0B8237EC6A5A2908AEB380379F49F25EE43F9DAD796D0)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在AGC控制台创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/r1k1dy5bSqWo-d5-GOl1UQ/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=F6F9DACB7325D135B4A93D5260523DD09B1221595FC25F77A20D3F7D4D4CE888)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/tl8lrCP-RwOLOo23KpqxrA/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=BF329C2856E999D4E9779AE1F55181FC690729CB2795B088C43804D31297EE80)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   说明

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/UbPB4cWhRwqgXCYrJt0f3Q/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=A2561F7101DAC5DA377CBAD1E5602AA388805D283B1C98C98E1F161A50DE5E39)

### 将游离元服务添加到AGC项目下

游离元服务指未关联任何AGC项目的元服务。创建工程时，如需要关联的AGC元服务为游离状态，则您需要将该元服务添加到您的AGC项目下。

注意

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/KS_rwA6gRsKvBmqQwXHUlg/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=B3EE69F7D74B58910E6BFEC6881D904AFB2C394A2EF42B9CBF55BC78DD01A192)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/dOADocQSQvenVvutELVJig/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=2EE1F297D543741A745292DAC39E88779252E32128B26D20F3052AC13D9608C9)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/XDhgH0KFQEuJJ3gI5ky8Qg/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=C6946778837643CCE6BECEB7ABE63EC8C06D6278F86882E9FCBCBE5B2387A109)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/UlnO1atQS3qe1rASYRmGPQ/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=CD428FDE6C0391B678C4FFDB300CB0D2F8F70BFC07C43C349C6D3E3F8CA1B8A8)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/OEfcaOGDSAikC1x4rsroQQ/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=9C75759FE06074CBCE4E88932307FEE703F29380B6CA7BFE4A3D8E9C99BB7908)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/PVKodkrjTx2yY0Sm9UR1KQ/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=8B6C090FDD7F7DB21E3C8C05215D4BF1994BDBE5AE118437EA536E6AF068939E)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/bZs9DjgtRxWH853-_ClkWw/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=5EDEE907EE19573F3AA7F600F5F86DF43694586FA530AB33FEBEC12ACE25FBFD)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ZcMvO7ItR4-7BSAMDKUyFw/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20260429T054456Z&HW-CC-Expire=86400&HW-CC-Sign=951325E99520F91BA0EF853946A5A543A29A061315177A6B306408E4D060DBCA)
