---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-faq
title: 常见问题FAQ
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 常见问题FAQ
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0932f0449625002f7f6f327e4a9654c63e51fed0e46176a0164eef1bcf82759b
---

## ohpm-repo私仓工具获取与升级

* 从[下载中心](https://developer.huawei.com/consumer/cn/download/ohpm-repo)上获取最新ohpm-repo工具包。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Cc_jJSp6Sg2v7ppn7W0lng/zh-cn_image_0000002530911382.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=88D06A065E652FC94F4970F293926FF3902FAFD729C5A637AAE42AE05D59F8A9 "点击放大")
* ohpm-repo升级指导：在升级之前请务必进行好数据的备份，具体的升级指导文档见：[ohpm-repo版本升级](ide-ohpm-repo-upgrade.md)。

## ohpm-repo启动后如何修改配置文件，并使得修改后配置文件生效

* **版本1.0.1**：停止当前ohpm-repo服务，修改ohpm-repo压缩包解压根目录中conf目录中的配置文件，然后重新执行start命令。
* **版本1.1.0**：停止当前ohpm-repo服务，修改部署根目录中conf目录下的配置文件，然后重新执行start命令。
* **版本2.X.X**：停止当前ohpm-repo服务，根据前一次ohpm-repo启动是否指定配置文件进行区别处理：
  + 上一次执行install命令指定配置文件：找到指定的配置文件进行修改，然后重新执行install，指定修改后配置文件，再执行start命令启动ohpm-repo。
  + 上一次执行install命令未指定配置文件：未指定配置文件即默认使用压缩包解压目录中conf下的配置文件，则修改默认使用的配置文件，然后不指定配置文件执行install，再执行start启动ohpm-repo。

## ohpm-repo部署目录和ohpm-repo解压目录说明

* **ohpm-repo解压目录**：<binary\_root>，ohpm-repo安装包解压后所在的根目录，存放的是ohpm-repo压缩包解压后的内容。
* **ohpm-repo部署目录**：<deploy\_root>，ohpm-repo运行时产生数据的存储位置，包括配置文件，日志文件，加密组件等信息。ohpm-repo部署目录在不同版本有不同的配置方法。
* + ohpm-repo 1.0.1版本：不支持自定义ohpm-repo部署目录，仅支持使用默认路径。
  + ohpm-repo 1.1.0版本：在使用ohpm-repo start或ohpm-repo deploy命令时，支持通过配置--deploy\_root参数来指定ohpm-repo的部署目录，不指定使用默认路径。
  + ohpm-repo 2.X.X版本：
    - 方法一：在配置文件中配置参数--deploy\_root可指定ohpm-repo的部署目录，执行ohpm-repo install命令生效。
    - 方法二：使用ohpm-repo deploy命令部署多实例，支持通过配置--deploy\_root参数来指定ohpm-repo的部署目录；不指定使用默认路径。

  注意

  ohpm-repo部署目录默认路径如下：

  + **Windows系统默认路径**：~/AppData/Roaming/Huawei/ohpm-repo
  + **Linux/macOS系统默认路径**: ~/ohpm-repo

  ohpm-repo部署目录和ohpm-repo解压目录不要放在**同一目录**中。

## ohpm-repo 的权限管理

### 账户权限：系统管理员和系统普通用户

1. **账户的注册**

   ohpm-repo账户有两种类型：用户类型和管理员类型。ohpm-repo初次启动默认有一个管理员账户：账户名：admin，密码：12345Qq!。

   * 通过ohpm-repo管理界面的注册按钮新增用户类型：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/hgBrdk9GRoeqjPN9pozj_w/zh-cn_image_0000002561751375.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=046A982E93FB4AFD9FD0A5AB62D8A6C3DA4F4B7B8254FA7A1D9878D08D7F28C6 "点击放大")
   * 登录任一管理员账户，能够在ohpm-repo的用户管理界面新增用户并管理其他用户（删除用户，变更用户类型，重置密码）：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/tputp_y2S7q3ir_6aQNZqw/zh-cn_image_0000002530911410.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=23DC111B798A443A0052191042436D5F93639196C15A88FD79E9463EEE8B746E "点击放大")
