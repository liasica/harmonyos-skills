---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-releasenote
title: 版本说明
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 版本说明
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6d1676dfeab019549094cf8334cca63eec6bf9c0fb0c4902878f59050eef1ed
---

## ohpm-repo 6.0.1

### 新增特性

* 支持编辑个人的邮箱和手机号。具体请参考[个人中心主页](ide-ohpm-web-user-center.md)。
* 支持编辑用户的邮箱和手机号。具体请参考[用户管理](ide-ohpm-user-management.md)。
* 支持批量上传三方包。具体请参考[仓库管理](ide-ohpm-depot-management.md)和[配置文件](ide-ohpm-repo-configuration.md)
* 支持配置自定义登录验证插件。具体请参考[自定义登录验证插件](ide-custom-sign-plugin.md)和[配置文件](ide-ohpm-repo-configuration.md)。
* 私仓访问外部公仓时，支持进行https认证证书校验。具体请参考[配置文件](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)、[ohpm-repo export\_pkginfo](ide-ohpm-repo-export-pkginfo.md)、[ohpm-repo batch\_download](ide-ohpm-repo-batch-download.md)和[uplinks](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_uplinks)。

## ohpm-repo 6.0.0

### 新增特性

在编辑仓库时，支持分别设置标准版本发布策略和先行版本发布策略。具体请参考[仓库管理](ide-ohpm-depot-management.md)。

## ohpm-repo 5.5.1

### 新增特性

支持返回固定版本的元数据。具体请参考[ohpm仓库接口协议](ide-interface-protocol.md#section1520210917535)。

### 变更特性

**ohpm-repo不再依赖node-fetch三方库**

ohpm-repo依赖的node-fetch三方库由于长时间未更新维护。从ohpm-repo 5.5.1版本开始，不再依赖node-fetch三方库。

**变更影响**

基于ohpm-repo开发的插件，若使用了ohpm-repo依赖的node-fetch三方库，在升级到ohpm-repo 5.5.1版本后，使用该插件会有报错提示（找不到node-fetch库）。

**适配指导**

方案一：将该插件中的node-fetch替换成其他三方库。

方案二：在ohpm-repo安装包中执行“npm install node-fetch@2.7.0”，自行安装上node-fetch三方库。

## ohpm-repo 5.4.5 Beta

### 新增特性

新增CheckUpdate API，支持查询当前引入的三方库是否有更新。具体请参考[CheckUpdate](ide-interface-protocol.md#section10485176173712)。

## ohpm-repo 5.4.3 Beta

### 新增特性

* ohpm-repo支持基于dockerfile进行私仓服务搭建。具体请参考[基于Dockerfile部署ohpm-repo私仓](ide-ohpm-dockerfile.md)。
* ohpm-repo拉取元数据时支持拉取精简版本的元数据。具体请参考[ohpm仓库接口协议](ide-interface-protocol.md#section1520210917535)。

## ohpm-repo 5.4.0

### 新增特性

ohpm-repo支持导出和导入包权限数据。具体请参考[ohpm-repo export\_pkgPermission](ide-ohpm-repo-export-pkgpermission.md)和[ohpm-repo import\_pkgPermission](ide-ohpm-repo-import-pkgpermission.md)。

## ohpm-repo 5.3.0

### 新增特性

* 支持配置多个仓库，并能够为每个仓库设置可读策略，可写策略和发布策略。具体请参考[仓库管理](ide-ohpm-depot-management.md)。

* 支持为每个包配置管理权限，支持配置包的查看者，维护者和所有者。具体请参考[包权限管理](ide-package-permission-management.md)。

## ohpm-repo 5.2.0

### 新增特性

ohpm-repo支持三方库字节码文件的OHMUrl版本一致性校验。具体请参考[content\_check\_plugin](ide-ohpm-repo-configuration.md#section1216516278174)。

**说明** 

更多历史版本请参考[版本说明](../harmonyos-releases/history-versions.md)。
