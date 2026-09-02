---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-44
title: 如何实现动态修改应用图标
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何实现动态修改应用图标
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:c77253aa71c5bb760405ccc1c455c05e8365c6aa7e7fdaf447adab25b182c38e
---

## 场景一

### 问题现象

动态图标切换调用selectDynamicIcon接口只能再次进入应用才能生效吗？

### 解决方案

通常情况下通过使用[selectDynamicIcon](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerselectdynamicicon)接口可以实现实时动态切换应用图标，而不需要重启应用。但如果应用包名中出现下划线，可能会造成切换图标无法即刻生效，该问题在5.0.0.135版本后已修复，升级最新版本可解决该问题。

## 场景二

### 问题现象

用户切换为个性图标B后，卸载重新下载安装应用，是否会保留用户设置的图标B？

### 解决方案

不会，重新下载后会重新回到默认图标。

## 场景三

### 问题现象

应用图标可以配置多少个图标，开发者需要配置更多的图标如何申请？

### 解决方案

默认可配置5个图标，最多可以配置10个，超出5个可以在AGC的互动中心联系在线客服申请添加配额或发送邮件申请。

邮件发送地址与[开通图标管理服务](../harmonyos-guides/appgallery-appinfo-manage.md#申请开通服务)一致，邮件标题和内容需要参考如下模板稍作修改，注意区分：

邮件标题：HarmonyOS应用图标数量扩充申请-XXX应用。

邮件内容：

开发者账号ID：XXXXX；

应用名称：XXXXX；

应用ID：XXXXX；

应用包名：XXXXX；

应用状态：XXXXX；

申请说明：默认5个应用图标无法满足开发需求，申请扩充应用图标数量至X个。

## 场景四

### 问题现象

如何实现动态修改应用图标，能否提供参考案例？

### 解决方案

可以参考[应用图标动态切换](../harmonyos-guides/appgallery-appinfo-use.md)。
