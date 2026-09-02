---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-19
title: 项目多人开发时会导致signingConfigs冲突，该如何协调
breadcrumb: FAQ > DevEco Studio > 签名服务 > 项目多人开发时会导致signingConfigs冲突，该如何协调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:faa6f18675b005bbcb4fc3979cd9a2716a453143d5860bef10f2cf4e0b70b711
---

## 问题现象

多人开发时，build-profile.json5里的签名信息因使用绝对路径上传到git仓库后，其他人下载到本地后使用该签名配置信息无法正常签名，报错如下：

```txt
hvigor ERROR: Failed :entry:default@SignHap...
> hvigor ERROR: Unsupported state or unable to authenticate data
Detail: Signing failed. Reconfigure the signature or clear the E:\work\1200_iabp_harmonyos folder and perform signing again.
at E:\work\1200_iabp_harmonyos\build-profile.json5
> hvigor ERROR: BUILD FAILED in 8 s 43 ms
```

## 背景知识

* git多人协作的核心需求。
  + 分布式架构：git的分布式特性允许每个开发者拥有完整的代码仓库副本，支持离线操作和本地版本控制，降低对中心服务器的依赖。
  + 并行开发：通过分支机制实现功能隔离，开发者可在独立分支上工作，避免直接修改主分支代码。
  + 代码整合：通过合并（Merge）或变基（Rebase）操作将多分支代码整合到主分支，确保代码最终一致性。
* 签名配置个性化导致的文件冲突。
  + [手动签名](../harmonyos-guides/ide-signing.md#section297715173233)场景下，每个开发者的本地签名参数（如storePassword、keyAlias、certpath等）因设备差异而不同，直接修改[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)会导致该文件频繁被改动。
  + 即便开发者设置相同密码，不同设备生成的加密值仍会不同，进一步加剧文件内容不一致问题。

## 问题定位

多人开发时，将配置好的发布证书签名所在的build-profile.json5文件使用git进行提交，会导致signingConfigs冲突的问题现象发生。

## 分析结论

1. 根据背景知识，手动签名场景下，每个开发者的本地签名参数因设备差异而不同。
2. 当多人开发时未将build-profile.json5文件中的签名配置信息外置化，配置发布证书签名导致不同设备的storePassword和keyPassword不一样，使得build-profile.json5在不同设备中显示的内容也不同，所以多人开发手动签名后使用git提交build-profile.json5文件就会导致该文件冲突。

## 修改建议

* **方式一：signingConfigs中使用相对路径。**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/myx9dLZFQwWmLZKCgPN81w/zh-cn_image_0000002677866951.png "点击放大")

  签名使用相对路径可以做到多人共用签名、git不冲突、可以将团队内设备的udid都添加到该签名中就可以直接安装。但是可能存在的问题：

  1. 签名上传可能有安全性问题。
  2. 当新增权限（需要ACL提权的）、新增设备的udid都需要管理该签名的人重签名一份上传，其他人有需要时再重新拉取代码。
* **方式二：使用自定义构建任务动态修改signingConfigs。**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/BX9UOrydTkKPU5gTSoXJbQ/zh-cn_image_0000002678026805.png "点击放大")

  这种方式可以将签名配置信息独立出来，git不冲突，每人也可使用自己的签名，流水线构建时使用专属签名即可。

  参考示例1：[动态修改签名和编译配置](../harmonyos-guides/ide-hvigor-config-ohos-sample.md#section973053620286)。

  参考示例2：

  1. 签名信息外置化。

     创建独立配置文件，将material这部分签名配置从build-profile.json5中剥离。

     新建external-signing-config.json（文件名可自定义），内容示例：[signingConfigs字段示例](../harmonyos-guides/ide-hvigor-build-profile-app.md#section153288223224)。

     将此文件添加到.gitignore，避免敏感信息提交至版本库。
  2. 动态加载签名配置。

     修改hvigorfile.ts，通过自定义构建任务动态读取外部配置文件，在工程级hvigorfile.ts里引入外部json配置（如：external-signing-config.json）。可参考[在hvigorfile.ts中通过overrides关键字导出动态配置](../harmonyos-guides/ide-hvigor-config-ohos-guide.md#section19588121902)。

     删除build-profile.json5中的signingConfigs字段，避免本地配置覆盖动态逻辑。
  3. 团队协同规范。

     统一加密材料，团队内部共享同一份证书文件（.p12/.cer等），但各自通过DevEco Studio生成本地加密密码，避免跨设备加密结果差异。
* **方式三：使用自定义构建任务调用签名工具进行命令行签名**。

  准备好HAP签名工具hap\_sign\_tool.jar，使用命令行对HAP进行签名。（证书文件需自行准备好，参考方式二第3步）参考链接：[对未签名的HAP/APP进行签名](../harmonyos-guides/ide-command-line-building-app.md#section103321051433)。

## 常见FAQ

Q：如果忽略build-profile.json5文件，IDE又没有自动初始化build-profile.json5，会直接找不到ProjectStructure的选项。如果追踪build-profile.json5，那不同人在signingConfigs生成密钥时又会有改动。该如何处理？

A：可以尝试将文件提交，文件里的signingConfigs内容不提交，只提交空数组。

Q：如果多人开发，签名信息代码提交上去，会导致其他设备无法正常使用，要怎么做到通用？

A：关于应用/服务的签名，分为自动签名和手动签名两种。可以尝试使用手动签名，并且在申请证书时选择添加多个设备，便可以多人使用同一套签名，可以在多个设备上调试。

具体步骤为手动签名->申请证书->获取密钥->共同打包上传，之后就可以避免多人协作时自动签名冲突的问题。

详情可以参考如下内容：[配置调试签名](../harmonyos-guides/ide-signing.md)。

Q：多人开发时，项目拷贝传递后由于手动签名用的绝对路径会导致签名失败，signingConfigs的这些文件路径能不能配置相对路径？

A：signingConfigs使用手动签名的签名文件可以设置相对路径。在工程目录下创建签名文件的文件夹，并将material内的所有签名文件存放于该文件夹下（包含.csr文件），并在工程根目录的build-profile.json5内配置对应的相对路径来引用即可。

例如："storeFile": "./sign/test.p12"。
