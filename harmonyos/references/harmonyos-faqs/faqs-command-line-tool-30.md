---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-30
title: 如何解决Could not find Node.js.Please install Node.js first
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何解决Could not find Node.js.Please install Node.js first
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7c77f4c658c2417a75abe5781684f240315a791a29b6c8901fe17dd3acb2972f
---

## 问题现象

codelinter在Linux环境执行报错：Could not find Node.js.Please install Node.js first。

## 背景知识

[codelinter](../harmonyos-guides/ide-command-line-codelinter.md)同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

## 解决方案

1. 通过命令行工具排查是否安装node，并配置环境变量。
2. 检查当前环境是否支持which命令，若不支持请安装，或者通过如下规避方式：通过修改command-line-tools\codelinter\bin路径下的脚本，将which命令替换为当前系统支持的命令即可。
