---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-typical-scenario
title: 典型场景展示
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 典型场景展示
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:12+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a5fb333daba0cc8fc2c11cdb15839318bcf050d0a5e9585bd0bf7375cdd9f351
---

如下展示两种智能填充的典型场景。

## 实名购票场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

**说明** 

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/IBtvY2fAQs2tuIKH_Xs0Sw/zh-cn_image_0000002820406585.png?HW-CC-KV=V1&HW-CC-Date=20261119T014817Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DA777E37D566BA64756106BBDD608C4DACF6B46CB40AE9DAB3CF983A9CEF587)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/j9f87RjmRgKaDtaTCjPROw/zh-cn_image_0000002791726606.png?HW-CC-KV=V1&HW-CC-Date=20261119T014817Z&HW-CC-Expire=31536000000&HW-CC-Sign=6159D85E0FC67753BE0726A230C5C7E1BFC027EDDB404C9A45007E6DADB5183E)

## 填写收货地址场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

**说明** 

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/WS4Jv3_wSde5aD7oso6dgA/zh-cn_image_0000002791566634.png?HW-CC-KV=V1&HW-CC-Date=20261119T014817Z&HW-CC-Expire=31536000000&HW-CC-Sign=8265EAACDF173CF91291EF1728A2F051A534B33C6F6B7171F12522D2B1595D75)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bNO8MGPhTiKxEc0I5B7NJg/zh-cn_image_0000002820526587.png?HW-CC-KV=V1&HW-CC-Date=20261119T014817Z&HW-CC-Expire=31536000000&HW-CC-Sign=1519D8B556551B18D744AAD9477A56EFEE12B25380E12296BDC45BAD437B4BC3)

## 示例代码

```typescript
import { autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SmartFill {
  @State isClicked: boolean = false;

  build() {
// ...

      Column({ space: 5 }) {
        Row() {
          Text('昵称：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.NICKNAME).selectionMenuHidden(true)
        }

        Row() {
          Text('姓名：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
        }

        Row() {
          Text('手机号码：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PHONE_NUMBER).selectionMenuHidden(true)
        }

        Row() {
          Text('邮箱：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.EMAIL_ADDRESS).selectionMenuHidden(true)
        }

        Row() {
          Text('身份证号：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.ID_CARD_NUMBER).selectionMenuHidden(true)
        }

        Row() {
          Text('地址：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.FORMAT_ADDRESS).selectionMenuHidden(true)
        }

        Button('保存')
          .onClick(() => {
            if (!this.isClicked) {
              // 主动触发保存历史表单输入。
              try {
                autoFillManager.requestAutoSave(this.getUIContext());
              } catch (err) {
                let e: BusinessError = err as BusinessError;
                hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
              }
              this.isClicked = true;
              // 设置超时时间以防止重复点击按钮保存历史表单输入。
              setTimeout(() => {
                this.isClicked = false;
              }, 1000);
              // 或者通过路由跳转其他页面触发保存历史表单输入。
              this.getUIContext().getRouter().pushUrl({
                url: 'pages/xxxxxx'
              });
            }
          })
          .width('50%')
      }
      .alignItems(HorizontalAlign.Center)
      .height('100%')
      .width('100%')
// ...
  }
}
```

**说明** 

* 智能填充在页面发生跳转的时候，或者手动触发保存逻辑的时候，方可触发保存表单逻辑。
* 剪贴板文本内容识别功能现已实现超过90%的准确率。尽管如此，我们认识到在特定场景下仍可能出现识别误差。为了提升填表数据的准确性，我们建议在关键环节引入增强校验。这些校验措施包括但不限于：

  1. 格式校验：自动检测输入格式，确保数据符合预设标准。
  2. 确认提示：在提交前通过弹窗提示用户再次确认信息，避免输入错误。
* 若在页面中也提供了弹窗提醒填充建议的功能，为避免弹窗冲突，建议将对应输入组件的[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)属性设置为"false"以关闭智能填充功能。
