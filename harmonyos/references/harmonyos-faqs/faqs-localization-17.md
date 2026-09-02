---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-17
title: 资源文件string.json中修改后无法同步修改代码
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 资源文件string.json中修改后无法同步修改代码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6720fb082e306366b31417a3652ff65a956cb7dea447c7dc4ddc93a9b87215ea
---

## 问题现象

在string.json文件中定义了多个字符串资源，如果项目中多处使用getContext().resourceManager.getStringByNameSync("")获取指定键名的字符串资源，那么在资源文件修改key值时,getContext().resourceManager.getStringByNameSync("")这里面的key不会同步修改。

## 背景知识

在HarmonyOS开发中，getContext().resourceManager.getStringByNameSync("") 方法用于同步获取资源管理器中的字符串资源。该方法接收一个字符串类型的参数，表示资源的名称，如果没有指定名称，方法将返回一个空字符串。

## 解决方案

通过getContext().resourceManager.getStringSync($r("app.string.EntryAbility\_desc").id) 获取即可完成双向同步修改。
