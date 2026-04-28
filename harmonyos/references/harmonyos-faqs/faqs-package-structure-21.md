---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-21
title: 如何正确引用HAR/HSP包模块
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何正确引用HAR/HSP包模块
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:9d0202ae49e8ffdb0b3b39e02671acd837d550451e0517e5508bf02166adc13c
---

在HarmonyOS应用开发中，处理包（HAR/HSP）模块间的依赖很常见。正确的依赖处理方式能确保代码模块化和可维护性，同时减少团队开发中的管理与沟通成本。以下是如何引用包模块的推荐和不推荐做法。

* 推荐方式：

  import { add } from "library";
* 不推荐方式：

  不推荐使用相对路径或绝对路径进行引用。这种做法会破坏模块间的隔离性，增加团队开发的管理和沟通成本，且难以维护。例如：

  import { add } from "../../library/src/main/ets/page/Index";

总结来说，为了保持代码的模块化、提高可维护性以及降低团队协作的复杂度，推荐使用包名进行模块间的依赖引用。避免使用相对或绝对路径，以维护项目的结构清晰和高效的团队合作。更多请参见[HAR](../harmonyos-guides/har-package.md)。
