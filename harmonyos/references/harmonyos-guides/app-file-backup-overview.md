---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-backup-overview
title: 应用数据备份恢复概述
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 应用数据备份恢复概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca8787d3eda48ce1ed9679bd85a3ddf1df483edc7d4389a26ba37b91bd54809a
---

用户在使用应用的过程中，会产生对应的应用数据，如配置信息、业务数据等。为了保证用户数据不会因为应用升级、迁移等操作而丢失，应用需要接入数据备份恢复。

在开发前，需要先了解ExtensionAbility组件，建议参考[ExtensionAbility组件概述](extensionability-overview.md)。

BackupExtensionAbility是Stage模型中扩展组件ExtensionAbility的派生类，用于提供备份及恢复应用数据的能力。它是一种无界面的扩展组件，随着备份恢复任务的启动而运行，随着备份恢复任务的结束而退出。

不同应用所需实现的场景不同，分为：

* [应用接入数据备份恢复](app-file-backup-extension.md)：应用均可以接入数据备份恢复，在接入后，应用可通过修改配置文件定制备份恢复框架的行为，包括是否允许备份恢复、备份哪些数据。

  应用本身无法触发数据的备份和恢复，仅能进行备份恢复的配置。在[应用克隆](app-file-clone.md)和[应用数据迁移](app-data-migration-overview.md)中会触发数据备份恢复，应用本身接入数据备份恢复即可。如需验证接入效果请参考[应用数据备份恢复验证指导](app-file-backup-dataclone.md)。
* 应用触发数据备份恢复（仅对系统应用开放）。
