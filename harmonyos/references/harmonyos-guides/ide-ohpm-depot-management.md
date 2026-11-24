---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-depot-management
title: 仓库管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 仓库管理
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:20+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a959fe90afe437958ec87494b5b7ea359ea2fdbc4a1c016f1d0b32e50bdd2fa5
---

仓库管理主要负责管理仓库信息，包括仓库中所有包权限管理，包的上传与下架和uplinks管理。

## 管理仓库

ohpm-repo从5.3.0开始支持多仓配置，并且支持对每个仓库进行权限编辑。

仓库权限分为读权限和写权限。当用户在执行下载包、上传包、下架现有包和编辑包标签时，需要同时具有仓库的对应权限和[包的对应权限](ide-package-permission-management.md)，缺一不可。

| 仓库权限类型 | 前提条件 | 可执行操作 | 典型场景 |
| --- | --- | --- | --- |
| 可读 | 1. 公开可读  2. 授权可读，用户位于授权可读白名单中 | * 下载包 | 开发者获取依赖包 |
| 可写 | 1. 公开可写  2. 授权可写，用户位于授权可写白名单中 | * 下载包 * 上传包 * 下架现有包 * 编辑包标签（Tag） | 维护者更新仓库内容 |

管理仓库页面展示当前所拥有的仓库信息，包含如下四个功能：

1. 管理仓库三方包。
2. 编辑仓库。
3. 删除仓库。
4. 新增仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/HNmxyvSWS9yZffOeF4SeLA/zh-cn_image_0000002808885097.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=819F9EE532B3A8E737FE37786608D4F1609311B01A96151693889A4C8D278115 "点击放大")

### 管理三方包

管理三方包页面包含权限管理和上下架两部分。

### 权限管理

ohpm-repo从5.3.0版本开始支持配置包级别的访问权限。系统管理员能够对仓库中所有的包进行权限管理，支持配置包的可见性、白名单和管理所有者。支持通过包名模糊检索到需要管理权限的包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/1GX88GvhSo2AhrC_o4m8xA/zh-cn_image_0000002779565440.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAF9C25CCB025126C53D9501E6D60DB8A8A0698187BA26827DC9D46BE8844482 "点击放大")

* 区域1：可见性配置，能够配置一个包的可见性，默认为公开可读。当配置为授权可读时，支持在区域2中添加可读白名单。当包设置为公开可读时，所有用户对包具有下载和查看权限；当包设置为授权可读时，仅添加在可读白名单中的用户具有包的下载权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/0k2FCsGmT62u_UcwSxgeaQ/zh-cn_image_0000002779405440.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EF9209932E6F228DFA78387B2DCD5F70F0CE037AA69C842FF7B2ECFD6C3321C "点击放大")

* 区域2：白名单配置，在白名单中的用户将具有包的下载和查看权限，包的所有者和维护者会自动添加到包的白名单中。点击“新增用户”或“删除”按钮，可以在白名单配置中添加或者删除查看者用户，所有者和维护者用户禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/5jw1P_mZRZaTga3Ggz_Z_w/zh-cn_image_0000002808765001.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD8D908E61BE1E1909BD13F705905AD477DD29888BBC66D88B141B75C97A4847 "点击放大")

* 区域3：管理所有者，包的所有者具有包的下载，上传，下架和编辑包tag权限。支持对包所有者进行新增和删除，当包仅剩唯一一个所有者用户时，禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/mSSZLkRjRReejiE203pWUA/zh-cn_image_0000002779405460.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=16FB074D16E4B9C8F97E0C95CB23BAA16AADEA3D2BADA8B0B7A35201D24ADB54 "点击放大")

### 上下架

点击“管理ohpm仓库三方包”按钮，进入仓库管理详情面板，展示所有已上传至ohpm-repo的三方包信息。上下架包含上传三方包、批量上传三方包、单个包下架、批量包下架和搜索三方包功能。

ohpm-repo从6.0.1版本开始，支持批量上传三方包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9h4Nnbw4TXaCRyKGz28KOQ/zh-cn_image_0000002779565466.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E7994D8E094C654391AA9A586906B2071751591343F24F6143F7AF500E82102 "点击放大")

