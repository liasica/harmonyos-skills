---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-depot-management
title: 仓库管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 仓库管理
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:49992da7b2fd8a9bf8f6e0ab63a95e067263cda18eb57ffe1f7b4eca1e37f68d
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/qYIAETvDS7GdXWcz-4yKmg/zh-cn_image_0000002808885097.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC14CD82D8AB756627E12DCE11725FE8682D10EBA214633E490BFCF64277280D "点击放大")

### 管理三方包

管理三方包页面包含权限管理和上下架两部分。

### 权限管理

ohpm-repo从5.3.0版本开始支持配置包级别的访问权限。系统管理员能够对仓库中所有的包进行权限管理，支持配置包的可见性、白名单和管理所有者。支持通过包名模糊检索到需要管理权限的包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/gVKNwUqyQ9iUuet40DDEwQ/zh-cn_image_0000002779565440.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D3E8D2AFB4C7CBCF0EA7B2080C0AF4C72A4B976C04745FD31C87BCD5D1CC3F4 "点击放大")

* 区域1：可见性配置，能够配置一个包的可见性，默认为公开可读。当配置为授权可读时，支持在区域2中添加可读白名单。当包设置为公开可读时，所有用户对包具有下载和查看权限；当包设置为授权可读时，仅添加在可读白名单中的用户具有包的下载权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/HkE0WAJ3SOOjirTRK7ihCA/zh-cn_image_0000002779405440.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FAFDB9A0456377D4DB69371783695C915A1C4014A4CF3D7FE69AB36EFC263B3 "点击放大")

* 区域2：白名单配置，在白名单中的用户将具有包的下载和查看权限，包的所有者和维护者会自动添加到包的白名单中。点击“新增用户”或“删除”按钮，可以在白名单配置中添加或者删除查看者用户，所有者和维护者用户禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/5ow3Vi-4Qoia1wBL-e04AQ/zh-cn_image_0000002808765001.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B557133D706AA97B85917A176E50CFFA75D7767239A6C274B2C2CB8CA06A9F6 "点击放大")

* 区域3：管理所有者，包的所有者具有包的下载，上传，下架和编辑包tag权限。支持对包所有者进行新增和删除，当包仅剩唯一一个所有者用户时，禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/cJR6OgbZSRa3WdZSuW_8JQ/zh-cn_image_0000002779405460.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=33226F066828E84E018DAD0A1CF1972113A074B904A6720C99F13DCFB7D005AD "点击放大")

### 上下架

点击“管理ohpm仓库三方包”按钮，进入仓库管理详情面板，展示所有已上传至ohpm-repo的三方包信息。上下架包含上传三方包、批量上传三方包、单个包下架、批量包下架和搜索三方包功能。

ohpm-repo从6.0.1版本开始，支持批量上传三方包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/0BA2x7mfRk2J_325FxW4YA/zh-cn_image_0000002779565466.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5195CEF3ACB160B3A20ACFFA15D460D2386B32B99360C4E4C6D5CF46DA37762 "点击放大")

* 区域1：上传三方包，点击“上传三方包”按钮，选择本地的三方包文件，将其上传至仓库中，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/H1h9BD8qRt6LCwg9AiJoSA/zh-cn_image_0000002779405500.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5690EF1EED08BA087855EC049EBC479CF9EC30854FC49935FBB4C7C27FF8EE1 "点击放大")
* 区域2：批量上传三方包，点击“批量上传三方包”按钮，选择本地的.zip文件，将其上传至仓库中，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/M-9ou6BuQ1aab1LHN3ZpQQ/zh-cn_image_0000002779565458.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2C909AA7145337243DF9D7FED3E4E86F8A29D0BBB8C3C86522A154E06E75A98 "点击放大")
* 区域3：下架，点击指定包右边的“下架”按钮，进行单个包下架操作，输入下架原因即可完成包的下架，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1uRNvd7uRA-4Ph1PkUxjfw/zh-cn_image_0000002808885115.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=948FC4C846C3DC0E104F7939656E9E46DBB26A5A4C7FE3C4DCBB26F86674DE25 "点击放大")
* 区域4：批量下架，勾选包左边的待选框，点击“批量下架”按钮，能够批量下架已勾选的包，可以通过改变页面底部每页包含的数据值，批量下架更多的包。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/yzK3nrHBRLarEloht3vQVA/zh-cn_image_0000002779565426.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6874CF848928059651E4AE119CD4AB95B044AE37372E8D39EFDCB047BA4EB66 "点击放大")
* 区域5：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选。支持通过Name、Version、Publisher、Author和PublishTime字段筛选包数据。例如筛选出Name带有数字3，版本号大于等于2.0.0，发布人为accessToken1的包，数据筛选效果如下图所示：

  - Name：支持对包名进行模糊搜索。

  - Version：支持输入最小版本号和最大版本号，进行版本号区间搜索。

  - Publisher：支持对包发布者名称进行模糊搜索。

  - Author：支持对包作者名称进行模糊搜索。

  - PublishTime：支持对包发布时间进行区间搜索。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/lt8oN0NMTJiXedzFBEtIHA/zh-cn_image_0000002808765047.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED7D90CF4ED56EC8682DEEEED8B744F1EEB5565744FB27DA1D7C70E167885DF2 "点击放大")

