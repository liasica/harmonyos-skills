---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file-configuration
title: 应用共享目录配置
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用共享目录配置
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:af31f26fcd4e1bbc97b904cd2ec5a311cdf58c31ca2b46991c5d95fdfd455c48
---

从API版本23开始，系统支持配置共享目录。在[应用文件分享](share-app-file.md)场景中，开发者可[配置共享目录](share-app-file-configuration.md#配置共享目录)，配置后仅共享目录中的文件可供用户分享给其他应用查阅，以防止应用敏感数据泄露。配置仅在手机（Phone）、平板（Tablet）上生效。

**说明** 

从API版本26.0.0开始，可配置共享目录范围扩大，请开发者按照最新范围进行配置，下述配置指导配套版本为26.0.0。

从API版本26.0.0开始，系统支持配置应用捐献沙箱目录。当配置了共享目录时，开发者可[配置捐献沙箱目录](share-app-file-configuration.md#配置捐献沙箱目录)。捐献目录为共享目录的子目录。应用配置捐献目录后，文件管理器等系统应用可访问并操作其中的文件数据。

以文件管理器上的交互体验为例，应用配置了捐献目录后，用户在手机、平板设备上可通过文件管理器查阅、修改捐献目录中的文件。配置仅在手机（Phone）、平板（Tablet）上生效。

## 开发步骤

1. 开发者可在应用模块级配置文件[src/main/module.json5](module-configuration-file.md)的module标签中添加shareFiles标签，以实现对沙箱共享目录权限的限制。若未配置共享目录，则默认允许应用共享其自身沙箱内的文件。

   **shareFiles标签**

   ```json5
   {
     "module": {
       // ...
       "shareFiles": "$profile:share_files", // 资源配置，指向profile下面定义的配置文件share_files.json
       // ...
     }
   }
   ```
2. 在开发视图的resources/base/profile目录中定义配置文件share\_files.json，以标识当前模块所有共享路径的权限信息。

   文件名可修改为符合系统命名规则的文件名，但需要和shareFiles标签配置的文件名一致。

   **share\_files标签说明**

   | 属性名称 | 含义 | 数据类型 | 必填 |
   | --- | --- | --- | --- |
   | scopes | 允许共享的范围，详见[配置共享目录](share-app-file-configuration.md#配置共享目录)。 | 对象数组 | 否 |
   | sharingOSPath | 应用捐献给操作系统的沙箱目录，详见[配置捐献沙箱目录](share-app-file-configuration.md#配置捐献沙箱目录)。 | 字符串 | 否 |
   | sharingOSSubpath | 应用捐献给操作系统的沙箱目录的子目录，详见[配置捐献沙箱目录](share-app-file-configuration.md#配置捐献沙箱目录)。 | 字符串 | 否 |
   | sharingOSPermission | 应用捐献给操作系统的沙箱目录的访问权限，详见[配置捐献沙箱目录](share-app-file-configuration.md#配置捐献沙箱目录)。 | 字符串 | 否 |

   **说明** 

   应用更新时如涉及配置变更，将依据新配置进行管控，已分享文件的临时权限不受影响。

### 配置共享目录

| 属性名称 | 含义 | 数据类型 | 必填 |
| --- | --- | --- | --- |
| path | 共享路径配置，路径第一级支持el1~el5级别加密目录，第二级仅支持下列目录：  - base  - distributedfiles  - cloud  详细限制见[路径限制说明](share-app-file-configuration.md#路径限制说明)。  **起始版本：** 26.0.0 | string | scopes存在时必填 |
| permission | 共享路径权限。支持的取值如下：  - r：只读。  - r+w：读写。  **起始版本：** 23 | string | scopes存在时必填 |

### 路径限制说明

1.路径深度限制：

* 单路径最浅需配置2级，如/el2/base。
* 单路径最深可配置10级，如/el2/base/files/level4/level5/level6/level7/level8/level9/level10。

2.路径数量限制：

* 配置的路径不可重复，最多可配置20条路径。

3.路径格式限制：

* 必须以/开头，不允许有'.'、'..'、'\0'字符，不允许以'/'结尾。

4.父子目录限制：

* 存在父目录配置时，不允许配置子目录。
* 如已配置/el2/base/parentsA，那么不允许再配置/el2/base/parentsA/childrenA，允许配置/el2/base/parentsB/childrenB。

5.验证方式及定位：

* 为保持与旧版本系统的兼容性，当应用的任何一条路径配置不符合路径限制时，会自动清除该应用的全部已配置路径。可通过系统日志搜索相关报错，关键字："TransAndSetToMapInner failed for bundle"。

### 配置捐献沙箱目录

应用需要向操作系统捐献沙箱目录时，需要在配置文件share\_files.json中填写sharingOSPath、sharingOSSubpath、sharingOSPermission三个字段。

| 属性名称 | 含义 | 数据类型 |
| --- | --- | --- |
| sharingOSPath | 应用捐献给操作系统的沙箱目录，取值必须为scopes列表中已配置的path值。未配置该字段则表示不向操作系统捐献目录，系统应用如文件管理器、FilePicker等将无法查看应用捐献的沙箱目录。  **起始版本：** 26.0.0 | 字符串 |
| sharingOSSubpath | 应用捐献给操作系统的沙箱目录的子目录。仅当sharingOSPath配置时必填，长度不超过32个字符，将"sharingOSPath"+"sharingOSSubpath"拼接后的路径，作为捐献给操作系统的目录，""空串代表直接捐献sharingOSPath，有字符则以/开头，不允许有'.'、'..'、'\0'字符。  **起始版本：** 26.0.0 | 字符串 |
| sharingOSPermission | 应用捐献给操作系统的沙箱目录的访问权限。仅当sharingOSPath配置时必填，权限必须是scopes中对应路径permission的一个子集，不可超出原配置权限。  **起始版本：** 26.0.0 | 字符串 |

share\_files.json示例：

```json
{
  "share_files": {
    "scopes": [
      {
        "path": "/el2/base/files",
        "permission": "r+w"
      },
      {
        "path": "/el3/distributedfiles/files/tmp",
        "permission": "r+w"
      }
    ],
    "sharingOSPath" : "/el2/base/files",
    "sharingOSSubpath" : "/subdir",
    "sharingOSPermission": "r"
  }
}
```
