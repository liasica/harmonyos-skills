---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-pkgpermission
title: ohpm-repo export_pkgPermission
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo export_pkgPermission
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:18+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b78f061509255f3975a41e88364079626efd96427f3d8626a2c51eea8492286f
---

ohpm-repo 5.4.0版本开始，支持导出包权限数据。

## 命令格式

```screen
ohpm-repo export_pkgPermission [option]
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

```screen
ohpm-repo export_pkgPermission
```

结果示例：

```screen
PS D:\> ohpm-repo export_pkgPermission
...
[2025-09-16T14:58:24.806] [INFO] default - successfully exported all package permissions: saved to "D:\packagePermission_1758005904806.json".
```

```screen
// packagePermission_1758005904806.json中记录着ohpm-repo中所有仓库的包权限
[
  {
    "repoName": "groupone",
    "packageName": "testone",
    "readPolicy": 1, // 记录包的可见性配置（1：公开可读，2：授权可读）
    "packagePermission": {
      "admin": 4, // 记录用户名为admin的用户对该包的权限 （1：查看者权限，2：维护者权限，4：所有者权限）
      "user": 2,
    }
  },
  ...
  {
    "repoName": "ohpm",
    "packageName": "testtwo",
    "readPolicy": 2,
    "packagePermission": {
      "admin": 2,
      "user": 4,
    }
  }
]
```

**从ohpm-repo中仅导出仓库名为ohpm的包权限**

```screen
ohpm-repo export_pkgPermission --repos ohpm
```

结果示例：

```screen
PS D:\> ohpm-repo export_pkgPermission --repos ohpm
... 
[2025-09-16T15:41:06.124] [INFO] default - successfully exported all package permissions for the specified repository: saved to "D:\packagePermission_1758008466123.json".
```

```screen
// packagePermission_1758008466123.json中记录着ohpm-repo中仓库ohpm的包权限
[
  {
    "repoName": "ohpm",
    "packageName": "testtwo",
    "readPolicy": 2,
    "packagePermission": {
      "admin": 2,
      "user": 4,
    }
  },
  ...
]
```