2. **账户的权限说明**
   * 系统管理员：允许有多个系统管理员。
     + 用户管理：创建新用户，编辑用户类型，修改其他用户类型和重置其他用户密码。
     + 仓库管理：编辑仓库，管理三方包（可以通过ohpm-repo管理界面直接发包），编辑uplink仓库和配置代理信息。
     + 系统设置：添加oh-package.json5检查规则，重置系统密钥和添加支持匿名化配置。
     + 组织管理：查看所有组织信息，编辑或删除所管理组织，能够编辑所有组织的管理员。
     + 操作日志：能够记录用户所有操作记录。
     + 认证管理：支持公私钥认证和AccessToken认证。
     + 包权限管理：支持对单个三方包配置精细化的权限控制，包含包的所有者、包的维护者和包的查看者。
   * 系统普通用户：允许有多个系统普通用户。
     + 组织管理：查看所在组织列表，编辑或删除所管理组织信息。
     + 认证管理：支持公私钥认证和AccessToken认证。
     + 包权限管理：支持对单个三方包配置精细化的权限控制，包含包的所有者、包的维护者和包的查看者。

### 组织权限：组织成员和组织管理员

1. **组织创建与组织权限的编辑**
   * 组织的新增和删除：登录系统管理员账户，在组织管理界面，通过新增按钮创建组织，当前系统管理员默认成为该组织的管理员；通过删除按钮删除组织。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ZgqoZKFgT-Op9FJL8smlvw/zh-cn_image_0000002530751426.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=2A01190E9474FFB3B49D02BF051046CF80CD10103130B1D7479100FF00C5BB83 "点击放大")
   * 组织普通成员的添加和删除：登录组织管理员的账户，在组织管理界面，选中需要添加用户的组织的详情按钮，然后在成员界面通过新增按钮添加组织成员，通过删除按钮删除组织成员。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ul9DvDWKQG648-fEEdW44Q/zh-cn_image_0000002561831325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=91F271092AA934247C2E9E5B2D90082494D3E487198B05E332650FF2C7B8B40C "点击放大")
   * 组织管理员的添加和删除：登录系统管理员账户，在组织管理界面，选中需要添加用户的组织的编辑组织管理员按钮，然后在编辑组织管理员界面通过新增组织管理员按钮添加组织管理员，通过删除按钮删除组织管理员。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/JPl7-aeGSf6LsO-DwPBvOg/zh-cn_image_0000002561751331.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=C95E254DAD96BCA4A4EAD56DDC8D2ADA8C58F018A5B3EA561FF8EE6C5D2C6E24 "点击放大")
2. **组织的权限说明**
   * 组织用户：允许有多个组织用户。
     + 上传包：能够上传带有该组织的三方包
     + 下架包：能够下架成员自己上传的三方包
   * 组织管理员：允许有多个组织管理员。
     + 上传包：能够上传带有该组织的三方包
     + 下架包：能够下架组织下所有成员上传的包
     + 组织编辑：编辑所属组织，删除与组织管理员权限变更
     + 组织成员编辑：管理所属组织成员的添加与删除

### 上传包和卸载包权限管理

三方包可以分为有组织的包和没有组织的包两类，上传和下架包可以通过ohpm-repo和ohpm命令行工具两种方式操作。

* 通过ohpm-repo管理界面中仓库管理上传和下架包：只有系统管理员才有此权限。**有组织包管理**：系统管理员可对所在组织的全部包执行上架与下架操作；**无组织包管理**：系统管理员可上架所有无组织包（注：无组织包的所有版本仅限单一用户上传），并拥有下架全部无组织包的权限。
* 通过ohpm命令行工具上传和下架包：配置.ohpmrc文件时，无论采用公私钥认证还是AccessToken认证，认证信息配置会标识唯一的用户信息，对于带组织的包，能够上传和下架用户所属组织的所有包；对于无组织的包，能够上传和下架所有的包。

## ohpm-repo 的元数据与三方包数据管理

### 元数据与三方包数据介绍

ohpm-repo的数据包括两部分：

