---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/assessment-kit-intro
title: Automatic Scene Configuration Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > Automatic Scene Configuration Kit（场景配置服务） > Automatic Scene Configuration Kit简介
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:806ce9a7356fb450e3791b1dff142556cb9559df5536ada6c0d07f66353c1fd3
---

从API version 26.0.1开始，Automatic Scene Configuration Kit（场景配置服务）为应用提供场景化的系统能力配置与管控能力，由系统在系统侧实施配置与管控，应用无需自行实现拦截逻辑，也无法绕过或自行解除限制。本Kit当前由评估管理（assessment）模块承载上述能力，面向线上考试、培训测评等需要保障过程公平的业务场景，管控全程需用户确认或可被用户感知。

## 使用场景

* 线上正式考试：在学业水平考试、招生入学考试等正式考试场景中，限制作答期间设备的部分系统能力，防止作弊与试题泄露。
* 职业认证与标准化测验：在职业资格认证、语言能力测验等标准化测验场景中，为所有考生提供一致的受限作答环境，保障成绩可比。
* 培训测评：在企业培训、课程结业测评等场景中，限制与测评无关的应用运行，帮助参与者专注完成测评。

## 能力范围

* 评估管理：提供评估场景的开始与结束、评估状态查询与评估配置获取、评估过程事件回调，以及评估期间通知受限等系统能力管控。开发详情参见[评估管理开发指南](assessment-guide.md)，接口详情参见[@ohos.customization.assessment (评估管理)](../harmonyos-references/js-apis-customization-assessment.md)。

## 亮点/特征

* **系统侧统一管控**：场景内的系统能力限制由系统在系统侧统一实施，不依赖应用自身实现，应用无法绕过，也无法自行解除。
* **管控全程需用户确认或可被用户感知**：进入管控前由系统弹出确认弹窗征得用户同意，用户取消则管控不生效，管控解除后设备恢复正常状态。
* **管控状态与中断原因可回调感知**：应用通过回调获取场景开始、中断与结束事件，中断事件携带原因码与描述信息。

## 约束与限制

* 本Kit能力仅可在Stage模型下使用。
* 支持设备：Phone | PC/2in1 | Tablet。
* 调用本Kit能力需申请受限权限，权限信息、审批规则与模块级规格参见[评估管理开发指南](assessment-guide.md#约束与限制)。

## 与相关Kit的关系

* [Ability Kit](abilitykit-overview.md)：本Kit依赖Ability Kit提供的应用模型与上下文能力，仅支持Stage模型应用，场景配置请求需由具备UIAbility上下文的应用发起。
* [Notification Kit](notification-overview.md)：场景管控生效期间通知受限，包括无铃声、震动与横幅等，该限制由系统侧统一实施，本Kit不单独提供通知相关接口。

## 与开发指南的关系

本文说明Automatic Scene Configuration Kit是什么、提供哪些模块与Kit级约束；[评估管理开发指南](assessment-guide.md)说明评估管理模块怎么做，含模块级约束与限制、开发流程、接口说明、示例代码、调测验证与常见问题；[Automatic Scene Configuration Kit术语](assessment-glossary.md)统一本文档集的名词定义；接口签名与错误码参见../reference/apis-assessment-kit/下的[@ohos.customization.assessment (评估管理)](../harmonyos-references/js-apis-customization-assessment.md)与[评估管理错误码](../harmonyos-references/errorcode-assessment.md)。
