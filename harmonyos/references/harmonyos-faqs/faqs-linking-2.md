---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-linking-2
title: App Linking跳转问题
breadcrumb: FAQ > 应用服务开发 > 应用链接跳转服务（App Linking Kit） > App Linking跳转问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:9f06a23b6f4080e89f9ecd76082f92048d91ad4d5af7354ff1a1e31e8c844e2c
---

## 问题现象

开发者在AGC开通了App Linking服务，并且在域名服务器上配置了对应文件，AGC上面也显示发布成功，但是点击跳转失败，提示16000019，是什么原因呢？

## 背景知识

App Linking：为开发者提供了统一的链接跳转能力，可以基于社交平台、应用链接等形态，满足对用户的拉新、促活等场景，后续还将规划应用短链等能力，支持链接跳转逻辑可配置，提供更加灵活的链接跳转能力。

## 解决方案

[16000019](../harmonyos-references/errorcode-ability.md#section16000019-隐式启动未查找到匹配应用)是隐式拉起失败，可能的原因是隐式启动的参数配置有误或者指定的HAP包未安装。

排查方式：

1. 检查目标应用代码中的skills配置：
   * "entities"列表中必须包含"entity.system.browsable"；
   * "actions"列表中必须包含"ohos.want.action.viewData"；
   * "uris"列表中必须包含"scheme"为"https"且"host"为域名地址的元素，可选属性包含"path"、"pathStartWith"和"pathRegex"，具体请参见"[uris标签说明](../harmonyos-guides/app-uri-config.md#uris标签说明)"；
   * "domainVerify"设置为true，表示开启域名校验开关。
2. 检查应用中指定的目标应用HAP包是否安装成功。

## 常见FAQ

Q：HarmonyOS是否支持从短信链接跳转到指定App？

A:可以设置一个链接，点击此链接，就能拉起目标应用。然后把此链接放进短信中，即可实现从短信链接跳转App。此链接可以使用App Linking实现。设置链接具体操作步骤可参考[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)。

Q：已接入扫码直达服务，如何在应用的生命周期内获取到对应的码值信息？

A：参考官网接入扫码直达服务-[开发步骤](../doccenter-capabilities/scan-directservice.md#开发步骤)中的代码，根据不同的启动场景（冷启动/热启动）在onCreate/onNewWant中获取到对应的码值信息，并作出相应的处理。

Q：点击App Linking从短信链接跳转到指定App，为何页面是空白的？

A：配置直达应用市场能力，直达应用市场链接配置后不是即时生效的，一般要24小时生效，也有可能出现48小时生效的情况。

Q：拉起应用的Harmony相关参数应该如何填写？

A：在AGC上创建项目，并在项目中开通App Linking，创建应用链接，形成聚合链接，详情可参考[目标方应用配置应用链接能力](../harmonyos-guides/app-linking-startupapp.md#配置应用链接能力)和[目标方应用配置聚合链接能力](../harmonyos-guides/applinking-cross-platform.md#配置聚合链接能力)。

Q：使用App Linking链接拉起应用，但拿不到回调，怎么处理？

A：拉起应用，拿不到回调。非App Linking问题，登录回调是三方SDK的功能。

Q：App Linking无法设置scheme为HTTP跳转到应用？

A：App Linking明确规定链接的scheme必须为https。这种设计通过https加密传输保障了通信安全，同时结合域名校验机制，可防止恶意劫持和仿冒应用。

Q：应用没有上架，配置了App Linking，path配置的是/open，但发现如果从其他App内手动跳转，是可以唤起App，但是在浏览器内访问则无法唤起。

A：如果配置了path，就会精确匹配到这个path才能跳转；AG直达功能，需要在架版本包含App Linking功能才可生效；关于是否可以跳转到已安装的App上，需要看App是否已经配置了参数。

应用跳转链接不能在浏览器中直接输入，要跳转此应用，需要将App Linking的链接作为超链接数据，然后点击进行跳转，例如H5页面的a标签，或者将该链接复制进备忘录形成超链接形式。如果手机没有安装应用，想要跳转应用市场请参考[通过直达应用市场能力跳转至应用市场下载详情页](../harmonyos-guides/applinking-direct-to-ag.md)。

Q：通过附件中Form表单请求时，是否会触发App Linking的跳转机制？

A：通过普通表单（Form）的HTTP请求不会直接触发App Linking跳转机制。

App Linking的触发条件：App Linking需要特定的URI格式，且需通过openLink()接口或特定组件（如ArkWeb中的链接点击）主动调用才能触发跳转。表单的常规HTTP请求属于普通网络行为，无法直接激活App Linking机制。

Q：AGC后台已开通App Linking，但是配置完域名链接发布后状态是失败是报错信息为：下载源JSON文件失败，请确认源文件是否存在异常？

A：App Linking发布链接后平台状态显示失败，可以点击旁边的查看来获取到错误信息，遇到这种问题的可能原因：

1. 网络原因：域名下服务器网络问题导致下载JSON文件失败。
2. 网站链接安全性问题：如果网站证书不安全，也可能导致直接下载JSON文件失败（可以通过复制JSON配置链接后在浏览器中点击查看来确认是否可以直接查看），另外JSON文件中配置的AppID如果不在AGC配置的应用列表中，状态也会显示失败。

Q：系统读NFC标签是否可通过App Linking进行应用跳转？

A：NFC系统服务集成了App Linking能力。在NFC标签中写入配置好的URI（无需包含包名），即可实现安装即拉起应用，未安装则跳转应用市场的功能。

Q：应用安装情况下可以直接使用包名唤醒，但是在应用卸载时候想要使用链接唤醒应用详情失败。

A：跳转失败有可能在于没有正确配置path。

path：路径，表示域名服务器上的目录或文件路径，该字段在scheme存在时才有意义。path字段不支持通配符，如果需要使用通配符，可以采用pathRegex字段。

pathRegex：路径正则，该字段在scheme存在时才有意义，表示域名服务器上的目录或文件路径的正则表达式，用于正则匹配。

Q：放置文件applinking.json的作用是什么？每次调用scheme拉起App都需要访问该文件吗？

A：applinking.json文件放到域名服务器主要用于域名校验，表明该服务支持的应用才能打开，防止仿冒应用打开。在AGC发布的时候会访问一次applinking.json文件，后续缓存在AGC，手机都是访问的AGC，不会直接访问这个文件，AGC每隔24小时访问一次applinking.json文件。

Q：App Linking在配置path、pathStartWith、pathRegex时前后多加了/会有影响吗？

A：path、pathStartWith、pathRegex的取值前后均不需要加斜杠/，如果多加了/可能会影响匹配失败。

Q：在AGC创建元服务的App linking链接时报错：源JSON文件中未找到正确的AppID，请检查源JSON文件的配置是否准确？

A：报错是由于applinking.json配置文件中appIdentifier字段值错误或缺失导致，此字段必须与AGC控制台的应用标识符严格匹配，否则系统无法验证域名与应用的关系。元服务需参考[在开发者网站上关联元服务](../doccenter-atomic-service/atomic-applinking.md)配置正确的appIdentifier字段值。

Q：在AGC创建应用链接时错出现报错：源JSON文件中的index字段不符合要求，请检查配置是否准确？

A：报错是由于applinking.json文件中类型不对导致的，比如HarmonyOS应用在applinking.json文件中类型为atomicServices，或者元服务应用在applinking.json文件中类型为apps。需要改为对应的正确类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Fxbjma90RdqfIUcpNoKm1g/zh-cn_image_0000002719054371.png "点击放大")

Q：应用链接发布失败后，在域名服务器上重新完成了applinking.json配置文件放置，为何AGC显示的状态仍然是"失败"？

A：应用链接发布失败后，重新设置applinking.json配置文件，并不会自动去刷新配置状态，需要在AGC平台重新发布配置。

Q：App Linking配置pathRegex使用负向前瞻正则表达式后，点击链接无法拉起应用而是打开浏览器，如何解决？

A：系统不支持负向前瞻（如(?!...)）等高级正则操作符，使用后系统会跳过该路由规则，将链接直接重定向到浏览器。建议使用pathStartWith显式列出应用支持的路径前缀，系统会自动将未匹配的路径重定向到浏览器，无需通过正则排除。pathStartWith的配置方式请参考[uris标签说明](../harmonyos-guides/app-uri-config.md#uris标签说明)。

Q：配置App Linking直达应用市场能力后，未安装应用时未跳转到应用市场而是打开了域名服务器地址，如何解决？

A：在配置直达应用市场链接时，域名地址末尾需要加上斜杠"/"，例如https://www.example.com/。直达链接配置的是.\*，表示域名+斜杠+任意值，即使不需要匹配任意路径值，斜杠"/"也必须保留。具体配置方式请参考[通过直达应用市场能力跳转至应用市场下载详情页](../harmonyos-guides/applinking-direct-to-ag.md)。
