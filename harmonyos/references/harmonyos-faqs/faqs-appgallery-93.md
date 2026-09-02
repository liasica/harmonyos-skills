---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-93
title: HarmonyOS指定设备发布常见错误码深度解析
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS指定设备发布常见错误码深度解析
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:37d13614a22969ecba830ca615d6f1fd580a90e93a551a9fd7ecbfbb7891c02e
---

## 问题现象

[指定设备发布](../app/agc-help-internal-test-0000002270709477.md)是一种由开发者自行控制测试设备和版本的内部测试方式，实际在用户下载安装应用过程中可能会出现一些问题，本文针对常见的[错误码](../app/agc-help-internal-test-errorcode-0000002295325157.md)做深度解析，帮助开发者更好地分析解决问题。

## 背景知识

使用指定设备发布可以将应用发布上传至开发者自己的服务器或者第三方云上，团队参与测试的人员可以将应用下载到授权的设备上测试。更灵活发布版本和限定测试范围，及时修复问题并优化版本体验。

相较于邀请测试，指定设备发布不需要上架应用市场；相较于In-house发布，指定设备不需要申请特殊账号。更多功能和描述可参考[业务介绍](../app/agc-help-internal-test-overview-0000002253054942.md)。

## 解决方案

1. **错误码10019：描述文件验签失败；**

   解决方案：请检查描述文件的签名密钥与安装包的签名密钥，确保二者保持一致。请使用签名工具进行本地验证。操作如下：

   * 获取签名后的描述文件（如manifest.json5），根据[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)说明，执行如下命令：

     java -jar manifest-sign-tool-1.0.0.jar -operation verify -inputFile C:\xxx\manifest.json5 -keystore C:\xxx\internaltest.p12 -keystorepasswd internaltest

     其中：
   1. operation为操作类型，验证签名时为verify；
   2. inputFile为需要生成签名的manifest.json5文件路径；
   3. keystore为p12密钥文件路径，对应Store file(\*.p12)；
   4. keystorepasswd为密钥文件密码，对应Store password；
   5. manifest-sign-tool-1.0.0.jar可通过[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)获取。
   * 确保描述文件签名时使用的签名密钥p12和安装包使用的签名密钥是一致的。特别注意安装包有多产物和多签名密钥的情况。
2. **错误码10021：安装包证书校验失败；**

   解决方案：请检查是否使用了正确的[发布证书](../app/agc-help-release-cert-0000002283336729.md)和[指定设备发布Profile](../app/agc-help-internaltest-profile-0000002283260129.md)打包安装包。请确保设备UDID在指定设备发布Profile指定的设备列表内。操作如下：

   * 获取到hap安装包，使用文本编辑器直接以文本方式打开。
   * 搜索关键词"app-distribution-type"，指定设备发布对应的分发类型为internaltesting，若是其他值，说明使用的Profile类型错误，需要重新[申请指定设备发布Profile](../app/agc-help-internaltest-profile-0000002283260129.md)。
   * 搜索关键词"device-ids"，检查对应的UDID值是否包含设备的UDID，只有在device-ids中的设备才允许安装应用，参考[UDID获取方法](../app/agc-help-add-device-0000002283189937.md#section67331926102911)。
   * 搜索关键词"type""，指定设备分发的类型为release，若是其他值（如debug），需要重新打包。

     示例如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/OuEHxJJfQ0SY_j8YWFF81g/zh-cn_image_0000002640108094.png "点击放大")
3. **错误码10000：DeepLink格式错误；**

   解决方案：

   * DeepLink正确格式为：store://enterprise/manifest?url= encodeURIComponent（描述文件下载URL）。
   * 描述文件下载URL使用HTTPS协议。
   * 描述文件下载URL以“.json5”结尾。
   * 描述文件下载URL的域名与描述文件内deployDomain字段值一致。
   * 描述文件中deployDomain不要带协议头和端口号，正常格式为：[xx.huawei.com](http://xx.huawei.com/)。不要写成https://xx.huawei.com:80；
4. **错误码10026：身份校验不通过；**

   解决方案：请确认设备的身份验证功能（设备华为账号、生物识别和密码）是否正常，以及使用者本人的合法性，确认无误后再重试。

   常见原因还有手机网络连接了代理导致，可以断开代理重试。

## 常见FAQ

Q：点击应用提示“应用已过期”，如何解决？

A：指定设备发布应用版本存在有效期，当前为90天。使用超过有效期后，该应用版本将无法启动。请更新应用版本号（versionCode）后重新编译打包并部署，即可正常下载安装新版本应用。

Q：同一个安装包在不同设备上，有的设备提示过期，有的设备正常运行是什么情况？

A：应用版本有效期是以设备首次安装的时间为起点计算（非版本编译时间），从安装日向后推90个自然日。由于不同设备安装时间不同，同一版本可能出现部分设备提示过期、部分设备未过期的情况。部分非商用机和商用机存在差异也可能出现该问题，需要通过更新版本号（versionCode）解决。

Q：使用指定设备方式做内部测试下载后无法安装应用怎么办？

A：请自行排查是否使用构建Deeplink实现下载应用方式安装应用，具体请参考[指定设备发布应用](../app/agc-help-internal-test-release-app-0000002260691994.md)。