* 区域1：上传三方包，点击“上传三方包”按钮，选择本地的三方包文件，将其上传至仓库中，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/4aODFMcgSQa6QEG3gM_yIg/zh-cn_image_0000002779405500.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDEF56CE8D391F4E060D89685E03F7491DBA3EF23CA3F536BF819CF66E25FFEF "点击放大")
* 区域2：批量上传三方包，点击“批量上传三方包”按钮，选择本地的.zip文件，将其上传至仓库中，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/SM2_d4jwTiatmFtqALn-aA/zh-cn_image_0000002779565458.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=657DEBBBF50E08BCA8767FD5214CBC62EEA290D0E9BE43BAE0D4D33B9C05E798 "点击放大")
* 区域3：下架，点击指定包右边的“下架”按钮，进行单个包下架操作，输入下架原因即可完成包的下架，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/hn640lBWSF-3K1bAE7WxaQ/zh-cn_image_0000002808885115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEB636E313CB6521B47094F54D6D25414874A4AF0ADF88F664B499D64E0B4778 "点击放大")
* 区域4：批量下架，勾选包左边的待选框，点击“批量下架”按钮，能够批量下架已勾选的包，可以通过改变页面底部每页包含的数据值，批量下架更多的包。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/HSRVZZ78TkKX70ESfFi5jQ/zh-cn_image_0000002779565426.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=3950A667E8BB6A9991A7C2742BA6AE814CC76A6C019F2E0D0E61DEC7EFC68A61 "点击放大")
* 区域5：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选。支持通过Name、Version、Publisher、Author和PublishTime字段筛选包数据。例如筛选出Name带有数字3，版本号大于等于2.0.0，发布人为accessToken1的包，数据筛选效果如下图所示：

  - Name：支持对包名进行模糊搜索。

  - Version：支持输入最小版本号和最大版本号，进行版本号区间搜索。

  - Publisher：支持对包发布者名称进行模糊搜索。

  - Author：支持对包作者名称进行模糊搜索。

  - PublishTime：支持对包发布时间进行区间搜索。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Fx77lfALTcG8aZkgzDDicw/zh-cn_image_0000002808765047.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBEF6E88EBFA2E5F9C886DDB5FA72ED0A9A56ED9A31DFBAD29F518F65DA5E2AE "点击放大")

### 编辑仓库

**ohpm-repo 6.0.0及以上版本**

从ohpm-repo 6.0.0版本开始，发布策略设置发生变化，支持分别设置标准版本发布策略和先行版本发布策略。标准版本（如1.0.0）和先行版本（如1.0.0-snapshot快照）的定义具体请参考[版本号格式](ide-ohpm-version-rules.md#section1340910343311)。

点击指定仓库的“编辑”图标按钮，进入仓库信息编辑界面，可以修改仓库的Name 、Uplink、可读策略、授权可读白名单、可写策略，授权可写白名单、标准版本发布策略、先行版本发布策略和描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/gSuZi9MtSDyRE7G7pCPO-A/zh-cn_image_0000002808885085.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=55869FDC28C8AC028F3FACB192A3FC5F921791B1A11CD4D20670FE109D39FDCD "点击放大")

