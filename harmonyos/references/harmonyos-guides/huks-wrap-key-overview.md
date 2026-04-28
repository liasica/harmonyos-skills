---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-wrap-key-overview
title: 加密导出导入密钥介绍
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 加密导出导入密钥 > 加密导出导入密钥介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:40fda5b37f0126c16d990d1733274fa7fe057a1625a86ea81e7735ad10876f8b
---

为支持应用在卸载后仍能保留密钥，从API 20开始，HUKS新增了加密导出密钥与加密导入密钥的功能。

由于应用卸载时，其在HUKS中存储的密钥会被清除，通过加密导出导入密钥功能，开发者可在应用卸载前将密钥加密导出保存，并在应用重新安装后将加密密钥导入恢复，从而实现应用卸载后保留密钥。

说明

* 仅在手机、平板、PC/2in1、智能穿戴上支持加密导出导入密钥功能。
* 需要加密导出的密钥，必须在生成时就指定为允许加密导出。
* 加密导出的密钥，只能在同一台设备上的同一应用导入。
* 支持加密导出导入[群组密钥](huks-group-key-overview.md)。当导出时为普通密钥，导入时指定为群组密钥时，需要认证TUI PIN，其他情况可以直接导入。