* 元数据：ohpm-repo运行过程中生成的用户数据和上传包后包的描述数据，在配置文件中，通过在配置文件中db选项配置存储信息。
* 三方包数据：ohpm-repo运行后，通过ohpm-repo管理界面和ohpm命令行工具发布三方包到ohpm-repo中后，三方包的包文件数据，通过在配置文件中store选项配置存储信息。

### 元数据和三方包数据存储方式介绍

* 元数据：可以存放在本地文件（fileDb）和mysql数据库（mysql）。
* 三方包数据：可以存放在本地文件（file storage）,sftp服务器（sftp storage）和自定义插件存储（custom storage，包括各种云存储）。

  元数据和三方包数据的存储方法不能够随意搭配，匹配规则和支持的ohpm-repo版本信息见下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/4TIFM4zcQJu8zuLrE1Z_Hw/zh-cn_image_0000002561831349.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=64813EDF1F05DAC63826BDB8A3372F1B0474EF00917031D460AC9E8C59A3ED99 "点击放大")

  存储方式的变更：如果元数据和包数据的存储位置需要改变，可以通过数据迁移指导进行完成。

## ohpm-repo认证方式

ohpm在执行publish，unpublish和dist-tags等需要修改ohpm-repo数据库内容命令时，需要获取读写权限才能够操作。

从ohpm-repo5.0.5版本开始，如果ohpm-repo配置不支持匿名访问，ohpm在执行install，info和update命令时需要通过AccessToken认证或者自定义AccessToken认证方法，正确配置读写/只读AccessToken信息获取读权限。

### 认证方式说明

* **证书认证：**通过嵌入加密ssh证书进行身份验证，需要输入密码，获得读写权限。
* **AccessToken认证（对接数据库中用户数据）：**AccessToken是ohpm-repo 2.1.0版本新引入的认证机制（需配套使用1.6.0及以上版本的ohpm命令行工具），用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。在与ohpm-repo交互时，客户端会自动附带Token进行身份验证，实现免密认证。配置只读AccessToken获得读权限，配置读写AccessToken获得读写权限。
* **自定义AccessToken认证（对接自定义的用户数据）：**AccessToken是ohpm-repo 2.3.0版本新引入的认证机制（需配套使用1.8.0及以上版本的ohpm命令行工具），如果开发者不想把用户的数据存储在所配置的db存储路径中，可以[自定义认证插件](ide-custom-auth-plugin.md)，对接自定义的用户数据。AccessToken的有效性由自定义的用户数据认证。配置只读AccessToken获得读权限，配置读写AccessToken获得读写权限。

### 认证失败FAQ

### 使用证书认证执行publish/unpublish/dist-tags等命令失败

* **现象**：报错信息为：ERROR: Publish failed, detail: The "key\_path" is empty - configure "key\_path" in the .ohpmrc file.
* **原因分析**：没有正确配置证书认证参数。
* **解决方法**：
  + 确保通过ssh-keygen工具生成的公私钥文件是成对的。
  + 确保在ohpm-repo私仓管理界面配置公钥信息，在ohpm的配置文件.ohpmrc配置publish\_id，publish\_registry和key\_path等参数。

### 使用证书认证在git-bash终端下执行ohpm publish XX.har发包到ohpm-repo中报错：The content of private key in the key\_path error

* **现象**：在git-bash终端下运行ohpm publish命令出现 “The content of private key in the key\_path error”错误，报错截图为：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ZuP1bhIQR0Kv9-MTRvbCjQ/zh-cn_image_0000002561831315.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=910BA501370B07AB78CCD01CF487A55074757E5F3E099A775D95A28B60882833 "点击放大")
* **原因分析**：使用ohpm publish命令上传包时，此时如果使用ssh证书密码认证，程序需要通过TTY流读取用户输入的密码，git安装的版本过低其携带的git-bash会导致TTY流丢失，从而出现该错误。
* **解决方法**：
  + 方法一：从git官网下载安装最新版本git，使用最新版本携带的git-bash终端进行操作。
  + 方法二：在当前git安装目录下的etc目录中新增git-bash.config文件，git-bash.config文件里面添加一行MSYS=enable\_pcon 配置。重新打开git-bash终端运行ohpm publish命令即可。

### 使用AccessToken认证，执行publish/unpublish/dist-tags等命令失败

