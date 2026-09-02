---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-97
title: HarmonyOS应用上架包签名信息获取
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS应用上架包签名信息获取
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:abff9e3e52fc820684ee47dfe85c45c2ed68b9c1cf4a8ff214f025db240c5606
---

## 问题现象

HarmonyOS应用打包使用的证书有调试证书和发布证书区分，上架应用市场的应用必须用发布证书打包，而发布证书打包的应用无法安装，因此怎么获取发布上架包的签名信息呢？

## 背景知识

HarmonyOS应用经常需要集成一些开放能力，不管是华为开放能力还是三方能力，都需要做鉴权，鉴权的方式根据不同产品提供，一般是通过软件包的签名信息做鉴权，签名信息依赖于证书，而HarmonyOS应用打包有调试证书和发布证书区分，上架应用市场的应用必须用发布证书打包，为了保证应用上架后用户的体验，因此必须配置在架应用的签名信息。签名信息一般可通过公钥指纹和appId来承载。应用相关如：

1. 华为开放能力使用[公钥指纹](../harmonyos-guides/application-dev-overview.md#条件必选添加公钥指纹)鉴权，涉及的场景服务有华为账号，应用内支付，钱包服务等。具体的操作步骤可以参见[配置公钥指纹。](../app/agc-help-cert-fingerprint-0000002278002933.md)
2. 部分三方服务使用appId鉴权，具体的获取方式参考[bundleInfo.signatureInfo.appId。](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#signatureinfo)正确的appId形式为："包名\_签名信息"。

## 解决方案

不管是本地调试包还是上架包，签名信息都依赖于密钥库文件(p12文件)，只要保证上架的app包使用的和本地调试的hap一样的p12文件，则相关的公钥指纹或者appId都不会发生变化。

1. 本地调试包获取appId的方式有两种：
   * 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含[signatureInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#signatureinfo)签名信息，签名信息中包含appId信息。
   * 安装应用后通过[bm](../harmonyos-guides/bm-tool.md)工具获取。参考命令：hdc shel bm dump -n {bundlename} | grep appId

2. 上架包获取appId的方式也有两种。
   * 如前面简述，如果上架包使用的和本地调试包一样的p12文件，则可以参考本地调试包的方式获取appId。
   * 发布邀请测试，从应用市场安装应用，然后通过[bm](../harmonyos-guides/bm-tool.md)工具获取，该方式也可以进一步验证同一p12编译的软件包appId是一致的。

## 常见FAQ

Q：公钥指纹和appId是什么关系，怎么获取公钥指纹？

A：不管公钥指纹还是appId，都是签名信息的表现形式，公钥指纹在AGC上生成证书后可以直接获取，参见[配置公钥指纹。](../app/agc-help-cert-fingerprint-0000002278002933.md)

Q：公钥指纹和appId可以相互转换吗？

A：通过公钥指纹暂时无法计算对应的appId，但获取appId后可以通过hash算法计算公钥指纹，具体操作有：

1. 获取appId，如：com.example.demo\_BWashfosahfsoafjsoafhj\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ASDASAFdsafdDFAawWS=;
2. 去除包名信息，获取签名信息保存为txt文件，如sign.txt。
3. Windows系统下可通过**certutil -hashfile sign.txt SHA256**命令获取，Mac系统下可通过**shasum -a 256 sign.txt**命令获取。

Q：指纹配置成功后大约25小时生效，能否加速生效？

A：配置公钥指纹10分钟后，您可通过修改应用工程中app.json5中的versionCode触发公钥指纹生效。

## 总结

1. 不管是本地调试包还是上架包，签名信息都依赖于密钥库文件(p12文件)，只要保证上架的app包使用的和本地调试的hap一样的p12文件，则相关的公钥指纹或者appId都不会发生变化。
2. 签名信息是唯一的，通过签名信息能很好的完成业务的鉴权，一般表现形式是公钥指纹或appId。部分业务通过[fingerprint](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#signatureinfo)鉴权，但是使用的签名证书发生变化时，fingerprint也会发生变化。因此涉及到该业务要及时关注fingerprint的值是否正确。
