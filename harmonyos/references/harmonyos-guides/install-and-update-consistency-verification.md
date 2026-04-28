---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/install-and-update-consistency-verification
title: 应用安装与更新一致性校验
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包基础知识 > 应用程序包安装卸载与更新 > 应用安装与更新一致性校验
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:951cd40f01238e5e1121d8806fcec880c0eedfe73171567512c48d34d7272f44
---

随着应用发展越来越复杂，应用也被拆成多个模块进行开发维护，不同的团队负责单个或者多个模块，应用在安装更新过程中会针对不同的字段进行一致性校验和验证，保证应用的安全合法性。本文介绍多模块安装或更新时，签名证书、配置文件的一致性校验规则。

说明

[app.json5配置文件](app-configuration-file.md)中versionCode字段一致，表示安装或更新包同版本，否则为不同版本。

使用打包工具进行打包时，会进行合法性校验。详情请参考[打包工具](packing-tool.md)。

## 签名证书一致性校验

| 字段名称 | 说明 | 安装一致性校验规则 | 更新一致性校验规则 |
| --- | --- | --- | --- |
| appId | 应用的appId，表示应用的唯一标识，详情信息可参考[什么是appId](common-problem-of-application.md#什么是appid)。 | 是 | appId和appIdentifier任一相同即可。 |
| appIdentifier | 应用的唯一标识。详情信息可参考[什么是appIdentifier](common-problem-of-application.md#什么是appidentifier)。 | 是 | appId和appIdentifier任一相同即可。 |
| appDistributionType | 应用[Profile文件](../app/agc-help-release-profile-0000002248341090.md)中的类型，标识应用的发布上架类型，如类型为[企业MDM应用发布](../app/agc-help-enterprise-mdm-profile-0000002248341094.md)。 | 是 | 更新不同版本时无校验，同版本有校验。 |
| appProvisionType | 应用签名证书类型。[Profile签名文件](../app/agc-help-profile-overview-0000002283260125.md)的类型，分为debug和release。debug为本地调试使用，release为上架应用市场使用。 | 是 | 更新不同版本时无校验，同版本有校验。 |
| apl | 表示应用程序的[APL等级](app-permission-mgmt-overview.md#权限机制中的基本概念)，系统定义的apl包括：normal、system\_basic和system\_core。 | 是 | 更新不同版本时无校验，同版本有校验。 |

## 配置文件一致性校验

| 字段名称 | 说明 | 安装一致性校验规则 | 更新一致性校验规则 |
| --- | --- | --- | --- |
| bundleName | 标识应用名称。该字段来源于[app.json5配置文件](app-configuration-file.md)中的bundleName字段。 | 是 | 是 |
| versionCode | 标识应用版本号。该字段来源于[app.json5配置文件](app-configuration-file.md)中的versionCode字段。 | 是 | 是 |
| apiReleaseType | 标识应用运行需要的API目标版本的类型。设备中未安装该应用，该应用包含多个模块包，模块一个一个安装时，不检验一致性。该字段来源于[app.json5配置文件](app-configuration-file.md)中的apiReleaseType字段。 | 否 | 是 |
| targetBundleName | 标识当前包所指定的目标应用，配置该字段的应用为具有overlay特征的应用。该字段来源[app.json5配置文件](app-configuration-file.md)中targetBundleName字段。 | 是 | 是 |
| targetPriority | 标识当前应用的优先级。该字段来源于[app.json5配置文件](app-configuration-file.md)中的targetPriority字段。 | 是 | 是 |
| bundleType | 标识应用的类型。该字段来源于[app.json5配置文件](app-configuration-file.md)中的bundleType字段。 | 是 | 是 |
| installationFree | 标识是否支持免安装。该字段来源于[module.json5配置文件](module-configuration-file.md)中的installationFree字段。 | 是 | 是 |
| debug | 标识应用是否可调试。该字段来源于[app.json5配置文件](app-configuration-file.md)中的debug字段。 | 是 | 否 |
| moduleType | 标识模块的类型。该字段来源于[module.json5配置文件](module-configuration-file.md)中的type字段。 | 是，同版本entry类型的moduleName不能修改 | 是 |
