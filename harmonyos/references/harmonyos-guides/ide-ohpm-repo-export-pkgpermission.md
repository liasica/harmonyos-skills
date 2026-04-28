---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkgpermission
title: ohpm-repo export_pkgPermission
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo export_pkgPermission
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:45+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4df6b8f1216e7df2767df2472e73dc8ab845183fd8eaa2974927528d0c5a41bc
---

ohpm-repo 5.4.0版本开始，支持导出包权限数据。

## 命令格式

```
1. ohpm-repo export_pkgPermission [option]
```

## 功能描述

在当前的工作目录中，导出记录包权限的packagePermission\_xxx.json文件。

## 选项

### --repos

* 默认值：无

* 类型：String

在export\_pkgPermission命令后面配置--repos <string>，导出ohpm-repo中指定仓库的包权限。多个仓库之间通过英文逗号隔开，例如"export\_pkgPermission --repos one,two"，即导出仓库one和仓库two中的包权限。若未配置此参数，将默认导出ohpm-repo中所有仓库的包权限。

## 示例

**从ohpm-repo中导出所有仓库的包权限**

```
1. ohpm-repo export_pkgPermission
```

结果示例：

```
1. PS D:\> ohpm-repo export_pkgPermission
2. ...
3. [2025-09-16T14:58:24.806] [INFO] default - successfully exported all package permissions: saved to "D:\packagePermission_1758005904806.json".
```

```
1. // packagePermission_1758005904806.json中记录着ohpm-repo中所有仓库的包权限
2. [
3. {
4. "repoName": "groupone",
5. "packageName": "testone",
6. "readPolicy": 1, // 记录包的可见性配置（1：公开可读，2：授权可读）
7. "packagePermission": {
8. "admin": 4, // 记录用户名为admin的用户对该包的权限 （1：查看者权限，2：维护者权限，4：所有者权限）
9. "user": 2,
10. }
11. },
12. ...
13. {
14. "repoName": "ohpm",
15. "packageName": "testtwo",
16. "readPolicy": 2,
17. "packagePermission": {
18. "admin": 2,
19. "user": 4,
20. }
21. }
22. ]
```

**从ohpm-repo中仅导出仓库名为ohpm的包权限**

```
1. ohpm-repo export_pkgPermission --repos ohpm
```

结果示例：

```
1. PS D:\> ohpm-repo export_pkgPermission --repos ohpm
2. ...
3. [2025-09-16T15:41:06.124] [INFO] default - successfully exported all package permissions for the specified repository: saved to "D:\packagePermission_1758008466123.json".
```

```
1. // packagePermission_1758008466123.json中记录着ohpm-repo中仓库ohpm的包权限
2. [
3. {
4. "repoName": "ohpm",
5. "packageName": "testtwo",
6. "readPolicy": 2,
7. "packagePermission": {
8. "admin": 2,
9. "user": 4,
10. }
11. },
12. ...
13. ]
```
