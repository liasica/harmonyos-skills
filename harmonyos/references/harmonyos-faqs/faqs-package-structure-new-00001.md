---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-new-00001
title: 应用预装及上架全量包与取包逻辑说明
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 应用预装及上架全量包与取包逻辑说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:fdff2e6fcda9837535c3cfbe5489c0b882efc07a82464fc5a7f36904da37e99c
---

## 问题现象

问题一：应用预装场景只装一个基础包，上架应用商店的时候上架一个全量的包是否可行。

问题二：预装取包的逻辑是根据deliveryWithInstall: true属性，还是根据模块包名取的。

## 背景知识

应用预装是指设备出厂前将应用包预置到系统中。在HarmonyOS中，应用可通过配置deliveryWithInstall属性控制模块是否随应用安装。按需加载机制依赖ag\_config.json配置文件识别应用管控信息，依赖包也要求安装。

## 解决方案

问题一：可行。

问题二：预装是按"deliveryWithInstall: true"加上依赖包预置包体，并预置了ag\_config.json配置文件。按需加载是通过该文件识别应用管控信息，依赖包也要求安装。