* Name：仓库的名称。当仓库发过包或者已添加授权可读白名单或可写白名单时，禁止修改仓库名。
* Uplink：配置代理仓库地址。其中Uplink为下拉框选择，选项为仓库管理页面的[uplinks](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_uplinks)面板配置的Uplink仓库。
* 可读策略： 分为公开可读和授权可读。当一个仓库被设置为授权可读时，将出现授权可读名单配置项，系统管理员默认具有仓库读和写权限。当仓库设置为公开可读时，所有用户对仓库具有读权限，能够访问仓库中包的信息和下载包；当设置为授权可读时，仅授权可读白名单中用户拥有仓库的读权限。当仓库可读策略设置为授权可读时，可写策略默认选择授权可写，不可修改。
* 授权可读名单：当可读策略选择授权可读时，将出现授权可读名单配置项，能够逐个添加仓库可读用户。授权可读白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 可写策略：分为公开可写和授权可写。当一个仓库被设置为授权可写时，将出现授权可写名单配置项，仅在可写名单中的用户具有仓库的写权限，具有写权限默认具有读权限，系统管理员默认具有仓库读写权限。当仓库设置为公开可写时，所有用户对仓库具有写权限，能够对仓库中的包进行下载，上传，下架和编辑tag操作；当设置为授权可写时，仅授权可写白名单中用户拥有仓库的写权限。
* 授权可写名单：当可写策略选择授权可写时，将出现授权可写名单配置项，能够逐个添加仓库可写用户。授权可写白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 标准版本发布策略：分为禁止同版本覆盖和支持同版本覆盖两种模式，只针对标准版本生效。在禁止同版本覆盖模式下，若尝试向仓库重复发布同一版本的包，系统会报错提示“该三方库已存在此版本”，确保版本唯一性。在支持同版本覆盖模式下，允许重复发布同版本包，新包将直接覆盖旧包，适用于需要持续更新的场景。用户可通过配置灵活选择适合的发布策略。**覆盖操作不可逆，请谨慎选择**。
* 先行版本发布策略：分为禁止同版本覆盖和支持同版本覆盖两种模式，只针对先行版本生效。在禁止同版本覆盖模式下，若尝试向仓库重复发布同一版本的包，系统会报错提示“该三方库已存在此版本”，确保版本唯一性。在支持同版本覆盖模式下，允许重复发布同版本包，新包将直接覆盖旧包，适用于需要持续更新的场景。用户可通过配置灵活选择适合的发布策略。**覆盖操作不可逆，请谨慎选择**。

**ohpm-repo 6.0.0以下版本**

点击指定仓库的“编辑”图标按钮，进入仓库信息编辑界面，可以修改仓库的Name 、Uplink、可读策略、授权可读白名单、可写策略，授权可写白名单、发布策略和描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/9h5dje4fQuSkBW0-LWyAQg/zh-cn_image_0000002779405494.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AC65478F07207E979E7E4F7C4EBF2B013D4ADC578F4A6139E27487526CA3792 "点击放大")

* Name：仓库的名称。当仓库发过包或者已添加授权可读白名单或可写白名单时，禁止修改仓库名。
* Uplink：配置代理仓库地址。其中Uplink为下拉框选择，选项为仓库管理页面的[uplinks](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_uplinks)面板配置的Uplink仓库。
* 可读策略： 分为公开可读和授权可读。当一个仓库被设置为授权可读时，将出现授权可读名单配置项，系统管理员默认具有仓库读和写权限。当仓库设置为公开可读时，所有用户对仓库具有读权限，能够访问仓库中包的信息和下载包；当设置为授权可读时，仅授权可读白名单中用户拥有仓库的读权限。当仓库可读策略设置为授权可读时，可写策略默认选择授权可写，不可修改。
* 授权可读名单：当可读策略选择授权可读时，将出现授权可读名单配置项，能够逐个添加仓库可读用户。授权可读白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 可写策略：分为公开可写和授权可写。当一个仓库被设置为授权可写时，将出现授权可写名单配置项，仅在可写名单中的用户具有仓库的写权限，具有写权限默认具有读权限，系统管理员默认具有仓库读写权限。当仓库设置为公开可写时，所有用户对仓库具有写权限，能够对仓库中的包进行下载，上传，下架和编辑tag操作；当设置为授权可写时，仅授权可写白名单中用户拥有仓库的写权限。
* 授权可写名单：当可写策略选择授权可写时，将出现授权可写名单配置项，能够逐个添加仓库可写用户。授权可写白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 发布策略：分为禁止同版本覆盖和支持同版本覆盖两种模式。在禁止同版本覆盖模式下，若尝试向仓库重复发布同一版本的包，系统会报错提示“该三方库已存在此版本”，确保版本唯一性。在支持同版本覆盖模式下，允许重复发布同版本包，新包将直接覆盖旧包，适用于需要持续更新的场景。用户可通过配置灵活选择适合的发布策略。**覆盖操作不可逆，请谨慎选择**。

### 删除仓库

点击“删除”图标按钮将删除当前选中的仓库。当仓库下存在上架包时禁止删除仓库，当仅剩最后一个仓库时禁止删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ZpxlejdyT0qryBfpkt7RWw/zh-cn_image_0000002808765009.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF317CB9A65845F8EF11AA3D1C27E27DEC6D68B86D0DDA33E2B6B8CFE6F0B443 "点击放大")

