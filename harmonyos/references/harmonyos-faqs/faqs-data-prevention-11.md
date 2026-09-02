---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-data-prevention-11
title: 应用更换证书后，能否访问之前用Asset Store Kit（ASSET）存储的关键资产
breadcrumb: FAQ > 系统开发 > 安全 > 数据安全存储（Data Prevention） > 应用更换证书后，能否访问之前用Asset Store Kit（ASSET）存储的关键资产
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:05fa4eae1eae136c8a79b50522f55d659026f2b2074b551279ea0f35ffa31411
---

## 问题现象

应用更换证书后，如果证书公钥变更，会导致ASSET识别的应用身份（AppID）发生变化，使得应用无法访问之前存储的关键资产。

## 解决方案

所有的关键资产都受属主访问控制保护，只允许关键资产被其属主（写入该关键资产的业务）访问。ASSET从系统获取应用的AppID（由包名、下划线和证书公钥的Base64编码组成）来识别应用身份。只要应用的证书公钥（p12文件）不变，ASSET获取到的AppID就和证书变更之前一样，应用就能访问之前存储的关键资产。

若证书公钥必须变更，应用可以考虑以下方案：

1、利用ASSET的群组共享功能，为关键资产设置群组属性，证书更新后应用可以读取同一个群组的关键资产；

2、在更新证书前使用其他方案备份数据，如使用Universal Keystore Kit（密钥管理服务）临时加密关键资产保存到应用沙箱里。
