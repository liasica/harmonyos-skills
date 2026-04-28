---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory
title: 应用沙箱目录
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用沙箱目录
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8129f8f97c20b53f5fabeda873653258965d45edbe172d4915a1dbcbcbb680d8
---

应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。

* 对于每个应用，系统会在内部存储空间映射出一个专属的“应用沙箱目录”，它是“[应用文件目录](app-sandbox-directory.md#应用文件目录与应用文件路径)”与一部分系统文件（应用运行必需的少量系统文件）所在的目录组成的集合。
* 应用沙箱限制了应用可见的数据范围。在“应用沙箱目录”中，应用默认仅能看到自己的应用文件以及少量的系统文件（应用运行必需的少量系统文件）。在全量挂载的设备平台上，文件管理应用可查看其他应用存放在el2/base下的数据。
* 应用可以在“应用文件目录”下保存和处理自己的应用文件；系统文件及其目录对于应用是只读的；应用若需要访问用户文件，请参考[用户文件](user-file-overview.md)使用指导。

下图展示了应用沙箱下，应用可访问的文件范围和方式。

**图1** 应用沙箱文件访问关系图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/AcLeRNYQSryqlPWmqsxvFA/zh-cn_image_0000002552798612.png?HW-CC-KV=V1&HW-CC-Date=20260427T234110Z&HW-CC-Expire=86400&HW-CC-Sign=7C1E48862F62FEBE725ECD5C506798F184992987E2A39E2951CAB9972819FC71)

## 应用沙箱目录与应用沙箱路径

在应用沙箱保护机制下，应用无法获知除自身应用文件目录之外的其他应用或用户的数据目录位置及存在。同时，所有应用的目录可见范围均经过权限隔离与文件路径挂载隔离，形成了独立的路径视图，屏蔽了实际物理路径：

* 如下图所示，在普通应用（也称三方应用）视角下，不仅可见的目录与文件数量限制了范围，并且可见的目录与文件路径也与系统进程等其他进程看到的不同。我们将普通应用视角下看到的“应用沙箱目录”下某个文件或某个具体目录的路径，称为“应用沙箱路径”。
* 开发者在应用开发调试时，可能需要向应用沙箱下推送一些文件以期望在应用内访问或测试。可以通过DevEco Studio向应用安装路径中放入目标文件，详见[应用安装资源访问](resource-categories-and-access.md#资源访问)。
* 实际物理路径与沙箱路径并非1:1的映射关系，沙箱路径总是少于系统进程视角可见的物理路径。部分调试进程视角下的物理路径在对应的应用沙箱目录下没有对应路径。

**图2** 应用沙箱路径（不同权限与角色的进程下可见的文件路径不同）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/TrpGNUwRTMCvUWrpXe7Nvw/zh-cn_image_0000002583438307.png?HW-CC-KV=V1&HW-CC-Date=20260427T234110Z&HW-CC-Expire=86400&HW-CC-Sign=4C50EB95B77BFE24E3FAD6920070BAB765EDC4E90FE956F471D3D40033E4F9E0)

## 应用文件目录与应用文件路径

如前文所述，“应用沙箱目录”内分为两类：应用文件目录和系统文件目录。

系统文件目录对应用的可见范围由HarmonyOS系统预置，开发者无需关注。

在此主要介绍应用文件目录，如下图所示。应用文件目录下的文件或目录路径称为应用文件路径。各文件路径具有不同的属性和特征。

**图3** 应用文件目录结构图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/xY-oNBF4S0u0A2k1OLIYcA/zh-cn_image_0000002552958262.png?HW-CC-KV=V1&HW-CC-Date=20260427T234110Z&HW-CC-Expire=86400&HW-CC-Sign=E18E4D7D566116637F3910F787FCFA19C972891A48E9A8FAD0F44AEF371BA769)

说明

* 禁止直接使用上图中四级目录之前的目录名组成的路径字符串，否则可能导致后续应用版本因应用文件路径变化导致不兼容问题。
* 应通过Context属性获取应用文件路径，包括但不限于上图中绿色背景的路径。 Context上下文获取及上述应用文件路径的获取，详见[应用上下文Context](application-context-stage.md)。

