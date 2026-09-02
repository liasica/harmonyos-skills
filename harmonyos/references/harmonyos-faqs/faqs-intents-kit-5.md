---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-intents-kit-5
title: 意图框架接入流程问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 意图框架服务（Intents Kit） > 意图框架接入流程问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e27cb09c29ef9925db78d340191386b6c3ff538c99445081537069f52aaff116
---

## 问题现象

元服务/应用如何接入意图框架？

## 背景知识

[Intents Kit](../harmonyos-guides/intents-introduction.md)（意图框架服务）是HarmonyOS级的意图标准体系，意图连接了应用/元服务内的业务功能。意图框架能帮开发者将应用/元服务内的业务功能，智能分发到各系统入口，这个过程即智慧分发。其中系统入口包括：小艺对话、小艺搜索、小艺建议。

## 解决方案

元服务Intents Kit的开发方式与传统应用Intents Kit的开发方式相同，[接入流程](../harmonyos-guides/intents-access-flow.md)分为意向、开发、验证和上架四个步骤，有[习惯推荐](../harmonyos-guides/intents-habit-rec-access-programme.md)、[事件推荐](../harmonyos-guides/intents-event-rec-access-programme.md)、[技能调用](../harmonyos-guides/intents-skill-all-rec-access-programme.md)、[本地搜索](../harmonyos-guides/intents-search-rec-access-programme.md)几种接入方案，开发者可根据实际场景选取合适的接入方案完成元服务与意图框架的对接。

## 常见FAQ

Q：1000101101：failed because The application has not been registered with the InsightIntent报错原因？

A：接入时没有进行开发步骤中的调试白名单申请环节。

Q：为什么意图框架服务接入方案中云侧意图显示空白？

A：应用市场上架软件包后，没有进行意图框架的注册。

Q：意图框架目前开放智慧分发特性的垂域有哪些？