* **现象**：报错信息为ERROR: Publish failed, detail: The "key\_path" is empty - configure "key\_path" in the .ohpmrc file.
* **原因分析**：没有正确配置AccessToken或者当前工具版本不支持该功能。
* **解决方法**：
  + 升级工具版本：从ohpm-repo2.1.0和ohpm 1.6.0版本起，开始支持AccessToken功能，确保ohpm-repo和ohpm升级到对应的版本。
  + 在ohpm配置文件.ohpmrc中配置AccessToken错误，请遵循如下步骤完成配置：
    - 在ohpm客户端的配置文件.ohpmrc中新增一行//<ip>:<port>/repos/ohpm/:\_auth=<token>
    - *//<ip>:<port>/repos/ohpm/*是客户端publish\_registry去除协议名的部分url,<token>是生成的token。
    - 使用ohpm客户端执行publish等命令。

## 应用内hsp包如何发布到ohpm-repo

1. 如果需要发布应用内hsp包到ohpm-repo，需要确保安装指定版本的软件：
   * **ohpm-cli命令行工具**：1.3.0版本开始支持。
   * **DevEco Studio**：4.1.0版本开始支持。
   * **ohpm-repo私仓**： 1.1.0版本开始支持。
2. 应用内hsp包不能直接发布在ohpm-repo，需要获得.tgz格式的包文件，再上传到ohpm-repo。
3. 有两种获得.tgz的方法：
   * 当使用DevEco Studio软件时，点击release发布，可获得.tgz包，具体步骤请参考：[开发动态共享包](ide-hsp.md)。
   * 如果已经获得了一个包的.hsp文件和.har文件，可在两个文件所在的目录中执行tar命令生成.tgz包文件：

     ```
     1. // 打包 libhsp.har 和 libhsp.hsp 文件，生成 libhsp.tgz文件
     2. tar -czvf libhsp.tgz libhsp.har libhsp.hsp
     ```

## 执行ohpm-repo命令报错

### 在执行ohpm-repo install或者ohpm-repo start的时候报错：server install failed: YAMLException: bad indentation of a mapping entry

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/KeOEY0EfRSWiey6aRy85xw/zh-cn_image_0000002561831337.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=889B356B66C1FC56416303E78275A76F85F503D2058AF661440A064B6B588153 "点击放大")

ohpm-repo的配置文件config.yaml中配置缩进格式不对，并且在报错信息中会提示出错误的位置。

### 执行命令ohpm-repo <command>，报错ohpm-repo不存在或者<command>命令不存在。

* **报错ohpm-repo不存在**：ohpm-repo工具包解压目录中bin目录的路径没有配置到系统环境变量path中，需要手动添加[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)，或者进入bin目录，在命令前面加上 ./，即执行命令./ohpm-repo <command>方式使命令生效。
* **报错<command>命令不存在**：查询当前ohpm-repo版本是否是2.X.X，部分命令2.0.0版本之后才存在，例如install和remove\_instance。

### ohpm-repo成功启动后，根据配置文件中的listen值访问ohpm-repo私仓管理界面，界面不显示信息或者无法打开页面

* **可能性一**：浏览器和ohpm-repo不兼容导致不显示内容，当ohpm-repo成功启动后，打开ohpm-repo管理页面并不显示内容，这可能是因为当前用户使用的浏览器与ohpm-repo不兼容，请下载最新版本的浏览器，重新输入listen值进行访问。
* **可能性二**：服务未启动，执行命令ohpm-repo install和ohpm-repo start，启动ohpm-repo私仓服务。
* **可能性三**：ohpm-repo私仓管理界面访问地址不正确，请在浏览器中输入ohpm-repo配置文件config.yaml中配置的listen值。

### 机器A部署ohpm-repo私仓服务，在机器B上通过A的域名+端口访问已部署的ohpm-repo私仓服务，打开包的描述页出错

* **现象**：报错信息如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/juvKHNvNS0eQoQRxsoJamA/zh-cn_image_0000002561751361.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=B4E318FB3C7A50CC211991FCF7536C4709196789E69C273D649EC545DF7B05F4 "点击放大")
* **原因分析**：部署ohpm-repo的机器没有配置server，使用的是默认的server，host为localhost，在其他机器中不能访问。
* **解决方法**：修改部署ohpm-repo机器A的配置文件，添加store.config.server的配置。建议手动修改host为本机的ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<本机ip/域名>:8088。

