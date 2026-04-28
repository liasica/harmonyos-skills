---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file-configuration
title: 应用共享目录配置
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用共享目录配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ded5dc74b6bfaa63d53ae7904d7e2ff034468ab5d4d48887d32c2290fdf2133e
---

从API version 23开始，系统新增支持共享目录配置功能。在[应用文件分享](share-app-file.md)场景中，开发者可配置共享目录范围，防止应用敏感数据泄露。

## 开发步骤

1. 开发者可在应用模块级配置文件[src/main/module.json5](module-configuration-file.md)的module标签中添加shareFiles标签，以实现对沙箱共享目录权限的限制。若未配置共享目录，则默认允许应用共享其自身沙箱内的文件。

   **shareFiles标签**

   ```
   1. {
   2. "module": {
   3. // ...
   4. "shareFiles": "$profile:share_files", // 资源配置，指向profile下面定义的配置文件share_files.json
   5. // ...
   6. }
   7. }
   ```
2. 在开发视图的resources/base/profile下面定义配置文件share\_files.json，以标识当前模块所有共享路径的权限信息。

   文件名share\_files可修改为任意合法文件名，但需要和shareFiles标签配置的文件名一致。

   **share\_files标签说明**

   | 属性名称 | 含义 | 数据类型 | 必填 |
   | --- | --- | --- | --- |
   | scopes | 允许共享的范围，详见scopes标签说明。 | 对象数组 | 否 |

   **scopes标签说明**

   | 属性名称 | 含义 | 数据类型 | 必填 |
   | --- | --- | --- | --- |
   | path | 共享路径配置，当前仅支持[el2目录](share-app-file.md#应用可分享目录)，scopes中的path不可重复。支持的取值如下：  - /base/files  - /base/preferences  - /base/haps | string | scopes存在时必填 |
   | permission | 共享路径权限。支持的取值如下：  - r：只读。  - r+w：读写。 | string | scopes存在时必填 |

说明

应用更新时如涉及配置变更，将依据新配置进行管控，已分享文件的临时权限不受影响。

share\_files.json示例：

```
1. {
2. "share_files": {
3. "scopes": [
4. {
5. "path": "/base/files",
6. "permission": "r+w"
7. }
8. ]
9. }
10. }
```
