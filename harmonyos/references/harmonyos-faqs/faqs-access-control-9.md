---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-9
title: 系统安全能力哪些是天然具备的，哪些需要开发者适配
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 系统安全能力哪些是天然具备的，哪些需要开发者适配
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4268dc873318fb2c9efbd432d21c87efc62c073e3b178d5923f620a6cb86769a
---

* **系统机制无需三方适配****：**应用沙箱隔离、权限管理、App签名、代码签名、应用加密、数据分级标签、SELinux、Capability、CFI、堆栈保护、安全启动、系统OTA升级安全、内核完整性保护、MAC随机化、安全芯片管理框架、TEE。
* **需要适配的安全机制：**混淆加固（默认开启）、EL1/EL2类文件加密、EL3/EL4类文件加密、DLP数据版权保护、密码自动填充、FIDO/IFAA、人脸认证、分布式认证、指纹认证、PIN认证、设备风险查询、实名认证、申请开发者证书（Debug 和 Release）、申请Provision Profile（权限申请 - 可选）、代码安全扫描、Release签名上架发布。
* **需要遵守的审核项：**应用合规扫描、应用权限审核。
