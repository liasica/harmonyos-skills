---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish
title: 发布共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:19+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:d4a1cc132ed78c386ef00604bccddf0c393a781e829288f7dc55057e66964597
---

## 发布HAR共享包

发布打包的HAR，可供其他开发者安装和引用。接下来将介绍如何发布HAR共享包。

**说明** 

OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考[ohpm私仓搭建工具](ide-ohpm-repo-overview.md)。

1. 在HAR模块中（与src文件夹同一级目录下），添加如下文件：
   * 新建README.md文件：在README.md文件中必须包含包的介绍和引用方式，还可以根据包的内容添加更详细介绍。
   * 新建CHANGELOG.md文件：填写HAR的版本更新记录。
   * 添加LICENSE文件：LICENSE许可文件。
2. 重新[编译HAR模块](ide-har.md#section7892044183814)，生成\*.har文件。

   **说明** 

   若修改了HAR包模块级oh-package.json5文件中version字段信息，请先执行Build > Clean Project指令，再重新进行Build全量构建。
3. 利用工具ssh-keygen生成公、私钥，可执行以下命令：

   ```screen
   ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh_ohpm/mykey
   ```

   **说明** 

   1. ~/.ssh\_ohpm/mykey 为私钥文件 mykey 的文件路径，按照实际情况指定。指定的私钥存储目录必须存在。
   2. 追加了.pub后缀的相应公钥文件会存放在和私钥相同的目录下。
   3. ohpm包管理器只支持加密密钥认证，请在生成公私钥时输入密码。
4. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)官网，单击主页右上角的**个人中心**，新增OHPM公钥，将公钥文件（mykey.pub）的内容粘贴到公钥输入框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/b_chdz1xSkWEpZOnoc9Y2w/zh-cn_image_0000002779406494.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=D87A78D3D80206451692935AC01D3A250C65474FCCC163AF220C336FBA9EA1D6)
5. 打开命令行工具，将对应私钥文件路径配置到 .ohpmrc 文件中 key\_path 字段上，可执行以下命令进行配置：

   ```screen
   ohpm config set key_path  ~/.ssh_ohpm/mykey
   ```
6. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn)官网，单击主页右上角的**个人中心**，复制发布码，获取发布码并配置到 .ohpmrc 文件中，可执行如下命令：

   ```screen
   ohpm config set publish_id your_publish_id
   ```
7. 执行如下命令发布HAR，<HAR路径>需指定为.har文件的具体路径。

   ```screen
   ohpm publish <HAR路径>
   ```

## 发布HSP共享包

如需在应用内共享HSP，需编译生成\*.tgz包后，将HSP共享包上传至私仓。

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/6Gx6TU9lT_u_QD2-QjM8EA/zh-cn_image_0000002808766049.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=51DBAEE8C9161F37AD584B82492D8CF5A36EF532E4F9BDA7EBC7BFE1340B48BD)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/yn3U_IkERRe8iHbSkrUldg/zh-cn_image_0000002779566470.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=C705C0B4B94DBF216EC9590F5FE2B37AEA6AF4D95E212D70D9F9DE88418EF362)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/KEhErh4GTGyThLUZL2vZtg/zh-cn_image_0000002779566464.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C374166E5D8C567B157A35C38F700BD18F2FFC6BB618BECBBE1DF5519DA5D53)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/sv8fWTFURsS5d-NbZWUUGw/zh-cn_image_0000002808886129.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=D93B38ECEA466B17E1BDFC5AB14647395F0D06393222EBB94DA74B3797DD56FB)
3. 将HSP共享包上传至私仓，具体参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#section1710514092415)。
