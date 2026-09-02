---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-kit-new-00002
title: IKEv2 IPSec MSCHAPv2类型VPN无法连接如何解决
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > IKEv2 IPSec MSCHAPv2类型VPN无法连接如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:234695df0e2ecd73094fd15d5b15fda610112280a0d8f485e4f60ab16e6e8cee
---

## 问题现象

升级系统版本后，IKEv2 IPsec MSCHAPv2类型VPN无法连接。

## 背景知识

VPN连接时需要验证服务器证书，证书验证依赖根证书。可通过[VPN扩展](../harmonyos-guides/net-vpnextension.md#简介)建立VPN连接。

## 问题定位

当前系统VPN不支持读取系统预置的根证书。如果连接时VPN服务器不发送根证书，则VPN连接会因证书验证失败而无法建立。

## 分析结论

系统VPN不支持读取系统预置的根证书，当VPN服务器不发送根证书时，证书验证失败导致VPN无法连接。

## 修改建议

手动安装并选择根证书。

1. 下载根证书：根证书类型需咨询VPN服务提供商，由服务提供商提供连接所需的证书类型和证书下载方式。以ISRG Root X1根证书为例，打开系统自带浏览器，在搜索栏输入ISRG Root X1证书下载地址并点击搜索，弹出下载标签后点击立即下载，等待ISRG Root X1证书下载完成。
2. 安装根证书：打开设置>隐私和安全>高级>证书与凭据>从储存设备安装>CA证书，在弹出页面点击浏览，点击浏览器后选中下载的证书，点击完成即可完成证书安装。
3. 选择根证书：新建VPN时，正常填写VPN信息后，IPsec CA证书选择已安装的根证书（如ISRG Root X1）后保存即可。
