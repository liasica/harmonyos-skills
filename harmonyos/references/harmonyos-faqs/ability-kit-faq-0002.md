---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0002
title: Context类型与关系常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > Context类型与关系常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:43+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:480d910fb4ca75abf0263dea942a41a676f8cf84528bc224acf5f00ab15c4a04
---

**Q：API参考文档中说明getContext方法从API version 18开始弃用，建议使用UIContext中的getHostContext替代。在使用过程中发现，将返回值类型注解为Context时编译报错，请问两者有什么差异？**

**A**：

| 对比维度 | getContext | getHostContext |
| --- | --- | --- |
| 废弃状态 | 从API 18起废弃，不再推荐使用。 | API 12引入，API 18起作为推荐替代方案。 |
| 返回值类型 | Context | Context|undefined |
| 获取Context方式 | let context: Context = getContext(this); | let context: Context|undefined = this.getUIContext().getHostContext(); |

**Q：ApplicationContext、UIAbilityContext、Context的区别是什么？**

**A**：ApplicationContext 和 UIAbilityContext 都继承自基类 Context，不同的 Context 具有不同的属性和方法。

ApplicationContext：应用级别的Context，提供了订阅应用组件生命周期变化、系统内存变化和应用系统环境变化的能力。可以在UIAbility、ExtensionAbility、AbilityStage中获取。

UIAbilityContext：每个UIAbility包含一个Context属性，用于操作应用组件和获取组件配置信息。

参考链接：[应用上下文Context](../harmonyos-guides/application-context-stage.md)。

**Q：UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系？**

**A**：常见UIContext、Ability、UIAbilityContext的关系如下：

1. Ability的上下文是AbilityContext。ArkUI实例的上下文是[UIContext](../harmonyos-guides/arkts-global-interface.md)，由窗口创建并管理所有UI对象。窗口可以通过[windowStage.loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)拉起ArkUI实例。
2. Ability是应用管理生命周期的对象，持有window对象。
3. UIAbility的上下文是UIAbilityContext。UIContext与UIAbilityContext没有直接联系，无法互相转化。