1. 一级目录data/：应用文件根目录。
2. 二级目录storage/：应用持久化文件目录。
3. 三级目录el1/~el5/：不同文件加密类型。

   EL1(Encryption Level 1):

   * 保护设备上所有文件的基础安全能力。设备开机后，用户无需完成身份验证即可访问EL1保护的文件。除非有特殊需求，否则不建议使用此方法。
   * 如果直接窃取设备存储介质上的密文，攻击者无法脱机进行解密。

   EL2(Encryption Level 2):

   * 在EL1的基础上，增加首次认证后的文件保护能力。设备开机后，用户在通过首次认证后，通过EL2能力保护的文件才能被访问。此后只要设备没有关机，通过EL2能力保护的文件一直可被访问。推荐应用默认使用该方式。
   * 如果在关机后丢失手机，攻击者无法读取EL2保护的文件。

   EL3(Encryption Level 3):

   * 与EL4整体能力类似，但和EL4的区别是，在锁屏下可创建新的文件，但无法读取。如无特殊必要，无需使用该方式。

   EL4(Encryption Level 4):

   * 在EL2的基础上，增加设备锁屏时的文件保护能力。在用户锁屏时，通过EL4能力保护的数据将无法被访问。如无特殊必要，无需使用该方式。
   * 如果设备在锁屏状态下被盗，攻击者无法读取EL4保护的文件。

   EL5(Encryption Level 5):

   * 在EL2的基础上，增加设备锁屏时的文件保护能力。在用户锁屏后，满足一定条件时，通过EL5能力保护的数据将无法被访问，但可以继续创建和读写新的文件。如无特殊必要，无需使用该方式。
   * 默认情况下不会生成EL5的相关目录，应用若需要使用EL5目录，则需要配置访问E类加密数据库的权限。具体配置方法详见[E类加密数据库的使用](encrypted-estore-guidelines.md)。

   说明

   应用如无特殊需要，应将数据存放在el2加密目录下，以尽可能保证数据安全。但是对于某些场景，一些应用文件需要在用户首次认证前就可被访问，例如时钟、闹铃、壁纸等，此时应用需要将这些文件存放到设备级加密区（el1）。

   开发者可通过监听[COMMON\_EVENT\_USER\_UNLOCKED](../harmonyos-references/commoneventmanager-definitions.md#common_event_user_unlocked)事件感知当前用户首次认证完成。

   切换应用文件加密类型目录的方法请参见[获取和修改加密分区](application-context-stage.md#获取和修改加密分区)。
4. 四级、五级目录：

   通过ApplicationContext获取distributedfiles目录或base下的files、cache、preferences、temp等目录的路径，应用全局信息存放在这些目录下。

   通过UIAbilityContext、AbilityStageContext、ExtensionContext可以获取HAP级别应用文件路径。HAP信息可以存放在这些目录下，存放在此目录的文件会跟随HAP的卸载而删除，不会影响App级别目录下的文件。在开发态，一个应用包含一个或者多个HAP，详见[Stage模型应用程序包结构](application-package-structure-stage.md)。

   应用文件路径具体说明及生命周期如下表所示。

   **表1** 应用文件路径详细说明

   | 目录名 | Context属性名称 | 类型 | 说明 |
   | --- | --- | --- | --- |
   | bundle | bundleCodeDir | 安装文件路径 | 应用安装后的App的HAP资源包所在目录；随应用卸载而清理。  不能通过拼接路径访问资源文件，应使用[资源管理接口](../harmonyos-references/js-apis-resource-manager.md)访问资源。  可以用于存储应用的代码资源数据，主要包括应用安装的HAP资源包、可重复使用的库文件以及插件资源等。此路径下存储的代码资源数据可以被用于动态加载。 |
   | base | NA | 本设备文件路径 | 应用在本设备上存放持久化数据的目录（随应用卸载而清理），子目录包含files/、cache/、temp/和haps/。  不建议将cookie、密码和token等高风险信息明文存储在此目录下。 |
   | database | databaseDir | 数据库路径 | 应用在el2加密条件下存放通过分布式数据库服务操作的文件目录；随应用卸载而清理。  仅用于保存应用的私有数据库数据，主要包括数据库文件等。此路径下仅适用于存储分布式数据库相关文件数据。 |
   | distributedfiles | distributedFilesDir | 分布式文件路径 | 应用在el2加密条件下存放分布式文件的目录，应用将文件放入该目录可分布式跨设备直接访问；随应用卸载而清理。  可以用于保存应用分布式场景下的数据，主要包括应用多设备共享文件、应用多设备备份文件、应用多设备群组协助文件。此路径下存储这些数据，使得应用更加适合多设备使用场景。  **注意**：  distributedfiles下的.remote\_share目录由系统创建管理，应用请勿创建或操作。  distributedfiles目录支持直接操作其他设备文件，请勿随意删除该目录下的文件。详细注意事项请参考[跨设备文件共享和访问](file-access-across-devices.md) 。 |
   | files | filesDir | 应用通用文件路径 | 应用在本设备内部存储上通用的存放默认长期保存的文件路径；随应用卸载而清理。  可以用于保存应用的任何私有数据，主要包括用户持久性文件、图片、媒体文件以及日志文件等。此路径下存储这些数据，使得数据保持私有、安全且持久有效。 |
   | cache | cacheDir | 应用缓存文件路径 | 应用在本设备内部存储上用于缓存下载的文件或可重新生成的缓存文件的路径，应用cache目录大小超过配额或者系统空间达到一定条件，自动触发清理该目录下文件；用户通过系统空间管理类应用也可能触发清理该目录。应用需判断文件是否仍存在，决策是否需重新缓存该文件；随应用卸载而清理。  可以用于保存应用的缓存数据，主要包括离线数据、图片缓存、数据库备份以及临时文件等。此路径下存储的数据可能会被系统自动清理，因此不要存储重要数据。 |
   | preferences | preferencesDir | 应用首选项文件路径 | 应用在本设备内部存储上通过数据库API存储配置类或首选项的目录；随应用卸载而清理。详见[通过用户首选项实现数据持久化](data-persistence-by-preferences.md)。  可以用于保存应用的首选项数据，主要包括应用首选项文件以及配置文件等。此路径下仅适用于存储少量数据。 |
   | temp | tempDir | 应用临时文件路径 | 应用在本设备内部存储上仅在应用运行期间产生和需要的文件，应用退出后即清理。  可以用于保存应用的临时生成的数据，主要包括数据库缓存、图片缓存、临时日志文件、以及下载的应用安装包文件等。此路径下存储使用后即可删除的数据。 |

## 应用沙箱路径和真实物理路径的对应关系

在应用沙箱路径下读写文件，经过映射转换，实际读写的是真实物理路径中的应用文件，应用沙箱路径与真实物理路径对应关系如下表所示。

其中<USERID>为当前用户ID，从100开始递增，<EXTENSIONPATH>为moduleName-extensionName。应用是否以Extension独立沙箱运行可参考[ExtensionAbility组件](extensionability-overview.md)。

| 应用沙箱路径 | 物理路径 |
| --- | --- |
| /data/storage/el1/bundle | 应用安装包目录：  /data/app/el1/bundle/public/<PACKAGENAME> |
| /data/storage/el1/base | 应用el1级别加密数据目录：  - 非独立沙箱运行的应用：/data/app/el1/<USERID>/base/<PACKAGENAME>  - 以独立沙箱运行的Extension应用： /data/app/el1/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/base | 应用el2级别加密数据目录：  - 非独立沙箱运行的应用：/data/app/el2/<USERID>/base/<PACKAGENAME>  - 以独立沙箱运行的Extension应用： /data/app/el2/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el1/database | 应用el1级别加密数据库目录：  - 非独立沙箱运行的应用：/data/app/el1/<USERID>/database/<PACKAGENAME>  - 以独立沙箱运行的Extension应用：/data/app/el1/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/database | 应用el2级别加密数据库目录：  - 非独立沙箱运行的应用：/data/app/el2/<USERID>/database/<PACKAGENAME>  - 以独立沙箱运行的Extension应用：/data/app/el2/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/distributedfiles | 应用el2加密级别有账号分布式数据融合目录：  - 物理目录：/mnt/hmdfs/<USERID>/account/merge\_view/data/<PACKAGENAME> |