### 编辑仓库

**ohpm-repo 6.0.0及以上版本**

从ohpm-repo 6.0.0版本开始，发布策略设置发生变化，支持分别设置标准版本发布策略和先行版本发布策略。标准版本（如1.0.0）和先行版本（如1.0.0-snapshot快照）的定义具体请参考[版本号格式](ide-ohpm-version-rules.md#section1340910343311)。

点击指定仓库的“编辑”图标按钮，进入仓库信息编辑界面，可以修改仓库的Name 、Uplink、可读策略、授权可读白名单、可写策略，授权可写白名单、标准版本发布策略、先行版本发布策略和描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/K0KjPR47SKOIGtRMKbMnuw/zh-cn_image_0000002808885085.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=469340F75C81C047CB9842750337698069AE2DDFF32C7A9CCE5EED9707D73B21 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/byiFEbJsRums5TndVBUyOw/zh-cn_image_0000002779405494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=823D56C2A80B5EE088955E792FB5044383A026FB747BDEBFB3EA8ECDB40DD062 "点击放大")

* Name：仓库的名称。当仓库发过包或者已添加授权可读白名单或可写白名单时，禁止修改仓库名。
* Uplink：配置代理仓库地址。其中Uplink为下拉框选择，选项为仓库管理页面的[uplinks](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_uplinks)面板配置的Uplink仓库。
* 可读策略： 分为公开可读和授权可读。当一个仓库被设置为授权可读时，将出现授权可读名单配置项，系统管理员默认具有仓库读和写权限。当仓库设置为公开可读时，所有用户对仓库具有读权限，能够访问仓库中包的信息和下载包；当设置为授权可读时，仅授权可读白名单中用户拥有仓库的读权限。当仓库可读策略设置为授权可读时，可写策略默认选择授权可写，不可修改。
* 授权可读名单：当可读策略选择授权可读时，将出现授权可读名单配置项，能够逐个添加仓库可读用户。授权可读白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 可写策略：分为公开可写和授权可写。当一个仓库被设置为授权可写时，将出现授权可写名单配置项，仅在可写名单中的用户具有仓库的写权限，具有写权限默认具有读权限，系统管理员默认具有仓库读写权限。当仓库设置为公开可写时，所有用户对仓库具有写权限，能够对仓库中的包进行下载，上传，下架和编辑tag操作；当设置为授权可写时，仅授权可写白名单中用户拥有仓库的写权限。
* 授权可写名单：当可写策略选择授权可写时，将出现授权可写名单配置项，能够逐个添加仓库可写用户。授权可写白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 发布策略：分为禁止同版本覆盖和支持同版本覆盖两种模式。在禁止同版本覆盖模式下，若尝试向仓库重复发布同一版本的包，系统会报错提示“该三方库已存在此版本”，确保版本唯一性。在支持同版本覆盖模式下，允许重复发布同版本包，新包将直接覆盖旧包，适用于需要持续更新的场景。用户可通过配置灵活选择适合的发布策略。**覆盖操作不可逆，请谨慎选择**。

### 删除仓库