### 执行ohpm-repo install时报错：fail to initialize encryption component: Error: invalid crypto component.

* **现象**：报错信息如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/yhfs8_LGSei3MnYTnbpigA/zh-cn_image_0000002561831307.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=505E2156E49999ADDD08A0057DD60A6A8BD4A62938831849F61A521D78749927 "点击放大")
* **原因分析**：在ohpm-repo私仓部署根目录deploy\_root中，加密组件meta文件受到损坏，处于失效状态。ohpm-repo私仓中，uplink的代理地址信息和证书认证的公钥信息均通过meta加密组件进行加密存储。
* **解决方法**：
  + 如果是版本升级导致的问题，请找回上一个版本中meta文件，替换当前版本的meta文件。
  + 其他原因导致meta文件损坏，需要执行如下步骤：
    1. 清空数据库中表publickey和uplinkproxy中的内容（操作数据库前请提前备份，避免误删数据影响开发）。
    2. 删除受损的meta文件。
    3. 重新执行ohpm-repo install命令，生成新的meta文件。
    4. 在ohpm-repo管理界面的仓库管理处，重新配置uplink的代理信息。
    5. 在ohpm-repo管理界面的认证管理处，重新配置证书认证的公钥数据。

## 执行ohpm publish XX.har发包到ohpm-repo私仓中报错

### 报错：connect ECONNREFUSED ::1:8089

* **现象**： 配置文件中store.config.server为http://Localhost:8089，其host为localhost，ohpm执行publish命令，命令行报如下错误

  ```
  1. ohpm ERROR request to http://Localhost:8089/repos/ohpm/Login failed, reason: connect ECONNREFUSED ::1:8089
  ```
* **原因：** 通过报错信息最后的listen值::1:8089可知：localhost没有被正确解析为127.0.0.1，而是被解析为::1，这是因为iPv6协议优先级大于iPv4协议，故localhost解析为 ::1 (127.0.0.1 ipv6的形式)。
* **解决方法**：
  + 方法一：修改iPv4的解析优先级，使其大于iPv6的优先级。
  + 方法二：把server中的localhost修改为127.0.0.1。

### 报错：The content of private key in the key\_path error.

* **现象**：ohpm执行publish命令，命令行报错信息为：

  ```
  1. The content of private key in the key_path error.
  ```
* **解决方法**：输入的密码错误，请重新输入或重新配置密钥。

### 报错：HttpCode 400 Group does not exist!

* **现象**：ohpm执行publish命令，命令行报错信息为

  HttpCode 400 Group does not exist!
* **解决方法**：有一些三方包包含组织名，只有发布包的用户在该组织下才具有发包的能力。报错信息表明三方包具有组织名，但组织未被创建。在ohpm中包的命名格式为：@<group>/<package\_name>，其中<group>为组织名，打开ohpm-repo管理界面，添加组织即可成功发布包。

### 报错：HttpCode 400 You are not a developer of the group!

* **现象**：ohpm执行publish命令，命令行报错信息为：

  ```
  1. HttpCode 400 You are not a developer of the group!
  ```

* **解决方法**：有一些三方包包含组织名，只有发布包的用户在该组织下才具有发包的能力。报错信息表明已经有管理员账户添加了该包组织，但是当前账户没有在该组织的成员里面。在ohpm中包的命名格式为@<group>/<package\_name>，其中<group>为组织名，找到创建<group>组织的负责人账户，然后负责人账户登录ohpm-repo管理界面，进入组织的详情里，添加需要发包的账户为组织的成员，成员即可发布具有对应组织名的包。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/hyHUtFPCT46cdph6eftrQQ/zh-cn_image_0000002530911388.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=E0FAF18029604CF21FB194D77803E11241329CE5C32CCECD36E724524F2FE331 "点击放大")

### 报错：ohpm ERROR: HttpCode 404 Not Found

* **现象**：ohpm执行publish命令，命令行报错信息如下：

  ```
  1. ohpm ERROR: HttpCode 404 Not Found
  ```
