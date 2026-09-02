---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-8
title: 如何安装指定路径下的应用包
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 如何安装指定路径下的应用包
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:a96756e09a7fa8ef175f45910590ce440521ef73cb117993613806438ad7007b
---

## 问题现象

调用接口[bundleManager.install](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstall)安装应用更新包时，报以下错误：

Failed to install bundles. Code is 9201002, message is Failed to install the application. [MSG\_ERR\_INSTALL\_PERMISSION\_DENIED]。

调用接口[bundleManager.installMarketApps](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstallmarketapps22)安装企业市场应用时，也可能返回9201002错误码，错误信息为Failed to install the application. $。

## 背景知识

[bundleManager.install](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstall)用于静默安装指定路径下的应用包，此接口只能安装分发类型为enterprise\_mdm（MDM应用）和enterprise\_normal（企业普通应用）类型的应用。

[bundleManager.installMarketApps](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstallmarketapps22)用于安装企业市场应用，调用此接口前需要完成HEM商用部署，否则会返回9201002错误码。

## 解决方案

1. 检查调用方（调用bundleManager.install接口的APP）是否属于设备管理应用，且已激活状态。
   * 创建一个设备管理应用需要完成以下步骤：
     1. 申请资质。
     2. 创建EnterpriseAdminExtensionAbility。
     3. 声明接口所需权限。更详细的步骤参考：[MDM应用开发指南](../harmonyos-guides/mdm-kit-guide.md)。
   * 激活设备管理应用。

     调试阶段使用hdc shell edm enable-admin命令激活。正式发布时通过HEM平台激活。
2. 检查被调用方（待安装APP）分发类型是否为enterprise\_mdm（MDM应用）和enterprise\_normal（企业普通应用）。
   * 待安装的应用需集成企业MDM应用发布证书。[申请企业MDM应用发布Profile](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)。
   * 查询待安装APP是否属于enterprise\_mdm（MDM应用）和enterprise\_normal（企业普通应用）。

     通过getBundleInfoForSelf接口查询应用自身的BundleInfo，其中BundleInfo.appInfo.appDistributionType为应用的分发类型，检查是否为enterprise\_mdm（MDM应用）和enterprise\_normal（企业普通应用）类型的应用。
3. 检查待安装APP路径是否正确。

   用hdc命令把安装包push到物理路径上，通过[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)，找到对应的沙箱路径，把沙箱路径作为hapFilePaths参数传入。

   一般情况下，安装包在沙箱中的路径形如"/data/storage/el2/base/cache/files/xxxx.hap"。
4. 若调用[bundleManager.installMarketApps](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstallmarketapps22)接口返回9201002错误码，需确认是否已完成企业MDM应用商用申请。
   * bundleManager.installMarketApps接口需要走[企业MDM应用商用申请](https://developer.huawei.com/business/cn/doc/HEM/developer-commercial-license-0000002469392504)流程才会生效，仅走企业MDM应用测试不会生效。
   * 完成商用申请后，重新调用接口验证安装是否成功。

## 常见FAQ

Q：MDM应用可以通过bundleManager.install接口自升级吗？

A：可以，将InstallParam的参数installFlag值设置为1即可。

Q：MDM应用升级是整包升级还是部分升级？

A：MDM应用升级为整包升级，通过bundleManager.install接口传入完整的hap包路径进行安装或覆盖安装，不支持部分升级。

Q：MDM应用可以静默升级吗？

A：可以，通过bundleManager.install接口可以静默安装指定路径下的应用包，实现MDM应用的静默升级。

Q：bundleManager.install接口是否支持安装包含HSP的多模块应用？

A：支持。安装包含HSP的多模块应用时，所有模块都需要经过签名，且必须使用发布证书。

Q：单模块应用改为多模块应用后，通过bundleManager.install接口覆盖安装是否存在问题？

A：支持覆盖安装。如遇兼容性问题可反馈处理。

Q：终端安装企业重签名证书后，调用bundleManager.install安装未经过企业重签名的应用，报什么错误码？

A：错误码为9201002，错误信息为Failed to install the application[MSG\_ERR\_INSTALL\_PERMISSION\_DENIED]。

Q：调用bundleManager.installMarketApps接口返回9201002错误码如何处理？

A：需确认是否已完成企业MDM应用商用申请。bundleManager.installMarketApps接口需要走[企业MDM应用商用申请](https://developer.huawei.com/business/cn/doc/HEM/developer-commercial-license-0000002469392504)流程才会生效，仅走企业MDM应用测试不会生效。

Q：在双空间安装hap的限制规格是什么？

A：企业Release应用：

如在个人空间安装，安装/更新到个人空间，安装/更新成功；安装/更新到企业空间，安装/更新失败。

如在企业空间安装，安装/更新到个人空间，安装/更新失败；安装/更新到企业空间，安装/更新成功。

Q：双空间设备上，企业空间已安装某应用后，在个人空间通过[bundleManager.install](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstall)接口安装同一应用时，[InstallParam](../harmonyos-references/js-apis-enterprise-bundlemanager.md#installparam)的installFlag设置为0无法安装，设置为1可以安装，是否为正常现象？

A：属于正常现象。安装信息全局共享，不区分空间。同一个包安装过一次后即存在安装记录，因此在个人空间使用installFlag为0（应用初次安装）时会因已存在安装记录而安装失败，使用installFlag为1（应用覆盖安装）时可以正常安装。

Q：bundleManager.installMarketApps接口是否支持跳转至应用市场下载任意应用？

A：bundleManager.installMarketApps接口为静默下载安装，无需跳转到应用市场。接口传入的包名必须是应用市场已上架的应用包名，并且需要[在HEM平台上加入企业应用](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_equipment_app-management-0000002468952084)，该接口需依赖外部网络。

Q：“在HEM平台上加入企业应用”是指自建应用市场还是需要跳转至应用市场下载的应用？

A：“在HEM平台上加入企业应用”是指在HEM管理台的企业应用管理界面中添加需要在设备上安装的应用，并非指自建应用市场。添加后的应用可在策略管理中选中，通过bundleManager.installMarketApps接口静默下载安装。
