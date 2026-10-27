---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0005
title: 应用打包与安装操作常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 应用打包与安装操作常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b6c1d91d424b0ba36a04d4c58b6f0ed9065c4402b1446499bd7643a40e042645
---

**Q：启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，应该如何检查应用的可见性设置？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/PvPQQbFkRYydW4-oE86xCA/zh-cn_image_0000002770980364.png)

**A**：解决措施如下：

* 在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
* FA模型工程：在config.json文件的abilities字段中，将visible设置为true。

**Q：如何安装打包出来的App包（通过什么命令安装）？**

**A**：App资源包是无法直接安装的，需要通过应用市场下载才能安装，最后通过解析App包安装的还是HAP包。

**Q：如何将多工程的HAP打包成一个App？**

**A**：将多工程的HAP打包成一个App的步骤如下：

1. 分别对不同工程的模块进行打包，执行DevEco Studio中的Build Hap指令。在outputs文件夹下获取未签名的hap包和pack.info文件。
2. 合并所有模块的pack.info文件，生成app级别的pack.info文件，格式如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/TI3bVOSxRy-7m1BjpPJ4-w/zh-cn_image_0000002771140334.png "点击放大")

   summary.app为整个包的配置信息，保证唯一。summary.modules和packages取模块级别pack.info文件中相对应的第1个值填入。
3. 在SDK toolchains工具的lib文件夹下执行以下命令打包未签名的app包：java -jar app\_packing\_tool.jar --mode app --force true --pack-info-path [pack.info 文件路径] --hap-path [hap 包路径，使用逗号隔开] --out-path [输出 app 包路径，以 .app 结尾]。
4. 签名app包在SDK toolchains工具lib文件下执行指令java -jar hap-sign-tool.jar sign-app -mode localSign -keystoreFile [P12签名文件] -keystorePwd [keystorePwd] -keyAlias [keyAlias] -keyPwd [keyPwd] -signAlg [signAlg] -profileFile [P7b签名文件] -appCertFile [CER签名文件] -inFile [未签名App包路径] -outFile [签名App包路径]。

**Q：应用安装后，HAP文件在哪个目录路径？**

**A**：目录路径："/data/app/el1/bundle/public/<bundleName>"。

参考链接：[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。