### 新增仓库

**ohpm-repo 6.0.0及以上版本**

点击“+”图标按钮将新增一个仓库，可以对仓库的Name、Uplink、可读策略、可写策略、发布策略和描述信息进行编辑。可读策略默认为公开可读，可写策略默认为公开可写，标准版本（如1.0.0）发布策略默认为禁止同版本覆盖，先行版本（如1.0.0-snapshot快照）发布策略默认为禁止同版本覆盖。最多支持创建20个仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/QEImq-bYQNKE-_7DlfOeKw/zh-cn_image_0000002808885121.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=81E8052FD668218852FE8C828761724348CD9AD141FD48CA903633CEF2BB4121 "点击放大")

**ohpm-repo 6.0.0以下版本**

点击“+”图标按钮将新增一个仓库，可以对仓库的Name、Uplink、可读策略、可写策略、发布策略和描述信息进行编辑。可读策略默认为公开可读，可写策略默认为公开可写，发布策略默认为禁止同版本覆盖。最多支持创建20个仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/m9EljideTk675taISSH_jA/zh-cn_image_0000002808765025.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=70FF2ECDB199E513FEF06D95DC06608857E9858D4A2405E2A600B1CE49B53596 "点击放大")

## uplinks

uplinks功能可以让当前仓库获取配置的uplink仓库的所有包，若从某个已配置uplink的仓库下载当前仓库中不存在的三方包时，则会通过uplink仓库下载该包，如果访问uplink仓库需要代理，请配置好所需代理信息，uplink页面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/KSFDkzz1SsGt_3--vJIqvw/zh-cn_image_0000002779405468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2D360F0F5CFE944DDFB52097FCF8A29FC76B890E1ECC666B598B4F8783E0D6A "点击放大")

1. 点击新增按钮，可以创建新的uplink仓库。一旦完成新增uplink仓库的设置，必须前往仓库管理 > 管理仓库 > 编辑页面进行应用，这样该功能才会生效，且ohpm-repo只允许同时配置一个uplink仓库。uplink仓库地址不建议配置为其他ohpm-repo的地址，避免出现仓库A配置uplink为仓库B，仓库B配置uplink为仓库A，导致循环查找问题。

   ohpm-repo从6.0.1版本开始，新增uplink证书校验开关（默认开启）。开启状态下，系统将验证HTTPS协议uplink地址的服务器证书，请提前在config.yaml的uplink\_ca\_files中配置可信CA证书，详见[配置文件](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)，关闭开关则跳过证书校验。

   页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/YfeWDmaeQyWIXTSZTi7abw/zh-cn_image_0000002779405478.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C794EB76FFD283805DFEE26D744D2FFD8221D55C68AB1DE7A1ACE1EE534366AD "点击放大")
2. 点击编辑，可以修改已配置的uplink仓库信息，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/GGytP5IcS9yh4tz9qtPGww/zh-cn_image_0000002808765015.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=09CE8E03393CC888CBAD1216EBCED988267AA734E83572DE239F12E4059A5928 "点击放大")
3. 点击删除，可以删除配置的uplink仓库，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2_7mi5v7RMSBsQ6g4ucvzw/zh-cn_image_0000002808765039.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D1DBA1BECE7791072ABDBBECD3250C4A5049B65FD19C73A5A30165403E1738F "点击放大")
4. 由于搭建的ohpm-repo私仓可能需要通过代理来访问已配置的uplink仓库，因此ohpm-repo提供了代理功能。点击配置代理，可以添加代理信息，页面效果如下图所示：

   **说明** 

   HttpProxy、HttpsProxy和uplinks仓库地址有关，与搭建的代理服务器协议无关。若uplinks仓库地址是http协议，则选择HttpProxy配置代理；若uplinks仓库地址是https协议，则选择HttpsProxy配置代理。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/wiTj_gPYTQaHhcNkMmDtWQ/zh-cn_image_0000002779405484.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E1D8553DD409869D4CE8CE292D0A059ABDD4189FB2D8FD1E23D2C909D2DBF36 "点击放大")
