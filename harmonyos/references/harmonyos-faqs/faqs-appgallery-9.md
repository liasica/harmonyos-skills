---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-9
title: HarmonyOS指定设备发布描述文件签名sign字段如何生成
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS指定设备发布描述文件签名sign字段如何生成
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:affba22e9309e01eb7884d00faf4f73b5e680596000f2b25f062b14d47108996
---

## 问题现象

使用[指定设备发布](../app/agc-help-internal-test-0000002270709477.md)发布应用，在使用[构建Deeplink实现下载应用](../app/agc-help-internal-test-release-app-0000002260691994.md)生成应用描述文件（例如：manifest.json5，文件名可自定义）时，需要获取描述文件签名（即sign字段），应该如何获取sign的值呢？

## 背景知识

* 需要根据提供的[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)来生成sign字段。
* 生成签名所需要manifest-sign-tool-1.0.0.jar也需要通过[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)获取。

## 解决方案

1. 描述文件不是由项目生成，但可以通过应用的module.json5和app.json5文件生成，具体字段可以参考[构建Deeplink实现下载应用](../app/agc-help-internal-test-release-app-0000002260691994.md)说明，并根据实际情况手动填写对应的参数，保存到本地即可。
2. 描述文件生成后保存本地，参照如下命令生成描述文件签名sign：

   ```screen
   java -jar manifest-sign-tool-1.0.0.jar -operation sign -mode localjks -inputFile D:\old_manifest.json5 -outputFile D:\new_manifest.json5 -keystore D:\internaltest.p12 -keystorepasswd Abc123456 -keyaliaspasswd Abc123456 -privatekey internaltest
   ```

   其中：
   1. operation为操作类型，生成签名时为sign，验证签名时为verify；
   2. mode为获取签名的模式，本地为localjks，远端为remote，参考示例选择localjks；
   3. inputFile为需要生成签名描述文件路径，参考示例为D:\old\_manifest.json5；
   4. outputFile为输出的带sign的描述文件路径，参考示例为D:\new\_manifest.json5；
   5. keystore为p12密钥文件路径，对应[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)中的keystore Name(\*.p12)，参考示例为D:\internaltest.p12；
   6. keystorepasswd为密钥文件密码，对应[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)的Key store Password，参考示例为Abc123456；
   7. keyaliaspasswd为私钥的密码，对应[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)的Key password，参考示例为Abc123456；
   8. privatekey为私钥的别名，对应[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)的Alias，参考示例为internaltest；

**说明：**

执行operation指令时，其中old\_manifest.json5的sign字段无需填写，生成的new\_manifest.json5会自动补充，以下为执行前后示例：

old\_manifest.json5：

"sign": "描述文件签名"

new\_manifest.json5：

"sign": "MEUCIEl\*\*\*\*4AVZyWFc="

**须知** 

低版本的JDK会限制加密强度并产生报错，需要升级JDK到1.8.0.3\*或更高版本（不包括java11的版本）。

## 常见FAQ

Q：指定设备发布时提示错误码10019：描述文件验签失败，如何处理？

A：检查描述文件的签名密钥与安装包的签名密钥，确保二者保持一致。使用签名工具进行本地验证，获取签名后的描述文件（如manifest.json5），执行如下命令进行验签：

```screen
java -jar manifest-sign-tool-1.0.0.jar -operation verify -inputFile C:\xxx\manifest.json5 -keystore C:\xxx\internaltest.p12 -keystorepasswd internaltest
```

其中operation为操作类型，验证签名时为verify；inputFile为需要验签的manifest.json5文件路径；keystore为p12密钥文件路径；keystorepasswd为密钥文件密码。manifest-sign-tool-1.0.0.jar可通过[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)获取。特别注意安装包有多产物和多签名密钥的情况，需确保描述文件签名时使用的签名密钥p12和安装包使用的签名密钥一致。更多内容可参考[文档](faqs-appgallery-93.md)。
