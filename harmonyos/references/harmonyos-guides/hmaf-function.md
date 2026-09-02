---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-function
title: 通过Function组件拉起智能体
breadcrumb: 指南 > AI > Agent Framework Kit（智能体框架服务） > 通过Function组件拉起智能体
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:34+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:f36110e659f71332a434484cc9cbc5f9f689391f69562df232b9041f0404dac3
---

## 场景介绍

* Function组件分为图标组件和按钮组件，无标题时默认显示图标组件，有标题时默认显示按钮组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nMffW_D1TkCGVHH8eI3tbA/zh-cn_image_0000002736434421.png)
* Function图标组件效果：综合型入口。不带用户意图，可作为应用内智能体主入口。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/vPD68AELT_m205h-NfCXcA/zh-cn_image_0000002706835274.png)
* Function按钮组件：允许应用自定义功能描述的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/x6F0m2ODRsaznMxi85-pdQ/zh-cn_image_0000002736314379.png)

## 开发前准备

* 开发智能体，具体请参见[开发Agent](../service/developing-intelligent-agents-0000002435989592.md)。
* 关联应用，具体请参见[关联应用](../service/related-applications-0000002437785706.md)。
* 确保已在终端设备上登录华为账号，并且处于联网状态。

## 开发步骤

1. 从项目根目录进入/src/main/ets/pages/Index.ets文件，将FunctionComponent及相关其它类引入到工程。

   ```typescript
   import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. （可选）可以在组件加载前通过[isAgentSupport](../harmonyos-references/hmaf-function-component.md#isagentsupport)来判断当前的agentId是否可用，若agentId有效且Agent功能支持时再加载组件。

   ```typescript
     @State isAgentSupport: boolean = false;
     
     aboutToAppear() {
        this.checkAgentSupport()
     }
     async checkAgentSupport() {
       try {
         let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
         this.isAgentSupport = await this.controller.isAgentSupport(context, this.agentId)
       } catch (err) {
         hilog.error(0x0001, 'AgentExample', `err code: ${err.code}, message: ${err.message}`)
       }
     }

     build() {
       Column() {
         if (this.isAgentSupport) {
           FunctionComponent({
             agentId: this.agentId,
             onError: (err: BusinessError) => {
               hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
             },
             options: {
                 title: '智能创建',
                 queryText: '创建一个新的模式'
             }
           })
         }
       }
     }
   ```
3. 构建一个简单配置的页面，在页面中引入FunctionComponent组件，并传入对应的参数。其中agentId、onError是必填参数。其他可选参数可参见[FunctionComponent（功能组件）](../harmonyos-references/hmaf-function-component.md)。Function组件布局可参考[组件布局](arkts-layout-development.md)。

   ```typescript
   @Entry
   @Component
   export struct AgentExample {
     private controller: FunctionController = new FunctionController();
     private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentId，由小艺智能体平台在创建智能体时指定
     build() {
       Column() {
         FunctionComponent({
           agentId: this.agentId,
           onError: (err: BusinessError) => {
             hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
           },
           options: {
             title: '',
             queryText: ''
           },
           controller: this.controller
         })
       }
     }
   }
   ```
4. 添加订阅事件。

   ```typescript
     aboutToAppear() {
        this.initListeners();
     }
     initListeners() {
       this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback);
       this.controller?.on('agentDialogClosed', this.onAgentClosedCallback);
     }
     onAgentOpenedCallback = () => {
       hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback');
     };
     onAgentClosedCallback = () => {
       hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback');
     };
     aboutToDisappear() {
       this.controller?.off('agentDialogOpened');
       this.controller?.off('agentDialogClosed');
     }
     
     build() {
       Column() {
         FunctionComponent({
           agentId: this.agentId,
           onError: (err: BusinessError) => {
             hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
           },
           controller: this.controller
         })
       }
     }
   ```

## 开发实例

点击按钮，打开智能体对话框。

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

import {
  FunctionComponent,
  FunctionController
} from '@kit.AgentFrameworkKit';

@Entry
@Component
export struct AgentExample {
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.initListeners();
  }
  initListeners() {
    this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback);
    this.controller?.on('agentDialogClosed', this.onAgentClosedCallback);
  }
  onAgentOpenedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback');
  };
  onAgentClosedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback');
  };
  aboutToDisappear() {
    this.controller?.off('agentDialogOpened');
    this.controller?.off('agentDialogClosed');
  }
  
  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
        },
        options: {
          title: '智能创建',
          queryText: '创建一个新的情景',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}
```
