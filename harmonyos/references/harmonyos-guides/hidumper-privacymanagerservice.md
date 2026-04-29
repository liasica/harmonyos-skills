---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper-privacymanagerservice
title: PrivacyManagerService
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > hidumper > PrivacyManagerService
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:66e6c9c3532dc5987bdfe7e67eafaa0ce3a418f9d81ae5a69c88884eeaeb2b6d
---

PrivacyManagerService是访问控制基于[hidumper](hidumper.md)增强开发的命令行能力，可显示访问控制基础信息，获取敏感权限使用记录。

## 环境准备

根据hidumper工具指导，完成[环境准备](hidumper.md#环境要求)。

## 获取帮助信息

如果需要查看帮助信息，可以通过下列命令实现。

```
1. hidumper -s PrivacyManagerService -a '-h'
```

**使用样例：**

```
1. -------------------------------[ability]-------------------------------

4. ----------------------------------PrivacyManagerService----------------------------------
5. Privacy Dump:
6. Usage:
7. -h: command help
8. -t <TOKEN_ID>: according to specific token id dump permission used records
```

## 获取敏感权限使用记录信息

支持通过应用进程的tokenid，查看敏感权限使用记录的信息，可以通过下列命令实现。

```
1. hidumper -s PrivacyManagerService -a '-t <tokenId>'
```

命令所需的tokenId可以通过[atm-tool](atm-tool.md#查询命令)进行查询。

**使用样例：**

```
1. hidumper -s PrivacyManagerService -a '-t 536992218'

3. -------------------------------[ability]-------------------------------

6. ----------------------------------PrivacyManagerService----------------------------------
7. Privacy Dump:
8. {
9. "permissionRecord": [
10. {
11. "bundleName": "com.ohos.camera",
12. "isRemote": false,
13. "permissionName": "ohos.permission.READ_IMAGEVIDEO",
14. "lastAccessTime": 1508577149393,
15. "lastAccessDuration": 0,
16. "accessCount": 2
17. }
18. ]
19. }
```
