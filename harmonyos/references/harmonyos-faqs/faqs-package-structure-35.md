---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-35
title: 如何将多工程的HAP打包成一个App
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何将多工程的HAP打包成一个App
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bb8f1d0faaa991d46cafdbf64c1b2e5b45bec7e06b776f627b80e6329785c5d6
---

1. 分别对不同工程的模块进行打包，执行DevEco Studio中的Build Hap指令。在outputs文件夹下获取未签名的hap包和pack.info文件。
2. 合并所有模块的pack.info文件，生成app级别的pack.info文件，格式如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/j1m8o_FDRKSKflFXwvzc2A/zh-cn_image_0000002654795233.png)

   summary.app为整个包的配置信息，保证唯一。summary.modules和packages取模块级别pack.info文件中相对应的第1个值填入。
3. 在SDK toolchains工具的lib文件夹下执行以下命令打包未签名的app包：`java -jar app\_packing\_tool.jar --mode app --force true --pack-info-path [pack.info 文件路径] --hap-path [hap 包路径，使用逗号隔开] --out-path [输出 app 包路径，以 .app 结尾]。
4. 签名app包在SDK toolchains工具lib文件下执行指令java -jar hap-sign-tool.jar sign-app -mode localSign -keystoreFile [P12签名文件] -keystorePwd [keystorePwd] -keyAlias [keyAlias] -keyPwd [keyPwd] -signAlg [signAlg] -profileFile [P7b签名文件] -appCertFile [CER签名文件] -inFile [未签名App包路径] -outFile [签名App包路径]。
