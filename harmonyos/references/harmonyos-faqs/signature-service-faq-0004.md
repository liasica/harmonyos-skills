---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-faq-0004
title: 应用签名配置与证书使用常见问题
breadcrumb: FAQ > DevEco Studio > 签名服务 > 常见问题 > 应用签名配置与证书使用常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5be15ef00b637a8f4abc0af1a013884a641225278dc36af7c354fa075e88b125
---

**Q：如何通过DevEco Studio对HAP/APP包进行签名？**

**A**：通过DevEco Studio自带的签名工具，可以对已打包的HAP/APP包进行签名，具体步骤如下。

**说明** 

建议使用DevEco Studio 6.0.2 Beta1及以上的版本。

1. 通过DevEco Studio生成密钥和证书请求文件，并向HarmonyOS 开发者中心申请发布证书和Profile文件，具体请参考[准备签名文件](../harmonyos-guides/ide-publish-app.md#section793484619307)。
2. 准备好签名工具hap-sign-tool.jar，在${DevEco Studio安装目录}/sdk/default/openharmony/toolchains/lib下。
3. 在签名工具目录下，使用如下命令进行签名。详细的签名工具指导请参考[应用包签名工具](https://gitcode.com/openharmony/developtools_hapsigner)。

   ```shell
   java -jar hap-sign-tool.jar sign-app -keyAlias "demo_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "D:\demo.cer" -profileFile "D:\demo.p7b" -inFile "D:\hap-unsigned.hap" -keystoreFile "D:\demo.p12" -outFile "D:\hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
   ```

关于该命令中需要修改的参数说明如下，其余参数不需要修改：

* keyAlias：密钥别名。
* appCertFile：申请的发布证书文件，格式为.cer。
* profileFile：申请的发布Profile文件，格式为.p7b。
* inFile：通过Hvigor打包生成的未携带签名信息的HAP。
* keystoreFile：密钥库文件，格式为.p12。
* outFile：经过签名后生成的携带签名信息的HAP。
* keyPwd：密钥密码。
* keystorePwd：密钥库密码。

**说明** 

如果要对APP进行签名，只需将inFile和outFile参数修改为APP包即可。

**Q：HAP包中的“--BEGIN CERTIFICATE--”是什么格式的数据？**

**A**：证书签名时，支持DER和PEM的格式，“--BEGIN CERTIFICATE--”是DER格式的数据，可以直接使用。

**Q：如何获取应用包的签名指纹信息，即“.p12文件”信息？**

**A**：建议通过DevEco Studio自动化签名后，从.p12文件右侧的指纹按钮复制获取指纹信息。
