---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpmrc
title: ohpmrc
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > ohpmrc
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24ea63aaa339e535c7e686480ff85849d8b9e3cce3d971c815aececa8a50b7db
---

ohpm配置文件。

## 描述

ohpm从命令行和.ohpmrc文件中获取其配置内容。ohpm config命令可用于修改用户级.ohpmrc文件的内容。

## 文件

* 项目级配置文件：/path/to/my/project/.ohpmrc
* 用户级配置文件：~/.ohpm/.ohpmrc
* 所有 ohpm 配置文件均是 ini 格式：<key>= <value> 的参数列表

注意

* 命令行工具会优先读取项目级的配置文件。如果缺少某些配置项，将从用户级配置文件中读取缺失的配置项信息。
* 在工程任意子目录下执行ohpm命令，都可以读取到项目级的.ohpmrc配置。

## 注释

.ohpmrc 文件中以"#"或";"字符为注释符。

## 更新配置

执行如下命令可设置用户级配置：

```
1. ohpm config set key value
```

## 默认配置项

| **配置项** | **字段名称** | **字段说明** | **字段类型** | **默认值** | **备注** |
| --- | --- | --- | --- | --- | --- |
| **仓库设置** | registry | 下载仓库 | 字符串 | https://ohpm.openharmony.cn/ohpm/ | 支持配置多个仓库地址，以英文逗号分隔。系统将按照配置的先后顺序依次检索这些仓库，直到成功下载目标包。例如：当需要下载包a时，会优先从第一个配置的仓库地址查找，若未找到则自动尝试下一个仓库，依此类推。 |
| @group:registry | 指定仓库 | 字符串 | "" | 根据group指定组织的仓库地址。支持配置多个仓库地址，以英文逗号间隔，且优先级大于registry配置，系统将按照配置的先后顺序依次检索这些仓库，直到成功下载目标包。 |
| **发布设置** | publish\_registry | 发布仓库 | 字符串 | https://ohpm.openharmony.cn/ohpm/ | 配置发布的仓库地址，仅支持配置一个仓库地址。 |
| publish\_id | 用户发布号 | 字符串 | "" | 用户发布号，用来发布三方库，全局唯一。 |
| **路径设置** | cache | 缓存路径 | 字符串 | ~/.ohpm/cache | - |
| key\_path | 私钥路径 | 字符串 | "" | 利用ssh-keygen工具生成的私钥的放置路径地址。 |
| crypto\_path | 加密组件路径 | 字符串 | "" | 加密组件路径地址。详情请见：[crypto\_path](ide-ohpmrc.md#section18322038185010)。 |
| **网络设置** | no\_proxy | 不使用proxy代理 | 字符串 | "" | 配置不使用代理的仓库地址，可配置多个，以英文逗号间隔；值可以是域名或者ip，支持二级域名通配符\*（例如：\*.huawei.com）。 |
| http\_proxy | http代理 | 字符串 | "" | 支持用户名和密码的网络代理，特殊字符需要转义。示例：http://proxy\_server:port、http://username:password@proxy\_server:port。 |
| https\_proxy | https代理 | 字符串 | "" | 支持用户名和密码的网络代理，特殊字符需要转义。示例：https://proxy\_server:port、http://username:password@proxy\_server:port。 |
| strict\_ssl | ssl校验 | 布尔 | true | 默认值为true，校验https证书；若配置为false，则不校验https证书。 |
| ca\_files | ca证书路径 | 字符串 | "" | strict\_ssl=true时校验服务端证书需要的ca证书放置路径，可以放置多个证书路径，以英文逗号间隔。详情请见：[CA证书获取及配置](ide-ohpmrc.md#zh-cn_topic_0000001792216397_ca证书获取及配置)。 |
| fetch\_timeout | 请求超时时间 | 数值 | 60000 | 取值范围：[10000，360000]，单位为毫秒。如果设置的fetch\_timeout值不在取值范围内，则默认为：60000。 |
| **并发设置** | max\_concurrent | 最大并发量 | 数值 | 50 | 取值范围：[1, 200]，设置每个模块在安装时允许的最大并发量。 |
| retry\_times | 出错重试次数 | 数值 | 1 | 取值范围：[0, 5], 针对白名单内的异常，程序会按配置重试指定次数，白名单有：   * ECONNRESET：连接被对端重置 * ECONNREFUSED：连接被服务器拒绝 * ETIMEDOUT：连接超时 * RESPONSETIMEOUT：响应超时 * TARBADARCHIVE：包格式异常 |
| retry\_interval | 出错重试间隔时间 | 数值 | 1000 | 取值范围：[1000, 60000], 单位毫秒。 |
| **依赖冲突设置** | resolve\_conflict | 开启自动解决依赖版本冲突功能 | 布尔 | true | 默认开启。当设置为true或缺省时，ohpm会自动处理依赖版本冲突，详情请见：[resolve\_conflict](ide-ohpmrc.md#section368717475562)。 |
| resolve\_conflict\_strict | 开启严格模式依赖冲突处理功能 | 布尔 | false | 默认关闭。当设置为true时，ohpm会按照严格模式处理依赖版本冲突，详情请见：[resolve\_conflict\_strict](ide-ohpmrc.md#section1942983310492)。 |
| **安全设置** | key\_passphrase | 已加密的私钥密码 | 字符串 | "" | 默认为空，使用加密命令将私钥密码加密，执行涉及公私钥的认证命令时，自动使用key\_passphrase对私钥文件进行解密，无需用户手动输入私钥密码。详情请见：[key\_passphrase](ide-ohpmrc.md#section10698175182316)。 |
| **其他设置** | log\_level | 日志级别 | 字符串 | info | 可设置日志输出级别，对应级别类型有debug、info、warn、error。详情请见：[log\_level](ide-ohpmrc.md#section1539817345376)。 |
| install\_all | 是否安装工程所有模块的依赖 | 布尔 | true | 默认为true。当设置为true或缺省时，在执行ohpm install、ohpm update、ohpm uninstall时，将会安装工程下所有模块的依赖。详情请见[install\_all](ide-ohpmrc.md#section1260011476535)。 |
| :\_auth和:\_read\_auth | AccessToken配置项 | 字符串 | 无 | ohpm-repo支持使用access token进行认证。详情请见[AccessToken](ide-ohpmrc.md#section74219299467)。 |
| enforce\_dependency\_key | 开启依赖名称校验 | 布尔 | false | 默认为false。设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。详情请见[enforce\_dependency\_key](ide-ohpmrc.md#section920325116547)。 |
| ensure\_dependency\_include | 开启依赖扫描功能 | 布尔 | false | 默认为false。从ohpm 1.7.0开始，在执行ohpm publish命令时，会检查发布包的源码中，静态导入的三方依赖是否都声明在oh-package.json5的dependencies或dynamicDependencies中。若缺少依赖声明且字段设置为false时，会提示相应告警信息；设置为true时，则会使命令执行失败并提示错误信息。详情请见[ensure\_dependency\_include](ide-ohpmrc.md#section1291814578276)。 |
| projectPackageJson:<project\_root> | 工程oh-package.json5配置覆盖 | 字符串 | 无 | 用于覆盖工程根目录下oh-package.json5中的配置。   * 配置项名称中的<project\_root>表示工程根目录路径（根据实际情况替换为真实的工程根目录路径）。 * 配置项的值为指定的工程级oh-package.json5文件的路径，支持使用相对路径（当使用相对路径时，根路径为<project\_root>）。   详情请见[.ohpmrc中projectPackageJson配置](ide-oh-package-json5.md#section140251819254)。 |
| disallow\_nested\_package | 开启包内.har/.tgz依赖  配置路径检测 | 布尔 | false | 默认为false。设置为true后，在执行prepublish/publish时，会扫描包内是否存在'./'形式配置且后缀为.har/.tgz格式的依赖，如果存在，则会使命令执行失败并提示报错信息。详情见[disallow\_nested\_package](ide-ohpmrc.md#section1237023983514)。 |
| odm\_r2\_project\_root | 开启overrideDependencyMap中相对路径自动转换功能 | 布尔 | false | 默认为false。设置为true后，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情见[odm\_r2\_project\_root](ide-ohpmrc.md#section136621053184912)。 |
| enable\_cross\_process\_lock | 启用跨进程锁 | 布尔 | false | 默认为false。由于oh\_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令，若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，则必须将该配置设置为true，以保证这多个命令以串行的方式运行。 |
| compability\_log\_level | 兼容性字段检测日志等级 | 字符串 | warn | 默认为warn。在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），如果未配置，则会根据日志等级打印提示或报错。详情请见[compability\_log\_level](ide-ohpmrc.md#section96369529419)。 |
| use\_stream\_threshold\_size | 流式上传阈值 | 数值 | 5 | 取值范围：[0, 300]，单位mb。当publish三方库的文件体积大于此阈值时将会使用流式上传三方库，如果仓库不存在流式上传接口则自动转为Base64方式上传。 |
| lockfile\_stable\_order | oh-package-lock.json5内容稳定排序 | 布尔 | false | 默认为false。若设置为true，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。 |
| enable\_unified\_lockfile | lockfile合一 | 布尔 | false | 默认为false。若设置为true，会将所有模块的oh-package-lock.json5文件整合进项目下的oh-package-lock.json5。详情请见[enable\_unified\_lockfile](ide-ohpmrc.md#section101671095818)。 |
| enable\_boost\_extraction\_speed | 文件解压提速 | 布尔 | false | 默认为false。若设置为true，在ohpm安装时，会使用更高效的文件解压方法，该功能当前处于实验阶段，详情请见[enable\_boost\_extraction\_speed](ide-ohpmrc.md#section20410165616573)。 |
| enable\_lock\_inner\_pkg\_version | 依赖内部的.har或.tgz依赖版本锁定 | 布尔 | true | 默认为true。若设置为false，在ohpm安装时，不会将依赖内部的.har或.tgz子依赖的版本保存至oh-package-lock.json5，详情请见[enable\_lock\_inner\_pkg\_version](ide-ohpmrc.md#section1834543398)。 |
| case\_sensitive\_check | 路径大小写敏感检测 | 布尔 | false | 默认为false。若设置为true，在执行ohpm相关命令时，如果ohpm检测到工程中文件的配置路径和文件的实际路径存在大小写不一致问题时，则会报错提示开发者修改，详情请见[case\_sensitive\_check](ide-ohpmrc.md#section2045412394117)。  该配置项仅在Windows环境下生效。 |

## CA证书获取及配置

说明

CA证书的获取需要区分系统：当从Windows系统浏览器下载的证书仅适用于Windows系统，当从Mac系统浏览器中获取的证书适用于Mac系统和Linux系统。

### Windows系统获取CA证书

依次访问以下证书下载地址，并根据下图操作下载CA证书到本地：

```
1. https://ohpm.openharmony.cn/
2. https://contentcenter-drcn.dbankcdn.cn/   //该域名用于文件资源下载，访问根路径仅可用于获取CA证书
```

访问https://ohpm.openharmony.cn/地址，下载证书，请选择保存类型为**证书链**（访问https://contentcenter-drcn.dbankcdn.cn/ 执行相同操作）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ofIaZ9tUTlmxaDsM476sHw/zh-cn_image_0000002530753130.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=BAF3F359187F9BA378A163FFFD66C11C968B543DB2B9592CD864DE1BB5C5E1BA "点击放大")

通过访问https://ohpm.openharmony.cn/地址获取证书openharmony.cn.crt，通过访问https://contentcenter-drcn.dbankcdn.cn/地址获取证书update.hicloud.crt，在 .ohpmrc 文件中配置 ca\_files=证书路径1，证书路径2（两个文件均需配置）。

```
1. ca_files=D:\_.openharmony.cn.crt,D:\update.hicloud.crt
```

### Mac系统获取CA证书

依次访问以下证书下载地址，并根据下图操作下载CA证书到本地：

```
1. https://ohpm.openharmony.cn/
2. https://contentcenter-drcn.dbankcdn.cn/   //该域名用于文件资源下载，访问根路径仅可用于获取CA证书
```

访问https://ohpm.openharmony.cn/地址，下载证书，请选择保存类型为**证书链**（访问https://contentcenter-drcn.dbankcdn.cn/ 执行相同操作）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/TAakNA8YRb6SfJk6PcPmFA/zh-cn_image_0000002561833063.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=BD248B586C58435402D85C59CACEBE86F5D5B97FBFF8C6921AE43223316218F2 "点击放大")

通过访问https://ohpm.openharmony.cn/地址获取证书openharmony.cn.pem，通过访问https://contentcenter-drcn.dbankcdn.cn/地址获取证书update.hicloud.pem，在 .ohpmrc 文件中配置 ca\_files=证书路径1，证书路径2（两个文件均需配置）。

```
1. ca_file=/Users/用户名/_.openharmony.cn.pem,/Users/用户名/_.update.hicloud.pem
```

## log\_level

可设置ohpm日志输出级别，对应级别类型有debug、info、warn、error，默认为：info。开发者在执行ohpm命令时，不同日志级别的区别和效果如下所示。

* debug：控制台会打印debug、info、warn、error日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/HO7ElxS5S8y9D3l1SuExzg/zh-cn_image_0000002530753164.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=0DBEB141582ED95E5415EEE85773857AF5C19D56EDE1D41D1AAADBD56F38ABD7)
* info：控制台会打印info、warn、error日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QspZene6Tsy3kTgSXb2oNA/zh-cn_image_0000002561833055.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=4EDD3761F17C86DEB9A0D54A6BDA2264FBFCD905F9F1A8E20A2BD26C0D775D7A)
* warn：控制台会打印warn、error日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/c6EUyeB0RrmUU4D6PnKwhw/zh-cn_image_0000002530753138.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=81BF1D7223195FB38FD96A17741DDEFAD56FCE0AAC2BFB6AC68917DA79C9ECCB)
* error：控制台只会打印error日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/owXktjYRTkSjyLs8ti_q0A/zh-cn_image_0000002530753144.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=69C1830ADA4DC6DC308D980F31D6F12C87436A1889516FA055FFB21A042CA28C)

## install\_all

在ohpm客户端1.8.0版本的.ohpmrc中支持install\_all配置，用于控制ohpm install，ohpm update，ohpm uninstall的行为，install\_all在.ohpmrc文件中设置为true或缺省时：

* 使用ohpm install命令时，将安装工程下所有模块的依赖，与使用ohpm install --all行为一致；
* 使用ohpm update时，将默认更新本模块下依赖并安装工程下所有模块的依赖，与使用ohpm update --all一致；
* 使用ohpm uninstall时，将默认删除本模块下依赖并安装工程下所有模块的依赖，与使用ohpm uninstall --all一致。

## resolve\_conflict

在ohpm客户端1.5.0版本开始支持依赖版本冲突自动解决功能。只需要在.ohpmrc文件中，将resolve\_conflict配置为true或缺省，即可开启该功能。依赖冲突的处理策略为：当您的项目同时依赖了某个三方库的不同版本时，ohpm将选择其中的最高版本进行安装。

注意

若某个三方库同时存在远程版本和本地版本（本地文件或源码依赖），无论本地版本的版本号是否大于远程版本，ohpm的冲突处理策略都会优先选择本地版本作为待安装的版本。

### 模块内依赖版本冲突

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/W2BYoeELRtSjUNDvpNhXTQ/zh-cn_image_0000002561833039.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=50F68AE95C40C653FE37D818A06190F178816634A77D19D0583BCE3F808A733C)

如上图所示的依赖路径中，moduleA 为您正在开发的模块，其直接依赖为 B@1.1，C@1.1。其中 B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/__WurYkSSmaw9UcRmEM_fg/zh-cn_image_0000002530913128.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=8D3237DB591E28757BCFC5511B5016851F585DE4AA7D6BCB13FC4125BC0792A7)

### 模块间依赖版本冲突

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/YvdLuj5kS_-3yPzMGHhgAw/zh-cn_image_0000002530913118.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=B696220C17420B228944B171564981E68A2599F0A242376D5F0C370415CB9F3A)

如上图所示的依赖路径中，moduleA、moduleB 为您同一项目下正在开发的两个模块，其中moduleA 依赖 B@1.1，moduleB 依赖 C@1.1，B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，并且您是使用 ohpm install --all 进行安装时，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/qV6uNYHEQqWWLauEKFtEgw/zh-cn_image_0000002530753128.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=246B1FE6C20059F36CF1F587D13FD347BA251300B481EEAD5FDAA390C3BDFAF6)

### 更新依赖版本的场景

当您希望将您某个模块的直接依赖更新成另一个版本，如下图所示，您手动将 C@1.1 更新为 C@1.2：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Dk79zPxjSY6ibwc83ohLeQ/zh-cn_image_0000002561753077.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=1B5D4DF8DD13F82831DFA0CE28E97F81ACFA5D7E091FD940D9E62703B08B2FA5)

由于 C 更新为 C@1.2 后，不再依赖 D，若依赖 D 的版本在更新 C 版本之前已经通过 ohpm 的自动冲突处理机制锁定为 D@1.3 版本，此时 C 版本的升级将不会导致 D 的版本由 D@1.3 回退为 D@1.2，这样可以保证每一次更新都只是在上一次结果上进行影响最小的修改，最终的依赖路径将会被解析为下图蓝色箭头所指向的路径：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/3mPkHrV3RZewEtZR3owOig/zh-cn_image_0000002530753158.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=26FA9E207A9BDDDD99EC910CE3C32F0648F848F2996F3E604479F09738527092)

对于上述场景，如果希望D版本同时也回退至D@1.2版本，则需要在ohpm install之前执行ohpm clean命令清理各模块下的oh-package-lock.json5文件，以消除上一次安装结果的影响。

### ohpm install命令带--target\_path选项时依赖冲突处理

target\_path下是hvigor在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），详见[target\_path](ide-ohpm-install.md#section79331822125611)。在生成的oh-package.json5中，依赖的版本部分可能包含targetName，示例："version": "1.0.0+targetName"。

包含targetName信息的版本完整格式为：<major>.<minor>.<patch>[-<pre-release>][+<targetName>]，此时冲突处理规则如下：

1、<major>.<minor>.<patch>[-<pre-release>]部分的比较规则依然遵循上文各场景所描述的处理规则，即取版本号最大的依赖。

2、当两个版本<major>.<minor>.<patch>[-<pre-release>]部分一致时，取尾部有[+<targetName>]信息的依赖。

注意

1、当两个版本尾部均有[+<targetName>]信息，且targetName不一致时，会根据<target\_path>/dependencyMap.json5中targetName是否为空进行区分处理。

* 当targetName空时，打印警告提示。
* 当targetName有值时，报错提示并中断程序。

2、当两个依赖中有一个是本地依赖时，优先取本地依赖；当两个依赖均是本地依赖时，获取本地依赖包内oh-package.json5配置的version再次按照上述规则继续比较。

### 限制条件说明

1. 若希望解决当前项目所有模块下的依赖版本冲突，请使用ohpm install --all完成依赖安装。
2. 若在执行ohpm update或ohpm uninstall命令后，可能会破坏项目原有的依赖版本冲突处理结果。请额外执行一次ohpm install --all命令，重新处理当前项目所有模块下的依赖版本冲突。
3. 当本地文件（.har或.tgz后缀）依赖之间、本地源码模块依赖之间、本地文件（.har或.tgz后缀）依赖与本地源码模块依赖之间出现冲突时，ohpm自动冲突处理机制会比较该依赖内部oh-package.json5文件中version字段配置的版本号大小，版本号大的将会被安装。

   注意

   如难以感知本地文件或本地源码依赖中的版本号，建议使用[overrides](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)来处理冲突。

## resolve\_conflict\_strict

ohpm客户端从5.0.9版本，开始支持严格的依赖版本冲突处理机制。在.ohpmrc文件中，将resolve\_conflict\_strict配置为true开启该功能。

严格模式下，当您的项目同时依赖了某个三方库的不同版本时，ohpm将按照严格模式冲突决策算法决策出最符合要求的版本进行安装，当程序不能决策出符合要求的版本时将报错。

### 严格模式冲突决策算法

* 同一依赖，存在一个固定版本（如：1.0.1）、多个范围版本（如：^1.0.0、~1.1.0、>1.0.0等）时，如果该固定版本在所有范围版本交集区间内，则最终安装该固定版本，否则冲突决策失败；
* 同一依赖，仅存在多个范围版本时，如果所有范围版本存在交集，则最终安装仓库中存在且在交集区间内的最高版本；若所有范围版本不存在交集区间，则冲突决策失败；
* 使用同一本地依赖（如：./a.har），依赖存放路径不一致时，冲突决策失败；
* 同一依赖，同时存在本地版本（如：./a.har）与远程版本（如：^1.0.0）时，冲突决策失败；
* 同一依赖，存在多个固定版本时，冲突决策失败。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Lt70vLDNRY2GtZmG3p_HoA/zh-cn_image_0000002561753091.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=A015DF5986FAF1E255E5E2126A7C7F049E9A30D618A3A933F1F517C301253F19 "点击放大")

注意

1. 严格模式下，依赖冲突决策成功时，ohpm会打印被解决冲突的依赖的警告信息，包含：依赖名称、所有冲突的版本、最终安装版本、受影响的模块列表。
2. 严格模式下，依赖冲突决策失败时，ohpm会打印依赖冲突树并在树上高亮显示解决失败的依赖及版本和所有解决失败的依赖的错误信息，包含：依赖名称、所有冲突的版本。当依赖存在版本冲突时，可以通过[overrides](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)配置解决。

### 示例

1. 将resolve\_conflict\_strict开关设置为true：

   ```
   1. ohpm config set resolve_conflict_strict true
   ```
2. 在AppTest3工程根目录的oh-package.json5中配置依赖@ohos/axios：

   ```
   1. {
   2. "modelVersion": "6.1.0",
   3. "description": "Please describe the basic information.",
   4. "dependencies": {
   5. "@ohos/axios": "2.2.5"
   6. }
   7. }
   ```
3. 在AppTest3工程下entry模块的oh-package.json5中配置依赖@ohos/axios：

   ```
   1. {
   2. "name": "entry",
   3. "version": "1.0.0",
   4. "description": "Please describe the basic information.",
   5. "main": "",
   6. "author": "",
   7. "license": "",
   8. "dependencies": {
   9. "@ohos/axios": "2.2.6"
   10. }
   11. }
   ```
4. 在AppTest3工程下任意目录执行命令：ohpm install --all，根据严格的依赖版本冲突处理规则，此时ohpm会安装失败并打印依赖冲突树，如下所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/x8j4oElfSg-S9sDAgmfnpg/zh-cn_image_0000002561833049.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=155F10344F5A11D0FA05CB30CF0A2BD66F18BC9C02B3EF9E83DC8E840D9160E9)

## crypto\_path

ohpm客户端从5.2.0版本开始，支持对敏感配置项进行加密存储和读取。

**支持加密的敏感配置项**：

| 配置项 | 说明 | 示例格式 |
| --- | --- | --- |
| [key\_passphrase](ide-ohpmrc.md#section10698175182316) | 必须加密，对应 key\_path 的私钥密码 | key\_passphrase=security:xxx |
| http\_proxy | 代理用户名密码部分可加密（username:password替换为密文） | http\_proxy=http://security:xxx@proxy:port |
| https\_proxy | 代理用户名密码部分可加密（username:password替换为密文） | https\_proxy=https://security:xxx@proxy:port |
| [AccessToken](ide-ohpmrc.md#section74219299467) | 仓库认证配置（:\_auth 和 :\_read\_auth） | //<仓库地址>/:\_auth=security:xxx  //<仓库地址>/:\_read\_auth=security:xxx |

用户可通过以下流程实现配置加密：

1. 使用 [ohpm config encrypt](ide-ohpm-config.md#section1085417514102) 命令生成加密组件并对标准输入的数据加密。
2. 在 .ohpmrc 文件中配置 crypto\_path 加密组件路径和敏感配置项。

   ```
   1. crypto_path=D:\path\to\crypto_dir
   2. key_passphrase=security:xxx
   3. http_proxy=http://security:xxx@proxy:port
   4. https_proxy=https://security:xxx@proxy:port
   5. //<仓库地址>/:_auth=security:xxx
   6. //<仓库地址>/:_read_auth=security:xxx
   ```

说明

1、key\_passphrase 配置项必须使用密文格式配置，其余敏感配置项仍兼容明文配置。

2、命令执行时，根据优先级（项目级 > 用户级 .ohpmrc）获取命令所需的敏感配置项后，使用该配置项同层级的 crypto\_path 指定的加密组件进行解密。

## key\_passphrase

ohpm 客户端从5.2.0版本开始，支持在 .ohpmrc 文件中配置 key\_passphrase 私钥密码，用于自动解密 key\_path 对应的私钥文件。

* 执行 ohpm publish、ohpm unpublish 等需要认证的命令时，系统会自动使用 key\_passphrase 解密私钥，无需手动输入密码。
* key\_passphrase 必须是通过 [ohpm config encrypt](ide-ohpm-config.md#section1085417514102) 命令生成的密文。
* 需同时配置 key\_path 私钥文件路径。
* 需同时配置 [crypto\_path](ide-ohpmrc.md#section18322038185010) 加密组件路径，用于运行时解密 key\_passphrase。

**示例**

在项目级或用户级 .ohpmrc 文件中配置，执行 publish 命令，用户无需手动输入密码即可完成推包操作。

```
1. key_path=:\path\to\key_file
2. crypto_path=D:\path\to\crypto_dir
3. key_passphrase=security:xxx
```

## AccessToken

AccessToken是 ohpm-repo 2.1.0版本新引入的认证机制，用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。

在与 ohpm-repo 交互时，客户端会自动附带Token进行身份验证。该Token分两种权限等级：

1. 只读Token允许执行info和install操作；
2. 读写Token除了包含只读权限外，还支持publish和unpublish操作。

每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。

### 如何获取AccessToken

当前AccessToken仅 ohpm-repo 支持，登录成功后，在ohpm-repo首页的右上角 > 认证管理 > AccessToken页面进行生成。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/rr89t98mRMuryS8x4Y_bbA/zh-cn_image_0000002561833079.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=F23A17BCBE27A325E907C115CE2CD77A0A896BEDFC3D59141D94F01EAE60731C)

### 如何配置AccessToken

在".ohpmrc"文件配置示例如下：

```
1. //127.0.0.1:8088/repos/ohpm/:_auth=readWriteToken
2. //127.0.0.1:8088/repos/ohpm/:_read_auth=readOnlyToken
```

其中 ：

* //127.0.0.1:8088/repos/ohpm/ 是ohpm-repo的registry地址去除协议名的部分；
* :\_auth 和 :\_read\_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish操作时只会使用读写Token。每种Token最多配置三条。

## enforce\_dependency\_key

ohpm从1.7.0版本开始，支持在.ohpmrc文件中配置enforce\_dependency\_key，该配置项值为布尔类型，默认为false。将配置设置为true后，ohpm会校验各模块的oh-package.json5中配置的直接依赖中的本地依赖名称与其对应的包名（模块名）是否一致，若不一致会导致依赖安装失败并在错误日志中打印出不一致的依赖名称与其对应的包名（模块名）。

**示例：**

在MyApplication工程下存在一个名称为foo的模块，foo模块的oh-package.json5如下所示：

```
1. {
2. "name": "foo",
3. "version": "2.0.0",
4. "description": "Please describe the basic information.",
5. }
```

在MyApplication工程下存在另一个名称为bar的模块，且bar模块中依赖了foo模块，bar模块的oh-package.json5如下所示：

```
1. {
2. "name": "bar",
3. "version": "1.0.0",
4. "description": "Please describe the basic information.",
5. "dependencies": {
6. "fee": "file:../foo"
7. },
8. }
```

如上所示，bar模块的oh-package.json5中配置了对foo模块的依赖，并为foo模块起了一个别名为fee。当在.ohpmrc中将enforce\_dependency\_key配置为true时：

```
1. enforce_dependency_key=true
```

此时在MyApplication下执行ohpm install --all命令将打印如下错误日志，同时会中断命令的执行：

```
1. ohpm ERROR: local dependency "fee" found in "D:\DevecostudioProjects\MyApplication2\bar\oh-package.json5" does not match the actual name "foo" of its oh-package.json5
2. ohpm ERROR: Install failed, detail: There are some dependency names that are inconsistent with the actual package names.
```

若没有配置enforce\_dependency\_key或将其配置为false时，命令将不会被中断，同时上述错误日志的日志级别将会下调为告警日志：

```
1. ohpm WARN: local dependency "fee" found in "D:\DevecostudioProjects\MyApplication2\bar\oh-package.json5" does not match the actual name "foo" of its oh-package.json5
```

建议在.ohpmrc文件中配置enforce\_dependency\_key为true，禁止以别名的方式配置本地依赖，避免出现如下场景：

基于上述示例，在MyApplication下真的存在一个名称为fee的模块，且该模块的版本号小于foo模块，fee模块的oh-package.json5如下所示：

```
1. {
2. "name": "fee",
3. "version": "1.0.0",  // 小于foo的版本号2.0.0
4. "description": "Please describe the basic information.",
5. }
```

且entry模块中同时依赖了fee与bar，entry模块的oh-package.json5依赖配置如下所示：

```
1. {
2. "name": "entry",
3. "version": "1.0.0",
4. "dependencies": {
5. "fee": "file:../fee",
6. "bar": "file:../bar"
7. },
8. }
```

此时在entry的依赖树中，依赖fee存在两个版本：一个别名为fee的foo模块，一个名称为fee的fee模块，若此时开启了[resolve\_conflict](ide-ohpmrc.md#section368717475562)，由于fee模块的实际版本号为1.0.0要小于foo模块的版本号2.0.0，在执行ohpm install时将只会在entry模块的oh\_modules下安装以fee为别名的foo模块，而实际的fee模块则不会被安装，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/IyI6x4YGR_6GnBcGsii5iw/zh-cn_image_0000002530913160.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=E98366498D893D8B2141086CD578675EB8D9E6342AE4E7123FB91EF3EFB3344D "点击放大")

在entry的oh\_modules下会生成一个名称为fee的软链接，该链接却指向foo模块的实际路径：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/GeWqO0jUQO219GKa0Xq05w/zh-cn_image_0000002561753059.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=B89DCF21FF8396F8388C0CEFF6906C6D53BC145446AB7F46DA818D86CF7272A5 "点击放大")

如果entry实际希望依赖的是真实的fee模块而不是foo模块，则此时会导致entry无法编译成功。

注意

1、从ohpm客户端5.0.7开始，若项目级build-profile.json5文件中strictMode字段下配置了useNormalizedOHMUrl开关且useNormalizedOHMUrl=true，则该配置优先级高于enforce\_dependency\_key，如果ohpm检测到依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行；若未配置useNormalizedOHMUrl或useNormalizedOHMUrl=false时，是否校验别名一致性则根据enforce\_dependency\_key配置决定。

2、项目级build-profile.json5文件中，products节点下任意product字段配置了useNormalizedOHMUrl=true，则ohpm中useNormalizedOHMUrl开关会被设置为true，即ohpm检测到项目中依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行。

## ensure\_dependency\_include

ohpm从1.7.0版本开始，支持在.ohpmrc文件中配置ensure\_dependency\_include，该配置项值为布尔类型，默认为false。

在ohpm prepublish/publish时，ohpm会扫描待发布包的内容，如果代码中import了某个包的内容，但相应的包没有配置在dependencies/dynamicDependencies中，即如果该配置项的值为true，则ohpm会打印错误信息并中断执行；否则，ohpm只会打印告警提示。

例如，test.har包的代码中import了@ohos/hypium包，但test.har的oh-package.json5的dependencies中未配置@ohos/hypium依赖。下面就ensure\_dependency\_include开关为true/false时ohpm publish的行为进行举例说明。

### 示例1

1. 将ensure\_dependency\_include开关置为false：

   ```
   1. ohpm config set ensure_dependency_include false
   ```
2. 发布test.har包。

   ```
   1. ohpm publish test.har
   ```
3. 当ensure\_dependency\_include=false时，发布完成后将打印告警提示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/_9WN3D5hRlaq7H263o7LUA/zh-cn_image_0000002561833057.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=23E732AD674247E748122BCA715468559AA3BDDE01B4576064744EC44524F7EF)

### 示例2

1. 将ensure\_dependency\_include开关置为true：

   ```
   1. ohpm config set ensure_dependency_include true
   ```
2. 发布test.har包。

   ```
   1. ohpm publish test.har
   ```
3. 当ensure\_dependency\_include=true时，发布时将报错。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nVVHtEofQTGiKYsQoNcvwg/zh-cn_image_0000002530753152.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=A88A074C06CC1C5322C79F7E73BC998AB02ABEDF78FA01A5D251EAE99483D951)

## disallow\_nested\_package

ohpm从1.8.0版本开始，支持在.ohpmrc文件中配置disallow\_nested\_package，该配置项值为布尔类型，默认为false。在ohpm prepublish/publish时，ohpm会扫描待发布包的dependencies和dynamicDependencies依赖配置，如果依赖配置中存在相对路径或绝对路径配置的.har、.tgz依赖且disallow\_nested\_package开关为true，则ohpm会报错提示。

### 示例

1. lib\_nested.har包的dependencies中配置了如下依赖：

   ```
   1. {
   2. "dependencies": {
   3. "liblib_nested.so": "file:./src/main/cpp/types/liblib_nested",
   4. "hsp": "./libs/hsp-default.tgz",
   5. "lib_har": "./libs/lib_har.har"
   6. }
   7. }
   ```
2. 将disallow\_nested\_package 开关置为true。

   ```
   1. ohpm config set disallow_nested_package true
   ```
3. 发布lib\_nested.har。

   ```
   1. ohpm publish lib_nested.har
   ```
4. 当disallow\_nested\_package=true时，发布时将报错。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/VE8mTjk-TRiXlxo4hkIq_g/zh-cn_image_0000002561753069.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=5EE41F5D0BEB1EBC310195B4D9F75FA009525BA3C417DBEDD57A878E0E073649)

## odm\_r2\_project\_root

odm\_r2\_project\_root是ohpm客户端1.8.0新增的开关配置，默认为false，可以通过config命令或直接在.ohpmrc文件中修改其值。

当该配置为true时，若在overrideDependencyMap中配置的依赖项替换文件中存在以相对路径配置的本地依赖项时，在ohpm运行时会基于工程根路径来查找这些本地依赖项。

示例：

1. .ohpmrc中开启odm\_r2\_project\_root：

   ```
   1. odm_r2_project_root=true
   ```
2. overrideDependencyMap配置示例：

   在工程根目录下的oh\_package.json5中增加overrideDependencyMap配置，如下：

   ```
   1. {
   2. "overrideDependencyMap": {
   3. "lib1": "lib1-override-dep-map.json5",
   4. "lib2": "lib2-override-dep-map.json5"
   5. }
   6. }
   ```
3. 依赖项"lib1"的依赖项替换文件lib1-override-dep-map.json5示例：

   ```
   1. {
   2. "dependencies": {
   3. "@ohos/test": "file:./test.har"
   4. }
   5. }
   ```

如上第3步所示，当odm\_r2\_project\_root开关设置为true时，在ohpm运行时会以工程根目录为起点查找"./test.har"，比如：工程根路径为：D:\path\to\MyProject，在ohpm运行时解析得到test.har的绝对路径为：D:\path\to\MyProject\test.har。

## compability\_log\_level

ohpm客户端从5.0.1开始新增开关配置'compability\_log\_level'字段，用于控制在缺少兼容性检测需要的字段时ohpm的处理逻辑。

compability\_log\_level字段默认赋值为'warn'，可配置的日志等级请见[开关配置项说明](ide-ohpmrc.md#section139481140114517)。

在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），详见[模块级oh-package.json5字段说明](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)，下面统称 '兼容性字段'，如果未配置，则会根据日志等级打印提示或报错。

### 开关配置项说明

* close：关闭功能，不主动检测兼容性字段。
* info：检测到未配置的兼容性字段时，打印info日志。
* warn：检测到未配置的兼容性字段时，打印警告日志。
* error：检测到未配置的兼容性字段时，打印报错提示并中断程序。

## enable\_unified\_lockfile

ohpm客户端从5.1.1开始新增开关配置enable\_unified\_lockfile字段。启用此特性后，ohpm将自动整合项目中所有子模块的oh-package-lock.json5文件，统一生成至项目根目录的oh-package-lock.json5文件中。

启用enable\_unified\_lockfile=true后，项目级统一管理lockfile锁文件，针对模块间存在重复依赖的场景，显著减少ohpm install耗时，优化构建流程。

注意

启用enable\_unified\_lockfile=true后，原分散在各模块下的.hsp依赖安装目录将统一迁移至项目根目录。在流水线上开启此特性时，需搭配配套的hvigor使用。

## enable\_boost\_extraction\_speed

ohpm客户端从5.3.0开始新增开关配置enable\_boost\_extraction\_speed字段。ohpm安装时涉及对.har/.tgz三方包文件的解压和遍历，启用此特性后，将使用高性能方法进行解压和遍历，当工程中存在大文件依赖时，可以显著减少ohpm install耗时。该功能当前处于实验阶段，暂不支持解压包含软链接的三方包文件。

## enable\_lock\_inner\_pkg\_version

ohpm客户端从5.3.1开始新增开关配置enable\_lock\_inner\_pkg\_version字段。默认为true，若设置为false，在ohpm安装时，不会将依赖内部的.har或.tgz子依赖的版本保存至oh-package-lock.json5，以防oh-package-lock.json5中保存不存在的路径导致二次安装报错。

如下图所示，蓝色箭头标识最终要安装的依赖，安装的依赖D@1.0.0来自依赖B@1.0.0（依赖名称和依赖版本相同的依赖会被定性为相同依赖，最终安装哪个由依赖构建先后顺序决定）, 因B@1.0.0并没有安装，但oh-package-lock.json5中锁定了依赖D的版本，在二次安装时会爆出D的依赖路径不存在错误，此时需要将该开关设置为false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/oaoHxz3KSPiqsDfJ57HTqw/zh-cn_image_0000002561753083.png?HW-CC-KV=V1&HW-CC-Date=20260427T235738Z&HW-CC-Expire=86400&HW-CC-Sign=23E5D2EE0DADD78DB8481C83D177AF9E41CCF00B4A9E571537E6A5D3DAD0337F)

**oh-package-lock.json5示例**

1. 生成library.har，oh-package.json5如下。

   ```
   1. {
   2. "name": "library",
   3. "version": "1.0.0",
   4. "description": "Please describe the basic information.",
   5. "author": "",
   6. "license": "Apache-2.0",
   7. "dependencies": {
   8. "inner": "./libs/inner.har"
   9. },
   10. "types": "Index.d.ets",
   11. "artifactType": "obfuscation",
   12. "compatibleSdkVersion": 21,
   13. "compatibleSdkType": "HarmonyOS",
   14. "obfuscated": false
   15. }
   ```
2. entry依赖library.har，oh-package.json5如下。

   ```
   1. {
   2. "name": "entry",
   3. "version": "1.0.0",
   4. "description": "Please describe the basic information.",
   5. "main": "",
   6. "author": "",
   7. "license": "",
   8. "dependencies": {
   9. "library": "./library.har"
   10. }
   11. }
   ```
3. .ohpmrc中配置开关：enable\_lock\_inner\_pkg\_version=false，工程任意目录下执行命令：ohpm install --all，此时生成的entry/oh-package-lock.json5中不会锁定内部包inner的版本，如下所示。

   ```
   1. {
   2. ......
   3. "specifiers": {
   4. "library@library.har": "library@library.har"
   5. },
   6. "packages": {
   7. "library@library.har": {
   8. "name": "library",
   9. "version": "1.0.0",

   11. "resolved": "library.har",
   12. "registryType": "local",
   13. "dependencies": {
   14. "inner": "./libs/inner.har"
   15. }
   16. }
   17. }
   18. }
   ```

   enable\_lock\_inner\_pkg\_version=true时，entry/oh-package-lock.json5结果如下：

   ```
   1. {
   2. ......
   3. "specifiers": {
   4. "inner@../oh_modules/.ohpm/library@85ursk4cfzbgycewlyxweed+cyyeeixxig5mlazoo+g=/oh_modules/library/libs/inner.har": "
   5. inner@../oh_modules/.ohpm/library@c0jkxsxl3amvdd7rr1enrkrejzharxwucdoyc29br+u=/oh_modules/library/libs/inner.har",
   6. "library@library.har": "library@library.har"
   7. },
   8. "packages": {
   9. "
   10. inner@../oh_modules/.ohpm/library@c0jkxsxl3amvdd7rr1enrkrejzharxwucdoyc29br+u=/oh_modules/library/libs/inner.har
   11. ": {
   12. "name": "inner",
   13. "version": "1.0.0",
   14. "resolved": "../oh_modules/.ohpm/library@c0jkxsxl3amvdd7rr1enrkrejzharxwucdoyc29br+u=/oh_modules/library/libs/inner.har"
   15. "registryType": "local"
   16. },
   17. "library@library.har": {
   18. "name": "library",
   19. "version": "1.0.0",
   20. "resolved": "library.har"
   21. "registryType": "local",
   22. "dependencies": {
   23. "inner": "./libs/inner.har"
   24. }
   25. }
   26. }
   27. }
   ```

## case\_sensitive\_check

ohpm客户端从6.21.0新增开关配置"case\_sensitive\_check"字段。若设置为true，在执行ohpm相关命令时，如果ohpm检测到工程中文件的配置路径和文件的实际路径存在大小写不一致问题时，则会报错提示开发者修改。该配置项仅在Windows环境下生效。

**检测范围**

* .har包、.tgz包、工程中的module作为依赖时的路径。
* prefix、target\_path、parameterFile的命令中配置的目录或路径。
* overrides配置项中的本地依赖路径，overrideDependencyMap配置项涉及的配置文件及文件内的本地依赖路径，parameterFile配置文件及文件内的本地依赖路径。

**示例**

1. 准备本地har包：test.har，该har包内oh-package.json5中name为：test，将其放置在模块entry的libs目录下。
2. entry依赖test.har，则原始依赖路径为：<project\_dir>/entry/libs/test.har， entry的oh-package.json5内容如下：

   ```
   1. {
   2. "name": "entry",
   3. "version": "1.0.0",
   4. "description": "Please describe the basic information.",
   5. "dependencies": {
   6. "test": "./Libs/test.har"
   7. }
   8. }
   ```
3. 执行ohpm install，ohpm可检测到test.har的实际路径（<project\_dir>/entry/libs/test.har）与配置路径（<project\_dir>/entry/Libs/test.har）大小写不一致(配置时libs目录名存在大写字母：'L'，与原始目录名不一致)，此时ohpm会报错提示并中断执行。
