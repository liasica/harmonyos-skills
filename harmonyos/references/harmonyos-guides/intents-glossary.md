---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-glossary
title: Intents Kit术语
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > Intents Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f002e427e99ede49c111550421b917eff3caf7094db8ba8a3659abf005340426
---

## C

### Cloud-Side Intent；云侧意图

意图调用或意图共享的数据处理和响应发生在开发者云侧服务器的意图。

### Cloud-Side Intent Invocation；云侧意图调用

HarmonyOS理解用户意图后，请求开发者云侧服务器的信息或者数据，通过文本、卡片、语音播报等方式呈现给用户。

### Cloud-Side Intent Sharing；云侧意图共享

开发者将意图相关事件数据从服务端共享给Intents Kit，用于事件推荐服务。

## D

### Device-Side Intent；端侧意图

意图调用或意图共享的数据处理和响应发生在应用或元服务中的意图。

### Device-Side Intent Invocation；端侧意图调用

HarmonyOS在设备侧向开发者的应用/元服务发起的意图执行请求，由应用/元服务在本地处理并返回结果。

### Device-Side Intent Sharing；端侧意图共享

开发者将意图相关实体数据共享给Intents Kit，用于习惯推荐或内容搜索等服务。

## E

### Event-based Notification；事件推荐

事件发生变动且满足推荐规则时，会在小艺建议入口向指定用户推荐该事件的提醒卡片。

### Execution Mode；执行模式

意图的运行方式，包括前台执行（拉起应用界面）和后台执行（在应用进程内后台处理）两种模式。开发者需在意图配置文件中通过该字段声明。

### Event Revoking；事件撤销

删除数据超过时效期的事件，不再推送给用户。

## H

### Habit-based Recommendation；习惯推荐

根据用户的行为习惯且满足推荐规则时，会在小艺建议入口向该用户推荐与此习惯相关的服务卡片。

## I

### Intent；意图

开发者根据Intents Kit规范接入的业务功能，HarmonyOS会结合当前上下文在相应的时机进行意图的推荐和执行。比如开发者根据Intents Kit规范将转账功能声明为一个意图，当用户在小艺中明确表达了转账的诉求时，小艺则会拉起相关应用的转账页面，为用户提供转账服务。

### Intent Invocation；意图调用

根据输入的用户意图，执行开发者按照Intents Kit规范暴露出的业务功能，完成任务闭环。

### Intent Registration；意图注册

开发者在小艺开放平台上编辑并保存已实现的云侧意图或端侧意图，Intents Kit利用HarmonyOS的大模型、多维设备感知等AI能力将注册的意图进行智能分发。

### Intent Sharing；意图共享

开发者通过意图共享接口将意图数据捐赠给Intents Kit。Intents Kit根据捐赠的数据为用户提供便捷的功能直达体验。

## L

### Location-based Recommendation；位置推荐

根据用户的位置信息且满足推荐规则时，在小艺建议入口向该用户推荐与此位置相关的服务卡片。

## S

### Skill Invocation；技能调用

Intents Kit依托系统AI大模型能力做深度用户输入理解，并通过解析的用户意图对接应用或元服务内的功能和内容，最终实现任务闭环的特性。

### Smart Distribution；智慧分发

Intents Kit利用HarmonyOS的大模型、多维设备感知等AI能力，将开发者已实现的意图智能分发到小艺对话、小艺搜索、小艺建议等系统入口，完成相应的功能。

### SID；云侧事件捐赠凭证

第三方账号与华为账号的关联ID。Intents Kit通过该ID进行事件和用户的关联，用于将事件推送给指定用户。
