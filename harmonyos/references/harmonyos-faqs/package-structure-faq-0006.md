---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0006
title: 多HAP包集成同一HSP规则与配置常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 多HAP包集成同一HSP规则与配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:803b0557730895495bad7cb3a5d26834ff0004adcdc8f2498197b298bf61204c
---

**Q：代码复用在软件工程中很常见。复杂业务场景中，一般会将业务功能实现拆分成各个模块，并将通用的能力/服务抽象到底层通用框架/模块。如果只有一个应用，各个模块可以放在同一个工程下，来实现代码和资源的共享；如果有多个应用，即多个HAP包，怎么去集成同一个HSP呢？**

**A**：实现不同项目的代码和资源共享，需要使用集成态HSP。可以将需要复用的工程代码产物包改成集成态HSP，以此来解决业务工程和基础工程间bundleName的强耦合问题，但versionCode、minAPIVersion字段仍需要人工提前规划，来保证这些字段在这两个工程间一致。

1. 规划版本号和最小API版本，即保证versionCode、minAPIVersion字段在多个项目工程一致。
2. 使用[集成态HSP](../harmonyos-guides/integrated-hsp.md)来完成bundleName字段的解耦。
3. 关于后续演进，请参考下面场景：

   场景一：业务工程不涉及改动，但基础工程需要演进（功能增强/修复bug等）。只需要修改基础工程中的versionCode、minAPIVersion（如果涉及的话）。其他业务工程后续迭代时，增加对应业务工程的versionCode版本，使之与基础工程中的versionCode版本一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/8d_TblAmTIGsk1HGtKlkDw/zh-cn_image_0000002772029372.png "点击放大")

   场景二：基础工程不涉及改动，业务工程需要演进（功能增强/修复bug等）。不仅需要增加业务工程中的versionCode，同时需要修改基础工程中的versionCode。如果涉及到minAPIVersion改动，同理，也需要两者一起修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/IWH3JSueR--SuwuV07cZow/zh-cn_image_0000002801429155.png "点击放大")

**Q：安装HAP包时提示错误码10024？**

**A**：是因为基础工程的bundleName、versionCode、minAPIVersion没有与业务工程一致。这种场景需要基础工程使用集成态HSP来解决（集成态HSP的bundleName可以不一致，但versionCode、minAPIVersion仍需要与业务工程一致）。另外，需要注意的是，使用时工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于应用内HSP。

**Q：企业内部应用是否可以使用集成态HSP？**

**A**：可以。
