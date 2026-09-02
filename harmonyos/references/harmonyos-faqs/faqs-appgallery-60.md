---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-60
title: 如何解决内部测试安装失败，报错误码17700018的问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何解决内部测试安装失败，报错误码17700018的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:99cb089a866ec6141fbdced12cb9ef0bcff2b69ae675d609c7d24d6a06a3d2d6
---

## 问题现象

在使用内部测试，进行安装时安装失败提示：17700018安装失败。根据文档了解到该错误码是由于安装HAP或者HSP时，依赖的模块不存在，但是无法确定是什么模块不存在，对于此类问题如何排查？

## 背景知识

* [内部测试](../app/agc-help-internal-test-0000002270709477.md)：将应用发布上传至开发中的服务器或者第三方云上，团队参与测试的人员可以将应用下载到授权的设备上测试。无需提交应用至华为应用市场，可以更灵活控制版本发布节奏。
* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* [集成态HSP](../harmonyos-guides/integrated-hsp.md)：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于宿主应用HAP的应用内HSP。

## 问题定位

定位步骤可以参考如下：

1. 当安装HAP或者HSP时，依赖的模块不存在。BundleInstaller.install就会抛出[17700018](https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700018-安装失败依赖的模块不存在)错误码。
2. 检查描述文件中HSP和HAP是齐全，所有依赖的module都需要配置到描述文件中。
3. 描述文件配置确认正常，检查应用是否使用了集成态HSP，[内部测试仅支持编译HAP和应用内HSP包](../app/agc-help-internal-test-build-app-0000002295372093.md)。

## 分析结论

* 17700018错误是由于安装HAP或者HSP时其依赖的模块不存在。需要在内部测试描述文件中补齐所有依赖的module.
* 应用开发过程中使用了集成态HSP，会导致对应的依赖无法安装报17700018的错误。

## 修改建议

1. 确认描述文件中应用依赖的所有module都已经按[配置规则](../app/agc-help-internal-test-release-app-0000002260691994.md)配置完成。
2. 如果应用使用了集成态HSP可以使用以下两种解决方案:
   * 将TGZ格式共享包转换为.HAR格式并打包到HAP中，具体转换方法可以[参考文档](../harmonyos-guides-V14/ide-tgz-har-migrating-V14.md)。
   * 将集成态HSP转换为应用内HSP，在应用中通过内部测试证书打包。

## 常见FAQ

Q：描述文件中包含了所有的HSP和HAP，且未使用集成态HSP，安装仍然报错17700018是什么原因？

A：应用安装对应module的HSP或HAP包时会按描述文件中的deviceTypes过滤，目前仅支持phone（手机）和tablet（平板）。如果deviceTypes缺少phone或者tablet，会导致对应module没有分发到设备，导致安装报错。因此需要检查描述文件中module对应的deviceTypes是否正确。