A：目前开放的垂域有旅游、视频、新闻、音乐等，详情可点击[各垂域的智慧分发特性列表](../service/intents-ai-distribution-characteristic-0000001901922213.md#section2656133582215)查看。

Q：为什么小艺意图框架调试打开后，设备一直显示未切换至“真机模式”。

A：应用已经上架，意图框架接入申请已经审核通过，但是还在灰度测试，完成后才能进行功能测试。

Q：APP如何开通意图框架服务？打开意图框架调试后，在小艺建议中没有看到测试条目怎么办？

A：开通意图框架服务参考[意图框架上架配置指导](../harmonyos-guides/intents-kit-listing-configuration.md)。在样机中打开设置，高级搜索意图框架，打开意图框架调试，再跑应用程序，等待1分钟左右，才能在小艺建议中看到测试条目。

Q：元服务接入意图框架需要额外开发分发功能吗？

A：不需要，意图框架能帮开发者将应用/元服务内的业务功能，智能分发到各系统入口，这个过程即[智慧分发](../harmonyos-guides/intents-introduction.md#智慧分发)。

Q：与小艺有哪些系统交互，比如是否需要上传历史问答记录等，数据存留是在本地还是云端。我们在小艺里能搜到某应用，但在应用市场里是搜索不到的？

A：交互方式：智能体通过系统级入口（如小艺语音）触发，无需上传历史问答记录。

数据存储：用户操作数据默认本地存储，云端数据需经用户授权后加密传输。

分发差异：小艺的分发和应用市场不同，小艺的分发特性可以参考[智慧分发特性](../service/intents-ai-distribution-characteristic-0000001901922213.md)。

Q：在哪些华为产品上可以使用，手机端的版本、ipad端、车载端等，EMUI是否可以支持？

A：支持手机、平板、车载等HarmonyOS设备，小艺智能体和意图框架都为HarmonyOS 5.0后HarmonyOS Next特性。

Q：开发者测试时提供的基础信息中的华为账号（uid）是开发者账号还是测试用户的华为账号？如何提供？

A：华为账号指的是开发者账号。可以通过如下两个步骤：

1. 电脑使用浏览器（以Chrome为例）登录华为商城，并且在网页上面登录华为账号。
2. 按F12进入开发者工具界面，按照“Application->cookies->网站地址->uid”的路径获取uid。

Q：小艺意图框架只支持Schema中预定义的意图嘛，是否可以在对应垂域下自定义一个意图？

A：从API version 20开始，支持通过[装饰器](../harmonyos-guides/insight-intent-decorator-development.md)开发标准意图以及自定义意图。

Q：使用意图框架时，应用和元服务哪个方案效率更高呢？两者分别适用于什么场景呢？

A：在使用意图框架服务时，应用和元服务都需要进行相同工作量的开发，才能实现意图调用，具体可参考[接入方案](../harmonyos-guides/intents-habit-rec-access-programme.md)。而元服务是HarmonyOS提供的一种轻量应用程序形态，具备秒开直达，适用于免安装场景；应用则需先安装。因此两者在意图识别方面都能完整处理。

Q：多个应用接入同一个意图时，系统会如何调用应用？

A：如果有多个应用都接入了同一个意图，HarmonyOS系统采用了一种基于任务优先级和调度策略的机制来管理应用程序。当用户触发该意图时，会根据各个应用的优先级和匹配度来决定最终哪个应用会被调用。具体来说，系统会根据应用的优先级和意图的匹配度进行排序，然后选择匹配度最高且优先级最高的应用进行调用。

如果多个应用的匹配度和优先级相同，系统会根据任务的创建时间或其他调度策略来选择调用哪个应用。如果一个应用设置了更高的优先级，或者在短时间内创建了更多的任务，系统会优先调度该应用。

综上所述，最终哪个应用会被调用取决于具体的系统的调度策略和应用的优先级设置。在实际开发中，建议应用开发者合理设置应用的优先级，以提高应用的响应速度和用户体验。

* 任务优先级：应用可以设置任务的优先级，系统会优先调度高优先级的任务。
* 调度策略：系统根据任务的需求和系统资源的情况，选择合适的任务进行调度。
* 应用优先级设置：应用可以通过设置自己的优先级来影响调度结果。通常，应用可以在配置文件中设置优先级，或者在运行时动态调整优先级。

Q：如果在第一次启动APP时使用insightIntent.shareIntent传了数据，那么之后的启动APP还需要再次调用shareIntent方法吗？再次调用是否会覆盖？

A：不需要再次调用，再次调用会覆盖。

Q：数据量多的时候的通常的解决方案是什么？

A：每次共享的数据条数不限，但是每次最多50KB数据量，可以一次性传多条数据。

Q：如何通过意图拉起同一个页面的多种不同场景？

A：当前意图只支持拉起页面，但是可以通过意图的传参自行处理不同的业务场景。

Q：基于函数的装饰器方案只需要添加装饰器就可以了吗？其他地方是否需要添加说明文件。

A：第一步在需要执行的函数Class上添加@InsightIntentFunction进行意图声明，第二步在目标执行函数上添加@InsightIntentFunctionMethod装饰器即可。

Q：如何接入意图框架功能一步达的场景？对应的domain如何填写？

A：接入意图框架功能一步达请参考[功能一步达场景方案](../harmonyos-guides/intents-skill-all-rec-one-step.md)，其中，功能一步达场景的domain固定为“ToolsDomain”，意图调用调测请参考[配置文件接入方式自测试方案](../harmonyos-guides/intents-skill-all-rec-dp-self-validation-con.md)，上架流程参考[意图标准协议上架指导](../harmonyos-guides/intents-kit-listing-standard-protocol.md)，不需要MCP协议上架。

Q：测试用户是否须为该项目团队下的成员？

A：是的，测试用户须为该项目团队下的成员，添加用户自测试方案可参考：[装饰器接入方式自测试方案](../harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator.md)。

Q：如何理解接入方案中的意图注册、端侧意图共享、端侧意图调用？

A：参考[Intents Kit接入流程](../harmonyos-guides/intents-access-flow.md)，各阶段指导文档对应的任务描述为：

* 意图注册：在DevEco Studio中开发时，注册对应的意图。
* 端侧意图共享：开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。
* 端侧意图调用：开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。

Q：意图框架调试，设备真机模式调试时出现无法切换到真机模式的问题。

A：意图框架调试开关再开关一次，中间需要等待半分钟间隔。

Q：如何实现和小艺说“使用银行转账”和“使用银行查询交易明细”，跳转到银行APP并拉起对应功能以及在小艺输入“转账”或者“查询交易明细”的时候，能在支持该服务的APP列表中展示银行APP？

A：接入“银行转账”场景可以参考意图框架金融理财垂域的[发起转账](../harmonyos-guides/insight-intent-access-specifications.md#发起转账)场景接入。“使用银行查询交易明细”场景可以参考同垂域的[查看账户变动](../harmonyos-guides/insight-intent-access-specifications.md#查看账户变动)场景接入。

Q：意图框架在应用和元服务中的接入哪个效率更好？分别适用于什么场景？

A：在应用和元服务中接入意图框架的流程是一致的，可以参考[接入方案](../harmonyos-guides/intents-habit-rec-access-programme.md)。意图响应方面由于元服务不存在应用启动，可以秒开直达，在使用效率上有显著的优势，适用于免安装场景应用则需要安装。但两者都具备完整的意图识别流程。

Q：意图框架公开测试完成后如何进行下一步操作，是否可以按照[意图标准协议上架指导](../harmonyos-guides/intents-kit-listing-standard-protocol.md)继续操作？

A：在意图标准协议上架前需要保证应用已经正式上架应用市场。所以需要先提交应用上架审核，审核通过正式上架后在进行下一步操作。

Q：个人开发者在AppGallery Connect平台的“开放能力管理”中搜索不到意图框架（Intents Kit）能力怎么办？

A：意图框架（Intents Kit）目前仅对企业开发者开放，个人开发者无法在AppGallery Connect的“开放能力管理”中搜索到该能力。建议使用企业账号参考[Intents Kit接入流程](../harmonyos-guides/intents-access-flow.md)申请接入。

## 总结

意图框架的接入流程操作步骤较多，但一般严格按照示范流程进行操作都可以正常接入意图框架，若接入过程中出现异常问题，可以重新审查接入流程操作，是否有遗漏操作或错误操作。
