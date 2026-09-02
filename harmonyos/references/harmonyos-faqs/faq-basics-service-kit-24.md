---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-24
title: 发送消息后，消息列表内容未刷新
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 发送消息后，消息列表内容未刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:41755ef2940868e86535122a5ad0d85cbd91632c9b9d5c64a852f52c8d5a0ebd
---

## 问题现象

点击进入聊天界面进行信息回复，发送后返回消息列表，最后一条消息显示的还是对方的信息，刚刚回复的信息没有刷新显示。

## 背景知识

* [List组件](../harmonyos-guides/arkts-layout-development-create-list.md)常被用于进行列表类功能开发，如消息列表、商品列表等。
* [Emitter](../harmonyos-guides/itc-with-emitter.md)是一种作用在进程内的事件处理机制，为应用程序提供订阅事件、发布事件、取消事件订阅的能力。可以用于实现线程间通信功能。

## 问题定位

1. 使用[DevEco Testing](../harmonyos-guides/get-familiar.md)中的实用工具>UIViewer工具，查看消息列表和聊天界面的布局，发现消息列表和聊天界面都是由List组件构成，每条消息都是通过[Text组件](../harmonyos-guides/arkts-common-components-text-display.md)进行展示。
2. 查看刚进入消息列表时以及点击发送后的日志：

   ```shell
   // 进入消息列表时
   07-28 15:34:28.318   28479-28479   A03D00/com.XXX/JSAPP  com.XXX     I     [7-28 15:34:28:318]: INFO: V2NIMConversationService: convFields [{"conversationId":"3615776|1|999","type":1,"serverExtension":"","groupIds":[],"lastMessage":{"lastMessageState":0,"messageRefer":{"conversationType":1,"conversationId":"3615776|1|999","senderId":"3615776","receiverId":"999","messageServerId":"15101753626977","createTime":1753686264116,"messageClientId":"e9b221687eaded97827d7da2463735a5"},"messageType":0,"text":"XXX","sendingState":1,"callbackExtension":"","senderName":""},"unreadCount":0,"stickTop":false,"sortOrder":1753686264116,"version":166268231681,"deleteFlag":false,"createTime":1753683886779,"updateTime":1753688060142}]
   07-28 15:34:28.352   28479-28479   A03D00/com.XXX/JSAPP  com.XXX     I     [7-28 15:34:28:352]: INFO: V2NIMConversationService: emit onConversationCreated, triggerConversationCreated, conversation: {"conversationId":"3615776|1|999","type":1,"stickTop":false,"groupIds":[],"localExtension":"","serverExtension":"","unreadCount":0,"createTime":1753683886779,"sortOrder":1753686264116,"updateTime":1753688060142,"isLocal":false,"lastMessage":{"lastMessageState":0,"messageRefer":{"conversationType":1,"conversationId":"3615776|1|999","senderId":"3615776","receiverId":"999","messageServerId":"15101753626977","createTime":1753686264116,"messageClientId":"e9b221687eaded97827d7da2463735a5"},"messageType":0,"text":"XXX","sendingState":1,"callbackExtension":"","senderName":""},"mute":false,"name":"999","avatar":""}
   ```

   ```shell
   // 发送消息后
   07-28 15:37:31.688   28479-28479   A03D00/com.XXXX/JSAPP  com.XXXX     I     [7-28 15:37:31:688]: INFO: V2NIMConversationService: on V2NIMConversationService/sendMessage, message: {"messageClientId":"185adabed80acd9ee3f03bafb5764022","createTime":1753688251668,"senderId":"3615776","receiverId":"999","conversationType":1,"conversationId":"3615776|1|999","isSelf":true,"sendingState":3,"messageType":0,"text":"XXXX","_antispamConfig":{"antispamEnabled":true},"_messageConfig":{"unreadEnabled":true,"roamingEnabled":true,"readReceiptEnabled":false,"historyEnabled":true,"onlineSyncEnabled":true,"offlineEnabled":true,"lastMessageUpdateEnabled":true},"_pushConfig":{"pushEnabled":true,"pushNickEnabled":true,"forcePush":false},"_routeConfig":{"routeEnabled":true},"resend":false}, sendingState: 3
   ```

   发现刚进入消息列表时会有一次刷新数据的请求，而点击发送后却只有传输消息的操作，没有再次请求刷新数据。
3. 排查代码，查看发送按钮的[onClick事件](../harmonyos-references/ts-universal-events-click.md)中是否有关通知刷新数据的操作。

## 分析结论

发送按钮的onClick事件回调内只进行了数据传输，没有请求数据刷新的操作，导致消息发送成功却未刷新消息列表显示的最后一条消息内容。

## 修改建议

在发送按钮的onClick事件回调中添加请求数据刷新的操作，使用Emitter通知消息列表刷新，确保每次发送都可以实时同步。

1. 导入线程通讯模块。

   ```ts
   import { emitter, Callback } from '@kit.BasicServicesKit';
   ```
2. 在消息接收页面实现数据的监听和展示。

   ```ts
   @Sendable
   class Sample {
     constructor(inputMessage: string) {
       this.count = inputMessage;
     }

     printCount(): string {
       return this.count;
     }

     count: string;
   }

   @Entry
   @Component
   struct ShowMessage {
     @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
     @State message: string | undefined = 'Hello!';
     event: emitter.InnerEvent = {
       // 定义一个eventId为1的事件。
       eventId: 1
     };
     // 定义一个事件的回调处理函数，当收到对应的事件后执行回调函数
     callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>) => {
       this.message = eventData.data?.count;
     };

     @Builder
     pageMap(name: string) {
       if (name === "NavDestinationTitle1") {
         SendMessage();
       }
     }

     aboutToAppear(): void {
       // 收到eventId为1的事件后执行回调函数
       emitter.on(this.event, this.callback);
     }

     build() {
       Column() {
         Navigation(this.pageInfos) {
           Column({ space: 20 }) {
             Text(this.message) // 展示最后一条消息

             Button('跳转')
               .onClick(() => {
                 this.pageInfos.pushPath({ name: 'NavDestinationTitle1' }); // 点击跳转聊天界面
               })
           }
           .width('100%')
           .height('100%')
           .justifyContent(FlexAlign.Center)
         }
         .navDestination(this.pageMap)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
3. 在消息发送页面中实现数据的变更并通知消息接收页面更新展示。

   ```ts
   @Component
   export struct SendMessage {
     @Consume('pageInfos') pageInfos: NavPathStack;
     @State inputMessage: string = '';
     event: emitter.InnerEvent = {
       eventId: 1
     };

     build() {
       NavDestination() {
         Column({ space: 20 }) {
           TextInput()
             .width('90%')
             .onChange((value: string) => {
               this.inputMessage = value; // 记录输入框的信息
             })

           Button('发送')
             .onClick(() => {
               let eventData: emitter.GenericEventData<Sample> = {
                 data: new Sample(this.inputMessage)
               };
               emitter.emit(this.event, eventData); // 点击发送后刷新最后一条数据
             })
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Center)
       }
       .hideBackButton(true)
       .onBackPressed(() => {
         this.pageInfos.pop(); // 弹出路由栈栈顶元素
         return true;
       })
     }
   }
   ```
