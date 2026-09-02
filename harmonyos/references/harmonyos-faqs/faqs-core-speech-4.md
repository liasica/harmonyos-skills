---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-4
title: 实时语音识别与音频文件识别的功能实现
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 实时语音识别与音频文件识别的功能实现
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:39+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:83e7870900776e8e67d9470dd00c19f45ce9189f101e8035281db530a769ecde
---

## 问题现象

开发者在开发语音识别功能时通常会有两种场景，实时语音识别与音频文件识别，这两种场景该如何实现？

## 背景知识

[语音识别](../harmonyos-guides/speechrecognizer-guide.md)可以在手机/平板等设备在无网状态下，为听障人士或不方便收听音频场景提供音频转文本能力。HarmonyOS侧提供了语音识别能力speechRecognizer，可以将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为pcm音频文件或者实时语音。

## 解决方案

语音识别的场景有两类：**实时语音识别**与**音频文件识别**，具体实现代码可参考官网[开发实例](../harmonyos-guides/speechrecognizer-guide.md#开发实例)。

**说明** 

音频文件识别目前只支持pcm音频文件，如使用的是非pcm格式，请参考[音频解码](../harmonyos-guides/audio-decoding.md)进行转换。

## 常见FAQ

Q：用户的语音识别数据最后是保存在华为的服务器上面了吗？

A：Core Speech Kit语音识别的数据是不会保存到华为服务器上的。Core Speech Kit语音识别是在用户手机上处理的，HarmonyOS侧不会保存处理结果到华为服务器的，即使没有网络也是可以使用该能力的。

Q：实时录音识别与实时音频识别，哪个识别速度更快？

A：实时录音识别和实时音频识别只是针对应用场景的不同采取不同的方案与识别速度、及时率无关。

Q：StartParams参数中的sessionId有什么作用？

A：sessionId是用于标识每个识别会话的独特标识符，它在startListening()方法中被用来关联特定的识别请求。通常sessionId应由开发者在调用startListening()时指定，并且在后续的事件处理中用于区分不同的识别会话。

Q：语音识别支持识别阿拉伯数字吗？

A：支持识别阿拉伯数字。

Q：语音识别会将音频上传到华为服务器吗？

A：不会，CreateEngineParams当前仅支持离线模式。

Q：HarmonyOS有离线语音识别吗？支持多语言吗？

A：语音识别支持的语种类型：中文普通话；支持的模型类型：离线。

Q：是否可以实现用户说出唤醒词，触发后拉起APP内的语音助手的能力？

A：可以基于系统Core Speech Kit实现在线流式识别，应用在前台开启录音，同时使用Core Speech Kit的[speechRecognizer（语音识别）](../harmonyos-references/hms-ai-speechrecognizer.md)在onResult校验结果，实现语音唤醒功能。