* **解决方法**：ohpm配置文件中的配置项publish\_registry配置错误，未配置端口或路径不全，正确的配置例如：

  ```
  1. publish_registry = http://localhost:8089/repos/ohpm
  ```

### 报错：Same ohpm package is exists!

* **现象**：ohpm执行publish命令，命令行报错信息为：Same ohpm package is exists!

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/fHRBaUQXTLeOZFn9wsI5gA/zh-cn_image_0000002530911422.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=2DA7B5E39DF1AB48FD1B10989A1AF7912A8D559D2DD2465B972AB6E4F3449556 "点击放大")
* **原因分析**：对没有组织三方库进行升级时，只能由原来发包用户升级，不能变更其他用户升级。
* **解决方法**：使用原来发包用户可以继续升级上传，不能变更用户对已经上传的包升级；如果需要支持不同用户升级上传包，包名必须带有组织名。

### 报错：Request Entity Too Large

* **现象**：ohpm执行publish命令，命令行报错信息为：Request Entity Too Large。
* **原因分析**：当使用nginx作为反向代理服务器时，发送过大的包，超过了nginx配置中设置的client\_max\_body\_size的限制。默认情况下，nginx设置此值为1MB。
* **解决方法**：修改nginx中参数client\_max\_body\_size的配置，设置一个与上架包相匹配的大小。

### 报错：The packageType is no equals the exists packageType!

* **现象**：ohpm执行publish命令，命令行报错信息为：The packageType is no equals the exists packageType!
* **原因分析**：当前上传包的包是一个har包，仓库中已经存在同名的hsp包，har包和hsp包不能够同名。
* **解决方法**：
  + 方法一：修改需要上传包的名称，避免与已经上传的hsp包同名；
  + 方法二：下架已经上传的所有同名hsp包，然后再上传同名的har包（下架包后，再次上传同名的第三方包会受限并锁定一段时间，以防止滥用。您可以通过在config.yaml文件中设置upload\_lock\_hour参数来调整这个锁定期的时长）。

## 执行ohpm install XX.har从ohpm-repo私仓中下载包报错

### ohpm-repo配置uplink后，执行install命令下载uplink所配置仓库中的包失败

* 当添加了uplink的时候，首先确认是否在管理仓库的地方，选用了新增的uplink，下图表示新增的uplink没有被选中，uplink处为空：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/EoFBWRgIQU6ogiGGG3E2yw/zh-cn_image_0000002530751414.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=47788E34AAD0ACD420DFDB4A74D7EA9BDDDEBAAB70B055EBD02548AA96E60483 "点击放大")
* 如果新增的uplink中存在所需的三方包，但是下载不下来，可能是需要配置uplink的代理信息，配置位置如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/4lDU5Et0QcqhxCRTb0s9DQ/zh-cn_image_0000002530751436.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=C7D161B038E56F9510A6D0C1305BFEF5F3D952A8D2978D275285A535D80FEE24 "点击放大")

## 访问ohpm-repo私仓管理界面报错

### 访问ohpm-repo私仓管理界面中页面功能，报错：非法请求

* **现象**：访问ohpm-repo私仓管理界面的页面功能，报错“非法请求”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/1tFfPsDwSeK6zHHQE_oarQ/zh-cn_image_0000002530751402.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=485C49E51BEDFAD84D01C53F9F06D496634D9C840D1CE2CF5C3620161900B010 "点击放大")

* **原因分析**：在ohpm-repo私仓5.0.2版本中，新增接口防重放攻击机制，该机制将校验ohpm-repo私仓所有涉及修改数据请求中的时间戳。若请求携带的时间戳与服务器当前时间相差超过1分钟（超前或滞后），系统将拒绝该请求，并返回“非法请求”错误。
* **解决方法**：为确保系统正常运行，请保持服务器与客户端浏览器时间同步。

### 访问ohpm-repo私仓管理页面，报错“加密组件无效”。