点击“删除”图标按钮将删除当前选中的仓库。当仓库下存在上架包时禁止删除仓库，当仅剩最后一个仓库时禁止删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/6blt2bHATLSOl4zwWNLDlg/zh-cn_image_0000002808765009.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBC5BAFF604866D51CF1AEA354002ADD17F0ADB8343A237F63C8F399C96987C1 "点击放大")

### 新增仓库

**ohpm-repo 6.0.0及以上版本**

点击“+”图标按钮将新增一个仓库，可以对仓库的Name、Uplink、可读策略、可写策略、发布策略和描述信息进行编辑。可读策略默认为公开可读，可写策略默认为公开可写，标准版本（如1.0.0）发布策略默认为禁止同版本覆盖，先行版本（如1.0.0-snapshot快照）发布策略默认为禁止同版本覆盖。最多支持创建20个仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/tjbs3dA8QSCbceC_6DzEag/zh-cn_image_0000002808885121.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7448A9D9EDDA94A2ABB43ED8E1B22AD3F645D3C90EBEB013071705E18A5C516 "点击放大")

**ohpm-repo 6.0.0以下版本**

点击“+”图标按钮将新增一个仓库，可以对仓库的Name、Uplink、可读策略、可写策略、发布策略和描述信息进行编辑。可读策略默认为公开可读，可写策略默认为公开可写，发布策略默认为禁止同版本覆盖。最多支持创建20个仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/2FsQ81kcRxmZVDMb24ggbw/zh-cn_image_0000002808765025.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B8B7865987E6C580B94FA0DA5FFEA013852FF0599CC6E06B37AC612F2BBD27B "点击放大")

## uplinks

uplinks功能可以让当前仓库获取配置的uplink仓库的所有包，若从某个已配置uplink的仓库下载当前仓库中不存在的三方包时，则会通过uplink仓库下载该包，如果访问uplink仓库需要代理，请配置好所需代理信息，uplink页面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/LJJBIULMT9-R0kd2GBSH7A/zh-cn_image_0000002779405468.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0608C5DE724EF686898368EED05BF7712688345502AC17B2DCEB92E9979E2EB "点击放大")

1. 点击新增按钮，可以创建新的uplink仓库。一旦完成新增uplink仓库的设置，必须前往仓库管理 > 管理仓库 > 编辑页面进行应用，这样该功能才会生效，且ohpm-repo只允许同时配置一个uplink仓库。uplink仓库地址不建议配置为其他ohpm-repo的地址，避免出现仓库A配置uplink为仓库B，仓库B配置uplink为仓库A，导致循环查找问题。

   ohpm-repo从6.0.1版本开始，新增uplink证书校验开关（默认开启）。开启状态下，系统将验证HTTPS协议uplink地址的服务器证书，请提前在config.yaml的uplink\_ca\_files中配置可信CA证书，详见[配置文件](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)，关闭开关则跳过证书校验。

   页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/rGmzd8XKSdKa-wDWgAdGnA/zh-cn_image_0000002779405478.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7433D5C062D65FF9948F450F0B4E9CC58A06A6ED8BAEC6A9E9A9EF63ACA137 "点击放大")
2. 点击编辑，可以修改已配置的uplink仓库信息，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/pXdSZ37URTmS5ZK_z6yO7Q/zh-cn_image_0000002808765015.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F1B7040A72A170AD215C6554F71C990C15F6BFD45CC30628506857123ED430E "点击放大")
3. 点击删除，可以删除配置的uplink仓库，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/AHvYl2iUQZ-yEnjwUfec1w/zh-cn_image_0000002808765039.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=D551B3A01B371D3E6ED037791077F43A439D73D75A4376A18728E8D9DA0A35A6 "点击放大")
4. 由于搭建的ohpm-repo私仓可能需要通过代理来访问已配置的uplink仓库，因此ohpm-repo提供了代理功能。点击配置代理，可以添加代理信息，页面效果如下图所示：

   **说明** 

   HttpProxy、HttpsProxy和uplinks仓库地址有关，与搭建的代理服务器协议无关。若uplinks仓库地址是http协议，则选择HttpProxy配置代理；若uplinks仓库地址是https协议，则选择HttpsProxy配置代理。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ri-hazorR2iIIHZyUksRhA/zh-cn_image_0000002779405484.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AA91239297916E534ADF5B929510903C8FB0B6D8F25FE10EADF9BED24E7DCF1 "点击放大")
