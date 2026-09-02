---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataaugmentation-localchatmodel
title: 端侧问答模型
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > 端侧问答模型
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f7b6620d3cc8f0e56efbff62d285e64819c958382dc2256ed437408b92bd8aa8
---

## 概述

当应用通过RAG接口进行知识问答时，系统会经过以下处理流程：问题分解、查询改写、知识检索和检索生成，该流程需要与大语言模型（LLM）进行多次交互。应用可选择两种部署方案：

* 使用自建的云端大模型。
* 采用Kit提供的端侧问答模型能力。

选择端侧问答模型方案具有以下优势：

* 免除云端大模型的运维成本。
* 增强用户数据安全性（数据在端侧处理）。

## 约束与限制

1. 当前端侧模型问答仅支持PC/2in1设备类型。
2. 当前端侧模型问答仅对企业开发者提供申请能力。

## 接口说明

端侧问答模型关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/dataaugmentation-localchatmodel-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/dataaugmentation-localchatmodel-api.md#init)(): Promise<boolean> | 初始化端侧问答模型，负责拉起模型管理应用。 |
| [chat](../harmonyos-references/dataaugmentation-localchatmodel-api.md#chat)(info: [QuestionInfo](../harmonyos-references/dataaugmentation-localchatmodel-api.md#questioninfo), config: [Config](../harmonyos-references/dataaugmentation-localchatmodel-api.md#config), callback: AsyncCallback<[Answer](../harmonyos-references/dataaugmentation-localchatmodel-api.md#answer)>): Promise<void> | 与端侧模型进行交互，实现端侧模型的问答功能。 |

**须知** 

模型资源来自[Matrix](https://matrix.openharmony.cn/#/model/main)模型库，[chat](../harmonyos-references/dataaugmentation-localchatmodel-api.md#chat)接口默认调用模型为Qwen25-7B-Instruct。

## 开发步骤

### 申请权限

申请ohos.permission.INTERNET权限，配置方式请参阅声明权限[声明权限](declare-permissions.md)。

### 功能开发

1. 调用[init](../harmonyos-references/dataaugmentation-localchatmodel-api.md#init)接口，拉起本地AI模型管理。
2. 本地AI模型管理首次拉起，弹出隐私声明界面，同意后下载默认模型。
3. 本地AI模型管理非首次拉起，打开设置>系统>本地AI模型管理，下载默认模型。
4. 等待模型下载完成后，调用[chat](../harmonyos-references/dataaugmentation-localchatmodel-api.md#chat)接口，开始进行端侧问答。

## 示例代码

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { localChatModel } from '@kit.DataAugmentationKit'

type MessageType = 'tips' | 'request' | 'response';
interface ChatMessage {
  type: MessageType;
  content: string;
}

@Entry
@Component
struct Index {
  @State title: string = '端侧大模型问答助手';
  @State isStreamMode: boolean = true;
  @State messages: ChatMessage[] = [];
  @State inputText: string = '';
  @State initFlag: boolean = false;
  @State isProcessing: boolean = false;
  @State responseContent: string = '';
  @State chatCounter: number = 0;

  // 页面加载时，拉起模型管理应用
  onPageShow() {
    this.initModel();
  }

  private async initModel(): Promise<void> {
    try {
      this.initFlag = await localChatModel.init();
      // ...
    } catch (error) {
      this.initFlag = false;
      // ...
    }
  }

  private scroller: Scroller = new Scroller();
  // ...

  private async DoChat(questionId: number): Promise<void> {
    if (!this.inputText.trim() || this.isProcessing) {
      return;
    }
    const requestQuestion = this.inputText.trim();
    if (!requestQuestion) {
      return;
    }
    this.inputText = '';
    // ...
    this.responseContent = '思考中...';
    this.isProcessing = true;

    const questionInfo: localChatModel.QuestionInfo = {
      questionId: questionId,
      content: requestQuestion
    };

    const localConfig: localChatModel.Config = {
      isStream: this.isStreamMode
    };
    const localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
      // ...
      if (ans.content && ans.content.trim() !== '') {
        if (this.responseContent == '思考中...') {
          this.responseContent = '';
        }
        this.responseContent += ans.content;
        // ...
      }
      // ...

      if (ans.isFinished) {
        // ...
        this.isProcessing = false;
      }
    };

    try {
      localChatModel.chat(questionInfo, localConfig, localChatCallback);
    } catch (error) {
      // ...
      this.isProcessing = false;
    }
  }

  private clearChat(): void {
    this.messages = [];
  }

  build() {
    Stack({ alignContent: Alignment.Top }) {
      Column() {
        Row() {
          // ...
          Row() {
            Button(this.isStreamMode ? '流式' : '非流式')
              .height(28)
              .fontSize(16)
              .fontWeight(500)
              .backgroundColor('#0c000000')
              .fontColor('#0A59F7')
              .borderRadius(8)
              .onClick(() => {
                this.isStreamMode = !this.isStreamMode;
                // ...
              })
          }
          .margin({ right: 12 })
        }
        .width('100%')
        .height(56)
        .backgroundColor(Color.White)
        .borderRadius(8)
        .shadow({
          radius: 4,
          color: '#1a73e888',
          offsetX: 0,
          offsetY: 2
        })

        // 聊天区域
        Scroll(this.scroller) {
          Column() {
            ForEach(this.messages, (msg: ChatMessage, index: number) => {
              if (msg.type === 'tips') {
                Row() {
                  Text(msg.content)
                    .fontSize(14)
                    .fontColor('#666')
                    .textAlign(TextAlign.Center)
                    .padding(8)
                }
                .width('100%')
                .justifyContent(FlexAlign.Center)
                .margin({ top: index === 0 ? 0 : 12 })
              } else if (msg.type === 'request') {
                Row() {
                  Blank()
                  Text(msg.content)
                    .fontSize(16)
                    .fontColor(Color.White)
                    .padding(10)
                    .backgroundColor('#1a73e8')
                    .borderRadius(8)
                }
                .width('100%')
                .margin({ top: 12 })
                .justifyContent(FlexAlign.End)
              } else if (msg.type === 'response') {
                Row() {
                  Column() {
                    Text(msg.content)
                      .fontSize(16)
                      .fontColor('#333')
                      .lineHeight(20)
                      .padding(10)
                      .backgroundColor(Color.White)
                      .borderRadius(8)
                  }
                  .borderRadius(8)
                  .margin({ left: 8 })

                  Blank()
                }
                .width('100%')
                .margin({ top: 12 })
                .justifyContent(FlexAlign.Start)
              }
            }, (msg: ChatMessage) => msg.toString())

            // 加载指示器
            if (this.isProcessing) {
              Row() {
                Column() {
                  Text(this.responseContent)
                    .fontSize(16)
                    .fontColor('#333')
                    .lineHeight(20)
                    .padding(10)
                    .backgroundColor(Color.White)
                    .borderRadius(8)
                }
                .borderRadius(8)
                .margin({ left: 8 })

                Blank()
              }
              .width('100%')
              .margin({ top: 12 })
            }
          }
          .padding(12)
          .width('100%')
        }
        .width('100%')
        .layoutWeight(1)
        .margin({ bottom: 12 })

        // 输入区域
        Column() {
          Row() {
            TextInput({ text: this.inputText, placeholder: '请输入您的问题...' })
              .flexGrow(1)
              .height(42)
              .fontSize(16)
              .padding(8)
              .backgroundColor(Color.White)
              .borderRadius(8)
              .width('85%')
              .onChange((value: string) => {
                this.inputText = value;
              })
              .onSubmit(() => {
                if (!this.isProcessing && this.inputText.trim() !== '') {
                  const chatId = this.chatCounter++;
                  this.DoChat(chatId);
                }
              })

            Button('发送')
              .height(40)
              .fontSize(16)
              .fontWeight(500)
              .margin({ right: 12 })
              .backgroundColor('#0A59F7')
              .fontColor(Color.White)
              .borderRadius(8)
              .onClick(() => {
                if (!this.isProcessing && this.inputText.trim() !== '') {
                  const chatId = this.chatCounter++;
                  this.DoChat(chatId);
                }
              })
              .opacity(this.isProcessing || this.inputText.trim() === '' ? 0.4 : 1)

            Button('清空')
              .height(40)
              .fontSize(16)
              .fontWeight(500)
              .fontColor('#fff')
              .backgroundColor('#ea4335')
              .borderRadius(8)
              .onClick(() => {
                this.clearChat();
              })
          }
          .width('100%')
          .justifyContent(FlexAlign.SpaceBetween)
          .alignItems(VerticalAlign.Center)
        }
        .width('100%')
        .padding(8)
        .backgroundColor(Color.White)
        .borderRadius(8)
        .shadow({
          radius: 4,
          color: '#1a73e888',
          offsetX: 0,
          offsetY: 2
        })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#f0f5ff')
      .padding(20)
    }
    .width('100%')
    .height('100%')
  }
}
```