* **现象**：打开ohpm-repo私仓管理界面，访问仓库管理页面中uplink代理配置页面，或访问认证管理页面中证书认证配置页面，报错“加密组件无效”，且已经配置的信息被清空。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/hUt2b3muQTG5YbDZ4tPv7Q/zh-cn_image_0000002530751394.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=39C9036DF8B5C466FFFA8EE048B1ED7A21C89EB0C46660E1376F6B7FEEF82747 "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/bUpPZVuDRuuuWVAaQYwe2g/zh-cn_image_0000002561751351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=01889099E9F55AFDE203D2E3BD1398798F088317173373E197EC2349C9554864 "点击放大")
* **原因**：uplink代理的地址信息和证书认证的公钥信息存储均需要加密，加密组件为ohpm-repo私仓部署根目录deploy\_root中的meta文件。如果加密时的meta文件和解密时的meta文件不一致，会导致解密数据失败。
* **解决方法**：
  + 如果是版本升级导致的问题，请找回上一个版本中meta文件，替换当前版本的meta文件，保证加密组件的一致性。
  + 其他原因导致使用meta文件解密失败，需要执行如下步骤：
    1. 清空数据库中表publickey和uplinkproxy中的内容（操作数据库前请提前备份，避免误删数据影响开发）。
    2. 删除解密失败的meta文件。
    3. 重新执行ohpm-repo install命令，生成新的meta文件。
    4. 在ohpm-repo管理界面的仓库管理处，重新配置uplink的代理信息。
    5. 在ohpm-repo管理界面的认证管理处，重新配置证书认证的公钥数据。

### 访问ohpm-repo私仓管理界面，报错：“系统配置错误，请联系管理员”

* **现象**：访问ohpm-repo私仓管理界面，在ohpm-repo管理界面报错“非法请求”，在ohpm-repo运行日志报错：“verify reverse proxy usage: set "use\_reverse\_proxy" to false in config.yaml if not used, or refresh "x-forwarded-for" in Nginx if it is.”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/YbtdxSSFS9iRnAQ4fatUfw/zh-cn_image_0000002561751337.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=250222D4CA64AFF1131866C4A453D096EA151951225802871C26B6169FFD6340)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Q0OGQ-UPSp61LDUqinbxiQ/zh-cn_image_0000002530911398.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=CA1CBC03A0DF6E274A4F7453CDC18F2D9ADFE260D49293D604772C699A197F5A "点击放大")

* **原因分析**：在ohpm-repo私仓5.0.7版本中，配置文件新增配置项[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)，用于判断是否已使用反向代理。如果配置use\_reverse\_proxy值为true，但未使用反向代理或者在配置反向代理时未刷新x-forwarded-for值，将导致从请求头获取到x-forwarded-for值为空，报此错误。
* **解决方法**：只有已使用反向代理，才能够将配置项use\_reverse\_proxy置为true，且需要在反向代理配置时刷新x-forwarded-for值（如果存在多级代理，只需要在最外层代理配置），配置命令为：“proxy\_set\_header x-forwarded-for $remote\_addr”。

## 配置ohpm-repo私仓工具环境变量

### **Windows环境**

1. 在任务栏搜索框或开始菜单中，搜索“环境变量”，选择“**编辑系统环境变量**”。
2. 在弹出的“系统属性”窗口中，点击右下角的“**环境变量**”按钮。

3. 在弹出的“环境变量”窗口中，在系统变量中找到“**Path**”变量。
4. 编辑Path变量，将ohpm-repo工具包解压目录下的bin目录路径添加到新的一行中。
5. 连续点击所有打开的窗口上的“**确定**”，进行保存。
6. 重新打开命令行终端，即可使用 [ohpm-repo 相关命令](ide-ohpm-repo-command.md)。

### **Linux和macOS环境**

1. 打开命令行终端，执行以下命令编辑 .bashrc 文件。

   ```
   1. vim ~/.bashrc
   ```
2. 按 i 进入插入模式（底部显示 -- INSERT --）。
3. 在文件末尾新起一行，添加以下内容：

   ```
   1. export PATH="$PATH:[指定路径]"  // 其中的[指定路径]请替换为 ohpm-repo 工具包解压目录中 bin 目录的路径
   ```
4. 按 Esc 键退出插入模式，输入 :wq 然后按 Enter 来保存并退出。
5. 输入下面的命令使配置生效后，即可使用 [ohpm-repo 相关命令](ide-ohpm-repo-command.md)。

   ```
   1. source ~/.bashrc
   ```
