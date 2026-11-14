---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish
title: 发布共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:46+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:6f4fc443436ede4dbd694c4311e7e3e4eb7e9e740017782b6ce48101eff8551a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/thrhb0w1TEGaI9qC47KdlQ/zh-cn_image_0000002779406494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=76A4F364527548D0090E4673C7FD77B2BB471C17DD55781A52E2C0731258A48E)
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

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/KZdF58bDTLaWN-rRXUcocQ/zh-cn_image_0000002808766049.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=66944065810FC53651553C6AC80697C49A4590120D5A3D5A1A9F5A72A4B821D1)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/xVn0S8S4QZauQcZ4WUOFPA/zh-cn_image_0000002779566470.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=612083E21FAA3D996CE3AAA3279C9EBD70D952853D9D9AC31AC4DF34AB3FF258)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Ric23lEpSUuDMseXyCmiXg/zh-cn_image_0000002779566464.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=79B2C0F90F776E29CC9D6B4FD0776F09F33A9040C083F2B3BCC37C3D2A3D6658)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/H-30QWSTRPOM4tLl3HiyFA/zh-cn_image_0000002808886129.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=C10A22E705BDAEDE0D5460FD076961CE0BA325CAF64BCB1945D3D69F8734B28B)
3. 将HSP共享包上传至私仓，具体参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#section1710514092415)。
