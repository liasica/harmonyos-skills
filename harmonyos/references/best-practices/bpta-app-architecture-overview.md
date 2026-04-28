---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-architecture-overview
title: 架构概览
breadcrumb: 最佳实践 > 应用架构 > 架构概览
category: best-practices
scraped_at: 2026-04-28T08:19:40+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:46c563f3b4e22c2d6e8d0b3d4869995172c8149c3bd900902ccec327626a705f
---

应用规模扩大和业务需求复杂化导致代码复杂度增加。良好的应用架构设计至关重要，旨在使应用更易于维护、扩展和测试。

在应用开发过程中，经常面临以下挑战：

* 代码组织不清晰，模块间的耦合度高，导致一个模块的变动可能影响其他模块，增加维护难度。
* 应用扩展性不足，添加新功能通常需要大幅修改现有代码。

为了解决这些问题，开发者应关注以下方面的架构设计：

* [分层架构设计](bpta-layered-architecture-design.md)：将应用划分为产品定制层、基础特性层和公共能力层，降低层间依赖性，提升代码可维护性。分层架构设计明确每层的职责和层间的交互机制，提供清晰的结构化开发框架。
* [模块化设计](bpta-modular-design.md)：将应用分解为多个功能模块，每个模块执行特定的功能。模块化设计提高代码的可理解性和可复用性，简化应用扩展和维护，降低系统各部分之间的耦合度。

说明

本文所介绍的HarmonyOS推荐的分层架构设计和模块化设计实例可参考"[HMOS世界](https://gitcode.com/harmonyos_samples/hmosworld)"。
