---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish
title: 发布共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:26+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:23b650df036d999666060c78d5a9abe35f85fa44542f43ad45cacde38f3c76f1
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/3dAGtvaVRvGeP7ZKP9QeWw/zh-cn_image_0000002779406494.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=42DEBADCF7EE71FC594313382221A8F162F5F9BE77C0CEA58D48DB5CF669809E)
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

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/vgM7ezU1Tmed4DuQvsZflA/zh-cn_image_0000002808766049.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=87B6C2001C686BB4849AB0E719CEE262B3D26B822283954DEA3CB2387E9A9346)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/mA0ADWncRcK5AY17gRHSJQ/zh-cn_image_0000002779566470.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5D417419CC710BB4E241CE0D72EE2E3C73810EDF787F3F84E43D19A7CD2DE9C)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/l_Ei0Y6fRyiCbW461OUdPw/zh-cn_image_0000002779566464.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FE5C2ED332E26B9D1DE0BDBDE10E544AB8BD81620E9F05EBCEC161D35EDA513)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/wacIk4KLQn-Bl9BlvJX4qQ/zh-cn_image_0000002808886129.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=03C44846D9D79F84AC9B84C52DAE592411DF0230FEF57CE0E8651055315F33FA)
3. 将HSP共享包上传至私仓，具体参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#section1710514092415)。
